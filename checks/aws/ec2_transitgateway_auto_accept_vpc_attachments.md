# Amazon EC2 Transit Gateways should not automatically accept VPC attachment requests

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_transitgateway_auto_accept_vpc_attachments` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| サブサービス | transit-gateway |
| 重大度 | high |
| カテゴリ | Uncategorized |
| チェックタイプ | Infrastructure Security |
| リソースタイプ | AwsEc2TransitGateway |
| リソースグループ | network |

## 説明

Ensure EC2 transit gateways are not automatically accepting shared VPC attachments. We get a fail if a transit gateway is configured to automatically accept shared VPC attachment requests.

## リスク

Turning on AutoAcceptSharedAttachments allows a transit gateway to automatically accept any cross-account VPC attachment requests without verification. This increases the risk of unauthorized VPC attachments, compromising network security.

## 推奨事項

Turn off AutoAcceptSharedAttachments to ensure that only authorized VPC attachment requests are accepted

- 推奨リンク：[https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html#tgw-modifying](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html#tgw-modifying)

## 修正手順


### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-23](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-23)

## 参考資料

- [https://docs.aws.amazon.com/config/latest/developerguide/ec2-transit-gateway-auto-vpc-attach-disabled.html](https://docs.aws.amazon.com/config/latest/developerguide/ec2-transit-gateway-auto-vpc-attach-disabled.html)
- [https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html#tgw-modifying](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html#tgw-modifying)

## 技術情報

- Source Metadata：[sources/aws/ec2_transitgateway_auto_accept_vpc_attachments/metadata.json](../../sources/aws/ec2_transitgateway_auto_accept_vpc_attachments/metadata.json)
- Source Code：[sources/aws/ec2_transitgateway_auto_accept_vpc_attachments/check.py](../../sources/aws/ec2_transitgateway_auto_accept_vpc_attachments/check.py)
- Source Metadata Path：`sources/aws/ec2_transitgateway_auto_accept_vpc_attachments/metadata.json`
- Source Code Path：`sources/aws/ec2_transitgateway_auto_accept_vpc_attachments/check.py`
