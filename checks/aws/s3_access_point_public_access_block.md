# Block Public Access Settings enabled on Access Points.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `s3_access_point_public_access_block` |
| クラウドプラットフォーム | AWS |
| サービス | s3 |
| 重大度 | critical |
| カテゴリ | Uncategorized |
| チェックタイプ | Data Protection |
| リソースタイプ | AwsS3AccessPoint |
| リソースグループ | storage |

## 説明

Ensures that public access is blocked on S3 Access Points.

## リスク

Leaving S3 access points open to the public in AWS can lead to data exposure, breaches, compliance violations, unauthorized access, and data integrity issues.

## 推奨事項

Ensure S3 access points are private by default, applying strict access controls, and regularly auditing permissions to prevent unauthorized public access.

- 推奨リンク：[https://docs.aws.amazon.com/config/latest/developerguide/s3-access-point-public-access-blocks.html](https://docs.aws.amazon.com/config/latest/developerguide/s3-access-point-public-access-blocks.html)

## 修正手順


### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-19](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-19)

## 参考資料

- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html#access-points-policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html#access-points-policies)
- [https://docs.aws.amazon.com/config/latest/developerguide/s3-access-point-public-access-blocks.html](https://docs.aws.amazon.com/config/latest/developerguide/s3-access-point-public-access-blocks.html)

## 技術情報

- Source Metadata：[sources/aws/s3_access_point_public_access_block/metadata.json](../../sources/aws/s3_access_point_public_access_block/metadata.json)
- Source Code：[sources/aws/s3_access_point_public_access_block/check.py](../../sources/aws/s3_access_point_public_access_block/check.py)
- Source Metadata Path：`sources/aws/s3_access_point_public_access_block/metadata.json`
- Source Code Path：`sources/aws/s3_access_point_public_access_block/check.py`
