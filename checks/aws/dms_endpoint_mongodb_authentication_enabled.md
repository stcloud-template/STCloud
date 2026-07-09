# DMS MongoDB endpoint has an authentication mechanism enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `dms_endpoint_mongodb_authentication_enabled` |
| 云平台 | AWS |
| 服务 | dms |
| 严重等级 | medium |
| 类别 | identity-access |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Effects/Data Exposure |
| 资源类型 | AwsDmsEndpoint |
| 资源组 | database |

## 描述

**AWS DMS MongoDB endpoints** use an authentication mechanism. Configuration expects `AuthType` not `no` (e.g., `password`) with an `authMechanism` such as `scram_sha_1` or `mongodb_cr`.

## 风险

Without authentication, unauthenticated connections can access the source, degrading **confidentiality** and **integrity**. Adversaries could read or modify migrated documents, hijack CDC, inject data, or exfiltrate records during replication.

## 推荐措施

Enforce **strong authentication** on MongoDB endpoints: set `AuthType` to `password` and use `authMechanism` like `scram_sha_1`. Apply **least privilege** database accounts, store secrets in **Secrets Manager**, and pair with **TLS** for defense in depth.

## 修复步骤


### CLI

```text
aws dms modify-endpoint --endpoint-arn <endpoint-arn> --mongodb-settings '{"AuthType":"password"}' --username <username> --password <password>
```

### Native IaC

```yaml
# CloudFormation: enable authentication on a MongoDB DMS endpoint
Resources:
  <example_resource_name>:
    Type: AWS::DMS::Endpoint
    Properties:
      EndpointIdentifier: <example_resource_name>
      EndpointType: source
      EngineName: mongodb
      MongoDbSettings:
        AuthType: password  # CRITICAL: sets authentication mode to 'password' so auth is enabled
```

### Terraform

```hcl
# Terraform: enable authentication on a MongoDB DMS endpoint
resource "aws_dms_endpoint" "<example_resource_name>" {
  endpoint_id   = "<example_resource_name>"
  endpoint_type = "source"
  engine_name   = "mongodb"

  mongodb_settings {
    auth_type = "password"  # CRITICAL: enables authentication for the MongoDB endpoint
  }
}
```

### Other

1. In the AWS Console, go to Database Migration Service > Endpoints
2. Select the MongoDB endpoint and click Modify
3. Under MongoDB settings, set Authentication mode to Password
4. Enter Username and Password
5. Click Save changes

## 参考资料

- [https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/dms-controls.html#dms-11](https://docs.aws.amazon.com/securityhub/latest/userguide/dms-controls.html#dms-11)

## 技术信息

- Source Metadata：[sources/aws/dms_endpoint_mongodb_authentication_enabled/metadata.json](../../sources/aws/dms_endpoint_mongodb_authentication_enabled/metadata.json)
- Source Code：[sources/aws/dms_endpoint_mongodb_authentication_enabled/check.py](../../sources/aws/dms_endpoint_mongodb_authentication_enabled/check.py)
- Source Metadata Path：`sources/aws/dms_endpoint_mongodb_authentication_enabled/metadata.json`
- Source Code Path：`sources/aws/dms_endpoint_mongodb_authentication_enabled/check.py`
