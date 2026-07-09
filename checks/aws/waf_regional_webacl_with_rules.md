# AWS WAF Classic Regional Web ACL has at least one rule or rule group

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `waf_regional_webacl_with_rules` |
| 云平台 | AWS |
| 服务 | waf |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls |
| 资源类型 | AwsWafRegionalWebAcl |
| 资源组 | security |

## 描述

**AWS WAF Classic Regional web ACL** contains at least one **rule** or **rule group** to inspect and act on HTTP(S) requests. An ACL with no entries is considered empty.

## 风险

With no rules, the web ACL performs no inspection, letting malicious traffic through. - **Confidentiality**: data exposure via SQLi/XSS - **Integrity**: unauthorized actions or tampering - **Availability**: abuse/bot traffic causing degradation or denial

## 推荐措施

Populate each web ACL with at least one **rule** or **rule group** that inspects requests and enforces **least privilege**. Apply defense in depth by combining managed and custom rules, include rate controls where appropriate, and review regularly. *Default to blocking undesired traffic; only permit required patterns*.

## 修复步骤


### CLI

```text
aws waf-regional update-web-acl --web-acl-id <your-web-acl-id> --change-token $(aws waf-regional get-change-token --query 'ChangeToken' --output text) --updates '[{"Action":"INSERT","ActivatedRule":{"Priority":1,"RuleId":"<your-rule-id>","Action":{"Type":"BLOCK"}}}]'
```

### Native IaC

```yaml
# CloudFormation: Ensure the Web ACL has at least one rule
Resources:
  <example_resource_name>:
    Type: AWS::WAFRegional::WebACL
    Properties:
      Name: "<example_resource_name>"
      MetricName: "<example_resource_name>"
      DefaultAction:
        Type: ALLOW
      # Critical: adding any rule to the Web ACL makes it non-empty and passes the check
      Rules:
        - Action:
            Type: BLOCK
          Priority: 1
          RuleId: "<example_resource_id>"  # Rule to insert into the Web ACL
```

### Terraform

```hcl
# Terraform: Ensure the Web ACL has at least one rule
resource "aws_wafregional_web_acl" "<example_resource_name>" {
  name        = "<example_resource_name>"
  metric_name = "<example_resource_name>"

  default_action {
    type = "ALLOW"
  }

  # Critical: add at least one rule so the Web ACL is not empty
  rules {
    priority = 1
    rule_id  = "<example_resource_id>"
    action {
      type = "BLOCK"
    }
  }
}
```

### Other

1. Open the AWS Console and go to AWS WAF
2. In the left pane, click Web ACLs and switch to AWS WAF Classic if prompted
3. Select the Regional Web ACL and open the Rules tab
4. Click Edit web ACL
5. In Rules, select an existing rule or rule group and choose Add rule to web ACL
6. Click Save changes

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html#waf-4](https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html#waf-4)
- [https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-editing.html](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-editing.html)
- [https://docs.aws.amazon.com/waf/latest/developerguide/waf-rules.html](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rules.html)

## 技术信息

- Source Metadata：[sources/aws/waf_regional_webacl_with_rules/metadata.json](../../sources/aws/waf_regional_webacl_with_rules/metadata.json)
- Source Code：[sources/aws/waf_regional_webacl_with_rules/check.py](../../sources/aws/waf_regional_webacl_with_rules/check.py)
- Source Metadata Path：`sources/aws/waf_regional_webacl_with_rules/metadata.json`
- Source Code Path：`sources/aws/waf_regional_webacl_with_rules/check.py`
