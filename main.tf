terraform {
  required_version = ">= 1.6.0"

  required_providers {
    hcloud = {
      source  = "hetznercloud/hcloud"
      version = "~> 1.60"
    }
  }
}

provider "hcloud" {}

resource "hcloud_ssh_key" "default" {
  name       = "windows-main-key"
  public_key = file("C:/Users/Óli/.ssh/github_key.pub")
}

resource "hcloud_server" "vps" {
  name        = "besta-vedrid"
  server_type = "cx23"
  image       = "ubuntu-24.04"
  location    = "nbg1"
  ssh_keys    = [hcloud_ssh_key.default.id]

  public_net {
    ipv4_enabled = true
    ipv6_enabled = true
  }
}

output "server_ip" {
  value = hcloud_server.vps.ipv4_address
}