# Amazon EC2 Transit Gateways should not automatically accept VPC attachment requests

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_transitgateway_auto_accept_vpc_attachments` |
| 云平台 | AWS |
| 服务 | ec2 |
| 子服务 | transit-gateway |
| 严重等级 | high |
| 类别 | Uncategorized |
| 检查类型 | Infrastructure Security |
| 资源类型 | AwsEc2TransitGateway |
| 资源组 | network |

## 描述

Ensure EC2 transit gateways are not automatically accepting shared VPC attachments. We get a fail if a transit gateway is configured to automatically accept shared VPC attachment requests.

## 风险

Turning on AutoAcceptSharedAttachments allows a transit gateway to automatically accept any cross-account VPC attachment requests without verification. This increases the risk of unauthorized VPC attachments, compromising network security.

## 推荐措施

Turn off AutoAcceptSharedAttachments to ensure that only authorized VPC attachment requests are accepted

- 推荐链接：[https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html#tgw-modifying](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html#tgw-modifying)

## 修复步骤


### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-23](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-23)

## 参考资料

- [https://docs.aws.amazon.com/config/latest/developerguide/ec2-transit-gateway-auto-vpc-attach-disabled.html](https://docs.aws.amazon.com/config/latest/developerguide/ec2-transit-gateway-auto-vpc-attach-disabled.html)
- [https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html#tgw-modifying](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html#tgw-modifying)

## 技术信息

- Source Metadata：[sources/aws/ec2_transitgateway_auto_accept_vpc_attachments/metadata.json](../../sources/aws/ec2_transitgateway_auto_accept_vpc_attachments/metadata.json)
- Source Code：[sources/aws/ec2_transitgateway_auto_accept_vpc_attachments/check.py](../../sources/aws/ec2_transitgateway_auto_accept_vpc_attachments/check.py)
- Source Metadata Path：`sources/aws/ec2_transitgateway_auto_accept_vpc_attachments/metadata.json`
- Source Code Path：`sources/aws/ec2_transitgateway_auto_accept_vpc_attachments/check.py`
