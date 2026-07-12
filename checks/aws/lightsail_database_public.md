# Lightsail database public access disabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `lightsail_database_public` |
| クラウドプラットフォーム | AWS |
| サービス | lightsail |
| 重大度 | high |
| カテゴリ | internet-exposed |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exposure, TTPs/Initial Access |
| リソースタイプ | Other |
| リソースグループ | compute |

## 説明

**Lightsail managed database** is evaluated for **public accessibility**. When `public mode` is enabled, the database accepts connections from the Internet using its endpoint and port; otherwise, access is limited to authorized Lightsail resources.

## リスク

**Publicly reachable databases** expose confidential data and credentials to the Internet, enabling: - **Brute-force** and credential stuffing - **Data exfiltration** via unauthorized queries - **Service disruption** from scanning or DoS Compromise enables **lateral movement** and tampering, impacting confidentiality, integrity, and availability.

## 推奨事項

Disable **public mode** and keep the database reachable only from trusted, private networks. - Enforce **least privilege** and network segmentation - Use bastion hosts, tunnels, or private endpoints for admin access - If exposure is unavoidable, restrict by IP, rotate credentials, and monitor connections for **defense in depth**

## 修正手順


### CLI

```text
aws lightsail update-relational-database --relational-database-name <example_resource_name> --no-publicly-accessible
```

### Native IaC

```yaml
# CloudFormation: disable public access on an existing Lightsail database
Resources:
  <example_resource_name>:
    Type: AWS::Lightsail::Database
    Properties:
      RelationalDatabaseName: <example_resource_name>
      PubliclyAccessible: false  # Critical: turns off public mode so the database is not publicly accessible
```

### Terraform

```hcl
# Disable public access for a Lightsail database
resource "aws_lightsail_database" "<example_resource_name>" {
  name                 = "<example_resource_name>"
  availability_zone    = "<availability_zone>"
  blueprint_id         = "<blueprint_id>"
  bundle_id            = "<bundle_id>"
  master_database_name = "<master_database_name>"
  master_username      = "<master_username>"
  master_password      = "<master_password>"

  publicly_accessible = false  # Critical: ensures the database is not publicly accessible
}
```

### Other

1. In the AWS Console, go to Lightsail > Databases
2. Select <example_resource_name>
3. Open the Networking tab
4. In Public mode, toggle Off
5. Wait until status returns to Available

## 参考資料

- [https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-databases.html](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-databases.html)
- [https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-database-public-mode.html](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-database-public-mode.html)
- [https://spinupwp.com/doc/external-database-amazon-lightsail/](https://spinupwp.com/doc/external-database-amazon-lightsail/)

## 技術情報

- Source Metadata：[sources/aws/lightsail_database_public/metadata.json](../../sources/aws/lightsail_database_public/metadata.json)
- Source Code：[sources/aws/lightsail_database_public/check.py](../../sources/aws/lightsail_database_public/check.py)
- Source Metadata Path：`sources/aws/lightsail_database_public/metadata.json`
- Source Code Path：`sources/aws/lightsail_database_public/check.py`
