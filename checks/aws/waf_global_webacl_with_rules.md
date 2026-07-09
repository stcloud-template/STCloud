# AWS WAF Classic global Web ACL has at least one rule or rule group

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `waf_global_webacl_with_rules` |
| 云平台 | AWS |
| 服务 | waf |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls |
| 资源类型 | AwsWafWebAcl |
| 资源组 | security |

## 描述

**AWS WAF Classic global web ACLs** are evaluated for the presence of at least one **rule** or **rule group** that inspects HTTP(S) requests

## 风险

With no rules, the web ACL relies solely on its default action. If `allow`, hostile traffic reaches origins uninspected; if `block`, legitimate traffic can be denied. - SQLi/XSS can expose data (confidentiality) - Malicious requests can alter state (integrity) - Bots and scraping can drain resources (availability)

## 推荐措施

Populate each global web ACL with effective protections: - Use rule groups and targeted rules (managed, rate-based, IP sets) - Apply least privilege: default `block` where feasible; explicitly `allow` required traffic - Layer defenses and enable logging to tune policies - *Consider migrating to WAFv2*

## 修复步骤


### CLI

```text
aws waf update-web-acl --web-acl-id <WEB_ACL_ID> --change-token <CHANGE_TOKEN> --updates '[{"Action":"INSERT","ActivatedRule":{"Priority":1,"RuleId":"<RULE_ID>","Action":{"Type":"BLOCK"}}}]'
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::WAF::WebACL
    Properties:
      Name: <example_resource_name>
      MetricName: <example_metric_name>
      DefaultAction:
        Type: ALLOW
      Rules:
        - Action:
            Type: BLOCK
          Priority: 1
          RuleId: <example_rule_id>  # Critical: Adds a rule so the Web ACL is not empty
          # This ensures the Web ACL has at least one rule, changing FAIL to PASS
```

### Terraform

```hcl
resource "aws_waf_web_acl" "<example_resource_name>" {
  name        = "<example_resource_name>"
  metric_name = "<example_metric_name>"

  default_action {
    type = "ALLOW"
  }

  rules { # Critical: Adds at least one rule so the Web ACL is not empty
    priority = 1
    rule_id  = "<example_rule_id>"
    type     = "REGULAR"
    action {
      type = "BLOCK"
    }
  }
}
```

### Other

1. Open the AWS console and go to WAF
2. In the left menu, click Switch to AWS WAF Classic
3. At the top, set Filter to Global (CloudFront)
4. Click Web ACLs and select your web ACL
5. On the Rules tab, click Edit web ACL
6. In Rules, select an existing rule or rule group and click Add rule to web ACL
7. Click Save changes

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html#waf-8](https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html#waf-8)
- [https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-editing.html](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-editing.html)
- [https://docs.aws.amazon.com/waf/latest/developerguide/waf-rules.html](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rules.html)

## 技术信息

- Source Metadata：[sources/aws/waf_global_webacl_with_rules/metadata.json](../../sources/aws/waf_global_webacl_with_rules/metadata.json)
- Source Code：[sources/aws/waf_global_webacl_with_rules/check.py](../../sources/aws/waf_global_webacl_with_rules/check.py)
- Source Metadata Path：`sources/aws/waf_global_webacl_with_rules/metadata.json`
- Source Code Path：`sources/aws/waf_global_webacl_with_rules/check.py`
