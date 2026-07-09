# Ensure IAM password policy require at least one lowercase letter

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_password_policy_lowercase` |
| 云平台 | AWS |
| 服务 | iam |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| 资源类型 | Other |
| 资源组 | IAM |

## 描述

Ensure IAM password policy requires at least one uppercase letter

## 风险

Password policies are used to enforce password complexity requirements. IAM password policies can be used to ensure password are comprised of different character sets. It is recommended that the password policy require at least one lowercase letter.

## 推荐措施

Ensure "Requires at least one lowercase letter" is checked under "Password Policy".

- 推荐链接：[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html)

## 技术信息

- Source Metadata：[sources/aws/iam_password_policy_lowercase/metadata.json](../../sources/aws/iam_password_policy_lowercase/metadata.json)
- Source Code：[sources/aws/iam_password_policy_lowercase/check.py](../../sources/aws/iam_password_policy_lowercase/check.py)
- Source Metadata Path：`sources/aws/iam_password_policy_lowercase/metadata.json`
- Source Code Path：`sources/aws/iam_password_policy_lowercase/check.py`
