# Check if IAM identities (users,groups,roles) have the AWSCloudShellFullAccess policy attached.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_policy_cloudshell_admin_not_attached` |
| 云平台 | AWS |
| 服务 | iam |
| 严重等级 | medium |
| 类别 | trust-boundaries |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/CIS AWS Foundations Benchmark |
| 资源类型 | AwsIamPolicy |
| 资源组 | IAM |

## 描述

This control checks whether an IAM identity (user, role, or group) has the AWS managed policy AWSCloudShellFullAccess attached. The control fails if an IAM identity has the AWSCloudShellFullAccess policy attached.

## 风险

Attaching the AWSCloudShellFullAccess policy to IAM identities grants broad permissions, including internet access and file transfer capabilities, which can lead to security risks such as data exfiltration. The principle of least privilege should be followed to avoid excessive permissions.

## 推荐措施

Detach the AWSCloudShellFullAccess policy from the IAM identity to restrict excessive permissions and adhere to the principle of least privilege.

- 推荐链接：[https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html)

## 修复步骤


### CLI

```text
aws iam detach-user/role/group-policy --user/role/group-name <user/role/group-name> --policy-arn arn:aws:iam::aws:policy/AWSCloudShellFullAccess
```

### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-27](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-27)

## 参考资料

- [https://docs.aws.amazon.com/config/latest/developerguide/iam-policy-blacklisted-check.html](https://docs.aws.amazon.com/config/latest/developerguide/iam-policy-blacklisted-check.html)
- [https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html)

## 技术信息

- Source Metadata：[sources/aws/iam_policy_cloudshell_admin_not_attached/metadata.json](../../sources/aws/iam_policy_cloudshell_admin_not_attached/metadata.json)
- Source Code：[sources/aws/iam_policy_cloudshell_admin_not_attached/check.py](../../sources/aws/iam_policy_cloudshell_admin_not_attached/check.py)
- Source Metadata Path：`sources/aws/iam_policy_cloudshell_admin_not_attached/metadata.json`
- Source Code Path：`sources/aws/iam_policy_cloudshell_admin_not_attached/check.py`
