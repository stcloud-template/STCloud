# AWS WAFv2 Web ACL has Amazon CloudWatch metrics enabled for all rules and rule groups

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `wafv2_webacl_rule_logging_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | wafv2 |
| 重大度 | medium |
| カテゴリ | logging |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls |
| リソースタイプ | AwsWafv2WebAcl |
| リソースグループ | security |

## 説明

**AWS WAFv2 Web ACLs** are assessed to confirm that every associated **rule** and **rule group** has **CloudWatch metrics** enabled for visibility into rule evaluations and traffic

## リスク

Absent **CloudWatch metrics**, WAF telemetry is lost, masking spikes, rule bypasses, and misconfigurations. This delays detection of SQLi/XSS probes and bot floods, risking data confidentiality, request integrity, and application availability.

## 推奨事項

Enable **CloudWatch metrics** for all WAF rules and rule groups (*including managed rule groups*). Use consistent metric names, centralize dashboards and alerts, and review trends to validate rule efficacy. Integrate with a SIEM for **defense in depth** and tune rules based on telemetry.

## 修正手順


### Native IaC

```yaml
# CloudFormation: Enable CloudWatch metrics on WAFv2 Web ACL rules
Resources:
  <example_resource_name>:
    Type: AWS::WAFv2::WebACL
    Properties:
      Name: <example_resource_name>
      Scope: REGIONAL
      DefaultAction:
        Allow: {}
      VisibilityConfig:
        SampledRequestsEnabled: true
        CloudWatchMetricsEnabled: true
        MetricName: <metric_name>
      Rules:
        - Name: <example_rule_name>
          Priority: 1
          Statement:
            ManagedRuleGroupStatement:
              VendorName: AWS
              Name: AWSManagedRulesCommonRuleSet
          OverrideAction:
            None: {}
          VisibilityConfig:
            SampledRequestsEnabled: true
            CloudWatchMetricsEnabled: true  # Critical: enables CloudWatch metrics for this rule
            MetricName: <rule_metric_name>  # Required with CloudWatch metrics
```

### Terraform

```hcl
# Terraform: Enable CloudWatch metrics on WAFv2 Web ACL rules
resource "aws_wafv2_web_acl" "<example_resource_name>" {
  name  = "<example_resource_name>"
  scope = "REGIONAL"

  default_action { allow {} }

  visibility_config {
    cloudwatch_metrics_enabled = true
    metric_name                = "<metric_name>"
    sampled_requests_enabled   = true
  }

  rule {
    name     = "<example_rule_name>"
    priority = 1

    statement {
      managed_rule_group_statement {
        vendor_name = "AWS"
        name        = "AWSManagedRulesCommonRuleSet"
      }
    }

    override_action { none {} }

    visibility_config {
      cloudwatch_metrics_enabled = true  # Critical: enables CloudWatch metrics for this rule
      metric_name                = "<rule_metric_name>"  # Required with CloudWatch metrics
      sampled_requests_enabled   = true
    }
  }
}
```

### Other

1. In AWS Console, go to AWS WAF & Shield > Web ACLs, select the Web ACL
2. Open the Rules tab, edit each rule, and enable CloudWatch metrics (Visibility configuration > CloudWatch metrics enabled), then Save
3. For rule groups: go to AWS WAF & Shield > Rule groups, select the rule group, edit Visibility configuration, enable CloudWatch metrics, then Save

## 参考資料

- [https://support.icompaas.com/support/solutions/articles/62000233644-ensure-aws-wafv2-webacl-rule-or-rule-group-has-amazon-cloudwatch-metrics-enabled](https://support.icompaas.com/support/solutions/articles/62000233644-ensure-aws-wafv2-webacl-rule-or-rule-group-has-amazon-cloudwatch-metrics-enabled)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html](https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html#waf-12](https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html#waf-12)

## 技術情報

- Source Metadata：[sources/aws/wafv2_webacl_rule_logging_enabled/metadata.json](../../sources/aws/wafv2_webacl_rule_logging_enabled/metadata.json)
- Source Code：[sources/aws/wafv2_webacl_rule_logging_enabled/check.py](../../sources/aws/wafv2_webacl_rule_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/wafv2_webacl_rule_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/wafv2_webacl_rule_logging_enabled/check.py`
