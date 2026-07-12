# Check if RDS instances enforce SSL/TLS encryption for client connections (Microsoft SQL Server, PostgreSQL, MySQL, MariaDB, Aurora PostgreSQL, and Aurora MySQL).

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `rds_instance_transport_encrypted` |
| クラウドプラットフォーム | AWS |
| サービス | rds |
| 重大度 | high |
| カテゴリ | encryption |
| リソースタイプ | AwsRdsDbInstance |
| リソースグループ | database |

## 説明

For SQL Server, PostgreSQL, and Aurora PostgreSQL databases, if the `rds.force_ssl` parameter value is set to 0, SSL/TLS connections are not enforced. For MySQL, Aurora MySQL, and MariaDB databases, if the `require_secure_transport` parameter value is set to OFF, SSL/TLS connections are not enforced. Enforcing SSL/TLS ensures that all client connections to RDS instances are encrypted, protecting sensitive information in transit.

## リスク

If not enabled, sensitive information in transit is not protected.

## 推奨事項

Ensure that instances provisioned with Amazon RDS enforce SSL/TLS for client connections to meet security and compliance requirements.

- 推奨リンク：[https://aws.amazon.com/premiumsupport/knowledge-center/rds-connect-ssl-connection/](https://aws.amazon.com/premiumsupport/knowledge-center/rds-connect-ssl-connection/)

## 修正手順


### CLI

```text
aws rds modify-db-parameter-group --region <REGION_NAME> --db-parameter-group-name <PARAMETER_GROUP_NAME> --parameters ParameterName='rds.force_ssl',ParameterValue='1',ApplyMethod='pending-reboot'
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/transport-encryption.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/transport-encryption.html)

## 参考資料

- [https://aws.amazon.com/premiumsupport/knowledge-center/rds-connect-ssl-connection/](https://aws.amazon.com/premiumsupport/knowledge-center/rds-connect-ssl-connection/)

## 技術情報

- Source Metadata：[sources/aws/rds_instance_transport_encrypted/metadata.json](../../sources/aws/rds_instance_transport_encrypted/metadata.json)
- Source Code：[sources/aws/rds_instance_transport_encrypted/check.py](../../sources/aws/rds_instance_transport_encrypted/check.py)
- Source Metadata Path：`sources/aws/rds_instance_transport_encrypted/metadata.json`
- Source Code Path：`sources/aws/rds_instance_transport_encrypted/check.py`
