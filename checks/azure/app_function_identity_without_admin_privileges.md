# Ensure that your Azure functions are not configured with an identity with admin privileges

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `app_function_identity_without_admin_privileges` |
| クラウドプラットフォーム | Azure |
| サービス | app |
| サブサービス | function |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.Web/sites |
| リソースグループ | serverless |

## 説明

It is important to ensure that Azure functions are not configured with administrative privileges to maintain the principle of least privilege and reduce the attack surface. By limiting the privileges of Azure functions, potential security risks and data leaks can be mitigated.

## リスク

If Azure functions are configured with administrative privileges, it increases the risk of unauthorized access, privilege escalation, and data breaches. Attackers can exploit these privileges to gain access to sensitive data and compromise the entire system.

## 推奨事項

To remediate this issue, ensure that Azure functions are not configured with an identity that has administrative privileges. Instead, use the principle of least privilege to grant only the necessary permissions to Azure functions. For more information, refer to the official documentation: Use the principle of least privilege.

- 推奨リンク：[https://docs.microsoft.com/en-us/azure/architecture/framework/security/design-identity-authorization#use-the-principle-of-least-privilege](https://docs.microsoft.com/en-us/azure/architecture/framework/security/design-identity-authorization#use-the-principle-of-least-privilege)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Functions/azure-function-admin-permissions.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Functions/azure-function-admin-permissions.html)

## 参考資料

- [https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview)
- [https://docs.microsoft.com/en-us/azure/architecture/framework/security/design-identity-authorization#use-the-principle-of-least-privilege](https://docs.microsoft.com/en-us/azure/architecture/framework/security/design-identity-authorization#use-the-principle-of-least-privilege)

## 技術情報

- Source Metadata：[sources/azure/app_function_identity_without_admin_privileges/metadata.json](../../sources/azure/app_function_identity_without_admin_privileges/metadata.json)
- Source Code：[sources/azure/app_function_identity_without_admin_privileges/check.py](../../sources/azure/app_function_identity_without_admin_privileges/check.py)
- Source Metadata Path：`sources/azure/app_function_identity_without_admin_privileges/metadata.json`
- Source Code Path：`sources/azure/app_function_identity_without_admin_privileges/check.py`
