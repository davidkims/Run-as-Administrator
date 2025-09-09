# Run-as-Administrator

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
