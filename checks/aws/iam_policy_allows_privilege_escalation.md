# Ensure no Customer Managed IAM policies allow actions that may lead into Privilege Escalation

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_policy_allows_privilege_escalation` |
| 云平台 | AWS |
| 服务 | iam |
| 严重等级 | high |
| 类别 | privilege-escalation |
| 检查类型 | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| 资源类型 | AwsIamPolicy |
| 资源组 | IAM |

## 描述

Ensure no Customer Managed IAM policies allow actions that may lead into Privilege Escalation

## 风险

Users with some IAM permissions are allowed to elevate their privileges up to administrator rights.

## 推荐措施

Grant usage permission on a per-resource basis and applying least privilege principle.

- 推荐链接：[https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege)

## 技术信息

- Source Metadata：[sources/aws/iam_policy_allows_privilege_escalation/metadata.json](../../sources/aws/iam_policy_allows_privilege_escalation/metadata.json)
- Source Code：[sources/aws/iam_policy_allows_privilege_escalation/check.py](../../sources/aws/iam_policy_allows_privilege_escalation/check.py)
- Source Metadata Path：`sources/aws/iam_policy_allows_privilege_escalation/metadata.json`
- Source Code Path：`sources/aws/iam_policy_allows_privilege_escalation/check.py`
