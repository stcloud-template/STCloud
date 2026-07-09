# Ensure 'User consent for applications' is set to 'Do not allow user consent'

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `entra_policy_restricts_user_consent_for_apps` |
| 云平台 | Azure |
| 服务 | entra |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | #microsoft.graph.authorizationPolicy |
| 资源组 | IAM |

## 描述

Require administrators to provide consent for applications before use.

## 风险

If Microsoft Entra ID is running as an identity provider for third-party applications, permissions and consent should be limited to administrators or pre-approved. Malicious applications may attempt to exfiltrate data or abuse privileged user accounts.

## 推荐措施

1. From Azure Home select the Portal Menu 2. Select Microsoft Entra ID 3. Select Enterprise Applications 4. Select Consent and permissions 5. Select User consent settings 6. Set User consent for applications to Do not allow user consent 7. Click save

- 推荐链接：[https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-privileged-access#pa-1-separate-and-limit-highly-privilegedadministrative-users](https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-privileged-access#pa-1-separate-and-limit-highly-privilegedadministrative-users)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/ActiveDirectory/users-can-consent-to-apps-accessing-company-data-on-their-behalf.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/ActiveDirectory/users-can-consent-to-apps-accessing-company-data-on-their-behalf.html#)

## 参考资料

- [https://learn.microsoft.com/en-gb/entra/identity/enterprise-apps/configure-user-consent?pivots=portal](https://learn.microsoft.com/en-gb/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)
- [https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-privileged-access#pa-1-separate-and-limit-highly-privilegedadministrative-users](https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-privileged-access#pa-1-separate-and-limit-highly-privilegedadministrative-users)

## 技术信息

- Source Metadata：[sources/azure/entra_policy_restricts_user_consent_for_apps/metadata.json](../../sources/azure/entra_policy_restricts_user_consent_for_apps/metadata.json)
- Source Code：[sources/azure/entra_policy_restricts_user_consent_for_apps/check.py](../../sources/azure/entra_policy_restricts_user_consent_for_apps/check.py)
- Source Metadata Path：`sources/azure/entra_policy_restricts_user_consent_for_apps/metadata.json`
- Source Code Path：`sources/azure/entra_policy_restricts_user_consent_for_apps/check.py`
