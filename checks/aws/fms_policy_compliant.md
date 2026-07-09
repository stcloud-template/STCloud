# All AWS FMS policies in the admin account are compliant for all accounts

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `fms_policy_compliant` |
| 云平台 | AWS |
| 服务 | fms |
| 严重等级 | medium |
| 类别 | internet-exposed, trust-boundaries |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | Other |
| 资源组 | security |

## 描述

**Firewall Manager** policies in the administrator account are evaluated for organization-wide compliance. The assessment reviews each policy's account-level status and flags entries marked `NON_COMPLIANT` or unset. It also identifies when no effective policies exist within the administrator scope.

## 风险

Policy drift or absence leaves in-scope resources without enforced controls, degrading **confidentiality**, **integrity**, and **availability**. Missing WAF, Shield, security group, or network firewall baselines can enable DDoS exposure, unsafe routes, and open access, leading to unauthorized entry and data exfiltration.

## 推荐措施

Maintain centralized enforcement with **Firewall Manager**: define mandatory policies for all relevant accounts/resources, enable automatic remediation where appropriate, and continuously monitor compliance. Apply **least privilege** and **defense in depth** by standardizing web, network, and DNS protections and alerting on drift.

## 修复步骤


### Other

1. Sign in to the AWS console with the Firewall Manager administrator account
2. Open Firewall Manager > Security policies
3. If no policies exist: Click Create policy, choose the policy type you use, set scope to All accounts, enable Automatic remediation, and create the policy
4. If policies exist with Noncompliant accounts: Open the policy > Edit > enable Automatic remediation and ensure scope includes All accounts > Save
5. In AWS Config (organization management account): Settings > Organization settings > Enable recording for all accounts and all regions > Save
6. Return to each Firewall Manager policy and verify Accounts within policy scope show Compliant

## 参考资料

- [https://aws.amazon.com/firewall-manager/faqs/](https://aws.amazon.com/firewall-manager/faqs/)
- [https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-fms-intro.html](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-fms-intro.html)
- [https://www.amazonaws.cn/en/firewall-manager/faqs/](https://www.amazonaws.cn/en/firewall-manager/faqs/)
- [https://docs.aws.amazon.com/waf/latest/developerguide/fms-compliance.html](https://docs.aws.amazon.com/waf/latest/developerguide/fms-compliance.html)

## 技术信息

- Source Metadata：[sources/aws/fms_policy_compliant/metadata.json](../../sources/aws/fms_policy_compliant/metadata.json)
- Source Code：[sources/aws/fms_policy_compliant/check.py](../../sources/aws/fms_policy_compliant/check.py)
- Source Metadata Path：`sources/aws/fms_policy_compliant/metadata.json`
- Source Code Path：`sources/aws/fms_policy_compliant/check.py`
