# AWS WAF Classic Global rule has at least one condition

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `waf_global_rule_with_conditions` |
| 云平台 | AWS |
| 服务 | waf |
| 严重等级 | medium |
| 类别 | internet-exposed |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls |
| 资源类型 | AwsWafRule |
| 资源组 | security |

## 描述

**AWS WAF Classic global rules** contain at least one **condition** that matches HTTP(S) requests the rule evaluates for action (e.g., `allow`, `block`, `count`).

## 风险

**No-condition rules** never match traffic, providing no filtering. Malicious requests (SQLi/XSS, bots) can reach origins, impacting **confidentiality** (data exfiltration), **integrity** (tampering), and **availability** (service disruption). They may also create a false sense of coverage.

## 推荐措施

Attach at least one precise **condition** to every rule, aligned to known threats and application context. Apply **least privilege** for traffic, use managed rule groups for **defense in depth**, and routinely review rules to remove placeholders. *If on Classic*, plan migration to WAFv2.

## 修复步骤


### CLI

```text
aws waf update-rule --rule-id <example_resource_id> --change-token <example_change_token> --updates '[{"Action":"INSERT","Predicate":{"Negated":false,"Type":"IPMatch","DataId":"<example_resource_id>"}}]' --region us-east-1
```

### Native IaC

```yaml
# CloudFormation: ensure the WAF Classic Global rule has at least one condition
Resources:
  <example_resource_name>:
    Type: AWS::WAF::Rule
    Properties:
      Name: <example_resource_name>
      MetricName: <example_metric_name>
      # Critical: add at least one predicate (condition) so the rule is not empty
      Predicates:
        - Negated: false  # evaluate as-is
          Type: IPMatch
          DataId: <example_resource_id>  # existing IPSet ID
```

### Terraform

```hcl
# Ensure the WAF Classic Global rule has at least one condition
resource "aws_waf_rule" "<example_resource_name>" {
  name        = "<example_resource_name>"
  metric_name = "<example_metric_name>"

  # Critical: add at least one predicate (condition) so the rule is not empty
  predicate {
    data_id = "<example_resource_id>"  # existing IPSet ID
    negated = false
    type    = "IPMatch"
  }
}
```

### Other

1. Open the AWS Console > AWS WAF, then click Switch to AWS WAF Classic
2. In Global (CloudFront) scope, go to Rules and select the target rule
3. Click Edit (or Add rule) > Add condition
4. Choose a condition type (e.g., IP match), select an existing condition, set it to does (not negated)
5. Click Update/Save to apply

## 参考资料

- [https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-rules-editing.html](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-rules-editing.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html#waf-6](https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html#waf-6)
- [https://docs.aws.amazon.com/config/latest/developerguide/waf-global-rule-not-empty.html](https://docs.aws.amazon.com/config/latest/developerguide/waf-global-rule-not-empty.html)

## 技术信息

- Source Metadata：[sources/aws/waf_global_rule_with_conditions/metadata.json](../../sources/aws/waf_global_rule_with_conditions/metadata.json)
- Source Code：[sources/aws/waf_global_rule_with_conditions/check.py](../../sources/aws/waf_global_rule_with_conditions/check.py)
- Source Metadata Path：`sources/aws/waf_global_rule_with_conditions/metadata.json`
- Source Code Path：`sources/aws/waf_global_rule_with_conditions/check.py`
