# Network Firewall policy has at least one rule group associated

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `networkfirewall_policy_rule_group_associated` |
| クラウドプラットフォーム | AWS |
| サービス | networkfirewall |
| 重大度 | high |
| カテゴリ | trust-boundaries |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls (USA) |
| リソースタイプ | AwsNetworkFirewallFirewall |
| リソースグループ | network |

## 説明

Network Firewall policies have one or more **stateful** or **stateless rule groups** associated to define packet inspection and handling. Policies with no rule groups are identified.

## リスク

Without rule groups, traffic isn't meaningfully inspected, allowing unauthorized flows across VPC boundaries. Impacts: - Confidentiality: data exfiltration - Integrity: unauthorized changes via exposed services - Availability: C2, scanning, or DoS traffic passes; enables lateral movement

## 推奨事項

Associate appropriate **stateful** and **stateless rule groups** with every policy. - Enforce a **deny-by-default** posture (least privilege) - Use vetted managed rule groups as a baseline, then tailor to workloads - Review and test regularly; version rules, monitor logs, and require change control

## 修正手順


### Native IaC

```yaml
# CloudFormation: Attach at least one rule group to a Network Firewall policy
Resources:
  FirewallPolicy:
    Type: AWS::NetworkFirewall::FirewallPolicy
    Properties:
      FirewallPolicyName: <example_resource_name>
      FirewallPolicy:
        StatelessDefaultActions:
          - aws:forward_to_sfe
        StatelessFragmentDefaultActions:
          - aws:forward_to_sfe
        # Critical: Associate at least one rule group with the policy to pass the check
        StatefulRuleGroupReferences:
          - ResourceArn: <example_resource_arn>  # Critical line: references an existing rule group ARN
```

### Terraform

```hcl
# Attach at least one rule group to a Network Firewall policy
resource "aws_networkfirewall_firewall_policy" "<example_resource_name>" {
  name = "<example_resource_name>"

  firewall_policy {
    stateless_default_actions          = ["aws:forward_to_sfe"]
    stateless_fragment_default_actions = ["aws:forward_to_sfe"]

    # Critical: Associate at least one rule group with the policy to pass the check
    stateful_rule_group_reference {
      resource_arn = "<example_resource_arn>"  # Critical line: references an existing rule group ARN
    }
  }
}
```

### Other

1. Open the AWS Console and go to VPC > Network Firewall > Firewall policies
2. Select the target firewall policy
3. In Stateful rule groups (or Stateless rule groups), choose Add rule groups (or Add managed stateful/stateless rule groups)
4. Select at least one existing rule group and choose Add to policy
5. Click Save

## 参考資料

- [https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-groups.html](https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-groups.html)
- [https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-policy-updating.html](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-policy-updating.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/networkfirewall-controls.html#networkfirewall-3](https://docs.aws.amazon.com/securityhub/latest/userguide/networkfirewall-controls.html#networkfirewall-3)
- [https://medium.com/slalom-blog/secure-internet-access-egress-filtering-with-aws-network-firewall-ddf52ae121f9](https://medium.com/slalom-blog/secure-internet-access-egress-filtering-with-aws-network-firewall-ddf52ae121f9)
- [https://docs.aws.amazon.com/de_de/network-firewall/latest/developerguide/nwfw-using-managed-rule-groups-add-to-policy.html](https://docs.aws.amazon.com/de_de/network-firewall/latest/developerguide/nwfw-using-managed-rule-groups-add-to-policy.html)

## 技術情報

- Source Metadata：[sources/aws/networkfirewall_policy_rule_group_associated/metadata.json](../../sources/aws/networkfirewall_policy_rule_group_associated/metadata.json)
- Source Code：[sources/aws/networkfirewall_policy_rule_group_associated/check.py](../../sources/aws/networkfirewall_policy_rule_group_associated/check.py)
- Source Metadata Path：`sources/aws/networkfirewall_policy_rule_group_associated/metadata.json`
- Source Code Path：`sources/aws/networkfirewall_policy_rule_group_associated/check.py`
