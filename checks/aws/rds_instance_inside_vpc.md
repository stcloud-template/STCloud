# Check if RDS instances are deployed within a VPC.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `rds_instance_inside_vpc` |
| クラウドプラットフォーム | AWS |
| サービス | rds |
| 重大度 | high |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks, AWS Security Best Practices |
| リソースタイプ | AwsRdsDbInstance |
| リソースグループ | database |

## 説明

Check if RDS instances are deployed within a VPC.

## リスク

If your RDS instances are not deployed within a VPC, they are not isolated from the public internet and are exposed to potential security threats. Deploying RDS instances within a VPC allows you to control inbound and outbound traffic to and from the instances, and provides an additional layer of security to your database instances.

## 推奨事項

Ensure that your RDS instances are deployed within a VPC to provide an additional layer of security to your database instances.

- 推奨リンク：[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)

## 修正手順


### CLI

```text
aws rds modify-db-instance --db-instance-identifier <instance-identifier> --vpc-security-group-ids <vpc-security-group-ids>
```

### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-18](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-18)

## 参考資料

- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.Subnets](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.Subnets)
- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)

## 技術情報

- Source Metadata：[sources/aws/rds_instance_inside_vpc/metadata.json](../../sources/aws/rds_instance_inside_vpc/metadata.json)
- Source Code：[sources/aws/rds_instance_inside_vpc/check.py](../../sources/aws/rds_instance_inside_vpc/check.py)
- Source Metadata Path：`sources/aws/rds_instance_inside_vpc/metadata.json`
- Source Code Path：`sources/aws/rds_instance_inside_vpc/check.py`
