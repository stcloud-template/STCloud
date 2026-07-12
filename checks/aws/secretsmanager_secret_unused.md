# Secrets Manager secret has been accessed within the last 90 days

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `secretsmanager_secret_unused` |
| クラウドプラットフォーム | AWS |
| サービス | secretsmanager |
| 重大度 | medium |
| カテゴリ | secrets |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices |
| リソースタイプ | AwsSecretsManagerSecret |
| リソースグループ | security |

## 説明

**AWS Secrets Manager secrets** with no retrieval activity beyond a configured window (default `90` days) are identified as **unused** based on their most recent access timestamp

## リスク

Unused yet valid secrets jeopardize **confidentiality** and **integrity**: - Reuse by ex-users or leaked code enables unauthorized access - Limited rotation/revocation increases stealth persistence and data exfiltration - Secret sprawl adds operational risk and extra cost

## 推奨事項

Apply a **lifecycle policy** for secrets: - Require ownership tags and periodic reviews - Rotate or disable, then retire secrets unused beyond policy - Enforce **least privilege** and monitor retrievals with alerts - Automate cleanup using recovery windows to prevent accidental loss

## 修正手順


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

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/secretsmanager-controls.html#secretsmanager-3](https://docs.aws.amazon.com/securityhub/latest/userguide/secretsmanager-controls.html#secretsmanager-3)
- [https://support.icompaas.com/support/solutions/articles/62000233606-ensure-secrets-manager-secrets-are-not-unused](https://support.icompaas.com/support/solutions/articles/62000233606-ensure-secrets-manager-secrets-are-not-unused)
- [https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_delete-secret.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_delete-secret.html)

## 技術情報

- Source Metadata：[sources/aws/secretsmanager_secret_unused/metadata.json](../../sources/aws/secretsmanager_secret_unused/metadata.json)
- Source Code：[sources/aws/secretsmanager_secret_unused/check.py](../../sources/aws/secretsmanager_secret_unused/check.py)
- Source Metadata Path：`sources/aws/secretsmanager_secret_unused/metadata.json`
- Source Code Path：`sources/aws/secretsmanager_secret_unused/check.py`
