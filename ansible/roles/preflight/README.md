# 🛫 Preflight Role

This Ansible role performs pre-deployment checks to ensure that all required configuration values and infrastructure prerequisites are present and valid before continuing with the OpenCMMC Stack deployment.

## ✅ Features

- Validates required variables are defined
- Ensures SSH public key format is correct
- Checks email formatting using regex
- Verifies DNS resolution for target domain
- Logs all validation steps to the `evidence/99_preflight/` directory

## 📂 Evidence Artifacts

Validation checks are written to:

```
evidence/
└── 99_preflight/
    └── validation_checks.md
```

## 🔍 Tags

Use with:
```bash
ansible-playbook site.yml --tags preflight
```

## 🔧 Variables Checked

- `default_user`
- `ssh_authorized_key`
- `domain_name`
- `hostname`
- `mailcow_admin_user`
- `mailcow_admin_password`
- `mailcow_fqdn`
- `mailcow_letsencrypt_email`
