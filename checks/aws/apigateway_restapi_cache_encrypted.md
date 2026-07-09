# API Gateway REST API stage cache data is encrypted at rest

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `apigateway_restapi_cache_encrypted` |
| 云平台 | AWS |
| 服务 | apigateway |
| 严重等级 | medium |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsApiGatewayStage |
| 资源组 | api_gateway |

## 描述

API Gateway REST API stages with caching have **cache data encrypted at rest**. The evaluation targets stages where caching is enabled and verifies that stored responses are protected via the `Encrypt cache data` setting.

## 风险

Unencrypted cache contents can expose response payloads, tokens, or PII if cache storage, backups, or admin tooling are accessed outside normal controls, harming **confidentiality** and enabling replay or session hijacking. Disclosure also reveals API patterns, aiding **lateral movement** and targeted abuse.

## 推荐措施

- Enable **encryption at rest** for any cached stage (`Encrypt cache data`). - Apply **least privilege** to stage administration and cache invalidation. - Avoid caching sensitive endpoints; use short TTLs and scheduled cache flushes for **defense in depth**.

## 修复步骤


### CLI

```text
aws apigateway update-stage --rest-api-id <restapi-id> --stage-name <stage-name> --patch-operations op=replace,path=/*/*/caching/dataEncrypted,value=true
```

### Native IaC

```yaml
# CloudFormation: enable encryption for all cached methods in a stage
Resources:
  <example_resource_name>:
    Type: AWS::ApiGateway::Stage
    Properties:
      StageName: <example_resource_name>
      RestApiId: <example_resource_id>
      DeploymentId: <example_resource_id>
      MethodSettings:
        - ResourcePath: /*
          HttpMethod: "*"
          CacheDataEncrypted: true  # Critical: encrypt cached responses at rest for all methods
```

### Terraform

```hcl
# Enable encryption for all cached methods in the stage
resource "aws_api_gateway_stage" "<example_resource_name>" {
  rest_api_id   = "<example_resource_id>"
  stage_name    = "<example_resource_name>"
  deployment_id = "<example_resource_id>"

  method_settings {
    resource_path        = "/*"
    http_method          = "*"
    cache_data_encrypted = true  # Critical: encrypt cached responses at rest
  }
}
```

### Other

1. Open the AWS Console and go to API Gateway
2. Select your REST API, then click Stages and choose the affected stage
3. In Method overrides (or Cache settings), enable Encrypt cache data
4. Save changes

## 参考资料

- [https://www.clouddefense.ai/compliance-rules/nist-800-53-5/au/apigateway-stage-cache-encryption-at-rest-enabled](https://www.clouddefense.ai/compliance-rules/nist-800-53-5/au/apigateway-stage-cache-encryption-at-rest-enabled)
- [https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html#enable-api-gateway-caching](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html#enable-api-gateway-caching)
- [https://support.icompaas.com/support/solutions/articles/62000233641-ensure-api-gateway-rest-api-cache-data-is-encrypted-at-rest](https://support.icompaas.com/support/solutions/articles/62000233641-ensure-api-gateway-rest-api-cache-data-is-encrypted-at-rest)
- [https://docs.fortifyfox.com/docs/aws-foundational-security-best-practices/apigateway/api-gw-cache-encrypted/index.html](https://docs.fortifyfox.com/docs/aws-foundational-security-best-practices/apigateway/api-gw-cache-encrypted/index.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/apigateway-controls.html#apigateway-5](https://docs.aws.amazon.com/securityhub/latest/userguide/apigateway-controls.html#apigateway-5)
- [https://www.clouddefense.ai/compliance-rules/aws-fs-practices/apigateway/foundational-security-apigateway-5](https://www.clouddefense.ai/compliance-rules/aws-fs-practices/apigateway/foundational-security-apigateway-5)
- [https://www.cloudanix.com/docs/aws/audit/apigatewaymonitoring/rules/apigateway_enable_encryption_api_cache](https://www.cloudanix.com/docs/aws/audit/apigatewaymonitoring/rules/apigateway_enable_encryption_api_cache)

## 技术信息

- Source Metadata：[sources/aws/apigateway_restapi_cache_encrypted/metadata.json](../../sources/aws/apigateway_restapi_cache_encrypted/metadata.json)
- Source Code：[sources/aws/apigateway_restapi_cache_encrypted/check.py](../../sources/aws/apigateway_restapi_cache_encrypted/check.py)
- Source Metadata Path：`sources/aws/apigateway_restapi_cache_encrypted/metadata.json`
- Source Code Path：`sources/aws/apigateway_restapi_cache_encrypted/check.py`
