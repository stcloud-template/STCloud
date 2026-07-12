# GuardDuty detector is managed by an administrator account or is the administrator with member accounts

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `guardduty_centrally_managed` |
| クラウドプラットフォーム | AWS |
| サービス | guardduty |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | AwsGuardDutyDetector |
| リソースグループ | security |

## 説明

Amazon GuardDuty detectors are under **centralized management** when linked to a delegated administrator account, or when the detector's account serves as the **administrator** with associated member accounts.

## リスク

Lack of central management fragments **visibility** and slows **incident response** across accounts and regions. Adversaries can persist unnoticed, perform **lateral movement**, exfiltrate data, and alter configurations, harming **confidentiality**, **integrity**, and **availability**.

## 推奨事項

Designate a **delegated administrator** (preferably via *AWS Organizations*) and enroll all accounts as **members**. Enable auto-enrollment for new accounts, standardize detector settings across required regions, and route findings to central monitoring. Apply **least privilege** and **separation of duties**.

## 修正手順


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

## 参考資料

- [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_accounts.html](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_accounts.html)

## 技術情報

- Source Metadata：[sources/aws/guardduty_centrally_managed/metadata.json](../../sources/aws/guardduty_centrally_managed/metadata.json)
- Source Code：[sources/aws/guardduty_centrally_managed/check.py](../../sources/aws/guardduty_centrally_managed/check.py)
- Source Metadata Path：`sources/aws/guardduty_centrally_managed/metadata.json`
- Source Code Path：`sources/aws/guardduty_centrally_managed/check.py`
