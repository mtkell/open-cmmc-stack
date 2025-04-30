# Podman Services Role

This Ansible role provisions and manages containerized infrastructure components (excluding Nextcloud AIO) using **Podman**. It includes configurations for Wazuh, Mailcow, Redis, and more.

## Variables

```yaml
podman_services:
  - name: redis
    image: redis:7
    state: started
    restart_policy: always
    ports: []
    volumes: []
    env: {}
```

## Usage

Include in your playbook:

```yaml
- hosts: all
  roles:
    - role: podman_services
```

## Notes

- Only non-root Podman containers are supported
- Customize via `podman_services` variable in `defaults/main.yml`
