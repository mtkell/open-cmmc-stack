#!/bin/bash
apt update && apt install -y git python3-pip curl ufw
pip3 install ansible
ufw allow OpenSSH
ufw --force enable
git clone https://github.com/mtkell/open-cmmc-stack.git /opt/open-cmmc-stack
cd /opt/open-cmmc-stack/ansible
ansible-playbook -i localhost, secure_ubuntu.yml
