# API Gateway REST API stage has client certificate enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `apigateway_restapi_client_certificate_enabled` |
| 云平台 | AWS |
| 服务 | apigateway |
| 严重等级 | medium |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Encryption in Transit, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/PCI-DSS, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls (USA) |
| 资源类型 | AwsApiGatewayStage |
| 资源组 | api_gateway |

## 描述

**API Gateway stage** has a **client certificate** configured so HTTP/S integrations can perform **mutual TLS** and authenticate API Gateway to the backend

## 风险

Without client authentication to the backend, requests cannot be proven to originate from API Gateway. Direct calls to the backend may bypass gateway policies, enabling unauthorized access and data tampering. This degrades **integrity** and **confidentiality** and reduces auditability.

## 推荐措施

Enable **mutual TLS** from API Gateway to the backend with a **client certificate**, and configure the backend to trust only that identity. Apply **zero trust** and **least privilege**: block public access to the backend, restrict networks, rotate certificates, and monitor authentication failures.

## 修复步骤


### CLI

```text
aws apigateway update-stage --rest-api-id <REST_API_ID> --stage-name <STAGE_NAME> --patch-operations op=replace,path=/clientCertificateId,value=<CLIENT_CERT_ID>
```

### Native IaC

```yaml
# CloudFormation: attach a client certificate to a REST API stage
Resources:
  ClientCert:
    Type: AWS::ApiGateway::ClientCertificate

  ApiStage:
    Type: AWS::ApiGateway::Stage
    Properties:
      StageName: <example_resource_name>
      RestApiId: <example_resource_id>
      DeploymentId: <example_resource_id>
      ClientCertificateId: !Ref ClientCert  # Critical: enables client certificate on the stage
```

### Terraform

```hcl
# Terraform: attach a client certificate to a REST API stage
resource "aws_api_gateway_client_certificate" "example" {}

resource "aws_api_gateway_stage" "<example_resource_name>" {
  stage_name          = "<example_resource_name>"
  rest_api_id         = "<example_resource_id>"
  deployment_id       = "<example_resource_id>"
  client_certificate_id = aws_api_gateway_client_certificate.example.id  # Critical: enables client certificate on the stage
}
```

### Other

1. In the AWS Console, go to API Gateway > REST APIs and select your API
2. In the left menu, click Client Certificates and create one (Generate)
3. In the left menu, click Stages and select the target stage
4. In Settings, find Client certificate and select the created certificate
5. Click Save Changes

## 参考资料

- [https://aws.amazon.com/blogs/compute/introducing-mutual-tls-authentication-for-amazon-api-gateway/](https://aws.amazon.com/blogs/compute/introducing-mutual-tls-authentication-for-amazon-api-gateway/)

## 技术信息

- Source Metadata：[sources/aws/apigateway_restapi_client_certificate_enabled/metadata.json](../../sources/aws/apigateway_restapi_client_certificate_enabled/metadata.json)
- Source Code：[sources/aws/apigateway_restapi_client_certificate_enabled/check.py](../../sources/aws/apigateway_restapi_client_certificate_enabled/check.py)
- Source Metadata Path：`sources/aws/apigateway_restapi_client_certificate_enabled/metadata.json`
- Source Code Path：`sources/aws/apigateway_restapi_client_certificate_enabled/check.py`
