# Ensure Automatic Key Rotation is Enabled Within Azure Key Vault for the Supported Services

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `keyvault_key_rotation_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | keyvault |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | KeyVault |
| リソースグループ | security |

## 説明

Automatic Key Rotation is available in Public Preview. The currently supported applications are Key Vault, Managed Disks, and Storage accounts accessing keys within Key Vault. The number of supported applications will incrementally increased.

## リスク

Once set up, Automatic Private Key Rotation removes the need for manual administration when keys expire at intervals determined by your organization's policy. The recommended key lifetime is 2 years. Your organization should determine its own key expiration policy.

## 推奨事項

Note: Azure CLI and Powershell use ISO8601 flags to input timespans. Every timespan input will be in the format P<timespanInISO8601Format>(Y,M,D). The leading P is required with it denoting period. The (Y,M,D) are for the duration of Year, Month,and Day respectively. A time frame of 2 years, 2 months, 2 days would be (P2Y2M2D). From Azure Portal 1. From Azure Portal select the Portal Menu in the top left. 2. Select Key Vaults. 3. Select a Key Vault to audit. 4. Under Objects select Keys. 5. Select a key to audit. 6. In the top row select Rotation policy. 7. Select an Expiry time. 8. Set Enable auto rotation to Enabled. 9. Set an appropriate Rotation option and Rotation time. 10. Optionally set the Notification time. 11. Select Save. 12. Repeat steps 3-11 for each Key Vault and Key. From PowerShell Run the following command for each key to update its policy: Set-AzKeyVaultKeyRotationPolicy -VaultName test-kv -Name test-key -PolicyPath rotation_policy.json

- 推奨リンク：[https://docs.microsoft.com/en-us/azure/storage/common/customer-managed-keys-overview#update-the-key-version](https://docs.microsoft.com/en-us/azure/storage/common/customer-managed-keys-overview#update-the-key-version)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.microsoft.com/en-us/azure/key-vault/keys/how-to-configure-key-rotation](https://docs.microsoft.com/en-us/azure/key-vault/keys/how-to-configure-key-rotation)
- [https://docs.microsoft.com/en-us/azure/storage/common/customer-managed-keys-overview#update-the-key-version](https://docs.microsoft.com/en-us/azure/storage/common/customer-managed-keys-overview#update-the-key-version)

## 技術情報

- Source Metadata：[sources/azure/keyvault_key_rotation_enabled/metadata.json](../../sources/azure/keyvault_key_rotation_enabled/metadata.json)
- Source Code：[sources/azure/keyvault_key_rotation_enabled/check.py](../../sources/azure/keyvault_key_rotation_enabled/check.py)
- Source Metadata Path：`sources/azure/keyvault_key_rotation_enabled/metadata.json`
- Source Code Path：`sources/azure/keyvault_key_rotation_enabled/check.py`
