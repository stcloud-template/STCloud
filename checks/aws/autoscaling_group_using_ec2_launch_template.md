# Amazon EC2 Auto Scaling group uses an EC2 launch template

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `autoscaling_group_using_ec2_launch_template` |
| クラウドプラットフォーム | AWS |
| サービス | autoscaling |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices |
| リソースタイプ | AwsAutoScalingAutoScalingGroup |
| リソースグループ | compute |

## 説明

**EC2 Auto Scaling groups** use an **EC2 launch template** directly or via a `mixed instances policy` to define instance configuration and versioned settings.

## リスク

Without a launch template, there is no **versioned, auditable baseline** for instance settings, increasing configuration drift. Inconsistent metadata and network options can enable unauthorized access or unstable deployments, degrading confidentiality and availability.

## 推奨事項

Adopt **launch templates** for all Auto Scaling groups and include them in any `mixed instances policy`. Use versioning with approvals, enforce hardened defaults (least privilege roles, secure metadata like `IMDSv2`, encrypted storage), and apply change control to ensure consistency and defense in depth.

## 修正手順


### CLI

```text
aws autoscaling update-auto-scaling-group --auto-scaling-group-name <example_resource_name> --launch-template LaunchTemplateId=<template-id>
```

### Native IaC

```yaml
# CloudFormation: attach a Launch Template to the ASG
Resources:
  ASG:
    Type: AWS::AutoScaling::AutoScalingGroup
    Properties:
      MinSize: '0'
      MaxSize: '1'
      VPCZoneIdentifier:
        - <example_subnet_id>
      LaunchTemplate: # critical: ensures the ASG uses an EC2 launch template (fixes the check)
        LaunchTemplateId: <example_launch_template_id> # references the EC2 Launch Template
        Version: $Default
```

### Terraform

```hcl
# Terraform: attach a Launch Template to the ASG
resource "aws_autoscaling_group" "example" {
  min_size            = 0
  max_size            = 1
  vpc_zone_identifier = ["<example_subnet_id>"]

  launch_template {
    id      = "<example_launch_template_id>" # critical: ensures the ASG uses an EC2 launch template (fixes the check)
    version = "$Default"
  }
}
```

### Other

1. In the AWS console, go to EC2 > Auto Scaling Groups
2. Select <example_resource_name> and click Edit
3. Under "Launch template or configuration", choose Launch template and select your template and version (Default or Latest)
4. Click Update to save

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/asg-launch-template.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/asg-launch-template.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/autoscaling-controls.html#autoscaling-9](https://docs.aws.amazon.com/securityhub/latest/userguide/autoscaling-controls.html#autoscaling-9)
- [https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-launch-template.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-launch-template.html)

## 技術情報

- Source Metadata：[sources/aws/autoscaling_group_using_ec2_launch_template/metadata.json](../../sources/aws/autoscaling_group_using_ec2_launch_template/metadata.json)
- Source Code：[sources/aws/autoscaling_group_using_ec2_launch_template/check.py](../../sources/aws/autoscaling_group_using_ec2_launch_template/check.py)
- Source Metadata Path：`sources/aws/autoscaling_group_using_ec2_launch_template/metadata.json`
- Source Code Path：`sources/aws/autoscaling_group_using_ec2_launch_template/check.py`
