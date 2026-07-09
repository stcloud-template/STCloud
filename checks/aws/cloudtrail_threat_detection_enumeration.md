# CloudTrail logs show no potential enumeration activity

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudtrail_threat_detection_enumeration` |
| 云平台 | AWS |
| 服务 | cloudtrail |
| 严重等级 | critical |
| 类别 | threat-detection |
| 检查类型 | TTPs/Discovery, Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis, Unusual Behaviors/User |
| 资源类型 | AwsCloudTrailTrail |
| 资源组 | monitoring |

## 描述

**CloudTrail activity** is analyzed for AWS identities executing a broad mix of discovery APIs like `List*`, `Describe*`, and `Get*` within a recent time window. An identity exceeding a configurable ratio of these actions indicates potential enumeration behavior by that principal.

## 风险

Concentrated discovery activity signals **reconnaissance** with valid credentials. Adversaries can map assets and policies to enable **privilege escalation**, target data stores for **exfiltration** (confidentiality), and identify services to disrupt (availability), supporting stealthy lateral movement.

## 推荐措施

Apply **least privilege** to limit `List*`/`Describe*`/`Get*` to necessary resources and roles; use **separation of duties**. - Enforce MFA and short-lived sessions - Use **SCPs** to curb unnecessary discovery - Baseline expected reads and alert on spikes as **defense in depth**

## 修复步骤


### CLI

```text
aws iam update-access-key --user-name <USER_NAME> --access-key-id <ACCESS_KEY_ID> --status Inactive
```

### Native IaC

```yaml
# CloudFormation: deny common enumeration APIs for a specific IAM user
Resources:
  DenyEnumerationPolicy:
    Type: AWS::IAM::Policy
    Properties:
      PolicyName: deny-enumeration
      PolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Deny  # CRITICAL: blocks typical enumeration calls
            Action:
              - ec2:Describe*   # CRITICAL: deny EC2 describe APIs
              - iam:List*       # CRITICAL: deny IAM list APIs
              - s3:List*        # CRITICAL: deny S3 list APIs
              - s3:Get*         # CRITICAL: deny S3 get APIs (e.g., GetBucketAcl)
            Resource: "*"
      Users:
        - "<example_resource_name>"  # CRITICAL: target the enumerating user
```

### Terraform

```hcl
# Deny common enumeration APIs for a specific IAM user
resource "aws_iam_user_policy" "<example_resource_name>" {
  name = "deny-enumeration"
  user = "<example_user_name>"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect   = "Deny", # CRITICAL: blocks typical enumeration calls
      Action   = [
        "ec2:Describe*",   # CRITICAL
        "iam:List*",       # CRITICAL
        "s3:List*",        # CRITICAL
        "s3:Get*"          # CRITICAL
      ],
      Resource = "*"
    }]
  })
}
```

### Other

1. In AWS Console, go to IAM > Users and open the user shown in the alert (ARN in the finding)
2. Select the Security credentials tab
3. For each active Access key, click Deactivate to set status to Inactive
4. If the activity came from an EC2 instance role: go to EC2 > Instances > select the instance > Security > IAM role > Detach IAM role
5. Re-run the check to confirm no new enumeration events occur

## 参考资料

- [https://medium.com/falconforce/falconfriday-detecting-enumeration-in-aws-0xff25-orangecon-25-edition-4aee83651088](https://medium.com/falconforce/falconfriday-detecting-enumeration-in-aws-0xff25-orangecon-25-edition-4aee83651088)
- [https://www.elastic.co/guide/en/security/8.19/aws-discovery-api-calls-via-cli-from-a-single-resource.html](https://www.elastic.co/guide/en/security/8.19/aws-discovery-api-calls-via-cli-from-a-single-resource.html)
- [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-logging-data-events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-logging-data-events)
- [https://aws.plainenglish.io/aws-cloudtrail-event-cheatsheet-a-detection-engineers-guide-to-critical-api-calls-part-1-04fb1588556f](https://aws.plainenglish.io/aws-cloudtrail-event-cheatsheet-a-detection-engineers-guide-to-critical-api-calls-part-1-04fb1588556f)
- [https://support.icompaas.com/support/solutions/articles/62000233455-ensure-there-are-no-potential-enumeration-threats-in-cloudtrail-](https://support.icompaas.com/support/solutions/articles/62000233455-ensure-there-are-no-potential-enumeration-threats-in-cloudtrail-)

## 技术信息

- Source Metadata：[sources/aws/cloudtrail_threat_detection_enumeration/metadata.json](../../sources/aws/cloudtrail_threat_detection_enumeration/metadata.json)
- Source Code：[sources/aws/cloudtrail_threat_detection_enumeration/check.py](../../sources/aws/cloudtrail_threat_detection_enumeration/check.py)
- Source Metadata Path：`sources/aws/cloudtrail_threat_detection_enumeration/metadata.json`
- Source Code Path：`sources/aws/cloudtrail_threat_detection_enumeration/check.py`
