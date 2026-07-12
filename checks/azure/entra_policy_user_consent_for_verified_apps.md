# Ensure 'User consent for applications' Is Set To 'Allow for Verified Publishers'

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `entra_policy_user_consent_for_verified_apps` |
| クラウドプラットフォーム | Azure |
| サービス | entra |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | #microsoft.graph.authorizationPolicy |
| リソースグループ | IAM |

## 説明

Allow users to provide consent for selected permissions when a request is coming from a verified publisher.

## リスク

If Microsoft Entra ID is running as an identity provider for third-party applications, permissions and consent should be limited to administrators or pre-approved. Malicious applications may attempt to exfiltrate data or abuse privileged user accounts.

## 推奨事項

1. From Azure Home select the Portal Menu 2. Select Microsoft Entra ID 3. Select Enterprise Applications 4. Select Consent and permissions 5. Select User consent settings 6. Under User consent for applications, select Allow user consent for apps from verified publishers, for selected permissions 7. Select Save

- 推奨リンク：[https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-privileged-access#pa-1-separate-and-limit-highly-privilegedadministrative-users](https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-privileged-access#pa-1-separate-and-limit-highly-privilegedadministrative-users)

## 修正手順

No remediation steps available.

## 参考資料

- [https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal#configure-user-consent-to-applications](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal#configure-user-consent-to-applications)
- [https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-privileged-access#pa-1-separate-and-limit-highly-privilegedadministrative-users](https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-privileged-access#pa-1-separate-and-limit-highly-privilegedadministrative-users)

## 技術情報

- Source Metadata：[sources/azure/entra_policy_user_consent_for_verified_apps/metadata.json](../../sources/azure/entra_policy_user_consent_for_verified_apps/metadata.json)
- Source Code：[sources/azure/entra_policy_user_consent_for_verified_apps/check.py](../../sources/azure/entra_policy_user_consent_for_verified_apps/check.py)
- Source Metadata Path：`sources/azure/entra_policy_user_consent_for_verified_apps/metadata.json`
- Source Code Path：`sources/azure/entra_policy_user_consent_for_verified_apps/check.py`
