# Region has at least one CloudTrail trail logging

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudtrail_multi_region_enabled` |
| 云平台 | AWS |
| 服务 | cloudtrail |
| 严重等级 | high |
| 类别 | logging, forensics-ready |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark |
| 资源类型 | AwsCloudTrailTrail |
| 资源组 | monitoring |

## 描述

**AWS CloudTrail** has at least one trail with `logging` enabled in every region. A **multi-region trail** or a regional trail counts for coverage in that region.

## 风险

Missing coverage in any region creates **visibility gaps**. Attackers can use lesser-monitored regions to run API actions, hide **unauthorized changes**, and exfiltrate data without audit trails, weakening **detective controls**, hindering **forensics**, and delaying response (confidentiality and integrity).

## 推荐措施

Use a **multi-region CloudTrail trail** or per-region trails so `logging` is active in every region, including unused ones. Centralize logs, enforce **least privilege** to log stores, and add **defense-in-depth** with encryption, integrity validation, and retention. Continuously monitor trail health to catch gaps.

## 修复步骤


### Native IaC

```yaml
# CloudFormation: Create a multi-region CloudTrail and start logging
Resources:
  <example_resource_name>:
    Type: AWS::CloudTrail::Trail
    Properties:
      TrailName: <example_resource_name>
      S3BucketName: <example_resource_name>
      IsMultiRegionTrail: true  # Critical: applies the trail to all regions
      IsLogging: true           # Critical: ensures the trail is logging
```

### Terraform

```hcl
# Terraform: Multi-region CloudTrail with logging enabled
resource "aws_cloudtrail" "<example_resource_name>" {
  name           = "<example_resource_name>"
  s3_bucket_name = "<example_resource_name>"

  is_multi_region_trail = true  # Critical: applies the trail to all regions
  enable_logging        = true  # Critical: ensures the trail is logging
}
```

### Other

1. In the AWS Console, go to CloudTrail > Trails
2. If no trail exists: Click Create trail, enter a name, choose an S3 bucket, set Apply trail to all regions = Yes, then Create (logging starts)
3. If a trail exists: Select it, click Edit, set Apply trail to all regions = Yes, Save
4. If Status shows Not logging, click Start logging

## 参考资料

- [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrailconcepts.html#cloudtrail-concepts-management-events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrailconcepts.html#cloudtrail-concepts-management-events)

## 技术信息

- Source Metadata：[sources/aws/cloudtrail_multi_region_enabled/metadata.json](../../sources/aws/cloudtrail_multi_region_enabled/metadata.json)
- Source Code：[sources/aws/cloudtrail_multi_region_enabled/check.py](../../sources/aws/cloudtrail_multi_region_enabled/check.py)
- Source Metadata Path：`sources/aws/cloudtrail_multi_region_enabled/metadata.json`
- Source Code Path：`sources/aws/cloudtrail_multi_region_enabled/check.py`
