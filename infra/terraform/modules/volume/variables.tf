variable "name" {
  description = "Volume name"
  type        = string
}

variable "size" {
  description = "Volume size in GB"
  type        = number
  default     = 20
}

variable "server_id" {
  description = "ID of the server to attach the volume to"
  type        = number
}
