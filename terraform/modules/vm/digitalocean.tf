resource "digitalocean_droplet" "vm" {
  count  = var.provider == "digitalocean" ? 1 : 0
  name   = "open-cmmc-${var.service_name}"
  region = var.region
  image  = "ubuntu-22-04-x64"
  size   = "s-1vcpu-1gb"
  ssh_keys = var.ssh_keys
  tags = [for tag_key, tag_value in var.tags : "${tag_key}:${tag_value}"]
}
