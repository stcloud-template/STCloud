# CloudTrail trail records S3 object-level read events for all S3 buckets

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudtrail_s3_dataevents_read_enabled` |
| 云平台 | AWS |
| 服务 | cloudtrail |
| 严重等级 | low |
| 类别 | logging, forensics-ready |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsCloudTrailTrail |
| 资源组 | monitoring |

## 描述

**CloudTrail trails** log **S3 object-level read data events** for all buckets, capturing object access (for example `GetObject`) via selectors targeting `AWS::S3::Object`

## 风险

Without **object-level read logging**, S3 access is opaque. Attackers or insiders can exfiltrate data via `GetObject` without audit trails, eroding **confidentiality** and hindering **forensics**, anomaly detection, and incident response.

## 推荐措施

Enable CloudTrail **data events** for S3 objects with `ReadOnly` (or `All`) across all current and future buckets. Use a multi-Region trail, centralize logs in an encrypted bucket with lifecycle retention, and integrate monitoring/alerts to support **defense in depth** and accountable access.

## 修复步骤


### CLI

```text
aws cloudtrail put-event-selectors --trail-name <example_resource_name> --event-selectors '[{"ReadWriteType":"ReadOnly","DataResources":[{"Type":"AWS::S3::Object","Values":["arn:aws:s3"]}]}]'
```

### Native IaC

```yaml
# CloudFormation: enable S3 object-level READ data events for all buckets on a trail
Resources:
  <example_resource_name>:
    Type: AWS::CloudTrail::Trail
    Properties:
      S3BucketName: <example_resource_name>
      EventSelectors:
        - ReadWriteType: ReadOnly        # CRITICAL: log read-only data events
          DataResources:
            - Type: AWS::S3::Object      # CRITICAL: target S3 object-level events
              Values:
                - arn:aws:s3             # CRITICAL: applies to all S3 buckets/objects
```

### Terraform

```hcl
# Terraform: enable S3 object-level READ data events for all buckets on a trail
resource "aws_cloudtrail" "<example_resource_name>" {
  name           = "<example_resource_name>"
  s3_bucket_name = "<example_resource_name>"

  event_selector {
    read_write_type = "ReadOnly"                 # CRITICAL: log read-only data events
    data_resource {
      type   = "AWS::S3::Object"                 # CRITICAL: target S3 object-level events
      values = ["arn:aws:s3"]                    # CRITICAL: apply to all S3 buckets/objects
    }
  }
}
```

### Other

1. In the AWS Console, open CloudTrail and select Trails
2. Open your trail and go to the Data events section
3. Add data event for S3 and choose All current and future S3 buckets
4. Select only Read events (or All if Read-only is unavailable)
5. Save changes

## 参考资料

- [https://awswala.medium.com/enable-cloudtrail-data-events-logging-for-objects-in-an-s3-bucket-33cade51ae2b](https://awswala.medium.com/enable-cloudtrail-data-events-logging-for-objects-in-an-s3-bucket-33cade51ae2b)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-23](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-23)
- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-cloudtrail-logging-for-s3.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-cloudtrail-logging-for-s3.html)
- [https://www.plerion.com/cloud-knowledge-base/ensure-object-level-logging-for-read-events-enabled-for-s3-bucket](https://www.plerion.com/cloud-knowledge-base/ensure-object-level-logging-for-read-events-enabled-for-s3-bucket)

## 技术信息

- Source Metadata：[sources/aws/cloudtrail_s3_dataevents_read_enabled/metadata.json](../../sources/aws/cloudtrail_s3_dataevents_read_enabled/metadata.json)
- Source Code：[sources/aws/cloudtrail_s3_dataevents_read_enabled/check.py](../../sources/aws/cloudtrail_s3_dataevents_read_enabled/check.py)
- Source Metadata Path：`sources/aws/cloudtrail_s3_dataevents_read_enabled/metadata.json`
- Source Code Path：`sources/aws/cloudtrail_s3_dataevents_read_enabled/check.py`
