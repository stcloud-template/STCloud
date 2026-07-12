# Ensure no Customer Managed IAM policies allow actions that may lead into Privilege Escalation

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_policy_allows_privilege_escalation` |
| クラウドプラットフォーム | AWS |
| サービス | iam |
| 重大度 | high |
| カテゴリ | privilege-escalation |
| チェックタイプ | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| リソースタイプ | AwsIamPolicy |
| リソースグループ | IAM |

## 説明

Ensure no Customer Managed IAM policies allow actions that may lead into Privilege Escalation

## リスク

Users with some IAM permissions are allowed to elevate their privileges up to administrator rights.

## 推奨事項

Grant usage permission on a per-resource basis and applying least privilege principle.

- 推奨リンク：[https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege)

## 技術情報

- Source Metadata：[sources/aws/iam_policy_allows_privilege_escalation/metadata.json](../../sources/aws/iam_policy_allows_privilege_escalation/metadata.json)
- Source Code：[sources/aws/iam_policy_allows_privilege_escalation/check.py](../../sources/aws/iam_policy_allows_privilege_escalation/check.py)
- Source Metadata Path：`sources/aws/iam_policy_allows_privilege_escalation/metadata.json`
- Source Code Path：`sources/aws/iam_policy_allows_privilege_escalation/check.py`
