# Check for Virtual Machine Instances with Public IP Addresses

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `compute_instance_public_ip` |
| クラウドプラットフォーム | GCP |
| サービス | compute |
| 重大度 | high |
| カテゴリ | internet-exposed |
| リソースタイプ | VMInstance |
| リソースグループ | compute |

## 説明

Check for Virtual Machine Instances with Public IP Addresses

## リスク

To reduce your attack surface, Compute instances should not have public IP addresses. Instead, instances should be configured behind load balancers, to minimize the instance's exposure to the internet.

## 推奨事項

Ensure that your Google Compute Engine instances are not configured to have external IP addresses in order to minimize their exposure to the Internet.

- 推奨リンク：[https://cloud.google.com/compute/docs/instances/connecting-to-instance](https://cloud.google.com/compute/docs/instances/connecting-to-instance)

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-public-policies/bc_gcp_public_2#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-public-policies/bc_gcp_public_2#terraform)

### Other

[https://docs.ST Cloud.com/checks/gcp/google-cloud-public-policies/bc_gcp_public_2](https://docs.ST Cloud.com/checks/gcp/google-cloud-public-policies/bc_gcp_public_2)

## 参考資料

- [https://cloud.google.com/compute/docs/instances/connecting-to-instance](https://cloud.google.com/compute/docs/instances/connecting-to-instance)

## 技術情報

- Source Metadata：[sources/gcp/compute_instance_public_ip/metadata.json](../../sources/gcp/compute_instance_public_ip/metadata.json)
- Source Code：[sources/gcp/compute_instance_public_ip/check.py](../../sources/gcp/compute_instance_public_ip/check.py)
- Source Metadata Path：`sources/gcp/compute_instance_public_ip/metadata.json`
- Source Code Path：`sources/gcp/compute_instance_public_ip/check.py`
