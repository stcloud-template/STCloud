# API Gateway REST API with a public endpoint has an authorizer configured

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `apigateway_restapi_public_with_authorizer` |
| 云平台 | AWS |
| 服务 | apigateway |
| 严重等级 | medium |
| 类别 | internet-exposed, identity-access |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, TTPs/Initial Access/Unauthorized Access, Effects/Data Exposure |
| 资源类型 | AwsApiGatewayRestApi |
| 资源组 | api_gateway |

## 描述

**API Gateway REST APIs** exposed to the Internet are evaluated for an attached **authorizer** that enforces caller identity (Lambda authorizer or Cognito user pool) on method invocations. Focus is on whether public endpoints require authenticated requests rather than accepting anonymous calls.

## 风险

Without an **authorizer** on a public API, anonymous callers can: - Read or alter data (confidentiality/integrity) - Trigger backend actions, impacting systems - Abuse traffic, degrading availability and inflating costs Endpoint enumeration also enables broader discovery and lateral movement.

## 推荐措施

Enforce **authentication** on all Internet-facing APIs by attaching an **authorizer** (Cognito user pool or Lambda) that validates tokens and scopes. Apply defense in depth: - Restrictive resource policies and IP controls - WAF, throttling, quotas, rate limits - Least-privilege backend access and comprehensive logging

## 修复步骤


### CLI

```text
aws apigateway create-authorizer --rest-api-id <rest_api_id> --name <example_resource_name> --type TOKEN --authorizer-uri arn:aws:apigateway:<region>:lambda:path/2015-03-31/functions/arn:aws:lambda:<region>:<account-id>:function:<example_resource_name>/invocations --identity-source 'method.request.header.Authorization'
```

### Native IaC

```yaml
# CloudFormation: Create a minimal Lambda TOKEN authorizer for a public REST API
Resources:
  <example_resource_name>:
    Type: AWS::ApiGateway::Authorizer
    Properties:
      Name: <example_resource_name>
      RestApiId: <example_resource_id>
      Type: TOKEN  # Critical: adds an authorizer to the REST API
      IdentitySource: method.request.header.Authorization  # Critical: header to read token from
      AuthorizerUri: arn:aws:apigateway:<region>:lambda:path/2015-03-31/functions/arn:aws:lambda:<region>:<account-id>:function/<example_resource_name>/invocations  # Critical: Lambda authorizer function URI
```

### Terraform

```hcl
# Terraform: Minimal Lambda TOKEN authorizer for API Gateway REST API
resource "aws_api_gateway_authorizer" "<example_resource_name>" {
  name            = "<example_resource_name>"
  rest_api_id     = "<example_resource_id>"
  type            = "TOKEN"  # Critical: enables a Lambda authorizer on the REST API
  identity_source = "method.request.header.Authorization"  # Critical: header to read token
  authorizer_uri  = "arn:aws:apigateway:<region>:lambda:path/2015-03-31/functions/arn:aws:lambda:<region>:<account-id>:function/<example_resource_name>/invocations"  # Critical: Lambda authorizer function URI
}
```

### Other

1. In the AWS Console, open API Gateway and select your REST API
2. In the left pane, click Authorizers > Create authorizer
3. Choose Lambda (TOKEN) or Cognito User Pool
4. For Lambda: select the function and set Identity source to method.request.header.Authorization; for Cognito: select the user pool
5. Click Create authorizer to add it to the API

## 参考资料

- [https://support.icompaas.com/support/solutions/articles/62000233640-check-if-api-gateway-public-endpoint-has-an-authorizer-configured](https://support.icompaas.com/support/solutions/articles/62000233640-check-if-api-gateway-public-endpoint-has-an-authorizer-configured)
- [https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-endpoint-types.html](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-endpoint-types.html)
- [https://api7.ai/blog/secure-rest-api-in-aws-api-gateway](https://api7.ai/blog/secure-rest-api-in-aws-api-gateway)
- [https://supertokens.com/blog/lambda-authorizers](https://supertokens.com/blog/lambda-authorizers)
- [https://clerk.com/blog/how-to-secure-api-gateway-using-jwt-and-lambda-authorizers-with-clerk](https://clerk.com/blog/how-to-secure-api-gateway-using-jwt-and-lambda-authorizers-with-clerk)
- [https://aws.plainenglish.io/6-rest-api-security-best-practices-you-can-achieve-with-amazon-api-gateway-2-authentication-62b5171989bd](https://aws.plainenglish.io/6-rest-api-security-best-practices-you-can-achieve-with-amazon-api-gateway-2-authentication-62b5171989bd)
- [https://stackoverflow.com/questions/68512642/how-to-configure-aws-api-gateway-without-authorizer](https://stackoverflow.com/questions/68512642/how-to-configure-aws-api-gateway-without-authorizer)
- [https://auth0.com/docs/customize/integrations/aws/aws-api-gateway-custom-authorizers](https://auth0.com/docs/customize/integrations/aws/aws-api-gateway-custom-authorizers)

## 技术信息

- Source Metadata：[sources/aws/apigateway_restapi_public_with_authorizer/metadata.json](../../sources/aws/apigateway_restapi_public_with_authorizer/metadata.json)
- Source Code：[sources/aws/apigateway_restapi_public_with_authorizer/check.py](../../sources/aws/apigateway_restapi_public_with_authorizer/check.py)
- Source Metadata Path：`sources/aws/apigateway_restapi_public_with_authorizer/metadata.json`
- Source Code Path：`sources/aws/apigateway_restapi_public_with_authorizer/check.py`
