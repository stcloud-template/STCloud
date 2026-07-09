# AWS WAF Classic global rule group has at least one rule

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `waf_global_rulegroup_not_empty` |
| 云平台 | AWS |
| 服务 | waf |
| 严重等级 | high |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls |
| 资源类型 | AwsWafRuleGroup |
| 资源组 | security |

## 描述

**AWS WAF Classic global rule groups** are assessed for the presence of **one or more rules**. Empty groups are identified even when referenced by a web ACL, meaning the group adds no match logic.

## 风险

An empty rule group performs no inspection, so web requests pass without WAF scrutiny. This creates blind spots enabling: - **Confidentiality**: data exfiltration via SQLi/XSS - **Integrity**: parameter tampering - **Availability**: bot abuse and layer-7 DoS It also creates a false sense of protection when attached.

## 推荐措施

Populate each rule group with **effective rules** aligned to application threats; choose `block` or `count` actions as appropriate. Prefer **managed rule groups** as a baseline and layer custom rules for **least privilege**. Avoid placeholder groups, test in staging, and monitor metrics to tune.

## 修复步骤


### CLI

```text
aws waf update-rule-group --rule-group-id <rule-group-id> --updates Action=INSERT,ActivatedRule={Priority=1,RuleId=<rule-id>,Action={Type=BLOCK}} --change-token <change-token> --region us-east-1
```

### Native IaC

```yaml
# CloudFormation: ensure the WAF Classic global rule group has at least one rule
Resources:
  <example_resource_name>:
    Type: AWS::WAF::RuleGroup
    Properties:
      Name: <example_resource_name>
      MetricName: examplemetric
      ActivatedRules:
        - Priority: 1                 # Critical: adds a rule to the group (makes it non-empty)
          RuleId: <example_resource_id>  # Critical: ID of the existing rule to add
          Action:
            Type: BLOCK              # Critical: required action when activating the rule
```

### Terraform

```hcl
# Terraform: ensure the WAF Classic global rule group has at least one rule
resource "aws_waf_rule_group" "<example_resource_name>" {
  name        = "<example_resource_name>"
  metric_name = "examplemetric"

  activated_rule {
    priority = 1                      # Critical: adds a rule to the group (makes it non-empty)
    rule_id  = "<example_resource_id>" # Critical: ID of the existing rule to add
    action {
      type = "BLOCK"                 # Critical: required action when activating the rule
    }
  }
}
```

### Other

1. Open the AWS Console and go to AWS WAF, then switch to AWS WAF Classic
2. At the top, set scope to Global (CloudFront)
3. Go to Rule groups and select the target rule group
4. Click Edit rule group
5. Select an existing rule, choose its action (e.g., BLOCK), and click Add rule to rule group
6. Click Update to save

## 参考资料

- [https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-groups.html](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-groups.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html#waf-7](https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html#waf-7)
- [https://docs.aws.amazon.com/waf/latest/developerguide/classic-rule-group-editing.html](https://docs.aws.amazon.com/waf/latest/developerguide/classic-rule-group-editing.html)

## 技术信息

- Source Metadata：[sources/aws/waf_global_rulegroup_not_empty/metadata.json](../../sources/aws/waf_global_rulegroup_not_empty/metadata.json)
- Source Code：[sources/aws/waf_global_rulegroup_not_empty/check.py](../../sources/aws/waf_global_rulegroup_not_empty/check.py)
- Source Metadata Path：`sources/aws/waf_global_rulegroup_not_empty/metadata.json`
- Source Code Path：`sources/aws/waf_global_rulegroup_not_empty/check.py`
