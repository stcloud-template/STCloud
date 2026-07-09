# Glue ETL job has continuous CloudWatch logging enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `glue_etl_jobs_logging_enabled` |
| 云平台 | AWS |
| 服务 | glue |
| 严重等级 | medium |
| 类别 | logging |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | Other |
| 资源组 | analytics |

## 描述

**AWS Glue jobs** are assessed for **continuous CloudWatch logging**, confirming that runtime events and outputs are sent to **CloudWatch Logs** via the `--enable-continuous-cloudwatch-log` configuration.

## 风险

Missing job logs hide execution details and access patterns, enabling undetected credential abuse, data exfiltration in scripts, or tampering with transforms. This reduces confidentiality and integrity, hinders incident response, and can mask failures that impact availability.

## 推荐措施

Enable **continuous logging** to **CloudWatch Logs** for all Glue jobs. Centralize logs with retention and KMS encryption, restrict read access, and alert on anomalies and failures. Apply **least privilege** to job roles and use **defense in depth** by correlating logs across services.

## 修复步骤


### CLI

```text
aws glue update-job --job-name <example_resource_name> --job-update '{"DefaultArguments":{"--enable-continuous-cloudwatch-log":"true"}}'
```

### Native IaC

```yaml
Resources:
  GlueJob:
    Type: AWS::Glue::Job
    Properties:
      Role: "<example_resource_id>"
      Command:
        Name: glueetl
        ScriptLocation: "s3://<example_resource_name>/script.py"
      DefaultArguments:
        "--enable-continuous-cloudwatch-log": "true"  # Critical: enables continuous CloudWatch logging to pass the check
```

### Terraform

```hcl
resource "aws_glue_job" "<example_resource_name>" {
  name     = "<example_resource_name>"
  role_arn = "<example_resource_id>"

  command {
    script_location = "s3://<example_resource_name>/script.py"
  }

  default_arguments = {
    "--enable-continuous-cloudwatch-log" = "true" # Critical: enables continuous CloudWatch logging to pass the check
  }
}
```

### Other

1. Open the AWS Glue console and go to Jobs
2. Select the job and click Edit
3. Expand Advanced properties
4. Under Continuous logging, check Enable logs in CloudWatch
5. Save

## 参考资料

- [https://docs.aws.amazon.com/glue/latest/dg/monitor-continuous-logging.html](https://docs.aws.amazon.com/glue/latest/dg/monitor-continuous-logging.html)
- [https://docs.aws.amazon.com/glue/latest/dg/monitor-continuous-logging-enable.html](https://docs.aws.amazon.com/glue/latest/dg/monitor-continuous-logging-enable.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/glue-controls.html#glue-2](https://docs.aws.amazon.com/securityhub/latest/userguide/glue-controls.html#glue-2)

## 技术信息

- Source Metadata：[sources/aws/glue_etl_jobs_logging_enabled/metadata.json](../../sources/aws/glue_etl_jobs_logging_enabled/metadata.json)
- Source Code：[sources/aws/glue_etl_jobs_logging_enabled/check.py](../../sources/aws/glue_etl_jobs_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/glue_etl_jobs_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/glue_etl_jobs_logging_enabled/check.py`
