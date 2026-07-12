# ELBv2 Application Load Balancer listeners use HTTPS or redirect HTTP to HTTPS

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `elbv2_ssl_listeners` |
| クラウドプラットフォーム | AWS |
| サービス | elbv2 |
| 重大度 | medium |
| カテゴリ | encryption |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exposure |
| リソースタイプ | AwsElbv2LoadBalancer |
| リソースグループ | network |

## 説明

**Application Load Balancer listeners** are assessed for **encrypted ingress**: either only `HTTPS` listeners are present, or any `HTTP` listener redirects to `HTTPS`.

## リスク

Exposed `HTTP` paths allow traffic to travel in plaintext, enabling interception, credential theft, session hijacking, and response tampering. This weakens confidentiality and integrity and makes **MITM** on public or shared networks feasible.

## 推奨事項

Enforce **TLS everywhere**: use `HTTPS` listeners and make all `HTTP` listeners redirect to `HTTPS` only. Do not forward plaintext. Apply **defense in depth** with strong TLS policies and managed certificates, and consider `HSTS` to prevent users from reaching `http`.

## 修正手順


### CLI

```text
aws elbv2 modify-listener --listener-arn <listener_arn> --default-actions '[{"Type":"redirect","RedirectConfig":{"Protocol":"HTTPS","Port":"443","StatusCode":"HTTP_301"}}]'
```

### Native IaC

```yaml
# CloudFormation: Redirect HTTP listener to HTTPS
Resources:
  <example_resource_name>:
    Type: AWS::ElasticLoadBalancingV2::Listener
    Properties:
      LoadBalancerArn: <example_resource_id>
      Protocol: HTTP
      Port: 80
      DefaultActions:
        - Type: redirect
          RedirectConfig:
            Protocol: HTTPS  # Critical: redirect HTTP to HTTPS
            Port: '443'      # Critical: target HTTPS port
            StatusCode: HTTP_301  # Critical: enforce redirect
```

### Terraform

```hcl
# Terraform: Redirect HTTP listener to HTTPS
resource "aws_lb_listener" "<example_resource_name>" {
  load_balancer_arn = "<example_resource_id>"
  protocol          = "HTTP"
  port              = 80

  default_action {
    type = "redirect"
    redirect {
      protocol   = "HTTPS"   # Critical: redirect to HTTPS
      port       = "443"     # Critical: target HTTPS port
      status_code = "HTTP_301" # Critical: enforce redirect
    }
  }
}
```

### Other

1. Open the EC2 console and go to Load Balancers
2. Select the Application Load Balancer and open the Listeners tab
3. Select the HTTP:80 listener and choose Edit (or View/edit rules)
4. Set the default action to Redirect to, Protocol: HTTPS, Port: 443, Status code: HTTP_301
5. Save changes

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-1](https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-1)
- [https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html)

## 技術情報

- Source Metadata：[sources/aws/elbv2_ssl_listeners/metadata.json](../../sources/aws/elbv2_ssl_listeners/metadata.json)
- Source Code：[sources/aws/elbv2_ssl_listeners/check.py](../../sources/aws/elbv2_ssl_listeners/check.py)
- Source Metadata Path：`sources/aws/elbv2_ssl_listeners/metadata.json`
- Source Code Path：`sources/aws/elbv2_ssl_listeners/check.py`
