# Ensure That Microsoft Defender for IoT Hub Is Set To 'On'

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `defender_ensure_iot_hub_defender_is_on` |
| 云平台 | Azure |
| 服务 | defender |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | DefenderIoT |
| 资源组 | security |

## 描述

Microsoft Defender for IoT acts as a central security hub for IoT devices within your organization.

## 风险

IoT devices are very rarely patched and can be potential attack vectors for enterprise networks. Updating their network configuration to use a central security hub allows for detection of these breaches.

## 推荐措施

1. Go to IoT Hub. 2. Select a IoT Hub to validate. 3. Select Overview in Defender for IoT. 4. Click on Secure your IoT solution, and complete the onboarding.

- 推荐链接：[https://learn.microsoft.com/en-us/azure/defender-for-iot/device-builders/quickstart-onboard-iot-hub](https://learn.microsoft.com/en-us/azure/defender-for-iot/device-builders/quickstart-onboard-iot-hub)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://azure.microsoft.com/en-us/services/iot-defender/#overview](https://azure.microsoft.com/en-us/services/iot-defender/#overview)
- [https://learn.microsoft.com/en-us/azure/defender-for-iot/device-builders/quickstart-onboard-iot-hub](https://learn.microsoft.com/en-us/azure/defender-for-iot/device-builders/quickstart-onboard-iot-hub)

## 技术信息

- Source Metadata：[sources/azure/defender_ensure_iot_hub_defender_is_on/metadata.json](../../sources/azure/defender_ensure_iot_hub_defender_is_on/metadata.json)
- Source Code：[sources/azure/defender_ensure_iot_hub_defender_is_on/check.py](../../sources/azure/defender_ensure_iot_hub_defender_is_on/check.py)
- Source Metadata Path：`sources/azure/defender_ensure_iot_hub_defender_is_on/metadata.json`
- Source Code Path：`sources/azure/defender_ensure_iot_hub_defender_is_on/check.py`
