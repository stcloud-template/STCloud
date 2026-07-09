# Security Hub is enabled with standards or integrations configured

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `securityhub_enabled` |
| 云平台 | AWS |
| 服务 | securityhub |
| 严重等级 | high |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards |
| 资源类型 | Other |
| 资源组 | security |

## 描述

**AWS Security Hub** is `ACTIVE` in the Region and has at least one enabled **security standard** or connected **integration**. Otherwise, it is either not enabled or enabled without standards/integrations.

## 风险

Absent **Security Hub coverage** or standards, security signals are fragmented and **control checks** don't run. High-risk findings can be missed or delayed, enabling data exfiltration, persistence, and lateral movement. This reduces **visibility** and undermines **confidentiality, integrity, and availability** across accounts/Regions.

## 推荐措施

- Enable in all required accounts/Regions - Turn on relevant **standards** (`AWS FSBP`, `CIS`) - Connect AWS and third-party **integrations** - Use **central configuration** and **least privilege** - Automate triage and monitor continuously for **defense in depth**

## 修复步骤


### Native IaC

```yaml
# CloudFormation: Enable Security Hub and at least one standard
Resources:
  <example_resource_name>Hub:
    Type: AWS::SecurityHub::Hub
    # Critical: Enables Security Hub in this account/Region

  <example_resource_name>Standard:
    Type: AWS::SecurityHub::Standard
    Properties:
      StandardsArn: arn:aws:securityhub:<REGION>::standards/aws-foundational-security-best-practices/v/1.0.0  # Critical: enables a standard so the check passes
```

### Terraform

```hcl
# Enable Security Hub
resource "aws_securityhub_account" "<example_resource_name>" {}

# Critical: Enable at least one standard so the check passes
resource "aws_securityhub_standards_subscription" "<example_resource_name>_fsbp" {
  standards_arn = "arn:aws:securityhub:<REGION>::standards/aws-foundational-security-best-practices/v/1.0.0" # Enables AWS FSBP
}
```

### Other

1. Open the AWS console and go to Security Hub
2. If prompted (first use): click Enable Security Hub and keep the default standards selected, then choose Enable
3. If Security Hub is already enabled: go to Security standards and enable AWS Foundational Security Best Practices
4. Wait for the status to show Enabled

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-enable-disable.html](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-enable-disable.html)

## 技术信息

- Source Metadata：[sources/aws/securityhub_enabled/metadata.json](../../sources/aws/securityhub_enabled/metadata.json)
- Source Code：[sources/aws/securityhub_enabled/check.py](../../sources/aws/securityhub_enabled/check.py)
- Source Metadata Path：`sources/aws/securityhub_enabled/metadata.json`
- Source Code Path：`sources/aws/securityhub_enabled/check.py`
