variable "fqdn_root" {
  description = "Base domain used for subdomain routing (e.g., example.com)"
  type        = string
}

variable "infrastructure_provider" {
  description = "Target infrastructure provider (e.g., aws, azure, gcp, digitalocean, proxmox)"
  type        = string
}

variable "vm_definitions" {
  description = "Map of service names to regions and tags"
  type = map(object({
    region = string
    tags   = map(string)
  }))
}

variable "digitalocean_token" {
  description = "API token for DigitalOcean"
  type        = string
  sensitive   = true
}

variable "proxmox_api_url" { ... }
variable "proxmox_user" { ... }
variable "proxmox_password" { ... }
variable "proxmox_node" { ... }
variable "proxmox_template" { ... }

variable "fqdn_root" {
  description = "Base domain for DNS records (e.g., example.com)"
  type        = string
}

variable "cloudflare_api_token" {
  description = "API token for Cloudflare with DNS edit permissions"
  type        = string
  sensitive   = true
}

variable "cloudflare_zone_id" {
  description = "Zone ID of the domain in Cloudflare"
  type        = string
}
