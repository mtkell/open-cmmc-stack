terraform {
  required_version = ">= 1.3.0"

  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.0"
    }
  }
}

provider "local" {}

locals {
  services = var.vm_definitions
}

module "vm" {
  source     = "./modules/vm"
  for_each   = local.services

  service_name = each.key
  provider     = var.infrastructure_provider
  region       = each.value.region
  tags         = each.value.tags
}

# Create a DNS A record for each deployed service
module "dns" {
  source   = "./modules/dns_record"
  for_each = local.services

  zone_id     = var.cloudflare_zone_id
  subdomain   = each.key
  ip_address  = module.vm[each.key].ip_address
}
