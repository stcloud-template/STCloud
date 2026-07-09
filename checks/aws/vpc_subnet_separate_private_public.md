# VPC has both public and private subnets

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `vpc_subnet_separate_private_public` |
| 云平台 | AWS |
| 服务 | vpc |
| 严重等级 | medium |
| 类别 | trust-boundaries |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability |
| 资源类型 | AwsEc2Subnet |
| 资源组 | network |

## 描述

**Amazon VPCs** are assessed for network segmentation: at least one **public subnet** (internet-routable) and one **private subnet** (non-internet-routable). It flags VPCs with no subnets, only public subnets, or only private subnets.

## 风险

Missing subnet separation erodes **segmentation**. - Only public: workloads face Internet exposure, enabling scanning, brute force, and lateral movement, threatening **confidentiality** and **integrity**. - Only private: no controlled egress can break patching and dependencies, impacting **availability**. - No subnets: misconfiguration leaves services unreachable.

## 推荐措施

Segment each VPC: put internet-facing endpoints in **public subnets** and internal workloads in **private subnets**. Restrict ingress/egress with tight route tables, NACLs, and security groups, minimizing `0.0.0.0/0`. Apply **least privilege** and **defense in depth**. Provide controlled outbound for private subnets via managed egress and use hardened admin access patterns.

## 修复步骤


### Native IaC

```yaml
# CloudFormation: add one public and one private subnet to a VPC
Resources:
  InternetGateway:
    Type: AWS::EC2::InternetGateway

  VPCGatewayAttachment:
    Type: AWS::EC2::VPCGatewayAttachment
    Properties:
      VpcId: <example_resource_id>
      InternetGatewayId: !Ref InternetGateway

  PublicSubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: <example_resource_id>
      CidrBlock: 10.0.1.0/24  # creates a subnet to be made public via route

  PrivateSubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: <example_resource_id>
      CidrBlock: 10.0.2.0/24  # creates a subnet that remains private (no IGW route)

  PublicRouteTable:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: <example_resource_id>

  PublicDefaultRoute:
    Type: AWS::EC2::Route
    DependsOn: VPCGatewayAttachment
    Properties:
      RouteTableId: !Ref PublicRouteTable
      DestinationCidrBlock: 0.0.0.0/0  # CRITICAL: makes routes to the Internet
      GatewayId: !Ref InternetGateway    # CRITICAL: via Internet Gateway

  PublicAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      SubnetId: !Ref PublicSubnet
      RouteTableId: !Ref PublicRouteTable  # CRITICAL: marks this subnet as public

  PrivateRouteTable:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: <example_resource_id>

  PrivateAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      SubnetId: !Ref PrivateSubnet
      RouteTableId: !Ref PrivateRouteTable  # CRITICAL: no IGW route -> private subnet
```

### Terraform

```hcl
# Terraform: add one public and one private subnet to a VPC
resource "aws_internet_gateway" "<example_resource_name>" {
  vpc_id = "<example_resource_id>"
}

resource "aws_subnet" "public_<example_resource_name>" {
  vpc_id     = "<example_resource_id>"
  cidr_block = "10.0.1.0/24"
}

resource "aws_subnet" "private_<example_resource_name>" {
  vpc_id     = "<example_resource_id>"
  cidr_block = "10.0.2.0/24"
}

resource "aws_route_table" "public_<example_resource_name>" {
  vpc_id = "<example_resource_id>"
  route {                         # CRITICAL: makes subnet public via IGW
    cidr_block = "0.0.0.0/0"      # default route to Internet
    gateway_id = aws_internet_gateway.<example_resource_name>.id
  }
}

resource "aws_route_table_association" "public_assoc_<example_resource_name>" {
  subnet_id      = aws_subnet.public_<example_resource_name>.id
  route_table_id = aws_route_table.public_<example_resource_name>.id  # CRITICAL
}

resource "aws_route_table" "private_<example_resource_name>" {
  vpc_id = "<example_resource_id>"  # CRITICAL: no IGW route keeps subnet private
}

resource "aws_route_table_association" "private_assoc_<example_resource_name>" {
  subnet_id      = aws_subnet.private_<example_resource_name>.id
  route_table_id = aws_route_table.private_<example_resource_name>.id  # CRITICAL
}
```

### Other

1. In the AWS console, go to VPC > Your VPCs and select the failing VPC
2. Attach an Internet Gateway if none exists: Internet Gateways > Create > Attach to the VPC
3. Create two subnets: Subnets > Create subnet
   - Subnet A (public): CIDR e.g., 10.0.1.0/24
   - Subnet B (private): CIDR e.g., 10.0.2.0/24
4. Create a route table for public subnet: Route tables > Create
   - Add route: 0.0.0.0/0 -> Internet Gateway (IGW)
   - Associate this route table to Subnet A (public)
5. Create a route table for private subnet: Route tables > Create
   - Do not add a route to an Internet Gateway
   - Associate this route table to Subnet B (private)
6. Verify the VPC now has at least one subnet with an IGW route (public) and one without (private)

## 参考资料

- [https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario2.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario2.html)

## 技术信息

- Source Metadata：[sources/aws/vpc_subnet_separate_private_public/metadata.json](../../sources/aws/vpc_subnet_separate_private_public/metadata.json)
- Source Code：[sources/aws/vpc_subnet_separate_private_public/check.py](../../sources/aws/vpc_subnet_separate_private_public/check.py)
- Source Metadata Path：`sources/aws/vpc_subnet_separate_private_public/metadata.json`
- Source Code Path：`sources/aws/vpc_subnet_separate_private_public/check.py`
