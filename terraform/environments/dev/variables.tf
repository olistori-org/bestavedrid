variable "hcloud_token" {
  type      = string
  sensitive = true
}

variable "ssh_public_key" {
  type      = string
  sensitive = true
}

variable "server_name" {
  type    = string
  default = "besta-vedrid"
}

variable "server_type" {
  type    = string
  default = "cx23"
}

variable "server_image" {
  type    = string
  default = "ubuntu-24.04"
}

variable "location" {
  type    = string
  default = "nbg1"
}

variable "ssh_allowed_ips" {
  type        = list(string)
  description = "CIDR blocks allowed to SSH into the server"
}