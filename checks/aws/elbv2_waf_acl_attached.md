# Application Load Balancer has a WAF Web ACL attached

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `elbv2_waf_acl_attached` |
| 云平台 | AWS |
| 服务 | elbv2 |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Initial Access |
| 资源类型 | AwsElbv2LoadBalancer |
| 资源组 | network |

## 描述

Application Load Balancers are evaluated for an associated **AWS WAF web ACL** that governs HTTP(S) requests. The evaluation detects ALBs missing a web ACL and recognizes associations from **WAFv2** or regional **WAF Classic**.

## 风险

Absent a **WAF web ACL**, ALBs accept unfiltered Layer 7 traffic, enabling: - **Injection** (SQLi/XSS) harming confidentiality and integrity - **Credential stuffing** and **bot abuse** - **Resource exhaustion** degrading availability

## 推荐措施

Associate a **WAF web ACL** with each ALB as **defense in depth**. Use managed and custom rules, IP reputation lists, and rate limiting to block attacks. Continuously tune policies and monitor logs. *Apply least privilege* by scoping rules to required paths, methods, and sources.

## 修复步骤


### CLI

```text
aws wafv2 associate-web-acl --web-acl-arn <WEB_ACL_ARN> --resource-arn <ALB_ARN>
```

### Native IaC

```yaml
# CloudFormation: associate an existing WAFv2 Web ACL to an ALB
Resources:
  <example_resource_name>:
    Type: AWS::WAFv2::WebACLAssociation
    Properties:
      ResourceArn: <example_resource_id>  # CRITICAL: ALB ARN to protect
      WebACLArn: <example_resource_id>    # CRITICAL: WAFv2 Web ACL ARN to attach
```

### Terraform

```hcl
# Associate WAFv2 Web ACL with an ALB
resource "aws_wafv2_web_acl_association" "<example_resource_name>" {
  resource_arn = "<example_resource_id>" # CRITICAL: ALB ARN
  web_acl_arn  = "<example_resource_id>" # CRITICAL: WAFv2 Web ACL ARN
}
```

### Other

1. In the AWS Console, open **WAF & Shield**
2. Go to **Web ACLs** and select your regional Web ACL
3. Click **Associated AWS resources** > **Associate resource**
4. Select the target **Application Load Balancer** and click **Associate**

## 参考资料

- [https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-associating-aws-resource.html](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-associating-aws-resource.html)

## 技术信息

- Source Metadata：[sources/aws/elbv2_waf_acl_attached/metadata.json](../../sources/aws/elbv2_waf_acl_attached/metadata.json)
- Source Code：[sources/aws/elbv2_waf_acl_attached/check.py](../../sources/aws/elbv2_waf_acl_attached/check.py)
- Source Metadata Path：`sources/aws/elbv2_waf_acl_attached/metadata.json`
- Source Code Path：`sources/aws/elbv2_waf_acl_attached/check.py`
