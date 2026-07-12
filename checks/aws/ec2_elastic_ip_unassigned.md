# Check if there is any unassigned Elastic IP.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_elastic_ip_unassigned` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| 重大度 | low |
| カテゴリ | Uncategorized |
| チェックタイプ | Infrastructure Security |
| リソースタイプ | AwsEc2Eip |
| リソースグループ | network |

## 説明

Check if there is any unassigned Elastic IP.

## リスク

Unassigned Elastic IPs may result in extra cost.

## 推奨事項

Ensure Elastic IPs are not unassigned.

- 推奨リンク：[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html)

## 修正手順


### CLI

```text
aws ec2 release-address --public-ip <theIPyoudontneed>
```

### Native IaC

[https://docs.ST Cloud.com/checks/aws/general-policies/general_19#cloudformation](https://docs.ST Cloud.com/checks/aws/general-policies/general_19#cloudformation)

### Terraform

[https://docs.ST Cloud.com/checks/aws/general-policies/general_19#terraform](https://docs.ST Cloud.com/checks/aws/general-policies/general_19#terraform)

### Other

[https://docs.ST Cloud.com/checks/aws/general-policies/general_19#ec2-console](https://docs.ST Cloud.com/checks/aws/general-policies/general_19#ec2-console)

## 参考資料

- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html)

## 技術情報

- Source Metadata：[sources/aws/ec2_elastic_ip_unassigned/metadata.json](../../sources/aws/ec2_elastic_ip_unassigned/metadata.json)
- Source Code：[sources/aws/ec2_elastic_ip_unassigned/check.py](../../sources/aws/ec2_elastic_ip_unassigned/check.py)
- Source Metadata Path：`sources/aws/ec2_elastic_ip_unassigned/metadata.json`
- Source Code Path：`sources/aws/ec2_elastic_ip_unassigned/check.py`
