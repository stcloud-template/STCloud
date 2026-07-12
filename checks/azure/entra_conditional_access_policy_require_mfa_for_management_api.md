# Ensure Multifactor Authentication is Required for Windows Azure Service Management API

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `entra_conditional_access_policy_require_mfa_for_management_api` |
| クラウドプラットフォーム | Azure |
| サービス | entra |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | #microsoft.graph.conditionalAccess |
| リソースグループ | IAM |

## 説明

This recommendation ensures that users accessing the Windows Azure Service Management API (i.e. Azure Powershell, Azure CLI, Azure Resource Manager API, etc.) are required to use multifactor authentication (MFA) credentials when accessing resources through the Windows Azure Service Management API.

## リスク

Administrative access to the Windows Azure Service Management API should be secured with a higher level of scrutiny to authenticating mechanisms. Enabling multifactor authentication is recommended to reduce the potential for abuse of Administrative actions, and to prevent intruders or compromised admin credentials from changing administrative settings.

## 推奨事項

1. From the Azure Admin Portal dashboard, open Microsoft Entra ID. 2. Click Security in the Entra ID blade. 3. Click Conditional Access in the Security blade. 4. Click Policies in the Conditional Access blade. 5. Click + New policy. 6. Enter a name for the policy. 7. Click the blue text under Users. 8. Under Include, select All users. 9. Under Exclude, check Users and groups. 10. Select users or groups to be exempted from this policy (e.g. break-glass emergency accounts, and non-interactive service accounts) then click the Select button. 11. Click the blue text under Target Resources. 12. Under Include, click the Select apps radio button. 13. Click the blue text under Select. 14. Check the box next to Windows Azure Service Management APIs then click the Select button. 15. Click the blue text under Grant. 16. Under Grant access check the box for Require multifactor authentication then click the Select button. 17. Before creating, set Enable policy to Report-only. 18. Click Create. After testing the policy in report-only mode, update the Enable policy setting from Report-only to On.

- 推奨リンク：[https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-cloud-apps](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-cloud-apps)

## 修正手順

No remediation steps available.

## 参考資料

- [https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-policy-azure-management](https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-policy-azure-management)
- [https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-cloud-apps](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-cloud-apps)

## 技術情報

- Source Metadata：[sources/azure/entra_conditional_access_policy_require_mfa_for_management_api/metadata.json](../../sources/azure/entra_conditional_access_policy_require_mfa_for_management_api/metadata.json)
- Source Code：[sources/azure/entra_conditional_access_policy_require_mfa_for_management_api/check.py](../../sources/azure/entra_conditional_access_policy_require_mfa_for_management_api/check.py)
- Source Metadata Path：`sources/azure/entra_conditional_access_policy_require_mfa_for_management_api/metadata.json`
- Source Code Path：`sources/azure/entra_conditional_access_policy_require_mfa_for_management_api/check.py`
