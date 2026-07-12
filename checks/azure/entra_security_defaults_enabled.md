# Ensure Security Defaults is enabled on Microsoft Entra ID

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `entra_security_defaults_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | entra |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | #microsoft.graph.identitySecurityDefaultsEnforcementPolicy |
| リソースグループ | security |

## 説明

Security defaults in Microsoft Entra ID make it easier to be secure and help protect your organization. Security defaults contain preconfigured security settings for common attacks. Security defaults is available to everyone. The goal is to ensure that all organizations have a basic level of security enabled at no extra cost. You may turn on security defaults in the Azure portal.

## リスク

Security defaults provide secure default settings that we manage on behalf of organizations to keep customers safe until they are ready to manage their own identity security settings. For example, doing the following: - Requiring all users and admins to register for MFA. - Challenging users with MFA - when necessary, based on factors such as location, device, role, and task. - Disabling authentication from legacy authentication clients, which can’t do MFA.

## 推奨事項

1. From Azure Home select the Portal Menu. 2. Browse to Microsoft Entra ID > Properties 3. Select Manage security defaults 4. Set the Enable security defaults to Enabled 5. Select Save

- 推奨リンク：[https://techcommunity.microsoft.com/t5/microsoft-entra-blog/introducing-security-defaults/ba-p/1061414](https://techcommunity.microsoft.com/t5/microsoft-entra-blog/introducing-security-defaults/ba-p/1061414)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/ActiveDirectory/security-defaults-enabled.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/ActiveDirectory/security-defaults-enabled.html#)

## 参考資料

- [https://learn.microsoft.com/en-us/entra/fundamentals/security-defaults](https://learn.microsoft.com/en-us/entra/fundamentals/security-defaults)
- [https://techcommunity.microsoft.com/t5/microsoft-entra-blog/introducing-security-defaults/ba-p/1061414](https://techcommunity.microsoft.com/t5/microsoft-entra-blog/introducing-security-defaults/ba-p/1061414)

## 技術情報

- Source Metadata：[sources/azure/entra_security_defaults_enabled/metadata.json](../../sources/azure/entra_security_defaults_enabled/metadata.json)
- Source Code：[sources/azure/entra_security_defaults_enabled/check.py](../../sources/azure/entra_security_defaults_enabled/check.py)
- Source Metadata Path：`sources/azure/entra_security_defaults_enabled/metadata.json`
- Source Code Path：`sources/azure/entra_security_defaults_enabled/check.py`
