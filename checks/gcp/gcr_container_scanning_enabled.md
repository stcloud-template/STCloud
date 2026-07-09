# Ensure Image Vulnerability Scanning using GCR Container Scanning or a third-party provider

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `gcr_container_scanning_enabled` |
| 云平台 | GCP |
| 服务 | gcr |
| 子服务 | Container Scanning |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Security, Configuration |
| 资源类型 | Service |
| 资源组 | container |

## 描述

Scan images stored in Google Container Registry (GCR) for vulnerabilities using GCR Container Scanning or a third-party provider. This helps identify and mitigate security risks associated with known vulnerabilities in container images.

## 风险

Without image vulnerability scanning, container images stored in GCR may contain known vulnerabilities, increasing the risk of exploitation by malicious actors.

## 推荐措施

Enable vulnerability scanning for images stored in GCR using GCR Container Scanning or a third-party provider.

- 推荐链接：[https://cloud.google.com/container-registry/docs/container-best-practices](https://cloud.google.com/container-registry/docs/container-best-practices)

## 修复步骤


### CLI

```text
gcloud services enable containerscanning.googleapis.com
```

### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/ensure-gcp-gcr-container-vulnerability-scanning-is-enabled#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/ensure-gcp-gcr-container-vulnerability-scanning-is-enabled#terraform)

## 参考资料

- [https://cloud.google.com/container-registry/docs/container-analysis](https://cloud.google.com/container-registry/docs/container-analysis)
- [https://cloud.google.com/container-registry/docs/container-best-practices](https://cloud.google.com/container-registry/docs/container-best-practices)

## 技术信息

- Source Metadata：[sources/gcp/gcr_container_scanning_enabled/metadata.json](../../sources/gcp/gcr_container_scanning_enabled/metadata.json)
- Source Code：[sources/gcp/gcr_container_scanning_enabled/check.py](../../sources/gcp/gcr_container_scanning_enabled/check.py)
- Source Metadata Path：`sources/gcp/gcr_container_scanning_enabled/metadata.json`
- Source Code Path：`sources/gcp/gcr_container_scanning_enabled/check.py`
