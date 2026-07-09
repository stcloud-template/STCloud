# Ensure Cloud Asset Inventory Is Enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_cloud_asset_inventory_enabled` |
| 云平台 | GCP |
| 服务 | iam |
| 子服务 | Asset Inventory |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | Service |
| 资源组 | governance |

## 描述

GCP Cloud Asset Inventory is services that provides a historical view of GCP resources and IAM policies through a time-series database. The information recorded includes metadata on Google Cloud resources, metadata on policies set on Google Cloud projects or resources, and runtime information gathered within a Google Cloud resource.

## 风险

Gaining insight into Google Cloud resources and policies is vital for tasks such as DevOps, security analytics, multi-cluster and fleet management, auditing, and governance. With Cloud Asset Inventory you can discover, monitor, and analyze all GCP assets in one place, achieving a better understanding of all your cloud assets across projects and services.

## 推荐措施

Ensure that Cloud Asset Inventory is enabled for all your GCP projects in order to efficiently manage the history and the inventory of your cloud resources. Google Cloud Asset Inventory is a fully managed metadata inventory service that allows you to view, monitor, analyze, and gain insights for your Google Cloud and Anthos assets. Cloud Asset Inventory is disabled by default in each GCP project.

- 推荐链接：[https://cloud.google.com/asset-inventory/docs](https://cloud.google.com/asset-inventory/docs)

## 修复步骤


### CLI

```text
gcloud services enable cloudasset.googleapis.com
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudAPI/enabled-cloud-asset-inventory.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudAPI/enabled-cloud-asset-inventory.html)

## 参考资料

- [https://cloud.google.com/asset-inventory/docs](https://cloud.google.com/asset-inventory/docs)

## 技术信息

- Source Metadata：[sources/gcp/iam_cloud_asset_inventory_enabled/metadata.json](../../sources/gcp/iam_cloud_asset_inventory_enabled/metadata.json)
- Source Code：[sources/gcp/iam_cloud_asset_inventory_enabled/check.py](../../sources/gcp/iam_cloud_asset_inventory_enabled/check.py)
- Source Metadata Path：`sources/gcp/iam_cloud_asset_inventory_enabled/metadata.json`
- Source Code Path：`sources/gcp/iam_cloud_asset_inventory_enabled/check.py`
