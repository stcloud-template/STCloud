# Check if there are SAML Providers then STS can be used

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_check_saml_providers_sts` |
| 云平台 | AWS |
| 服务 | iam |
| 严重等级 | low |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| 资源类型 | Other |
| 资源组 | IAM |

## 描述

Check if there are SAML Providers then STS can be used

## 风险

Without SAML provider users with AWS CLI or AWS API access can use IAM static credentials. SAML helps users to assume role by default each time they authenticate.

## 推荐措施

Enable SAML provider and use temporary credentials. You can use temporary security credentials to make programmatic requests for AWS resources using the AWS CLI or AWS API (using the AWS SDKs ). The temporary credentials provide the same permissions that you have with use long-term security credentials such as IAM user credentials. In case of not having SAML provider capabilities prevent usage of long-lived credentials.

- 推荐链接：[https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithSAML.html](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithSAML.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithSAML.html](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithSAML.html)

## 技术信息

- Source Metadata：[sources/aws/iam_check_saml_providers_sts/metadata.json](../../sources/aws/iam_check_saml_providers_sts/metadata.json)
- Source Code：[sources/aws/iam_check_saml_providers_sts/check.py](../../sources/aws/iam_check_saml_providers_sts/check.py)
- Source Metadata Path：`sources/aws/iam_check_saml_providers_sts/metadata.json`
- Source Code Path：`sources/aws/iam_check_saml_providers_sts/check.py`
