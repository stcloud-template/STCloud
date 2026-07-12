# Glue data catalog connection password is encrypted with a KMS key

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `glue_data_catalogs_connection_passwords_encryption_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | glue |
| 重大度 | high |
| カテゴリ | encryption |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark |
| リソースタイプ | Other |
| リソースグループ | analytics |

## 説明

**AWS Glue Data Catalog** settings for **connection password encryption** are evaluated to confirm an AWS KMS key is configured to encrypt passwords stored in connection properties.

## リスク

Unencrypted connection passwords can be read from the catalog or responses, letting attackers or over-privileged users obtain database credentials. This jeopardizes confidentiality of linked data stores, enables unauthorized modifications, and can facilitate lateral movement across environments.

## 推奨事項

Enable **connection password encryption** in the Data Catalog with a customer-managed KMS key. - Apply **least privilege** to the KMS key and Glue roles - Prefer keeping responses encrypted (`ReturnConnectionPasswordEncrypted`) - Rotate keys and monitor access for **defense in depth**

## 修正手順


### CLI

```text
aws glue put-data-catalog-encryption-settings --data-catalog-encryption-settings '{"ConnectionPasswordEncryption":{"ReturnConnectionPasswordEncrypted":true,"AwsKmsKeyId":"<kms_key_arn>"}}'
```

### Native IaC

```yaml
# CloudFormation: enable Glue Data Catalog connection password encryption
Resources:
  <example_resource_name>:
    Type: AWS::Glue::DataCatalogEncryptionSettings
    Properties:
      DataCatalogEncryptionSettings:
        ConnectionPasswordEncryption:
          ReturnConnectionPasswordEncrypted: true  # Critical: encrypts connection passwords
          KmsKeyId: <kms_key_arn>  # Critical: KMS key used for encryption
```

### Terraform

```hcl
# Enable Glue Data Catalog connection password encryption
resource "aws_glue_data_catalog_encryption_settings" "<example_resource_name>" {
  data_catalog_encryption_settings {
    # Critical: enables password encryption with a KMS key
    connection_password_encryption {
      return_connection_password_encrypted = true
      aws_kms_key_id                       = "<kms_key_arn>"
    }

    # Required block for this resource; keep minimal
    encryption_at_rest {
      catalog_encryption_mode = "DISABLED"
    }
  }
}
```

### Other

1. In the AWS Console, go to AWS Glue
2. Click Settings (left menu)
3. Under Data catalog settings, check Encrypt connection passwords
4. Select your KMS key (symmetric CMK)
5. Click Save

## 参考資料

- [https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-security.html](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-security.html)
- [https://docs.aws.amazon.com/glue/latest/dg/encrypt-connection-passwords.html](https://docs.aws.amazon.com/glue/latest/dg/encrypt-connection-passwords.html)

## 技術情報

- Source Metadata：[sources/aws/glue_data_catalogs_connection_passwords_encryption_enabled/metadata.json](../../sources/aws/glue_data_catalogs_connection_passwords_encryption_enabled/metadata.json)
- Source Code：[sources/aws/glue_data_catalogs_connection_passwords_encryption_enabled/check.py](../../sources/aws/glue_data_catalogs_connection_passwords_encryption_enabled/check.py)
- Source Metadata Path：`sources/aws/glue_data_catalogs_connection_passwords_encryption_enabled/metadata.json`
- Source Code Path：`sources/aws/glue_data_catalogs_connection_passwords_encryption_enabled/check.py`
