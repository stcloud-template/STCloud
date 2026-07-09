# DMS endpoint has SSL enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `dms_endpoint_ssl_enabled` |
| 云平台 | AWS |
| 服务 | dms |
| 严重等级 | high |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Effects/Data Exposure |
| 资源类型 | AwsDmsEndpoint |
| 资源组 | database |

## 描述

**AWS DMS endpoints** have their SSL/TLS mode inspected; any value other than `none` denotes encrypted connections between the replication instance and databases. Supported modes include `require`, `verify-ca`, and `verify-full`.

## 风险

Without TLS, data in transit can be read or altered, affecting: - **Confidentiality** via packet sniffing and credential leakage - **Integrity** through **MITM** tampering of migration streams - **Availability** from session hijack or task disruption

## 推荐措施

Configure endpoints to use SSL/TLS at least `require`; prefer `verify-ca` or `verify-full` where supported. Manage trusted CA material and rotate regularly. Apply **defense in depth** with private connectivity and strict IAM, and enforce this posture via policy-as-code and continuous validation.

## 修复步骤


### CLI

```text
aws dms modify-endpoint --endpoint-arn <endpoint-arn> --ssl-mode require
```

### Native IaC

```yaml
# CloudFormation: Set SSL on a DMS endpoint
Resources:
  <example_resource_name>:
    Type: AWS::DMS::Endpoint
    Properties:
      EndpointIdentifier: <example_resource_name>
      EndpointType: source
      EngineName: sqlserver
      ServerName: <server_name>
      Port: 1433
      Username: <username>
      Password: <password>
      SslMode: require  # CRITICAL: enables SSL (not "none"), fixing the finding
```

### Terraform

```hcl
# Terraform: Set SSL on a DMS endpoint
resource "aws_dms_endpoint" "<example_resource_name>" {
  endpoint_id   = "<example_resource_name>"
  endpoint_type = "source"
  engine_name   = "sqlserver"
  server_name   = "<server_name>"
  port          = 1433
  username      = "<username>"
  password      = "<password>"

  ssl_mode = "require" # CRITICAL: enables SSL (not "none"), fixing the finding
}
```

### Other

1. In the AWS DMS console, go to Endpoints
2. Select the non-compliant endpoint and choose Modify
3. Set SSL mode to Require (or Verify-ca/Verify-full if required by your engine and certificate is available)
4. If Verify-ca/Verify-full is selected, choose the appropriate CA certificate
5. Save changes, then Test connection to confirm

## 参考资料

- [https://aws.amazon.com/blogs/database/configuring-ssl-encryption-on-oracle-and-postgresql-endpoints-in-aws-dms/](https://aws.amazon.com/blogs/database/configuring-ssl-encryption-on-oracle-and-postgresql-endpoints-in-aws-dms/)
- [https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.SSL.html](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.SSL.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/dms-controls.html#dms-9](https://docs.aws.amazon.com/securityhub/latest/userguide/dms-controls.html#dms-9)

## 技术信息

- Source Metadata：[sources/aws/dms_endpoint_ssl_enabled/metadata.json](../../sources/aws/dms_endpoint_ssl_enabled/metadata.json)
- Source Code：[sources/aws/dms_endpoint_ssl_enabled/check.py](../../sources/aws/dms_endpoint_ssl_enabled/check.py)
- Source Metadata Path：`sources/aws/dms_endpoint_ssl_enabled/metadata.json`
- Source Code Path：`sources/aws/dms_endpoint_ssl_enabled/check.py`
