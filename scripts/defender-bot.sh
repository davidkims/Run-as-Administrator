#!/usr/bin/env bash
# Defender bot setup script to download dependencies via optional proxy.
set -euo pipefail

PROXY=""
DRY_RUN=0

usage() {
  cat <<USAGE
Usage: $0 [--proxy PROXY_URL] [--dry-run]

Options:
  --proxy PROXY_URL  Use the specified proxy for all downloads.
  --dry-run          Print commands without downloading files.
USAGE
}

while [ $# -gt 0 ]; do
  case "$1" in
    --proxy)
      PROXY="$2"; shift 2;;
    --dry-run)
      DRY_RUN=1; shift;;
    -h|--help)
      usage; exit 0;;
    *)
      echo "Unknown option: $1" >&2; usage; exit 1;;
  esac
done

# Generic download function using curl.
download() {
  local url="$1";
  local dest="$2";
  if [ "$DRY_RUN" -eq 1 ]; then
    echo "[DRY-RUN] Would download $url to $dest";
    return;
  fi
  if [ -n "$PROXY" ]; then
    echo "Downloading $url via proxy $PROXY";
    curl -fL -x "$PROXY" -o "$dest" "$url";
  else
    echo "Downloading $url";
    curl -fL -o "$dest" "$url";
  fi
}

# Download URLs for required tools.
MAVEN_URL="https://archive.apache.org/dist/maven/maven-3/3.9.6/binaries/apache-maven-3.9.6-bin.zip"
DOCKER_URL="https://download.docker.com/linux/static/stable/x86_64/docker-24.0.5.tgz"
JDK_URL="https://download.oracle.com/java/21/latest/jdk-21_linux-x64_bin.tar.gz"
SPRING_URL="https://repo.spring.io/release/org/springframework/boot/spring-boot-cli/3.2.2/spring-boot-cli-3.2.2-bin.tar.gz"

mkdir -p downloads
cd downloads

download "$MAVEN_URL" maven.zip
download "$DOCKER_URL" docker.tgz
download "$JDK_URL" jdk.tar.gz
download "$SPRING_URL" spring-boot-cli.tgz

echo "Downloads complete: $(ls)"
