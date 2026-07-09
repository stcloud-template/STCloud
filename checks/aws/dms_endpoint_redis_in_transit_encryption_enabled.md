# DMS endpoint for Redis OSS is encrypted in transit

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `dms_endpoint_redis_in_transit_encryption_enabled` |
| 云平台 | AWS |
| 服务 | dms |
| 严重等级 | medium |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Encryption in Transit, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls (USA), Software and Configuration Checks/Industry and Regulatory Standards/PCI-DSS, Software and Configuration Checks/Industry and Regulatory Standards/ISO 27001 Controls |
| 资源类型 | AwsDmsEndpoint |
| 资源组 | database |

## 描述

**DMS Redis OSS endpoints** are assessed for the presence of **TLS** in their endpoint settings, such as `ssl-encryption`, indicating encrypted connections between the DMS replication instance and Redis.

## 风险

Without **TLS**, traffic between DMS and Redis can be intercepted or altered, compromising **confidentiality** and **integrity**. Attackers can perform **man-in-the-middle** interception, steal auth tokens, and inject or corrupt migrated data.

## 推荐措施

Enable **TLS** on Redis OSS endpoints (e.g., `ssl-encryption`) and require server certificate validation. Prohibit plaintext connections, prefer private networking, and enforce **least privilege** for DMS roles to strengthen **defense in depth**.

## 修复步骤


### Native IaC

```yaml
# CloudFormation: Enable TLS for Redis OSS DMS endpoint
Resources:
  <example_resource_name>:
    Type: AWS::DMS::Endpoint
    Properties:
      EndpointIdentifier: <example_resource_name>
      EndpointType: target
      EngineName: redis
      RedisSettings:
        ServerName: <example_resource_name>
        Port: 6379
        AuthType: none
        SslSecurityProtocol: ssl-encryption  # Critical: enables TLS for in-transit encryption
```

### Terraform

```hcl
# Enable TLS for Redis OSS DMS endpoint
resource "aws_dms_endpoint" "<example_resource_name>" {
  endpoint_id   = "<example_resource_id>"
  endpoint_type = "target"
  engine_name   = "redis"

  redis_settings {
    server_name           = "<example_resource_name>"
    port                  = 6379
    auth_type             = "none"
    ssl_security_protocol = "ssl-encryption" # Critical: enables TLS for in-transit encryption
  }
}
```

### Other

1. In the AWS Console, go to Database Migration Service > Endpoints
2. Select the Redis OSS endpoint and click Modify
3. Set SSL security protocol (Encryption in transit) to "SSL encryption"
4. Save changes

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/dms-controls.html#dms-12](https://docs.aws.amazon.com/securityhub/latest/userguide/dms-controls.html#dms-12)
- [https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redis.html#CHAP_Target.Redis.EndpointSettings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redis.html#CHAP_Target.Redis.EndpointSettings)
- [https://support.icompaas.com/support/solutions/articles/62000233450-ensure-encryption-in-transit-for-dms-endpoints-for-redis-oss](https://support.icompaas.com/support/solutions/articles/62000233450-ensure-encryption-in-transit-for-dms-endpoints-for-redis-oss)

## 技术信息

- Source Metadata：[sources/aws/dms_endpoint_redis_in_transit_encryption_enabled/metadata.json](../../sources/aws/dms_endpoint_redis_in_transit_encryption_enabled/metadata.json)
- Source Code：[sources/aws/dms_endpoint_redis_in_transit_encryption_enabled/check.py](../../sources/aws/dms_endpoint_redis_in_transit_encryption_enabled/check.py)
- Source Metadata Path：`sources/aws/dms_endpoint_redis_in_transit_encryption_enabled/metadata.json`
- Source Code Path：`sources/aws/dms_endpoint_redis_in_transit_encryption_enabled/check.py`
