# API Gateway REST API endpoint is private

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `apigateway_restapi_public` |
| 云平台 | AWS |
| 服务 | apigateway |
| 严重等级 | medium |
| 类别 | internet-exposed |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Initial Access |
| 资源类型 | AwsApiGatewayRestApi |
| 资源组 | api_gateway |

## 描述

**Amazon API Gateway REST APIs** are evaluated for endpoint exposure: **internet-accessible** endpoints versus **private VPC-only** access via interface VPC endpoints (`AWS PrivateLink`).

## 风险

Internet exposure increases attack surface: - **Confidentiality**: misconfigured or anonymous methods can leak data - **Integrity**: unauthorized calls can change backend state - **Availability/cost**: bots or DDoS can exhaust capacity and spike spend

## 推荐措施

Prefer **private** REST APIs reachable via interface VPC endpoints (`PRIVATE`). *If public access is required*, apply **least privilege** and **defense in depth**: - Restrict with resource policies (`aws:SourceVpc`/`aws:SourceVpce`) - Enforce strong auth (IAM, Cognito, or authorizers) - Add AWS WAF, throttling, usage plans, and comprehensive logging

## 修复步骤


### CLI

```text
aws apigateway update-rest-api --rest-api-id <REST_API_ID> --patch-operations op=replace,path=/endpointConfiguration/types/0,value=PRIVATE
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::ApiGateway::RestApi
    Properties:
      Name: <example_resource_name>
      EndpointConfiguration:
        Types:
          - PRIVATE  # Critical: sets the REST API endpoint to Private, removing public access
```

### Terraform

```hcl
resource "aws_api_gateway_rest_api" "<example_resource_name>" {
  name = "<example_resource_name>"

  endpoint_configuration {
    types = ["PRIVATE"]  # Critical: makes the REST API private
  }
}
```

### Other

1. Open the AWS console and go to API Gateway
2. Under REST APIs, select your API
3. In the left menu, click Settings
4. Set Endpoint Type to Private
5. Click Save changes

## 参考资料

- [https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-apis.html](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-apis.html)
- [https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-resource-policies-examples.html#apigateway-resource-policies-source-vpc-example](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-resource-policies-examples.html#apigateway-resource-policies-source-vpc-example)
- [https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html)
- [https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-resource-policies.html](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-resource-policies.html)

## 技术信息

- Source Metadata：[sources/aws/apigateway_restapi_public/metadata.json](../../sources/aws/apigateway_restapi_public/metadata.json)
- Source Code：[sources/aws/apigateway_restapi_public/check.py](../../sources/aws/apigateway_restapi_public/check.py)
- Source Metadata Path：`sources/aws/apigateway_restapi_public/metadata.json`
- Source Code Path：`sources/aws/apigateway_restapi_public/check.py`
