# Ensure that 'Users can create Microsoft 365 groups in Azure portals, API or PowerShell' is set to 'No'

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `entra_users_cannot_create_microsoft_365_groups` |
| クラウドプラットフォーム | Azure |
| サービス | entra |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.Users/Settings |
| リソースグループ | IAM |

## 説明

Restrict Microsoft 365 group creation to administrators only.

## リスク

Restricting Microsoft 365 group creation to administrators only ensures that creation of Microsoft 365 groups is controlled by the administrator. Appropriate groups should be created and managed by the administrator and group creation rights should not be delegated to any other user.

## 推奨事項

1. From Azure Home select the Portal Menu 2. Select Microsoft Entra ID 3. Then Groups 4. Select General in settings 5. Set Users can create Microsoft 365 groups in Azure portals, API or PowerShell to No

- 推奨リンク：[https://learn.microsoft.com/en-us/microsoft-365/solutions/manage-creation-of-groups?view=o365-worldwide&redirectSourcePath=%252fen-us%252farticle%252fControl-who-can-create-Office-365-Groups-4c46c8cb-17d0-44b5-9776-005fced8e618](https://learn.microsoft.com/en-us/microsoft-365/solutions/manage-creation-of-groups?view=o365-worldwide&redirectSourcePath=%252fen-us%252farticle%252fControl-who-can-create-Office-365-Groups-4c46c8cb-17d0-44b5-9776-005fced8e618)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/ActiveDirectory/users-can-create-office-365-groups.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/ActiveDirectory/users-can-create-office-365-groups.html#)

## 参考資料

- [https://learn.microsoft.com/en-us/microsoft-365/community/all-about-groups#microsoft-365-groups](https://learn.microsoft.com/en-us/microsoft-365/community/all-about-groups#microsoft-365-groups)
- [https://learn.microsoft.com/en-us/microsoft-365/solutions/manage-creation-of-groups?view=o365-worldwide&redirectSourcePath=%252fen-us%252farticle%252fControl-who-can-create-Office-365-Groups-4c46c8cb-17d0-44b5-9776-005fced8e618](https://learn.microsoft.com/en-us/microsoft-365/solutions/manage-creation-of-groups?view=o365-worldwide&redirectSourcePath=%252fen-us%252farticle%252fControl-who-can-create-Office-365-Groups-4c46c8cb-17d0-44b5-9776-005fced8e618)

## 技術情報

- Source Metadata：[sources/azure/entra_users_cannot_create_microsoft_365_groups/metadata.json](../../sources/azure/entra_users_cannot_create_microsoft_365_groups/metadata.json)
- Source Code：[sources/azure/entra_users_cannot_create_microsoft_365_groups/check.py](../../sources/azure/entra_users_cannot_create_microsoft_365_groups/check.py)
- Source Metadata Path：`sources/azure/entra_users_cannot_create_microsoft_365_groups/metadata.json`
- Source Code Path：`sources/azure/entra_users_cannot_create_microsoft_365_groups/check.py`
