# Ensure no root account access key exists

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_no_root_access_key` |
| 云平台 | AWS |
| 服务 | iam |
| 严重等级 | critical |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| 资源类型 | AwsIamAccessKey |
| 资源组 | IAM |

## 描述

Ensure no root account access key exists

## 风险

The root account is the most privileged user in an AWS account. AWS Access Keys provide programmatic access to a given AWS account. It is recommended that all access keys associated with the root account be removed. Removing access keys associated with the root account limits vectors by which the account can be compromised. Removing the root access keys encourages the creation and use of role based accounts that are least privileged.

## 推荐措施

Use the credential report to check the user and ensure the access_key_1_active and access_key_2_active fields are set to FALSE. If using AWS Organizations, consider enabling Centralized Root Management and removing individual root credentials.

- 推荐链接：[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html)

## 技术信息

- Source Metadata：[sources/aws/iam_no_root_access_key/metadata.json](../../sources/aws/iam_no_root_access_key/metadata.json)
- Source Code：[sources/aws/iam_no_root_access_key/check.py](../../sources/aws/iam_no_root_access_key/check.py)
- Source Metadata Path：`sources/aws/iam_no_root_access_key/metadata.json`
- Source Code Path：`sources/aws/iam_no_root_access_key/check.py`
