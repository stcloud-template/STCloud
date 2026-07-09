# SNS topic is not publicly accessible

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `sns_topics_not_publicly_accessible` |
| 云平台 | AWS |
| 服务 | sns |
| 严重等级 | high |
| 类别 | internet-exposed |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exposure, TTPs/Initial Access |
| 资源类型 | AwsSnsTopic |
| 资源组 | messaging |

## 描述

**SNS topic policies** are analyzed for **public principals** (e.g., `*`). Topics that grant access without restrictive conditions such as `aws:SourceArn`, `aws:SourceAccount`, `aws:PrincipalOrgID`, or `sns:Endpoint` scoping are treated as publicly accessible.

## 风险

**Public SNS topics** allow anyone or unknown accounts to: - **Subscribe** and siphon messages (confidentiality) - **Publish** spoofed payloads that alter workflows (integrity) - **Flood** messages causing outages and costs (availability) They also enable cross-account abuse and bypass expected trust boundaries.

## 推荐措施

Restrict the **topic policy** to specific principals and minimal actions: - Avoid `Principal:*` - Allow only needed actions (e.g., `sns:Publish`) - Add conditions like `aws:SourceArn`, `aws:SourceAccount`, `aws:PrincipalOrgID`, or `sns:Endpoint` Apply **least privilege**, separate duties, and review policies regularly.

## 修复步骤


### CLI

```text
aws sns set-topic-attributes --topic-arn <TOPIC_ARN> --attribute-name Policy --attribute-value '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"AWS":"arn:aws:iam::<ACCOUNT_ID>:root"},"Action":"sns:Publish","Resource":"<TOPIC_ARN>"}]}'
```

### Native IaC

```yaml
# CloudFormation: restrict SNS topic policy to the account (not public)
Resources:
  <example_resource_name>:
    Type: AWS::SNS::TopicPolicy
    Properties:
      Topics:
        - arn:aws:sns:<region>:<account_id>:<example_resource_name>
      PolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Action: sns:Publish
            Resource: arn:aws:sns:<region>:<account_id>:<example_resource_name>
            Principal:
              AWS: arn:aws:iam::<account_id>:root  # Critical: restrict to account root to remove public access
```

### Terraform

```hcl
# Restrict SNS topic policy to the account (not public)
resource "aws_sns_topic_policy" "<example_resource_name>" {
  arn    = "<TOPIC_ARN>"
  policy = jsonencode({
    Version   = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Action    = "sns:Publish"
      Resource  = "<TOPIC_ARN>"
      Principal = { AWS = "arn:aws:iam::<ACCOUNT_ID>:root" } # Critical: restrict principal to the account to remove public access
    }]
  })
}
```

### Other

1. Open the Amazon SNS console and select Topics
2. Choose the topic and go to the Access policy tab
3. Edit the policy and remove any Principal set to "*" (Everyone/Public)
4. Add a statement allowing only your account root: Principal = arn:aws:iam::<ACCOUNT_ID>:root with Action sns:Publish and Resource set to the topic ARN
5. Save changes

## 参考资料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/SNS/topics-everyone-publish.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/SNS/topics-everyone-publish.html)
- [https://docs.aws.amazon.com/config/latest/developerguide/sns-topic-policy.html](https://docs.aws.amazon.com/config/latest/developerguide/sns-topic-policy.html)

## 技术信息

- Source Metadata：[sources/aws/sns_topics_not_publicly_accessible/metadata.json](../../sources/aws/sns_topics_not_publicly_accessible/metadata.json)
- Source Code：[sources/aws/sns_topics_not_publicly_accessible/check.py](../../sources/aws/sns_topics_not_publicly_accessible/check.py)
- Source Metadata Path：`sources/aws/sns_topics_not_publicly_accessible/metadata.json`
- Source Code Path：`sources/aws/sns_topics_not_publicly_accessible/check.py`
