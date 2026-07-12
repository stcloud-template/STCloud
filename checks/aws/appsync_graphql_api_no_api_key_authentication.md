# AWS AppSync GraphQL API does not use API key authentication

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `appsync_graphql_api_no_api_key_authentication` |
| クラウドプラットフォーム | AWS |
| サービス | appsync |
| 重大度 | high |
| カテゴリ | identity-access |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, TTPs/Initial Access/Unauthorized Access |
| リソースタイプ | AwsAppSyncGraphQLApi |
| リソースグループ | api_gateway |

## 説明

**AWS AppSync GraphQL APIs** are examined for the default authorization type. The finding indicates an API configured with `API_KEY` instead of IAM, Cognito, OIDC, or Lambda authorizers.

## リスク

Static **API keys** can be leaked or reused, enabling unauthorized queries and mutations. - **Confidentiality**: unrestricted data reads - **Integrity**: unauthorized writes and schema misuse - **Accountability**: no user identity for auditing, difficult revocation and scoping

## 推奨事項

Replace `API_KEY` with stronger modes and apply least privilege: - **AWS_IAM** for service-to-service - **Cognito User Pools** or **OIDC** for end users - **Lambda authorizer** for custom logic *If guest access is unavoidable*, limit to read-only fields, enforce throttling, use short key lifetimes, and apply schema-level authorization.

## 修正手順


### CLI

```text
aws appsync update-graphql-api --api-id <api-id> --name <api-name> --authentication-type AWS_IAM
```

### Native IaC

```yaml
# CloudFormation: set default auth to non-API key
Resources:
  <example_resource_name>:
    Type: AWS::AppSync::GraphQLApi
    Properties:
      Name: <example_resource_name>
      AuthenticationType: AWS_IAM  # Critical: switches default auth away from API_KEY
```

### Terraform

```hcl
# AppSync GraphQL API with non-API key auth
resource "aws_appsync_graphql_api" "<example_resource_name>" {
  name                = "<example_resource_name>"
  authentication_type = "AWS_IAM"  # Critical: avoids API_KEY default auth
}
```

### Other

1. In the AWS Console, go to AppSync > APIs and select your GraphQL API
2. Open Settings (Authorization)
3. Change Default authorization mode to AWS IAM (or Cognito/OIDC/Lambda)
4. Click Save

## 参考資料

- [https://aws.amazon.com/blogs/mobile/graphql-security-appsync-amplify/](https://aws.amazon.com/blogs/mobile/graphql-security-appsync-amplify/)
- [https://docs.aws.amazon.com/appsync/latest/devguide/security-authz.html](https://docs.aws.amazon.com/appsync/latest/devguide/security-authz.html)
- [https://support.icompaas.com/support/solutions/articles/62000233666-ensure-aws-appsync-graphql-apis-should-not-be-authenticated-with-api-keys](https://support.icompaas.com/support/solutions/articles/62000233666-ensure-aws-appsync-graphql-apis-should-not-be-authenticated-with-api-keys)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/appsync-controls.html#appsync-5](https://docs.aws.amazon.com/securityhub/latest/userguide/appsync-controls.html#appsync-5)

## 技術情報

- Source Metadata：[sources/aws/appsync_graphql_api_no_api_key_authentication/metadata.json](../../sources/aws/appsync_graphql_api_no_api_key_authentication/metadata.json)
- Source Code：[sources/aws/appsync_graphql_api_no_api_key_authentication/check.py](../../sources/aws/appsync_graphql_api_no_api_key_authentication/check.py)
- Source Metadata Path：`sources/aws/appsync_graphql_api_no_api_key_authentication/metadata.json`
- Source Code Path：`sources/aws/appsync_graphql_api_no_api_key_authentication/check.py`
