variable "server_name" {
  description = "Name of the server"
  type        = string
}

variable "server_type" {
  description = "Hetzner server type (e.g. cx22)"
  type        = string
}

variable "location" {
  description = "Hetzner datacenter location (e.g. nbg1)"
  type        = string
}

variable "image" {
  description = "OS image (e.g. ubuntu-24.04)"
  type        = string
}

variable "ssh_key_name" {
  description = "Name of the SSH key registered in Hetzner Cloud"
  type        = string
}
