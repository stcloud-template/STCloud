# Secrets Manager secret has been accessed within the last 90 days

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `secretsmanager_secret_unused` |
| 云平台 | AWS |
| 服务 | secretsmanager |
| 严重等级 | medium |
| 类别 | secrets |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices |
| 资源类型 | AwsSecretsManagerSecret |
| 资源组 | security |

## 描述

**AWS Secrets Manager secrets** with no retrieval activity beyond a configured window (default `90` days) are identified as **unused** based on their most recent access timestamp

## 风险

Unused yet valid secrets jeopardize **confidentiality** and **integrity**: - Reuse by ex-users or leaked code enables unauthorized access - Limited rotation/revocation increases stealth persistence and data exfiltration - Secret sprawl adds operational risk and extra cost

## 推荐措施

Apply a **lifecycle policy** for secrets: - Require ownership tags and periodic reviews - Rotate or disable, then retire secrets unused beyond policy - Enforce **least privilege** and monitor retrievals with alerts - Automate cleanup using recovery windows to prevent accidental loss

## 修复步骤


### CLI

```text
aws secretsmanager delete-secret --secret-id <example_resource_id>
```

### Other

1. In the AWS Console, go to Secrets Manager
2. Select the unused secret
3. If the secret has replicas: in Replicate secret, select each replica and choose Actions > Delete replica
4. Choose Actions > Delete secret
5. Keep the default recovery window (or set one) and select Schedule deletion

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/secretsmanager-controls.html#secretsmanager-3](https://docs.aws.amazon.com/securityhub/latest/userguide/secretsmanager-controls.html#secretsmanager-3)
- [https://support.icompaas.com/support/solutions/articles/62000233606-ensure-secrets-manager-secrets-are-not-unused](https://support.icompaas.com/support/solutions/articles/62000233606-ensure-secrets-manager-secrets-are-not-unused)
- [https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_delete-secret.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_delete-secret.html)

## 技术信息

- Source Metadata：[sources/aws/secretsmanager_secret_unused/metadata.json](../../sources/aws/secretsmanager_secret_unused/metadata.json)
- Source Code：[sources/aws/secretsmanager_secret_unused/check.py](../../sources/aws/secretsmanager_secret_unused/check.py)
- Source Metadata Path：`sources/aws/secretsmanager_secret_unused/metadata.json`
- Source Code Path：`sources/aws/secretsmanager_secret_unused/check.py`
