# DMS endpoint for Neptune has IAM authorization enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `dms_endpoint_neptune_iam_authorization_enabled` |
| 云平台 | AWS |
| 服务 | dms |
| 严重等级 | medium |
| 类别 | identity-access |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Effects/Data Exposure |
| 资源类型 | AwsDmsEndpoint |
| 资源组 | database |

## 描述

**DMS Neptune endpoints** have **IAM authorization** enabled via the endpoint setting `IamAuthEnabled`.

## 风险

Without **IAM authorization**, migration components can interact with Neptune using broad trust, enabling unauthorized data loads, reads, or alterations. This degrades **confidentiality** and **integrity** and increases the chance of privilege abuse and data exfiltration.

## 推荐措施

Enable **IAM authorization** on Neptune endpoints (`IamAuthEnabled=true`) and use a **least privilege** service role limited to minimal Neptune and S3 permissions. Apply **defense in depth**: restrict network paths, separate duties for migration roles, and monitor access with logs and alerts.

## 修复步骤


### CLI

```text
aws dms modify-endpoint --endpoint-arn <endpoint-arn> --neptune-settings '{"IamAuthEnabled":true}'
```

### Native IaC

```yaml
# CloudFormation: Enable IAM authorization on a DMS Neptune endpoint
Resources:
  <example_resource_name>:
    Type: AWS::DMS::Endpoint
    Properties:
      EndpointType: target
      EngineName: neptune
      NeptuneSettings:
        ServiceAccessRoleArn: <example_resource_arn>
        S3BucketName: <example_resource_name>
        S3BucketFolder: <example_resource_name>
        IamAuthEnabled: true  # Critical: enables IAM authorization for the Neptune endpoint
```

### Other

1. In the AWS Console, go to Database Migration Service > Endpoints
2. Select the Neptune endpoint and click Modify
3. Expand Endpoint settings (Neptune settings) and set IAM authorization to Enabled
4. Ensure Service access role ARN is set, then click Save

## 参考资料

- [https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/dms-controls.html#dms-10](https://docs.aws.amazon.com/securityhub/latest/userguide/dms-controls.html#dms-10)

## 技术信息

- Source Metadata：[sources/aws/dms_endpoint_neptune_iam_authorization_enabled/metadata.json](../../sources/aws/dms_endpoint_neptune_iam_authorization_enabled/metadata.json)
- Source Code：[sources/aws/dms_endpoint_neptune_iam_authorization_enabled/check.py](../../sources/aws/dms_endpoint_neptune_iam_authorization_enabled/check.py)
- Source Metadata Path：`sources/aws/dms_endpoint_neptune_iam_authorization_enabled/metadata.json`
- Source Code Path：`sources/aws/dms_endpoint_neptune_iam_authorization_enabled/check.py`
