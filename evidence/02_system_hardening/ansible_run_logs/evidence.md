# 📋 Evidence – Ansible Execution Logs

## Description
This directory contains raw output of Ansible playbooks applied to the Ubuntu host.

## Artifacts
- `secure_ubuntu_run.log`
- `ansible-playbook-timestamped.json`
- Output showing configuration and user enforcement

## Reviewer Notes
Ensure playbook includes:
- SSH key enforcement
- Root login disabled
- Required auditd and aide tasks completed
