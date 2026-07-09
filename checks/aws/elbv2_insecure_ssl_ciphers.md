# ELBv2 load balancer uses a secure SSL policy on HTTPS listeners

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `elbv2_insecure_ssl_ciphers` |
| 云平台 | AWS |
| 服务 | elbv2 |
| 严重等级 | medium |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark, Software and Configuration Checks/Industry and Regulatory Standards/PCI-DSS |
| 资源类型 | AwsElbv2LoadBalancer |
| 资源组 | network |

## 描述

**ELBv2 HTTPS listeners** are assessed for use of **strong TLS policies**. Listeners whose `ssl_policy` is not in the approved set (TLS 1.2/1.3-focused policies) may include weak protocols or ciphers.

## 风险

Legacy or weak ciphers enable **downgrade** and **man-in-the-middle** attacks, allowing decryption of sessions, credential theft, and request tampering. This undermines **confidentiality** and **integrity** of data in transit and can expose cookies or tokens for **account takeover**.

## 推荐措施

Enforce **modern TLS** on load balancer listeners: - Use AWS recommended policies like `ELBSecurityPolicy-TLS13-1-2-2021-06` - Disable TLS 1.0/1.1 and weak ciphers; prefer suites with **forward secrecy** - Periodically review and update policies Apply **defense in depth** with strict client access and **least privilege** for changes.

## 修复步骤


### CLI

```text
aws elbv2 modify-listener --listener-arn <listener_arn> --ssl-policy ELBSecurityPolicy-TLS13-1-2-2021-06
```

### Native IaC

```yaml
# CloudFormation: Set a secure SSL policy on an HTTPS listener
Resources:
  <example_resource_name>:
    Type: AWS::ElasticLoadBalancingV2::Listener
    Properties:
      LoadBalancerArn: <example_resource_arn>
      Protocol: HTTPS
      Port: 443
      DefaultActions:
        - Type: forward
          TargetGroupArn: <example_resource_arn>
      Certificates:
        - CertificateArn: <example_certificate_arn>
      SslPolicy: ELBSecurityPolicy-TLS13-1-2-2021-06  # FIX: uses an approved secure policy to eliminate insecure ciphers
```

### Terraform

```hcl
# Terraform: Ensure HTTPS listener uses a secure SSL policy
resource "aws_lb_listener" "<example_resource_name>" {
  load_balancer_arn = "<example_resource_arn>"
  port              = 443
  protocol          = "HTTPS"
  ssl_policy        = "ELBSecurityPolicy-TLS13-1-2-2021-06" # FIX: approved secure policy
  certificate_arn   = "<example_certificate_arn>"

  default_action {
    type             = "forward"
    target_group_arn = "<example_resource_arn>"
  }
}
```

### Other

1. In the AWS Console, go to EC2 > Load Balancers
2. Select the load balancer and open the Listeners tab
3. Select the HTTPS listener and choose Edit
4. Set Security policy to ELBSecurityPolicy-TLS13-1-2-2021-06 (or any approved policy)
5. Save changes

## 参考资料

- [https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#describe-ssl-policies](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#describe-ssl-policies)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/security-policy.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/security-policy.html)

## 技术信息

- Source Metadata：[sources/aws/elbv2_insecure_ssl_ciphers/metadata.json](../../sources/aws/elbv2_insecure_ssl_ciphers/metadata.json)
- Source Code：[sources/aws/elbv2_insecure_ssl_ciphers/check.py](../../sources/aws/elbv2_insecure_ssl_ciphers/check.py)
- Source Metadata Path：`sources/aws/elbv2_insecure_ssl_ciphers/metadata.json`
- Source Code Path：`sources/aws/elbv2_insecure_ssl_ciphers/check.py`
