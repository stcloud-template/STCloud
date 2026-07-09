# Ensure that Amazon Cognito User Pool is associated with a WAF Web ACL

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cognito_user_pool_waf_acl_attached` |
| 云平台 | AWS |
| 服务 | cognito |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AwsCognitoUserPool |
| 资源组 | IAM |

## 描述

Web ACLs are used to control access to your content. You can use a Web ACL to control who can access your content. You can also use a Web ACL to block requests based on IP address, HTTP headers, HTTP body, URI, or URI query string parameters. You can associate a Web ACL with a Cognito User Pool to control access to your content.

## 风险

If a Web ACL is not associated with a Cognito User Pool, then the content is not protected by the Web ACL. This could lead to unauthorized access to your content.

## 推荐措施

The Web ACL should be associated with the Cognito User Pool. To associate a Web ACL with a Cognito User Pool, use the AWS Management Console.

- 推荐链接：[https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-waf.html](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-waf.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-waf.html](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-waf.html)

## 技术信息

- Source Metadata：[sources/aws/cognito_user_pool_waf_acl_attached/metadata.json](../../sources/aws/cognito_user_pool_waf_acl_attached/metadata.json)
- Source Code：[sources/aws/cognito_user_pool_waf_acl_attached/check.py](../../sources/aws/cognito_user_pool_waf_acl_attached/check.py)
- Source Metadata Path：`sources/aws/cognito_user_pool_waf_acl_attached/metadata.json`
- Source Code Path：`sources/aws/cognito_user_pool_waf_acl_attached/check.py`
