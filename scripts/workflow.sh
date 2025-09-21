#!/usr/bin/env bash
set -e

install_docker() {
  if ! command -v docker >/dev/null 2>&1; then
    echo "Installing Docker..."
    curl -fsSL https://get.docker.com -o get-docker.sh
    sh get-docker.sh
  else
    echo "Docker already installed. Upgrading..."
    sudo apt-get update -y
    sudo apt-get install -y docker-ce docker-ce-cli containerd.io || true
  fi
}

build_image() {
  docker build -f docker/Dockerfile -t finance-image .
}

run_container() {
  docker run --rm finance-image
}

install_teradata() {
  bash teradata/install_teradata.sh
}

create_financial_table() {
  echo "Applying financial table schema..."
  # Placeholder for running SQL inside Teradata
}

simulate_transactions() {
  python scripts/simulate_transactions.py
}

create_accounts() {
  python scripts/create_virtual_accounts.py
}

case "$1" in
  docker)
    install_docker
    ;;
  build)
    build_image
    ;;
  run)
    run_container
    ;;
  teradata)
    install_teradata
    create_financial_table
    ;;
  simulate)
    create_accounts
    simulate_transactions
    ;;
  *)
    echo "Usage: $0 {docker|build|run|teradata|simulate}"
    ;;
esac
