# Amazon Macie is enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `macie_is_enabled` |
| 云平台 | AWS |
| 服务 | macie |
| 严重等级 | medium |
| 类别 | secrets, forensics-ready |
| 检查类型 | Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/AWS Security Best Practices |
| 资源类型 | Other |
| 资源组 | security |

## 描述

**Amazon Macie** status is assessed per region with **S3** presence to determine if sensitive data discovery is operational. The outcome reflects whether Macie is active or in a `PAUSED`/not enabled state for the account and region.

## 风险

Without active Macie, sensitive data in **S3** can remain unclassified and exposed. Misconfigured access and public buckets may go undetected, enabling data exfiltration and secret leakage. This degrades confidentiality and widens breach blast radius by reducing visibility into where sensitive data resides.

## 推荐措施

Enable and maintain **Amazon Macie** in all regions hosting **S3** data. Use continuous sensitive data discovery, apply custom classifications for your data types, and route findings to monitoring. Enforce least privilege for Macie access and strengthen defense in depth with restrictive bucket policies and access controls.

## 修复步骤


### CLI

```text
aws macie2 enable-macie --region <REGION>
```

### Native IaC

```yaml
# CloudFormation: Enable Amazon Macie in this region
Resources:
  MacieSession:
    Type: AWS::Macie::Session
    Properties:
      Status: ENABLED  # Critical: Enables Macie for the account in this region
```

### Terraform

```hcl
# Enables Amazon Macie in this region
resource "aws_macie2_account" "main" {
  # Critical: Creating this resource enables Macie for the account in the region
}
```

### Other

1. Sign in to the AWS Management Console and switch to the target region
2. Open Amazon Macie
3. Click Get started or Enable Macie
4. If Macie shows Suspended/Paused, click Resume Macie
5. Repeat in each region with S3 buckets as needed

## 参考资料

- [https://aws.amazon.com/macie/getting-started/](https://aws.amazon.com/macie/getting-started/)

## 技术信息

- Source Metadata：[sources/aws/macie_is_enabled/metadata.json](../../sources/aws/macie_is_enabled/metadata.json)
- Source Code：[sources/aws/macie_is_enabled/check.py](../../sources/aws/macie_is_enabled/check.py)
- Source Metadata Path：`sources/aws/macie_is_enabled/metadata.json`
- Source Code Path：`sources/aws/macie_is_enabled/check.py`
