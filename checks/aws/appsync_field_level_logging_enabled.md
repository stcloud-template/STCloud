# AWS AppSync API has field-level logging set to ALL or ERROR

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `appsync_field_level_logging_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | appsync |
| 重大度 | medium |
| カテゴリ | logging |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | AwsAppSyncGraphQLApi |
| リソースグループ | api_gateway |

## 説明

**AWS AppSync GraphQL APIs** have **field-level logging** configured at the resolver level. The check looks for log levels of `ERROR` or `ALL` to confirm field resolution events are recorded.

## リスク

Without **field-level logs**, resolver access and mutations lack **auditability**, reducing detection of data exfiltration and tampering (**confidentiality and integrity**). Limited traces hinder incident response and root-cause analysis, increasing recovery time.

## 推奨事項

- Enable field-level logging at least `ERROR`; raise to `INFO`/`DEBUG`/`ALL` only for troubleshooting. - Enforce **least privilege** on the logging role. - Avoid sensitive data in logs; limit verbose content. - Set retention and consider log **sampling** to balance visibility and cost.

## 修正手順


### CLI

```text
aws appsync update-graphql-api --api-id <example_resource_id> --name <api-name> --authentication-type AWS_IAM --log-config fieldLogLevel=ERROR,cloudWatchLogsRoleArn=<cloudwatch_logs_role_arn>
```

### Native IaC

```yaml
# CloudFormation - Enable field-level logging for AppSync API
Resources:
  <example_resource_name>:
    Type: AWS::AppSync::GraphQLApi
    Properties:
      Name: <example_resource_name>
      AuthenticationType: AWS_IAM
      LogConfig:
        CloudWatchLogsRoleArn: arn:aws:iam::<account-id>:role/<example_resource_name>  # CRITICAL: allows AppSync to write logs
        FieldLogLevel: ERROR  # CRITICAL: sets field-level logging to a compliant level
```

### Terraform

```hcl
# Terraform - Enable field-level logging for AppSync API
resource "aws_appsync_graphql_api" "<example_resource_name>" {
  name                = "<example_resource_name>"
  authentication_type = "AWS_IAM"

  log_config {
    cloudwatch_logs_role_arn = "<cloudwatch_logs_role_arn>" # CRITICAL: permits logging to CloudWatch
    field_log_level          = "ERROR"                        # CRITICAL: compliant field-level logging
  }
}
```

### Other

1. In the AWS Console, go to AppSync and open your GraphQL API
2. Go to Settings > Logging
3. Turn on Enable logs
4. Set Field resolver log level to ERROR (or ALL)
5. Select an IAM role that allows AppSync to write to CloudWatch Logs
6. Click Save

## 参考資料

- [https://theburningmonk.com/2020/09/how-to-sample-appsync-resolver-logs/](https://theburningmonk.com/2020/09/how-to-sample-appsync-resolver-logs/)
- [https://lumigo.io/blog/how-to-monitor-and-debug-appsync-apis/](https://lumigo.io/blog/how-to-monitor-and-debug-appsync-apis/)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/appsync-controls.html#appsync-2](https://docs.aws.amazon.com/securityhub/latest/userguide/appsync-controls.html#appsync-2)
- [https://docs.aws.amazon.com/appsync/latest/APIReference/API_LogConfig.html](https://docs.aws.amazon.com/appsync/latest/APIReference/API_LogConfig.html)
- [https://blog.graphbolt.dev/debugging-aws-appsync-apis-with-cloudwatch](https://blog.graphbolt.dev/debugging-aws-appsync-apis-with-cloudwatch)
- [https://support.icompaas.com/support/solutions/articles/62000233678-ensure-aws-appsync-should-have-field-level-logging-enabled](https://support.icompaas.com/support/solutions/articles/62000233678-ensure-aws-appsync-should-have-field-level-logging-enabled)

## 技術情報

- Source Metadata：[sources/aws/appsync_field_level_logging_enabled/metadata.json](../../sources/aws/appsync_field_level_logging_enabled/metadata.json)
- Source Code：[sources/aws/appsync_field_level_logging_enabled/check.py](../../sources/aws/appsync_field_level_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/appsync_field_level_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/appsync_field_level_logging_enabled/check.py`
