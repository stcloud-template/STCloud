# EC2 Client VPN endpoints should have client connection logging enabled.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_client_vpn_endpoint_connection_logging_enabled` |
| 云平台 | AWS |
| 服务 | ec2 |
| 严重等级 | low |
| 类别 | Uncategorized |
| 资源类型 | AwsEc2ClientVpnEndpoint |
| 资源组 | network |

## 描述

This control checks whether an AWS Client VPN endpoint has client connection logging enabled. The control fails if the endpoint doesn't have client connection logging enabled.

## 风险

Client VPN endpoints allow remote clients to securely connect to resources in a Virtual Private Cloud (VPC) in AWS. Connection logs allow you to track user activity on the VPN endpoint and provides visibility.

## 推荐措施

To enable connection logging, see Enable connection logging for an existing Client VPN endpoint in the AWS Client VPN Administrator Guide.

- 推荐链接：[https://docs.aws.amazon.com/config/latest/developerguide/ec2-client-vpn-connection-log-enabled.html](https://docs.aws.amazon.com/config/latest/developerguide/ec2-client-vpn-connection-log-enabled.html)

## 修复步骤


### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-51](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-51)

## 参考资料

- [https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html)
- [https://docs.aws.amazon.com/config/latest/developerguide/ec2-client-vpn-connection-log-enabled.html](https://docs.aws.amazon.com/config/latest/developerguide/ec2-client-vpn-connection-log-enabled.html)

## 技术信息

- Source Metadata：[sources/aws/ec2_client_vpn_endpoint_connection_logging_enabled/metadata.json](../../sources/aws/ec2_client_vpn_endpoint_connection_logging_enabled/metadata.json)
- Source Code：[sources/aws/ec2_client_vpn_endpoint_connection_logging_enabled/check.py](../../sources/aws/ec2_client_vpn_endpoint_connection_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/ec2_client_vpn_endpoint_connection_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/ec2_client_vpn_endpoint_connection_logging_enabled/check.py`
