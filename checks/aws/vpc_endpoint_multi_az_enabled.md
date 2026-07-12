# Amazon VPC interface endpoint has subnets in multiple Availability Zones

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `vpc_endpoint_multi_az_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | vpc |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | AwsEc2VpcEndpointService |
| リソースグループ | network |

## 説明

**VPC interface endpoints** are evaluated for whether their endpoint network interfaces are placed in **multiple subnets**, which implies distribution across different **Availability Zones**. Endpoints present in only one subnet are identified.

## リスク

A **single-subnet endpoint** creates a **single-AZ dependency**. An AZ outage or routing issue can cut access to the service, reducing **availability**. Workloads may revert to **public endpoints**, exposing traffic to the Internet and risking **confidentiality** through interception or tampering.

## 推奨事項

Place interface endpoints in **multiple subnets across distinct AZs** to remove single-AZ reliance. Prefer zone-local routing so clients use the nearest endpoint, and combine with **private DNS** and restrictive **security groups** to limit exposure-supporting **defense in depth** and resilient connectivity.

## 修正手順


### CLI

```text
aws ec2 modify-vpc-endpoint --vpc-endpoint-id <example_resource_id> --add-subnet-ids <example_subnet_id_2>
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::EC2::VPCEndpoint
    Properties:
      VpcEndpointType: Interface
      VpcId: <example_resource_id>
      ServiceName: com.amazonaws.<region>.<service>
      SubnetIds:  # CRITICAL: include at least two subnets (preferably in different AZs) to pass the check
        - <example_subnet_id_1>
        - <example_subnet_id_2>
```

### Terraform

```hcl
resource "aws_vpc_endpoint" "<example_resource_name>" {
  vpc_id            = "<example_resource_id>"
  service_name      = "com.amazonaws.<region>.<service>"
  vpc_endpoint_type = "Interface"

  subnet_ids = [
    "<example_subnet_id_1>",
    "<example_subnet_id_2>"  # CRITICAL: add a second subnet (ideally in a different AZ) to satisfy multi-AZ
  ]
}
```

### Other

1. Open the AWS VPC console and go to Endpoints
2. Select the interface endpoint
3. Click Actions > Manage subnets
4. Select an additional subnet in a different Availability Zone
5. Click Modify subnets to save

## 参考資料

- [https://docs.aws.amazon.com/vpc/latest/privatelink/interface-endpoints.html](https://docs.aws.amazon.com/vpc/latest/privatelink/interface-endpoints.html)
- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/interface-vpc-endpoints.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/interface-vpc-endpoints.html)

## 技術情報

- Source Metadata：[sources/aws/vpc_endpoint_multi_az_enabled/metadata.json](../../sources/aws/vpc_endpoint_multi_az_enabled/metadata.json)
- Source Code：[sources/aws/vpc_endpoint_multi_az_enabled/check.py](../../sources/aws/vpc_endpoint_multi_az_enabled/check.py)
- Source Metadata Path：`sources/aws/vpc_endpoint_multi_az_enabled/metadata.json`
- Source Code Path：`sources/aws/vpc_endpoint_multi_az_enabled/check.py`
