# Check if any of the Public Addresses are in Shodan (requires Shodan API KEY).

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `compute_public_address_shodan` |
| 云平台 | GCP |
| 服务 | compute |
| 严重等级 | high |
| 类别 | internet-exposed |
| 检查类型 | Infrastructure Security |
| 资源类型 | GCPComputeAddress |
| 资源组 | network |

## 描述

Check if any of the Public Addresses are in Shodan (requires Shodan API KEY).

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

- Source Metadata：[sources/gcp/compute_public_address_shodan/metadata.json](../../sources/gcp/compute_public_address_shodan/metadata.json)
- Source Code：[sources/gcp/compute_public_address_shodan/check.py](../../sources/gcp/compute_public_address_shodan/check.py)
- Source Metadata Path：`sources/gcp/compute_public_address_shodan/metadata.json`
- Source Code Path：`sources/gcp/compute_public_address_shodan/check.py`
