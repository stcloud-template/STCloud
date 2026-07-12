# AppStream fleet session idle disconnect timeout is 10 minutes or less

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `appstream_fleet_session_idle_disconnect_timeout` |
| クラウドプラットフォーム | AWS |
| サービス | appstream |
| 重大度 | medium |
| カテゴリ | identity-access |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Effects/Data Exposure |
| リソースタイプ | Other |
| リソースグループ | compute |

## 説明

**Amazon AppStream fleets** are evaluated for the **idle disconnect timeout** setting, confirming it is configured to `10 minutes` (`<=600s`) or less before inactive users are dropped and the session's `disconnect_timeout` window begins.

## リスク

**Long idle sessions** keep desktops/apps accessible without user presence, enabling **session hijacking**, **shoulder surfing**, and **data exposure**. They also **consume capacity** and extend **billing**, reducing **availability** for other users.

## 推奨事項

Configure an **idle disconnect timeout 10 minutes**. Pair with a short `disconnect_timeout`, require **re-authentication** on reconnect, and enforce **least privilege**. Monitor session metrics and adjust per role to balance **security**, **cost**, and **user experience**.

## 修正手順


### CLI

```text
aws appstream update-fleet --name <FLEET_NAME> --idle-disconnect-timeout-in-seconds 600
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::AppStream::Fleet
    Properties:
      Name: <example_resource_name>
      InstanceType: stream.standard.small
      ComputeCapacity:
        DesiredInstances: 1
      IdleDisconnectTimeoutInSeconds: 600  # Critical: set to 10 minutes or less to pass the check
```

### Terraform

```hcl
resource "aws_appstream_fleet" "<example_resource_name>" {
  name          = "<example_resource_name>"
  instance_type = "stream.standard.small"
  image_name    = "<IMAGE_NAME>"

  compute_capacity {
    desired_instances = 1
  }

  idle_disconnect_timeout_in_seconds = 600  # Critical: enforce <= 10 minutes to pass the check
}
```

### Other

1. Open the AWS Console and go to AppStream 2.0 > Fleets
2. Select your fleet and click Edit
3. Find "Idle disconnect timeout"
4. Set it to 10 minutes (600 seconds) or less
5. Click Save

## 参考資料

- [https://docs.aws.amazon.com/appstream2/latest/developerguide/set-up-stacks-fleets.html](https://docs.aws.amazon.com/appstream2/latest/developerguide/set-up-stacks-fleets.html)
- [https://awscli.amazonaws.com/v2/documentation/api/2.9.6/reference/appstream/update-fleet.html](https://awscli.amazonaws.com/v2/documentation/api/2.9.6/reference/appstream/update-fleet.html)

## 技術情報

- Source Metadata：[sources/aws/appstream_fleet_session_idle_disconnect_timeout/metadata.json](../../sources/aws/appstream_fleet_session_idle_disconnect_timeout/metadata.json)
- Source Code：[sources/aws/appstream_fleet_session_idle_disconnect_timeout/check.py](../../sources/aws/appstream_fleet_session_idle_disconnect_timeout/check.py)
- Source Metadata Path：`sources/aws/appstream_fleet_session_idle_disconnect_timeout/metadata.json`
- Source Code Path：`sources/aws/appstream_fleet_session_idle_disconnect_timeout/check.py`
