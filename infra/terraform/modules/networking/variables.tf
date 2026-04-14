variable "name" {
  description = "Network name"
  type        = string
}

variable "ip_range" {
  description = "Network IP range (CIDR)"
  type        = string
  default     = "10.0.0.0/16"
}

variable "subnet_ip_range" {
  description = "Subnet IP range (CIDR)"
  type        = string
  default     = "10.0.1.0/24"
}

variable "network_zone" {
  description = "Network zone (e.g. eu-central)"
  type        = string
  default     = "eu-central"
}
