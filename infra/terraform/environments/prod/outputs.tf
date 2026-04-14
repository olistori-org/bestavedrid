output "server_ip" {
  description = "Public IP address of the prod server"
  value       = module.server.server_ip
}

output "server_id" {
  description = "ID of the prod server"
  value       = module.server.server_id
}
