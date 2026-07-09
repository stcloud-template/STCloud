# Block Public Access Settings enabled on Multi Region Access Points.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `s3_multi_region_access_point_public_access_block` |
| 云平台 | AWS |
| 服务 | s3 |
| 严重等级 | high |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsS3AccessPoint |
| 资源组 | storage |

## 描述

Ensures that public access is blocked on S3 Access Points.

## 风险

Leaving S3 multi region access points open to the public in AWS can lead to data exposure, breaches, compliance violations, unauthorized access, and data integrity issues.

## 推荐措施

Ensure S3 multi region access points are private by default, applying strict access controls, and regularly auditing permissions to prevent unauthorized public access.

- 推荐链接：[https://docs.aws.amazon.com/AmazonS3/latest/userguide/multi-region-access-point-block-public-access.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/multi-region-access-point-block-public-access.html)

## 修复步骤


### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-24](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-24)

## 参考资料

- [https://aws.amazon.com/es/getting-started/hands-on/getting-started-with-amazon-s3-multi-region-access-points/](https://aws.amazon.com/es/getting-started/hands-on/getting-started-with-amazon-s3-multi-region-access-points/)
- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/multi-region-access-point-block-public-access.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/multi-region-access-point-block-public-access.html)

## 技术信息

- Source Metadata：[sources/aws/s3_multi_region_access_point_public_access_block/metadata.json](../../sources/aws/s3_multi_region_access_point_public_access_block/metadata.json)
- Source Code：[sources/aws/s3_multi_region_access_point_public_access_block/check.py](../../sources/aws/s3_multi_region_access_point_public_access_block/check.py)
- Source Metadata Path：`sources/aws/s3_multi_region_access_point_public_access_block/metadata.json`
- Source Code Path：`sources/aws/s3_multi_region_access_point_public_access_block/check.py`
