# Ensure IAM instance roles are used for AWS resource access from instances

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_instance_profile_attached` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark |
| リソースタイプ | AwsEc2Instance |
| リソースグループ | compute |

## 説明

Ensure IAM instance roles are used for AWS resource access from instances.

## リスク

AWS access from within AWS instances can be done by either encoding AWS keys into AWS API calls or by assigning the instance to a role which has an appropriate permissions policy for the required access. AWS IAM roles reduce the risks associated with sharing and rotating credentials that can be used outside of AWS itself. If credentials are compromised, they can be used from outside of the AWS account.

## 推奨事項

Create an IAM instance role if necessary and attach it to the corresponding EC2 instance..

- 推奨リンク：[http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html)

## 修正手順


### Other

[https://github.com/cloudmatos/matos/tree/master/remediations/aws/ec2/attach_iam_roles_ec2_instances](https://github.com/cloudmatos/matos/tree/master/remediations/aws/ec2/attach_iam_roles_ec2_instances)

## 参考資料

- [http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html)

## 技術情報

- Source Metadata：[sources/aws/ec2_instance_profile_attached/metadata.json](../../sources/aws/ec2_instance_profile_attached/metadata.json)
- Source Code：[sources/aws/ec2_instance_profile_attached/check.py](../../sources/aws/ec2_instance_profile_attached/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_profile_attached/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_profile_attached/check.py`
