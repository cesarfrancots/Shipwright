#!/usr/bin/env bash
set -euo pipefail

# Usage: ./install.sh [--skills name1,name2] [--uninstall]

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="${SCRIPT_DIR}/skills"
UNINSTALL=0
SKILL_FILTER=""

usage() {
  cat <<'EOF'
Usage: ./install.sh [--skills name1,name2] [--uninstall]

Options:
  --skills     Install or uninstall only a comma-separated subset of skills
  --uninstall  Remove symlinks instead of creating them
  -h, --help   Show this help text
EOF
}

log() {
  printf '%s\n' "$*"
}

has_command() {
  command -v "$1" >/dev/null 2>&1
}

normalize_skills() {
  if [[ -z "${SKILL_FILTER}" ]]; then
    find "${SKILLS_DIR}" -mindepth 1 -maxdepth 1 -type d -exec basename {} \; | sort
  else
    printf '%s' "${SKILL_FILTER}" | tr ',' '\n' | sed '/^$/d' | sort -u
  fi
}

ensure_dir() {
  mkdir -p "$1"
}

remove_target() {
  local target="$1"
  if [[ -L "${target}" || -e "${target}" ]]; then
    rm -rf "${target}"
  fi
}

link_skill() {
  local source="$1"
  local target="$2"

  if [[ -L "${target}" ]]; then
    local current
    current="$(readlink "${target}")"
    if [[ "${current}" == "${source}" ]]; then
      log "unchanged ${target}"
      return
    fi
  fi

  remove_target "${target}"
  ln -s "${source}" "${target}"
  log "linked ${target} -> ${source}"
}

detect_platform_targets() {
  local repo_root="$1"
  local results=()

  if has_command claude; then
    results+=("${HOME}/.claude/skills")
  fi

  if has_command codex; then
    results+=("${HOME}/.codex/skills")
  fi

  if has_command copilot; then
    results+=("${repo_root}/.github/skills")
  fi

  printf '%s\n' "${results[@]}"
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --skills)
      shift
      [[ $# -gt 0 ]] || { log "missing value for --skills"; exit 1; }
      SKILL_FILTER="$1"
      ;;
    --uninstall)
      UNINSTALL=1
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      log "unknown argument: $1"
      usage
      exit 1
      ;;
  esac
  shift
done

mapfile -t SELECTED_SKILLS < <(normalize_skills)

if [[ "${#SELECTED_SKILLS[@]}" -eq 0 ]]; then
  log "no skills selected"
  exit 1
fi

mapfile -t TARGET_DIRS < <(detect_platform_targets "${SCRIPT_DIR}")

if [[ "${#TARGET_DIRS[@]}" -eq 0 ]]; then
  log "no supported platforms detected"
  log "detected platforms depend on available binaries: claude, codex, copilot"
  exit 1
fi

for skill in "${SELECTED_SKILLS[@]}"; do
  if [[ ! -d "${SKILLS_DIR}/${skill}" ]]; then
    log "skill not found: ${skill}"
    exit 1
  fi
done

log "pm-pilot installer"
log "mode: $([[ ${UNINSTALL} -eq 1 ]] && printf 'uninstall' || printf 'install')"
log "skills: ${SELECTED_SKILLS[*]}"

for target_dir in "${TARGET_DIRS[@]}"; do
  ensure_dir "${target_dir}"
  for skill in "${SELECTED_SKILLS[@]}"; do
    source_path="${SKILLS_DIR}/${skill}"
    target_path="${target_dir}/${skill}"
    if [[ ${UNINSTALL} -eq 1 ]]; then
      if [[ -L "${target_path}" || -e "${target_path}" ]]; then
        remove_target "${target_path}"
        log "removed ${target_path}"
      else
        log "missing ${target_path}"
      fi
    else
      link_skill "${source_path}" "${target_path}"
    fi
  done
done

log "summary"
for target_dir in "${TARGET_DIRS[@]}"; do
  log "- ${target_dir}"
done
