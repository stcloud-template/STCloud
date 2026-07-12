# Ensure That Microsoft Defender for Servers Is Set to 'On'

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `defender_ensure_defender_for_server_is_on` |
| クラウドプラットフォーム | Azure |
| サービス | defender |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | AzureDefenderPlan |
| リソースグループ | security |

## 説明

Ensure That Microsoft Defender for Servers Is Set to 'On'

## リスク

Turning on Microsoft Defender for Servers enables threat detection for Servers, providing threat intelligence, anomaly detection, and behavior analytics in the Microsoft Defender for Cloud.

## 推奨事項

Enabling Microsoft Defender for Cloud standard pricing tier allows for better security assessment with threat detection provided by the Microsoft Security Response Center (MSRC), advanced security policies, adaptive application control, network threat detection, and regulatory compliance management.

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-azure-defender-is-set-to-on-for-servers#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-azure-defender-is-set-to-on-for-servers#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/microsoft-defender-vm-server.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/microsoft-defender-vm-server.html)

## 参考資料

No external references available.

## 技術情報

- Source Metadata：[sources/azure/defender_ensure_defender_for_server_is_on/metadata.json](../../sources/azure/defender_ensure_defender_for_server_is_on/metadata.json)
- Source Code：[sources/azure/defender_ensure_defender_for_server_is_on/check.py](../../sources/azure/defender_ensure_defender_for_server_is_on/check.py)
- Source Metadata Path：`sources/azure/defender_ensure_defender_for_server_is_on/metadata.json`
- Source Code Path：`sources/azure/defender_ensure_defender_for_server_is_on/check.py`
