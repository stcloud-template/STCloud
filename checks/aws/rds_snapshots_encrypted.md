# Check if RDS Snapshots and Cluster Snapshots are encrypted.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `rds_snapshots_encrypted` |
| クラウドプラットフォーム | AWS |
| サービス | rds |
| 重大度 | medium |
| カテゴリ | encryption |
| リソースタイプ | AwsRdsDbSnapshot |
| リソースグループ | database |

## 説明

Check if RDS Snapshots and Cluster Snapshots are encrypted.

## リスク

Ensure that your manual Amazon RDS database snapshots are encrypted in order to achieve compliance for data-at-rest encryption within your organization.

## 推奨事項

When working with production databases that hold sensitive and critical data, it is strongly recommended to implement encryption at rest and protect your data from attackers or unauthorized personnel.

- 推奨リンク：[https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-4](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-4)

## 修正手順


### Native IaC

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/snapshot-encrypted.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/snapshot-encrypted.html#)

### Terraform

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/snapshot-encrypted.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/snapshot-encrypted.html#)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/snapshot-encrypted.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/snapshot-encrypted.html#)

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-4](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-4)

## 技術情報

- Source Metadata：[sources/aws/rds_snapshots_encrypted/metadata.json](../../sources/aws/rds_snapshots_encrypted/metadata.json)
- Source Code：[sources/aws/rds_snapshots_encrypted/check.py](../../sources/aws/rds_snapshots_encrypted/check.py)
- Source Metadata Path：`sources/aws/rds_snapshots_encrypted/metadata.json`
- Source Code Path：`sources/aws/rds_snapshots_encrypted/check.py`
