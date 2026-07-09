# Enforce Separation of Duties for KMS-Related Roles

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_role_kms_enforce_separation_of_duties` |
| 云平台 | GCP |
| 服务 | iam |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | IAMRole |
| 资源组 | IAM |

## 描述

Ensure that separation of duties is enforced for all Cloud Key Management Service (KMS) related roles. The principle of separation of duties (also known as segregation of duties) has as its primary objective the prevention of fraud and human error. This objective is achieved by dismantling the tasks and the associated privileges for a specific business process among multiple users/identities. Google Cloud provides predefined roles that can be used to implement the principle of separation of duties, where it is needed. The predefined Cloud KMS Admin role is meant for users to manage KMS keys but not to use them. The Cloud KMS CryptoKey Encrypter/Decrypter roles are meant for services who can use keys to encrypt and decrypt data, but not to manage them. To adhere to cloud security best practices, your IAM users should not have the Admin role and any of the CryptoKey Encrypter/Decrypter roles assigned at the same time.

## 风险

The principle of separation of duties can be enforced in order to eliminate the need for the IAM user/identity that has all the permissions needed to perform unwanted actions, such as using a cryptographic key to access and decrypt data which the user should not normally have access to.

## 推荐措施

It is recommended that the principle of 'Separation of Duties' is enforced while assigning KMS related roles to users.

- 推荐链接：[https://cloud.google.com/kms/docs/separation-of-duties](https://cloud.google.com/kms/docs/separation-of-duties)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudIAM/enforce-separation-of-duties-for-kms-related-roles.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudIAM/enforce-separation-of-duties-for-kms-related-roles.html)

## 参考资料

- [https://cloud.google.com/kms/docs/separation-of-duties](https://cloud.google.com/kms/docs/separation-of-duties)

## 技术信息

- Source Metadata：[sources/gcp/iam_role_kms_enforce_separation_of_duties/metadata.json](../../sources/gcp/iam_role_kms_enforce_separation_of_duties/metadata.json)
- Source Code：[sources/gcp/iam_role_kms_enforce_separation_of_duties/check.py](../../sources/gcp/iam_role_kms_enforce_separation_of_duties/check.py)
- Source Metadata Path：`sources/gcp/iam_role_kms_enforce_separation_of_duties/metadata.json`
- Source Code Path：`sources/gcp/iam_role_kms_enforce_separation_of_duties/check.py`
