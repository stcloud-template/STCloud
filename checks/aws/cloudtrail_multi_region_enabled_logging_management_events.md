# CloudTrail trail logs management events for read and write operations

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudtrail_multi_region_enabled_logging_management_events` |
| 云平台 | AWS |
| 服务 | cloudtrail |
| 严重等级 | low |
| 类别 | logging, forensics-ready |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark |
| 资源类型 | AwsCloudTrailTrail |
| 资源组 | monitoring |

## 描述

**CloudTrail trails** record **management events** (`read` and `write`) in every AWS region and are actively logging, using a multi-region trail or per-region coverage.

## 风险

Without region-wide management event logging, changes to identities, networking, and audit settings can go untracked. Adversaries can operate in overlooked regions to create resources, modify permissions, or disable logging, undermining **integrity**, **confidentiality**, and incident response.

## 推荐措施

Enable a **multi-region CloudTrail** that logs **management events** for `read` and `write` in all regions. Centralize logs in a separate, locked-down account; apply **least privilege**, encryption, retention, and integrity validation; and protect trails and storage with tamper-evident, deny-delete controls for **defense-in-depth**.

## 修复步骤


### Native IaC

```yaml
# CloudFormation: enable multi-region and log management events (read & write)
Resources:
  <example_resource_name>:
    Type: AWS::CloudTrail::Trail
    Properties:
      S3BucketName: <example_resource_name>
      IsMultiRegionTrail: true  # CRITICAL: apply the trail to all regions
      EventSelectors:
        - IncludeManagementEvents: true  # CRITICAL: log management events
          ReadWriteType: All             # CRITICAL: log both read and write
```

### Terraform

```hcl
# Terraform: enable multi-region and log management events (read & write)
resource "aws_cloudtrail" "<example_resource_name>" {
  name           = "<example_resource_name>"
  s3_bucket_name = "<example_resource_name>"

  is_multi_region_trail = true  # CRITICAL: apply the trail to all regions

  event_selector {
    include_management_events = true  # CRITICAL: log management events
    read_write_type           = "All" # CRITICAL: log both read & write
  }
}
```

### Other

1. In the AWS Console, go to CloudTrail > Trails and select your trail
2. Click Edit
3. Set Apply trail to all regions to Yes
4. Under Management events, set Read/write events to All
5. Click Save changes
6. If Logging is Off, click Start logging

## 参考资料

No external references available.

## 技术信息

- Source Metadata：[sources/aws/cloudtrail_multi_region_enabled_logging_management_events/metadata.json](../../sources/aws/cloudtrail_multi_region_enabled_logging_management_events/metadata.json)
- Source Code：[sources/aws/cloudtrail_multi_region_enabled_logging_management_events/check.py](../../sources/aws/cloudtrail_multi_region_enabled_logging_management_events/check.py)
- Source Metadata Path：`sources/aws/cloudtrail_multi_region_enabled_logging_management_events/metadata.json`
- Source Code Path：`sources/aws/cloudtrail_multi_region_enabled_logging_management_events/check.py`
