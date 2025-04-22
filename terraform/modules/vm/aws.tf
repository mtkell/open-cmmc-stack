resource "aws_instance" "vm" {
  count         = var.provider == "aws" ? 1 : 0
  ami           = var.aws_ami
  instance_type = "t3.micro"
  key_name      = var.ssh_key_name
  tags = merge(
    var.tags,
    { Name = "open-cmmc-${var.service_name}" }
  )
}
