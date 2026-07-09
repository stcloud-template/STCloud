# AWS WAFv2 Web ACL has at least one rule or rule group attached

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `wafv2_webacl_with_rules` |
| 云平台 | AWS |
| 服务 | wafv2 |
| 严重等级 | high |
| 类别 | internet-exposed |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls |
| 资源类型 | AwsWafv2WebAcl |
| 资源组 | security |

## 描述

**AWS WAFv2 web ACLs** are evaluated for the presence of at least one configured **rule** or **rule group** that defines how HTTP(S) requests are inspected and acted upon.

## 风险

Without rules, traffic is governed only by the web ACL `DefaultAction`, often allowing requests without inspection. This increases risks to **confidentiality** (data exfiltration via injection), **integrity** (XSS/parameter tampering), and **availability** (layer-7 DDoS, bot abuse).

## 推荐措施

Populate each web ACL with targeted rules or managed rule groups to enforce least-privilege web access: cover common exploits (SQLi/XSS), IP reputation, and rate limits, scoped to your apps. Use a conservative `DefaultAction`, monitor metrics/logs, and continually tune-supporting **defense in depth** and **zero trust**.

## 修复步骤


### Native IaC

```yaml
# CloudFormation: Add at least one rule to the WAFv2 WebACL
Resources:
  <example_resource_name>:
    Type: AWS::WAFv2::WebACL
    Properties:
      Scope: REGIONAL
      DefaultAction:
        Allow: {}
      VisibilityConfig:
        SampledRequestsEnabled: true
        CloudWatchMetricsEnabled: true
        MetricName: <example_resource_name>
      Rules:  # CRITICAL: Adding any rule/rule group here fixes the finding by making the Web ACL non-empty
        - Name: <example_rule_name>
          Priority: 0
          Statement:
            ManagedRuleGroupStatement:
              VendorName: AWS
              Name: AWSManagedRulesCommonRuleSet  # Uses an AWS managed rule group
          OverrideAction:
            Count: {}  # Non-blocking to minimize impact
          VisibilityConfig:
            SampledRequestsEnabled: true
            CloudWatchMetricsEnabled: true
            MetricName: <example_rule_name>
```

### Terraform

```hcl
# Terraform: Ensure the WAFv2 Web ACL has at least one rule
resource "aws_wafv2_web_acl" "<example_resource_name>" {
  name  = "<example_resource_name>"
  scope = "REGIONAL"

  default_action {
    allow {}
  }

  visibility_config {
    cloudwatch_metrics_enabled = true
    metric_name                = "<example_resource_name>"
    sampled_requests_enabled   = true
  }

  rule { # CRITICAL: Presence of this rule makes the Web ACL non-empty and passes the check
    name     = "<example_rule_name>"
    priority = 0
    statement {
      managed_rule_group_statement {
        name        = "AWSManagedRulesCommonRuleSet"
        vendor_name = "AWS"  # Minimal managed rule group
      }
    }
    override_action { count {} } # Non-blocking
    visibility_config {
      cloudwatch_metrics_enabled = true
      metric_name                = "<example_rule_name>"
      sampled_requests_enabled   = true
    }
  }
}
```

### Other

1. In the AWS Console, go to AWS WAF
2. Open Web ACLs and select the failing Web ACL
3. Go to the Rules tab and click Add rules
4. Choose Add managed rule group, select AWS > AWSManagedRulesCommonRuleSet
5. Set action to Count (to avoid blocking), then Add rule and Save
6. Verify the Web ACL now shows at least one rule

## 参考资料

- [https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-editing.html](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-editing.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html#waf-10](https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html#waf-10)
- [https://support.icompaas.com/support/solutions/articles/62000233642-ensure-aws-wafv2-webacl-has-at-least-one-rule-or-rule-group](https://support.icompaas.com/support/solutions/articles/62000233642-ensure-aws-wafv2-webacl-has-at-least-one-rule-or-rule-group)

## 技术信息

- Source Metadata：[sources/aws/wafv2_webacl_with_rules/metadata.json](../../sources/aws/wafv2_webacl_with_rules/metadata.json)
- Source Code：[sources/aws/wafv2_webacl_with_rules/check.py](../../sources/aws/wafv2_webacl_with_rules/check.py)
- Source Metadata Path：`sources/aws/wafv2_webacl_with_rules/metadata.json`
- Source Code Path：`sources/aws/wafv2_webacl_with_rules/check.py`
