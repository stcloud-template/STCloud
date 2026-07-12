# SNS subscription uses an HTTPS endpoint

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `sns_subscription_not_using_http_endpoints` |
| クラウドプラットフォーム | AWS |
| サービス | sns |
| 重大度 | high |
| カテゴリ | encryption |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Effects/Data Exposure |
| リソースタイプ | AwsSnsTopic |
| リソースグループ | messaging |

## 説明

Amazon SNS subscriptions are evaluated for endpoint protocol. Subscriptions using `http` are identified, while **HTTPS** endpoints indicate encrypted delivery in transit.

## リスク

Using **HTTP** leaves SNS deliveries unencrypted, compromising **confidentiality** via eavesdropping. MITM attackers can modify payloads or headers, damaging **integrity**, inject malicious content into downstream systems, or capture subscription data for spoofing and unauthorized actions.

## 推奨事項

Require **HTTPS** for all SNS subscription endpoints. Prefer domain-based endpoints, verify SNS message signatures, and apply **least privilege**. Enforce TLS using IAM conditions like `aws:SecureTransport`, and use private connectivity (VPC endpoints) where possible for defense in depth.

## 修正手順


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

## 参考資料

- [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sns-subscription.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sns-subscription.html)
- [https://docs.aws.amazon.com/sns/latest/dg/sns-security-best-practices.html#enforce-encryption-data-in-transit](https://docs.aws.amazon.com/sns/latest/dg/sns-security-best-practices.html#enforce-encryption-data-in-transit)

## 技術情報

- Source Metadata：[sources/aws/sns_subscription_not_using_http_endpoints/metadata.json](../../sources/aws/sns_subscription_not_using_http_endpoints/metadata.json)
- Source Code：[sources/aws/sns_subscription_not_using_http_endpoints/check.py](../../sources/aws/sns_subscription_not_using_http_endpoints/check.py)
- Source Metadata Path：`sources/aws/sns_subscription_not_using_http_endpoints/metadata.json`
- Source Code Path：`sources/aws/sns_subscription_not_using_http_endpoints/check.py`
