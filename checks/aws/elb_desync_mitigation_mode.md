# Classic Load Balancer desync mitigation mode is defensive or strictest

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `elb_desync_mitigation_mode` |
| 云平台 | AWS |
| 服务 | elb |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Initial Access, TTPs/Defense Evasion |
| 资源类型 | AwsElbLoadBalancer |
| 资源组 | network |

## 描述

**Classic Load Balancer** `desync_mitigation_mode` is evaluated to determine whether it is configured as **`defensive`** or **`strictest`**. Any other mode (such as `monitor`) is identified for attention.

## 风险

Without strict desync mitigation, **HTTP request smuggling** can occur, enabling: - Cache/queue poisoning (**integrity**) - Session hijacking and data exposure (**confidentiality**) - Unintended backend actions and abuse (**availability**)

## 推荐措施

Set CLB desync mitigation to **`defensive`** or, where compatible, **`strictest`**. Validate in staging to avoid client breakage. Apply **defense in depth**: enforce strict header handling, pair with WAF controls, and monitor non-compliant request indicators.

## 修复步骤


### CLI

```text
aws elb modify-load-balancer-attributes --load-balancer-name <load-balancer-name> --load-balancer-attributes '{"AdditionalAttributes":[{"Key":"elb.http.desyncmitigationmode","Value":"defensive"}]}'
```

### Terraform

```hcl
resource "aws_elb" "<example_resource_name>" {
  name               = "<example_resource_name>"
  availability_zones = ["<example_az>"]

  listener {
    instance_port     = 80
    instance_protocol = "http"
    lb_port           = 80
    lb_protocol       = "http"
  }

  desync_mitigation_mode = "defensive" # Critical: sets CLB desync mitigation to defensive to pass the check
}
```

### Other

1. Open the AWS Management Console and go to EC2
2. Under Load Balancing, select Load Balancers
3. Select your Classic Load Balancer
4. On the Attributes tab, click Edit
5. Set Desync mitigation mode to Defensive or Strictest
6. Click Save changes

## 参考资料

- [https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-desync-mitigation-mode.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-desync-mitigation-mode.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-14](https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-14)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/enable-configure-desync-mitigation-mode.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/enable-configure-desync-mitigation-mode.html)
- [https://support.icompaas.com/support/solutions/articles/62000233337-ensure-classic-load-balancer-is-configured-with-defensive-or-strictest-desync-mitigation-mode](https://support.icompaas.com/support/solutions/articles/62000233337-ensure-classic-load-balancer-is-configured-with-defensive-or-strictest-desync-mitigation-mode)

## 技术信息

- Source Metadata：[sources/aws/elb_desync_mitigation_mode/metadata.json](../../sources/aws/elb_desync_mitigation_mode/metadata.json)
- Source Code：[sources/aws/elb_desync_mitigation_mode/check.py](../../sources/aws/elb_desync_mitigation_mode/check.py)
- Source Metadata Path：`sources/aws/elb_desync_mitigation_mode/metadata.json`
- Source Code Path：`sources/aws/elb_desync_mitigation_mode/check.py`
