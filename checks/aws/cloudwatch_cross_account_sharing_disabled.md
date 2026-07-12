# CloudWatch does not allow cross-account sharing

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudwatch_cross_account_sharing_disabled` |
| クラウドプラットフォーム | AWS |
| サービス | cloudwatch |
| 重大度 | medium |
| カテゴリ | trust-boundaries, identity-access |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exposure |
| リソースタイプ | AwsIamRole |
| リソースグループ | IAM |

## 説明

**Amazon CloudWatch** cross-account sharing via the `CloudWatch-CrossAccountSharingRole` allows other AWS accounts to view your metrics, dashboards, and alarms. The presence of this role indicates that sharing is active.

## リスク

Granting other accounts visibility into observability data reduces **confidentiality** and enables **reconnaissance**. Adversaries or over-privileged partners can map architectures, profile workloads, and spot alerting gaps, increasing chances of **lateral movement** and **evasion**.

## 推奨事項

Disable **cross-account sharing** unless strictly required. If needed, restrict access to specific trusted accounts, scope read-only permissions to only necessary resources, and use a dedicated monitoring account. Apply **least privilege** and **separation of duties**, and regularly audit role trust and access patterns.

## 修正手順


### CLI

```text
aws cloudformation delete-stack --stack-name CloudWatch-CrossAccountSharingRole
```

### Other

1. Sign in to the AWS Management Console and open IAM
2. Go to Roles
3. Find and select the role named "CloudWatch-CrossAccountSharingRole"
4. Click Delete and confirm
5. If deletion is blocked because it is managed by CloudFormation: open CloudFormation, select the stack named "CloudWatch-CrossAccountSharingRole", and click Delete

## 参考資料

- [https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.html](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.html)

## 技術情報

- Source Metadata：[sources/aws/cloudwatch_cross_account_sharing_disabled/metadata.json](../../sources/aws/cloudwatch_cross_account_sharing_disabled/metadata.json)
- Source Code：[sources/aws/cloudwatch_cross_account_sharing_disabled/check.py](../../sources/aws/cloudwatch_cross_account_sharing_disabled/check.py)
- Source Metadata Path：`sources/aws/cloudwatch_cross_account_sharing_disabled/metadata.json`
- Source Code Path：`sources/aws/cloudwatch_cross_account_sharing_disabled/check.py`
