# Check if S3 buckets have secure transport policy.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `s3_bucket_secure_transport_policy` |
| クラウドプラットフォーム | AWS |
| サービス | s3 |
| 重大度 | medium |
| カテゴリ | encryption |
| チェックタイプ | Data Protection |
| リソースタイプ | AwsS3Bucket |
| リソースグループ | storage |

## 説明

Check if S3 buckets have secure transport policy.

## リスク

If HTTPS is not enforced on the bucket policy, communication between clients and S3 buckets can use unencrypted HTTP. As a result, sensitive information could be transmitted in clear text over the network or internet.

## 推奨事項

Ensure that S3 buckets have encryption in transit enabled.

- 推奨リンク：[https://aws.amazon.com/premiumsupport/knowledge-center/s3-bucket-policy-for-config-rule/](https://aws.amazon.com/premiumsupport/knowledge-center/s3-bucket-policy-for-config-rule/)

## 修正手順


### Other

[https://docs.ST Cloud.com/checks/aws/s3-policies/s3_15-secure-data-transport#aws-console](https://docs.ST Cloud.com/checks/aws/s3-policies/s3_15-secure-data-transport#aws-console)

## 参考資料

- [https://aws.amazon.com/premiumsupport/knowledge-center/s3-bucket-policy-for-config-rule/](https://aws.amazon.com/premiumsupport/knowledge-center/s3-bucket-policy-for-config-rule/)

## 技術情報

- Source Metadata：[sources/aws/s3_bucket_secure_transport_policy/metadata.json](../../sources/aws/s3_bucket_secure_transport_policy/metadata.json)
- Source Code：[sources/aws/s3_bucket_secure_transport_policy/check.py](../../sources/aws/s3_bucket_secure_transport_policy/check.py)
- Source Metadata Path：`sources/aws/s3_bucket_secure_transport_policy/metadata.json`
- Source Code Path：`sources/aws/s3_bucket_secure_transport_policy/check.py`
