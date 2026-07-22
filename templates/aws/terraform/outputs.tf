# Outputs
###################################
output "stcloud_scan_role_arn" {
  description = "ARN of the ST Cloud scan role"
  value       = aws_iam_role.stcloud_scan.arn
}

output "stcloud_scan_role_name" {
  description = "Name of the ST Cloud scan role"
  value       = aws_iam_role.stcloud_scan.name
}

output "external_id" {
  description = "External ID used for role assumption"
  value       = var.external_id
  sensitive   = true
}

output "s3_integration_enabled" {
  description = "Whether S3 integration is enabled"
  value       = var.enable_s3_integration
}
