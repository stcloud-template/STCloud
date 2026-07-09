# GuardDuty detector is managed by an administrator account or is the administrator with member accounts

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `guardduty_centrally_managed` |
| 云平台 | AWS |
| 服务 | guardduty |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsGuardDutyDetector |
| 资源组 | security |

## 描述

Amazon GuardDuty detectors are under **centralized management** when linked to a delegated administrator account, or when the detector's account serves as the **administrator** with associated member accounts.

## 风险

Lack of central management fragments **visibility** and slows **incident response** across accounts and regions. Adversaries can persist unnoticed, perform **lateral movement**, exfiltrate data, and alter configurations, harming **confidentiality**, **integrity**, and **availability**.

## 推荐措施

Designate a **delegated administrator** (preferably via *AWS Organizations*) and enroll all accounts as **members**. Enable auto-enrollment for new accounts, standardize detector settings across required regions, and route findings to central monitoring. Apply **least privilege** and **separation of duties**.

## 修复步骤


### CLI

```text
aws guardduty enable-organization-admin-account --admin-account-id <ADMIN_ACCOUNT_ID>
```

### Other

1. Sign in to the AWS Organizations management account
2. Open the AWS Organizations console
3. Go to Services > Amazon GuardDuty
4. Click Register delegated administrator
5. Enter the admin account ID and click Register

## 参考资料

- [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_accounts.html](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_accounts.html)

## 技术信息

- Source Metadata：[sources/aws/guardduty_centrally_managed/metadata.json](../../sources/aws/guardduty_centrally_managed/metadata.json)
- Source Code：[sources/aws/guardduty_centrally_managed/check.py](../../sources/aws/guardduty_centrally_managed/check.py)
- Source Metadata Path：`sources/aws/guardduty_centrally_managed/metadata.json`
- Source Code Path：`sources/aws/guardduty_centrally_managed/check.py`
