module "server" {
  source = "../../modules/hetzner-server"

  server_name  = "besta-vedrid-prod"
  server_type  = var.server_type
  location     = var.location
  ssh_key_name = var.ssh_key_name
  image        = var.image
}

module "firewall" {
  source = "../../modules/firewall"

  name      = "besta-vedrid-prod-firewall"
  server_id = module.server.server_id
}
