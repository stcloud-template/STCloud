# API Gateway REST API endpoint is private

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `apigateway_restapi_public` |
| クラウドプラットフォーム | AWS |
| サービス | apigateway |
| 重大度 | medium |
| カテゴリ | internet-exposed |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Initial Access |
| リソースタイプ | AwsApiGatewayRestApi |
| リソースグループ | api_gateway |

## 説明

**Amazon API Gateway REST APIs** are evaluated for endpoint exposure: **internet-accessible** endpoints versus **private VPC-only** access via interface VPC endpoints (`AWS PrivateLink`).

## リスク

Internet exposure increases attack surface: - **Confidentiality**: misconfigured or anonymous methods can leak data - **Integrity**: unauthorized calls can change backend state - **Availability/cost**: bots or DDoS can exhaust capacity and spike spend

## 推奨事項

Prefer **private** REST APIs reachable via interface VPC endpoints (`PRIVATE`). *If public access is required*, apply **least privilege** and **defense in depth**: - Restrict with resource policies (`aws:SourceVpc`/`aws:SourceVpce`) - Enforce strong auth (IAM, Cognito, or authorizers) - Add AWS WAF, throttling, usage plans, and comprehensive logging

## 修正手順


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

## 参考資料

- [https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-apis.html](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-apis.html)
- [https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-resource-policies-examples.html#apigateway-resource-policies-source-vpc-example](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-resource-policies-examples.html#apigateway-resource-policies-source-vpc-example)
- [https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html)
- [https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-resource-policies.html](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-resource-policies.html)

## 技術情報

- Source Metadata：[sources/aws/apigateway_restapi_public/metadata.json](../../sources/aws/apigateway_restapi_public/metadata.json)
- Source Code：[sources/aws/apigateway_restapi_public/check.py](../../sources/aws/apigateway_restapi_public/check.py)
- Source Metadata Path：`sources/aws/apigateway_restapi_public/metadata.json`
- Source Code Path：`sources/aws/apigateway_restapi_public/check.py`
