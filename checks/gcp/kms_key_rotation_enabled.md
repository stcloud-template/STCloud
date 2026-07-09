# Ensure KMS keys are rotated within a period of 90 days

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `kms_key_rotation_enabled` |
| 云平台 | GCP |
| 服务 | kms |
| 严重等级 | low |
| 类别 | Uncategorized |
| 资源类型 | CryptoKey |
| 资源组 | security |

## 描述

Ensure KMS keys are rotated within a period of 90 days

## 风险

Ensure that all your Cloud Key Management Service (KMS) keys are rotated within a period of 90 days in order to meet security and compliance requirements

## 推荐措施

After a successful key rotation, the older key version is required in order to decrypt the data encrypted by that previous key version.

- 推荐链接：[https://cloud.google.com/iam/docs/manage-access-service-accounts](https://cloud.google.com/iam/docs/manage-access-service-accounts)

## 修复步骤


### CLI

```text
gcloud kms keys update new --keyring=<KEY_RING> --location=<LOCATION> --nextrotation-time=<NEXT_ROTATION_TIME> --rotation-period=<ROTATION_PERIOD>
```

### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-general-policies/bc_gcp_general_4#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-general-policies/bc_gcp_general_4#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudKMS/rotate-kms-encryption-keys.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudKMS/rotate-kms-encryption-keys.html)

## 参考资料

- [https://cloud.google.com/iam/docs/manage-access-service-accounts](https://cloud.google.com/iam/docs/manage-access-service-accounts)

## 技术信息

- Source Metadata：[sources/gcp/kms_key_rotation_enabled/metadata.json](../../sources/gcp/kms_key_rotation_enabled/metadata.json)
- Source Code：[sources/gcp/kms_key_rotation_enabled/check.py](../../sources/gcp/kms_key_rotation_enabled/check.py)
- Source Metadata Path：`sources/gcp/kms_key_rotation_enabled/metadata.json`
- Source Code Path：`sources/gcp/kms_key_rotation_enabled/check.py`
