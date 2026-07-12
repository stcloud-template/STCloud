# VPC flow logs are enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `vpc_flow_logs_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | vpc |
| 重大度 | medium |
| カテゴリ | logging, forensics-ready |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark, Software and Configuration Checks/Industry and Regulatory Standards/PCI-DSS, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls (USA), Software and Configuration Checks/Industry and Regulatory Standards/NIST CSF Controls (USA) |
| リソースタイプ | AwsEc2Vpc |
| リソースグループ | network |

## 説明

**AWS VPCs** have **Flow Logs** configured to capture IP traffic for their network interfaces and deliver records to a logging destination. VPCs lacking an active flow log configuration are highlighted.

## リスク

Without flow logs, network activity is opaque, hindering detection and investigation of malicious traffic. Attackers can probe, exfiltrate, or move laterally unnoticed, impacting **confidentiality** and **integrity**; outages and misconfigurations are harder to diagnose, reducing **availability**.

## 推奨事項

Enable **VPC Flow Logs** for all VPCs to provide baseline telemetry. Prefer capturing at least `REJECT` and, for sensitive networks, `ALL`. Send logs to a centralized, access-controlled destination with retention. Apply **least privilege** to writers/readers and integrate with monitoring for **defense in depth**.

## 修正手順


### CLI

```text
aws ec2 create-flow-logs --resource-type VPC --resource-ids <VPC_ID> --traffic-type ALL --log-destination-type s3 --log-destination arn:aws:s3:::<S3_BUCKET_NAME>
```

### Native IaC

```yaml
# CloudFormation: Enable VPC Flow Logs to S3 for an existing VPC
Resources:
  FlowLog:
    Type: AWS::EC2::FlowLog
    Properties:
      ResourceId: <example_resource_id>         # Critical: target the VPC ID
      ResourceType: VPC                         # Critical: enable flow logs at VPC level
      TrafficType: ALL                          # Critical: log all traffic
      LogDestinationType: s3                    # Critical: send logs to S3 (no IAM role needed)
      LogDestination: arn:aws:s3:::<example_resource_name>  # Critical: S3 bucket ARN
```

### Terraform

```hcl
# Enable VPC Flow Logs to S3 for an existing VPC
resource "aws_flow_log" "vpc" {
  vpc_id               = "<example_resource_id>"                 # Critical: target the VPC to enable flow logs
  traffic_type         = "ALL"                                   # Critical: log all traffic
  log_destination_type = "s3"                                    # Critical: send logs to S3 (no IAM role needed)
  log_destination      = "arn:aws:s3:::<example_resource_name>"  # Critical: S3 bucket ARN
}
```

### Other

1. In the AWS Console, go to VPC > Your VPCs
2. Select the target VPC
3. Open the Flow logs tab and click Create flow log
4. Set Traffic type to All
5. Set Destination to S3 and enter Bucket ARN: arn:aws:s3:::<example_resource_name>
6. Click Create flow log

## 参考資料

- [http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/flow-logs.html](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/flow-logs.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/vpc-flow-logs-enabled.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/vpc-flow-logs-enabled.html)

## 技術情報

- Source Metadata：[sources/aws/vpc_flow_logs_enabled/metadata.json](../../sources/aws/vpc_flow_logs_enabled/metadata.json)
- Source Code：[sources/aws/vpc_flow_logs_enabled/check.py](../../sources/aws/vpc_flow_logs_enabled/check.py)
- Source Metadata Path：`sources/aws/vpc_flow_logs_enabled/metadata.json`
- Source Code Path：`sources/aws/vpc_flow_logs_enabled/check.py`
