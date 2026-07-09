# CloudWatch does not allow cross-account sharing

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudwatch_cross_account_sharing_disabled` |
| 云平台 | AWS |
| 服务 | cloudwatch |
| 严重等级 | medium |
| 类别 | trust-boundaries, identity-access |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exposure |
| 资源类型 | AwsIamRole |
| 资源组 | IAM |

## 描述

**Amazon CloudWatch** cross-account sharing via the `CloudWatch-CrossAccountSharingRole` allows other AWS accounts to view your metrics, dashboards, and alarms. The presence of this role indicates that sharing is active.

## 风险

Granting other accounts visibility into observability data reduces **confidentiality** and enables **reconnaissance**. Adversaries or over-privileged partners can map architectures, profile workloads, and spot alerting gaps, increasing chances of **lateral movement** and **evasion**.

## 推荐措施

Disable **cross-account sharing** unless strictly required. If needed, restrict access to specific trusted accounts, scope read-only permissions to only necessary resources, and use a dedicated monitoring account. Apply **least privilege** and **separation of duties**, and regularly audit role trust and access patterns.

## 修复步骤


### CLI

```text
aws cloudformation delete-stack --stack-name CloudWatch-CrossAccountSharingRole
```

### Other

1. Sign in to the AWS Management Console and open IAM
2. Go to Roles
3. Find and select the role named "CloudWatch-CrossAccountSharingRole"
4. Click Delete and confirm
5. If deletion is blocked because it is managed by CloudFormation: open CloudFormation, select the stack named "CloudWatch-CrossAccountSharingRole", and click Delete

## 参考资料

- [https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.html](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.html)

## 技术信息

- Source Metadata：[sources/aws/cloudwatch_cross_account_sharing_disabled/metadata.json](../../sources/aws/cloudwatch_cross_account_sharing_disabled/metadata.json)
- Source Code：[sources/aws/cloudwatch_cross_account_sharing_disabled/check.py](../../sources/aws/cloudwatch_cross_account_sharing_disabled/check.py)
- Source Metadata Path：`sources/aws/cloudwatch_cross_account_sharing_disabled/metadata.json`
- Source Code Path：`sources/aws/cloudwatch_cross_account_sharing_disabled/check.py`
