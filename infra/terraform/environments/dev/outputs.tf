output "server_ip" {
  description = "Public IP address of the dev server"
  value       = module.server.server_ip
}

output "server_id" {
  description = "ID of the dev server"
  value       = module.server.server_id
}
