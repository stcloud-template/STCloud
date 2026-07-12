# Application Load Balancer is not publicly accessible (no inbound TCP from 0.0.0.0/0 or ::/0)

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `elbv2_internet_facing` |
| クラウドプラットフォーム | AWS |
| サービス | elbv2 |
| 重大度 | medium |
| カテゴリ | internet-exposed |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark, TTPs/Initial Access |
| リソースタイプ | AwsElbv2LoadBalancer |
| リソースグループ | network |

## 説明

**ELBv2 Application Load Balancers** configured as `internet-facing` are assessed for exposure by reviewing attached **security groups**. Inbound TCP rules that allow `0.0.0.0/0` or `::/0` indicate unrestricted internet reachability.

## リスク

**Unrestricted ALB access** lets any client reach exposed endpoints, enabling **credential stuffing**, automated scanning, and **web exploits**. Impacts: - Confidentiality: data exfiltration - Integrity: unauthorized changes - Availability: increased attack surface and **DoS** potential

## 推奨事項

Enforce **least privilege** on security groups: avoid `0.0.0.0/0`; allow only trusted CIDRs or upstream services. Use an `internal` load balancer for non-public apps. For public endpoints, layer **WAF** rules, strict TLS, and rate limiting; consider **CloudFront/Shield** for defense in depth and reduced direct exposure.

## 修正手順


### Native IaC

```yaml
# CloudFormation Security Group for ALB with no public (0.0.0.0/0 or ::/0) TCP ingress
Resources:
  <example_resource_name>:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: ALB SG restricted ingress
      VpcId: "<example_resource_id>"
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 80
          ToPort: 80
          CidrIp: 10.0.0.0/8  # Critical: restricts inbound to private CIDR, preventing public access
```

### Terraform

```hcl
# Security Group for ALB with no public (0.0.0.0/0 or ::/0) TCP ingress
resource "aws_security_group" "<example_resource_name>" {
  name   = "alb-restricted-sg"
  vpc_id = "<example_resource_id>"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/8"] # Critical: restricts inbound to private CIDR, preventing public access
  }
}
```

### Other

1. In AWS Console, go to EC2 > Load Balancers and select the ALB
2. In the Description tab, note the attached Security Group and open it
3. Click Edit inbound rules
4. Delete any TCP rule with Source 0.0.0.0/0 or ::/0
5. If access is needed, add only specific private CIDRs or trusted security groups
6. Click Save rules

## 参考資料

- [https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-associating-aws-resource.html](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-associating-aws-resource.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/internet-facing-load-balancers.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/internet-facing-load-balancers.html)

## 技術情報

- Source Metadata：[sources/aws/elbv2_internet_facing/metadata.json](../../sources/aws/elbv2_internet_facing/metadata.json)
- Source Code：[sources/aws/elbv2_internet_facing/check.py](../../sources/aws/elbv2_internet_facing/check.py)
- Source Metadata Path：`sources/aws/elbv2_internet_facing/metadata.json`
- Source Code Path：`sources/aws/elbv2_internet_facing/check.py`
