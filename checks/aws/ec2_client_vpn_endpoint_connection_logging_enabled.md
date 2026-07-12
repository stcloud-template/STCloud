# EC2 Client VPN endpoints should have client connection logging enabled.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_client_vpn_endpoint_connection_logging_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| 重大度 | low |
| カテゴリ | Uncategorized |
| リソースタイプ | AwsEc2ClientVpnEndpoint |
| リソースグループ | network |

## 説明

This control checks whether an AWS Client VPN endpoint has client connection logging enabled. The control fails if the endpoint doesn't have client connection logging enabled.

## リスク

Client VPN endpoints allow remote clients to securely connect to resources in a Virtual Private Cloud (VPC) in AWS. Connection logs allow you to track user activity on the VPN endpoint and provides visibility.

## 推奨事項

To enable connection logging, see Enable connection logging for an existing Client VPN endpoint in the AWS Client VPN Administrator Guide.

- 推奨リンク：[https://docs.aws.amazon.com/config/latest/developerguide/ec2-client-vpn-connection-log-enabled.html](https://docs.aws.amazon.com/config/latest/developerguide/ec2-client-vpn-connection-log-enabled.html)

## 修正手順


### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-51](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-51)

## 参考資料

- [https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html)
- [https://docs.aws.amazon.com/config/latest/developerguide/ec2-client-vpn-connection-log-enabled.html](https://docs.aws.amazon.com/config/latest/developerguide/ec2-client-vpn-connection-log-enabled.html)

## 技術情報

- Source Metadata：[sources/aws/ec2_client_vpn_endpoint_connection_logging_enabled/metadata.json](../../sources/aws/ec2_client_vpn_endpoint_connection_logging_enabled/metadata.json)
- Source Code：[sources/aws/ec2_client_vpn_endpoint_connection_logging_enabled/check.py](../../sources/aws/ec2_client_vpn_endpoint_connection_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/ec2_client_vpn_endpoint_connection_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/ec2_client_vpn_endpoint_connection_logging_enabled/check.py`
