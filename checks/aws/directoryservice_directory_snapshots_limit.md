# Directory Service directory has adequate remaining manual snapshot quota

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `directoryservice_directory_snapshots_limit` |
| クラウドプラットフォーム | AWS |
| サービス | directoryservice |
| 重大度 | low |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Effects/Resource Consumption |
| リソースタイプ | Other |
| リソースグループ | IAM |

## 説明

**AWS Directory Service** directories with **manual snapshot capacity** fully consumed or nearly exhausted, based on current snapshot count relative to the directory's maximum allowed.

## リスク

With no remaining snapshot capacity, you cannot create new recovery points: - Reduced availability during outages or ransomware - Higher RPO from failed scheduled backups - Greater change risk (schema/OS updates) without a safe rollback

## 推奨事項

Adopt a **snapshot lifecycle policy**: rotate/expire old manual snapshots after verifying restores, and alert on low headroom. Prefer **automated backups** for cadence and retention. Enforce **least privilege** for snapshot creation. Design operations within the *hard per-directory cap* to prevent capacity exhaustion.

## 修正手順


### Other

1. In the AWS Console, go to Directory Service > Directories and open <example_resource_id>
2. Click Snapshots
3. Select older snapshots with Type = Manual and click Delete snapshot, confirm
4. Repeat until the number of manual snapshots is less than (manual limit - 2). For the default limit of 5, keep at most 2 manual snapshots
5. Verify Remaining manual snapshots > 2 on the Snapshots page

## 参考資料

- [https://support.icompaas.com/support/solutions/articles/62000233531--ensure-directory-service-manual-snapshots-limit-reached](https://support.icompaas.com/support/solutions/articles/62000233531--ensure-directory-service-manual-snapshots-limit-reached)
- [https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_limits.html](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_limits.html)

## 技術情報

- Source Metadata：[sources/aws/directoryservice_directory_snapshots_limit/metadata.json](../../sources/aws/directoryservice_directory_snapshots_limit/metadata.json)
- Source Code：[sources/aws/directoryservice_directory_snapshots_limit/check.py](../../sources/aws/directoryservice_directory_snapshots_limit/check.py)
- Source Metadata Path：`sources/aws/directoryservice_directory_snapshots_limit/metadata.json`
- Source Code Path：`sources/aws/directoryservice_directory_snapshots_limit/check.py`
