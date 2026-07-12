# Step Functions state machine has logging enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `stepfunctions_statemachine_logging_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | stepfunctions |
| 重大度 | medium |
| カテゴリ | logging |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis |
| リソースタイプ | AwsStepFunctionStateMachine |
| リソースグループ | serverless |

## 説明

**AWS Step Functions state machines** are configured to emit **execution logs** to CloudWatch Logs via a defined `loggingConfiguration` with a `level` set above `OFF`.

## リスク

Without **execution logs**, workflow failures and anomalies are **undetectable**, increasing MTTR and risking silent data loss. Missing audit trails weaken **integrity** oversight and complicate **forensics**, enabling misuse of invoked services to go unnoticed and creating **compliance** gaps.

## 推奨事項

Enable CloudWatch logging on all state machines at an appropriate `level` (e.g., `ERROR` or `ALL`) and send logs to a protected log group. Apply **least privilege** to log write/read, set **retention**, and avoid sensitive data unless required using `includeExecutionData`. Use X-Ray tracing for **defense in depth**.

## 修正手順


### CLI

```text
aws stepfunctions update-state-machine --state-machine-arn <state-machine-arn> --logging-configuration file://logging-config.json
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::StepFunctions::StateMachine
    Properties:
      RoleArn: arn:aws:iam::<account-id>:role/<example_role_name>
      DefinitionString: |
        {"StartAt":"Pass","States":{"Pass":{"Type":"Pass","End":true}}}
      LoggingConfiguration:
        Destinations:
          - CloudWatchLogsLogGroup:
              LogGroupArn: arn:aws:logs:<region>:<account-id>:log-group:<log-group-name>:*  # Critical: target CloudWatch Logs group
        Level: ERROR  # Critical: enables logging (not OFF)
```

### Terraform

```hcl
resource "aws_sfn_state_machine" "<example_resource_name>" {
  name       = "<example_resource_name>"
  role_arn   = "arn:aws:iam::<account-id>:role/<example_role_name>"
  definition = jsonencode({ StartAt = "Pass", States = { Pass = { Type = "Pass", End = true } } })

  logging_configuration {
    log_destination = "arn:aws:logs:<region>:<account-id>:log-group:<log-group-name>:*"  # Critical: CloudWatch Logs destination
    level           = "ERROR"                                                              # Critical: enables logging
  }
}
```

### Other

1. Open AWS Console > Step Functions > State machines
2. Select the state machine and click Edit
3. In Logging, enable logging
4. Choose an existing CloudWatch Logs log group
5. Set Level to Error (or All)
6. Save changes

## 参考資料

- [https://docs.aws.amazon.com/step-functions/latest/dg/logging.html](https://docs.aws.amazon.com/step-functions/latest/dg/logging.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/stepfunctions-controls.html#stepfunctions-1](https://docs.aws.amazon.com/securityhub/latest/userguide/stepfunctions-controls.html#stepfunctions-1)
- [https://support.icompaas.com/support/solutions/articles/62000233757-ensure-step-functions-state-machines-should-have-logging-enabled](https://support.icompaas.com/support/solutions/articles/62000233757-ensure-step-functions-state-machines-should-have-logging-enabled)

## 技術情報

- Source Metadata：[sources/aws/stepfunctions_statemachine_logging_enabled/metadata.json](../../sources/aws/stepfunctions_statemachine_logging_enabled/metadata.json)
- Source Code：[sources/aws/stepfunctions_statemachine_logging_enabled/check.py](../../sources/aws/stepfunctions_statemachine_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/stepfunctions_statemachine_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/stepfunctions_statemachine_logging_enabled/check.py`
