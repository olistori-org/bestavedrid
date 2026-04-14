# Deployment

## Overview

The system is deployed to a Hetzner VPS using:
- **Terraform** — provisions the server, firewall, and SSH keys
- **Ansible** — configures the server and deploys the application
- **Docker Compose** — runs the application containers
- **GitHub Actions** — automates CI and deployment on push to `main`

## Prerequisites

- Terraform >= 1.5.0
- Ansible >= 2.15
- Hetzner Cloud account and API token
- SSH key registered in Hetzner Cloud

## 1. Provision Infrastructure with Terraform

```bash
cd infra/terraform/environments/prod
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars with your actual values
terraform init
terraform plan
terraform apply
```

Note the output `server_ip` — you will need it for the Ansible inventory.

## 2. Update Ansible Inventory

Edit `ansible/inventories/prod/hosts.ini` and replace `YOUR_SERVER_IP` with the actual IP from Terraform output.

## 3. Configure Server with Ansible

```bash
cd ansible
ansible-galaxy collection install -r requirements.yml
ansible-playbook playbooks/bootstrap-server.yml -i inventories/prod/hosts.ini
```

## 4. Deploy Application

```bash
ansible-playbook playbooks/deploy-app.yml -i inventories/prod/hosts.ini
```

## Automated Deployment via GitHub Actions

Deployment runs automatically on push to `main` via `.github/workflows/deploy.yml`.

The workflows are configured to run on your self-hosted runner with these labels:
- `self-hosted`
- `Linux`
- `X64`

This matches your VPS runner setup and keeps CI, ansible-lint, and deployment on the same machine class.

Required GitHub Secrets:

| Secret | Description |
|---|---|
| `HCLOUD_TOKEN` | Hetzner Cloud API token |

Because deployment now runs on the self-hosted runner installed directly on the VPS, SSH deployment secrets are no longer required for the standard deploy workflow.

## Environment Variables

Copy `.env.example` to `.env` and fill in the required values before deployment:

```bash
cp .env.example .env
```

Secrets such as database passwords and API keys should be stored in GitHub Secrets and injected at runtime — never committed to the repository.
