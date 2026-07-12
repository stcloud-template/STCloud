# Region has AWS Elastic Disaster Recovery (DRS) enabled with at least one recovery job

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `drs_job_exist` |
| クラウドプラットフォーム | AWS |
| サービス | drs |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices |
| リソースタイプ | Other |
| リソースグループ | compute |

## 説明

**AWS Elastic Disaster Recovery** is assessed per Region to verify the service is **initialized** and that at least one **recovery or drill job** exists, demonstrating that failover has been exercised.

## リスク

Without DRS enabled or any prior jobs, workloads are **unprotected and untested**, undermining **availability**. During outages or ransomware, recovery may be delayed or fail, increasing RTO/RPO, causing **data loss** and prolonged downtime.

## 推奨事項

Enable DRS in required Regions and protect critical workloads. Define RTO/RPO and run **regular recovery drills** to validate launch settings and dependencies. Apply **least privilege**, monitor replication health, and document failover procedures to ensure consistent, repeatable recovery.

## 修正手順


### Other

1. In the AWS Console, switch to the target Region
2. Open Elastic Disaster Recovery (DRS)
3. Click "Set default replication settings" (or Settings > Initialize) and choose "Configure and initialize" to enable DRS in this Region
4. Go to "Source servers" > "Add server", copy the install command, run it on one server, and wait until it shows Data replication status = Healthy and Ready for recovery
5. Select that server, choose "Initiate recovery drill" (or "Initiate recovery") and confirm to create a job
6. Verify under "Recovery job history" that the job completes

## 参考資料

- [https://aws.amazon.com/blogs/storage/cross-region-disaster-recovery-using-aws-elastic-disaster-recovery/](https://aws.amazon.com/blogs/storage/cross-region-disaster-recovery-using-aws-elastic-disaster-recovery/)
- [https://docs.aws.amazon.com/drs/latest/userguide/quick-start-guide-gs.html](https://docs.aws.amazon.com/drs/latest/userguide/quick-start-guide-gs.html)
- [https://aws.amazon.com/disaster-recovery/](https://aws.amazon.com/disaster-recovery/)
- [https://docs.aws.amazon.com/drs/latest/userguide/recovery-job.html](https://docs.aws.amazon.com/drs/latest/userguide/recovery-job.html)

## 技術情報

- Source Metadata：[sources/aws/drs_job_exist/metadata.json](../../sources/aws/drs_job_exist/metadata.json)
- Source Code：[sources/aws/drs_job_exist/check.py](../../sources/aws/drs_job_exist/check.py)
- Source Metadata Path：`sources/aws/drs_job_exist/metadata.json`
- Source Code Path：`sources/aws/drs_job_exist/check.py`
