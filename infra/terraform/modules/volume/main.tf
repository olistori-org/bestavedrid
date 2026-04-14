resource "hcloud_volume" "this" {
  name      = var.name
  size      = var.size
  server_id = var.server_id
  automount = true
  format    = "ext4"
}
