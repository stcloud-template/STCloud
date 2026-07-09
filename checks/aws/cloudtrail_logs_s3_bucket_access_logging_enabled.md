# CloudTrail trail destination S3 bucket has access logging enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudtrail_logs_s3_bucket_access_logging_enabled` |
| 云平台 | AWS |
| 服务 | cloudtrail |
| 严重等级 | medium |
| 类别 | logging, forensics-ready |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark |
| 资源类型 | AwsCloudTrailTrail |
| 资源组 | monitoring |

## 描述

CloudTrail trails deliver logs to an S3 bucket; this evaluates whether that bucket has **S3 server access logging** enabled to record requests against it. *If the destination bucket is outside the account or audit scope, a manual review is indicated.*

## 风险

Without access logging on the CloudTrail logs bucket, access and changes to log files lack an independent audit trail. Attackers could read, delete, or replace logs without attribution, undermining **log confidentiality** and **integrity**, and slowing **incident response**.

## 推荐措施

Enable **S3 server access logging** on the CloudTrail logs bucket and write logs to a separate, tightly controlled bucket. Apply **least privilege**, enable **versioning**, and consider **Object Lock** to deter tampering. Centralize monitoring to support defense-in-depth and rapid investigation.

## 修复步骤


### CLI

```text
aws s3api put-bucket-logging --bucket <CLOUDTRAIL_BUCKET_NAME> --bucket-logging-status "{\"LoggingEnabled\":{\"TargetBucket\":\"<TARGET_BUCKET_NAME>\"}}"
```

### Native IaC

```yaml
# CloudFormation: enable S3 access logging on the CloudTrail destination bucket
Resources:
  <example_log_bucket_name>:
    Type: AWS::S3::Bucket

  <example_cloudtrail_bucket>:
    Type: AWS::S3::Bucket
    Properties:
      LoggingConfiguration:
        DestinationBucketName: !Ref <example_log_bucket_name>  # Critical: turns on server access logging to this destination bucket
        # This enables access logging so the check passes
```

### Terraform

```hcl
# Enable access logging on the CloudTrail S3 bucket
resource "aws_s3_bucket" "<example_log_bucket_name>" {
  bucket = "<example_log_bucket_name>"
}

resource "aws_s3_bucket" "<example_bucket_name>" {
  bucket = "<example_bucket_name>"
}

resource "aws_s3_bucket_logging" "<example_resource_name>" {
  bucket        = aws_s3_bucket.<example_bucket_name>.id
  target_bucket = aws_s3_bucket.<example_log_bucket_name>.id  # Critical: enables server access logging to the target bucket
}
```

### Other

1. In the AWS Console, go to S3 and open the bucket used by your CloudTrail trail
2. Select the Properties tab
3. In Server access logging, click Edit
4. Enable logging and choose a different destination S3 bucket for the logs
5. Click Save changes

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/cloudtrail-controls.html](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudtrail-controls.html)
- [https://docs.aws.amazon.com/AmazonS3/latest/dev/security-best-practices.html](https://docs.aws.amazon.com/AmazonS3/latest/dev/security-best-practices.html)

## 技术信息

- Source Metadata：[sources/aws/cloudtrail_logs_s3_bucket_access_logging_enabled/metadata.json](../../sources/aws/cloudtrail_logs_s3_bucket_access_logging_enabled/metadata.json)
- Source Code：[sources/aws/cloudtrail_logs_s3_bucket_access_logging_enabled/check.py](../../sources/aws/cloudtrail_logs_s3_bucket_access_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/cloudtrail_logs_s3_bucket_access_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/cloudtrail_logs_s3_bucket_access_logging_enabled/check.py`
