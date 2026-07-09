# Container images used by containers should have vulnerabilities resolved

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `defender_container_images_resolved_vulnerabilities` |
| 云平台 | Azure |
| 服务 | defender |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.Security/assessments |
| 资源组 | security |

## 描述

Container images used by containers should have vulnerabilities resolved. Azure Defender for Container Registries can help you identify and resolve vulnerabilities in your container images. It provides vulnerability scanning and prioritized security recommendations for your container images. You can use Azure Defender for Container Registries to scan your container images for vulnerabilities and get prioritized security recommendations to resolve them. You can also use Azure Defender for Container Registries to monitor your container registries for security threats and get prioritized security recommendations to resolve them. Azure Defender for Container Registries integrates with Azure Security Center to provide a unified view of security across your container registries and other Azure resources. Azure Defender for Container Registries is part of Azure Defender, which provides advanced threat protection for your hybrid workloads. Azure Defender uses advanced analytics and global threat intelligence to detect attacks that might otherwise go unnoticed.

## 风险

If vulnerabilities are not resolved, attackers can exploit them to gain unauthorized access to your containerized applications and data.

## 推荐措施

No content available.

- 推荐链接：[https://learn.microsoft.com/en-us/azure/container-registry/scan-images-defender](https://learn.microsoft.com/en-us/azure/container-registry/scan-images-defender)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://learn.microsoft.com/en-us/azure/container-registry/container-registry-check-health](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-check-health)
- [https://learn.microsoft.com/en-us/azure/container-registry/scan-images-defender](https://learn.microsoft.com/en-us/azure/container-registry/scan-images-defender)

## 技术信息

- Source Metadata：[sources/azure/defender_container_images_resolved_vulnerabilities/metadata.json](../../sources/azure/defender_container_images_resolved_vulnerabilities/metadata.json)
- Source Code：[sources/azure/defender_container_images_resolved_vulnerabilities/check.py](../../sources/azure/defender_container_images_resolved_vulnerabilities/check.py)
- Source Metadata Path：`sources/azure/defender_container_images_resolved_vulnerabilities/metadata.json`
- Source Code Path：`sources/azure/defender_container_images_resolved_vulnerabilities/check.py`
