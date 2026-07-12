# VPC endpoint policy allows access only from trusted AWS accounts

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `vpc_endpoint_connections_trust_boundaries` |
| クラウドプラットフォーム | AWS |
| サービス | vpc |
| 重大度 | high |
| カテゴリ | trust-boundaries, identity-access |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Initial Access |
| リソースタイプ | AwsEc2VpcEndpointService |
| リソースグループ | network |

## 説明

**VPC endpoint policies** are assessed for restriction to configured **trusted AWS accounts**. If `Principal` values (including `*`) or account ARNs permit non-trusted principals, or conditions aren't sufficiently restrictive, the endpoint is identified. *Endpoints without editable policies are excluded.*

## リスク

Non-trusted principals using your endpoint can access AWS services as if from your VPC, weakening segmentation. This enables unauthorized reads/writes and data exfiltration from resources tied to the endpoint, harming **confidentiality** and **integrity**, and potentially increasing **costs**.

## 推奨事項

Apply **least privilege**: restrict endpoint policies to your account and an explicit allowlist of **trusted accounts**. Avoid `*` principals unless coupled with strict conditions. Prevent transitive trust across network links, and use resource policies and monitoring as **defense in depth** to limit endpoint use.

## 修正手順


### CLI

```text
aws ec2 modify-vpc-endpoint --vpc-endpoint-id <example_resource_id> --policy-document '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":"*","Action":"*","Resource":"*","Condition":{"StringEquals":{"aws:PrincipalAccount":["<TRUSTED_ACCOUNT_ID_1>","<TRUSTED_ACCOUNT_ID_2>"]}}}]}'
```

### Native IaC

```yaml
# CloudFormation: restrict VPC endpoint access to trusted accounts only
Resources:
  <example_resource_name>:
    Type: AWS::EC2::VPCEndpoint
    Properties:
      VpcId: <example_resource_id>
      ServiceName: com.amazonaws.<region>.<service>
      PolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal: "*"
            Action: "*"
            Resource: "*"
            Condition:                  # CRITICAL: restrict by trusted accounts
              StringEquals:             # CRITICAL: only allow specified accounts
                "aws:PrincipalAccount":   # CRITICAL: limits usage to these accounts
                  - "<TRUSTED_ACCOUNT_ID_1>"
                  - "<TRUSTED_ACCOUNT_ID_2>"
```

### Terraform

```hcl
# Add this to the existing VPC endpoint resource to restrict access
resource "aws_vpc_endpoint" "<example_resource_name>" {
  # ...existing required arguments for the endpoint...

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = "*"
      Action    = "*"
      Resource  = "*"
      Condition = {                       # CRITICAL: restrict by trusted accounts
        StringEquals = {
          "aws:PrincipalAccount" = [      # CRITICAL: only these accounts can use the endpoint
            "<TRUSTED_ACCOUNT_ID_1>",
            "<TRUSTED_ACCOUNT_ID_2>"
          ]
        }
      }
    }]
  })
}
```

### Other

1. Open the AWS Console and go to VPC > Endpoints
2. Select the endpoint and choose Actions > Manage policy
3. Select Custom and paste this minimal policy, replacing with your trusted account IDs:
   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": "*",
         "Action": "*",
         "Resource": "*",
         "Condition": {
           "StringEquals": {
             "aws:PrincipalAccount": [
               "<TRUSTED_ACCOUNT_ID_1>",
               "<TRUSTED_ACCOUNT_ID_2>"
             ]
           }
         }
       }
     ]
   }
   ```
4. Click Save

## 参考資料

- [https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html)

## 技術情報

- Source Metadata：[sources/aws/vpc_endpoint_connections_trust_boundaries/metadata.json](../../sources/aws/vpc_endpoint_connections_trust_boundaries/metadata.json)
- Source Code：[sources/aws/vpc_endpoint_connections_trust_boundaries/check.py](../../sources/aws/vpc_endpoint_connections_trust_boundaries/check.py)
- Source Metadata Path：`sources/aws/vpc_endpoint_connections_trust_boundaries/metadata.json`
- Source Code Path：`sources/aws/vpc_endpoint_connections_trust_boundaries/check.py`
