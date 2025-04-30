# 🔐 Ansible Role: secure_ubuntu

Harden an Ubuntu 22.04 LTS host to meet **CMMC Level 2** compliance requirements using a modular, auditable Ansible role.

This role configures:
- SSH and login security
- Non-root administrative user
- System auditing and file integrity monitoring
- UFW firewall
- Secure banners for compliance
- Automatic updates and password policies

## ✅ CMMC Practices Addressed

| Domain | Practice      | Description                                             |
|--------|---------------|---------------------------------------------------------|
| AC     | AC.1.001      | Limit system access to authorized users                |
| AC     | AC.3.017      | Display system use notifications (login banner)        |
| CM     | CM.2.062      | Employ security configuration baseline                 |
| SI     | SI.1.210      | Identify unauthorized use of systems                   |
| SI     | SI.3.219      | Detect and report unauthorized changes to software     |

## 📦 Requirements

- Ubuntu 22.04 LTS
- Ansible >= 2.11

## 🚀 Role Variables

```yaml
secure_user: cmmcadmin
ssh_pubkey_path: "~/.ssh/id_rsa.pub"
```

> Set `ssh_pubkey_path` to the local path of the public key to be authorized for `secure_user`.

## 📁 Example Playbook

```yaml
- name: Apply CMMC hardening baseline
  hosts: all
  become: yes
  roles:
    - role: secure_ubuntu
      vars:
        secure_user: cmmcadmin
        ssh_pubkey_path: "~/.ssh/id_rsa.pub"
```

## 📁 File Structure

```
roles/
└── secure_ubuntu/
    ├── defaults/
    │   └── main.yml
    ├── meta/
    │   └── main.yml
    ├── tasks/
    │   ├── main.yml
    │   ├── ssh.yml
    │   ├── user.yml
    │   ├── firewall.yml
    │   ├── audit_aide.yml
    │   ├── banner.yml
    │   ├── updates.yml
    │   └── password_policy.yml
    └── README.md
```

## 🔒 License

MIT License

## 🧠 Author

Maintained by **Kell Engineering**  
https://github.com/mtkell/open-cmmc-stack
