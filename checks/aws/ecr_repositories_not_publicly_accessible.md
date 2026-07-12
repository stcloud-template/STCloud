# ECR repository is not publicly accessible

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ecr_repositories_not_publicly_accessible` |
| クラウドプラットフォーム | AWS |
| サービス | ecr |
| 重大度 | critical |
| カテゴリ | internet-exposed, container-security |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Initial Access, Effects/Data Exposure |
| リソースタイプ | AwsEcrRepository |
| リソースグループ | container |

## 説明

**Amazon ECR repositories** are evaluated for **public exposure** via repository policies that allow anonymous principals (e.g., `Principal: "*"`) to access the repo, including image listing, pulling, or modification.

## リスク

**Public access to ECR repositories** weakens **confidentiality** and **integrity**. Anyone can pull images, exposing proprietary code or embedded secrets; if pushes are allowed, attackers can poison images, enabling supply-chain compromise. Uncontrolled pulls can raise **egress costs** and leak repository metadata.

## 推奨事項

Apply **least privilege** to repository policies: - Avoid `Principal:"*"` and block anonymous access - Grant minimal actions to specific accounts/roles - Require authenticated pulls/pushes via IAM - Use **private connectivity** (e.g., VPC endpoints) - Add **defense in depth** with image scanning and signing

## 修正手順


### CLI

```text
aws ecr delete-repository-policy --repository-name <example_resource_name>
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::ECR::Repository
    Properties:
      RepositoryPolicyText:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Principal:
              AWS: "arn:aws:iam::<example_resource_id>:root"  # Critical: restricts access to a specific AWS account; removes public (*) access
            Action: "ecr:*"
```

### Terraform

```hcl
resource "aws_ecr_repository_policy" "<example_resource_name>" {
  repository = "<example_resource_name>"
  policy     = jsonencode({
    Version   = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { AWS = "arn:aws:iam::<example_resource_id>:root" } # Critical: restricts access to a specific AWS principal; removes public (*) access
      Action    = "ecr:*"
    }]
  })
}
```

### Other

1. In the AWS Console, go to Amazon ECR > Repositories
2. Select the repository
3. Open the Permissions tab and click Edit
4. Remove any statement with Principal set to "*", or replace it with specific AWS ARN(s) (e.g., arn:aws:iam::<example_resource_id>:root)
5. Save changes

## 参考資料

- [https://docs.aws.amazon.com/AmazonECR/latest/public/security_iam_service-with-iam.html](https://docs.aws.amazon.com/AmazonECR/latest/public/security_iam_service-with-iam.html)

## 技術情報

- Source Metadata：[sources/aws/ecr_repositories_not_publicly_accessible/metadata.json](../../sources/aws/ecr_repositories_not_publicly_accessible/metadata.json)
- Source Code：[sources/aws/ecr_repositories_not_publicly_accessible/check.py](../../sources/aws/ecr_repositories_not_publicly_accessible/check.py)
- Source Metadata Path：`sources/aws/ecr_repositories_not_publicly_accessible/metadata.json`
- Source Code Path：`sources/aws/ecr_repositories_not_publicly_accessible/check.py`
