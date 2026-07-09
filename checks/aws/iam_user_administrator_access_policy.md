# Ensure No IAM Users Have Administrator Access Policy

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_user_administrator_access_policy` |
| 云平台 | AWS |
| 服务 | iam |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | AwsIamUser |
| 资源组 | IAM |

## 描述

This check ensures that no IAM users in your AWS account have the 'AdministratorAccess' policy attached. IAM users with this policy have unrestricted access to all AWS services and resources, which poses a significant security risk if misused.

## 风险

IAM users with administrator-level permissions can perform any action on any resource in your AWS environment. If these permissions are granted to users unnecessarily or to individuals without sufficient knowledge, it can lead to security vulnerabilities, data leaks, data loss, or unexpected charges.

## 推荐措施

Replace the 'AdministratorAccess' policy with more specific permissions that follow the Principle of Least Privilege. Consider implementing IAM roles such as 'IAM Master' and 'IAM Manager' to manage permissions more securely.

- 推荐链接：[https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

## 修复步骤


### CLI

```text
aws iam detach-user-policy --user-name <username> --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/IAM/admin-permissions.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/IAM/admin-permissions.html)

## 参考资料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html)
- [https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

## 技术信息

- Source Metadata：[sources/aws/iam_user_administrator_access_policy/metadata.json](../../sources/aws/iam_user_administrator_access_policy/metadata.json)
- Source Code：[sources/aws/iam_user_administrator_access_policy/check.py](../../sources/aws/iam_user_administrator_access_policy/check.py)
- Source Metadata Path：`sources/aws/iam_user_administrator_access_policy/metadata.json`
- Source Code Path：`sources/aws/iam_user_administrator_access_policy/check.py`
