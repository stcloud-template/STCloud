# AWS Organization has only trusted delegated administrators

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `organizations_delegated_administrators` |
| 云平台 | AWS |
| 服务 | organizations |
| 严重等级 | critical |
| 类别 | identity-access |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | Other |
| 资源组 | governance |

## 描述

**AWS Organizations delegated administrators** are compared against a predefined **trusted list** to identify delegations that are not explicitly approved. The evaluation also notes when no delegated administrators exist.

## 风险

Unapproved delegated administrators can alter **SCPs**, invite/move accounts, and create privileged roles, enabling **privilege escalation**. This undermines guardrails, risking loss of **integrity**, exposure of **confidentiality** across accounts, and impacts **availability** through organization-wide policy changes.

## 推荐措施

Restrict delegation to vetted accounts using **least privilege** and **separation of duties**. Maintain a centrally governed **approved allowlist**, review it regularly, and remove unused delegations. Enforce **strong authentication** for admin roles and monitor Organizations policy changes for **defense in depth**.

## 修复步骤


### Other

1. Sign in to the AWS Management Console with the organization management account
2. Open AWS Organizations
3. In the left pane, select **Delegated administrators**
4. Select the untrusted account (by Account ID) from the list
5. For each service shown for that account, choose **Deregister delegated administrator** and confirm
6. Repeat for all untrusted accounts until only trusted accounts (or none) remain

## 参考资料

- [https://docs.aws.amazon.com/organizations/latest/userguide/orgs_delegate_policies.html](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_delegate_policies.html)

## 技术信息

- Source Metadata：[sources/aws/organizations_delegated_administrators/metadata.json](../../sources/aws/organizations_delegated_administrators/metadata.json)
- Source Code：[sources/aws/organizations_delegated_administrators/check.py](../../sources/aws/organizations_delegated_administrators/check.py)
- Source Metadata Path：`sources/aws/organizations_delegated_administrators/metadata.json`
- Source Code Path：`sources/aws/organizations_delegated_administrators/check.py`
