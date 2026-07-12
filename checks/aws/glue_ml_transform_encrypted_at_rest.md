# Glue ML Transform is encrypted at rest

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `glue_ml_transform_encrypted_at_rest` |
| クラウドプラットフォーム | AWS |
| サービス | glue |
| 重大度 | medium |
| カテゴリ | encryption |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls (USA) |
| リソースタイプ | Other |
| リソースグループ | analytics |

## 説明

**AWS Glue ML transforms** are evaluated for **encryption at rest** of transform user data using **KMS keys**. The finding highlights transforms where encryption is not configured.

## リスク

Without encryption, **confidentiality** is weakened: transform artifacts, mappings, and sample datasets may be readable via storage access, backups, or cross-account exposure. This can lead to data disclosure and aid **lateral movement** by revealing schemas and data relationships.

## 推奨事項

Enable **KMS-backed encryption at rest** for all ML transforms and prefer **customer-managed keys**. - Apply **least privilege** key policies and rotate keys - Enforce **defense in depth** with network and IAM controls - Monitor key usage and transform access with audit logs

## 修正手順


### CLI

```text
aws glue update-ml-transform --transform-id <transform-id> --transform-encryption '{"MlUserDataEncryption":{"MlUserDataEncryptionMode":"SSE-KMS","KmsKeyId":"<kms-key-arn>"}}'
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::Glue::MLTransform
    Properties:
      Role: <example_resource_id>
      InputRecordTables:
        - DatabaseName: <example_resource_name>
          TableName: <example_resource_name>
      TransformParameters:
        TransformType: FIND_MATCHES
        FindMatchesParameters:
          PrimaryKeyColumnName: <example_resource_name>
      TransformEncryption:
        MlUserDataEncryption:
          MlUserDataEncryptionMode: SSE-KMS  # Critical: enables ML user data encryption at rest
          KmsKeyId: <kms-key-arn>            # Critical: KMS key used for encryption
```

### Terraform

```hcl
resource "aws_glue_ml_transform" "<example_resource_name>" {
  name     = "<example_resource_name>"
  role_arn = "<example_resource_id>"

  input_record_tables {
    database_name = "<example_resource_name>"
    table_name    = "<example_resource_name>"
  }

  parameters {
    transform_type = "FIND_MATCHES"
    find_matches_parameters {
      primary_key_column_name = "<example_resource_name>"
    }
  }

  transform_encryption {
    ml_user_data_encryption {
      ml_user_data_encryption_mode = "SSE-KMS"   # Critical: enables encryption at rest
      kms_key_id                   = "<kms-key-arn>" # Critical: KMS key used for encryption
    }
  }
}
```

### Other

1. In the AWS Management Console, open AWS Glue
2. Go to Machine learning > Transforms and select the target transform
3. Click Edit
4. Under Encryption, enable ML user data encryption
5. Choose an AWS KMS key
6. Save changes

## 参考資料

- [https://docs.aws.amazon.com/glue/latest/dg/encryption-at-rest.html](https://docs.aws.amazon.com/glue/latest/dg/encryption-at-rest.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/glue-controls.html#glue-3](https://docs.aws.amazon.com/securityhub/latest/userguide/glue-controls.html#glue-3)

## 技術情報

- Source Metadata：[sources/aws/glue_ml_transform_encrypted_at_rest/metadata.json](../../sources/aws/glue_ml_transform_encrypted_at_rest/metadata.json)
- Source Code：[sources/aws/glue_ml_transform_encrypted_at_rest/check.py](../../sources/aws/glue_ml_transform_encrypted_at_rest/check.py)
- Source Metadata Path：`sources/aws/glue_ml_transform_encrypted_at_rest/metadata.json`
- Source Code Path：`sources/aws/glue_ml_transform_encrypted_at_rest/check.py`
