# Ensure that 'Multi-Factor Auth Status' is 'Enabled' for all Non-Privileged Users

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `entra_non_privileged_user_has_mfa` |
| クラウドプラットフォーム | Azure |
| サービス | entra |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | #microsoft.graph.users |
| リソースグループ | IAM |

## 説明

Enable multi-factor authentication for all non-privileged users.

## リスク

Multi-factor authentication requires an individual to present a minimum of two separate forms of authentication before access is granted. Multi-factor authentication provides additional assurance that the individual attempting to gain access is who they claim to be. With multi-factor authentication, an attacker would need to compromise at least two different authentication mechanisms, increasing the difficulty of compromise and thus reducing the risk.

## 推奨事項

Activate one of the available multi-factor authentication methods for users in Microsoft Entra ID.

- 推奨リンク：[https://learn.microsoft.com/en-us/entra/identity/authentication/tutorial-enable-azure-mfa](https://learn.microsoft.com/en-us/entra/identity/authentication/tutorial-enable-azure-mfa)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/ActiveDirectory/multi-factor-authentication-for-all-non-privileged-users.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/ActiveDirectory/multi-factor-authentication-for-all-non-privileged-users.html#)

## 参考資料

- [https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mfa-howitworks](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mfa-howitworks)
- [https://learn.microsoft.com/en-us/entra/identity/authentication/tutorial-enable-azure-mfa](https://learn.microsoft.com/en-us/entra/identity/authentication/tutorial-enable-azure-mfa)

## 技術情報

- Source Metadata：[sources/azure/entra_non_privileged_user_has_mfa/metadata.json](../../sources/azure/entra_non_privileged_user_has_mfa/metadata.json)
- Source Code：[sources/azure/entra_non_privileged_user_has_mfa/check.py](../../sources/azure/entra_non_privileged_user_has_mfa/check.py)
- Source Metadata Path：`sources/azure/entra_non_privileged_user_has_mfa/metadata.json`
- Source Code Path：`sources/azure/entra_non_privileged_user_has_mfa/check.py`
