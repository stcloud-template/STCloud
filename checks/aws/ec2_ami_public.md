# Ensure there are no EC2 AMIs set as Public.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_ami_public` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| サブサービス | ami |
| 重大度 | critical |
| カテゴリ | internet-exposed |
| チェックタイプ | Infrastructure Security |
| リソースタイプ | Other |
| リソースグループ | compute |

## 説明

Ensure there are no EC2 AMIs set as Public.

## リスク

When your AMIs are publicly accessible, they are available in the Community AMIs where everyone with an AWS account can use them to launch EC2 instances. Your AMIs could contain snapshots of your applications (including their data), therefore exposing your snapshots in this manner is not advised.

## 推奨事項

We recommend your EC2 AMIs are not publicly accessible, or generally available in the Community AMIs.

- 推奨リンク：[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cancel-sharing-an-AMI.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cancel-sharing-an-AMI.html)

## 修正手順


### CLI

```text
aws ec2 modify-image-attribute --region <REGION> --image-id <EC2_AMI_ID> --launch-permission {"Remove":[{"Group":"all"}]}
```

### Other

[https://docs.ST Cloud.com/checks/aws/public-policies/public_8](https://docs.ST Cloud.com/checks/aws/public-policies/public_8)

## 参考資料

- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cancel-sharing-an-AMI.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cancel-sharing-an-AMI.html)

## 技術情報

- Source Metadata：[sources/aws/ec2_ami_public/metadata.json](../../sources/aws/ec2_ami_public/metadata.json)
- Source Code：[sources/aws/ec2_ami_public/check.py](../../sources/aws/ec2_ami_public/check.py)
- Source Metadata Path：`sources/aws/ec2_ami_public/metadata.json`
- Source Code Path：`sources/aws/ec2_ami_public/check.py`
