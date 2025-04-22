variable "ssh_keys" {
  description = "List of DigitalOcean SSH key fingerprints or IDs"
  type        = list(string)
}

variable "aws_ami" {
  description = "AMI ID to use for AWS EC2 instance"
  type        = string
  default     = "ami-0c55b159cbfafe1f0" # Ubuntu 22.04 in us-east-1 (example)
}

variable "ssh_key_name" {
  description = "AWS SSH key pair name"
  type        = string
}

variable "azure_resource_group" {
  description = "Azure resource group name"
  type        = string
}

variable "azure_nic_id" {
  description = "Azure network interface ID"
  type        = string
}

variable "ssh_public_key" {
  description = "Public SSH key for Azure admin login"
  type        = string
}

variable "gcp_project_id" {
  description = "Google Cloud Project ID"
  type        = string
}

variable "gcp_region" {
  description = "Google Cloud region"
  type        = string
}

variable "gcp_zone" {
  description = "Google Cloud zone"
  type        = string
}

variable "gcp_credentials_file" {
  description = "Path to GCP service account JSON key file"
  type        = string
}
