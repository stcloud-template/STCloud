# Directory Service directory has adequate remaining manual snapshot quota

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `directoryservice_directory_snapshots_limit` |
| 云平台 | AWS |
| 服务 | directoryservice |
| 严重等级 | low |
| 类别 | resilience |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Effects/Resource Consumption |
| 资源类型 | Other |
| 资源组 | IAM |

## 描述

**AWS Directory Service** directories with **manual snapshot capacity** fully consumed or nearly exhausted, based on current snapshot count relative to the directory's maximum allowed.

## 风险

With no remaining snapshot capacity, you cannot create new recovery points: - Reduced availability during outages or ransomware - Higher RPO from failed scheduled backups - Greater change risk (schema/OS updates) without a safe rollback

## 推荐措施

Adopt a **snapshot lifecycle policy**: rotate/expire old manual snapshots after verifying restores, and alert on low headroom. Prefer **automated backups** for cadence and retention. Enforce **least privilege** for snapshot creation. Design operations within the *hard per-directory cap* to prevent capacity exhaustion.

## 修复步骤


### Other

1. In the AWS Console, go to Directory Service > Directories and open <example_resource_id>
2. Click Snapshots
3. Select older snapshots with Type = Manual and click Delete snapshot, confirm
4. Repeat until the number of manual snapshots is less than (manual limit - 2). For the default limit of 5, keep at most 2 manual snapshots
5. Verify Remaining manual snapshots > 2 on the Snapshots page

## 参考资料

- [https://support.icompaas.com/support/solutions/articles/62000233531--ensure-directory-service-manual-snapshots-limit-reached](https://support.icompaas.com/support/solutions/articles/62000233531--ensure-directory-service-manual-snapshots-limit-reached)
- [https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_limits.html](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_limits.html)

## 技术信息

- Source Metadata：[sources/aws/directoryservice_directory_snapshots_limit/metadata.json](../../sources/aws/directoryservice_directory_snapshots_limit/metadata.json)
- Source Code：[sources/aws/directoryservice_directory_snapshots_limit/check.py](../../sources/aws/directoryservice_directory_snapshots_limit/check.py)
- Source Metadata Path：`sources/aws/directoryservice_directory_snapshots_limit/metadata.json`
- Source Code Path：`sources/aws/directoryservice_directory_snapshots_limit/check.py`
