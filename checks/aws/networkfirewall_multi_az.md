# Network Firewall firewall is deployed across multiple Availability Zones

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `networkfirewall_multi_az` |
| クラウドプラットフォーム | AWS |
| サービス | networkfirewall |
| 重大度 | high |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls, Effects/Denial of Service |
| リソースタイプ | AwsNetworkFirewallFirewall |
| リソースグループ | network |

## 説明

**AWS Network Firewall firewalls** are assessed for **multi-AZ deployment**, expecting subnet mappings in more than one Availability Zone. A configuration with only one subnet mapping indicates a single-AZ firewall.

## リスク

Single-AZ firewalls are a single point of failure. An AZ outage can drop or blackhole traffic, degrading **availability**, or prompt route changes that bypass inspection, exposing **confidentiality** and **integrity** to unfiltered access, data exfiltration, and lateral movement.

## 推奨事項

Deploy firewalls across `>=2` AZs with a dedicated subnet in each used AZ. Maintain per-AZ, symmetric routing to the local endpoint to preserve stateful inspection. Apply **defense in depth** and automate drift controls and AZ failover tests to sustain resilience.

## 修正手順


### CLI

```text
aws network-firewall associate-subnets --firewall-arn <FIREWALL_ARN> --subnet-mappings SubnetId=<SUBNET_ID_IN_DIFFERENT_AZ>
```

### Native IaC

```yaml
# CloudFormation: Ensure the firewall spans multiple AZs by adding a second subnet mapping
Resources:
  <example_resource_name>:
    Type: AWS::NetworkFirewall::Firewall
    Properties:
      FirewallName: <example_resource_name>
      FirewallPolicyArn: <example_firewall_policy_arn>
      VpcId: <example_vpc_id>
      SubnetMappings:
        - SubnetId: <subnet-id-1>
        - SubnetId: <subnet-id-2>  # CRITICAL: second subnet in a different AZ to achieve multi-AZ
```

### Terraform

```hcl
# Terraform: Add a second subnet_mapping to deploy the firewall across multiple AZs
resource "aws_networkfirewall_firewall" "<example_resource_name>" {
  name                = "<example_resource_name>"
  firewall_policy_arn = "<example_firewall_policy_arn>"
  vpc_id              = "<example_vpc_id>"

  subnet_mapping {
    subnet_id = "<subnet-id-1>"
  }

  subnet_mapping {
    subnet_id = "<subnet-id-2>"  # CRITICAL: second subnet in a different AZ for multi-AZ
  }
}
```

### Other

1. Open the AWS Console and go to VPC > Network Firewall > Firewalls
2. Select your firewall and open the Firewall details tab
3. In Associated policy and VPC, click Edit
4. Click Add new subnet, choose an additional Availability Zone and its subnet in the same VPC
5. Ensure at least two AZs are selected, then click Save

## 参考資料

- [https://docs.aws.amazon.com/id_id/network-firewall/latest/developerguide/arch-two-zone-igw.html](https://docs.aws.amazon.com/id_id/network-firewall/latest/developerguide/arch-two-zone-igw.html)
- [https://aws.amazon.com/es/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall/](https://aws.amazon.com/es/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall/)
- [https://docs.aws.amazon.com/network-firewall/latest/developerguide/arch-two-zone-igw.html](https://docs.aws.amazon.com/network-firewall/latest/developerguide/arch-two-zone-igw.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/networkfirewall-controls.html#networkfirewall-1](https://docs.aws.amazon.com/securityhub/latest/userguide/networkfirewall-controls.html#networkfirewall-1)

## 技術情報

- Source Metadata：[sources/aws/networkfirewall_multi_az/metadata.json](../../sources/aws/networkfirewall_multi_az/metadata.json)
- Source Code：[sources/aws/networkfirewall_multi_az/check.py](../../sources/aws/networkfirewall_multi_az/check.py)
- Source Metadata Path：`sources/aws/networkfirewall_multi_az/metadata.json`
- Source Code Path：`sources/aws/networkfirewall_multi_az/check.py`
