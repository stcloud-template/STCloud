# Ensure IAM policies that allow full "cloudtrail:*" privileges are not created

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_policy_no_full_access_to_cloudtrail` |
| クラウドプラットフォーム | AWS |
| サービス | iam |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| リソースタイプ | AwsIamPolicy |
| リソースグループ | IAM |

## 説明

Ensure IAM policies that allow full "cloudtrail:*" privileges are not created

## リスク

CloudTrail is a critical service and IAM policies should follow least privilege model for this service in particular

## 推奨事項

It is more secure to start with a minimum set of permissions and grant additional permissions as necessary, rather than starting with permissions that are too lenient and then trying to tighten them later. List policies an analyze if permissions are the least possible to conduct business activities.

- 推奨リンク：[http://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html](http://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

## 修正手順

No remediation steps available.

## 参考資料

- [http://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html](http://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

## 技術情報

- Source Metadata：[sources/aws/iam_policy_no_full_access_to_cloudtrail/metadata.json](../../sources/aws/iam_policy_no_full_access_to_cloudtrail/metadata.json)
- Source Code：[sources/aws/iam_policy_no_full_access_to_cloudtrail/check.py](../../sources/aws/iam_policy_no_full_access_to_cloudtrail/check.py)
- Source Metadata Path：`sources/aws/iam_policy_no_full_access_to_cloudtrail/metadata.json`
- Source Code Path：`sources/aws/iam_policy_no_full_access_to_cloudtrail/check.py`
