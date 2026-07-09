# Ensure centralized root credentials management is enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_root_credentials_management_enabled` |
| 云平台 | AWS |
| 服务 | iam |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | Other |
| 资源组 | IAM |

## 描述

Checks if centralized management of root credentials for member accounts in AWS Organizations is enabled. This ensures that root credentials are managed centrally, reducing the risk of unauthorized access or mismanagement.

## 风险

Without centralized root credentials management, member accounts retain full control over their root user credentials, increasing the risk of credential misuse, mismanagement, or compromise.

## 推荐措施

Enable centralized management of root access for member accounts using the CLI or IAM console.

- 推荐链接：[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-enable-root-access.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-enable-root-access.html)

## 修复步骤


### CLI

```text
aws iam enable-organizations-root-credentials-management
```

## 参考资料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#id_root-user-access-management](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#id_root-user-access-management)
- [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-enable-root-access.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-enable-root-access.html)

## 技术信息

- Source Metadata：[sources/aws/iam_root_credentials_management_enabled/metadata.json](../../sources/aws/iam_root_credentials_management_enabled/metadata.json)
- Source Code：[sources/aws/iam_root_credentials_management_enabled/check.py](../../sources/aws/iam_root_credentials_management_enabled/check.py)
- Source Metadata Path：`sources/aws/iam_root_credentials_management_enabled/metadata.json`
- Source Code Path：`sources/aws/iam_root_credentials_management_enabled/check.py`
