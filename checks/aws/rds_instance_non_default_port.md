# Check if RDS instances are using non-default ports.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `rds_instance_non_default_port` |
| クラウドプラットフォーム | AWS |
| サービス | rds |
| 重大度 | low |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices |
| リソースタイプ | AwsRdsDbInstance |
| リソースグループ | database |

## 説明

Checks if an instance uses a port other than the default port of the database engine. The control fails if the RDS instance uses the default port.

## リスク

Using a default database port exposes the instance to potential security vulnerabilities, as attackers are more likely to target known, commonly-used ports. This may result in unauthorized access to the database or increased susceptibility to automated attacks.

## 推奨事項

Modify the RDS instance to use a non-default port, and ensure that the security group permits access to the new port.

- 推奨リンク：[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)

## 修正手順


### CLI

```text
aws rds modify-db-instance --db-instance-identifier <db-instance-id> --port <non-default-port>
```

### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-23](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-23)

## 参考資料

- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)

## 技術情報

- Source Metadata：[sources/aws/rds_instance_non_default_port/metadata.json](../../sources/aws/rds_instance_non_default_port/metadata.json)
- Source Code：[sources/aws/rds_instance_non_default_port/check.py](../../sources/aws/rds_instance_non_default_port/check.py)
- Source Metadata Path：`sources/aws/rds_instance_non_default_port/metadata.json`
- Source Code Path：`sources/aws/rds_instance_non_default_port/check.py`
