# Ensure That Microsoft Defender for IoT Hub Is Set To 'On'

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `defender_ensure_iot_hub_defender_is_on` |
| クラウドプラットフォーム | Azure |
| サービス | defender |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | DefenderIoT |
| リソースグループ | security |

## 説明

Microsoft Defender for IoT acts as a central security hub for IoT devices within your organization.

## リスク

IoT devices are very rarely patched and can be potential attack vectors for enterprise networks. Updating their network configuration to use a central security hub allows for detection of these breaches.

## 推奨事項

1. Go to IoT Hub. 2. Select a IoT Hub to validate. 3. Select Overview in Defender for IoT. 4. Click on Secure your IoT solution, and complete the onboarding.

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/defender-for-iot/device-builders/quickstart-onboard-iot-hub](https://learn.microsoft.com/en-us/azure/defender-for-iot/device-builders/quickstart-onboard-iot-hub)

## 修正手順

No remediation steps available.

## 参考資料

- [https://azure.microsoft.com/en-us/services/iot-defender/#overview](https://azure.microsoft.com/en-us/services/iot-defender/#overview)
- [https://learn.microsoft.com/en-us/azure/defender-for-iot/device-builders/quickstart-onboard-iot-hub](https://learn.microsoft.com/en-us/azure/defender-for-iot/device-builders/quickstart-onboard-iot-hub)

## 技術情報

- Source Metadata：[sources/azure/defender_ensure_iot_hub_defender_is_on/metadata.json](../../sources/azure/defender_ensure_iot_hub_defender_is_on/metadata.json)
- Source Code：[sources/azure/defender_ensure_iot_hub_defender_is_on/check.py](../../sources/azure/defender_ensure_iot_hub_defender_is_on/check.py)
- Source Metadata Path：`sources/azure/defender_ensure_iot_hub_defender_is_on/metadata.json`
- Source Code Path：`sources/azure/defender_ensure_iot_hub_defender_is_on/check.py`
