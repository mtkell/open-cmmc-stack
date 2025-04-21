# ✅ Preflight Validation Checks

**Status:** PASSED  
Timestamp: {{ ansible_date_time.iso8601 }}

## Variables
- default_user: `{{ default_user }}`
- domain_name: `{{ domain_name }}`
- hostname: `{{ hostname }}`
- mailcow_admin_user: `{{ mailcow_admin_user }}`
- mailcow_fqdn: `{{ mailcow_fqdn }}`
- mailcow_letsencrypt_email: `{{ mailcow_letsencrypt_email }}`

## DNS Resolution
- Domain `{{ domain_name }}` resolved to: `{{ domain_lookup.stdout | default('N/A') }}`

## SSH Key Format
- SSH key validated against standard format

## Email Format
- Email passed regex validation
