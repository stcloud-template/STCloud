# Ensure a support role has been created to manage incidents with AWS Support

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_support_role_created` |
| クラウドプラットフォーム | AWS |
| サービス | iam |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| リソースタイプ | AwsIamRole |
| リソースグループ | IAM |

## 説明

Ensure a support role has been created to manage incidents with AWS Support

## リスク

AWS provides a support center that can be used for incident notification and response, as well as technical support and customer services. Create an IAM Role to allow authorized users to manage incidents with AWS Support.

## 推奨事項

Create an IAM role for managing incidents with AWS.

- 推奨リンク：[https://docs.aws.amazon.com/awssupport/latest/user/using-service-linked-roles-sup.html](https://docs.aws.amazon.com/awssupport/latest/user/using-service-linked-roles-sup.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/awssupport/latest/user/using-service-linked-roles-sup.html](https://docs.aws.amazon.com/awssupport/latest/user/using-service-linked-roles-sup.html)

## 技術情報

- Source Metadata：[sources/aws/iam_support_role_created/metadata.json](../../sources/aws/iam_support_role_created/metadata.json)
- Source Code：[sources/aws/iam_support_role_created/check.py](../../sources/aws/iam_support_role_created/check.py)
- Source Metadata Path：`sources/aws/iam_support_role_created/metadata.json`
- Source Code Path：`sources/aws/iam_support_role_created/check.py`
