# API Gateway REST API stage has X-Ray tracing enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `apigateway_restapi_tracing_enabled` |
| 云平台 | AWS |
| 服务 | apigateway |
| 严重等级 | low |
| 类别 | logging |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsApiGatewayStage |
| 资源组 | api_gateway |

## 描述

**API Gateway REST API stages** have **AWS X-Ray active tracing** enabled to sample incoming requests and produce distributed traces across connected services.

## 风险

Without X-Ray tracing, you lose end-to-end visibility, hindering detection of timeouts, errors, and anomalous latency. This delays incident response and root-cause analysis, increasing MTTR and risking partial outages (availability) and undetected integration failures (integrity).

## 推荐措施

Enable **X-Ray active tracing** on all API Gateway stages and propagate trace context through downstream services. Use prudent sampling, correlate traces with logs/metrics, and alert on errors/latency. Apply **least privilege** to X-Ray access and use **defense in depth** for observability.

## 修复步骤


### CLI

```text
aws apigateway update-stage --rest-api-id <restapi-id> --stage-name <stage-name> --patch-operations op=replace,path=/tracingEnabled,value=true
```

### Native IaC

```yaml
# CloudFormation: Enable X-Ray tracing on an API Gateway REST API stage
Resources:
  <example_resource_name>:
    Type: AWS::ApiGateway::Stage
    Properties:
      RestApiId: <example_resource_id>
      DeploymentId: <example_resource_id>
      StageName: <example_resource_name>
      TracingEnabled: true  # Critical: enables AWS X-Ray tracing for this stage
```

### Terraform

```hcl
# Enable X-Ray tracing on an API Gateway REST API stage
resource "aws_api_gateway_stage" "example" {
  rest_api_id = "<example_resource_id>"
  deployment_id = "<example_resource_id>"
  stage_name  = "<example_resource_name>"
  xray_tracing_enabled = true  # Critical: enables AWS X-Ray tracing for this stage
}
```

### Other

1. Open the AWS Console and go to API Gateway
2. Select your REST API and choose Stages
3. Select the target stage
4. Open the Logs/Tracing tab, check Enable X-Ray Tracing
5. Click Save

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/apigateway-controls.html#apigateway-3](https://docs.aws.amazon.com/securityhub/latest/userguide/apigateway-controls.html#apigateway-3)
- [https://docs.aws.amazon.com/xray/latest/devguide/xray-services-apigateway.html](https://docs.aws.amazon.com/xray/latest/devguide/xray-services-apigateway.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/APIGateway/tracing.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/APIGateway/tracing.html)

## 技术信息

- Source Metadata：[sources/aws/apigateway_restapi_tracing_enabled/metadata.json](../../sources/aws/apigateway_restapi_tracing_enabled/metadata.json)
- Source Code：[sources/aws/apigateway_restapi_tracing_enabled/check.py](../../sources/aws/apigateway_restapi_tracing_enabled/check.py)
- Source Metadata Path：`sources/aws/apigateway_restapi_tracing_enabled/metadata.json`
- Source Code Path：`sources/aws/apigateway_restapi_tracing_enabled/check.py`
