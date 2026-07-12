# Check if an Azure Public IP is exposed in Shodan (requires Shodan API KEY).

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `network_public_ip_shodan` |
| クラウドプラットフォーム | Azure |
| サービス | network |
| 重大度 | high |
| カテゴリ | internet-exposed |
| リソースタイプ | Network |
| リソースグループ | network |

## 説明

Check if an Azure Public IP is exposed in Shodan (requires Shodan API KEY).

## リスク

If an Azure Public IP is exposed in Shodan, it can be accessed by anyone on the internet. This can lead to unauthorized access to your resources.

## 推奨事項

Check Identified IPs, Consider changing them to private ones and delete them from Shodan.

- 推奨リンク：[https://www.shodan.io/](https://www.shodan.io/)

## 修正手順

No remediation steps available.

## 参考資料

- [https://www.shodan.io/](https://www.shodan.io/)

## 技術情報

- Source Metadata：[sources/azure/network_public_ip_shodan/metadata.json](../../sources/azure/network_public_ip_shodan/metadata.json)
- Source Code：[sources/azure/network_public_ip_shodan/check.py](../../sources/azure/network_public_ip_shodan/check.py)
- Source Metadata Path：`sources/azure/network_public_ip_shodan/metadata.json`
- Source Code Path：`sources/azure/network_public_ip_shodan/check.py`
