# CloudWatch log group contains no secrets in its log events

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudwatch_log_group_no_secrets_in_logs` |
| クラウドプラットフォーム | AWS |
| サービス | cloudwatch |
| 重大度 | medium |
| カテゴリ | secrets |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis, Sensitive Data Identifications/Passwords, Sensitive Data Identifications/Security, Effects/Data Exposure |
| リソースタイプ | Other |
| リソースグループ | monitoring |

## 説明

**CloudWatch Logs** log groups are analyzed for potential **secrets** embedded in log events across their streams. Detection flags patterns resembling credentials (API keys, passwords, tokens, keys) and reports the secret types and where they appear within the log group.

## リスク

Leaked **credentials in logs** erode confidentiality and enable unauthorized API calls. Attackers reusing tokens/keys can escalate privileges, alter resources, and exfiltrate data. Subscriptions and exports widen exposure, and users with `logs:Unmask` can reveal values, increasing the blast radius.

## 推奨事項

Avoid logging **secrets** via application sanitization and data minimization. Apply CloudWatch data protection policies to audit and mask sensitive patterns. Enforce *least privilege* for log readers and restrict `logs:Unmask`. Rotate exposed keys, reduce retention, and monitor findings to validate controls.

## 修正手順


### CLI

```text
aws logs put-data-protection-policy --log-group-identifier <example_resource_name> --policy-document '{"Statement":[{"DataIdentifier":["arn:aws:dataprotection::aws:data-identifier/Credentials"],"Operation":{"Audit":{"FindingsDestination":{}}}},{"DataIdentifier":["arn:aws:dataprotection::aws:data-identifier/Credentials"],"Operation":{"Deidentify":{"MaskConfig":{}}}}]}'
```

### Native IaC

```yaml
# CloudFormation: apply data protection policy to mask secrets in a log group
Resources:
  LogGroup:
    Type: AWS::Logs::LogGroup
    Properties:
      LogGroupName: <example_resource_name>
      # Critical: Enables masking of detected credentials at egress so secrets aren't exposed
      DataProtectionPolicy: |
        {"Statement":[{"DataIdentifier":["arn:aws:dataprotection::aws:data-identifier/Credentials"],"Operation":{"Audit":{"FindingsDestination":{}}}},{"DataIdentifier":["arn:aws:dataprotection::aws:data-identifier/Credentials"],"Operation":{"Deidentify":{"MaskConfig":{}}}}]}
```

### Terraform

```hcl
# Apply a CloudWatch Logs data protection policy to mask secrets
resource "aws_cloudwatch_log_group" "log_group" {
  name = "<example_resource_name>"

  # Critical: Masks detected credentials so secrets aren't visible and the check passes
  data_protection_policy = jsonencode({
    Statement = [
      {
        DataIdentifier = [
          "arn:aws:dataprotection::aws:data-identifier/Credentials"
        ]
        Operation = { Audit = { FindingsDestination = {} } }
      },
      {
        DataIdentifier = [
          "arn:aws:dataprotection::aws:data-identifier/Credentials"
        ]
        Operation = { Deidentify = { MaskConfig = {} } }
      }
    ]
  })
}
```

### Other

1. In AWS Console, go to CloudWatch > Logs > Log groups and open <example_resource_name>
2. Select the Data protection tab and click Create policy
3. Under Managed data identifiers, select Credentials (or AwsSecretKey if listed)
4. Click Activate data protection to save
5. Re-ingest or generate new logs to ensure sensitive data is masked

## 参考資料

- [https://support.icompaas.com/support/solutions/articles/62000233413-ensure-secrets-are-not-logged-in-cloudwatch-logs](https://support.icompaas.com/support/solutions/articles/62000233413-ensure-secrets-are-not-logged-in-cloudwatch-logs)
- [https://awsfundamentals.com/blog/masking-sensitive-data-with-amazon-cloudwatch-logs-data-protection-policies](https://awsfundamentals.com/blog/masking-sensitive-data-with-amazon-cloudwatch-logs-data-protection-policies)
- [https://repost.aws/questions/QUermjg18CSMqfSKo4CuTAaA/hide-sensitive-data-in-cloudwatch-logs](https://repost.aws/questions/QUermjg18CSMqfSKo4CuTAaA/hide-sensitive-data-in-cloudwatch-logs)
- [https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html)
- [https://levelup.gitconnected.com/masking-sensitive-data-in-aws-cloudwatch-logs-1b3c66d0ddcb](https://levelup.gitconnected.com/masking-sensitive-data-in-aws-cloudwatch-logs-1b3c66d0ddcb)

## 技術情報

- Source Metadata：[sources/aws/cloudwatch_log_group_no_secrets_in_logs/metadata.json](../../sources/aws/cloudwatch_log_group_no_secrets_in_logs/metadata.json)
- Source Code：[sources/aws/cloudwatch_log_group_no_secrets_in_logs/check.py](../../sources/aws/cloudwatch_log_group_no_secrets_in_logs/check.py)
- Source Metadata Path：`sources/aws/cloudwatch_log_group_no_secrets_in_logs/metadata.json`
- Source Code Path：`sources/aws/cloudwatch_log_group_no_secrets_in_logs/check.py`
