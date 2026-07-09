# Ensure unused User Access Keys are disabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_user_accesskey_unused` |
| 云平台 | AWS |
| 服务 | iam |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks |
| 资源类型 | AwsIamUser |
| 资源组 | IAM |

## 描述

Ensure unused User Access Keys are disabled

## 风险

To increase the security of your AWS account, remove IAM user credentials (that is, passwords and access keys) that are not needed. For example, when users leave your organization or no longer need AWS access.

## 推荐措施

Find the credentials that they were using and ensure that they are no longer operational. Ideally, you delete credentials if they are no longer needed. You can always recreate them at a later date if the need arises. At the very least, you should change the password or deactivate the access keys so that the former users no longer have access.

- 推荐链接：[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_finding-unused.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_finding-unused.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_finding-unused.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_finding-unused.html)

## 技术信息

- Source Metadata：[sources/aws/iam_user_accesskey_unused/metadata.json](../../sources/aws/iam_user_accesskey_unused/metadata.json)
- Source Code：[sources/aws/iam_user_accesskey_unused/check.py](../../sources/aws/iam_user_accesskey_unused/check.py)
- Source Metadata Path：`sources/aws/iam_user_accesskey_unused/metadata.json`
- Source Code Path：`sources/aws/iam_user_accesskey_unused/check.py`
