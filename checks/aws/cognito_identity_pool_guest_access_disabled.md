# Ensure Cognito Identity Pool has guest access disabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cognito_identity_pool_guest_access_disabled` |
| 云平台 | AWS |
| 服务 | cognito |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | Other |
| 资源组 | IAM |

## 描述

Guest access allows unauthenticated users to access your identity pool. This is useful for public websites that allow users to sign in with a social identity provider, but it can also be a security risk. If you don't need guest access, you should disable it.

## 风险

If guest access is enabled, unauthenticated users can access your identity pool. This can be a security risk if you don't need guest access.

## 推荐措施

Gues access should be disabled for Cognito Identity Pool. To disable guest access, follow the steps in the Amazon Cognito documentation.

- 推荐链接：[https://docs.aws.amazon.com/location/latest/developerguide/authenticating-using-cognito.html](https://docs.aws.amazon.com/location/latest/developerguide/authenticating-using-cognito.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/location/latest/developerguide/authenticating-using-cognito.html](https://docs.aws.amazon.com/location/latest/developerguide/authenticating-using-cognito.html)

## 技术信息

- Source Metadata：[sources/aws/cognito_identity_pool_guest_access_disabled/metadata.json](../../sources/aws/cognito_identity_pool_guest_access_disabled/metadata.json)
- Source Code：[sources/aws/cognito_identity_pool_guest_access_disabled/check.py](../../sources/aws/cognito_identity_pool_guest_access_disabled/check.py)
- Source Metadata Path：`sources/aws/cognito_identity_pool_guest_access_disabled/metadata.json`
- Source Code Path：`sources/aws/cognito_identity_pool_guest_access_disabled/check.py`
