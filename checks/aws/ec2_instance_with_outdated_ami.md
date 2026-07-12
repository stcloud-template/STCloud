# Check for EC2 Instances Using Outdated AMIs

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_instance_with_outdated_ami` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | AwsEc2Instance |
| リソースグループ | compute |

## 説明

This check identifies EC2 instances using outdated Amazon Machine Images (AMIs) by auditing instances to gather AMI IDs, comparing them against the latest available versions, verifying suppo and security update status, and checking for deprecation.

## リスク

Using outdated AMIs can expose EC2 instances to security vulnerabilities, lack of support, and missing critical updates, increasing the risk of exploitation.

## 推奨事項

Regularly update your EC2 instances to use the latest AMIs to ensure they receive the latest security patches and updates.

- 推奨リンク：[https://repost.aws/knowledge-center/ec2-find-deprecated-ami](https://repost.aws/knowledge-center/ec2-find-deprecated-ami)

## 修正手順


### CLI

```text
aws ec2 describe-images --image-ids <ami-id>
```

### Other

[https://repost.aws/knowledge-center/ec2-find-deprecated-ami](https://repost.aws/knowledge-center/ec2-find-deprecated-ami)

## 参考資料

- [https://repost.aws/knowledge-center/ec2-find-deprecated-ami](https://repost.aws/knowledge-center/ec2-find-deprecated-ami)

## 技術情報

- Source Metadata：[sources/aws/ec2_instance_with_outdated_ami/metadata.json](../../sources/aws/ec2_instance_with_outdated_ami/metadata.json)
- Source Code：[sources/aws/ec2_instance_with_outdated_ami/check.py](../../sources/aws/ec2_instance_with_outdated_ami/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_with_outdated_ami/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_with_outdated_ami/check.py`
