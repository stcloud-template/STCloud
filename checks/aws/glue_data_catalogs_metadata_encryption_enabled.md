# Glue Data Catalog metadata is encrypted with KMS

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `glue_data_catalogs_metadata_encryption_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | glue |
| 重大度 | medium |
| カテゴリ | encryption |
| チェックタイプ | Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark |
| リソースタイプ | Other |
| リソースグループ | analytics |

## 説明

**AWS Glue Data Catalog** metadata is encrypted at rest when catalog settings use **SSE-KMS** with a KMS key. Catalogs that do not configure `SSE-KMS` for metadata are considered unencrypted.

## リスク

Unencrypted catalog metadata exposes schemas, partitions, and data locations, reducing **confidentiality**. Adversaries or over-privileged users can conduct **reconnaissance** and plan lateral movement; tampering with definitions can corrupt queries and results, impacting **integrity**.

## 推奨事項

Enable metadata encryption with **`SSE-KMS`**, preferably using a **customer-managed KMS key** for control and rotation. Apply **least privilege** to KMS and catalog access, restrict who can change settings, and monitor key usage. Use **defense in depth** by encrypting related analytics assets consistently.

## 修正手順


### CLI

```text
aws glue put-data-catalog-encryption-settings --data-catalog-encryption-settings '{"EncryptionAtRest":{"CatalogEncryptionMode":"SSE-KMS"}}'
```

### Native IaC

```yaml
# Enable Glue Data Catalog metadata encryption with KMS
Resources:
  <example_resource_name>:
    Type: AWS::Glue::DataCatalogEncryptionSettings
    Properties:
      DataCatalogEncryptionSettings:
        EncryptionAtRest:
          CatalogEncryptionMode: SSE-KMS  # Critical: enables KMS encryption for catalog metadata
```

### Terraform

```hcl
# Enable Glue Data Catalog metadata encryption with KMS
resource "aws_glue_data_catalog_encryption_settings" "<example_resource_name>" {
  data_catalog_encryption_settings {
    encryption_at_rest {
      catalog_encryption_mode = "SSE-KMS" # Critical: turns on KMS encryption for catalog metadata
    }
  }
}
```

### Other

1. In the AWS Console, go to AWS Glue
2. Open Data Catalog > Settings
3. Under Security configuration and encryption, check Metadata encryption
4. Leave the default AWS managed key selected (or choose a KMS key)
5. Click Save

## 参考資料

- [https://docs.aws.amazon.com/glue/latest/dg/encrypt-glue-data-catalog.html](https://docs.aws.amazon.com/glue/latest/dg/encrypt-glue-data-catalog.html)
- [https://docs.amazonaws.cn/en_us/athena/latest/ug/encryption.html](https://docs.amazonaws.cn/en_us/athena/latest/ug/encryption.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Glue/data-catalog-encryption-at-rest-with-cmk.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Glue/data-catalog-encryption-at-rest-with-cmk.html)
- [https://support.icompaas.com/support/solutions/articles/62000233381-ensure-glue-data-catalogs-are-not-publicly-accessible-](https://support.icompaas.com/support/solutions/articles/62000233381-ensure-glue-data-catalogs-are-not-publicly-accessible-)

## 技術情報

- Source Metadata：[sources/aws/glue_data_catalogs_metadata_encryption_enabled/metadata.json](../../sources/aws/glue_data_catalogs_metadata_encryption_enabled/metadata.json)
- Source Code：[sources/aws/glue_data_catalogs_metadata_encryption_enabled/check.py](../../sources/aws/glue_data_catalogs_metadata_encryption_enabled/check.py)
- Source Metadata Path：`sources/aws/glue_data_catalogs_metadata_encryption_enabled/metadata.json`
- Source Code Path：`sources/aws/glue_data_catalogs_metadata_encryption_enabled/check.py`
