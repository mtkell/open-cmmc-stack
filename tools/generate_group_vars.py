#!/usr/bin/env python3
"""
generate_group_vars.py – Converts deployment_config.yml into Ansible group_vars/all.yml
Author: OpenCMMC Stack Automation
"""

import yaml
from pathlib import Path
import sys

CONFIG_FILE = "deployment_config.yml"
OUTPUT_FILE = "group_vars/all.yml"

REQUIRED_FIELDS = [
    "global_admin_username", "admin_ssh_public_key", "domain_name",
    "hostname", "nextcloud_port", "mailcow_port", "keycloak_port",
    "keycloak_image", "nextcloud_aio_image", "mailcow_image"
]

def load_config():
    if not Path(CONFIG_FILE).exists():
        sys.exit(f"[!] {CONFIG_FILE} not found.")
    with open(CONFIG_FILE, "r") as f:
        return yaml.safe_load(f)

def validate_config(cfg):
    missing = [key for key in REQUIRED_FIELDS if key not in cfg]
    if missing:
        sys.exit(f"[!] Missing required keys in {CONFIG_FILE}: {', '.join(missing)}")

def build_output(cfg):
    return {
        # Global User
        "default_user": cfg["global_admin_username"],
        "default_shell": "/bin/bash",
        "ssh_authorized_key": cfg["admin_ssh_public_key"],

        # System Info
        "domain_name": cfg["domain_name"],
        "hostname": cfg["hostname"],
        "timezone": cfg.get("timezone", "UTC"),
        "dns_resolver_ip": cfg.get("dns_resolver_ip", "1.1.1.1"),

        # Network Ports
        "nextcloud_port": cfg["nextcloud_port"],
        "mailcow_port": cfg["mailcow_port"],
        "keycloak_port": cfg["keycloak_port"],
        "stepca_port": cfg.get("stepca_port", 9000),
        "wazuh_port": cfg.get("wazuh_port", 55000),

        # Container Images
        "nextcloud_aio_image": cfg["nextcloud_aio_image"],
        "keycloak_image": cfg["keycloak_image"],
        "mailcow_image": cfg["mailcow_image"],

        # Paths
        "nextcloud_data_dir": cfg.get("nextcloud_data_dir", "/srv/nextcloud"),
        "mailcow_data_dir": cfg.get("mailcow_data_dir", "/opt/mailcow"),
        "backup_base_dir": cfg.get("backup_base_dir", "/srv/backups"),
        "logs_dir": cfg.get("logs_dir", "/var/log/open-cmmc"),

        # System Accounts
        "svc_keycloak": cfg.get("svc_keycloak", "svc_keycloak"),
        "svc_mailcow": cfg.get("svc_mailcow", "svc_mailcow"),
        "svc_wazuh": cfg.get("svc_wazuh", "svc_wazuh"),
        "svc_stepca": cfg.get("svc_stepca", "svc_stepca"),

        # Backup
        "restic_password": cfg.get("restic_password", "changeme-securely"),
        "restic_repo": cfg.get("restic_repo", "/srv/backups/restic-repo"),

        # Mailcow
        "mailcow_hostname": cfg.get("mailcow_hostname", "mail"),
        "mailcow_fqdn": f"{cfg.get('mailcow_hostname', 'mail')}.{cfg['domain_name']}",
        "mailcow_admin_user": cfg.get("mailcow_admin_user", "admin"),
        "mailcow_admin_password": cfg.get("mailcow_admin_password", "changeme"),
        "mailcow_letsencrypt_email": cfg.get("mailcow_letsencrypt_email", "admin@localhost"),
        "mailcow_use_letsencrypt": cfg.get("mailcow_use_letsencrypt", "n"),

        # SSO & VPN
        "tailscale_auth_key": cfg.get("tailscale_auth_key", ""),
        "keycloak_realm": cfg.get("keycloak_realm", "OpenCMMC"),
        "keycloak_admin_user": cfg.get("keycloak_admin_user", "admin"),
        "keycloak_admin_password": cfg.get("keycloak_admin_password", "changeme"),
    }

def main():
    config = load_config()
    validate_config(config)
    output = build_output(config)

    Path("group_vars").mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        yaml.dump(output, f, sort_keys=False, default_flow_style=False)

    print(f"[✓] {OUTPUT_FILE} generated successfully from {CONFIG_FILE}")

if __name__ == "__main__":
    main()
