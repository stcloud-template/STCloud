# Ensure IAM Customer-Managed policies that allow full "*:*" administrative privileges are not attached

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_customer_attached_policy_no_administrative_privileges` |
| クラウドプラットフォーム | AWS |
| サービス | iam |
| 重大度 | high |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| リソースタイプ | AwsIamPolicy |
| リソースグループ | IAM |

## 説明

Ensure IAM Customer-Managed policies that allow full "*:*" administrative privileges are not attached

## リスク

IAM policies are the means by which privileges are granted to users, groups, or roles. It is recommended and considered a standard security advice to grant least privilege—that is, granting only the permissions required to perform a task. Determine what users need to do and then craft policies for them that let the users perform only those tasks instead of allowing full administrative privileges. Providing full administrative privileges instead of restricting to the minimum set of permissions that the user is required to do exposes the resources to potentially unwanted actions.

## 推奨事項

It is more secure to start with a minimum set of permissions and grant additional permissions as necessary, rather than starting with permissions that are too lenient and then trying to tighten them later. List policies an analyze if permissions are the least possible to conduct business activities.

- 推奨リンク：[http://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html](http://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/aws/iam-policies/iam_47#terraform](https://docs.ST Cloud.com/checks/aws/iam-policies/iam_47#terraform)

### Other

[https://docs.ST Cloud.com/checks/aws/iam-policies/iam_47](https://docs.ST Cloud.com/checks/aws/iam-policies/iam_47)

## 参考資料

- [http://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html](http://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

## 技術情報

- Source Metadata：[sources/aws/iam_customer_attached_policy_no_administrative_privileges/metadata.json](../../sources/aws/iam_customer_attached_policy_no_administrative_privileges/metadata.json)
- Source Code：[sources/aws/iam_customer_attached_policy_no_administrative_privileges/check.py](../../sources/aws/iam_customer_attached_policy_no_administrative_privileges/check.py)
- Source Metadata Path：`sources/aws/iam_customer_attached_policy_no_administrative_privileges/metadata.json`
- Source Code Path：`sources/aws/iam_customer_attached_policy_no_administrative_privileges/check.py`
