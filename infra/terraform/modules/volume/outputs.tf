output "volume_id" {
  description = "Volume ID"
  value       = hcloud_volume.this.id
}

output "linux_device" {
  description = "Linux device path for the volume"
  value       = hcloud_volume.this.linux_device
}
