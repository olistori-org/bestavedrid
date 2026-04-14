variable "name" {
  description = "Firewall name"
  type        = string
}

variable "server_id" {
  description = "ID of the server to attach the firewall to"
  type        = number
}
