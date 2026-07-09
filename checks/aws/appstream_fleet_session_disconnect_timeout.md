# AppStream fleet session disconnect timeout is 5 minutes or less

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `appstream_fleet_session_disconnect_timeout` |
| 云平台 | AWS |
| 服务 | appstream |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark |
| 资源类型 | Other |
| 资源组 | compute |

## 描述

**AppStream fleets** are evaluated for `DisconnectTimeoutInSeconds` being at or below `300` seconds (5 minutes), which defines how long a streaming session remains active after a user disconnects.

## 风险

Long disconnect times keep sessions active, enabling **session hijacking** or unintended reconnection on lost/stolen devices. This raises data exposure (confidentiality), permits unauthorized actions (integrity), and ties up capacity and costs (availability/operations).

## 推荐措施

Set `DisconnectTimeoutInSeconds` to `300` or less across fleets. Pair with a short `IdleDisconnectTimeoutInSeconds`, require re-authentication on reconnect, and enforce **least privilege**. Monitor session events and use **defense in depth** (network restrictions, device posture) to reduce takeover risk.

## 修复步骤


### CLI

```text
aws appstream update-fleet --name <example_resource_name> --disconnect-timeout-in-seconds 300
```

### Native IaC

```yaml
# CloudFormation: Set AppStream Fleet disconnect timeout to 5 minutes or less
Resources:
  ExampleFleet:
    Type: AWS::AppStream::Fleet
    Properties:
      Name: <example_resource_name>
      InstanceType: stream.standard.medium
      ImageName: <example_image_name>
      ComputeCapacity:
        DesiredInstances: 1
      DisconnectTimeoutInSeconds: 300  # CRITICAL: ensures session disconnect timeout is <= 300s
```

### Terraform

```hcl
# Terraform: Set AppStream Fleet disconnect timeout to 5 minutes or less
resource "aws_appstream_fleet" "<example_resource_name>" {
  name          = "<example_resource_name>"
  instance_type = "stream.standard.medium"
  image_name    = "<example_image_name>"

  compute_capacity {
    desired_instances = 1
  }

  disconnect_timeout_in_seconds = 300  # CRITICAL: ensures timeout is <= 300s
}
```

### Other

1. In the AWS console, go to Amazon AppStream 2.0 > Fleets
2. Select the fleet <example_resource_name> and choose Edit
3. Set Disconnect timeout to 5 minutes (300 seconds) or less
4. Save changes

## 参考资料

- [https://docs.aws.amazon.com/appstream2/latest/developerguide/set-up-stacks-fleets.html](https://docs.aws.amazon.com/appstream2/latest/developerguide/set-up-stacks-fleets.html)
- [https://awscli.amazonaws.com/v2/documentation/api/2.9.6/reference/appstream/update-fleet.html](https://awscli.amazonaws.com/v2/documentation/api/2.9.6/reference/appstream/update-fleet.html)

## 技术信息

- Source Metadata：[sources/aws/appstream_fleet_session_disconnect_timeout/metadata.json](../../sources/aws/appstream_fleet_session_disconnect_timeout/metadata.json)
- Source Code：[sources/aws/appstream_fleet_session_disconnect_timeout/check.py](../../sources/aws/appstream_fleet_session_disconnect_timeout/check.py)
- Source Metadata Path：`sources/aws/appstream_fleet_session_disconnect_timeout/metadata.json`
- Source Code Path：`sources/aws/appstream_fleet_session_disconnect_timeout/check.py`
