# Check if IAM users have Hardware MFA enabled.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_user_hardware_mfa_enabled` |
| 云平台 | AWS |
| 服务 | iam |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| 资源类型 | AwsIamUser |
| 资源组 | IAM |

## 描述

Check if IAM users have Hardware MFA enabled.

## 风险

Hardware MFA is preferred over virtual MFA.

## 推荐措施

Enable hardware MFA device for an IAM user from the AWS Management Console, the command line, or the IAM API.

- 推荐链接：[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_physical.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_physical.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_physical.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_physical.html)

## 技术信息

- Source Metadata：[sources/aws/iam_user_hardware_mfa_enabled/metadata.json](../../sources/aws/iam_user_hardware_mfa_enabled/metadata.json)
- Source Code：[sources/aws/iam_user_hardware_mfa_enabled/check.py](../../sources/aws/iam_user_hardware_mfa_enabled/check.py)
- Source Metadata Path：`sources/aws/iam_user_hardware_mfa_enabled/metadata.json`
- Source Code Path：`sources/aws/iam_user_hardware_mfa_enabled/check.py`
