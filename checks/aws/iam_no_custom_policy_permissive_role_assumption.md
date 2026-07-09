# Ensure that no custom IAM policies exist which allow permissive role assumption (e.g. sts:AssumeRole on *)

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_no_custom_policy_permissive_role_assumption` |
| 云平台 | AWS |
| 服务 | iam |
| 严重等级 | high |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks |
| 资源类型 | AwsIamPolicy |
| 资源组 | IAM |

## 描述

Ensure that no custom IAM policies exist which allow permissive role assumption (e.g. sts:AssumeRole on *)

## 风险

If not restricted unintended access could happen.

## 推荐措施

Use the least privilege principle when granting permissions.

- 推荐链接：[https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_permissions-to-switch.html#roles-usingrole-createpolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_permissions-to-switch.html#roles-usingrole-createpolicy)
- [https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html)

## 技术信息

- Source Metadata：[sources/aws/iam_no_custom_policy_permissive_role_assumption/metadata.json](../../sources/aws/iam_no_custom_policy_permissive_role_assumption/metadata.json)
- Source Code：[sources/aws/iam_no_custom_policy_permissive_role_assumption/check.py](../../sources/aws/iam_no_custom_policy_permissive_role_assumption/check.py)
- Source Metadata Path：`sources/aws/iam_no_custom_policy_permissive_role_assumption/metadata.json`
- Source Code Path：`sources/aws/iam_no_custom_policy_permissive_role_assumption/check.py`
