provider "digitalocean" {
  token = var.do_token
}

resource "digitalocean_droplet" "secure_host" {
  name       = "cmmc-hardened"
  region     = "nyc3"
  size       = "s-2vcpu-4gb"
  image      = "ubuntu-22-04-x64"
  ssh_keys   = [var.ssh_fingerprint]
  user_data  = file("${path.module}/bootstrap.sh")

  tags = ["cmmc", "secure-host"]
}

output "droplet_ip" {
  value = digitalocean_droplet.secure_host.ipv4_address
}
