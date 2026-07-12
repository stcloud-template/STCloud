# CloudWatch Log Group is not publicly accessible

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudwatch_log_group_not_publicly_accessible` |
| クラウドプラットフォーム | AWS |
| サービス | cloudwatch |
| 重大度 | high |
| カテゴリ | internet-exposed, identity-access |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, TTPs/Initial Access/Unauthorized Access, Effects/Data Exposure |
| リソースタイプ | Other |
| リソースグループ | monitoring |

## 説明

**CloudWatch Log Groups** with resource policies that grant access to any principal are identified. Statements using `Principal:"*"` or wildcard `Resource` that reference a log group ARN indicate that the log group is exposed through a public policy.

## リスク

Public access to log groups enables unauthorized reading of logs, revealing secrets and operational metadata, harming **confidentiality**. If broad actions are allowed, attackers can modify subscriptions or logs, undermining **integrity** and disrupting **availability** of audit evidence.

## 推奨事項

Remove public access from log group resource policies. Replace `Principal:"*"` and `Resource:"*"` with narrowly scoped principals and specific ARNs. Grant only necessary actions, apply conditions to constrain use, and enforce **least privilege** and **separation of duties** with regular policy reviews.

## 修正手順


### CLI

```text
aws logs delete-resource-policy --policy-name <policy-name>
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::Logs::ResourcePolicy
    Properties:
      PolicyName: <example_resource_name>
      PolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              AWS: "<example_account_id>"  # FIX: restrict to specific account (not *) to prevent public access
            Action: logs:PutSubscriptionFilter
            Resource: "arn:aws:logs:<region>:<account-id>:destination:<example_resource_name>"
```

### Terraform

```hcl
resource "aws_cloudwatch_log_resource_policy" "<example_resource_name>" {
  policy_name     = "<example_resource_name>"
  policy_document = jsonencode({
    Version   = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { AWS = "<example_account_id>" } # FIX: restrict Principal (not "*") to avoid public access
      Action    = "logs:PutSubscriptionFilter"
      Resource  = "arn:aws:logs:<region>:<account-id>:destination:<example_resource_name>"
    }]
  })
}
```

### Other

1. Open the CloudWatch console
2. Go to Logs > Resource policies
3. Select the policy that exposes your log groups (Principal set to "*" or Resource "*")
4. Click Delete and confirm

## 参考資料

- [https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.html](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.html)

## 技術情報

- Source Metadata：[sources/aws/cloudwatch_log_group_not_publicly_accessible/metadata.json](../../sources/aws/cloudwatch_log_group_not_publicly_accessible/metadata.json)
- Source Code：[sources/aws/cloudwatch_log_group_not_publicly_accessible/check.py](../../sources/aws/cloudwatch_log_group_not_publicly_accessible/check.py)
- Source Metadata Path：`sources/aws/cloudwatch_log_group_not_publicly_accessible/metadata.json`
- Source Code Path：`sources/aws/cloudwatch_log_group_not_publicly_accessible/check.py`
