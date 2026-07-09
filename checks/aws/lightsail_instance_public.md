# Lightsail instance has no publicly accessible ports

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `lightsail_instance_public` |
| 云平台 | AWS |
| 服务 | lightsail |
| 严重等级 | high |
| 类别 | internet-exposed |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Initial Access |
| 资源类型 | Other |
| 资源组 | compute |

## 描述

**Lightsail instances** that have a **public IP** and at least one firewall rule allowing **public ports** are treated as publicly exposed. The evaluation inspects instance addressing and port rules to detect any port or range marked `public`.

## 风险

Public IP plus open ports enables Internet scanning, brute force, and exploits. - Confidentiality: data exfiltration - Integrity: RCE/admin takeover via exposed services - Availability: DoS or abuse (botnets, cryptomining), service disruption

## 推荐措施

Apply **least privilege** network access: close unused ports, restrict sources (avoid `0.0.0.0/0`), and review IPv4/IPv6 rules. Use a **VPN** or **bastion host** for administration. Place services behind private networking or load balancers, and harden/monitor any required public endpoints.

## 修复步骤


### CLI

```text
aws lightsail put-instance-public-ports --instance-name <example_resource_name> --port-infos '[]'
```

### Native IaC

```yaml
# CloudFormation: remove all public ports from a Lightsail instance
Resources:
  ClosePublicPorts:
    Type: AWS::Lightsail::InstancePublicPorts
    Properties:
      InstanceName: <example_resource_name>
      PortInfos: []  # Critical: empty list clears all public ports so the instance is not publicly exposed
```

### Terraform

```hcl
# Terraform: ensure no public ports are open on the Lightsail instance
resource "aws_lightsail_instance_public_ports" "<example_resource_name>" {
  instance_name = "<example_resource_name>"

  # Critical: no port_info blocks -> no public ports are configured (closes all)
  dynamic "port_info" {
    for_each = []
    content {
      from_port = 0
      to_port   = 0
      protocol  = "tcp"
    }
  }
}
```

### Other

1. Sign in to the AWS Lightsail console
2. Go to Instances and select <example_resource_name>
3. Open the Networking tab
4. In IPv4 Firewall, delete all existing rules, then Save
5. If IPv6 is enabled, in IPv6 Firewall, delete all existing rules, then Save

## 参考资料

- [https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-editing-firewall-rules.html](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-editing-firewall-rules.html)
- [https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-public-ip-and-private-ip-addresses-in-amazon-lightsail.html#ipv4-addresses](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-public-ip-and-private-ip-addresses-in-amazon-lightsail.html#ipv4-addresses)

## 技术信息

- Source Metadata：[sources/aws/lightsail_instance_public/metadata.json](../../sources/aws/lightsail_instance_public/metadata.json)
- Source Code：[sources/aws/lightsail_instance_public/check.py](../../sources/aws/lightsail_instance_public/check.py)
- Source Metadata Path：`sources/aws/lightsail_instance_public/metadata.json`
- Source Code Path：`sources/aws/lightsail_instance_public/check.py`
