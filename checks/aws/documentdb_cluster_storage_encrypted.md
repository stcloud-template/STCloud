# DocumentDB cluster storage is encrypted at rest

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `documentdb_cluster_storage_encrypted` |
| クラウドプラットフォーム | AWS |
| サービス | documentdb |
| 重大度 | medium |
| カテゴリ | encryption |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/PCI-DSS, Software and Configuration Checks/Industry and Regulatory Standards/HIPAA Controls (USA), Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls (USA), Software and Configuration Checks/Industry and Regulatory Standards/ISO 27001 Controls, Effects/Data Exposure |
| リソースタイプ | AwsRdsDbCluster |
| リソースグループ | database |

## 説明

**Amazon DocumentDB clusters** are assessed for **storage encryption at rest** via the cluster's `encrypted` setting. It identifies clusters where data volumes, automated backups, and snapshots aren't protected by AWS KMS-managed encryption.

## リスク

Without at-rest encryption, cluster data, snapshots, and backups can be read in plaintext if copies are leaked, mis-shared, or underlying storage is accessed. This harms **confidentiality**, enables offline analysis and data exfiltration, and widens the blast radius of insider or backup repository compromise.

## 推奨事項

Enable **storage encryption at rest** for all DocumentDB clusters and prefer **customer-managed KMS keys** for control over access, rotation, and revocation. Apply **least privilege** to key usage, enforce **separation of duties**, and monitor key and snapshot access. *If a cluster isn't encrypted*, migrate to a new encrypted cluster.

## 修正手順


### CLI

```text
aws docdb create-db-cluster --db-cluster-identifier <DB_CLUSTER_ID> --engine docdb --master-username <MASTER_USERNAME> --master-user-password <MASTER_PASSWORD> --storage-encrypted
```

### Native IaC

```yaml
# CloudFormation: Create an encrypted DocumentDB cluster
Resources:
  <example_resource_name>:
    Type: AWS::DocDB::DBCluster
    Properties:
      Engine: docdb
      MasterUsername: <MASTER_USERNAME>
      MasterUserPassword: <MASTER_PASSWORD>
      StorageEncrypted: true  # Critical: enables encryption at rest to pass the check
```

### Terraform

```hcl
# Terraform: Encrypted DocumentDB cluster
resource "aws_docdb_cluster" "<example_resource_name>" {
  master_username   = "<MASTER_USERNAME>"
  master_password   = "<MASTER_PASSWORD>"
  storage_encrypted = true  # Critical: enables encryption at rest to pass the check
}
```

### Other

1. In the AWS Console, go to Amazon DocumentDB
2. Click Create cluster
3. Expand Show advanced settings
4. In Encryption-at-rest, select Enable encryption
5. Choose or keep the default KMS key
6. Click Create cluster

To replace an existing unencrypted cluster:
1. Select the unencrypted cluster > Actions > Take snapshot
2. After the snapshot completes, select it > Actions > Restore snapshot
3. In Encryption-at-rest, select Enable encryption and restore as a new cluster
4. Update your applications to use the new cluster endpoint

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/documentdb-controls.html#documentdb-1](https://docs.aws.amazon.com/securityhub/latest/userguide/documentdb-controls.html#documentdb-1)
- [https://docs.aws.amazon.com/documentdb/latest/developerguide/elastic-encryption.html](https://docs.aws.amazon.com/documentdb/latest/developerguide/elastic-encryption.html)
- [https://docs.aws.amazon.com/documentdb/latest/developerguide/encryption-at-rest.html](https://docs.aws.amazon.com/documentdb/latest/developerguide/encryption-at-rest.html)

## 技術情報

- Source Metadata：[sources/aws/documentdb_cluster_storage_encrypted/metadata.json](../../sources/aws/documentdb_cluster_storage_encrypted/metadata.json)
- Source Code：[sources/aws/documentdb_cluster_storage_encrypted/check.py](../../sources/aws/documentdb_cluster_storage_encrypted/check.py)
- Source Metadata Path：`sources/aws/documentdb_cluster_storage_encrypted/metadata.json`
- Source Code Path：`sources/aws/documentdb_cluster_storage_encrypted/check.py`
