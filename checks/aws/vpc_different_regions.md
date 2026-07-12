# VPCs are present in more than one region

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `vpc_different_regions` |
| クラウドプラットフォーム | AWS |
| サービス | vpc |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Effects/Denial of Service |
| リソースタイプ | AwsEc2Vpc |
| リソースグループ | network |

## 説明

Non-default **VPCs** are evaluated across the account to determine whether they exist in **more than one region**. The result reflects if your custom network topology is regionally distributed or concentrated in a single region.

## リスク

Single-region VPC deployment weakens **availability** and **resilience**. A regional outage, service disruption, or network control misconfiguration can cause broad downtime, hinder recovery, and increase the **blast radius** of incidents impacting business continuity.

## 推奨事項

Adopt a **multi-region network design**: - Create VPCs in at least two regions for critical workloads - Replicate routing, security controls, and endpoints consistently - Apply **fault tolerance** and **defense in depth** with data replication and resilient DNS/failover to avoid single-region dependency

## 修正手順


### CLI

```text
aws ec2 create-vpc --region <OTHER_REGION> --cidr-block <CIDR_BLOCK>
```

### Native IaC

```yaml
# Deploy this stack in a second AWS region to pass the check
Resources:
  <example_resource_name>:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16  # Critical: creates a non-default VPC in this region
```

### Terraform

```hcl
provider "aws" {
  alias  = "other"
  region = "<OTHER_REGION>" # Critical: ensures the VPC is created in a second region
}

resource "aws_vpc" "<example_resource_name>" {
  provider   = aws.other
  cidr_block = "10.0.0.0/16" # Critical: creates a non-default VPC in that region
}
```

### Other

1. Open the AWS Console and go to VPC
2. In the Region selector (top right), choose a different region than your existing non-default VPCs
3. Click Create VPC > VPC only
4. Enter an IPv4 CIDR block (e.g., 10.0.0.0/16)
5. Click Create VPC
6. Verify a non-default VPC now exists in this second region

## 参考資料

- [https://docs.aws.amazon.com/vpc/latest/userguide/vpc-example-private-subnets-nat.html](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-example-private-subnets-nat.html)
- [https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario2.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario2.html)

## 技術情報

- Source Metadata：[sources/aws/vpc_different_regions/metadata.json](../../sources/aws/vpc_different_regions/metadata.json)
- Source Code：[sources/aws/vpc_different_regions/check.py](../../sources/aws/vpc_different_regions/check.py)
- Source Metadata Path：`sources/aws/vpc_different_regions/metadata.json`
- Source Code Path：`sources/aws/vpc_different_regions/check.py`
