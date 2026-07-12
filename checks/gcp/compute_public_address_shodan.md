# Check if any of the Public Addresses are in Shodan (requires Shodan API KEY).

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `compute_public_address_shodan` |
| クラウドプラットフォーム | GCP |
| サービス | compute |
| 重大度 | high |
| カテゴリ | internet-exposed |
| チェックタイプ | Infrastructure Security |
| リソースタイプ | GCPComputeAddress |
| リソースグループ | network |

## 説明

Check if any of the Public Addresses are in Shodan (requires Shodan API KEY).

## リスク

Sites like Shodan index exposed systems and further expose them to wider audiences as a quick way to find exploitable systems.

## 推奨事項

Check Identified IPs, consider changing them to private ones and delete them from Shodan.

- 推奨リンク：[https://www.shodan.io/](https://www.shodan.io/)

## 修正手順

No remediation steps available.

## 参考資料

- [https://www.shodan.io/](https://www.shodan.io/)

## 技術情報

- Source Metadata：[sources/gcp/compute_public_address_shodan/metadata.json](../../sources/gcp/compute_public_address_shodan/metadata.json)
- Source Code：[sources/gcp/compute_public_address_shodan/check.py](../../sources/gcp/compute_public_address_shodan/check.py)
- Source Metadata Path：`sources/gcp/compute_public_address_shodan/metadata.json`
- Source Code Path：`sources/gcp/compute_public_address_shodan/check.py`
