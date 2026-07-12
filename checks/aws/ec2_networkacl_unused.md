# Unused Network Access Control Lists should be removed.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_networkacl_unused` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| 重大度 | low |
| カテゴリ | internet-exposed |
| リソースタイプ | AwsEc2NetworkAcl |
| リソースグループ | network |

## 説明

Ensure that there are no unused network access control lists (network ACLs) in your virtual private cloud (VPC). The control fails if the network ACL isn't associated with a subnet. The control doesn't generate findings for an unused default network ACL.

## リスク

Unused network ACLs may represent a potential security risk if left in place without purpose, as they could be mistakenly associated with subnets later.

## 推奨事項

For instructions on deleting an unused network ACL, see Deleting a network ACL in the Amazon VPC User Guide.

- 推奨リンク：[https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html#vpc-network-acl-delete](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html#vpc-network-acl-delete)

## 修正手順


### CLI

```text
aws ec2 delete-network-acl --network-acl-id <nacl_id>
```

### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-16](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-16)

## 参考資料

- [https://docs.aws.amazon.com/config/latest/developerguide/vpc-network-acl-unused-check.html](https://docs.aws.amazon.com/config/latest/developerguide/vpc-network-acl-unused-check.html)
- [https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html#vpc-network-acl-delete](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html#vpc-network-acl-delete)

## 技術情報

- Source Metadata：[sources/aws/ec2_networkacl_unused/metadata.json](../../sources/aws/ec2_networkacl_unused/metadata.json)
- Source Code：[sources/aws/ec2_networkacl_unused/check.py](../../sources/aws/ec2_networkacl_unused/check.py)
- Source Metadata Path：`sources/aws/ec2_networkacl_unused/metadata.json`
- Source Code Path：`sources/aws/ec2_networkacl_unused/check.py`
