# Ensure that token revocation is enabled for Amazon Cognito User Pools

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cognito_user_pool_client_token_revocation_enabled` |
| 云平台 | AWS |
| 服务 | cognito |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AwsCognitoUserPoolClient |
| 资源组 | IAM |

## 描述

Token revocation is a security feature that allows you to revoke tokens and end sessions for users. When you enable token revocation, Amazon Cognito automatically revokes tokens for users who sign out or are deleted. This helps protect your users' data and prevent unauthorized access to your resources.

## 风险

If token revocation is not enabled, users' tokens will not be revoked when they sign out or are deleted. This can lead to unauthorized access to your resources.

## 推荐措施

To enable token revocation for an Amazon Cognito User Pool, use the Amazon Cognito console or the AWS CLI. For more information, see the Amazon Cognito documentation.

- 推荐链接：[https://docs.aws.amazon.com/cognito/latest/developerguide/token-revocation.html](https://docs.aws.amazon.com/cognito/latest/developerguide/token-revocation.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/cognito/latest/developerguide/token-revocation.html](https://docs.aws.amazon.com/cognito/latest/developerguide/token-revocation.html)

## 技术信息

- Source Metadata：[sources/aws/cognito_user_pool_client_token_revocation_enabled/metadata.json](../../sources/aws/cognito_user_pool_client_token_revocation_enabled/metadata.json)
- Source Code：[sources/aws/cognito_user_pool_client_token_revocation_enabled/check.py](../../sources/aws/cognito_user_pool_client_token_revocation_enabled/check.py)
- Source Metadata Path：`sources/aws/cognito_user_pool_client_token_revocation_enabled/metadata.json`
- Source Code Path：`sources/aws/cognito_user_pool_client_token_revocation_enabled/check.py`
