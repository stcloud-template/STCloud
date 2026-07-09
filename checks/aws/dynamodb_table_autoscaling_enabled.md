# DynamoDB table uses on-demand capacity or has auto scaling enabled for read and write capacity units

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `dynamodb_table_autoscaling_enabled` |
| 云平台 | AWS |
| 服务 | dynamodb |
| 严重等级 | medium |
| 类别 | resilience |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Effects/Denial of Service, Effects/Resource Consumption |
| 资源类型 | AwsDynamoDbTable |
| 资源组 | database |

## 描述

**DynamoDB tables** use **automatic capacity scaling** via `on-demand` mode or `PROVISIONED` mode with **auto scaling** enabled for both `read` and `write` capacity units. Provisioned tables are evaluated for scaling on both dimensions.

## 风险

**Insufficient capacity scaling** causes throttling that degrades **availability** and increases latency. Sustained throttling can trigger retry storms, timeouts, and backlogs, risking missed writes or out-of-order processing that impacts **data integrity** and drives **operational costs**.

## 推荐措施

Adopt **elastic capacity**: prefer `on-demand` for unpredictable traffic, or use `PROVISIONED` with **auto scaling** on both reads and writes. Define safe utilization targets and bounds, monitor consumption, and plan for bursts to maintain **availability** and **resilience** over manual fixed throughput.

## 修复步骤


### CLI

```text
aws dynamodb update-table --table-name <table-name> --billing-mode PAY_PER_REQUEST
```

### Native IaC

```yaml
# CloudFormation: Set table to on-demand capacity
Resources:
  <example_resource_name>:
    Type: AWS::DynamoDB::Table
    Properties:
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: S
      KeySchema:
        - AttributeName: id
          KeyType: HASH
      BillingMode: PAY_PER_REQUEST  # Critical: enables on-demand capacity to pass the control
```

### Terraform

```hcl
# DynamoDB table with on-demand capacity
resource "aws_dynamodb_table" "<example_resource_name>" {
  name     = "<example_resource_name>"
  hash_key = "id"

  attribute {
    name = "id"
    type = "S"
  }

  billing_mode = "PAY_PER_REQUEST" # Critical: enables on-demand capacity to pass the control
}
```

### Other

1. Open the AWS console and go to DynamoDB
2. Click Tables and select your table
3. Open the Additional settings tab and click Edit in Read/write capacity
4. Set Capacity mode to On-demand (PAY_PER_REQUEST)
5. Click Save

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/dynamodb-controls.html#dynamodb-1](https://docs.aws.amazon.com/securityhub/latest/userguide/dynamodb-controls.html#dynamodb-1)
- [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.Console.html#AutoScaling.Console.ExistingTable](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.Console.html#AutoScaling.Console.ExistingTable)

## 技术信息

- Source Metadata：[sources/aws/dynamodb_table_autoscaling_enabled/metadata.json](../../sources/aws/dynamodb_table_autoscaling_enabled/metadata.json)
- Source Code：[sources/aws/dynamodb_table_autoscaling_enabled/check.py](../../sources/aws/dynamodb_table_autoscaling_enabled/check.py)
- Source Metadata Path：`sources/aws/dynamodb_table_autoscaling_enabled/metadata.json`
- Source Code Path：`sources/aws/dynamodb_table_autoscaling_enabled/check.py`
