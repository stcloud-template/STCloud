# Ensure Any of the ASC Default Policy Settings are Not Set to 'Disabled'

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `policy_ensure_asc_enforcement_enabled` |
| 云平台 | Azure |
| 服务 | policy |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.Authorization/policyAssignments |
| 资源组 | governance |

## 描述

None of the settings offered by ASC Default policy should be set to effect Disabled.

## 风险

A security policy defines the desired configuration of your workloads and helps ensure compliance with company or regulatory security requirements. ASC Default policy is associated with every subscription by default. ASC default policy assignment is a set of security recommendations based on best practices. Enabling recommendations in ASC default policy ensures that Azure security center provides the ability to monitor all of the supported recommendations and optionally allow automated action for a few of the supported recommendations.

## 推荐措施

1. From Azure Home select the Portal Menu 2. Select Policy 3. Select ASC Default for each subscription 4. Click on 'view Assignment' 5. Click on 'Edit assignment' 6. Ensure Policy Enforcement is Enabled 7. Click 'Review + Save'

- 推荐链接：[https://learn.microsoft.com/en-us/azure/defender-for-cloud/implement-security-recommendations](https://learn.microsoft.com/en-us/azure/defender-for-cloud/implement-security-recommendations)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://learn.microsoft.com/en-us/azure/defender-for-cloud/security-policy-concept](https://learn.microsoft.com/en-us/azure/defender-for-cloud/security-policy-concept)
- [https://learn.microsoft.com/en-us/azure/defender-for-cloud/implement-security-recommendations](https://learn.microsoft.com/en-us/azure/defender-for-cloud/implement-security-recommendations)

## 技术信息

- Source Metadata：[sources/azure/policy_ensure_asc_enforcement_enabled/metadata.json](../../sources/azure/policy_ensure_asc_enforcement_enabled/metadata.json)
- Source Code：[sources/azure/policy_ensure_asc_enforcement_enabled/check.py](../../sources/azure/policy_ensure_asc_enforcement_enabled/check.py)
- Source Metadata Path：`sources/azure/policy_ensure_asc_enforcement_enabled/metadata.json`
- Source Code Path：`sources/azure/policy_ensure_asc_enforcement_enabled/check.py`
