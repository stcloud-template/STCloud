# EventBridge global endpoint has event replication enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `eventbridge_global_endpoint_event_replication_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | eventbridge |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | AwsEventsEndpoint |
| リソースグループ | messaging |

## 説明

**EventBridge global endpoints** are configured with **event replication** `ENABLED` (not `DISABLED`) so custom events are replicated to both the primary and secondary Regions.

## リスク

**No event replication** degrades **availability** and increases **RPO** during Regional outages. - Events can be lost or delayed if the primary Region fails - Automatic recovery to the primary may not occur, prolonging failover - Cross-Region inconsistency can affect data integrity

## 推奨事項

Turn on **event replication** for global endpoints to ensure Regional resilience. Keep event buses, rules, and targets aligned across Regions. Use a dedicated IAM role with **least privilege** for replication. Design consumers for **idempotency** with unique IDs. Regularly test failover and monitor health as part of **defense in depth**.

## 修正手順


### CLI

```text
aws events update-endpoint --name <endpoint-name> --replication-config State=ENABLED --role-arn <role-arn>
```

### Native IaC

```yaml
# CloudFormation: Enable event replication on an EventBridge global endpoint
Resources:
  Endpoint:
    Type: AWS::Events::Endpoint
    Properties:
      Name: <example_resource_name>
      EventBuses:
        - EventBusArn: arn:aws:events:us-east-1:<example_resource_id>:event-bus/<example_resource_name>
        - EventBusArn: arn:aws:events:us-west-2:<example_resource_id>:event-bus/<example_resource_name>
      RoutingConfig:
        FailoverConfig:
          Primary:
            HealthCheck: arn:aws:route53:::healthcheck/<example_resource_id>
          Secondary:
            Route: us-west-2
      ReplicationConfig:
        State: ENABLED  # Critical: enables event replication
      RoleArn: arn:aws:iam::<example_resource_id>:role/<example_resource_name>  # Critical: role used by replication
```

### Terraform

```hcl
# Terraform (awscc): Enable event replication on an EventBridge global endpoint
resource "awscc_events_endpoint" "example" {
  name = "<example_resource_name>"

  event_buses = [
    { event_bus_arn = "arn:aws:events:us-east-1:<example_resource_id>:event-bus/<example_resource_name>" },
    { event_bus_arn = "arn:aws:events:us-west-2:<example_resource_id>:event-bus/<example_resource_name>" }
  ]

  routing_config = {
    failover_config = {
      primary   = { health_check = "arn:aws:route53:::healthcheck/<example_resource_id>" }
      secondary = { route        = "us-west-2" }
    }
  }

  replication_config = { state = "ENABLED" }  # Critical: enables event replication
  role_arn           = "arn:aws:iam::<example_resource_id>:role/<example_resource_name>"  # Critical: role used by replication
}
```

### Other

1. In the AWS Console, open Amazon EventBridge and go to Global endpoints
2. Select the endpoint and choose Edit
3. Under Event replication, check Event replication enabled
4. For Execution role, select an existing role or create a new one
5. Save changes

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/eventbridge-controls.html#eventbridge-4](https://docs.aws.amazon.com/securityhub/latest/userguide/eventbridge-controls.html#eventbridge-4)
- [https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-global-endpoints.html](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-global-endpoints.html)
- [https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_Endpoint.html](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_Endpoint.html)
- [https://docs.aws.amazon.com/config/latest/developerguide/global-endpoint-event-replication-enabled.html](https://docs.aws.amazon.com/config/latest/developerguide/global-endpoint-event-replication-enabled.html)
- [https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-ge-create-endpoint.html](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-ge-create-endpoint.html)
- [https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-ge-best-practices.html](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-ge-best-practices.html)
- [https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateEndpoint.html](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateEndpoint.html)
- [https://aws.amazon.com/blogs/compute/introducing-global-endpoints-for-amazon-eventbridge/](https://aws.amazon.com/blogs/compute/introducing-global-endpoints-for-amazon-eventbridge/)

## 技術情報

- Source Metadata：[sources/aws/eventbridge_global_endpoint_event_replication_enabled/metadata.json](../../sources/aws/eventbridge_global_endpoint_event_replication_enabled/metadata.json)
- Source Code：[sources/aws/eventbridge_global_endpoint_event_replication_enabled/check.py](../../sources/aws/eventbridge_global_endpoint_event_replication_enabled/check.py)
- Source Metadata Path：`sources/aws/eventbridge_global_endpoint_event_replication_enabled/metadata.json`
- Source Code Path：`sources/aws/eventbridge_global_endpoint_event_replication_enabled/check.py`
