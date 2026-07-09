# Ensure VM Disks for Critical VMs Are Encrypted With Customer-Supplied Encryption Keys (CSEK)

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `compute_instance_encryption_with_csek_enabled` |
| 云平台 | GCP |
| 服务 | compute |
| 严重等级 | high |
| 类别 | encryption |
| 资源类型 | Disks |
| 资源组 | storage |

## 描述

Customer-Supplied Encryption Keys (CSEK) are a feature in Google Cloud Storage and Google Compute Engine. If you supply your own encryption keys, Google uses your key to protect the Google-generated keys used to encrypt and decrypt your data. By default, Google Compute Engine encrypts all data at rest. Compute Engine handles and manages this encryption for you without any additional actions on your part. However, if you wanted to control and manage this encryption yourself, you can provide your own encryption keys.

## 风险

By default, Compute Engine service encrypts all data at rest. The cloud service manages this type of encryption without any additional actions from you and your application. However, if you want to fully control and manage instance disk encryption, you can provide your own encryption keys.

## 推荐措施

Ensure that the disks attached to your production Google Compute Engine instances are encrypted with Customer-Supplied Encryption Keys (CSEKs) in order to have complete control over the data-at-rest encryption and decryption process, and meet strict compliance requirements. These custom keys, also known as Customer-Supplied Encryption Keys (CSEKs), are used by Google Compute Engine to protect the Google-generated keys used to encrypt and decrypt your instance data. Compute Engine service does not store your CSEKs on its servers and cannot access your protected data unless you provide the required key.

- 推荐链接：[https://cloud.google.com/storage/docs/encryption/using-customer-supplied-keys](https://cloud.google.com/storage/docs/encryption/using-customer-supplied-keys)

## 修复步骤


### CLI

```text
gcloud compute disks create <DISK_NAME> --size=<SIZE> --type=<TYPE> --zone=<ZONE> --source-snapshot=<SOURCE_SNAPSHOT> --csek-key-file=<KEY_FILE>
```

### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-general-policies/bc_gcp_general_x#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-general-policies/bc_gcp_general_x#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/enable-encryption-with-csek.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/enable-encryption-with-csek.html)

## 参考资料

- [https://cloud.google.com/storage/docs/encryption/using-customer-supplied-keys](https://cloud.google.com/storage/docs/encryption/using-customer-supplied-keys)

## 技术信息

- Source Metadata：[sources/gcp/compute_instance_encryption_with_csek_enabled/metadata.json](../../sources/gcp/compute_instance_encryption_with_csek_enabled/metadata.json)
- Source Code：[sources/gcp/compute_instance_encryption_with_csek_enabled/check.py](../../sources/gcp/compute_instance_encryption_with_csek_enabled/check.py)
- Source Metadata Path：`sources/gcp/compute_instance_encryption_with_csek_enabled/metadata.json`
- Source Code Path：`sources/gcp/compute_instance_encryption_with_csek_enabled/check.py`
