# CloudTrail trail S3 bucket is not publicly accessible

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudtrail_logs_s3_bucket_is_not_publicly_accessible` |
| クラウドプラットフォーム | AWS |
| サービス | cloudtrail |
| 重大度 | critical |
| カテゴリ | internet-exposed |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Industry and Regulatory Standards/AWS Foundational Security Best Practices, Industry and Regulatory Standards/CIS AWS Foundations Benchmark, Effects/Data Exposure |
| リソースタイプ | AwsS3Bucket |
| リソースグループ | storage |

## 説明

CloudTrail log destination **S3 buckets** are inspected for ACL grants that expose data to the public `AllUsers` group. Buckets hosted in other accounts are flagged for out-of-scope review.

## リスク

Exposed CloudTrail logs erode **confidentiality** and **integrity**. Adversaries can harvest API activity to map accounts, roles, and keys, enabling **reconnaissance** and evasion. If write is allowed, logs can be **poisoned** or deleted, thwarting investigations and compromising incident timelines.

## 推奨事項

Apply **least privilege** to the log bucket: - Enable S3 `Block Public Access` (account and bucket) - Remove `AllUsers`/`AuthenticatedUsers` ACLs; avoid wildcard principals - Permit only CloudTrail and constrain with `aws:SourceArn` Use a dedicated private bucket and monitor for permission changes.

## 修正手順


### CLI

```text
aws s3api put-bucket-acl --bucket <example_resource_name> --acl private
```

### Native IaC

```yaml
# CloudFormation: ensure the CloudTrail S3 bucket ACL is not public
Resources:
  CloudTrailLogsBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: <example_resource_name>
      AccessControl: Private  # CRITICAL: sets bucket ACL to private, removing any AllUsers (public) grants
```

### Terraform

```hcl
# Ensure the CloudTrail S3 bucket ACL is private
resource "aws_s3_bucket_acl" "fix_cloudtrail_logs_bucket" {
  bucket = "<example_resource_name>"
  acl    = "private"  # CRITICAL: removes any public (AllUsers) ACL grants
}
```

### Other

1. Open the AWS S3 Console
2. Select the bucket used by CloudTrail
3. Go to Permissions > Access control list (ACL)
4. Click Edit under Public access, remove any grants to "Everyone (public access)" (uncheck Read/Write)
5. Save changes

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudTrail/cloudtrail-bucket-publicly-accessible.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudTrail/cloudtrail-bucket-publicly-accessible.html)
- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)
- [https://docs.aws.amazon.com/config/latest/developerguide/cloudtrail-s3-bucket-public-access-prohibited.html](https://docs.aws.amazon.com/config/latest/developerguide/cloudtrail-s3-bucket-public-access-prohibited.html)
- [https://docs.panther.com/alerts/alert-runbooks/built-in-policies/aws-cloudtrail-logs-s3-bucket-not-publicly-accessible](https://docs.panther.com/alerts/alert-runbooks/built-in-policies/aws-cloudtrail-logs-s3-bucket-not-publicly-accessible)

## 技術情報

- Source Metadata：[sources/aws/cloudtrail_logs_s3_bucket_is_not_publicly_accessible/metadata.json](../../sources/aws/cloudtrail_logs_s3_bucket_is_not_publicly_accessible/metadata.json)
- Source Code：[sources/aws/cloudtrail_logs_s3_bucket_is_not_publicly_accessible/check.py](../../sources/aws/cloudtrail_logs_s3_bucket_is_not_publicly_accessible/check.py)
- Source Metadata Path：`sources/aws/cloudtrail_logs_s3_bucket_is_not_publicly_accessible/metadata.json`
- Source Code Path：`sources/aws/cloudtrail_logs_s3_bucket_is_not_publicly_accessible/check.py`
