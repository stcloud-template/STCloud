# Glue connection has SSL enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `glue_database_connections_ssl_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | glue |
| 重大度 | high |
| カテゴリ | encryption |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark |
| リソースタイプ | Other |
| リソースグループ | analytics |

## 説明

**AWS Glue connections** require **TLS/SSL** for JDBC when the `JDBC_ENFORCE_SSL` property is set to `true`. This evaluates connection definitions to confirm SSL is enforced for traffic to external data stores.

## リスク

Absent TLS enforcement, JDBC traffic-including credentials, queries, and results-can be **intercepted or modified** in transit. This enables: - Confidentiality loss via sniffing/MITM - Integrity tampering of queries/results - Credential theft leading to broader database access

## 推奨事項

Enforce **TLS** on all Glue connections (set `JDBC_ENFORCE_SSL=true`) and require encryption on target databases. Apply **defense in depth**: validate certificates, restrict network exposure, prefer private connectivity, and use **least-privilege** credentials with rotation.

## 修正手順


### CLI

```text
aws glue update-connection --name <example_resource_name> --connection-input '{"Name":"<example_resource_name>","ConnectionType":"JDBC","ConnectionProperties":{"JDBC_CONNECTION_URL":"<example_jdbc_url>","JDBC_ENFORCE_SSL":"true"}}'
```

### Native IaC

```yaml
# CloudFormation: Enable SSL on a Glue JDBC connection
Resources:
  <example_resource_name>:
    Type: AWS::Glue::Connection
    Properties:
      ConnectionInput:
        ConnectionType: JDBC
        ConnectionProperties:
          JDBC_CONNECTION_URL: "<example_jdbc_url>"
          JDBC_ENFORCE_SSL: "true"  # Critical: forces SSL for the JDBC connection
```

### Terraform

```hcl
# Terraform: Enable SSL on a Glue JDBC connection
resource "aws_glue_connection" "<example_resource_name>" {
  name            = "<example_resource_name>"
  connection_type = "JDBC"

  connection_properties = {
    JDBC_CONNECTION_URL = "<example_jdbc_url>"
    JDBC_ENFORCE_SSL    = "true"  # Critical: forces SSL for the JDBC connection
  }
}
```

### Other

1. Open the AWS Console and go to AWS Glue > Data Catalog > Connections
2. Select the connection and click Edit
3. In Connection properties (Advanced properties), add key JDBC_ENFORCE_SSL with value true (or check Require SSL)
4. Click Save

## 参考資料

- [https://docs.aws.amazon.com/glue/latest/dg/encryption-in-transit.html](https://docs.aws.amazon.com/glue/latest/dg/encryption-in-transit.html)
- [https://support.icompaas.com/support/solutions/articles/62000233690-ensure-glue-connections-have-ssl-enabled](https://support.icompaas.com/support/solutions/articles/62000233690-ensure-glue-connections-have-ssl-enabled)

## 技術情報

- Source Metadata：[sources/aws/glue_database_connections_ssl_enabled/metadata.json](../../sources/aws/glue_database_connections_ssl_enabled/metadata.json)
- Source Code：[sources/aws/glue_database_connections_ssl_enabled/check.py](../../sources/aws/glue_database_connections_ssl_enabled/check.py)
- Source Metadata Path：`sources/aws/glue_database_connections_ssl_enabled/metadata.json`
- Source Code Path：`sources/aws/glue_database_connections_ssl_enabled/check.py`
