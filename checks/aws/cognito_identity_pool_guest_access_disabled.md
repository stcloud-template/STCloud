# Ensure Cognito Identity Pool has guest access disabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cognito_identity_pool_guest_access_disabled` |
| クラウドプラットフォーム | AWS |
| サービス | cognito |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | Other |
| リソースグループ | IAM |

## 説明

Guest access allows unauthenticated users to access your identity pool. This is useful for public websites that allow users to sign in with a social identity provider, but it can also be a security risk. If you don't need guest access, you should disable it.

## リスク

If guest access is enabled, unauthenticated users can access your identity pool. This can be a security risk if you don't need guest access.

## 推奨事項

Gues access should be disabled for Cognito Identity Pool. To disable guest access, follow the steps in the Amazon Cognito documentation.

- 推奨リンク：[https://docs.aws.amazon.com/location/latest/developerguide/authenticating-using-cognito.html](https://docs.aws.amazon.com/location/latest/developerguide/authenticating-using-cognito.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/location/latest/developerguide/authenticating-using-cognito.html](https://docs.aws.amazon.com/location/latest/developerguide/authenticating-using-cognito.html)

## 技術情報

- Source Metadata：[sources/aws/cognito_identity_pool_guest_access_disabled/metadata.json](../../sources/aws/cognito_identity_pool_guest_access_disabled/metadata.json)
- Source Code：[sources/aws/cognito_identity_pool_guest_access_disabled/check.py](../../sources/aws/cognito_identity_pool_guest_access_disabled/check.py)
- Source Metadata Path：`sources/aws/cognito_identity_pool_guest_access_disabled/metadata.json`
- Source Code Path：`sources/aws/cognito_identity_pool_guest_access_disabled/check.py`
