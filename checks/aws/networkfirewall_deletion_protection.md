# Network Firewall has deletion protection enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `networkfirewall_deletion_protection` |
| 云平台 | AWS |
| 服务 | networkfirewall |
| 严重等级 | medium |
| 类别 | resilience |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsNetworkFirewallFirewall |
| 资源组 | network |

## 描述

**AWS Network Firewall firewalls** have **deletion protection** enabled (`DeleteProtection=true`).

## 风险

Without deletion protection, a firewall can be removed accidentally or by a compromised identity, letting traffic bypass inspection and logging. This threatens **confidentiality** and **integrity** via unfiltered access, and harms **availability** through routing disruption and loss of perimeter controls.

## 推荐措施

Enable **deletion protection** on every firewall (`DeleteProtection=true`). Enforce **least privilege** to prevent delete actions, require **change approval** for firewall modifications, and implement guardrails with policy-as-code. Apply **defense in depth** so alternate controls contain traffic if a firewall is altered.

## 修复步骤


### CLI

```text
aws network-firewall update-firewall-delete-protection --firewall-name <FIREWALL_NAME> --delete-protection
```

### Native IaC

```yaml
# CloudFormation: enable deletion protection on a Network Firewall
Resources:
  <example_resource_name>:
    Type: AWS::NetworkFirewall::Firewall
    Properties:
      FirewallName: <example_resource_name>  # Required: unique name for the firewall
      FirewallPolicyArn: <example_resource_id>
      VpcId: <example_resource_id>
      SubnetMappings:
        - SubnetId: <example_resource_id>
      DeleteProtection: true  # Critical: enables deletion protection to pass the check
```

### Terraform

```hcl
# Terraform: enable deletion protection on a Network Firewall
resource "aws_networkfirewall_firewall" "<example_resource_name>" {
  name                = "<example_resource_name>"
  firewall_policy_arn = "<example_resource_id>"
  vpc_id              = "<example_resource_id>"

  subnet_mapping {
    subnet_id = "<example_resource_id>"
  }

  delete_protection = true  # Critical: prevents deletion to pass the check
}
```

### Other

1. Open the AWS console and go to VPC > Network Firewall > Firewalls
2. Select the target firewall
3. On Firewall details, choose Edit (or Change protections)
4. Enable Deletion protection
5. Save changes

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/networkfirewall-controls.html#networkfirewall-9](https://docs.aws.amazon.com/securityhub/latest/userguide/networkfirewall-controls.html#networkfirewall-9)

## 技术信息

- Source Metadata：[sources/aws/networkfirewall_deletion_protection/metadata.json](../../sources/aws/networkfirewall_deletion_protection/metadata.json)
- Source Code：[sources/aws/networkfirewall_deletion_protection/check.py](../../sources/aws/networkfirewall_deletion_protection/check.py)
- Source Metadata Path：`sources/aws/networkfirewall_deletion_protection/metadata.json`
- Source Code Path：`sources/aws/networkfirewall_deletion_protection/check.py`
