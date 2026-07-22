## Deployment using Terraform

This Terraform configuration creates the necessary IAM role and policies to allow ST Cloud to scan your AWS account, with optional S3 integration for storing scan reports.

### Quick Start

1. **Configure variables:**
   ```bash
   cp terraform.tfvars.example terraform.tfvars
   # Edit terraform.tfvars with your values
   ```

2. **Deploy:**
   ```bash
   terraform init
   terraform plan
   terraform apply
   ```

### Variables

- `external_id` (required): External ID for role assumption security
- `account_id` (required): AWS account ID of the identity used by the ST Cloud scanner
- `iam_principal` (required): IAM principal path used by the scanner, for example `role/STCloudScanner` or `user/stcloud-scanner`
- `enable_organizations` (optional): Enable read-only AWS Organizations discovery permissions (default: false)
- `enable_s3_integration` (optional): Enable S3 integration for storing scan reports (default: false)
- `s3_integration_bucket_name` (conditional): S3 bucket name for reports (required if `enable_s3_integration` is true)
- `s3_integration_bucket_account_id` (conditional): S3 bucket owner account ID (required if `enable_s3_integration` is true)

### Usage Examples

#### Basic deployment (without S3 integration)
```bash
terraform apply \
  -var="external_id=your-external-id-here" \
  -var="account_id=123456789012" \
  -var="iam_principal=role/STCloudScanner"
```

#### With S3 integration enabled
```bash
terraform apply \
  -var="external_id=your-external-id-here" \
  -var="account_id=123456789012" \
  -var="iam_principal=role/STCloudScanner" \
  -var="enable_s3_integration=true" \
  -var="s3_integration_bucket_name=your-s3-bucket-name" \
  -var="s3_integration_bucket_account_id=123456789012"
```

#### Using terraform.tfvars file (Recommended)
```bash
cp terraform.tfvars.example terraform.tfvars
# Edit the file with your values
terraform apply
```

#### Command line variables (Alternative)
```bash
terraform apply \
  -var="external_id=your-external-id-here" \
  -var="account_id=123456789012" \
  -var="iam_principal=role/STCloudScanner"
```

### Outputs

After successful deployment, you'll get:
- `stcloud_scan_role_arn`: The ARN of the created IAM role (use this in ST Cloud)
- `stcloud_scan_role_name`: The name of the IAM role
- `s3_integration_enabled`: Whether S3 integration is enabled

> **Note:** Terraform will use the AWS credentials of your default profile or AWS_PROFILE environment variable.
