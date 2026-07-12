# Network Firewall policy drops or forwards fragmented packets by default

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `networkfirewall_policy_default_action_fragmented_packets` |
| クラウドプラットフォーム | AWS |
| サービス | networkfirewall |
| 重大度 | high |
| カテゴリ | trust-boundaries |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls (USA), TTPs/Defense Evasion |
| リソースタイプ | AwsNetworkFirewallFirewall |
| リソースグループ | network |

## 説明

**Network Firewall policies** are assessed for the `StatelessFragmentDefaultActions` setting to confirm **fragmented UDP packets** use `aws:drop` or `aws:forward_to_sfe`.

## リスク

Using `aws:pass` for **fragmented UDP** lets uninspected traffic traverse the firewall. Attackers can evade filters via fragmentation, enabling **data exfiltration** (confidentiality), payload smuggling and lateral movement (integrity), and fragment floods that strain services (availability).

## 推奨事項

Set `StatelessFragmentDefaultActions` to `aws:drop` or `aws:forward_to_sfe` so fragments are blocked or sent for **stateful inspection**. Apply **least privilege** on traffic flows, use **defense in depth** with rule groups, and monitor logs for anomalous fragmentation.

## 修正手順


### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::NetworkFirewall::FirewallPolicy
    Properties:
      FirewallPolicyName: <example_resource_name>
      FirewallPolicy:
        StatelessDefaultActions:
          - aws:drop
        StatelessFragmentDefaultActions:
          - aws:drop  # Critical: ensures fragmented UDP packets are dropped by default to pass the check
```

### Terraform

```hcl
resource "aws_networkfirewall_firewall_policy" "<example_resource_name>" {
  name = "<example_resource_name>"

  firewall_policy {
    stateless_default_actions          = ["aws:drop"]
    stateless_fragment_default_actions = ["aws:drop"]  # Critical: drop fragmented UDP packets by default to pass the check
  }
}
```

### Other

1. Open the Amazon VPC console and go to Network Firewall > Firewall policies
2. Select the policy to edit and choose Edit
3. Under Stateless default actions, find Fragmented packets
4. Set the action to Drop (or Forward to stateful rule groups)
5. Save changes

## 参考資料

- [https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_FirewallPolicy.html](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_FirewallPolicy.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/networkfirewall-controls.html#networkfirewall-5](https://docs.aws.amazon.com/securityhub/latest/userguide/networkfirewall-controls.html#networkfirewall-5)
- [https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-policy-updating.html](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-policy-updating.html)
- [https://docs.aws.amazon.com/network-firewall/latest/developerguide/stateless-default-actions.html](https://docs.aws.amazon.com/network-firewall/latest/developerguide/stateless-default-actions.html)
- [https://docs.aws.amazon.com/config/latest/developerguide/netfw-policy-default-action-fragment-packets.html](https://docs.aws.amazon.com/config/latest/developerguide/netfw-policy-default-action-fragment-packets.html)

## 技術情報

- Source Metadata：[sources/aws/networkfirewall_policy_default_action_fragmented_packets/metadata.json](../../sources/aws/networkfirewall_policy_default_action_fragmented_packets/metadata.json)
- Source Code：[sources/aws/networkfirewall_policy_default_action_fragmented_packets/check.py](../../sources/aws/networkfirewall_policy_default_action_fragmented_packets/check.py)
- Source Metadata Path：`sources/aws/networkfirewall_policy_default_action_fragmented_packets/metadata.json`
- Source Code Path：`sources/aws/networkfirewall_policy_default_action_fragmented_packets/check.py`
