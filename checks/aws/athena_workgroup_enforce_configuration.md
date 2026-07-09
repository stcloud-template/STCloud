# Athena workgroup enforces workgroup configuration and cannot be overridden by client-side settings

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `athena_workgroup_enforce_configuration` |
| 云平台 | AWS |
| 服务 | athena |
| 严重等级 | medium |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsAthenaWorkGroup |
| 资源组 | analytics |

## 描述

**Athena workgroups** that set `enforce_workgroup_configuration=true` apply the **workgroup's settings** to every query, overriding client-side options for results location, expected bucket owner, encryption, and control of objects written to the results bucket.

## 风险

Without enforcement, clients may disable or change result **encryption**, redirect outputs to unintended or cross-account buckets, and bypass retention controls. This enables data exposure (C), result tampering (I), and weak auditability, complicating incident response.

## 推荐措施

Set `enforce_workgroup_configuration=true` to centralize control. Require **encrypted results** (prefer **SSE-KMS**), restrict output to approved S3 locations with expected bucket owner, and apply **least privilege**. Monitor results access and logs as part of **defense in depth**.

## 修复步骤


### CLI

```text
aws athena update-work-group --work-group <workgroup_name> --configuration-updates EnforceWorkGroupConfiguration=true
```

### Native IaC

```yaml
# CloudFormation: Enable enforcement of workgroup configuration
Resources:
  <example_resource_name>:
    Type: AWS::Athena::WorkGroup
    Properties:
      Name: <example_resource_name>
      WorkGroupConfiguration:
        EnforceWorkGroupConfiguration: true  # Critical: forces workgroup settings to override client-side settings
```

### Terraform

```hcl
# Terraform: Enable enforcement of workgroup configuration
resource "aws_athena_workgroup" "<example_resource_name>" {
  name = "<example_resource_name>"

  configuration {
    enforce_workgroup_configuration = true  # Critical: forces workgroup settings to override client-side settings
  }
}
```

### Other

1. Open the AWS Management Console and go to Amazon Athena
2. Click Workgroups, select the target workgroup
3. Click Edit workgroup
4. Check Override client-side settings (enforce workgroup settings)
5. Click Save

## 参考资料

- [https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html)
- [https://support.icompaas.com/support/solutions/articles/62000233407-ensure-that-workgroup-configuration-is-enforced-so-it-cannot-be-overriden-by-client-side-settings-](https://support.icompaas.com/support/solutions/articles/62000233407-ensure-that-workgroup-configuration-is-enforced-so-it-cannot-be-overriden-by-client-side-settings-)

## 技术信息

- Source Metadata：[sources/aws/athena_workgroup_enforce_configuration/metadata.json](../../sources/aws/athena_workgroup_enforce_configuration/metadata.json)
- Source Code：[sources/aws/athena_workgroup_enforce_configuration/check.py](../../sources/aws/athena_workgroup_enforce_configuration/check.py)
- Source Metadata Path：`sources/aws/athena_workgroup_enforce_configuration/metadata.json`
- Source Code Path：`sources/aws/athena_workgroup_enforce_configuration/check.py`
