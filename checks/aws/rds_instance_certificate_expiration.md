# Ensure that the SSL/TLS certificates configured for your Amazon RDS are not expired.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `rds_instance_certificate_expiration` |
| クラウドプラットフォーム | AWS |
| サービス | rds |
| 重大度 | high |
| カテゴリ | encryption |
| リソースタイプ | AwsRdsDbInstance |
| リソースグループ | database |

## 説明

To maintain Amazon RDS database security and avoid interruption of the applications that are using RDS and/or Aurora databases, rotate the required SSL/TLS certificates and update the deprecated Certificate Authority (CA) certificates at the Amazon RDS instance level.

## リスク

Interruption of application if the certificate expires.

## 推奨事項

To maintain Amazon RDS database security and avoid interruption of the applications that are using RDS and/or Aurora databases, rotate the required SSL/TLS certificates and update the deprecated Certificate Authority (CA) certificates at the Amazon RDS instance level.

- 推奨リンク：[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL-certificate-rotation.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL-certificate-rotation.html)

## 修正手順


### CLI

```text
aws rds modify-db-instance --region us-east-1 --db-instance-identifier cc-project5-mysql-database --ca-certificate-identifier "rds-ca-2019" --apply-immediately
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rotate-rds-certificates.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rotate-rds-certificates.html)

## 参考資料

- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL-certificate-rotation.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL-certificate-rotation.html)

## 技術情報

- Source Metadata：[sources/aws/rds_instance_certificate_expiration/metadata.json](../../sources/aws/rds_instance_certificate_expiration/metadata.json)
- Source Code：[sources/aws/rds_instance_certificate_expiration/check.py](../../sources/aws/rds_instance_certificate_expiration/check.py)
- Source Metadata Path：`sources/aws/rds_instance_certificate_expiration/metadata.json`
- Source Code Path：`sources/aws/rds_instance_certificate_expiration/check.py`
