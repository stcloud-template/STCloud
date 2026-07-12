# ELBv2 load balancer has at least one listener

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `elbv2_listeners_underneath` |
| クラウドプラットフォーム | AWS |
| サービス | elbv2 |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Effects/Denial of Service |
| リソースタイプ | AwsElbv2LoadBalancer |
| リソースグループ | network |

## 説明

**ELBv2 load balancer** requires at least one **listener** (protocol and port) to accept client connections and route requests to target groups. The finding indicates whether listeners are defined on the load balancer.

## リスク

Without a listener, the load balancer cannot accept connections, making back-end services unreachable. This harms **availability**, leads to client timeouts and errors, and disrupts integrations that rely on the load balancer's DNS endpoint.

## 推奨事項

Define at least one listener per load balancer. Prefer **HTTPS** on `443` to protect data in transit, and expose only required ports. Apply **least privilege** by limiting protocols and rules to intended traffic, and set an explicit default action to avoid unintended routing.

## 修正手順


### CLI

```text
aws elbv2 create-listener --load-balancer-arn <LOAD_BALANCER_ARN> --protocol HTTP --port 80 --default-actions 'Type=fixed-response,FixedResponseConfig={StatusCode=200}'
```

### Native IaC

```yaml
# CloudFormation: add a minimal listener to the ELBv2
Resources:
  <example_resource_name>:
    Type: AWS::ElasticLoadBalancingV2::Listener
    Properties:
      LoadBalancerArn: <example_load_balancer_arn>  # Critical: attaches the listener to the load balancer
      Port: 80                                      # Critical: defines the listener port
      Protocol: HTTP                                # Critical: defines the listener protocol
      DefaultActions:
        - Type: fixed-response                       # Critical: minimal required default action so the listener is valid
          FixedResponseConfig:
            StatusCode: '200'                       # Critical: required for fixed-response action
```

### Terraform

```hcl
# Terraform: add a minimal listener to the ELBv2
resource "aws_lb_listener" "<example_resource_name>" {
  load_balancer_arn = "<example_load_balancer_arn>"  # Critical: attaches the listener to the load balancer
  port              = 80                               # Critical: defines the listener port
  protocol          = "HTTP"                          # Critical: defines the listener protocol

  default_action {                                     # Critical: required default action so the listener is valid
    type = "fixed-response"
    fixed_response {
      status_code = "200"                             # Critical: required for fixed-response action
    }
  }
}
```

### Other

1. In the AWS Console, go to EC2 > Load Balancing > Load Balancers
2. Select the load balancer with the finding
3. Open the Listeners tab and click Add listener
4. Set Protocol to HTTP and Port to 80
5. For Default action, choose Return fixed response and set Status code to 200
6. Click Create/Save to add the listener

## 参考資料

- [https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html)

## 技術情報

- Source Metadata：[sources/aws/elbv2_listeners_underneath/metadata.json](../../sources/aws/elbv2_listeners_underneath/metadata.json)
- Source Code：[sources/aws/elbv2_listeners_underneath/check.py](../../sources/aws/elbv2_listeners_underneath/check.py)
- Source Metadata Path：`sources/aws/elbv2_listeners_underneath/metadata.json`
- Source Code Path：`sources/aws/elbv2_listeners_underneath/check.py`
