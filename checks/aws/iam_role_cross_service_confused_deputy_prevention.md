# Ensure IAM Service Roles prevents against a cross-service confused deputy attack

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_role_cross_service_confused_deputy_prevention` |
| クラウドプラットフォーム | AWS |
| サービス | iam |
| 重大度 | high |
| カテゴリ | trust-boundaries |
| リソースタイプ | AwsIamRole |
| リソースグループ | IAM |

## 説明

Ensure IAM Service Roles prevents against a cross-service confused deputy attack

## リスク

Allow attackers to gain unauthorized access to resources

## 推奨事項

To mitigate cross-service confused deputy attacks, it's recommended to use the aws:SourceArn and aws:SourceAccount global condition context keys in your IAM role trust policies. If the role doesn't support these fields, consider implementing alternative security measures, such as defining more restrictive resource-based policies or using service-specific trust policies, to limit the role's permissions and exposure. For detailed guidance, refer to AWS's documentation on preventing cross-service confused deputy issues.

- 推奨リンク：[https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html#cross-service-confused-deputy-prevention](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html#cross-service-confused-deputy-prevention)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html#cross-service-confused-deputy-prevention](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html#cross-service-confused-deputy-prevention)

## 技術情報

- Source Metadata：[sources/aws/iam_role_cross_service_confused_deputy_prevention/metadata.json](../../sources/aws/iam_role_cross_service_confused_deputy_prevention/metadata.json)
- Source Code：[sources/aws/iam_role_cross_service_confused_deputy_prevention/check.py](../../sources/aws/iam_role_cross_service_confused_deputy_prevention/check.py)
- Source Metadata Path：`sources/aws/iam_role_cross_service_confused_deputy_prevention/metadata.json`
- Source Code Path：`sources/aws/iam_role_cross_service_confused_deputy_prevention/check.py`
