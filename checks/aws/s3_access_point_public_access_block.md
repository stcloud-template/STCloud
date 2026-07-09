# Block Public Access Settings enabled on Access Points.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `s3_access_point_public_access_block` |
| 云平台 | AWS |
| 服务 | s3 |
| 严重等级 | critical |
| 类别 | Uncategorized |
| 检查类型 | Data Protection |
| 资源类型 | AwsS3AccessPoint |
| 资源组 | storage |

## 描述

Ensures that public access is blocked on S3 Access Points.

## 风险

Leaving S3 access points open to the public in AWS can lead to data exposure, breaches, compliance violations, unauthorized access, and data integrity issues.

## 推荐措施

Ensure S3 access points are private by default, applying strict access controls, and regularly auditing permissions to prevent unauthorized public access.

- 推荐链接：[https://docs.aws.amazon.com/config/latest/developerguide/s3-access-point-public-access-blocks.html](https://docs.aws.amazon.com/config/latest/developerguide/s3-access-point-public-access-blocks.html)

## 修复步骤


### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-19](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-19)

## 参考资料

- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html#access-points-policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html#access-points-policies)
- [https://docs.aws.amazon.com/config/latest/developerguide/s3-access-point-public-access-blocks.html](https://docs.aws.amazon.com/config/latest/developerguide/s3-access-point-public-access-blocks.html)

## 技术信息

- Source Metadata：[sources/aws/s3_access_point_public_access_block/metadata.json](../../sources/aws/s3_access_point_public_access_block/metadata.json)
- Source Code：[sources/aws/s3_access_point_public_access_block/check.py](../../sources/aws/s3_access_point_public_access_block/check.py)
- Source Metadata Path：`sources/aws/s3_access_point_public_access_block/metadata.json`
- Source Code Path：`sources/aws/s3_access_point_public_access_block/check.py`
