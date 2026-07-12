# All AWS FMS policies in the admin account are compliant for all accounts

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `fms_policy_compliant` |
| クラウドプラットフォーム | AWS |
| サービス | fms |
| 重大度 | medium |
| カテゴリ | internet-exposed, trust-boundaries |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | Other |
| リソースグループ | security |

## 説明

**Firewall Manager** policies in the administrator account are evaluated for organization-wide compliance. The assessment reviews each policy's account-level status and flags entries marked `NON_COMPLIANT` or unset. It also identifies when no effective policies exist within the administrator scope.

## リスク

Policy drift or absence leaves in-scope resources without enforced controls, degrading **confidentiality**, **integrity**, and **availability**. Missing WAF, Shield, security group, or network firewall baselines can enable DDoS exposure, unsafe routes, and open access, leading to unauthorized entry and data exfiltration.

## 推奨事項

Maintain centralized enforcement with **Firewall Manager**: define mandatory policies for all relevant accounts/resources, enable automatic remediation where appropriate, and continuously monitor compliance. Apply **least privilege** and **defense in depth** by standardizing web, network, and DNS protections and alerting on drift.

## 修正手順


### Other

1. Sign in to the AWS console with the Firewall Manager administrator account
2. Open Firewall Manager > Security policies
3. If no policies exist: Click Create policy, choose the policy type you use, set scope to All accounts, enable Automatic remediation, and create the policy
4. If policies exist with Noncompliant accounts: Open the policy > Edit > enable Automatic remediation and ensure scope includes All accounts > Save
5. In AWS Config (organization management account): Settings > Organization settings > Enable recording for all accounts and all regions > Save
6. Return to each Firewall Manager policy and verify Accounts within policy scope show Compliant

## 参考資料

- [https://aws.amazon.com/firewall-manager/faqs/](https://aws.amazon.com/firewall-manager/faqs/)
- [https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-fms-intro.html](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-fms-intro.html)
- [https://www.amazonaws.cn/en/firewall-manager/faqs/](https://www.amazonaws.cn/en/firewall-manager/faqs/)
- [https://docs.aws.amazon.com/waf/latest/developerguide/fms-compliance.html](https://docs.aws.amazon.com/waf/latest/developerguide/fms-compliance.html)

## 技術情報

- Source Metadata：[sources/aws/fms_policy_compliant/metadata.json](../../sources/aws/fms_policy_compliant/metadata.json)
- Source Code：[sources/aws/fms_policy_compliant/check.py](../../sources/aws/fms_policy_compliant/check.py)
- Source Metadata Path：`sources/aws/fms_policy_compliant/metadata.json`
- Source Code Path：`sources/aws/fms_policy_compliant/check.py`
