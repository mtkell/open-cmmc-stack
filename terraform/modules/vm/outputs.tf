output "ip_address" {
  value = (
    var.provider == "digitalocean" && length(digitalocean_droplet.vm) > 0 ? digitalocean_droplet.vm[0].ipv4_address :
    var.provider == "aws" && length(aws_instance.vm) > 0 ? aws_instance.vm[0].public_ip :
    var.provider == "azure" && length(azurerm_linux_virtual_machine.vm) > 0 ? azurerm_linux_virtual_machine.vm[0].public_ip_address :
    var.provider == "gcp" && length(google_compute_instance.vm) > 0 ? google_compute_instance.vm[0].network_interface[0].access_config[0].nat_ip :
    var.provider == "proxmox" ? proxmox_vm_qemu.vm[0].ipconfig0 :
    null
  )
}