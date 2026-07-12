# No potential privilege escalation activity detected in CloudTrail

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudtrail_threat_detection_privilege_escalation` |
| クラウドプラットフォーム | AWS |
| サービス | cloudtrail |
| 重大度 | critical |
| カテゴリ | threat-detection |
| チェックタイプ | TTPs/Privilege Escalation, Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis |
| リソースタイプ | AwsCloudTrailTrail |
| リソースグループ | monitoring |

## 説明

**CloudTrail** activity is analyzed for **identities** executing high-risk actions linked to **privilege escalation** (e.g., `Attach*Policy`, `PassRole`, `AssumeRole`, `CreateAccessKey`). Identities exceeding a configurable share of such events within a *recent time window* are highlighted for investigation.

## リスク

Escalation patterns can grant elevated entitlements, enabling: - Confidentiality loss via unauthorized data/secret access - Integrity compromise by changing IAM policies/roles - Availability impact by tampering with logging or resources This also facilitates lateral movement and persistence.

## 推奨事項

Apply **least privilege** and **defense in depth**: - Restrict `PassRole`, `Attach*Policy`, `UpdateAssumeRolePolicy`, `CreateAccessKey` - Enforce permission boundaries and SCPs - Require MFA and change approvals - Use multi-Region CloudTrail, immutable retention, and alerting on anomalous sequences

## 修正手順


### Native IaC

```yaml
# CloudFormation: Organization SCP to block common IAM privilege-escalation actions
Resources:
  <example_resource_name>:
    Type: AWS::Organizations::Policy
    Properties:
      Name: deny-iam-privesc
      Type: SERVICE_CONTROL_POLICY
      # Critical: This SCP denies risky IAM actions often used for privilege escalation
      # Explanation: Denying these actions organization-wide prevents future privesc activity detected by CloudTrail
      Content: |
        {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Deny",
              "Action": [
                "iam:AttachUserPolicy",
                "iam:AttachRolePolicy",
                "iam:PutUserPolicy",
                "iam:PutRolePolicy",
                "iam:PutGroupPolicy",
                "iam:AddUserToGroup",
                "iam:CreateAccessKey",
                "iam:CreateLoginProfile",
                "iam:UpdateLoginProfile",
                "iam:UpdateAssumeRolePolicy",
                "iam:CreatePolicyVersion",
                "iam:SetDefaultPolicyVersion",
                "iam:PassRole"
              ],
              "Resource": "*"
            }
          ]
        }
  <example_resource_name>Attachment:
    Type: AWS::Organizations::PolicyAttachment
    Properties:
      # Critical: Attach the SCP so it is enforced
      PolicyId: !Ref <example_resource_name>
      TargetId: <example_resource_id>  # OU, Root, or Account ID
```

### Terraform

```hcl
# SCP to block common IAM privilege-escalation actions
resource "aws_organizations_policy" "<example_resource_name>" {
  name = "deny-iam-privesc"
  type = "SERVICE_CONTROL_POLICY"

  # Critical: Deny risky IAM actions to prevent future privesc
  # Explanation: Blocks escalation techniques commonly seen in CloudTrail
  content = jsonencode({
    Version   = "2012-10-17",
    Statement = [
      {
        Effect   = "Deny",
        Action   = [
          "iam:AttachUserPolicy",
          "iam:AttachRolePolicy",
          "iam:PutUserPolicy",
          "iam:PutRolePolicy",
          "iam:PutGroupPolicy",
          "iam:AddUserToGroup",
          "iam:CreateAccessKey",
          "iam:CreateLoginProfile",
          "iam:UpdateLoginProfile",
          "iam:UpdateAssumeRolePolicy",
          "iam:CreatePolicyVersion",
          "iam:SetDefaultPolicyVersion",
          "iam:PassRole"
        ],
        Resource = "*"
      }
    ]
  })
}

resource "aws_organizations_policy_attachment" "<example_resource_name>_attach" {
  # Critical: Attach the SCP so it takes effect
  policy_id = aws_organizations_policy.<example_resource_name>.id
  target_id = "<example_resource_id>" # OU, Root, or Account ID
}
```

### Other

1. In AWS Console, open IAM and identify the AWS identity shown in the ST Cloud finding (user or role ARN)
2. If it is an IAM user:
   - Go to Security credentials > Access keys, set active keys to Inactive
   - Go to Permissions, detach all managed policies and delete inline policies
   - Go to Groups, remove the user from privileged groups
   - Go to Console password, delete the login profile
3. If it is an IAM role:
   - Go to Permissions, detach managed policies and delete inline policies
   - Go to Trust relationships, remove principals that should not assume the role and save
4. Re-run the scan after the detection window elapses to confirm no further privilege-escalation activity is detected

## 参考資料

- [https://rhinosecuritylabs.com/aws/aws-privilege-escalation-methods-mitigation/](https://rhinosecuritylabs.com/aws/aws-privilege-escalation-methods-mitigation/)
- [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-logging-data-events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-logging-data-events)
- [https://signmycode.com/blog/what-is-privilege-escalation-in-aws-recommendations-to-prevent-it](https://signmycode.com/blog/what-is-privilege-escalation-in-aws-recommendations-to-prevent-it)

## 技術情報

- Source Metadata：[sources/aws/cloudtrail_threat_detection_privilege_escalation/metadata.json](../../sources/aws/cloudtrail_threat_detection_privilege_escalation/metadata.json)
- Source Code：[sources/aws/cloudtrail_threat_detection_privilege_escalation/check.py](../../sources/aws/cloudtrail_threat_detection_privilege_escalation/check.py)
- Source Metadata Path：`sources/aws/cloudtrail_threat_detection_privilege_escalation/metadata.json`
- Source Code Path：`sources/aws/cloudtrail_threat_detection_privilege_escalation/check.py`
