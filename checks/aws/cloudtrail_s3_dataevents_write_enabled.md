# CloudTrail trail records all S3 object-level API operations for all buckets

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudtrail_s3_dataevents_write_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | cloudtrail |
| 重大度 | low |
| カテゴリ | logging, forensics-ready |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark |
| リソースタイプ | AwsCloudTrailTrail |
| リソースグループ | monitoring |

## 説明

**CloudTrail trails** include **S3 object-level data events** for **write (or all) operations** across **all current and future buckets**, via classic or advanced selectors. This records actions like `PutObject`, `DeleteObject`, and multipart uploads at the object level.

## リスク

Without object-level write logging, unauthorized or accidental changes and deletions can go unobserved, undermining data **integrity** and **availability**. Forensics lose visibility into who modified or removed objects, hindering detection of ransomware, rogue automation, or insider tampering.

## 推奨事項

Enable **CloudTrail S3 data events** for object-level **write** (and *optionally* read) across all buckets on a multi-Region trail. Apply **least privilege** to log storage, set **lifecycle** retention, and integrate alerts. Use **advanced selectors** to target sensitive buckets/operations for cost control and **defense in depth**.

## 修正手順


### CLI

```text
aws cloudtrail put-event-selectors --trail-name <example_resource_name> --event-selectors '[{"ReadWriteType":"WriteOnly","DataResources":[{"Type":"AWS::S3::Object","Values":["arn:aws:s3"]}]}]'
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::CloudTrail::Trail
    Properties:
      TrailName: <example_resource_name>
      S3BucketName: <example_resource_name>
      EventSelectors:
        - ReadWriteType: WriteOnly
          DataResources:
            - Type: AWS::S3::Object
              Values:
                - arn:aws:s3  # Critical: enables S3 object-level write data events for all buckets, fixing the check
```

### Terraform

```hcl
resource "aws_cloudtrail" "<example_resource_name>" {
  name           = "<example_resource_name>"
  s3_bucket_name = "<example_resource_name>"

  event_selector {
    read_write_type = "WriteOnly"
    data_resource {
      type   = "AWS::S3::Object"
      values = ["arn:aws:s3"]  # Critical: logs S3 object-level write events for all buckets to pass the check
    }
  }
}
```

### Other

1. In the AWS Console, open CloudTrail and go to Trails
2. Select <your trail> and click Edit under Data events
3. For Data event source, choose S3
4. Select All current and future S3 buckets
5. Check Write events (or All events)
6. Click Save changes

## 参考資料

- [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html)
- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-cloudtrail-logging-for-s3.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-cloudtrail-logging-for-s3.html)
- [https://www.go2share.net/article/s3-bucket-logging](https://www.go2share.net/article/s3-bucket-logging)
- [https://docs.amazonaws.cn/en_us/AmazonS3/latest/userguide/cloudtrail-logging-s3-info.html](https://docs.amazonaws.cn/en_us/AmazonS3/latest/userguide/cloudtrail-logging-s3-info.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-22](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-22)

## 技術情報

- Source Metadata：[sources/aws/cloudtrail_s3_dataevents_write_enabled/metadata.json](../../sources/aws/cloudtrail_s3_dataevents_write_enabled/metadata.json)
- Source Code：[sources/aws/cloudtrail_s3_dataevents_write_enabled/check.py](../../sources/aws/cloudtrail_s3_dataevents_write_enabled/check.py)
- Source Metadata Path：`sources/aws/cloudtrail_s3_dataevents_write_enabled/metadata.json`
- Source Code Path：`sources/aws/cloudtrail_s3_dataevents_write_enabled/check.py`
