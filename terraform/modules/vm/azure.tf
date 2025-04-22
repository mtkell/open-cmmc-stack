resource "azurerm_linux_virtual_machine" "vm" {
  count               = var.provider == "azure" ? 1 : 0
  name                = "open-cmmc-${var.service_name}"
  resource_group_name = var.azure_resource_group
  location            = var.region
  size                = "Standard_B1s"
  admin_username      = "ubuntu"

  admin_ssh_key {
    username   = "ubuntu"
    public_key = var.ssh_public_key
  }

  network_interface_ids = [var.azure_nic_id]
}
