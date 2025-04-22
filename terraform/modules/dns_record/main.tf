resource "cloudflare_record" "dns" {
  zone_id = var.zone_id
  name    = var.subdomain
  type    = "A"
  value   = var.ip_address
  ttl     = 300
  proxied = false
}
