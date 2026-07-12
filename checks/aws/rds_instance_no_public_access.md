# Ensure there are no Public Accessible RDS instances.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `rds_instance_no_public_access` |
| クラウドプラットフォーム | AWS |
| サービス | rds |
| 重大度 | critical |
| カテゴリ | internet-exposed |
| リソースタイプ | AwsRdsDbInstance |
| リソースグループ | database |

## 説明

Ensure there are no Public Accessible RDS instances.

## リスク

Publicly accessible databases could expose sensitive data to bad actors.

## 推奨事項

Using an AWS Config rule check for RDS public instances periodically and check there is a business reason for it.

- 推奨リンク：[https://docs.aws.amazon.com/config/latest/developerguide/rds-instance-public-access-check.html](https://docs.aws.amazon.com/config/latest/developerguide/rds-instance-public-access-check.html)

## 修正手順


### CLI

```text
aws rds modify-db-instance --db-instance-identifier <db_instance_id> --no-publicly-accessible --apply-immediately
```

### Native IaC

[https://docs.ST Cloud.com/checks/aws/public-policies/public_2#cloudformation](https://docs.ST Cloud.com/checks/aws/public-policies/public_2#cloudformation)

### Terraform

[https://docs.ST Cloud.com/checks/aws/public-policies/public_2#terraform](https://docs.ST Cloud.com/checks/aws/public-policies/public_2#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-publicly-accessible.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-publicly-accessible.html)

## 参考資料

- [https://docs.aws.amazon.com/config/latest/developerguide/rds-instance-public-access-check.html](https://docs.aws.amazon.com/config/latest/developerguide/rds-instance-public-access-check.html)

## 技術情報

- Source Metadata：[sources/aws/rds_instance_no_public_access/metadata.json](../../sources/aws/rds_instance_no_public_access/metadata.json)
- Source Code：[sources/aws/rds_instance_no_public_access/check.py](../../sources/aws/rds_instance_no_public_access/check.py)
- Source Metadata Path：`sources/aws/rds_instance_no_public_access/metadata.json`
- Source Code Path：`sources/aws/rds_instance_no_public_access/check.py`
