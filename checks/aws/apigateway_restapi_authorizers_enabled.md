# API Gateway REST API has an authorizer at API level or all methods are authorized

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `apigateway_restapi_authorizers_enabled` |
| 云平台 | AWS |
| 服务 | apigateway |
| 严重等级 | medium |
| 类别 | identity-access |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Initial Access |
| 资源类型 | AwsApiGatewayRestApi |
| 资源组 | api_gateway |

## 描述

**API Gateway REST APIs** are evaluated for **access control**: an **API-level authorizer** is present, or all resource methods use an authorization mechanism. Methods marked `NONE` indicate unauthenticated access.

## 风险

**Unauthenticated API methods** enable: - Arbitrary reads exposing data (**confidentiality**) - Unauthorized actions against backends (**integrity**) - Abuse and high traffic causing cost spikes or outages (**availability**) Attackers can enumerate endpoints and invoke integrations without tokens.

## 推荐措施

Require **authentication** on every method: use **Cognito user pools**, **Lambda authorizers**, or **IAM**; avoid `NONE`. - Enforce **least privilege** with scoped policies - Use **private endpoints** or resource policies for internal APIs - Add **rate limiting** and **WAF** for defense in depth

## 修复步骤


### Native IaC

```yaml
# CloudFormation: set method authorization so it's not public
Resources:
  <example_resource_name>:
    Type: AWS::ApiGateway::Method
    Properties:
      RestApiId: <example_resource_id>
      ResourceId: <example_resource_id>
      HttpMethod: GET
      AuthorizationType: AWS_IAM  # Critical: authorizes the method (not NONE)
```

### Terraform

```hcl
# Terraform: set method authorization so it's not public
resource "aws_api_gateway_method" "<example_resource_name>" {
  rest_api_id  = "<example_resource_id>"
  resource_id  = "<example_resource_id>"
  http_method  = "GET"
  authorization = "AWS_IAM" # Critical: authorizes the method (not NONE)
}
```

### Other

1. In the AWS Console, go to API Gateway > APIs (REST) and select your API
2. Open Resources, select a resource, then select a method (e.g., GET)
3. Click Method Request
4. Set Authorization to AWS_IAM (or an existing Cognito/Lambda authorizer)
5. Repeat for every method so none show Authorization = NONE
6. Deploy the API to apply changes

## 参考资料

- [https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html)

## 技术信息

- Source Metadata：[sources/aws/apigateway_restapi_authorizers_enabled/metadata.json](../../sources/aws/apigateway_restapi_authorizers_enabled/metadata.json)
- Source Code：[sources/aws/apigateway_restapi_authorizers_enabled/check.py](../../sources/aws/apigateway_restapi_authorizers_enabled/check.py)
- Source Metadata Path：`sources/aws/apigateway_restapi_authorizers_enabled/metadata.json`
- Source Code Path：`sources/aws/apigateway_restapi_authorizers_enabled/check.py`
