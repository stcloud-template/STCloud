# Macie automated sensitive data discovery is enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `macie_automated_sensitive_data_discovery_enabled` |
| 云平台 | AWS |
| 服务 | macie |
| 严重等级 | high |
| 类别 | secrets |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | Other |
| 资源组 | security |

## 描述

**Amazon Macie** administrator account has **automated sensitive data discovery** enabled for S3 data. The evaluation confirms the feature's status for the account in each Region.

## 风险

Without continuous discovery, sensitive S3 objects remain unclassified and unnoticed, weakening **confidentiality**. Over-permissive or public access can persist undetected, enabling **data exfiltration** and delaying containment and **forensic** response.

## 推荐措施

Enable and maintain `automated sensitive data discovery` for the Macie administrator across required Regions. Include relevant buckets, tune identifiers and allow lists to reduce noise, and route findings to monitoring. Complement with **least privilege** on S3 and **defense in depth** for data protection.

## 修复步骤


### CLI

```text
aws macie2 update-automated-discovery-configuration --status ENABLED --region <REGION>
```

### Other

1. In the AWS Console, open Amazon Macie
2. Select the correct Region from the Region selector
3. Go to Settings > Automated sensitive data discovery
4. Click Enable under Status (choose My account if prompted)
5. Repeat in other Regions where Macie is enabled if needed

## 参考资料

- [https://docs.aws.amazon.com/config/latest/developerguide/macie-auto-sensitive-data-discovery-check.html](https://docs.aws.amazon.com/config/latest/developerguide/macie-auto-sensitive-data-discovery-check.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/macie-controls.html#macie-2](https://docs.aws.amazon.com/securityhub/latest/userguide/macie-controls.html#macie-2)
- [https://docs.aws.amazon.com/macie/latest/user/discovery-asdd-account-enable.html](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd-account-enable.html)

## 技术信息

- Source Metadata：[sources/aws/macie_automated_sensitive_data_discovery_enabled/metadata.json](../../sources/aws/macie_automated_sensitive_data_discovery_enabled/metadata.json)
- Source Code：[sources/aws/macie_automated_sensitive_data_discovery_enabled/check.py](../../sources/aws/macie_automated_sensitive_data_discovery_enabled/check.py)
- Source Metadata Path：`sources/aws/macie_automated_sensitive_data_discovery_enabled/metadata.json`
- Source Code Path：`sources/aws/macie_automated_sensitive_data_discovery_enabled/check.py`
