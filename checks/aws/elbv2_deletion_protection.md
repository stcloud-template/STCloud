# ELBv2 load balancer has deletion protection enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `elbv2_deletion_protection` |
| クラウドプラットフォーム | AWS |
| サービス | elbv2 |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Denial of Service |
| リソースタイプ | AwsElbv2LoadBalancer |
| リソースグループ | network |

## 説明

**ELBv2 load balancers** with **deletion protection** (`deletion_protection.enabled`) are resistant to deletion through standard APIs. The assessment determines whether this attribute is enabled on each load balancer.

## リスク

Without **deletion protection**, a user or automated process can delete the load balancer, cutting off service endpoints and breaking routing, harming **availability**. Malicious or mistaken deletes enable **DoS**, disrupt blue/green rollbacks, and increase incident recovery time.

## 推奨事項

Enable **deletion protection** for production and other critical load balancers. Enforce **least privilege** to restrict delete actions, apply governance (tags and policy guardrails) for protected assets, and require **change control** with approvals. *For pipelines*, add checks that block deletion of protected resources.

## 修正手順


### CLI

```text
aws elbv2 modify-load-balancer-attributes --load-balancer-arn <lb_arn> --attributes Key=deletion_protection.enabled,Value=true
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::ElasticLoadBalancingV2::LoadBalancer
    Properties:
      Subnets:
        - <example_subnet_id_1>
        - <example_subnet_id_2>
      LoadBalancerAttributes:
        - Key: deletion_protection.enabled  # Critical: enable deletion protection
          Value: "true"                   # Ensures the LB cannot be deleted accidentally
```

### Terraform

```hcl
resource "aws_lb" "<example_resource_name>" {
  subnets = ["<example_subnet_id_1>", "<example_subnet_id_2>"]

  enable_deletion_protection = true # Critical: enables deletion protection to pass the check
}
```

### Other

1. In the AWS Console, go to EC2 > Load Balancers (under Load Balancing)
2. Select the target load balancer
3. Open the Attributes tab and click Edit attributes
4. Enable Deletion protection
5. Click Save changes

## 参考資料

- [https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html#deletion-protection](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html#deletion-protection)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/deletion-protection.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/deletion-protection.html)

## 技術情報

- Source Metadata：[sources/aws/elbv2_deletion_protection/metadata.json](../../sources/aws/elbv2_deletion_protection/metadata.json)
- Source Code：[sources/aws/elbv2_deletion_protection/check.py](../../sources/aws/elbv2_deletion_protection/check.py)
- Source Metadata Path：`sources/aws/elbv2_deletion_protection/metadata.json`
- Source Code Path：`sources/aws/elbv2_deletion_protection/check.py`
