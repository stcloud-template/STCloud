# DynamoDB table resource-based policy does not allow cross-account access

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `dynamodb_table_cross_account_access` |
| 云平台 | AWS |
| 服务 | dynamodb |
| 严重等级 | medium |
| 类别 | trust-boundaries |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, TTPs/Initial Access/Unauthorized Access, Effects/Data Exposure |
| 资源类型 | AwsDynamoDbTable |
| 资源组 | database |

## 描述

**DynamoDB tables** are evaluated for **resource-based policies** that permit cross-account or public principals. Tables without a resource policy, or with policies restricted to the same account, are identified as isolated configurations.

## 风险

Allowing other accounts to access a table affects: - **Confidentiality**: unauthorized reads/data exfiltration - **Integrity**: writes or deletes by external principals - **Availability**: capacity exhaustion and throttling - **Cost**: owner pays for external requests If public principals are allowed, exposure can be unrestricted.

## 推荐措施

Apply **least privilege**: - Avoid cross-account data access; *if required*, allow only named principals - Constrain with `aws:PrincipalOrgID`, `aws:SourceVpc`, `aws:PrincipalArn`; add `Deny` guardrails - Enable **Block Public Access** and monitor with **IAM Access Analyzer**

## 修复步骤


### CLI

```text
aws dynamodb delete-resource-policy --resource-arn <resource-arn>
```

### Other

1. Open the AWS Console and go to DynamoDB > Tables
2. Select <example_resource_name> and open the Permissions tab
3. In Resource-based policy, click Delete policy and confirm
4. Save changes to remove any cross-account access

## 参考资料

- [https://support.icompaas.com/support/solutions/articles/62000233614-ensure-dynamodb-tables-should-not-be-accessible-from-other-aws-accounts](https://support.icompaas.com/support/solutions/articles/62000233614-ensure-dynamodb-tables-should-not-be-accessible-from-other-aws-accounts)
- [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/access-control-resource-based.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/access-control-resource-based.html)
- [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/rbac-bpa-rbp.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/rbac-bpa-rbp.html)

## 技术信息

- Source Metadata：[sources/aws/dynamodb_table_cross_account_access/metadata.json](../../sources/aws/dynamodb_table_cross_account_access/metadata.json)
- Source Code：[sources/aws/dynamodb_table_cross_account_access/check.py](../../sources/aws/dynamodb_table_cross_account_access/check.py)
- Source Metadata Path：`sources/aws/dynamodb_table_cross_account_access/metadata.json`
- Source Code Path：`sources/aws/dynamodb_table_cross_account_access/check.py`
