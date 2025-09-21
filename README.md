# Run-as-Administrator

Run as Administrator

## Dependabot Auto Generation Workflow

This repository includes a GitHub Actions workflow that Dependabot can trigger to
repeatedly generate example Java, Maven, Docker, and Red Hat container assets.
The workflow lives in [`.github/workflows/dependabot-autogen.yml`](.github/workflows/dependabot-autogen.yml)
and calls [`scripts/dependabot-autogen.sh`](scripts/dependabot-autogen.sh) to
produce reproducible templates that are published as workflow artifacts.
