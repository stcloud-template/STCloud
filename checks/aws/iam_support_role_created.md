# Ensure a support role has been created to manage incidents with AWS Support

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_support_role_created` |
| 云平台 | AWS |
| 服务 | iam |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| 资源类型 | AwsIamRole |
| 资源组 | IAM |

## 描述

Ensure a support role has been created to manage incidents with AWS Support

## 风险

AWS provides a support center that can be used for incident notification and response, as well as technical support and customer services. Create an IAM Role to allow authorized users to manage incidents with AWS Support.

## 推荐措施

Create an IAM role for managing incidents with AWS.

- 推荐链接：[https://docs.aws.amazon.com/awssupport/latest/user/using-service-linked-roles-sup.html](https://docs.aws.amazon.com/awssupport/latest/user/using-service-linked-roles-sup.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/awssupport/latest/user/using-service-linked-roles-sup.html](https://docs.aws.amazon.com/awssupport/latest/user/using-service-linked-roles-sup.html)

## 技术信息

- Source Metadata：[sources/aws/iam_support_role_created/metadata.json](../../sources/aws/iam_support_role_created/metadata.json)
- Source Code：[sources/aws/iam_support_role_created/check.py](../../sources/aws/iam_support_role_created/check.py)
- Source Metadata Path：`sources/aws/iam_support_role_created/metadata.json`
- Source Code Path：`sources/aws/iam_support_role_created/check.py`
