# VPC subnet does not assign public IP addresses by default

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `vpc_subnet_no_public_ip_by_default` |
| 云平台 | AWS |
| 服务 | vpc |
| 严重等级 | high |
| 类别 | internet-exposed |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsEc2Subnet |
| 资源组 | network |

## 描述

**VPC subnets** where `MapPublicIpOnLaunch` is `true` automatically assign a public IPv4 address to instances at launch. This identifies subnets configured for default public IP assignment.

## 风险

**Internet-exposed instances** become reachable by default, enabling port scans, SSH/RDP brute force, and exploit attempts. Successful access can lead to data exfiltration (**confidentiality**), unauthorized changes (**integrity**), and outages (**availability**) through abuse or DDoS.

## 推荐措施

Disable subnet auto-assign to enforce **least-privilege exposure**. Place workloads in **private subnets**, use controlled egress (NAT or private endpoints), and prefer bastions or SSM for administration. *When public access is necessary*, assign IPs explicitly and restrict with tight security groups and routes for **defense in depth**.

## 修复步骤


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

## 参考资料

- [https://docs.aws.amazon.com/config/latest/developerguide/subnet-auto-assign-public-ip-disabled.html](https://docs.aws.amazon.com/config/latest/developerguide/subnet-auto-assign-public-ip-disabled.html)

## 技术信息

- Source Metadata：[sources/aws/vpc_subnet_no_public_ip_by_default/metadata.json](../../sources/aws/vpc_subnet_no_public_ip_by_default/metadata.json)
- Source Code：[sources/aws/vpc_subnet_no_public_ip_by_default/check.py](../../sources/aws/vpc_subnet_no_public_ip_by_default/check.py)
- Source Metadata Path：`sources/aws/vpc_subnet_no_public_ip_by_default/metadata.json`
- Source Code Path：`sources/aws/vpc_subnet_no_public_ip_by_default/check.py`
