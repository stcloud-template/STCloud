# VPC has Network Firewall enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `networkfirewall_in_all_vpc` |
| クラウドプラットフォーム | AWS |
| サービス | networkfirewall |
| 重大度 | medium |
| カテゴリ | trust-boundaries |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | AwsEc2Vpc |
| リソースグループ | network |

## 説明

**VPCs** with an **AWS Network Firewall** associated to the same VPC to inspect and filter network traffic. Identifies VPCs that do not have a Network Firewall resource linked to them.

## リスク

Without a **Network Firewall**, VPC traffic can bypass deep inspection and centralized policy enforcement, enabling **data exfiltration**, **command-and-control**, and **lateral movement**. Confidentiality is reduced by unmonitored flows; integrity and availability are threatened by malware and disruptive traffic.

## 推奨事項

Deploy **AWS Network Firewall** in each VPC or centralize inspection through a dedicated hub VPC. Adopt a `default-deny` posture with least-privilege rules, restrict egress to required destinations, segment workloads (**defense in depth**, **zero trust**), and enable logging to monitor and tune network policies.

## 修正手順


### CLI

```text
aws network-firewall create-firewall --firewall-name <example_resource_name> --firewall-policy-arn <example_resource_id> --vpc-id <example_resource_id> --subnet-mappings "SubnetId=<example_resource_id>"
```

### Native IaC

```yaml
# CloudFormation: Create a Network Firewall in the VPC
Resources:
  <example_resource_name>:
    Type: AWS::NetworkFirewall::Firewall
    Properties:
      FirewallName: <example_resource_name>
      FirewallPolicyArn: <example_resource_id>  # Critical: required policy for the firewall
      VpcId: <example_resource_id>              # Critical: associates the firewall to the target VPC (fixes the check)
      SubnetMappings:                           # Critical: creates firewall endpoints in the VPC
        - SubnetId: <example_resource_id>
```

### Terraform

```hcl
# Create a Network Firewall in the VPC
resource "aws_networkfirewall_firewall" "<example_resource_name>" {
  name                = "<example_resource_name>"
  firewall_policy_arn = "<example_resource_id>"  # Critical: required policy
  vpc_id              = "<example_resource_id>"  # Critical: associates firewall to the VPC (fixes the check)

  subnet_mapping {                                # Critical: creates firewall endpoint in the VPC
    subnet_id = "<example_resource_id>"
  }
}
```

### Other

1. In the AWS Console, go to Network Firewall > Firewalls > Create firewall
2. Enter a name and select the target VPC
3. Select an existing Firewall policy (or create one when prompted)
4. Add at least one subnet from the VPC under Subnet mappings
5. Choose Create firewall
6. Verify the firewall shows under the selected VPC

## 参考資料

- [https://docs.aws.amazon.com/network-firewall/latest/developerguide/vpc-config.html](https://docs.aws.amazon.com/network-firewall/latest/developerguide/vpc-config.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/NetworkFirewall/network-firewall-in-use.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/NetworkFirewall/network-firewall-in-use.html)
- [https://docs.aws.amazon.com/network-firewall/latest/developerguide/setting-up.html](https://docs.aws.amazon.com/network-firewall/latest/developerguide/setting-up.html)

## 技術情報

- Source Metadata：[sources/aws/networkfirewall_in_all_vpc/metadata.json](../../sources/aws/networkfirewall_in_all_vpc/metadata.json)
- Source Code：[sources/aws/networkfirewall_in_all_vpc/check.py](../../sources/aws/networkfirewall_in_all_vpc/check.py)
- Source Metadata Path：`sources/aws/networkfirewall_in_all_vpc/metadata.json`
- Source Code Path：`sources/aws/networkfirewall_in_all_vpc/check.py`
