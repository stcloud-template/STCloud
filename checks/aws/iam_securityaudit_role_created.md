# Ensure a Security Audit role has been created to conduct security audits

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_securityaudit_role_created` |
| 云平台 | AWS |
| 服务 | iam |
| 严重等级 | low |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| 资源类型 | AwsIamRole |
| 资源组 | IAM |

## 描述

Ensure a Security Audit role has been created to conduct security audits

## 风险

Creating an IAM role with a security audit policy provides a clear separation of duties between the security team and other teams within the organization. This helps to ensure that security-related activities are performed by authorized individuals with the appropriate expertise and access permissions.

## 推荐措施

Create an IAM role for conduct security audits with AWS.

- 推荐链接：[https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_security-auditor](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_security-auditor)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_security-auditor](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_security-auditor)

## 技术信息

- Source Metadata：[sources/aws/iam_securityaudit_role_created/metadata.json](../../sources/aws/iam_securityaudit_role_created/metadata.json)
- Source Code：[sources/aws/iam_securityaudit_role_created/check.py](../../sources/aws/iam_securityaudit_role_created/check.py)
- Source Metadata Path：`sources/aws/iam_securityaudit_role_created/metadata.json`
- Source Code Path：`sources/aws/iam_securityaudit_role_created/check.py`
