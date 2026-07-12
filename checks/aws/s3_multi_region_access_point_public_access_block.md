# Block Public Access Settings enabled on Multi Region Access Points.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `s3_multi_region_access_point_public_access_block` |
| クラウドプラットフォーム | AWS |
| サービス | s3 |
| 重大度 | high |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | AwsS3AccessPoint |
| リソースグループ | storage |

## 説明

Ensures that public access is blocked on S3 Access Points.

## リスク

Leaving S3 multi region access points open to the public in AWS can lead to data exposure, breaches, compliance violations, unauthorized access, and data integrity issues.

## 推奨事項

Ensure S3 multi region access points are private by default, applying strict access controls, and regularly auditing permissions to prevent unauthorized public access.

- 推奨リンク：[https://docs.aws.amazon.com/AmazonS3/latest/userguide/multi-region-access-point-block-public-access.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/multi-region-access-point-block-public-access.html)

## 修正手順


### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-24](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-24)

## 参考資料

- [https://aws.amazon.com/es/getting-started/hands-on/getting-started-with-amazon-s3-multi-region-access-points/](https://aws.amazon.com/es/getting-started/hands-on/getting-started-with-amazon-s3-multi-region-access-points/)
- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/multi-region-access-point-block-public-access.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/multi-region-access-point-block-public-access.html)

## 技術情報

- Source Metadata：[sources/aws/s3_multi_region_access_point_public_access_block/metadata.json](../../sources/aws/s3_multi_region_access_point_public_access_block/metadata.json)
- Source Code：[sources/aws/s3_multi_region_access_point_public_access_block/check.py](../../sources/aws/s3_multi_region_access_point_public_access_block/check.py)
- Source Metadata Path：`sources/aws/s3_multi_region_access_point_public_access_block/metadata.json`
- Source Code Path：`sources/aws/s3_multi_region_access_point_public_access_block/check.py`
