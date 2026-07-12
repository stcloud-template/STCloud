# Directory Service directory has log forwarding to CloudWatch Logs enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `directoryservice_directory_log_forwarding_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | directoryservice |
| 重大度 | medium |
| カテゴリ | logging |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | Other |
| リソースグループ | IAM |

## 説明

**AWS Directory Service directories** are configured to forward domain controller security event logs to **CloudWatch Logs** using log subscriptions. Evaluation identifies directories with or without this forwarding in place.

## リスク

Without forwarding, visibility into AD security events is lost, delaying detection of suspicious authentications, policy changes, or privilege grants. Attackers can escalate and persist unnoticed, risking unauthorized access (confidentiality) and identity/policy manipulation (integrity), while hampering forensics and response.

## 推奨事項

Enable and maintain **log forwarding** to CloudWatch Logs. - Centralize logs in a protected group with strict access and retention - Apply least privilege for delivery roles and readers; prevent tampering (immutability) - Alert on high-risk events and aggregate across Regions/accounts for defense in depth

## 修正手順


### Native IaC

```yaml
# CloudFormation: enable Directory Service log forwarding to CloudWatch Logs
Resources:
  LogGroup:
    Type: AWS::Logs::LogGroup
    Properties:
      LogGroupName: /aws/directoryservice/<example_resource_id>

  LogsResourcePolicy:
    Type: AWS::Logs::ResourcePolicy
    Properties:
      PolicyName: DSLogSubscription
      PolicyDocument: |
        {"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Service":"ds.amazonaws.com"},"Action":["logs:CreateLogStream","logs:PutLogEvents","logs:DescribeLogStreams"],"Resource":"arn:aws:logs:*:*:log-group:/aws/directoryservice/*"}]}

  DirectoryLogSubscription:
    Type: AWS::DirectoryService::LogSubscription
    Properties:
      DirectoryId: <example_resource_id>          # CRITICAL: target Directory Service ID to enable log forwarding
      LogGroupName: /aws/directoryservice/<example_resource_id>  # CRITICAL: CloudWatch Logs destination
```

### Terraform

```hcl
# Enable Directory Service log forwarding to CloudWatch Logs
resource "aws_cloudwatch_log_group" "ds" {
  name = "/aws/directoryservice/<example_resource_id>"
}

resource "aws_cloudwatch_log_resource_policy" "ds" {
  policy_name     = "DSLogSubscription"
  policy_document = jsonencode({
    Version   = "2012-10-17",
    Statement = [{
      Effect    = "Allow",
      Principal = { Service = "ds.amazonaws.com" },
      Action    = ["logs:CreateLogStream", "logs:PutLogEvents", "logs:DescribeLogStreams"],
      Resource  = "arn:aws:logs:*:*:log-group:/aws/directoryservice/*"
    }]
  })
}

resource "aws_directory_service_log_subscription" "enable" {
  directory_id  = "<example_resource_id>"                 # CRITICAL: enables log forwarding for this directory
  log_group_name = aws_cloudwatch_log_group.ds.name        # CRITICAL: CloudWatch Logs destination
}
```

### Other

1. In the AWS Console, go to Directory Service > Directories and open your directory
2. On the Directory details page, select the Networking & security tab
3. In Log forwarding, click Enable
4. Choose Create a new CloudWatch log group (or select an existing one)
5. Click Enable to start forwarding logs

## 参考資料

- [https://docs.amazonaws.cn/en_us/directoryservice/latest/admin-guide/ms_ad_enable_log_forwarding.html](https://docs.amazonaws.cn/en_us/directoryservice/latest/admin-guide/ms_ad_enable_log_forwarding.html)
- [https://docs.aws.amazon.com/directoryservice/latest/admin-guide/incident-response.html](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/incident-response.html)
- [https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_enable_log_forwarding.html](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_enable_log_forwarding.html)
- [https://support.icompaas.com/support/solutions/articles/62000233528--ensure-directory-service-monitoring-with-cloudwatch-logs](https://support.icompaas.com/support/solutions/articles/62000233528--ensure-directory-service-monitoring-with-cloudwatch-logs)

## 技術情報

- Source Metadata：[sources/aws/directoryservice_directory_log_forwarding_enabled/metadata.json](../../sources/aws/directoryservice_directory_log_forwarding_enabled/metadata.json)
- Source Code：[sources/aws/directoryservice_directory_log_forwarding_enabled/check.py](../../sources/aws/directoryservice_directory_log_forwarding_enabled/check.py)
- Source Metadata Path：`sources/aws/directoryservice_directory_log_forwarding_enabled/metadata.json`
- Source Code Path：`sources/aws/directoryservice_directory_log_forwarding_enabled/check.py`
