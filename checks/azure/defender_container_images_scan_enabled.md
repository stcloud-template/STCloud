# Ensure Image Vulnerability Scanning using Azure Defender image scanning or a third party provider

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `defender_container_images_scan_enabled` |
| 云平台 | Azure |
| 服务 | defender |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.Security |
| 资源组 | security |

## 描述

Scan images being deployed to Azure (AKS) for vulnerabilities. Vulnerability scanning for images stored in Azure Container Registry is generally available in Azure Security Center. This capability is powered by Qualys, a leading provider of information security. When you push an image to Container Registry, Security Center automatically scans it, then checks for known vulnerabilities in packages or dependencies defined in the file. When the scan completes (after about 10 minutes), Security Center provides details and a security classification for each vulnerability detected, along with guidance on how to remediate issues and protect vulnerable attack surfaces.

## 风险

Vulnerabilities in software packages can be exploited by hackers or malicious users to obtain unauthorized access to local cloud resources. Azure Defender and other third party products allow images to be scanned for known vulnerabilities.

## 推荐措施

No content available.

- 推荐链接：[https://learn.microsoft.com/en-us/azure/container-registry/scan-images-defender](https://learn.microsoft.com/en-us/azure/container-registry/scan-images-defender)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://learn.microsoft.com/en-us/azure/container-registry/container-registry-check-health](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-check-health)
- [https://learn.microsoft.com/en-us/azure/container-registry/scan-images-defender](https://learn.microsoft.com/en-us/azure/container-registry/scan-images-defender)

## 技术信息

- Source Metadata：[sources/azure/defender_container_images_scan_enabled/metadata.json](../../sources/azure/defender_container_images_scan_enabled/metadata.json)
- Source Code：[sources/azure/defender_container_images_scan_enabled/check.py](../../sources/azure/defender_container_images_scan_enabled/check.py)
- Source Metadata Path：`sources/azure/defender_container_images_scan_enabled/metadata.json`
- Source Code Path：`sources/azure/defender_container_images_scan_enabled/check.py`
