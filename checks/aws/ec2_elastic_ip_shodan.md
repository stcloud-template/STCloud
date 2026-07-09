# Check if any of the Elastic or Public IP are in Shodan (requires Shodan API KEY).

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_elastic_ip_shodan` |
| 云平台 | AWS |
| 服务 | ec2 |
| 严重等级 | high |
| 类别 | internet-exposed |
| 检查类型 | Infrastructure Security |
| 资源类型 | AwsEc2Eip |
| 资源组 | network |

## 描述

Check if any of the Elastic or Public IP are in Shodan (requires Shodan API KEY).

## 风险

Sites like Shodan index exposed systems and further expose them to wider audiences as a quick way to find exploitable systems.

## 推荐措施

Check Identified IPs, consider changing them to private ones and delete them from Shodan.

- 推荐链接：[https://www.shodan.io/](https://www.shodan.io/)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://www.shodan.io/](https://www.shodan.io/)

## 技术信息

- Source Metadata：[sources/aws/ec2_elastic_ip_shodan/metadata.json](../../sources/aws/ec2_elastic_ip_shodan/metadata.json)
- Source Code：[sources/aws/ec2_elastic_ip_shodan/check.py](../../sources/aws/ec2_elastic_ip_shodan/check.py)
- Source Metadata Path：`sources/aws/ec2_elastic_ip_shodan/metadata.json`
- Source Code Path：`sources/aws/ec2_elastic_ip_shodan/check.py`
