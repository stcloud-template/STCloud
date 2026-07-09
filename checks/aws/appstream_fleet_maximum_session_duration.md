# AppStream fleet maximum user session duration is less than 10 hours

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `appstream_fleet_maximum_session_duration` |
| 云平台 | AWS |
| 服务 | appstream |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices |
| 资源类型 | Other |
| 资源组 | compute |

## 描述

**AppStream fleets** enforce a **maximum user session duration**. This finding evaluates each fleet's configured limit against a threshold-default `10 hours` (`36000` seconds)-and identifies fleets whose session duration exceeds that limit.

## 风险

Overlong sessions widen the window for **session hijacking**, **lateral movement**, and **data exfiltration** if endpoints or tokens are compromised. Reduced reauthentication weakens **confidentiality** and **integrity**, and extended access can increase **costs** and resource contention.

## 推荐措施

Configure the **maximum session duration** to `<= 10 hours` (e.g., `600` minutes) or less based on data sensitivity. Prefer shorter limits, enforce **reauthentication** on renewal, apply **least privilege**, and enable **idle timeouts**. Monitor session activity as part of **defense in depth**.

## 修复步骤


### CLI

```text
aws appstream update-fleet --name <example_resource_name> --max-user-duration-in-seconds 3600
```

### Native IaC

```yaml
# CloudFormation: Set AppStream Fleet session duration below 10 hours
Resources:
  AppStreamFleet:
    Type: AWS::AppStream::Fleet
    Properties:
      Name: "<example_resource_name>"
      MaxUserDurationInSeconds: 3600  # CRITICAL: ensures max session duration is < 10h to pass the check
```

### Terraform

```hcl
# Terraform: Set AppStream Fleet session duration below 10 hours
resource "aws_appstream_fleet" "<example_resource_name>" {
  name                         = "<example_resource_name>"
  max_user_duration_in_seconds = 3600 # CRITICAL: ensures max session duration is < 10h to pass the check
}
```

### Other

1. Open the AWS Console and go to Amazon AppStream 2.0
2. Click Fleets and select <example_resource_name>
3. Click Edit
4. Set Maximum session duration to a value under 10 hours (e.g., 3600 seconds)
5. Save changes

## 参考资料

- [https://docs.aws.amazon.com/appstream2/latest/developerguide/set-up-stacks-fleets.html](https://docs.aws.amazon.com/appstream2/latest/developerguide/set-up-stacks-fleets.html)

## 技术信息

- Source Metadata：[sources/aws/appstream_fleet_maximum_session_duration/metadata.json](../../sources/aws/appstream_fleet_maximum_session_duration/metadata.json)
- Source Code：[sources/aws/appstream_fleet_maximum_session_duration/check.py](../../sources/aws/appstream_fleet_maximum_session_duration/check.py)
- Source Metadata Path：`sources/aws/appstream_fleet_maximum_session_duration/metadata.json`
- Source Code Path：`sources/aws/appstream_fleet_maximum_session_duration/check.py`
