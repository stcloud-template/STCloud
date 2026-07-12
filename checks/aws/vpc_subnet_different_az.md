# VPC has subnets in more than one Availability Zone

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `vpc_subnet_different_az` |
| クラウドプラットフォーム | AWS |
| サービス | vpc |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Effects/Denial of Service |
| リソースタイプ | AwsEc2Subnet |
| リソースグループ | network |

## 説明

**VPCs** are assessed for **subnets spread across multiple Availability Zones**. The finding distinguishes VPCs with subnets confined to a single AZ or with no subnets from those with subnets in `2+` distinct AZs.

## リスク

Single-AZ subnet layouts create a **single point of failure**, leading to **service downtime** during AZ outages, maintenance, or capacity events. Lack of **zonal redundancy** constrains load balancing and egress design, reduces **fault isolation**, and undermines availability and recovery objectives.

## 推奨事項

Distribute subnets across `2+` **Availability Zones** and deploy workloads in separate AZs for **high availability**. Mirror network tiers per AZ, align routing and egress per AZ, and enforce multi-AZ layouts with IaC and policy guardrails. *Regularly test failover* to validate resilience.

## 修正手順


### Native IaC

```yaml
# CloudFormation: create two subnets in different AZs to ensure VPC spans multiple AZs
Resources:
  SubnetA:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: <example_resource_id>
      CidrBlock: 10.0.0.0/24
      AvailabilityZone: <example_az_1>  # Critical: place subnet in AZ1 to start AZ diversity
  SubnetB:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: <example_resource_id>
      CidrBlock: 10.0.1.0/24
      AvailabilityZone: <example_az_2>  # Critical: second AZ ensures VPC has subnets in more than one AZ
```

### Terraform

```hcl
# Create two subnets in different AZs so the VPC spans multiple Availability Zones
resource "aws_subnet" "subnet_a" {
  vpc_id            = "<example_resource_id>"
  cidr_block        = "10.0.0.0/24"
  availability_zone = "<example_az_1>" # Critical: first AZ
}

resource "aws_subnet" "subnet_b" {
  vpc_id            = "<example_resource_id>"
  cidr_block        = "10.0.1.0/24"
  availability_zone = "<example_az_2>" # Critical: second AZ; ensures subnets in more than one AZ
}
```

### Other

1. In the AWS Console, go to VPC > Subnets
2. Click Create subnet
3. Select the target VPC (<example_resource_id>)
4. Add two subnets with non-overlapping CIDRs in different Availability Zones (e.g., <example_az_1> and <example_az_2>)
5. Click Create subnet to save

## 参考資料

- [https://docs.aws.amazon.com/pdfs/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/building-scalable-secure-multi-vpc-network-infrastructure.pdf](https://docs.aws.amazon.com/pdfs/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/building-scalable-secure-multi-vpc-network-infrastructure.pdf)
- [https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html)

## 技術情報

- Source Metadata：[sources/aws/vpc_subnet_different_az/metadata.json](../../sources/aws/vpc_subnet_different_az/metadata.json)
- Source Code：[sources/aws/vpc_subnet_different_az/check.py](../../sources/aws/vpc_subnet_different_az/check.py)
- Source Metadata Path：`sources/aws/vpc_subnet_different_az/metadata.json`
- Source Code Path：`sources/aws/vpc_subnet_different_az/check.py`
