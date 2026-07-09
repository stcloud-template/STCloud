# Ensure access keys are rotated every 90 days or less

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_rotate_access_key_90_days` |
| 云平台 | AWS |
| 服务 | iam |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| 资源类型 | AwsIamAccessKey |
| 资源组 | IAM |

## 描述

Ensure access keys are rotated every 90 days or less

## 风险

Access keys consist of an access key ID and secret access key which are used to sign programmatic requests that you make to AWS. AWS users need their own access keys to make programmatic calls to AWS from the AWS Command Line Interface (AWS CLI)- Tools for Windows PowerShell- the AWS SDKs- or direct HTTP calls using the APIs for individual AWS services. It is recommended that all access keys be regularly rotated.

## 推荐措施

Use the credential report to ensure access_key_X_last_rotated is less than 90 days ago.

- 推荐链接：[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html)

## 技术信息

- Source Metadata：[sources/aws/iam_rotate_access_key_90_days/metadata.json](../../sources/aws/iam_rotate_access_key_90_days/metadata.json)
- Source Code：[sources/aws/iam_rotate_access_key_90_days/check.py](../../sources/aws/iam_rotate_access_key_90_days/check.py)
- Source Metadata Path：`sources/aws/iam_rotate_access_key_90_days/metadata.json`
- Source Code Path：`sources/aws/iam_rotate_access_key_90_days/check.py`
