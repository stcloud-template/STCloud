# Ensure Security Defaults is enabled on Microsoft Entra ID

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `entra_security_defaults_enabled` |
| 云平台 | Azure |
| 服务 | entra |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | #microsoft.graph.identitySecurityDefaultsEnforcementPolicy |
| 资源组 | security |

## 描述

Security defaults in Microsoft Entra ID make it easier to be secure and help protect your organization. Security defaults contain preconfigured security settings for common attacks. Security defaults is available to everyone. The goal is to ensure that all organizations have a basic level of security enabled at no extra cost. You may turn on security defaults in the Azure portal.

## 风险

Security defaults provide secure default settings that we manage on behalf of organizations to keep customers safe until they are ready to manage their own identity security settings. For example, doing the following: - Requiring all users and admins to register for MFA. - Challenging users with MFA - when necessary, based on factors such as location, device, role, and task. - Disabling authentication from legacy authentication clients, which can’t do MFA.

## 推荐措施

1. From Azure Home select the Portal Menu. 2. Browse to Microsoft Entra ID > Properties 3. Select Manage security defaults 4. Set the Enable security defaults to Enabled 5. Select Save

- 推荐链接：[https://techcommunity.microsoft.com/t5/microsoft-entra-blog/introducing-security-defaults/ba-p/1061414](https://techcommunity.microsoft.com/t5/microsoft-entra-blog/introducing-security-defaults/ba-p/1061414)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/ActiveDirectory/security-defaults-enabled.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/ActiveDirectory/security-defaults-enabled.html#)

## 参考资料

- [https://learn.microsoft.com/en-us/entra/fundamentals/security-defaults](https://learn.microsoft.com/en-us/entra/fundamentals/security-defaults)
- [https://techcommunity.microsoft.com/t5/microsoft-entra-blog/introducing-security-defaults/ba-p/1061414](https://techcommunity.microsoft.com/t5/microsoft-entra-blog/introducing-security-defaults/ba-p/1061414)

## 技术信息

- Source Metadata：[sources/azure/entra_security_defaults_enabled/metadata.json](../../sources/azure/entra_security_defaults_enabled/metadata.json)
- Source Code：[sources/azure/entra_security_defaults_enabled/check.py](../../sources/azure/entra_security_defaults_enabled/check.py)
- Source Metadata Path：`sources/azure/entra_security_defaults_enabled/metadata.json`
- Source Code Path：`sources/azure/entra_security_defaults_enabled/check.py`
