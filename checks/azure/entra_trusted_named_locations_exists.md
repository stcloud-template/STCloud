# Ensure Trusted Locations Are Defined

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `entra_trusted_named_locations_exists` |
| クラウドプラットフォーム | Azure |
| サービス | entra |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | #microsoft.graph.ipNamedLocation |
| リソースグループ | network |

## 説明

Microsoft Entra ID Conditional Access allows an organization to configure Named locations and configure whether those locations are trusted or untrusted. These settings provide organizations the means to specify Geographical locations for use in conditional access policies, or define actual IP addresses and IP ranges and whether or not those IP addresses and/or ranges are trusted by the organization.

## リスク

Defining trusted source IP addresses or ranges helps organizations create and enforce Conditional Access policies around those trusted or untrusted IP addresses and ranges. Users authenticating from trusted IP addresses and/or ranges may have less access restrictions or access requirements when compared to users that try to authenticate to Microsoft Entra ID from untrusted locations or untrusted source IP addresses/ranges.

## 推奨事項

1. Navigate to the Microsoft Entra ID Conditional Access Blade 2. Click on the Named locations blade 3. Within the Named locations blade, click on IP ranges location 4. Enter a name for this location setting in the Name text box 5. Click on the + sign 6. Add an IP Address Range in CIDR notation inside the text box that appears 7. Click on the Add button 8. Repeat steps 5 through 7 for each IP Range that needs to be added 9. If the information entered are trusted ranges, select the Mark as trusted location check box 10. Once finished, click on Create

- 推奨リンク：[https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-identity-management#im-7-restrict-resource-access-based-on--conditions](https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-identity-management#im-7-restrict-resource-access-based-on--conditions)

## 修正手順

No remediation steps available.

## 参考資料

- [https://learn.microsoft.com/en-us/entra/identity/conditional-access/location-condition](https://learn.microsoft.com/en-us/entra/identity/conditional-access/location-condition)
- [https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-identity-management#im-7-restrict-resource-access-based-on--conditions](https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-identity-management#im-7-restrict-resource-access-based-on--conditions)

## 技術情報

- Source Metadata：[sources/azure/entra_trusted_named_locations_exists/metadata.json](../../sources/azure/entra_trusted_named_locations_exists/metadata.json)
- Source Code：[sources/azure/entra_trusted_named_locations_exists/check.py](../../sources/azure/entra_trusted_named_locations_exists/check.py)
- Source Metadata Path：`sources/azure/entra_trusted_named_locations_exists/metadata.json`
- Source Code Path：`sources/azure/entra_trusted_named_locations_exists/check.py`
