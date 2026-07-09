# Check if S3 buckets have secure transport policy.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `s3_bucket_secure_transport_policy` |
| 云平台 | AWS |
| 服务 | s3 |
| 严重等级 | medium |
| 类别 | encryption |
| 检查类型 | Data Protection |
| 资源类型 | AwsS3Bucket |
| 资源组 | storage |

## 描述

Check if S3 buckets have secure transport policy.

## 风险

If HTTPS is not enforced on the bucket policy, communication between clients and S3 buckets can use unencrypted HTTP. As a result, sensitive information could be transmitted in clear text over the network or internet.

## 推荐措施

Ensure that S3 buckets have encryption in transit enabled.

- 推荐链接：[https://aws.amazon.com/premiumsupport/knowledge-center/s3-bucket-policy-for-config-rule/](https://aws.amazon.com/premiumsupport/knowledge-center/s3-bucket-policy-for-config-rule/)

## 修复步骤


### Other

[https://docs.ST Cloud.com/checks/aws/s3-policies/s3_15-secure-data-transport#aws-console](https://docs.ST Cloud.com/checks/aws/s3-policies/s3_15-secure-data-transport#aws-console)

## 参考资料

- [https://aws.amazon.com/premiumsupport/knowledge-center/s3-bucket-policy-for-config-rule/](https://aws.amazon.com/premiumsupport/knowledge-center/s3-bucket-policy-for-config-rule/)

## 技术信息

- Source Metadata：[sources/aws/s3_bucket_secure_transport_policy/metadata.json](../../sources/aws/s3_bucket_secure_transport_policy/metadata.json)
- Source Code：[sources/aws/s3_bucket_secure_transport_policy/check.py](../../sources/aws/s3_bucket_secure_transport_policy/check.py)
- Source Metadata Path：`sources/aws/s3_bucket_secure_transport_policy/metadata.json`
- Source Code Path：`sources/aws/s3_bucket_secure_transport_policy/check.py`
