# Ensure Image Vulnerability Scanning using Azure Defender image scanning or a third party provider

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `defender_container_images_scan_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | defender |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.Security |
| リソースグループ | security |

## 説明

Scan images being deployed to Azure (AKS) for vulnerabilities. Vulnerability scanning for images stored in Azure Container Registry is generally available in Azure Security Center. This capability is powered by Qualys, a leading provider of information security. When you push an image to Container Registry, Security Center automatically scans it, then checks for known vulnerabilities in packages or dependencies defined in the file. When the scan completes (after about 10 minutes), Security Center provides details and a security classification for each vulnerability detected, along with guidance on how to remediate issues and protect vulnerable attack surfaces.

## リスク

Vulnerabilities in software packages can be exploited by hackers or malicious users to obtain unauthorized access to local cloud resources. Azure Defender and other third party products allow images to be scanned for known vulnerabilities.

## 推奨事項

No content available.

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/container-registry/scan-images-defender](https://learn.microsoft.com/en-us/azure/container-registry/scan-images-defender)

## 修正手順

No remediation steps available.

## 参考資料

- [https://learn.microsoft.com/en-us/azure/container-registry/container-registry-check-health](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-check-health)
- [https://learn.microsoft.com/en-us/azure/container-registry/scan-images-defender](https://learn.microsoft.com/en-us/azure/container-registry/scan-images-defender)

## 技術情報

- Source Metadata：[sources/azure/defender_container_images_scan_enabled/metadata.json](../../sources/azure/defender_container_images_scan_enabled/metadata.json)
- Source Code：[sources/azure/defender_container_images_scan_enabled/check.py](../../sources/azure/defender_container_images_scan_enabled/check.py)
- Source Metadata Path：`sources/azure/defender_container_images_scan_enabled/metadata.json`
- Source Code Path：`sources/azure/defender_container_images_scan_enabled/check.py`
