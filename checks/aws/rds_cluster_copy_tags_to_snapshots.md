# Check if RDS DB clusters have copy tags to snapshots enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `rds_cluster_copy_tags_to_snapshots` |
| クラウドプラットフォーム | AWS |
| サービス | rds |
| 重大度 | low |
| カテゴリ | Uncategorized |
| リソースタイプ | AwsRdsDbCluster |
| リソースグループ | database |

## 説明

Check if RDS DB clusters have copy tags to snapshots enabled, Aurora instances do not support this feature at instance level so those who are clustered will be scan by this check.

## リスク

If RDS clusters are not configured to copy tags to snapshots, it could lead to compliance issues as the snapshots will not inherit necessary metadata such as environment, owner, or purpose tags. This could result in inefficient tracking and management of RDS resources and their snapshots.

## 推奨事項

Ensure that the `CopyTagsToSnapshot` setting is enabled for all RDS clusters to propagate cluster tags to their snapshots for improved tracking and compliance.

- 推奨リンク：[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html#USER_Tagging.CopyTags](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html#USER_Tagging.CopyTags)

## 修正手順


### CLI

```text
aws rds modify-db-cluster --db-cluster-identifier <cluster-identifier> --copy-tags-to-snapshot
```

### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-16](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-16)

## 参考資料

- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html#USER_Tagging.CopyTags](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html#USER_Tagging.CopyTags)

## 技術情報

- Source Metadata：[sources/aws/rds_cluster_copy_tags_to_snapshots/metadata.json](../../sources/aws/rds_cluster_copy_tags_to_snapshots/metadata.json)
- Source Code：[sources/aws/rds_cluster_copy_tags_to_snapshots/check.py](../../sources/aws/rds_cluster_copy_tags_to_snapshots/check.py)
- Source Metadata Path：`sources/aws/rds_cluster_copy_tags_to_snapshots/metadata.json`
- Source Code Path：`sources/aws/rds_cluster_copy_tags_to_snapshots/check.py`
