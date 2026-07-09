# VPC has an Amazon EC2 VPC endpoint

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `vpc_endpoint_for_ec2_enabled` |
| 云平台 | AWS |
| 服务 | vpc |
| 严重等级 | medium |
| 类别 | internet-exposed, trust-boundaries |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability |
| 资源类型 | AwsEc2VpcEndpointService |
| 资源组 | network |

## 描述

**Amazon VPCs** are evaluated for an **interface VPC endpoint** to the **Amazon EC2 API** (`ec2`). Its presence indicates private EC2 API connectivity over **AWS PrivateLink** within the VPC.

## 风险

Without a private EC2 endpoint, EC2 API traffic exits via IGW/NAT. This expands exposure to network path threats (e.g., DNS hijack, MITM) and weakens egress isolation. It also adds an internet egress dependency for API access, reducing availability if NAT/edge paths fail.

## 推荐措施

Use an **interface VPC endpoint** for the EC2 service in each VPC that requires EC2 API access. - Enable **private DNS** to keep calls on the AWS network - Apply restrictive endpoint policies (least privilege) - Reduce reliance on public egress and layer controls for **defense in depth**

## 修复步骤


### CLI

```text
aws ec2 create-vpc-endpoint --vpc-id <VPC_ID> --service-name com.amazonaws.<REGION>.ec2 --vpc-endpoint-type Interface --subnet-ids <SUBNET_ID>
```

### Native IaC

```yaml
# CloudFormation: create an EC2 interface VPC endpoint in the VPC
Resources:
  VPCEndpoint:
    Type: AWS::EC2::VPCEndpoint
    Properties:
      VpcId: "<example_resource_id>"                 # CRITICAL: target VPC for the endpoint
      ServiceName: !Sub "com.amazonaws.${AWS::Region}.ec2"  # CRITICAL: EC2 interface endpoint service
      VpcEndpointType: Interface                      # CRITICAL: create an interface endpoint
      SubnetIds:                                      # CRITICAL: subnets to place the endpoint ENIs
        - "<example_resource_id>"
```

### Terraform

```hcl
# Create an EC2 interface VPC endpoint
resource "aws_vpc_endpoint" "<example_resource_name>" {
  vpc_id            = "<example_resource_id>"           # CRITICAL: target VPC
  service_name      = "com.amazonaws.<region>.ec2"      # CRITICAL: EC2 interface endpoint service
  vpc_endpoint_type = "Interface"                       # CRITICAL: interface endpoint
  subnet_ids        = ["<example_resource_id>"]         # CRITICAL: subnet(s) for endpoint ENIs
}
```

### Other

1. In the AWS console, go to VPC > Endpoints
2. Click Create endpoint
3. For Service category, choose AWS services and select Service name com.amazonaws.<region>.ec2
4. Select your VPC and at least one subnet
5. Click Create endpoint

## 参考资料

- [https://docs.aws.amazon.com/config/latest/developerguide/service-vpc-endpoint-enabled.html](https://docs.aws.amazon.com/config/latest/developerguide/service-vpc-endpoint-enabled.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-10](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-10)
- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/interface-vpc-endpoints.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/interface-vpc-endpoints.html)

## 技术信息

- Source Metadata：[sources/aws/vpc_endpoint_for_ec2_enabled/metadata.json](../../sources/aws/vpc_endpoint_for_ec2_enabled/metadata.json)
- Source Code：[sources/aws/vpc_endpoint_for_ec2_enabled/check.py](../../sources/aws/vpc_endpoint_for_ec2_enabled/check.py)
- Source Metadata Path：`sources/aws/vpc_endpoint_for_ec2_enabled/metadata.json`
- Source Code Path：`sources/aws/vpc_endpoint_for_ec2_enabled/check.py`
