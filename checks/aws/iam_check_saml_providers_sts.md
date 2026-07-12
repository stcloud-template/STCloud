# Check if there are SAML Providers then STS can be used

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_check_saml_providers_sts` |
| クラウドプラットフォーム | AWS |
| サービス | iam |
| 重大度 | low |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| リソースタイプ | Other |
| リソースグループ | IAM |

## 説明

Check if there are SAML Providers then STS can be used

## リスク

Without SAML provider users with AWS CLI or AWS API access can use IAM static credentials. SAML helps users to assume role by default each time they authenticate.

## 推奨事項

Enable SAML provider and use temporary credentials. You can use temporary security credentials to make programmatic requests for AWS resources using the AWS CLI or AWS API (using the AWS SDKs ). The temporary credentials provide the same permissions that you have with use long-term security credentials such as IAM user credentials. In case of not having SAML provider capabilities prevent usage of long-lived credentials.

- 推奨リンク：[https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithSAML.html](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithSAML.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithSAML.html](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithSAML.html)

## 技術情報

- Source Metadata：[sources/aws/iam_check_saml_providers_sts/metadata.json](../../sources/aws/iam_check_saml_providers_sts/metadata.json)
- Source Code：[sources/aws/iam_check_saml_providers_sts/check.py](../../sources/aws/iam_check_saml_providers_sts/check.py)
- Source Metadata Path：`sources/aws/iam_check_saml_providers_sts/metadata.json`
- Source Code Path：`sources/aws/iam_check_saml_providers_sts/check.py`
