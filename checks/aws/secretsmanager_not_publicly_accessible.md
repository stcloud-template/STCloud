# Secrets Manager secret resource policy does not allow public access

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `secretsmanager_not_publicly_accessible` |
| クラウドプラットフォーム | AWS |
| サービス | secretsmanager |
| 重大度 | high |
| カテゴリ | internet-exposed, secrets |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Credential Access, Effects/Data Exposure |
| リソースタイプ | AwsSecretsManagerSecret |
| リソースグループ | security |

## 説明

**AWS Secrets Manager secrets** are evaluated for **public exposure** through resource-based policies that grant broad access, such as `Principal: "*"`, which would allow any principal to perform actions on the secret.

## リスク

**Public access** to a secret enables uncontrolled retrieval of secret values, compromising **confidentiality**. If broad actions are allowed, attackers can modify or delete the secret, impacting **integrity** and **availability**, and use exposed credentials for unauthorized data access and **lateral movement**.

## 推奨事項

Apply **least privilege** to resource policies: - Remove wildcards and limit access to specific principals - Add contextual conditions (e.g., VPC endpoints, source account/ARN) - Enable safeguards that block public policies - Prefer private access paths - Periodically review related identity and KMS policies

## 修正手順


### CLI

```text
aws secretsmanager put-resource-policy --secret-id <secret-id> --resource-policy '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"AWS":"arn:aws:iam::<ACCOUNT_ID>:root"},"Action":"secretsmanager:GetSecretValue","Resource":"*"}]}' --block-public-policy
```

### Native IaC

```yaml
# CloudFormation: attach a non-public resource policy
Resources:
  <example_resource_name>:
    Type: AWS::SecretsManager::ResourcePolicy
    Properties:
      SecretId: "<example_resource_id>"
      BlockPublicPolicy: true  # Critical: prevents policies that allow public access
      ResourcePolicy:          # Critical: principal is restricted, not "*"
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              AWS: arn:aws:iam::<ACCOUNT_ID>:root
            Action: secretsmanager:GetSecretValue
            Resource: "*"
```

### Terraform

```hcl
# Restrict secret policy and block public access
resource "aws_secretsmanager_secret_policy" "<example_resource_name>" {
  secret_arn         = "<example_resource_id>"
  block_public_policy = true  # Critical: blocks public policies
  policy = jsonencode({       # Critical: principal is not "*"
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { AWS = "arn:aws:iam::<ACCOUNT_ID>:root" }
      Action    = "secretsmanager:GetSecretValue"
      Resource  = "*"
    }]
  })
}
```

### Other

1. Open AWS Console > Secrets Manager
2. Select the secret > Overview tab > Resource permissions > Edit permissions
3. Remove any statement with Principal set to "*" (or AWS: "*")
4. Add an allow statement for only your account root principal: arn:aws:iam::<ACCOUNT_ID>:root
5. Enable Block public access (if available) and click Save

## 参考資料

- [https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-policies.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-policies.html)
- [https://docs.aws.amazon.com/secretsmanager/latest/userguide/determine-acccess_examine-iam-policies.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/determine-acccess_examine-iam-policies.html)

## 技術情報

- Source Metadata：[sources/aws/secretsmanager_not_publicly_accessible/metadata.json](../../sources/aws/secretsmanager_not_publicly_accessible/metadata.json)
- Source Code：[sources/aws/secretsmanager_not_publicly_accessible/check.py](../../sources/aws/secretsmanager_not_publicly_accessible/check.py)
- Source Metadata Path：`sources/aws/secretsmanager_not_publicly_accessible/metadata.json`
- Source Code Path：`sources/aws/secretsmanager_not_publicly_accessible/check.py`
