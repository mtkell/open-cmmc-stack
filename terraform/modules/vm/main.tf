resource "digitalocean_droplet" "vm" {
  name   = "open-cmmc-${var.service_name}"
  region = var.region
  size   = "s-1vcpu-1gb"
  image  = "ubuntu-22-04-x64"

  tags = [for tag_key, tag_value in var.tags : "${tag_key}:${tag_value}"]

  ssh_keys = var.ssh_keys

  lifecycle {
    ignore_changes = [image]
  }
}
