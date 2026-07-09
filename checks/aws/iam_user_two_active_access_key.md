# Check if IAM users have two active access keys

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_user_two_active_access_key` |
| 云平台 | AWS |
| 服务 | iam |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| 资源类型 | AwsIamUser |
| 资源组 | IAM |

## 描述

Check if IAM users have two active access keys

## 风险

Access Keys could be lost or stolen. It creates a critical risk.

## 推荐措施

Avoid using long lived access keys.

- 推荐链接：[https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAccessKeys.html](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAccessKeys.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAccessKeys.html](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAccessKeys.html)

## 技术信息

- Source Metadata：[sources/aws/iam_user_two_active_access_key/metadata.json](../../sources/aws/iam_user_two_active_access_key/metadata.json)
- Source Code：[sources/aws/iam_user_two_active_access_key/check.py](../../sources/aws/iam_user_two_active_access_key/check.py)
- Source Metadata Path：`sources/aws/iam_user_two_active_access_key/metadata.json`
- Source Code Path：`sources/aws/iam_user_two_active_access_key/check.py`
