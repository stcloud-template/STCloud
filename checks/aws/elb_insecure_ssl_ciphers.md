# Elastic Load Balancer HTTPS listeners, if present, use the ELBSecurityPolicy-TLS-1-2-2017-01 policy

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `elb_insecure_ssl_ciphers` |
| 云平台 | AWS |
| 服务 | elb |
| 严重等级 | medium |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark, Software and Configuration Checks/Industry and Regulatory Standards/PCI-DSS, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls (USA) |
| 资源类型 | AwsElbLoadBalancer |
| 资源组 | network |

## 描述

Elastic Load Balancer HTTPS listeners are assessed for use of a **strong TLS policy**. Listeners associated with `ELBSecurityPolicy-TLS-1-2-2017-01` are considered to negotiate only modern protocols and ciphers, avoiding legacy SSL/TLS and weak suites.

## 风险

Legacy TLS or weak ciphers allow downgrades and man-in-the-middle decryption or tampering. Attackers can capture credentials, inject responses, and pivot, undermining data-in-transit **confidentiality** and **integrity**, and risking **availability** through failed handshakes.

## 推荐措施

Standardize on ELB policies enforcing **TLS 1.2+** with modern AEAD ciphers; disable legacy protocols and weak suites. Enable server cipher order, retire outdated policies, and review regularly for crypto agility. Validate client compatibility, use strong certificates, and monitor negotiation results.

## 修复步骤


### CLI

```text
aws elb set-load-balancer-policies-of-listener --load-balancer-name <lb_name> --load-balancer-port 443 --policy-names ELBSecurityPolicy-TLS-1-2-2017-01
```

### Native IaC

```yaml
# CloudFormation: Classic ELB with TLS 1.2-only security policy on HTTPS listener
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
          InstanceProtocol: HTTPS
          SSLCertificateId: <example_certificate_arn>
          PolicyNames:
            - ELBSecurityPolicy-TLS-1-2-2017-01  # Critical: attach TLS 1.2-only policy to the HTTPS listener
      Policies:
        - PolicyName: ELBSecurityPolicy-TLS-1-2-2017-01  # Critical: create policy referencing the predefined TLS 1.2 policy
          PolicyType: SSLNegotiationPolicyType
          Attributes:
            - Name: Reference-Security-Policy
              Value: ELBSecurityPolicy-TLS-1-2-2017-01  # Critical: enforce TLS 1.2-only
```

### Terraform

```hcl
# Create and attach TLS 1.2-only policy to a Classic ELB HTTPS listener
resource "aws_load_balancer_policy" "<example_resource_name>" {
  load_balancer_name = "<example_resource_name>"
  policy_name        = "ELBSecurityPolicy-TLS-1-2-2017-01"  # Critical: policy named as required by the check
  policy_type_name   = "SSLNegotiationPolicyType"

  policy_attributes {
    name  = "Reference-Security-Policy"
    value = "ELBSecurityPolicy-TLS-1-2-2017-01"  # Critical: reference the predefined TLS 1.2 policy
  }
}

resource "aws_load_balancer_listener_policy" "<example_resource_name>" {
  load_balancer_name = "<example_resource_name>"
  load_balancer_port = 443
  policy_names       = [aws_load_balancer_policy.<example_resource_name>.policy_name]  # Critical: attach policy to HTTPS listener
}
```

### Other

1. Open the AWS Management Console and go to EC2
2. In the left menu, under Load Balancing, click Load Balancers
3. Select your Classic Load Balancer
4. On the Listeners tab, click Manage listeners (or Edit)
5. Select the HTTPS (port 443) listener and under Security policy choose ELBSecurityPolicy-TLS-1-2-2017-01
6. Click Save changes

## 参考资料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/elb-security-policy.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/elb-security-policy.html)
- [https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#describe-ssl-policies](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#describe-ssl-policies)
- [https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/ssl-config-update.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/ssl-config-update.html)
- [https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html)

## 技术信息

- Source Metadata：[sources/aws/elb_insecure_ssl_ciphers/metadata.json](../../sources/aws/elb_insecure_ssl_ciphers/metadata.json)
- Source Code：[sources/aws/elb_insecure_ssl_ciphers/check.py](../../sources/aws/elb_insecure_ssl_ciphers/check.py)
- Source Metadata Path：`sources/aws/elb_insecure_ssl_ciphers/metadata.json`
- Source Code Path：`sources/aws/elb_insecure_ssl_ciphers/check.py`
