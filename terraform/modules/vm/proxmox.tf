resource "proxmox_vm_qemu" "vm" {
  count       = var.provider == "proxmox" ? 1 : 0
  name        = "open-cmmc-${var.service_name}"
  target_node = var.proxmox_node
  clone       = var.proxmox_template
  ...
}
