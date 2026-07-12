# Ensure that the default network does not exist

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `compute_network_default_in_use` |
| クラウドプラットフォーム | GCP |
| サービス | compute |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | Network |
| リソースグループ | network |

## 説明

Ensure that the default network does not exist

## リスク

The default network has a preconfigured network configuration and automatically generates insecure firewall rules.

## 推奨事項

When an organization deletes the default network, it may need to migrate or service onto a new network.

- 推奨リンク：[https://cloud.google.com/vpc/docs/using-vpc](https://cloud.google.com/vpc/docs/using-vpc)

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_7#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_7#terraform)

### Other

[https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_7](https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_7)

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudVPC/default-vpc-in-use.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudVPC/default-vpc-in-use.html)
- [https://cloud.google.com/vpc/docs/using-vpc](https://cloud.google.com/vpc/docs/using-vpc)

## 技術情報

- Source Metadata：[sources/gcp/compute_network_default_in_use/metadata.json](../../sources/gcp/compute_network_default_in_use/metadata.json)
- Source Code：[sources/gcp/compute_network_default_in_use/check.py](../../sources/gcp/compute_network_default_in_use/check.py)
- Source Metadata Path：`sources/gcp/compute_network_default_in_use/metadata.json`
- Source Code Path：`sources/gcp/compute_network_default_in_use/check.py`
