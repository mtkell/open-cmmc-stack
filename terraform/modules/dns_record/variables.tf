variable "zone_id" {
  description = "Cloudflare Zone ID"
  type        = string
}

variable "subdomain" {
  description = "Subdomain to create (e.g., mail, auth)"
  type        = string
}

variable "ip_address" {
  description = "Public IP address to point the A record to"
  type        = string
}
