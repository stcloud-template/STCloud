# AWS EventBridge event bus policy does not allow public access

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `eventbridge_bus_exposed` |
| 云平台 | AWS |
| 服务 | eventbridge |
| 严重等级 | high |
| 类别 | internet-exposed |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Initial Access/Unauthorized Access |
| 资源类型 | AwsEventsEventbus |
| 资源组 | messaging |

## 描述

EventBridge event bus resource policy is evaluated for **public access**, such as a `Principal: "*"` or overly broad conditions that allow any AWS account to publish events or manage rules on the bus.

## 风险

Publicly accessible event buses enable **event injection** and unauthorized rule changes, undermining **integrity** and enabling **lateral movement**. Attackers can trigger downstream targets, causing **data exposure**, service disruption, and unexpected **costs** through high-volume events.

## 推荐措施

Apply **least privilege** resource policies: limit principals to specific accounts or your organization, and constrain actions and event attributes (e.g., `source`, `detail-type`). Avoid `Principal: "*"`. Use **defense in depth** with rule patterns that include the expected `account`. Monitor policy changes and bus activity.

## 修复步骤


### CLI

```text
aws events remove-permission --event-bus-name <event_bus_name> --statement-id <statement_id>
```

### Native IaC

```yaml
# CloudFormation: restrict EventBridge event bus access to a specific account (not public)
Resources:
  <example_resource_name>:
    Type: AWS::Events::EventBusPolicy
    Properties:
      StatementId: AllowSpecificAccount
      Action: events:PutEvents
      Principal: arn:aws:iam::<example_account_id>:root  # CRITICAL: limit access to a specific AWS account to prevent public access
      # Omitting EventBusName applies this to the default event bus
```

### Terraform

```hcl
resource "aws_cloudwatch_event_bus_policy" "<example_resource_name>" {
  # CRITICAL: Principal is a specific AWS account, not "*", preventing public access
  policy = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "AllowSpecificAccount",
    "Effect": "Allow",
    "Principal": {"AWS": "arn:aws:iam::<example_account_id>:root"},
    "Action": "events:PutEvents",
    "Resource": "arn:aws:events:<example_region>:<example_account_id>:event-bus/default"
  }]
}
POLICY
}
```

### Other

1. Open the AWS Console and go to EventBridge > Event buses
2. Select the target event bus and open the Permissions tab
3. Click Edit policy
4. Remove any statement where Principal is "*" or AWS is "*"
5. If needed, add a statement allowing only your trusted account ID as Principal (arn:aws:iam::<ACCOUNT_ID>:root)
6. Save changes

## 参考资料

- [https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEvents-CrossAccountEventDelivery.html](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEvents-CrossAccountEventDelivery.html)
- [https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CWE_GettingStarted.html](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CWE_GettingStarted.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudWatchEvents/event-bus-exposed.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudWatchEvents/event-bus-exposed.html)
- [https://aws.amazon.com/blogs/compute/simplifying-cross-account-access-with-amazon-eventbridge-resource-policies/](https://aws.amazon.com/blogs/compute/simplifying-cross-account-access-with-amazon-eventbridge-resource-policies/)

## 技术信息

- Source Metadata：[sources/aws/eventbridge_bus_exposed/metadata.json](../../sources/aws/eventbridge_bus_exposed/metadata.json)
- Source Code：[sources/aws/eventbridge_bus_exposed/check.py](../../sources/aws/eventbridge_bus_exposed/check.py)
- Source Metadata Path：`sources/aws/eventbridge_bus_exposed/metadata.json`
- Source Code Path：`sources/aws/eventbridge_bus_exposed/check.py`
