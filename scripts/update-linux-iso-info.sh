#!/usr/bin/env bash
set -euo pipefail

OUTPUT_FILE="linux-iso-info.txt"

LATEST_VERSION=$(curl -s https://releases.ubuntu.com/ | grep -Eo '[0-9]+\.[0-9]+(\.[0-9]+)?/' | sort -V | tail -n1 | tr -d '/')
ISO_NAME=$(curl -s https://releases.ubuntu.com/${LATEST_VERSION}/ | grep -Eo 'ubuntu-[0-9.]+-desktop-amd64.iso' | head -n1)
ISO_URL="https://releases.ubuntu.com/${LATEST_VERSION}/${ISO_NAME}"

{
  echo "Latest Ubuntu Version: ${LATEST_VERSION}"
  echo "ISO File: ${ISO_NAME}"
  echo "Download URL: ${ISO_URL}"
  echo "Last Checked: $(date -u)"
} > "${OUTPUT_FILE}"

