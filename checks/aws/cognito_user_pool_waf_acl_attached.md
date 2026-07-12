# Ensure that Amazon Cognito User Pool is associated with a WAF Web ACL

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cognito_user_pool_waf_acl_attached` |
| クラウドプラットフォーム | AWS |
| サービス | cognito |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AwsCognitoUserPool |
| リソースグループ | IAM |

## 説明

Web ACLs are used to control access to your content. You can use a Web ACL to control who can access your content. You can also use a Web ACL to block requests based on IP address, HTTP headers, HTTP body, URI, or URI query string parameters. You can associate a Web ACL with a Cognito User Pool to control access to your content.

## リスク

If a Web ACL is not associated with a Cognito User Pool, then the content is not protected by the Web ACL. This could lead to unauthorized access to your content.

## 推奨事項

The Web ACL should be associated with the Cognito User Pool. To associate a Web ACL with a Cognito User Pool, use the AWS Management Console.

- 推奨リンク：[https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-waf.html](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-waf.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-waf.html](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-waf.html)

## 技術情報

- Source Metadata：[sources/aws/cognito_user_pool_waf_acl_attached/metadata.json](../../sources/aws/cognito_user_pool_waf_acl_attached/metadata.json)
- Source Code：[sources/aws/cognito_user_pool_waf_acl_attached/check.py](../../sources/aws/cognito_user_pool_waf_acl_attached/check.py)
- Source Metadata Path：`sources/aws/cognito_user_pool_waf_acl_attached/metadata.json`
- Source Code Path：`sources/aws/cognito_user_pool_waf_acl_attached/check.py`
