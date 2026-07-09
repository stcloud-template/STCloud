# Ensure IAM policies are attached only to groups or roles

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_policy_attached_only_to_group_or_roles` |
| 云平台 | AWS |
| 服务 | iam |
| 严重等级 | low |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| 资源类型 | AwsIamPolicy |
| 资源组 | IAM |

## 描述

Ensure IAM policies are attached only to groups or roles

## 风险

By default IAM users, groups, and roles have no access to AWS resources. IAM policies are the means by which privileges are granted to users, groups, or roles. It is recommended that IAM policies be applied directly to groups and roles but not users. Assigning privileges at the group or role level reduces the complexity of access management as the number of users grow. Reducing access management complexity may in-turn reduce opportunity for a principal to inadvertently receive or retain excessive privileges.

## 推荐措施

Remove any policy attached directly to the user. Use groups or roles instead.

- 推荐链接：[https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

## 技术信息

- Source Metadata：[sources/aws/iam_policy_attached_only_to_group_or_roles/metadata.json](../../sources/aws/iam_policy_attached_only_to_group_or_roles/metadata.json)
- Source Code：[sources/aws/iam_policy_attached_only_to_group_or_roles/check.py](../../sources/aws/iam_policy_attached_only_to_group_or_roles/check.py)
- Source Metadata Path：`sources/aws/iam_policy_attached_only_to_group_or_roles/metadata.json`
- Source Code Path：`sources/aws/iam_policy_attached_only_to_group_or_roles/check.py`
