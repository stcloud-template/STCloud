# Ensure multi-factor authentication (MFA) is enabled for all IAM users that have a console password.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_user_mfa_enabled_console_access` |
| 云平台 | AWS |
| 服务 | iam |
| 严重等级 | high |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| 资源类型 | AwsIamUser |
| 资源组 | IAM |

## 描述

Ensure multi-factor authentication (MFA) is enabled for all IAM users that have a console password.

## 风险

Unauthorized access to this critical account if password is not secure or it is disclosed in any way.

## 推荐措施

Enable MFA for the user's account. MFA is a simple best practice that adds an extra layer of protection on top of your user name and password. Recommended to use hardware keys over virtual MFA.

- 推荐链接：[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html)

## 技术信息

- Source Metadata：[sources/aws/iam_user_mfa_enabled_console_access/metadata.json](../../sources/aws/iam_user_mfa_enabled_console_access/metadata.json)
- Source Code：[sources/aws/iam_user_mfa_enabled_console_access/check.py](../../sources/aws/iam_user_mfa_enabled_console_access/check.py)
- Source Metadata Path：`sources/aws/iam_user_mfa_enabled_console_access/metadata.json`
- Source Code Path：`sources/aws/iam_user_mfa_enabled_console_access/check.py`
