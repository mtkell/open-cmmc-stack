# 🛠️ OpenCMMC Stack Tools

This directory contains helper scripts to streamline and automate deployment configurations.

## Files

- `generate_group_vars.py`: Converts the master `deployment_config.yml` into the Ansible `group_vars/all.yml`.

## Usage

```bash
python3 tools/generate_group_vars.py
```

Ensure `deployment_config.yml` is located in the project root.

### Prerequisites

- Python 3.x
- PyYAML (`pip install pyyaml`)
