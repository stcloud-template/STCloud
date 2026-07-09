# SSM Incidents replication set is ACTIVE and has at least one response plan

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ssmincidents_enabled_with_plans` |
| 云平台 | AWS |
| 服务 | ssmincidents |
| 严重等级 | medium |
| 类别 | resilience |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST CSF Controls (USA) |
| 资源类型 | Other |
| 资源组 | monitoring |

## 描述

**Incident Manager** uses a **replication set** and **response plans**. This evaluates whether a replication set exists and is `ACTIVE`, and that at least one response plan is configured for coordinated incident handling.

## 风险

Without an `ACTIVE` replication set or response plans, incidents lack coordinated engagement and automation, raising MTTR and impacting availability and integrity. Threats include prolonged outages, lateral movement, and data exfiltration from delayed containment and misrouted escalation.

## 推荐措施

Establish an `ACTIVE` **replication set** and create **response plans** that define engagement, escalation, runbooks, severity, and communication. Apply **least privilege** to automation roles, test plans regularly, integrate with monitoring to trigger them, and use **defense in depth** with redundant contacts and Regions.

## 修复步骤


### Native IaC

```yaml
# CloudFormation: create a minimal Incident Manager response plan
Resources:
  ResponsePlan:
    Type: AWS::SSMIncidents::ResponsePlan
    Properties:
      Name: <example_resource_name>  # Critical: ensures at least one response plan exists
      IncidentTemplate:              # Critical: required template for the response plan
        Title: <example_title>       # Critical: required
        Impact: 5                    # Critical: required (1=highest, 5=lowest)
```

### Terraform

```hcl
# Ensure replication set exists and becomes ACTIVE
resource "aws_ssmincidents_replication_set" "example" {
  regions {                      # Critical: creates the replication set so it can be ACTIVE
    region_name = "us-east-1"
  }
}

# Create a minimal response plan
resource "aws_ssmincidents_response_plan" "example" {
  name = "<example_resource_name>"  # Critical: ensures at least one response plan exists

  incident_template {                # Critical: required template for the plan
    title  = "<example_title>"
    impact = 5
  }
}
```

### Other

1. In the AWS Console, go to Systems Manager > Incident Manager
2. Replication sets > Create replication set > add at least one Region > Create; wait until Status is ACTIVE
3. Response plans > Create response plan > set Name, Title, and Impact > Create
4. Verify: Replication set shows ACTIVE and at least one response plan exists

## 参考资料

- [https://docs.aws.amazon.com/incident-manager/latest/userguide/response-plans.html](https://docs.aws.amazon.com/incident-manager/latest/userguide/response-plans.html)

## 技术信息

- Source Metadata：[sources/aws/ssmincidents_enabled_with_plans/metadata.json](../../sources/aws/ssmincidents_enabled_with_plans/metadata.json)
- Source Code：[sources/aws/ssmincidents_enabled_with_plans/check.py](../../sources/aws/ssmincidents_enabled_with_plans/check.py)
- Source Metadata Path：`sources/aws/ssmincidents_enabled_with_plans/metadata.json`
- Source Code Path：`sources/aws/ssmincidents_enabled_with_plans/check.py`
