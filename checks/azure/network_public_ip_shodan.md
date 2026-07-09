# Check if an Azure Public IP is exposed in Shodan (requires Shodan API KEY).

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `network_public_ip_shodan` |
| 云平台 | Azure |
| 服务 | network |
| 严重等级 | high |
| 类别 | internet-exposed |
| 资源类型 | Network |
| 资源组 | network |

## 描述

Check if an Azure Public IP is exposed in Shodan (requires Shodan API KEY).

## 风险

If an Azure Public IP is exposed in Shodan, it can be accessed by anyone on the internet. This can lead to unauthorized access to your resources.

## 推荐措施

Check Identified IPs, Consider changing them to private ones and delete them from Shodan.

- 推荐链接：[https://www.shodan.io/](https://www.shodan.io/)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://www.shodan.io/](https://www.shodan.io/)

## 技术信息

- Source Metadata：[sources/azure/network_public_ip_shodan/metadata.json](../../sources/azure/network_public_ip_shodan/metadata.json)
- Source Code：[sources/azure/network_public_ip_shodan/check.py](../../sources/azure/network_public_ip_shodan/check.py)
- Source Metadata Path：`sources/azure/network_public_ip_shodan/metadata.json`
- Source Code Path：`sources/azure/network_public_ip_shodan/check.py`
