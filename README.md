# Run-as-Administrator


Run as Administrator

## Dependabot Auto Generation Workflow

This repository includes a GitHub Actions workflow that Dependabot can trigger to
repeatedly generate example Java, Maven, Docker, and Red Hat container assets.
The workflow lives in [`.github/workflows/dependabot-autogen.yml`](.github/workflows/dependabot-autogen.yml)
and calls [`scripts/dependabot-autogen.sh`](scripts/dependabot-autogen.sh) to
produce reproducible templates that are published as workflow artifacts.
=======

Utility scripts and examples.

## AWS Access Key Management

`defenderbot_key_manager.py` provides a small command line interface for
listing, creating and deleting AWS IAM access keys for a given user.  When
creating a key, the script can optionally store the credentials in AWS
Secrets Manager.

### Usage

```
python defenderbot_key_manager.py list --user exampleUser
python defenderbot_key_manager.py create --user exampleUser --secret-name my/secret
python defenderbot_key_manager.py delete --user exampleUser --access-key-id AKIA...

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

Run as Administrator

## Defender Bot Workflow

This repository contains a script and GitHub Actions workflow to download Maven, Docker, Java (JDK), and Spring Boot CLI using an optional proxy server. The script targets Linux environments.

### Local Usage

Run the setup script and provide a proxy if needed:

```bash
bash scripts/defender-bot.sh --proxy http://proxy.example.com:8080
```

To preview the commands without downloading files, use dry-run mode:

```bash
bash scripts/defender-bot.sh --dry-run
```

### GitHub Actions

The workflow at `.github/workflows/defender-bot.yml` executes the script and reads the proxy URL from the `PROXY_URL` secret.
