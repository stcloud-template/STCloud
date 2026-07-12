# Check if RDS Snapshots and Cluster Snapshots are public.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `rds_snapshots_public_access` |
| クラウドプラットフォーム | AWS |
| サービス | rds |
| 重大度 | critical |
| カテゴリ | internet-exposed |
| リソースタイプ | AwsRdsDbSnapshot |
| リソースグループ | database |

## 説明

Check if RDS Snapshots and Cluster Snapshots are public.

## リスク

Publicly accessible services could expose sensitive data to bad actors. t is recommended that your RDS snapshots should not be public in order to prevent potential leak or misuse of sensitive data or any other kind of security threat. If your RDS snapshot is public, then the data which is backed up in that snapshot is accessible to all other AWS accounts.

## 推奨事項

Use AWS Config to identify any snapshot that is public.

- 推奨リンク：[https://docs.aws.amazon.com/config/latest/developerguide/rds-snapshots-public-prohibited.html](https://docs.aws.amazon.com/config/latest/developerguide/rds-snapshots-public-prohibited.html)

## 修正手順


### CLI

```text
aws rds modify-db-snapshot-attribute --db-snapshot-identifier <snapshot_id> --attribute-name restore --values-to-remove all
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/public-snapshots.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/public-snapshots.html)

## 参考資料

- [https://docs.aws.amazon.com/config/latest/developerguide/rds-snapshots-public-prohibited.html](https://docs.aws.amazon.com/config/latest/developerguide/rds-snapshots-public-prohibited.html)

## 技術情報

- Source Metadata：[sources/aws/rds_snapshots_public_access/metadata.json](../../sources/aws/rds_snapshots_public_access/metadata.json)
- Source Code：[sources/aws/rds_snapshots_public_access/check.py](../../sources/aws/rds_snapshots_public_access/check.py)
- Source Metadata Path：`sources/aws/rds_snapshots_public_access/metadata.json`
- Source Code Path：`sources/aws/rds_snapshots_public_access/check.py`
