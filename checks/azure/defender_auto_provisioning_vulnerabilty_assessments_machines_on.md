# Ensure that Auto provisioning of 'Vulnerability assessment for machines' is Set to 'On'

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `defender_auto_provisioning_vulnerabilty_assessments_machines_on` |
| 云平台 | Azure |
| 服务 | defender |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AzureDefenderPlan |
| 资源组 | security |

## 描述

Enable automatic provisioning of vulnerability assessment for machines on both Azure and hybrid (Arc enabled) machines.

## 风险

Vulnerability assessment for machines scans for various security-related configurations and events such as system updates, OS vulnerabilities, and endpoint protection, then produces alerts on threat and vulnerability findings.

## 推荐措施

1. From Azure Home select the Portal Menu. 2. Select Microsoft Defender for Cloud. 3. Then Environment Settings. 4. Select a subscription. 5. Click on Settings & Monitoring. 6. Ensure that Vulnerability assessment for machines is set to On. Repeat this for any additional subscriptions.

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/automatic-provisioning-vulnerability-assessment-machines.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/automatic-provisioning-vulnerability-assessment-machines.html)

## 参考资料

- [https://docs.microsoft.com/en-us/azure/defender-for-cloud/enable-data-collection?tabs=autoprovision-va](https://docs.microsoft.com/en-us/azure/defender-for-cloud/enable-data-collection?tabs=autoprovision-va)

## 技术信息

- Source Metadata：[sources/azure/defender_auto_provisioning_vulnerabilty_assessments_machines_on/metadata.json](../../sources/azure/defender_auto_provisioning_vulnerabilty_assessments_machines_on/metadata.json)
- Source Code：[sources/azure/defender_auto_provisioning_vulnerabilty_assessments_machines_on/check.py](../../sources/azure/defender_auto_provisioning_vulnerabilty_assessments_machines_on/check.py)
- Source Metadata Path：`sources/azure/defender_auto_provisioning_vulnerabilty_assessments_machines_on/metadata.json`
- Source Code Path：`sources/azure/defender_auto_provisioning_vulnerabilty_assessments_machines_on/check.py`
