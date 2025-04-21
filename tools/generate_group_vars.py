import yaml

# Load deployment_config.yml
with open('deployment_config.yml', 'r') as f:
    deployment_config = yaml.safe_load(f)

# Flattened structure for group_vars/all.yml
group_vars = {
    'default_user': deployment_config['global_admin_username'],
    'default_shell': '/bin/bash',
    'ssh_authorized_key': deployment_config['admin_ssh_public_key'],
    'global_admin_email': deployment_config['global_admin_email'],
    'domain_name': deployment_config['domain_name'],
    'hostname': deployment_config['hostname'],
    'timezone': deployment_config['timezone'],
    'dns_resolver_ip': deployment_config['dns_resolver_ip'],
    'ssh_port': deployment_config['ssh_port'],
    'disable_root_ssh': deployment_config['disable_root_ssh'],
    'enforce_key_authentication': deployment_config['enforce_key_authentication'],
    'nextcloud_port': deployment_config['nextcloud_port'],
    'mailcow_port': deployment_config['mailcow_port'],
    'keycloak_port': deployment_config['keycloak_port'],
    'stepca_port': deployment_config['stepca_port'],
    'wazuh_port': deployment_config['wazuh_port'],
    'tailscale_auth_key': deployment_config['tailscale_auth_key'],
    'mailcow_hostname': deployment_config['mailcow_hostname'],
    'mailcow_admin_user': deployment_config['mailcow_admin_user'],
    'mailcow_admin_password': deployment_config['mailcow_admin_password'],
    'mailcow_letsencrypt_email': deployment_config['mailcow_letsencrypt_email'],
    'mailcow_use_letsencrypt': deployment_config['mailcow_use_letsencrypt'],
    'keycloak_realm': deployment_config['keycloak_realm'],
    'nextcloud_aio_image': deployment_config['nextcloud_aio_image'],
    'keycloak_image': deployment_config['keycloak_image'],
    'mailcow_image': deployment_config['mailcow_image'],
    'nextcloud_data_dir': deployment_config['nextcloud_data_dir'],
    'mailcow_data_dir': deployment_config['mailcow_data_dir'],
    'backup_base_dir': deployment_config['backup_base_dir'],
    'logs_dir': deployment_config['logs_dir'],
    'restic_password': deployment_config['restic_password'],
    'restic_repo': deployment_config['restic_repo'],
    'svc_keycloak': deployment_config['svc_keycloak'],
    'svc_mailcow': deployment_config['svc_mailcow'],
    'svc_wazuh': deployment_config['svc_wazuh'],
    'svc_stepca': deployment_config['svc_stepca'],
    'banner_text': deployment_config['banner_text']
}

# Save to group_vars/all.yml
with open('group_vars/all.yml', 'w') as f:
    yaml.dump(group_vars, f, sort_keys=False, default_flow_style=False)
