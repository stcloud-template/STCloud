# CloudTrail trail S3 bucket has MFA delete enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudtrail_bucket_requires_mfa_delete` |
| クラウドプラットフォーム | AWS |
| サービス | cloudtrail |
| 重大度 | medium |
| カテゴリ | identity-access, forensics-ready |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark |
| リソースタイプ | AwsCloudTrailTrail |
| リソースグループ | monitoring |

## 説明

**CloudTrail log buckets** for actively logging trails are evaluated for **MFA Delete** on the associated S3 bucket. The assessment determines whether `MFA Delete` is configured on the in-account log bucket; *if the bucket resides in another account, its configuration should be verified separately*.

## リスク

Without **MFA Delete**, stolen or over-privileged credentials can permanently delete log versions or change versioning, compromising log **integrity** and **availability**. This enables attacker cover-ups, hinders **forensics**, and weakens evidence for investigations.

## 推奨事項

Enable `MFA Delete` on the CloudTrail log bucket with versioning enabled. Enforce **least privilege** so only tightly controlled identities can delete or alter logs, and require MFA for such actions. Apply **defense in depth** using a dedicated logging account and log file integrity validation.

## 修正手順


### CLI

```text
aws s3api put-bucket-versioning --bucket <CLOUDTRAIL_BUCKET_NAME> --versioning-configuration Status=Enabled,MFADelete=Enabled --mfa "<MFA_SERIAL> <MFA_CODE>"
```

### Other

1. Sign in to the AWS Management Console as the root user with MFA enabled
2. Open AWS CloudShell (from the top navigation bar)
3. Run:
   ```bash
   aws s3api put-bucket-versioning --bucket <CLOUDTRAIL_BUCKET_NAME> --versioning-configuration Status=Enabled,MFADelete=Enabled --mfa "<MFA_SERIAL> <MFA_CODE>"
   ```

## 参考資料

- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudTrail/cloudtrail-bucket-mfa-delete-enabled.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudTrail/cloudtrail-bucket-mfa-delete-enabled.html)

## 技術情報

- Source Metadata：[sources/aws/cloudtrail_bucket_requires_mfa_delete/metadata.json](../../sources/aws/cloudtrail_bucket_requires_mfa_delete/metadata.json)
- Source Code：[sources/aws/cloudtrail_bucket_requires_mfa_delete/check.py](../../sources/aws/cloudtrail_bucket_requires_mfa_delete/check.py)
- Source Metadata Path：`sources/aws/cloudtrail_bucket_requires_mfa_delete/metadata.json`
- Source Code Path：`sources/aws/cloudtrail_bucket_requires_mfa_delete/check.py`
