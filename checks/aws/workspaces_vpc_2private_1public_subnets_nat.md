# Workspace is in a private subnet and its VPC has at least 1 public subnet, 2 private subnets, and a NAT Gateway

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `workspaces_vpc_2private_1public_subnets_nat` |
| クラウドプラットフォーム | AWS |
| サービス | workspaces |
| 重大度 | high |
| カテゴリ | trust-boundaries, internet-exposed |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability |
| リソースタイプ | Other |
| リソースグループ | compute |

## 説明

Amazon WorkSpaces reside in a VPC that includes **2 private subnets** and **1 public subnet**, with the WorkSpace launched in a **private subnet** and the VPC providing **NAT Gateway** egress.

## リスク

Placing WorkSpaces in public subnets or lacking a NAT Gateway exposes desktops to direct Internet reachability, enabling credential attacks and session hijacking, harming **confidentiality** and **integrity**. Without controlled egress, updates and directory connectivity can fail, impacting **availability** and pushing teams to unsafe workarounds.

## 推奨事項

Launch WorkSpaces in **private subnets** and design the VPC with **one public** and **two private subnets**. Provide outbound access via a **NAT Gateway** and restrict inbound exposure per **network segmentation** and **least privilege**. Distribute subnets across AZs and avoid assigning public IPs to WorkSpaces for **defense in depth**.

## 修正手順


### Native IaC

```yaml
# Minimal VPC setup: 1 public subnet, 2 private subnets, and a NAT Gateway
Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16

  IGW:
    Type: AWS::EC2::InternetGateway

  AttachIGW:
    Type: AWS::EC2::VPCGatewayAttachment
    Properties:
      VpcId: !Ref VPC
      InternetGatewayId: !Ref IGW

  PublicSubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: 10.0.0.0/24

  PrivateSubnetA:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: 10.0.1.0/24   # PRIVATE SUBNET 1 (required)

  PrivateSubnetB:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: 10.0.2.0/24   # PRIVATE SUBNET 2 (required)

  NatEip:
    Type: AWS::EC2::EIP
    Properties:
      Domain: vpc

  NatGw:
    Type: AWS::EC2::NatGateway
    Properties:
      AllocationId: !GetAtt NatEip.AllocationId  # CRITICAL: NAT for private subnets' egress
      SubnetId: !Ref PublicSubnet                # CRITICAL: NAT must be in a public subnet

  PublicRt:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPC

  PublicDefaultRoute:
    Type: AWS::EC2::Route
    Properties:
      RouteTableId: !Ref PublicRt
      DestinationCidrBlock: 0.0.0.0/0
      GatewayId: !Ref IGW                       # CRITICAL: makes this a PUBLIC subnet

  AssocPublic:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      SubnetId: !Ref PublicSubnet
      RouteTableId: !Ref PublicRt

  PrivateRt:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPC

  PrivateDefaultRoute:
    Type: AWS::EC2::Route
    Properties:
      RouteTableId: !Ref PrivateRt
      DestinationCidrBlock: 0.0.0.0/0
      NatGatewayId: !Ref NatGw                  # CRITICAL: private subnets use NAT for internet

  AssocPrivateA:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      SubnetId: !Ref PrivateSubnetA
      RouteTableId: !Ref PrivateRt              # CRITICAL: Workspace subnet must associate to private RT

  AssocPrivateB:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      SubnetId: !Ref PrivateSubnetB
      RouteTableId: !Ref PrivateRt              # CRITICAL: Ensures at least 2 private subnets
```

### Terraform

```hcl
# Minimal VPC: 1 public subnet, 2 private subnets, and a NAT Gateway
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id
}

resource "aws_subnet" "public" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.0.0/24"
}

resource "aws_subnet" "private_a" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"  # PRIVATE SUBNET 1 (required)
}

resource "aws_subnet" "private_b" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.2.0/24"  # PRIVATE SUBNET 2 (required)
}

resource "aws_eip" "nat" {
  domain = "vpc"
}

resource "aws_nat_gateway" "nat" {
  allocation_id = aws_eip.nat.id               # CRITICAL: NAT for private subnets' egress
  subnet_id     = aws_subnet.public.id         # CRITICAL: NAT must be in a public subnet
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id
  route {                                      # CRITICAL: makes this a PUBLIC subnet
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }
}

resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}

resource "aws_route_table" "private" {
  vpc_id = aws_vpc.main.id
  route {                                      # CRITICAL: private subnets use NAT for internet
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat.id
  }
}

resource "aws_route_table_association" "private_a" {
  subnet_id      = aws_subnet.private_a.id     # CRITICAL: Workspace subnet must associate to private RT
  route_table_id = aws_route_table.private.id
}

resource "aws_route_table_association" "private_b" {
  subnet_id      = aws_subnet.private_b.id
  route_table_id = aws_route_table.private.id  # CRITICAL: Ensures at least 2 private subnets
}
```

### Other

1. In the AWS Console, go to VPC > Internet gateways and ensure an Internet Gateway is attached to the VPC.
2. Go to VPC > Subnets and ensure the VPC has at least one subnet to use as PUBLIC and two subnets to use as PRIVATE (preferably in different AZs). Create missing subnets if needed.
3. Go to VPC > NAT Gateways and Create NAT gateway in the PUBLIC subnet, allocating an Elastic IP.
4. Go to VPC > Route tables:
   - For the PUBLIC subnet's route table: add or ensure a 0.0.0.0/0 route targets the Internet Gateway (this marks it public).
   - For the PRIVATE subnets' route table(s): add or ensure a 0.0.0.0/0 route targets the NAT Gateway and remove any 0.0.0.0/0 route to an Internet Gateway. This makes them private with egress via NAT.
5. Ensure the WorkSpace's subnet is one of the PRIVATE subnets by associating its subnet to the private route table (Routes: 0.0.0.0/0 -> NAT Gateway).
6. Verify: the VPC now has >=1 public subnet, >=2 private subnets, at least one NAT Gateway, and the WorkSpace's subnet is private.

## 参考資料

- [https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-vpc.html](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-vpc.html)

## 技術情報

- Source Metadata：[sources/aws/workspaces_vpc_2private_1public_subnets_nat/metadata.json](../../sources/aws/workspaces_vpc_2private_1public_subnets_nat/metadata.json)
- Source Code：[sources/aws/workspaces_vpc_2private_1public_subnets_nat/check.py](../../sources/aws/workspaces_vpc_2private_1public_subnets_nat/check.py)
- Source Metadata Path：`sources/aws/workspaces_vpc_2private_1public_subnets_nat/metadata.json`
- Source Code Path：`sources/aws/workspaces_vpc_2private_1public_subnets_nat/check.py`
