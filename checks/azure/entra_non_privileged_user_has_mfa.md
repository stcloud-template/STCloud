# Ensure that 'Multi-Factor Auth Status' is 'Enabled' for all Non-Privileged Users

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `entra_non_privileged_user_has_mfa` |
| 云平台 | Azure |
| 服务 | entra |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | #microsoft.graph.users |
| 资源组 | IAM |

## 描述

Enable multi-factor authentication for all non-privileged users.

## 风险

Multi-factor authentication requires an individual to present a minimum of two separate forms of authentication before access is granted. Multi-factor authentication provides additional assurance that the individual attempting to gain access is who they claim to be. With multi-factor authentication, an attacker would need to compromise at least two different authentication mechanisms, increasing the difficulty of compromise and thus reducing the risk.

## 推荐措施

Activate one of the available multi-factor authentication methods for users in Microsoft Entra ID.

- 推荐链接：[https://learn.microsoft.com/en-us/entra/identity/authentication/tutorial-enable-azure-mfa](https://learn.microsoft.com/en-us/entra/identity/authentication/tutorial-enable-azure-mfa)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/ActiveDirectory/multi-factor-authentication-for-all-non-privileged-users.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/ActiveDirectory/multi-factor-authentication-for-all-non-privileged-users.html#)

## 参考资料

- [https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mfa-howitworks](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mfa-howitworks)
- [https://learn.microsoft.com/en-us/entra/identity/authentication/tutorial-enable-azure-mfa](https://learn.microsoft.com/en-us/entra/identity/authentication/tutorial-enable-azure-mfa)

## 技术信息

- Source Metadata：[sources/azure/entra_non_privileged_user_has_mfa/metadata.json](../../sources/azure/entra_non_privileged_user_has_mfa/metadata.json)
- Source Code：[sources/azure/entra_non_privileged_user_has_mfa/check.py](../../sources/azure/entra_non_privileged_user_has_mfa/check.py)
- Source Metadata Path：`sources/azure/entra_non_privileged_user_has_mfa/metadata.json`
- Source Code Path：`sources/azure/entra_non_privileged_user_has_mfa/check.py`
