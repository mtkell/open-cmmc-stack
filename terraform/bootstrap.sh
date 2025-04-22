#!/bin/bash
set -e

echo "🔧 Initializing Terraform..."
terraform init

echo "📐 Running Terraform plan..."
terraform plan -var-file=terraform.tfvars

echo "🚀 Applying Terraform configuration..."
terraform apply -auto-approve -var-file=terraform.tfvars

echo "✅ Done. Review outputs below:"
terraform output
