# VPC subnet does not assign public IP addresses by default

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `vpc_subnet_no_public_ip_by_default` |
| クラウドプラットフォーム | AWS |
| サービス | vpc |
| 重大度 | high |
| カテゴリ | internet-exposed |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | AwsEc2Subnet |
| リソースグループ | network |

## 説明

**VPC subnets** where `MapPublicIpOnLaunch` is `true` automatically assign a public IPv4 address to instances at launch. This identifies subnets configured for default public IP assignment.

## リスク

**Internet-exposed instances** become reachable by default, enabling port scans, SSH/RDP brute force, and exploit attempts. Successful access can lead to data exfiltration (**confidentiality**), unauthorized changes (**integrity**), and outages (**availability**) through abuse or DDoS.

## 推奨事項

Disable subnet auto-assign to enforce **least-privilege exposure**. Place workloads in **private subnets**, use controlled egress (NAT or private endpoints), and prefer bastions or SSM for administration. *When public access is necessary*, assign IPs explicitly and restrict with tight security groups and routes for **defense in depth**.

## 修正手順


### CLI

```text
aws ec2 modify-subnet-attribute --subnet-id <SUBNET_ID> --no-map-public-ip-on-launch
```

### Native IaC

```yaml
# CloudFormation: Subnet with public IP auto-assign disabled
Resources:
  ExampleSubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: <example_resource_id>
      CidrBlock: 10.0.1.0/24
      MapPublicIpOnLaunch: false  # Critical: disables automatic public IPv4 assignment on instance launch
```

### Terraform

```hcl
# Subnet with public IP auto-assign disabled
resource "aws_subnet" "example" {
  vpc_id     = "<example_resource_id>"
  cidr_block = "10.0.1.0/24"

  map_public_ip_on_launch = false  # Critical: prevents assigning public IPs by default
}
```

### Other

1. Open the AWS Console and go to VPC
2. Click Subnets and select the target subnet
3. Choose Actions > Edit subnet settings (or Modify auto-assign IP settings)
4. Uncheck Enable auto-assign public IPv4 address
5. Save changes

## 参考資料

- [https://docs.aws.amazon.com/config/latest/developerguide/subnet-auto-assign-public-ip-disabled.html](https://docs.aws.amazon.com/config/latest/developerguide/subnet-auto-assign-public-ip-disabled.html)

## 技術情報

- Source Metadata：[sources/aws/vpc_subnet_no_public_ip_by_default/metadata.json](../../sources/aws/vpc_subnet_no_public_ip_by_default/metadata.json)
- Source Code：[sources/aws/vpc_subnet_no_public_ip_by_default/check.py](../../sources/aws/vpc_subnet_no_public_ip_by_default/check.py)
- Source Metadata Path：`sources/aws/vpc_subnet_no_public_ip_by_default/metadata.json`
- Source Code Path：`sources/aws/vpc_subnet_no_public_ip_by_default/check.py`
