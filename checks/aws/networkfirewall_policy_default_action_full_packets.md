# Network Firewall firewall policy default stateless action for full packets is drop or forward

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `networkfirewall_policy_default_action_full_packets` |
| クラウドプラットフォーム | AWS |
| サービス | networkfirewall |
| 重大度 | high |
| カテゴリ | trust-boundaries |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls |
| リソースタイプ | AwsNetworkFirewallFirewall |
| リソースグループ | network |

## 説明

**AWS Network Firewall policies** define a **stateless default action** for full packets. This evaluates whether unmatched packets are handled by `aws:drop` or `aws:forward_to_sfe`, meaning they are either discarded or sent to the stateful engine rather than allowed to pass.

## リスク

Using `Pass` as the default allows unmatched full packets to bypass stateless filtering and stateful inspection, enabling reconnaissance, malware delivery, and covert data exfiltration. This undermines **confidentiality** and **integrity**, and can threaten **availability** through unfiltered attacks.

## 推奨事項

Enforce a **deny-by-default** posture: set the stateless default for full packets to `aws:drop` or `aws:forward_to_sfe`. Use explicit allow rules, layer **stateful inspection**, and maintain logging and reviews to support **defense in depth** and **least privilege**.

## 修正手順


### Native IaC

```yaml
# CloudFormation: set default stateless action for full packets to Drop
Resources:
  <example_resource_name>:
    Type: AWS::NetworkFirewall::FirewallPolicy
    Properties:
      FirewallPolicyName: <example_resource_name>
      FirewallPolicy:
        StatelessDefaultActions:
          - aws:drop  # CRITICAL: full packets default to Drop (fixes the check)
        StatelessFragmentDefaultActions:
          - aws:drop  # Required for a valid policy
```

### Terraform

```hcl
# Terraform: set default stateless action for full packets to Drop
resource "aws_networkfirewall_firewall_policy" "<example_resource_name>" {
  name = "<example_resource_name>"

  firewall_policy {
    stateless_default_actions          = ["aws:drop"]  # CRITICAL: full packets default to Drop (fixes the check)
    stateless_fragment_default_actions = ["aws:drop"]  # Required for a valid policy
  }
}
```

### Other

1. In the AWS console, open Amazon VPC
2. Under Network Firewall, select Firewall policies
3. Open the target firewall policy and choose Edit
4. In Stateless default actions (full packets), select Drop (or Forward to stateful rule groups)
5. Choose Save

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/networkfirewall-controls.html#networkfirewall-4](https://docs.aws.amazon.com/securityhub/latest/userguide/networkfirewall-controls.html#networkfirewall-4)
- [https://docs.aws.amazon.com/network-firewall/latest/developerguide/stateless-default-actions.html](https://docs.aws.amazon.com/network-firewall/latest/developerguide/stateless-default-actions.html)
- [https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-policy-updating.html](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-policy-updating.html)

## 技術情報

- Source Metadata：[sources/aws/networkfirewall_policy_default_action_full_packets/metadata.json](../../sources/aws/networkfirewall_policy_default_action_full_packets/metadata.json)
- Source Code：[sources/aws/networkfirewall_policy_default_action_full_packets/check.py](../../sources/aws/networkfirewall_policy_default_action_full_packets/check.py)
- Source Metadata Path：`sources/aws/networkfirewall_policy_default_action_full_packets/metadata.json`
- Source Code Path：`sources/aws/networkfirewall_policy_default_action_full_packets/check.py`
