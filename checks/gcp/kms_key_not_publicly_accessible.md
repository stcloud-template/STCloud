# Check for Publicly Accessible Cloud KMS Keys

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `kms_key_not_publicly_accessible` |
| 云平台 | GCP |
| 服务 | kms |
| 严重等级 | high |
| 类别 | internet-exposed |
| 资源类型 | CryptoKey |
| 资源组 | security |

## 描述

Check for Publicly Accessible Cloud KMS Keys

## 风险

Ensure that the IAM policy associated with your Cloud Key Management Service (KMS) keys is restricting anonymous and/or public access

## 推荐措施

To deny access from anonymous and public users, remove the bindings for 'allUsers' and 'allAuthenticatedUsers' members from the KMS key's IAM policy.

- 推荐链接：[https://cloud.google.com/kms/docs/iam](https://cloud.google.com/kms/docs/iam)

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-general-policies/ensure-that-cloud-kms-cryptokeys-are-not-anonymously-or-publicly-accessible#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-general-policies/ensure-that-cloud-kms-cryptokeys-are-not-anonymously-or-publicly-accessible#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudKMS/publicly-accessible-kms-cryptokeys.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudKMS/publicly-accessible-kms-cryptokeys.html)

## 参考资料

- [https://cloud.google.com/kms/docs/iam](https://cloud.google.com/kms/docs/iam)

## 技术信息

- Source Metadata：[sources/gcp/kms_key_not_publicly_accessible/metadata.json](../../sources/gcp/kms_key_not_publicly_accessible/metadata.json)
- Source Code：[sources/gcp/kms_key_not_publicly_accessible/check.py](../../sources/gcp/kms_key_not_publicly_accessible/check.py)
- Source Metadata Path：`sources/gcp/kms_key_not_publicly_accessible/metadata.json`
- Source Code Path：`sources/gcp/kms_key_not_publicly_accessible/check.py`
