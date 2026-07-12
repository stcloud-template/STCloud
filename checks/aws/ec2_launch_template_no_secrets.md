# Find secrets in EC2 Launch Template

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_launch_template_no_secrets` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| 重大度 | critical |
| カテゴリ | secrets |
| リソースタイプ | AwsEc2LaunchTemplate |
| リソースグループ | compute |

## 説明

Find secrets in EC2 Launch Template

## リスク

The use of a hard-coded password increases the possibility of password guessing. If hard-coded passwords are used, it is possible that malicious users gain access through the account in question.

## 推奨事項

Do not include sensitive information in user data within the launch templates, try to use Secrets Manager instead.

- 推奨リンク：[https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html)
- [https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)

## 技術情報

- Source Metadata：[sources/aws/ec2_launch_template_no_secrets/metadata.json](../../sources/aws/ec2_launch_template_no_secrets/metadata.json)
- Source Code：[sources/aws/ec2_launch_template_no_secrets/check.py](../../sources/aws/ec2_launch_template_no_secrets/check.py)
- Source Metadata Path：`sources/aws/ec2_launch_template_no_secrets/metadata.json`
- Source Code Path：`sources/aws/ec2_launch_template_no_secrets/check.py`
