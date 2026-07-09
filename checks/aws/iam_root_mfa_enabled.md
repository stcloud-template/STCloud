# Ensure MFA is enabled for the root account

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_root_mfa_enabled` |
| 云平台 | AWS |
| 服务 | iam |
| 严重等级 | critical |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| 资源类型 | AwsIamUser |
| 资源组 | IAM |

## 描述

Ensure MFA is enabled for the root account

## 风险

The root account is the most privileged user in an AWS account. MFA adds an extra layer of protection on top of a user name and password. With MFA enabled when a user signs in to an AWS website they will be prompted for their user name and password as well as for an authentication code from their AWS MFA device. When virtual MFA is used for root accounts it is recommended that the device used is NOT a personal device but rather a dedicated mobile device (tablet or phone) that is managed to be kept charged and secured independent of any individual personal devices. (non-personal virtual MFA) This lessens the risks of losing access to the MFA due to device loss / trade-in or if the individual owning the device is no longer employed at the company.

## 推荐措施

Using IAM console navigate to Dashboard and expand Activate MFA on your root account. If using AWS Organizations, consider enabling Centralized Root Management and removing individual root credentials.

- 推荐链接：[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#id_root-user_manage_mfa](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#id_root-user_manage_mfa)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#id_root-user_manage_mfa](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#id_root-user_manage_mfa)

## 技术信息

- Source Metadata：[sources/aws/iam_root_mfa_enabled/metadata.json](../../sources/aws/iam_root_mfa_enabled/metadata.json)
- Source Code：[sources/aws/iam_root_mfa_enabled/check.py](../../sources/aws/iam_root_mfa_enabled/check.py)
- Source Metadata Path：`sources/aws/iam_root_mfa_enabled/metadata.json`
- Source Code Path：`sources/aws/iam_root_mfa_enabled/check.py`
