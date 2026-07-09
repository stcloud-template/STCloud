# GuardDuty detector has no high severity findings

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `guardduty_no_high_severity_findings` |
| 云平台 | AWS |
| 服务 | guardduty |
| 严重等级 | high |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis, TTPs, Unusual Behaviors |
| 资源类型 | AwsGuardDutyDetector |
| 资源组 | security |

## 描述

**GuardDuty detectors** are evaluated for the presence of **High-severity findings**. This surfaces whether any detector currently has findings labeled `High` by GuardDuty.

## 风险

Unresolved **High findings** often signal active compromise, enabling: - Data exfiltration and unauthorized access (confidentiality) - Privilege escalation and tampering (integrity) - Disruption via malware/crypto-mining (availability) Attackers can pivot laterally and persist if not contained.

## 推荐措施

Treat **High findings** as incidents. - Prioritize triage and containment; isolate affected resources, rotate secrets - Automate alerting and response with playbooks; integrate into IR - Enforce **least privilege**, network segmentation, and hardened baselines - Continuously tune detections and remove unused access to prevent recurrence

## 修复步骤


### Other

1. Sign in to the AWS console and open Amazon GuardDuty
2. Use the Region selector to choose a Region where GuardDuty is enabled
3. Go to Findings and filter: Severity = High (7-8.9), Archived status = Not archived
4. Select all results, click Actions > Archive
5. Repeat steps 2-4 for every Region with GuardDuty enabled
6. Confirm there are 0 active High severity findings in each Region

## 参考资料

- [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings.html](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings.html)
- [https://docs.aws.amazon.com/prescriptive-guidance/latest/vulnerability-management/assess-and-prioritize-security-findings.html](https://docs.aws.amazon.com/prescriptive-guidance/latest/vulnerability-management/assess-and-prioritize-security-findings.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/GuardDuty/findings.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/GuardDuty/findings.html)

## 技术信息

- Source Metadata：[sources/aws/guardduty_no_high_severity_findings/metadata.json](../../sources/aws/guardduty_no_high_severity_findings/metadata.json)
- Source Code：[sources/aws/guardduty_no_high_severity_findings/check.py](../../sources/aws/guardduty_no_high_severity_findings/check.py)
- Source Metadata Path：`sources/aws/guardduty_no_high_severity_findings/metadata.json`
- Source Code Path：`sources/aws/guardduty_no_high_severity_findings/check.py`
