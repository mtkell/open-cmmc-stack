variable "do_token" {
  description = "DigitalOcean API token"
  type        = string
  sensitive   = true
}

variable "ssh_fingerprint" {
  description = "Your public SSH key fingerprint registered with DigitalOcean"
  type        = string
}
