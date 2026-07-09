# Ensure IAM Roles do not have AdministratorAccess policy attached

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_role_administratoraccess_policy` |
| 云平台 | AWS |
| 服务 | iam |
| 严重等级 | high |
| 类别 | trust-boundaries |
| 资源类型 | AwsIamRole |
| 资源组 | IAM |

## 描述

Ensure IAM Roles do not have AdministratorAccess policy attached

## 风险

The AWS-managed AdministratorAccess policy grants all actions for all AWS services and for all resources in the account and as such exposes the customer to a significant data leakage threat. It should be granted very conservatively. For granting access to 3rd party vendors, consider using alternative managed policies, such as ViewOnlyAccess or SecurityAudit.

## 推荐措施

Apply the principle of least privilege. Instead of AdministratorAccess, assign only the permissions necessary for specific roles and tasks. Create custom IAM policies with minimal permissions based on the principle of least privilege.

- 推荐链接：[https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_administrator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_administrator)
- [https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege)

## 技术信息

- Source Metadata：[sources/aws/iam_role_administratoraccess_policy/metadata.json](../../sources/aws/iam_role_administratoraccess_policy/metadata.json)
- Source Code：[sources/aws/iam_role_administratoraccess_policy/check.py](../../sources/aws/iam_role_administratoraccess_policy/check.py)
- Source Metadata Path：`sources/aws/iam_role_administratoraccess_policy/metadata.json`
- Source Code Path：`sources/aws/iam_role_administratoraccess_policy/check.py`
