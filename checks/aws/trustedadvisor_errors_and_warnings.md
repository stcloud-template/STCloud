# Trusted Advisor check has no errors or warnings

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `trustedadvisor_errors_and_warnings` |
| クラウドプラットフォーム | AWS |
| サービス | trustedadvisor |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices |
| リソースタイプ | Other |
| リソースグループ | monitoring |

## 説明

**AWS Trusted Advisor** check statuses are assessed to identify items in `warning` or `error`. The finding reflects the state reported by Trusted Advisor across categories such as **Security**, **Fault Tolerance**, **Service Limits**, and **Cost**, indicating where configurations or quotas require attention.

## リスク

Unaddressed **warnings/errors** can leave misconfigurations that impact CIA: - **Confidentiality**: public access or weak auth exposes data - **Integrity**: overly permissive settings allow unwanted changes - **Availability**: limit exhaustion or poor resilience triggers outages They can also increase unnecessary cost.

## 推奨事項

Adopt a continuous process to remediate Trusted Advisor findings: - Prioritize **`error`** then `warning` - Assign ownership and SLAs - Integrate alerts with workflows - Enforce **least privilege**, segmentation, encryption, MFA, and tested backups - Reassess regularly to confirm fixes and prevent regression

## 修正手順


### Other

1. Sign in to the AWS Console and open Trusted Advisor
2. Go to Checks and filter Status to Warning and Error
3. Open each failing check and click View details/Recommended actions
4. Apply the listed fix to the affected resources
5. Click Refresh on the check and repeat until all checks show OK

## 参考資料

- [https://aws.amazon.com/premiumsupport/technology/trusted-advisor/best-practice-checklist/](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/best-practice-checklist/)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/TrustedAdvisor/checks.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/TrustedAdvisor/checks.html)

## 技術情報

- Source Metadata：[sources/aws/trustedadvisor_errors_and_warnings/metadata.json](../../sources/aws/trustedadvisor_errors_and_warnings/metadata.json)
- Source Code：[sources/aws/trustedadvisor_errors_and_warnings/check.py](../../sources/aws/trustedadvisor_errors_and_warnings/check.py)
- Source Metadata Path：`sources/aws/trustedadvisor_errors_and_warnings/metadata.json`
- Source Code Path：`sources/aws/trustedadvisor_errors_and_warnings/check.py`
