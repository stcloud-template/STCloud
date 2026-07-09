# Transfer Family server has encryption in transit enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `transfer_server_in_transit_encryption_enabled` |
| 云平台 | AWS |
| 服务 | transfer |
| 严重等级 | high |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls, Software and Configuration Checks/Industry and Regulatory Standards/PCI-DSS, Software and Configuration Checks/Industry and Regulatory Standards/HIPAA Controls (USA), Effects/Data Exposure |
| 资源类型 | Other |
| 资源组 | storage |

## 描述

**AWS Transfer Family servers** are evaluated for presence of the unencrypted `FTP` protocol among enabled protocols, as opposed to encrypted options like SFTP, FTPS, or AS2.

## 风险

Allowing **FTP** exposes credentials and file contents in cleartext, breaking confidentiality. Adversaries can sniff or perform **MITM** to read or alter files, compromising integrity and enabling credential theft that can be reused for broader unauthorized access.

## 推荐措施

Remove `FTP`; permit only **SFTP**, **FTPS**, or **AS2** to enforce **encryption in transit**. Apply defense in depth: restrict by network location (allowlists/VPC), enforce strong cryptographic policies, and use least-privilege roles with monitoring.

## 修复步骤


### CLI

```text
aws transfer update-server --server-id <server-id> --protocols SFTP
```

### Native IaC

```yaml
# CloudFormation: ensure FTP is not enabled
Resources:
  <example_resource_name>:
    Type: AWS::Transfer::Server
    Properties:
      Protocols:
        - SFTP  # CRITICAL: Use SFTP only; excludes FTP (unencrypted)
```

### Terraform

```hcl
# Ensure FTP is not enabled
resource "aws_transfer_server" "<example_resource_name>" {
  protocols = ["SFTP"]  # CRITICAL: Excludes FTP to enforce encryption in transit
}
```

### Other

1. Open AWS Console > AWS Transfer Family
2. Go to Servers and select the server (<example_resource_id>)
3. Click Edit next to Protocols
4. Uncheck FTP and ensure at least SFTP (or FTPS/AS2) is selected
5. Save

## 参考资料

- [https://docs.aws.amazon.com/config/latest/developerguide/transfer-family-server-no-ftp.html](https://docs.aws.amazon.com/config/latest/developerguide/transfer-family-server-no-ftp.html)
- [https://docs.aws.amazon.com/transfer/latest/userguide/edit-server-config.html#edit-protocols](https://docs.aws.amazon.com/transfer/latest/userguide/edit-server-config.html#edit-protocols)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/transfer-controls.html#transfer-2](https://docs.aws.amazon.com/securityhub/latest/userguide/transfer-controls.html#transfer-2)

## 技术信息

- Source Metadata：[sources/aws/transfer_server_in_transit_encryption_enabled/metadata.json](../../sources/aws/transfer_server_in_transit_encryption_enabled/metadata.json)
- Source Code：[sources/aws/transfer_server_in_transit_encryption_enabled/check.py](../../sources/aws/transfer_server_in_transit_encryption_enabled/check.py)
- Source Metadata Path：`sources/aws/transfer_server_in_transit_encryption_enabled/metadata.json`
- Source Code Path：`sources/aws/transfer_server_in_transit_encryption_enabled/check.py`
