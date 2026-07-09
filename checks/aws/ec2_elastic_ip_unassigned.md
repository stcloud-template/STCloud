# Check if there is any unassigned Elastic IP.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_elastic_ip_unassigned` |
| 云平台 | AWS |
| 服务 | ec2 |
| 严重等级 | low |
| 类别 | Uncategorized |
| 检查类型 | Infrastructure Security |
| 资源类型 | AwsEc2Eip |
| 资源组 | network |

## 描述

Check if there is any unassigned Elastic IP.

## 风险

Unassigned Elastic IPs may result in extra cost.

## 推荐措施

Ensure Elastic IPs are not unassigned.

- 推荐链接：[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html)

## 修复步骤


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

## 参考资料

- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html)

## 技术信息

- Source Metadata：[sources/aws/ec2_elastic_ip_unassigned/metadata.json](../../sources/aws/ec2_elastic_ip_unassigned/metadata.json)
- Source Code：[sources/aws/ec2_elastic_ip_unassigned/check.py](../../sources/aws/ec2_elastic_ip_unassigned/check.py)
- Source Metadata Path：`sources/aws/ec2_elastic_ip_unassigned/metadata.json`
- Source Code Path：`sources/aws/ec2_elastic_ip_unassigned/check.py`
