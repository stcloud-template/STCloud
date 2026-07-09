# SNS subscription uses an HTTPS endpoint

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `sns_subscription_not_using_http_endpoints` |
| 云平台 | AWS |
| 服务 | sns |
| 严重等级 | high |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Effects/Data Exposure |
| 资源类型 | AwsSnsTopic |
| 资源组 | messaging |

## 描述

Amazon SNS subscriptions are evaluated for endpoint protocol. Subscriptions using `http` are identified, while **HTTPS** endpoints indicate encrypted delivery in transit.

## 风险

Using **HTTP** leaves SNS deliveries unencrypted, compromising **confidentiality** via eavesdropping. MITM attackers can modify payloads or headers, damaging **integrity**, inject malicious content into downstream systems, or capture subscription data for spoofing and unauthorized actions.

## 推荐措施

Require **HTTPS** for all SNS subscription endpoints. Prefer domain-based endpoints, verify SNS message signatures, and apply **least privilege**. Enforce TLS using IAM conditions like `aws:SecureTransport`, and use private connectivity (VPC endpoints) where possible for defense in depth.

## 修复步骤


### Native IaC

```yaml
# CloudFormation: Ensure SNS subscription uses HTTPS
Resources:
  <example_resource_name>:
    Type: AWS::SNS::Subscription
    Properties:
      TopicArn: <example_resource_id>
      Protocol: https              # Critical: use HTTPS protocol to remediate HTTP usage
      Endpoint: https://<example_endpoint>  # Critical: HTTPS endpoint URL
```

### Terraform

```hcl
# Terraform: Ensure SNS subscription uses HTTPS
resource "aws_sns_topic_subscription" "<example_resource_name>" {
  topic_arn = "<example_resource_id>"
  protocol  = "https"                      # Critical: enforce HTTPS protocol
  endpoint  = "https://<example_endpoint>" # Critical: HTTPS endpoint URL
}
```

### Other

1. Open the Amazon SNS console and go to Subscriptions
2. Select the subscription with Protocol set to HTTP and click Delete
3. Click Create subscription
4. Choose the same Topic ARN, set Protocol to HTTPS, and enter your HTTPS endpoint URL
5. Create the subscription and confirm it from your endpoint if required

## 参考资料

- [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sns-subscription.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sns-subscription.html)
- [https://docs.aws.amazon.com/sns/latest/dg/sns-security-best-practices.html#enforce-encryption-data-in-transit](https://docs.aws.amazon.com/sns/latest/dg/sns-security-best-practices.html#enforce-encryption-data-in-transit)

## 技术信息

- Source Metadata：[sources/aws/sns_subscription_not_using_http_endpoints/metadata.json](../../sources/aws/sns_subscription_not_using_http_endpoints/metadata.json)
- Source Code：[sources/aws/sns_subscription_not_using_http_endpoints/check.py](../../sources/aws/sns_subscription_not_using_http_endpoints/check.py)
- Source Metadata Path：`sources/aws/sns_subscription_not_using_http_endpoints/metadata.json`
- Source Code Path：`sources/aws/sns_subscription_not_using_http_endpoints/check.py`
