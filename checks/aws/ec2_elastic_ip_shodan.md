# Check if any of the Elastic or Public IP are in Shodan (requires Shodan API KEY).

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_elastic_ip_shodan` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| 重大度 | high |
| カテゴリ | internet-exposed |
| チェックタイプ | Infrastructure Security |
| リソースタイプ | AwsEc2Eip |
| リソースグループ | network |

## 説明

Check if any of the Elastic or Public IP are in Shodan (requires Shodan API KEY).

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

- Source Metadata：[sources/aws/ec2_elastic_ip_shodan/metadata.json](../../sources/aws/ec2_elastic_ip_shodan/metadata.json)
- Source Code：[sources/aws/ec2_elastic_ip_shodan/check.py](../../sources/aws/ec2_elastic_ip_shodan/check.py)
- Source Metadata Path：`sources/aws/ec2_elastic_ip_shodan/metadata.json`
- Source Code Path：`sources/aws/ec2_elastic_ip_shodan/check.py`
