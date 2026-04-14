output "network_id" {
  description = "Hetzner network ID"
  value       = hcloud_network.this.id
}

output "subnet_id" {
  description = "Hetzner subnet ID"
  value       = hcloud_network_subnet.this.id
}
