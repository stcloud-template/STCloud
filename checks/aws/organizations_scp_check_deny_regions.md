# AWS Organization restricts operations to only the configured AWS Regions with SCP policies

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `organizations_scp_check_deny_regions` |
| 云平台 | AWS |
| 服务 | organizations |
| 严重等级 | high |
| 类别 | identity-access |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | Other |
| 资源组 | governance |

## 描述

**AWS Organizations SCPs** limit account actions to approved regions using conditions on `aws:RequestedRegion`. This evaluates whether policies exist and fully restrict access to the configured allowlist, rather than only some regions.

## 风险

Without comprehensive Region limits, users or attackers can deploy resources in ungoverned locations, bypassing monitoring and guardrails. Impacts: - Data outside approved jurisdictions (confidentiality) - Policy gaps and drift (integrity) - IR blind spots and unexpected cost (availability)

## 推荐措施

Enforce Region governance with **SCPs** that allow only approved regions via `aws:RequestedRegion` conditions (deny-by-default). Apply across relevant OUs and accounts, with narrow exceptions for required global services. Review often; align to least privilege, data residency, and continuous monitoring.

## 修复步骤


### Native IaC

```yaml
# CloudFormation: SCP denying requests outside approved regions
Resources:
  <example_resource_name>Policy:
    Type: AWS::Organizations::Policy
    Properties:
      Name: <example_resource_name>
      Type: SERVICE_CONTROL_POLICY
      Content:
        Version: '2012-10-17'
        Statement:
          - Effect: Deny
            Action: "*"
            Resource: "*"
            Condition:
              StringNotEquals:
                aws:RequestedRegion:
                  - <REGION_1>  # Critical: only these regions are allowed; others are denied
                  - <REGION_2>

  <example_resource_name>Attachment:
    Type: AWS::Organizations::PolicyAttachment
    Properties:
      PolicyId: !Ref <example_resource_name>Policy
      TargetId: <example_resource_id>  # Critical: attach SCP to the root/OU/account
```

### Terraform

```hcl
# Terraform: SCP denying requests outside approved regions
resource "aws_organizations_policy" "<example_resource_name>" {
  name = "<example_resource_name>"
  type = "SERVICE_CONTROL_POLICY"
  content = jsonencode({
    Version   = "2012-10-17"
    Statement = [
      {
        Effect   = "Deny"
        Action   = "*"
        Resource = "*"
        Condition = {
          StringNotEquals = {
            "aws:RequestedRegion" = ["<REGION_1>", "<REGION_2>"] # Critical: only these regions are allowed; others are denied
          }
        }
      }
    ]
  })
}

resource "aws_organizations_policy_attachment" "<example_resource_name>" {
  policy_id = aws_organizations_policy.<example_resource_name>.id
  target_id = "<example_resource_id>" # Critical: attach to the root (r-xxxx), OU (ou-xxxx), or account ID
}
```

### Other

1. In the AWS Management Console, go to AWS Organizations
2. In Policies, ensure Service control policies are Enabled (click Enable if needed)
3. Go to Policies > Service control policies > Create policy
4. Paste this JSON as the policy content and save:
   {
     "Version": "2012-10-17",
     "Statement": [{
       "Effect": "Deny",
       "Action": "*",
       "Resource": "*",
       "Condition": {"StringNotEquals": {"aws:RequestedRegion": ["<REGION_1>", "<REGION_2>"]}}
     }]
   }
5. Attach the policy to the organization root (r-xxxx), target OU, or specific account
6. Verify the policy is attached and shows as Applied to the intended target

## 参考资料

- [https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_general.html#example-scp-deny-region](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_general.html#example-scp-deny-region)

## 技术信息

- Source Metadata：[sources/aws/organizations_scp_check_deny_regions/metadata.json](../../sources/aws/organizations_scp_check_deny_regions/metadata.json)
- Source Code：[sources/aws/organizations_scp_check_deny_regions/check.py](../../sources/aws/organizations_scp_check_deny_regions/check.py)
- Source Metadata Path：`sources/aws/organizations_scp_check_deny_regions/metadata.json`
- Source Code Path：`sources/aws/organizations_scp_check_deny_regions/check.py`
