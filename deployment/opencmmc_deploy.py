#!/usr/bin/env python3
import os
import yaml
import subprocess

CONFIG_PATH = "deployment/deployment_config.yml"

def prompt_input(prompt, default=None, required=True):
    while True:
        val = input(f"{prompt}{' [' + default + ']' if default else ''}: ").strip()
        if val:
            return val
        elif default is not None:
            return default
        elif not required:
            return ''
        else:
            print("This field is required.")

def write_config(config, path=CONFIG_PATH):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        yaml.dump(config, f)
    print(f"\n✅ Config written to {path}")

def run_terraform():
    print("\n🚀 Running Terraform provisioning...\n")
    subprocess.run(["terraform", "init"], cwd="terraform")
    subprocess.run(["terraform", "apply", "-auto-approve"], cwd="terraform")

def run_ansible():
    print("\n🔧 Running Ansible deployment...\n")
    subprocess.run([
        "ansible-playbook", "-i", "inventory/terraform_inventory.yml", "site.yml"
    ])

def main():
    print("🛡️ OpenCMMC Stack: Guided Deployment")
    config = {
        "cloud_provider": prompt_input("Cloud Provider (aws, azure, gcp, do, proxmox, bare-metal)"),
        "fqdn": prompt_input("Root Fully Qualified Domain Name (e.g., open-cmmc.example.com)"),
        "domain_name": prompt_input("Internal Domain Name (e.g., example.cmmc.local)"),
        "admin_email": prompt_input("Administrator email (for certs and contact)"),
        "admin_user": prompt_input("Admin system username", default="cmmcadmin"),
        "ssh_pubkey_path": prompt_input("Path to SSH public key", default="~/.ssh/id_rsa.pub"),
        "keycloak_realm": prompt_input("Keycloak Realm", default="OpenCMMC"),
        "tailscale_key": prompt_input("Tailscale Auth Key", required=False),
    }

    write_config(config)

    if prompt_input("Proceed with Terraform provisioning?", default="y").lower() == "y":
        run_terraform()

    if prompt_input("Proceed with Ansible deployment?", default="y").lower() == "y":
        run_ansible()

if __name__ == "__main__":
    main()
