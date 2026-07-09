# AWS Well-Architected Tool workload has no high or medium risks

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `wellarchitected_workload_no_high_or_medium_risks` |
| 云平台 | AWS |
| 服务 | wellarchitected |
| 严重等级 | medium |
| 类别 | resilience |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices |
| 资源类型 | Other |
| 资源组 | governance |

## 描述

**AWS Well-Architected workloads** are assessed for the presence and count of risks labeled `HIGH` or `MEDIUM` across the framework pillars. The result indicates whether any such risks remain recorded for the workload.

## 风险

`HIGH`/`MEDIUM` risks indicate gaps that can drive: - **Confidentiality** loss (public data, excessive access) - **Integrity** issues (weak controls, unmonitored changes) - **Availability** failures (fragile resilience, poor recovery) Adversaries can exploit open endpoints and broad privileges to escalate, exfiltrate, and disrupt.

## 推荐措施

Remediate findings, prioritizing `HIGH` then `MEDIUM`. Enforce **least privilege**, strong **encryption**, and continuous **logging/alerting**; minimize public exposure with **defense in depth**; architect for **resilience** with tested recovery. Embed regular reviews in the SDLC and automate guardrails for consistency.

## 修复步骤


### Other

1. In the AWS Console, open Services > Well-Architected Tool
2. Select the workload to fix
3. Open Improvement plan (or Answer questions) and filter to High and Medium risks
4. For each listed question, open it and change the answer to the AWS recommended best-practice choices until the question's risk shows Low/None, then click Save
5. Repeat until no High or Medium risks remain
6. Go back to the workload overview and confirm High = 0 and Medium = 0

## 参考资料

- [https://aws.amazon.com/architecture/well-architected/](https://aws.amazon.com/architecture/well-architected/)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/WellArchitected/findings.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/WellArchitected/findings.html)

## 技术信息

- Source Metadata：[sources/aws/wellarchitected_workload_no_high_or_medium_risks/metadata.json](../../sources/aws/wellarchitected_workload_no_high_or_medium_risks/metadata.json)
- Source Code：[sources/aws/wellarchitected_workload_no_high_or_medium_risks/check.py](../../sources/aws/wellarchitected_workload_no_high_or_medium_risks/check.py)
- Source Metadata Path：`sources/aws/wellarchitected_workload_no_high_or_medium_risks/metadata.json`
- Source Code Path：`sources/aws/wellarchitected_workload_no_high_or_medium_risks/check.py`
