# Ensure users of groups with AdministratorAccess policy have MFA tokens enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_administrator_access_with_mfa` |
| 云平台 | AWS |
| 服务 | iam |
| 严重等级 | high |
| 类别 | Uncategorized |
| 检查类型 | Infrastructure Security |
| 资源类型 | AwsIamUser |
| 资源组 | IAM |

## 描述

Ensure users of groups with AdministratorAccess policy have MFA tokens enabled

## 风险

Policy may allow Anonymous users to perform actions.

## 推荐措施

Ensure this repository and its contents should be publicly accessible.

- 推荐链接：[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html)

## 技术信息

- Source Metadata：[sources/aws/iam_administrator_access_with_mfa/metadata.json](../../sources/aws/iam_administrator_access_with_mfa/metadata.json)
- Source Code：[sources/aws/iam_administrator_access_with_mfa/check.py](../../sources/aws/iam_administrator_access_with_mfa/check.py)
- Source Metadata Path：`sources/aws/iam_administrator_access_with_mfa/metadata.json`
- Source Code Path：`sources/aws/iam_administrator_access_with_mfa/check.py`
