# Elastic Load Balancer is not internet-facing

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `elb_internet_facing` |
| クラウドプラットフォーム | AWS |
| サービス | elb |
| 重大度 | medium |
| カテゴリ | internet-exposed |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Effects/Data Exposure, TTPs/Initial Access |
| リソースタイプ | AwsElbLoadBalancer |
| リソースグループ | network |

## 説明

Elastic Load Balancers are evaluated for the `scheme` to determine whether they are **internet-facing** or internal, indicating if the endpoint is publicly reachable via a public DNS name.

## リスク

An unintended **internet-facing** load balancer exposes backends to the Internet, enabling reconnaissance, credential stuffing, and exploitation of app flaws. This can lead to data exposure (confidentiality), unauthorized changes (integrity), and **DDoS** or resource exhaustion (availability).

## 推奨事項

Use `internal` load balancers for private services and restrict exposure with **security groups**, subnets, and allowlists. For public endpoints, apply **defense in depth**: associate an **AWS WAF** web ACL (*when supported*), enforce **TLS**, least-privilege network rules, and consider **Shield** or rate limiting. Regularly review necessity of public access.

## 修正手順


### Native IaC

```yaml
# CloudFormation: create an internal load balancer
Resources:
  <example_resource_name>:
    Type: AWS::ElasticLoadBalancingV2::LoadBalancer
    Properties:
      Scheme: internal  # CRITICAL: makes the load balancer internal (not internet-facing)
      Subnets:
        - <example_resource_id>
        - <example_resource_id>
      SecurityGroups:
        - <example_resource_id>
```

### Terraform

```hcl
resource "aws_lb" "<example_resource_name>" {
  internal        = true  # CRITICAL: sets scheme to internal so it's not internet-facing
  subnets         = ["<example_resource_id>", "<example_resource_id>"]
  security_groups = ["<example_resource_id>"]
}
```

### Other

1. In AWS Console, go to EC2 > Load Balancers
2. Click Create load balancer (Application or Network)
3. Set Scheme to Internal
4. Select at least two subnets and a security group; recreate listeners/target groups as needed
5. Create the new load balancer and update DNS to its DNS name
6. Delete the old internet-facing load balancer

## 参考資料

- [https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-associating-aws-resource.html](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-associating-aws-resource.html)
- [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/internet-facing-load-balancers.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/internet-facing-load-balancers.html)

## 技術情報

- Source Metadata：[sources/aws/elb_internet_facing/metadata.json](../../sources/aws/elb_internet_facing/metadata.json)
- Source Code：[sources/aws/elb_internet_facing/check.py](../../sources/aws/elb_internet_facing/check.py)
- Source Metadata Path：`sources/aws/elb_internet_facing/metadata.json`
- Source Code Path：`sources/aws/elb_internet_facing/check.py`
