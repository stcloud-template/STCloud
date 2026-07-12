# AWS EventBridge event bus does not allow cross-account access

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `eventbridge_bus_cross_account_access` |
| クラウドプラットフォーム | AWS |
| サービス | eventbridge |
| 重大度 | high |
| カテゴリ | identity-access, trust-boundaries |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Initial Access/Unauthorized Access, Effects/Data Exposure |
| リソースタイプ | AwsEventsEventbus |
| リソースグループ | messaging |

## 説明

**EventBridge event bus** has a **resource policy** that grants **cross-account event delivery** to principals outside the account, including broad or public access. Focus is on buses whose policies permit external accounts to send events.

## リスク

**Cross-account event injection** can erode **integrity** and **availability**. Spoofed events may trigger rules and invoke downstream targets, causing unintended actions, data exposure via targets, lateral movement through over-privileged roles, and cost or service disruption from event floods.

## 推奨事項

Apply **least privilege** on the event bus resource policy: allow only specific account IDs or org scope (e.g., `aws:PrincipalOrgID`) and avoid wildcard `Principal` or `*`. Constrain rules to trusted senders using the `account` field and vetted sources, and add monitoring/throttling for **defense in depth**.

## 修正手順


### CLI

```text
aws events remove-permission --event-bus-name <event_bus_name> --statement-id <statement_id>
```

### Native IaC

```yaml
# CloudFormation: restrict EventBridge event bus to same account only
Resources:
  <example_resource_name>:
    Type: AWS::Events::EventBusPolicy
    Properties:
      StatementId: <example_resource_id>
      Action: events:PutEvents
      Principal: !Ref AWS::AccountId  # Critical: allows only this AWS account, blocking cross-account access
      EventBusName: <example_resource_name>
```

### Terraform

```hcl
# Terraform: restrict EventBridge event bus to same account only
resource "aws_cloudwatch_event_permission" "<example_resource_name>" {
  statement_id   = "<example_resource_id>"
  action         = "events:PutEvents"
  principal      = "<example_resource_id>" # Critical: set to your own AWS account ID to block cross-account access
  event_bus_name = "<example_resource_name>"
}
```

### Other

1. In the AWS Console, go to Amazon EventBridge > Event buses
2. Select the event bus (<event_bus_name>)
3. Open the Permissions tab and click Edit
4. Remove any statements that grant access to other accounts, an organization, or "*"
5. Save changes

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudWatchEvents/event-bus-cross-account-access.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudWatchEvents/event-bus-cross-account-access.html)
- [https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CWE_GettingStarted.html](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CWE_GettingStarted.html)
- [https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEvents-CrossAccountEventDelivery.html](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEvents-CrossAccountEventDelivery.html)

## 技術情報

- Source Metadata：[sources/aws/eventbridge_bus_cross_account_access/metadata.json](../../sources/aws/eventbridge_bus_cross_account_access/metadata.json)
- Source Code：[sources/aws/eventbridge_bus_cross_account_access/check.py](../../sources/aws/eventbridge_bus_cross_account_access/check.py)
- Source Metadata Path：`sources/aws/eventbridge_bus_cross_account_access/metadata.json`
- Source Code Path：`sources/aws/eventbridge_bus_cross_account_access/check.py`
