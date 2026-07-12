# API Gateway REST API stage has logging enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `apigateway_restapi_logging_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | apigateway |
| 重大度 | medium |
| カテゴリ | logging, forensics-ready |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Defense Evasion |
| リソースタイプ | AwsApiGatewayStage |
| リソースグループ | api_gateway |

## 説明

**API Gateway REST API stages** with **stage logging** enabled to emit execution or access logs to CloudWatch

## リスク

Without stage logging, API activity lacks visibility, hindering detection of abuse and incident response. Attackers can probe endpoints, exfiltrate data, or tamper integrations without traces, impacting confidentiality, integrity, and availability and blocking forensic investigation.

## 推奨事項

Enable **CloudWatch Logs** for all API Gateway stages, using `ERROR` or `INFO` as appropriate. Include request IDs (e.g., `$context.requestId`). Enforce **least privilege** on logs, set **retention** and **alerts** for anomalies. Avoid sensitive data in logs and use **defense in depth** with tracing.

## 修正手順


### CLI

```text
aws apigateway update-stage --rest-api-id <REST_API_ID> --stage-name <STAGE_NAME> --patch-operations op=replace,path='/*/*/logging/loglevel',value=ERROR
```

### Native IaC

```yaml
# CloudFormation: enable execution logging on a REST API stage
Resources:
  <example_resource_name>:
    Type: AWS::ApiGateway::Stage
    Properties:
      StageName: <example_resource_name>
      RestApiId: <example_resource_id>
      DeploymentId: <example_resource_id>
      MethodSettings:
        - ResourcePath: "/*"
          HttpMethod: "*"
          LoggingLevel: ERROR  # CRITICAL: turns on execution logging for all methods
```

### Terraform

```hcl
# Enable execution logging for all methods in a REST API stage
resource "aws_api_gateway_method_settings" "<example_resource_name>" {
  rest_api_id = "<example_resource_id>"
  stage_name  = "<example_resource_name>"
  method_path = "*/*"
  settings {
    logging_level = "ERROR"  # CRITICAL: enables stage execution logging
  }
}
```

### Other

1. In the API Gateway console, open Settings and set CloudWatch log role ARN if prompted
2. Go to APIs > select your REST API > Stages > select the stage
3. Click Logs and tracing > CloudWatch Logs > choose Errors only (or Errors and info)
4. Save changes

## 参考資料

- [https://docs.aws.amazon.com/apigateway/latest/developerguide/security-monitoring.html](https://docs.aws.amazon.com/apigateway/latest/developerguide/security-monitoring.html)
- [https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-logging.html](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-logging.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/APIGateway/cloudwatch-logs.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/APIGateway/cloudwatch-logs.html)
- [https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html)
- [https://repost.aws/knowledge-center/api-gateway-cloudwatch-logs](https://repost.aws/knowledge-center/api-gateway-cloudwatch-logs)
- [https://repost.aws/knowledge-center/api-gateway-missing-cloudwatch-logs](https://repost.aws/knowledge-center/api-gateway-missing-cloudwatch-logs)
- [https://docs.aws.amazon.com/apigateway/latest/developerguide/view-cloudwatch-log-events-in-cloudwatch-console.html](https://docs.aws.amazon.com/apigateway/latest/developerguide/view-cloudwatch-log-events-in-cloudwatch-console.html)

## 技術情報

- Source Metadata：[sources/aws/apigateway_restapi_logging_enabled/metadata.json](../../sources/aws/apigateway_restapi_logging_enabled/metadata.json)
- Source Code：[sources/aws/apigateway_restapi_logging_enabled/check.py](../../sources/aws/apigateway_restapi_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/apigateway_restapi_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/apigateway_restapi_logging_enabled/check.py`
