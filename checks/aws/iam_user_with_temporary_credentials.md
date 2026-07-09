# Ensure users make use of temporary credentials assuming IAM roles

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_user_with_temporary_credentials` |
| 云平台 | AWS |
| 服务 | iam |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Infrastructure Security |
| 资源类型 | AwsIamUser |
| 资源组 | IAM |

## 描述

Ensure users make use of temporary credentials assuming IAM roles

## 风险

As a best practice, use temporary security credentials (IAM roles) instead of creating long-term credentials like access keys, and don't create AWS account root user access keys.

## 推荐措施

As a best practice, use temporary security credentials (IAM roles) instead of creating long-term credentials like access keys, and don't create AWS account root user access keys.

- 推荐链接：[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)

## 技术信息

- Source Metadata：[sources/aws/iam_user_with_temporary_credentials/metadata.json](../../sources/aws/iam_user_with_temporary_credentials/metadata.json)
- Source Code：[sources/aws/iam_user_with_temporary_credentials/check.py](../../sources/aws/iam_user_with_temporary_credentials/check.py)
- Source Metadata Path：`sources/aws/iam_user_with_temporary_credentials/metadata.json`
- Source Code Path：`sources/aws/iam_user_with_temporary_credentials/check.py`
