# Data Access audit logs are enabled for Cloud Storage

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudstorage_audit_logs_enabled` |
| 云平台 | GCP |
| 服务 | cloudstorage |
| 严重等级 | medium |
| 类别 | logging |
| 资源类型 | cloudresourcemanager.googleapis.com/Project |
| 资源组 | governance |

## 描述

Data Access audit logs (DATA_READ and DATA_WRITE) are enabled for Cloud Storage at the project level. Unlike Admin Activity logs (enabled by default), Data Access logs must be explicitly configured to track read and write operations on Cloud Storage objects.

## 风险

Without Data Access audit logs, you cannot track who accessed or modified objects in your Cloud Storage buckets, making it difficult to detect unauthorized access, data exfiltration, or compliance violations.

## 推荐措施

Enable Data Access audit logs (DATA_READ and DATA_WRITE) for Cloud Storage at the project level to track all read and write operations on storage objects for security monitoring and compliance.

## 修复步骤


### Terraform

```hcl
resource "google_project_iam_audit_config" "storage_audit" {
  project = var.project_id
  service = "storage.googleapis.com"

  audit_log_config {
    log_type = "DATA_READ"
  }

  audit_log_config {
    log_type = "DATA_WRITE"
  }
}
```

### Other

1) Console → IAM & Admin → Audit Logs
2) Find 'Google Cloud Storage' in the list of services
3) Check the boxes for 'Data Read' and 'Data Write'
4) Click 'Save' to apply the configuration

Note: This is a project-level setting that applies to all Cloud Storage buckets in the project.

## 参考资料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudStorage/enable-data-access-audit-logs.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudStorage/enable-data-access-audit-logs.html)
- [https://cloud.google.com/storage/docs/audit-logging](https://cloud.google.com/storage/docs/audit-logging)

## 技术信息

- Source Metadata：[sources/gcp/cloudstorage_audit_logs_enabled/metadata.json](../../sources/gcp/cloudstorage_audit_logs_enabled/metadata.json)
- Source Code：[sources/gcp/cloudstorage_audit_logs_enabled/check.py](../../sources/gcp/cloudstorage_audit_logs_enabled/check.py)
- Source Metadata Path：`sources/gcp/cloudstorage_audit_logs_enabled/metadata.json`
- Source Code Path：`sources/gcp/cloudstorage_audit_logs_enabled/check.py`
