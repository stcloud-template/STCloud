# Ensure That RSASHA1 Is Not Used for the Key-Signing Key in Cloud DNS DNSSEC

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `dns_rsasha1_in_use_to_key_sign_in_dnssec` |
| クラウドプラットフォーム | GCP |
| サービス | dns |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | DNS_Zone |
| リソースグループ | network |

## 説明

NOTE: Currently, the SHA1 algorithm has been removed from general use by Google, and, if being used, needs to be whitelisted on a project basis by Google and will also, therefore, require a Google Cloud support contract. DNSSEC algorithm numbers in this registry may be used in CERT RRs. Zone signing (DNSSEC) and transaction security mechanisms (SIG(0) and TSIG) make use of particular subsets of these algorithms. The algorithm used for key signing should be a recommended one and it should be strong.

## リスク

SHA1 is considered weak and vulnerable to collision attacks.

## 推奨事項

Ensure that Domain Name System Security Extensions (DNSSEC) feature is not using the deprecated RSASHA1 algorithm for the Key-Signing Key (KSK) associated with your DNS managed zone file. The algorithm used for DNSSEC signing should be a strong one, such as ECDSAP256SHA256 algorithm, as this is secure and widely deployed, and therefore it is a good choice for both DNSSEC validation and signing.

- 推奨リンク：[https://cloud.google.com/dns/docs/dnssec-config](https://cloud.google.com/dns/docs/dnssec-config)

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_6#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_6#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudDNS/dns-sec-key-signing-algorithm-in-use.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudDNS/dns-sec-key-signing-algorithm-in-use.html)

## 参考資料

- [https://cloud.google.com/dns/docs/dnssec-config](https://cloud.google.com/dns/docs/dnssec-config)

## 技術情報

- Source Metadata：[sources/gcp/dns_rsasha1_in_use_to_key_sign_in_dnssec/metadata.json](../../sources/gcp/dns_rsasha1_in_use_to_key_sign_in_dnssec/metadata.json)
- Source Code：[sources/gcp/dns_rsasha1_in_use_to_key_sign_in_dnssec/check.py](../../sources/gcp/dns_rsasha1_in_use_to_key_sign_in_dnssec/check.py)
- Source Metadata Path：`sources/gcp/dns_rsasha1_in_use_to_key_sign_in_dnssec/metadata.json`
- Source Code Path：`sources/gcp/dns_rsasha1_in_use_to_key_sign_in_dnssec/check.py`
