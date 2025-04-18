# file_storage Role

This Ansible role deploys **Nextcloud All-in-One (AIO)** as the secure file sharing and collaboration solution in the OpenCMMC Stack.

## Features

- Pulls and runs the official `nextcloud/all-in-one` container image
- Sets up a persistent storage directory for CUI/FCI content
- Configures container restart and port mapping for access via reverse proxy

## Variables

| Variable              | Description                                | Default                     |
|-----------------------|--------------------------------------------|-----------------------------|
| `nextcloud_aio_image` | Container image for Nextcloud AIO          | `nextcloud/all-in-one:latest` |
| `nextcloud_data_dir`  | Host volume path for Nextcloud data        | `/mnt/ncdata`              |
| `nextcloud_port`      | Port exposed on the host                   | `8080`                     |

## Example Playbook

```yaml
- hosts: all
  roles:
    - role: file_storage
```

## Notes

- Make sure this container is **behind a reverse proxy** (e.g., NGINX or Caddy).
- Configure DNS and TLS externally as needed.
