# API Gateway V2 API stage has access logging enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `apigatewayv2_api_access_logging_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | apigatewayv2 |
| 重大度 | medium |
| カテゴリ | logging |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices |
| リソースタイプ | AwsApiGatewayV2Stage |
| リソースグループ | api_gateway |

## 説明

**API Gateway v2** stages have **access logging** configured to capture request details and deliver them to a logging destination (e.g., CloudWatch Logs or Firehose). The evaluation looks for logging being enabled at each API stage.

## リスク

Without access logs, API calls lack traceability, making it hard to spot credential misuse, route abuse, or anomalous traffic. This reduces confidentiality and integrity through undetected data access or manipulation, and impacts availability by slowing incident response.

## 推奨事項

Enable **stage-level access logging** to a centralized destination and use structured formats. Apply appropriate retention and restrict log access per **least privilege**. Integrate logs with monitoring and alerts to detect anomalies, and complement with **defense in depth** controls.

## 修正手順


### CLI

```text
aws apigatewayv2 update-stage --api-id <API_ID> --stage-name <STAGE_NAME> --access-log-settings DestinationArn=<LOG_GROUP_ARN>,Format='{"requestId":"$context.requestId"}'
```

### Native IaC

```yaml
# CloudFormation: Enable access logging on API Gateway V2 stage
Resources:
  <example_resource_name>:
    Type: AWS::ApiGatewayV2::Stage
    Properties:
      ApiId: <example_resource_id>
      StageName: <example_resource_name>
      AccessLogSettings: # Critical: enables access logging for the stage
        DestinationArn: <example_log_group_arn> # CloudWatch Logs log group ARN
        Format: '{"requestId":"$context.requestId"}' # Minimal required format
```

### Terraform

```hcl
# Terraform: Enable access logging on API Gateway V2 stage
resource "aws_apigatewayv2_stage" "<example_resource_name>" {
  api_id = "<example_resource_id>"
  name   = "<example_resource_name>"

  access_log_settings { # Critical: enables access logging for the stage
    destination_arn = "<example_log_group_arn>"
    format          = "{\"requestId\":\"$context.requestId\"}"
  }
}
```

### Other

1. In the AWS Console, go to API Gateway > your HTTP/WebSocket API
2. Open Stages and select the target stage
3. In Access logging, enable Access logging
4. Set Log destination ARN to your CloudWatch log group (or Firehose stream)
5. Set Log format to: {"requestId":"$context.requestId"}
6. Click Save

## 参考資料

- [https://docs.aws.amazon.com/apigateway/latest/developerguide/security-monitoring.html](https://docs.aws.amazon.com/apigateway/latest/developerguide/security-monitoring.html)
- [https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html)
- [https://support.icompaas.com/support/solutions/articles/62000229562-ensure-api-gateway-v2-has-access-logging-enabled](https://support.icompaas.com/support/solutions/articles/62000229562-ensure-api-gateway-v2-has-access-logging-enabled)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/APIGateway/api-gateway-stage-access-logging.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/APIGateway/api-gateway-stage-access-logging.html)

## 技術情報

- Source Metadata：[sources/aws/apigatewayv2_api_access_logging_enabled/metadata.json](../../sources/aws/apigatewayv2_api_access_logging_enabled/metadata.json)
- Source Code：[sources/aws/apigatewayv2_api_access_logging_enabled/check.py](../../sources/aws/apigatewayv2_api_access_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/apigatewayv2_api_access_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/apigatewayv2_api_access_logging_enabled/check.py`
