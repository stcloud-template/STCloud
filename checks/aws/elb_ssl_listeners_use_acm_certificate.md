# Classic Load Balancer HTTPS/SSL listeners use ACM-issued certificates

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `elb_ssl_listeners_use_acm_certificate` |
| クラウドプラットフォーム | AWS |
| サービス | elb |
| 重大度 | medium |
| カテゴリ | encryption |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | AwsElbLoadBalancer |
| リソースグループ | network |

## 説明

Classic Load Balancer HTTPS/SSL listeners use **AWS Certificate Manager** certificates that are **Amazon-issued** (certificate type `AMAZON_ISSUED`).

## リスク

Using imported or non Amazon-issued certificates reduces control over issuance and rotation, increasing chances of **expired or weak TLS**. This can trigger **service outages** and enable **man-in-the-middle** interception, compromising data **confidentiality** and **integrity**.

## 推奨事項

Standardize on **Amazon-issued ACM certificates** for CLB HTTPS/SSL listeners to ensure managed validation and **automatic renewal**. Apply **least privilege** to certificate operations, automate rotation, and monitor certificate health as part of **defense in depth**.

## 修正手順


### CLI

```text
aws elb set-load-balancer-listener-ssl-certificate --load-balancer-name <load-balancer-name> --load-balancer-port <port> --ssl-certificate-id <acm_certificate_arn>
```

### Native IaC

```yaml
# CloudFormation: Attach an Amazon-issued ACM cert to a CLB HTTPS/SSL listener
Resources:
  <example_resource_name>:
    Type: AWS::ElasticLoadBalancing::LoadBalancer
    Properties:
      AvailabilityZones:
        - <example_az>
      Listeners:
        - LoadBalancerPort: 443
          InstancePort: 443
          Protocol: HTTPS
          SSLCertificateId: <acm_certificate_arn>  # critical: use Amazon-issued ACM certificate to pass ELB.2
```

### Terraform

```hcl
# Terraform: Attach an Amazon-issued ACM cert to a CLB HTTPS/SSL listener
resource "aws_elb" "<example_resource_name>" {
  availability_zones = ["<example_az>"]

  listener {
    lb_port            = 443
    lb_protocol        = "https"
    instance_port      = 443
    instance_protocol  = "https"
    ssl_certificate_id = "<acm_certificate_arn>" # critical: Amazon-issued ACM cert to satisfy ELB.2
  }
}
```

### Other

1. In the AWS Console, go to EC2 > Load Balancing > Load Balancers (Classic)
2. Select the Classic Load Balancer
3. Open the Listeners tab and choose the HTTPS/SSL listener
4. Click Edit (or Change SSL certificate)
5. Select an ACM certificate that is Amazon-issued (not imported)
6. Save changes

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-2](https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-2)
- [https://docs.aws.amazon.com/config/latest/developerguide/elb-acm-certificate-required.html](https://docs.aws.amazon.com/config/latest/developerguide/elb-acm-certificate-required.html)

## 技術情報

- Source Metadata：[sources/aws/elb_ssl_listeners_use_acm_certificate/metadata.json](../../sources/aws/elb_ssl_listeners_use_acm_certificate/metadata.json)
- Source Code：[sources/aws/elb_ssl_listeners_use_acm_certificate/check.py](../../sources/aws/elb_ssl_listeners_use_acm_certificate/check.py)
- Source Metadata Path：`sources/aws/elb_ssl_listeners_use_acm_certificate/metadata.json`
- Source Code Path：`sources/aws/elb_ssl_listeners_use_acm_certificate/check.py`
