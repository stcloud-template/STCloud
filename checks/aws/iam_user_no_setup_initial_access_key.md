# Do not setup access keys during initial user setup for all IAM users that have a console password

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_user_no_setup_initial_access_key` |
| 云平台 | AWS |
| 服务 | iam |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| 资源类型 | AwsIamAccessKey |
| 资源组 | IAM |

## 描述

Do not setup access keys during initial user setup for all IAM users that have a console password

## 风险

AWS console defaults the checkbox for creating access keys to enabled. This results in many access keys being generated unnecessarily. In addition to unnecessary credentials, it also generates unnecessary management work in auditing and rotating these keys. Requiring that additional steps be taken by the user after their profile has been created will give a stronger indication of intent that access keys are (a) necessary for their work and (b) once the access key is established on an account that the keys may be in use somewhere in the organization.

## 推荐措施

From the IAM console: generate credential report and disable not required keys.

- 推荐链接：[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html)

## 技术信息

- Source Metadata：[sources/aws/iam_user_no_setup_initial_access_key/metadata.json](../../sources/aws/iam_user_no_setup_initial_access_key/metadata.json)
- Source Code：[sources/aws/iam_user_no_setup_initial_access_key/check.py](../../sources/aws/iam_user_no_setup_initial_access_key/check.py)
- Source Metadata Path：`sources/aws/iam_user_no_setup_initial_access_key/metadata.json`
- Source Code Path：`sources/aws/iam_user_no_setup_initial_access_key/check.py`
