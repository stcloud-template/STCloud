# Ensure Legacy Networks Do Not Exist

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `compute_network_not_legacy` |
| クラウドプラットフォーム | GCP |
| サービス | compute |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | Network |
| リソースグループ | network |

## 説明

In order to prevent use of legacy networks, a project should not have a legacy network configured. As of now, Legacy Networks are gradually being phased out, and you can no longer create projects with them. This recommendation is to check older projects to ensure that they are not using Legacy Networks.

## リスク

Google Cloud legacy networks have a single global IPv4 range which cannot be divided into subnets, and a single gateway IP address for the whole network. Legacy networks do not support several Google Cloud networking features such as subnets, alias IP ranges, multiple network interfaces, Cloud NAT (Network Address Translation), Virtual Private Cloud (VPC) Peering, and private access options for GCP services. Legacy networks are not recommended for high network traffic projects and are subject to a single point of contention or failure.

## 推奨事項

Ensure that your Google Cloud Platform (GCP) projects are not using legacy networks as this type of network is no longer recommended for production environments because it does not support advanced networking features. Instead, it is strongly recommended to use Virtual Private Cloud (VPC) networks for existing and future GCP projects.

- 推奨リンク：[https://cloud.google.com/vpc/docs/using-legacy#deleting_a_legacy_network](https://cloud.google.com/vpc/docs/using-legacy#deleting_a_legacy_network)

## 修正手順


### CLI

```text
gcloud compute networks delete <LEGACY_NETWORK_NAME>
```

### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/ensure-legacy-networks-do-not-exist-for-a-project#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/ensure-legacy-networks-do-not-exist-for-a-project#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudVPC/legacy-vpc-in-use.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudVPC/legacy-vpc-in-use.html#)

## 参考資料

- [https://cloud.google.com/vpc/docs/using-legacy#deleting_a_legacy_network](https://cloud.google.com/vpc/docs/using-legacy#deleting_a_legacy_network)

## 技術情報

- Source Metadata：[sources/gcp/compute_network_not_legacy/metadata.json](../../sources/gcp/compute_network_not_legacy/metadata.json)
- Source Code：[sources/gcp/compute_network_not_legacy/check.py](../../sources/gcp/compute_network_not_legacy/check.py)
- Source Metadata Path：`sources/gcp/compute_network_not_legacy/metadata.json`
- Source Code Path：`sources/gcp/compute_network_not_legacy/check.py`
