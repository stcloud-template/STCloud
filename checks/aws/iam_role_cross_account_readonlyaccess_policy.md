# Ensure IAM Roles do not have ReadOnlyAccess access for external AWS accounts

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_role_cross_account_readonlyaccess_policy` |
| 云平台 | AWS |
| 服务 | iam |
| 严重等级 | high |
| 类别 | trust-boundaries |
| 资源类型 | AwsIamRole |
| 资源组 | IAM |

## 描述

Ensure IAM Roles do not have ReadOnlyAccess access for external AWS accounts

## 风险

The AWS-managed ReadOnlyAccess policy is highly potent and exposes the customer to a significant data leakage threat. It should be granted very conservatively. For granting access to 3rd party vendors, consider using alternative managed policies, such as ViewOnlyAccess or SecurityAudit.

## 推荐措施

Remove the AWS-managed ReadOnlyAccess policy from all roles that have a trust policy, including third-party cloud accounts, or remove third-party cloud accounts from the trust policy of all roles that need the ReadOnlyAccess policy.

- 推荐链接：[https://docs.securestate.vmware.com/rule-docs/aws-iam-role-cross-account-readonlyaccess-policy](https://docs.securestate.vmware.com/rule-docs/aws-iam-role-cross-account-readonlyaccess-policy)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#awsmp_readonlyaccess](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#awsmp_readonlyaccess)
- [https://docs.securestate.vmware.com/rule-docs/aws-iam-role-cross-account-readonlyaccess-policy](https://docs.securestate.vmware.com/rule-docs/aws-iam-role-cross-account-readonlyaccess-policy)

## 技术信息

- Source Metadata：[sources/aws/iam_role_cross_account_readonlyaccess_policy/metadata.json](../../sources/aws/iam_role_cross_account_readonlyaccess_policy/metadata.json)
- Source Code：[sources/aws/iam_role_cross_account_readonlyaccess_policy/check.py](../../sources/aws/iam_role_cross_account_readonlyaccess_policy/check.py)
- Source Metadata Path：`sources/aws/iam_role_cross_account_readonlyaccess_policy/metadata.json`
- Source Code Path：`sources/aws/iam_role_cross_account_readonlyaccess_policy/check.py`
