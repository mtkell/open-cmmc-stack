resource "google_compute_instance" "vm" {
  count        = var.provider == "gcp" ? 1 : 0
  name         = "open-cmmc-${var.service_name}"
  machine_type = "e2-medium"
  zone         = var.gcp_zone

  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2204-lts"
    }
  }

  network_interface {
    network       = "default"
    access_config {} # This allocates a one-to-one NAT IP
  }

  metadata = {
    ssh-keys = "ubuntu:${var.ssh_public_key}"
  }

  tags = [for tag_key, tag_value in var.tags : "${tag_key}:${tag_value}"]
}
