# Direct Connect connections span at least two locations per region

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `directconnect_connection_redundancy` |
| 云平台 | AWS |
| 服务 | directconnect |
| 严重等级 | medium |
| 类别 | resilience |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/AWS Security Best Practices/Network Reachability |
| 资源类型 | Other |
| 资源组 | network |

## 描述

**AWS Direct Connect** connectivity is provisioned with **connection and location redundancy**-multiple connections spread across **at least two distinct Direct Connect locations** in each Region.

## 风险

Missing **connection/location redundancy** creates a **single point of failure**, degrading **availability**. A router, fiber, or site outage can sever private paths to AWS, stalling app traffic, data replication, and admin access, leading to timeouts or extended downtime until alternate paths are restored.

## 推荐措施

Apply **redundancy** and **defense in depth**: - Deploy 2 Direct Connect connections across **two distinct locations** - Use **dynamic, active/active routing** for automatic failover - Ensure **provider/device diversity** - Size capacity so one link loss doesn't overload remaining paths - Consider a **VPN** as tertiary backup

## 修复步骤


### CLI

```text
aws directconnect create-connection --region <REGION> --location <NEW_DX_LOCATION_CODE> --bandwidth 1Gbps --connection-name <example_resource_name>
```

### Terraform

```hcl
# Create an additional Direct Connect connection in a different location
resource "aws_dx_connection" "example" {
  name      = "<example_resource_name>"
  bandwidth = "1Gbps"
  location  = "<NEW_DX_LOCATION_CODE>" # Critical: choose a different DX location in the same Region to achieve location redundancy
}
```

### Other

1. In the AWS Console, go to Direct Connect > Connections
2. Click Create connection
3. Region: select the Region where the existing connection resides
4. Name: enter <example_resource_name>
5. Location: select a different Direct Connect location than your existing connection
6. Bandwidth: choose a supported value (e.g., 1 Gbps)
7. Click Create connection

## 参考资料

- [https://docs.aws.amazon.com/awssupport/latest/user/fault-tolerance-checks.html#amazon-direct-connect-location-resiliency](https://docs.aws.amazon.com/awssupport/latest/user/fault-tolerance-checks.html#amazon-direct-connect-location-resiliency)
- [https://repost.aws/knowledge-center/direct-connect-physical-redundancy](https://repost.aws/knowledge-center/direct-connect-physical-redundancy)
- [https://aws.amazon.com/directconnect/resiliency-recommendation/](https://aws.amazon.com/directconnect/resiliency-recommendation/)

## 技术信息

- Source Metadata：[sources/aws/directconnect_connection_redundancy/metadata.json](../../sources/aws/directconnect_connection_redundancy/metadata.json)
- Source Code：[sources/aws/directconnect_connection_redundancy/check.py](../../sources/aws/directconnect_connection_redundancy/check.py)
- Source Metadata Path：`sources/aws/directconnect_connection_redundancy/metadata.json`
- Source Code Path：`sources/aws/directconnect_connection_redundancy/check.py`
