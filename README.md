# Run-as-Administrator

## Financial Workflow

This repository provides a simple workflow for financial statement simulation.
Scripts allow you to:

- Install or upgrade Docker.
- Build a Docker image that generates a sample financial statement image.
- Run the container to produce `financial_statement.png`.
- Install Teradata and apply a financial statement table schema (placeholders).
- Generate virtual accounts and simulate deposit/withdrawal transactions.

Run `./scripts/workflow.sh` with one of the following commands:

- `docker` – install or upgrade Docker.
- `build` – build the financial image.
- `run` – run the container.
- `teradata` – install Teradata and apply the table schema.
- `simulate` – create accounts and simulate transactions.
