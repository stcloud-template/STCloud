# Ensure a Security Audit role has been created to conduct security audits

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_securityaudit_role_created` |
| クラウドプラットフォーム | AWS |
| サービス | iam |
| 重大度 | low |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| リソースタイプ | AwsIamRole |
| リソースグループ | IAM |

## 説明

Ensure a Security Audit role has been created to conduct security audits

## リスク

Creating an IAM role with a security audit policy provides a clear separation of duties between the security team and other teams within the organization. This helps to ensure that security-related activities are performed by authorized individuals with the appropriate expertise and access permissions.

## 推奨事項

Create an IAM role for conduct security audits with AWS.

- 推奨リンク：[https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_security-auditor](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_security-auditor)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_security-auditor](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_security-auditor)

## 技術情報

- Source Metadata：[sources/aws/iam_securityaudit_role_created/metadata.json](../../sources/aws/iam_securityaudit_role_created/metadata.json)
- Source Code：[sources/aws/iam_securityaudit_role_created/check.py](../../sources/aws/iam_securityaudit_role_created/check.py)
- Source Metadata Path：`sources/aws/iam_securityaudit_role_created/metadata.json`
- Source Code Path：`sources/aws/iam_securityaudit_role_created/check.py`
