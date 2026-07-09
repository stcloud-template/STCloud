# Internet-facing Application Load Balancer is protected by AWS Shield Advanced

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `shield_advanced_protection_in_internet_facing_load_balancers` |
| 云平台 | AWS |
| 服务 | shield |
| 严重等级 | medium |
| 类别 | internet-exposed, resilience |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Effects/Denial of Service |
| 资源类型 | AwsElbv2LoadBalancer |
| 资源组 | network |

## 描述

**Application Load Balancers** that are **internet-facing** are evaluated for an associated **AWS Shield Advanced** protection. Scope includes ALBs of type application with external exposure.

## 风险

Without enhanced DDoS protection, internet-facing ALBs are exposed to volumetric L3/L4 floods and HTTP L7 floods, compromising **availability** via outages and latency spikes. Sudden scaling can raise **costs**, while reduced visibility and response support extend disruption across dependent services.

## 推荐措施

Register internet-facing ALBs as **Shield Advanced protected resources** to strengthen **availability**. Use defense-in-depth: pair with **AWS WAF** for L7 filtering and rate limits, group related assets, enable health-based detection and proactive engagement, and enforce least-privilege IAM with continuous monitoring.

## 修复步骤


### CLI

```text
aws shield create-protection --name <ALB_NAME> --resource-arn <ALB_ARN>
```

### Native IaC

```yaml
Resources:
  ShieldProtection:
    Type: AWS::Shield::Protection
    Properties:
      Name: "<example_resource_name>"
      ResourceArn: "<example_resource_id>" # CRITICAL: Set to the ALB ARN to enable Shield Advanced protection for it
```

### Terraform

```hcl
resource "aws_shield_protection" "protect" {
  name         = "<example_resource_name>"
  resource_arn = "<example_resource_id>" # CRITICAL: ALB ARN; creating this enables Shield Advanced on the ALB
}
```

### Other

1. In the AWS Console, open AWS WAF & Shield
2. Go to Shield > Protected resources
3. Click Add resources to protect
4. Select the Region and resource type Application Load Balancer
5. Select your internet-facing ALB
6. Click Protect with Shield Advanced

## 参考资料

- [https://aws.amazon.com/documentation-overview/shield/](https://aws.amazon.com/documentation-overview/shield/)
- [https://docs.aws.amazon.com/waf/latest/developerguide/configure-new-protection.html](https://docs.aws.amazon.com/waf/latest/developerguide/configure-new-protection.html)

## 技术信息

- Source Metadata：[sources/aws/shield_advanced_protection_in_internet_facing_load_balancers/metadata.json](../../sources/aws/shield_advanced_protection_in_internet_facing_load_balancers/metadata.json)
- Source Code：[sources/aws/shield_advanced_protection_in_internet_facing_load_balancers/check.py](../../sources/aws/shield_advanced_protection_in_internet_facing_load_balancers/check.py)
- Source Metadata Path：`sources/aws/shield_advanced_protection_in_internet_facing_load_balancers/metadata.json`
- Source Code Path：`sources/aws/shield_advanced_protection_in_internet_facing_load_balancers/check.py`
