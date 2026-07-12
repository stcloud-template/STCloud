# Find secrets in EC2 User Data.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_instance_secrets_user_data` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| 重大度 | critical |
| カテゴリ | secrets |
| チェックタイプ | IAM |
| リソースタイプ | AwsEc2Instance |
| リソースグループ | compute |

## 説明

Find secrets in EC2 User Data.

## リスク

Secrets hardcoded into instance user data can be used by malware and bad actors to gain lateral access to other services.

## 推奨事項

Implement automated detective control (e.g. using tools like ST Cloud) to scan accounts for passwords and secrets. Use secrets manager service to store and retrieve passwords and secrets.

- 推奨リンク：[https://docs.aws.amazon.com/secretsmanager/latest/userguide/tutorials_basic.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/tutorials_basic.html)

## 修正手順


### CLI

```text
aws ec2 describe-instance-attribute --attribute userData --region <REGION> --instance-id <INSTANCE_ID> --query UserData.Value --output text > encodeddata; base64 --decode encodeddata
```

### Native IaC

[https://docs.ST Cloud.com/checks/aws/secrets-policies/bc_aws_secrets_1#cloudformation](https://docs.ST Cloud.com/checks/aws/secrets-policies/bc_aws_secrets_1#cloudformation)

### Terraform

[https://docs.ST Cloud.com/checks/aws/secrets-policies/bc_aws_secrets_1#terraform](https://docs.ST Cloud.com/checks/aws/secrets-policies/bc_aws_secrets_1#terraform)

### Other

[https://docs.ST Cloud.com/checks/aws/secrets-policies/bc_aws_secrets_1](https://docs.ST Cloud.com/checks/aws/secrets-policies/bc_aws_secrets_1)

## 参考資料

- [https://docs.aws.amazon.com/secretsmanager/latest/userguide/tutorials_basic.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/tutorials_basic.html)

## 技術情報

- Source Metadata：[sources/aws/ec2_instance_secrets_user_data/metadata.json](../../sources/aws/ec2_instance_secrets_user_data/metadata.json)
- Source Code：[sources/aws/ec2_instance_secrets_user_data/check.py](../../sources/aws/ec2_instance_secrets_user_data/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_secrets_user_data/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_secrets_user_data/check.py`
