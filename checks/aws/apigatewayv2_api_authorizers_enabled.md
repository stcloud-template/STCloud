# API Gateway V2 API has an authorizer configured

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `apigatewayv2_api_authorizers_enabled` |
| 云平台 | AWS |
| 服务 | apigatewayv2 |
| 严重等级 | medium |
| 类别 | identity-access |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, TTPs/Initial Access, Effects/Data Exposure |
| 资源类型 | AwsApiGatewayV2Api |
| 资源组 | api_gateway |

## 描述

**API Gateway v2 APIs** use **authorizers** (JWT/Cognito or Lambda) to authenticate requests. This evaluates whether an API has an authorizer configured to control access to its routes.

## 风险

Without an authorizer, anyone can invoke routes. - Confidentiality: exposure of data and metadata - Integrity: unauthorized state changes or actions - Availability/Cost: automated abuse of backends, traffic spikes, and unexpected spend

## 推荐措施

Enable an **authorizer** (JWT/Cognito or Lambda) so only authenticated principals can invoke routes. - Enforce **least privilege** with scopes/claims or policy decisions - Apply **defense in depth** with resource policies, throttling, and WAF - Avoid public routes unless explicitly required

## 修复步骤


### CLI

```text
aws apigatewayv2 create-authorizer --api-id <API_ID> --authorizer-type REQUEST --name <example_resource_name> --authorizer-uri arn:aws:apigateway:<REGION>:lambda:path/2015-03-31/functions/<LAMBDA_FUNCTION_ARN>/invocations --identity-source '$request.header.Authorization'
```

### Native IaC

```yaml
# CloudFormation: create a minimal Lambda authorizer for API Gateway v2
Resources:
  <example_resource_name>:
    Type: AWS::ApiGatewayV2::Authorizer
    Properties:
      ApiId: <example_resource_id>
      AuthorizerType: REQUEST  # Critical: enables a Lambda REQUEST authorizer on the API
      AuthorizerUri: arn:aws:apigateway:<REGION>:lambda:path/2015-03-31/functions/<LAMBDA_FUNCTION_ARN>/invocations  # Critical: Lambda authorizer function to invoke
      IdentitySource:  # Critical: where to read the auth token from
        - "$request.header.Authorization"
      Name: <example_resource_name>
```

### Terraform

```hcl
# Minimal AWS API Gateway v2 Lambda authorizer
resource "aws_apigatewayv2_authorizer" "<example_resource_name>" {
  api_id           = "<example_resource_id>"
  name             = "<example_resource_name>"
  authorizer_type  = "REQUEST"  # Critical: creates a Lambda REQUEST authorizer
  authorizer_uri   = "arn:aws:apigateway:<REGION>:lambda:path/2015-03-31/functions/<LAMBDA_FUNCTION_ARN>/invocations"  # Critical: Lambda to invoke
  identity_sources = ["$request.header.Authorization"]  # Critical: identity source for authorization
}
```

### Other

1. In the AWS Console, go to API Gateway > APIs and select your HTTP/WebSocket API
2. In the left nav, click Authorizers > Create authorizer
3. Choose Lambda as the authorizer type and select your Lambda function
4. Set Identity source to: $request.header.Authorization
5. Click Create to add the authorizer

## 参考资料

- [https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html)
- [https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html)
- [https://support.icompaas.com/support/solutions/articles/62000127114-ensure-api-gateway-has-configured-authorizers](https://support.icompaas.com/support/solutions/articles/62000127114-ensure-api-gateway-has-configured-authorizers)

## 技术信息

- Source Metadata：[sources/aws/apigatewayv2_api_authorizers_enabled/metadata.json](../../sources/aws/apigatewayv2_api_authorizers_enabled/metadata.json)
- Source Code：[sources/aws/apigatewayv2_api_authorizers_enabled/check.py](../../sources/aws/apigatewayv2_api_authorizers_enabled/check.py)
- Source Metadata Path：`sources/aws/apigatewayv2_api_authorizers_enabled/metadata.json`
- Source Code Path：`sources/aws/apigatewayv2_api_authorizers_enabled/check.py`
