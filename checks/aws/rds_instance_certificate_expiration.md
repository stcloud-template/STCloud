# Ensure that the SSL/TLS certificates configured for your Amazon RDS are not expired.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `rds_instance_certificate_expiration` |
| 云平台 | AWS |
| 服务 | rds |
| 严重等级 | high |
| 类别 | encryption |
| 资源类型 | AwsRdsDbInstance |
| 资源组 | database |

## 描述

To maintain Amazon RDS database security and avoid interruption of the applications that are using RDS and/or Aurora databases, rotate the required SSL/TLS certificates and update the deprecated Certificate Authority (CA) certificates at the Amazon RDS instance level.

## 风险

Interruption of application if the certificate expires.

## 推荐措施

To maintain Amazon RDS database security and avoid interruption of the applications that are using RDS and/or Aurora databases, rotate the required SSL/TLS certificates and update the deprecated Certificate Authority (CA) certificates at the Amazon RDS instance level.

- 推荐链接：[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL-certificate-rotation.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL-certificate-rotation.html)

## 修复步骤


### CLI

```text
aws rds modify-db-instance --region us-east-1 --db-instance-identifier cc-project5-mysql-database --ca-certificate-identifier "rds-ca-2019" --apply-immediately
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rotate-rds-certificates.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rotate-rds-certificates.html)

## 参考资料

- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL-certificate-rotation.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL-certificate-rotation.html)

## 技术信息

- Source Metadata：[sources/aws/rds_instance_certificate_expiration/metadata.json](../../sources/aws/rds_instance_certificate_expiration/metadata.json)
- Source Code：[sources/aws/rds_instance_certificate_expiration/check.py](../../sources/aws/rds_instance_certificate_expiration/check.py)
- Source Metadata Path：`sources/aws/rds_instance_certificate_expiration/metadata.json`
- Source Code Path：`sources/aws/rds_instance_certificate_expiration/check.py`
