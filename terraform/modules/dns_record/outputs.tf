output "fqdn" {
  value = "${var.subdomain}.${var.root_domain}"
}
