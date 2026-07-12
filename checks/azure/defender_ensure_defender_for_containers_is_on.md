# Ensure That Microsoft Defender for Containers Is Set To 'On'

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `defender_ensure_defender_for_containers_is_on` |
| クラウドプラットフォーム | Azure |
| サービス | defender |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | AzureDefenderPlan |
| リソースグループ | security |

## 説明

Ensure That Microsoft Defender for Containers Is Set To 'On'

## リスク

Ensure that Microsoft Defender for Cloud is enabled for all your Azure containers. Turning on the Defender for Cloud service enables threat detection for containers, providing threat intelligence, anomaly detection, and behavior analytics.

## 推奨事項

By default, Microsoft Defender for Cloud is not enabled for your Azure cloud containers. Enabling the Defender security service for Azure containers allows for advanced security defense against threats, using threat detection capabilities provided by the Microsoft Security Response Center (MSRC).

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-azure-defender-is-set-to-on-for-container-registries#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-azure-defender-is-set-to-on-for-container-registries#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/defender-container.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/defender-container.html)

## 参考資料

No external references available.

## 技術情報

- Source Metadata：[sources/azure/defender_ensure_defender_for_containers_is_on/metadata.json](../../sources/azure/defender_ensure_defender_for_containers_is_on/metadata.json)
- Source Code：[sources/azure/defender_ensure_defender_for_containers_is_on/check.py](../../sources/azure/defender_ensure_defender_for_containers_is_on/check.py)
- Source Metadata Path：`sources/azure/defender_ensure_defender_for_containers_is_on/metadata.json`
- Source Code Path：`sources/azure/defender_ensure_defender_for_containers_is_on/check.py`
