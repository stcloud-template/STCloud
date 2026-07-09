# Region with EBS snapshots has at least one EBS snapshot lifecycle policy defined

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `dlm_ebs_snapshot_lifecycle_policy_exists` |
| 云平台 | AWS |
| 服务 | dlm |
| 严重等级 | medium |
| 类别 | forensics-ready |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | Other |
| 资源组 | storage |

## 描述

**EBS snapshots** are expected to be governed by **Data Lifecycle Manager (DLM) policies** in each Region where snapshots exist. The evaluation looks for lifecycle policies that automate snapshot creation, retention, and cleanup for those snapshots.

## 风险

Without **automated lifecycle policies**, backups become inconsistent and error-prone, reducing availability and weakening recovery objectives. Missing retention rules cause premature deletion or snapshot sprawl, increasing cost and exposing stale data. Lack of cross-Region/account copies limits resilience to regional outages and malicious deletion.

## 推荐措施

Implement **DLM lifecycle policies** for all volumes that require backup. - Schedule creations to meet RPO/RTO - Define retention to prevent sprawl and enforce least data exposure - Use **least privilege** roles and separation of duties - Copy snapshots to another Region/account for **defense in depth** - Monitor policy health and coverage with tags

## 修复步骤


### CLI

```text
aws dlm create-lifecycle-policy --region <region> --execution-role-arn <execution-role-arn> --description "<description>" --state ENABLED --policy-details '{"PolicyType":"EBS_SNAPSHOT_MANAGEMENT","ResourceTypes":["VOLUME"],"TargetTags":[{"Key":"<tag_key>","Value":"<tag_value>"}],"Schedules":[{"CreateRule":{"Interval":24,"IntervalUnit":"HOURS"},"RetainRule":{"Count":1}}]}'
```

### Native IaC

```yaml
# CloudFormation: minimal EBS snapshot lifecycle policy
Resources:
  <example_resource_name>:
    Type: AWS::DLM::LifecyclePolicy
    Properties:
      Description: "<description>"
      ExecutionRoleArn: "<example_resource_arn>"
      State: ENABLED  # Critical: enables the policy so it is counted by the check
      PolicyDetails:
        PolicyType: EBS_SNAPSHOT_MANAGEMENT  # Critical: creates an EBS snapshot lifecycle policy
        ResourceTypes: [VOLUME]
        TargetTags:
          - Key: "<tag_key>"  # Critical: selects target volumes by tag
            Value: "<tag_value>"
        Schedules:
          - CreateRule:
              Interval: 24
              IntervalUnit: HOURS
            RetainRule:
              Count: 1
```

### Terraform

```hcl
# Terraform: minimal EBS snapshot lifecycle policy
resource "aws_dlm_lifecycle_policy" "<example_resource_name>" {
  description        = "<description>"
  execution_role_arn = "<example_resource_arn>"
  state              = "ENABLED" # Critical: enables the policy so it is counted by the check

  policy_details {
    policy_type    = "EBS_SNAPSHOT_MANAGEMENT" # Critical: creates an EBS snapshot lifecycle policy
    resource_types = ["VOLUME"]
    target_tags = {
      "<tag_key>" = "<tag_value>" # Critical: selects target volumes by tag
    }
    schedule {
      create_rule {
        interval      = 24
        interval_unit = "HOURS"
      }
      retain_rule {
        count = 1
      }
    }
  }
}
```

### Other

1. In the AWS console, switch to the Region that has EBS snapshots
2. Open EC2 > Lifecycle Manager (DLM) > Create lifecycle policy
3. Select EBS snapshot policy; Target resource: Volumes
4. Add Target tags: Key = <tag_key>, Value = <tag_value>
5. Set Schedule: Create every 24 hours; Retain 1 snapshot
6. Ensure State is Enabled and click Create policy

## 参考资料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/DLM/ebs-snapshot-automation.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/DLM/ebs-snapshot-automation.html)
- [https://repost.aws/articles/ARmYgZmA8MRQi89pWd9D7eFw/how-to-create-a-automate-backup-aws-data-lifecycle-management-using-snapshots](https://repost.aws/articles/ARmYgZmA8MRQi89pWd9D7eFw/how-to-create-a-automate-backup-aws-data-lifecycle-management-using-snapshots)
- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html#dlm-elements](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html#dlm-elements)

## 技术信息

- Source Metadata：[sources/aws/dlm_ebs_snapshot_lifecycle_policy_exists/metadata.json](../../sources/aws/dlm_ebs_snapshot_lifecycle_policy_exists/metadata.json)
- Source Code：[sources/aws/dlm_ebs_snapshot_lifecycle_policy_exists/check.py](../../sources/aws/dlm_ebs_snapshot_lifecycle_policy_exists/check.py)
- Source Metadata Path：`sources/aws/dlm_ebs_snapshot_lifecycle_policy_exists/metadata.json`
- Source Code Path：`sources/aws/dlm_ebs_snapshot_lifecycle_policy_exists/check.py`
