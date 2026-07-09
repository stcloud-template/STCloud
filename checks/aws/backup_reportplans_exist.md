# At least one AWS Backup report plan exists

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `backup_reportplans_exist` |
| 云平台 | AWS |
| 服务 | backup |
| 严重等级 | low |
| 类别 | logging |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsBackupBackupPlan |
| 资源组 | storage |

## 描述

**AWS Backup** environments with existing backup plans are assessed for the presence of at least one **report plan** that generates `jobs` or `compliance` reports.

## 风险

Without a report plan, backup failures and missed restores may go unnoticed, harming **availability** and recovery objectives. Gaps in retention, scheduling, or encryption controls can persist unreported, weakening **integrity** and auditability across accounts and Regions, increasing the chance of SLA breaches.

## 推荐措施

Establish and maintain **report plans** to continuously monitor backup activity and policy adherence. - Apply least privilege to report storage - Include relevant accounts and Regions for coverage - Review reports routinely and alert on anomalies - Enforce separation of duties between backup admins and auditors

## 修复步骤


### CLI

```text
aws backup create-report-plan --report-plan-name <REPORT_PLAN_NAME> --report-delivery-channel s3BucketName=<S3_BUCKET_NAME>,formats=CSV --report-setting reportTemplate=BACKUP_JOB_REPORT
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::Backup::ReportPlan
    Properties:
      ReportPlanName: <example_resource_name> # Critical: creates the report plan required to pass the check
      ReportDeliveryChannel:
        S3BucketName: <example_resource_name> # Critical: destination bucket for reports
        Formats:
          - CSV # Critical: valid report file format
      ReportSetting:
        ReportTemplate: BACKUP_JOB_REPORT # Critical: minimal template to enable job reports
```

### Terraform

```hcl
resource "aws_backup_report_plan" "<example_resource_name>" {
  name = "<example_resource_name>" # Critical: creates at least one report plan

  report_delivery_channel {
    s3_bucket_name = "<example_resource_name>" # Critical: destination bucket for reports
    formats        = ["CSV"] # Critical: valid report file format
  }

  report_setting {
    report_template = "BACKUP_JOB_REPORT" # Critical: minimal job report template
  }
}
```

### Other

1. Open the AWS Backup console and go to Reports
2. Click Create report plan
3. Select the Backup jobs (job report) template
4. Enter a Report plan name and choose an S3 bucket
5. Select CSV as the file format
6. Click Create report plan

## 参考资料

- [https://docs.aws.amazon.com/aws-backup/latest/devguide/create-report-plan-console.html](https://docs.aws.amazon.com/aws-backup/latest/devguide/create-report-plan-console.html)

## 技术信息

- Source Metadata：[sources/aws/backup_reportplans_exist/metadata.json](../../sources/aws/backup_reportplans_exist/metadata.json)
- Source Code：[sources/aws/backup_reportplans_exist/check.py](../../sources/aws/backup_reportplans_exist/check.py)
- Source Metadata Path：`sources/aws/backup_reportplans_exist/metadata.json`
- Source Code Path：`sources/aws/backup_reportplans_exist/check.py`
