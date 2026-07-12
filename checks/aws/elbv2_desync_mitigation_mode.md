# Application Load Balancer has desync mitigation mode set to strictest or defensive, or drops invalid header fields

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `elbv2_desync_mitigation_mode` |
| クラウドプラットフォーム | AWS |
| サービス | elbv2 |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Initial Access, Effects/Data Exposure |
| リソースタイプ | AwsElbv2LoadBalancer |
| リソースグループ | network |

## 説明

**Application Load Balancer** settings are reviewed for **HTTP desync protections**. It evaluates `routing.http.desync_mitigation_mode` for `strictest` or `defensive`; when neither is configured, it checks `routing.http.drop_invalid_header_fields.enabled` is `true` as a compensating control.

## リスク

Lacking robust desync mitigation enables inconsistent HTTP parsing and **request smuggling**: - **Confidentiality**: token theft, data exfiltration - **Integrity**: cache/queue poisoning, unauthorized actions - **Availability**: backend exhaustion and outages Only dropping invalid headers reduces but does not eliminate this exposure.

## 推奨事項

Set ALBs to `desync_mitigation_mode`=`strictest` (*or* `defensive` if compatibility is required) and keep `routing.http.drop_invalid_header_fields.enabled`=`true`. Apply **defense in depth**: validate RFC-compliant requests, roll out changes gradually with monitoring, and enforce **least privilege** on downstream services.

## 修正手順


### CLI

```text
aws elbv2 modify-load-balancer-attributes --load-balancer-arn <ALB_ARN> --attributes Key=routing.http.desync_mitigation_mode,Value=strictest
```

### Native IaC

```yaml
# CloudFormation: Set ALB desync mitigation mode
Resources:
  <example_resource_name>:
    Type: AWS::ElasticLoadBalancingV2::LoadBalancer
    Properties:
      Type: application
      Subnets:
        - <example_subnet_id1>
        - <example_subnet_id2>
      LoadBalancerAttributes:
        - Key: routing.http.desync_mitigation_mode  # Critical: enforce strictest/defensive desync mitigation to pass the check
          Value: strictest
```

### Terraform

```hcl
# Terraform: Set ALB desync mitigation mode
resource "aws_lb" "<example_resource_name>" {
  name    = "<example_resource_name>"
  subnets = ["<example_subnet_id1>", "<example_subnet_id2>"]

  desync_mitigation_mode = "strictest" # Critical: enforce strictest/defensive desync mitigation to pass the check
}
```

### Other

1. Open the AWS Console and go to EC2 > Load Balancers
2. Select your Application Load Balancer
3. Choose Actions > Edit attributes (or the Attributes tab > Edit)
4. Set Desync mitigation mode to Strictest (or Defensive)
5. Save changes

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-12](https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-12)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/drop-invalid-header-fields-enabled.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/drop-invalid-header-fields-enabled.html)
- [https://support.icompaas.com/support/solutions/articles/62000233515-ensure-the-application-load-balancer-is-configured-with-strictest-desync-mitigation-mode](https://support.icompaas.com/support/solutions/articles/62000233515-ensure-the-application-load-balancer-is-configured-with-strictest-desync-mitigation-mode)
- [https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html#desync-mitigation-mode](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html#desync-mitigation-mode)

## 技術情報

- Source Metadata：[sources/aws/elbv2_desync_mitigation_mode/metadata.json](../../sources/aws/elbv2_desync_mitigation_mode/metadata.json)
- Source Code：[sources/aws/elbv2_desync_mitigation_mode/check.py](../../sources/aws/elbv2_desync_mitigation_mode/check.py)
- Source Metadata Path：`sources/aws/elbv2_desync_mitigation_mode/metadata.json`
- Source Code Path：`sources/aws/elbv2_desync_mitigation_mode/check.py`
