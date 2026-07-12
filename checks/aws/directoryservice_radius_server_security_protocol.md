# Directory Service directory RADIUS server uses MS-CHAPv2

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `directoryservice_radius_server_security_protocol` |
| クラウドプラットフォーム | AWS |
| サービス | directoryservice |
| 重大度 | medium |
| カテゴリ | identity-access |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Credential Access |
| リソースタイプ | Other |
| リソースグループ | IAM |

## 説明

AWS Directory Service RADIUS configuration uses the **authentication protocol** defined for MFA integration. The finding evaluates whether directories with RADIUS enabled are set to `MS-CHAPv2` instead of weaker options like `PAP`, `CHAP`, or `MS-CHAPv1`.

## リスク

Using `PAP`, `CHAP`, or `MS-CHAPv1` weakens RADIUS-based MFA. `PAP` exposes cleartext credentials, while legacy CHAP variants permit offline cracking and replay, enabling unauthorized access to AD-integrated services and lateral movement, degrading confidentiality and integrity.

## 推奨事項

Standardize on `MS-CHAPv2` for RADIUS authentication to MFA providers. Disable `PAP`, `CHAP`, and `MS-CHAPv1` to prevent downgrades. Apply least privilege and defense in depth: use strong shared secrets, restrict network access to RADIUS endpoints, and monitor authentication logs for anomalies.

## 修正手順


### CLI

```text
aws ds update-radius --directory-id <example_resource_id> --radius-settings AuthenticationProtocol=MS-CHAPv2
```

### Terraform

```hcl
resource "aws_directory_service_radius_settings" "<example_resource_name>" {
  directory_id  = "<example_resource_id>"
  radius_servers = ["<RADIUS_SERVER_IP>"]
  shared_secret  = "<SHARED_SECRET>"

  authentication_protocol = "MS-CHAPv2" # Critical: sets the RADIUS auth protocol to MS-CHAPv2 to pass the check
}
```

### Other

1. In the AWS Console, open Directory Service and select your directory
2. Open the Networking & security tab (Multi-factor authentication section)
3. Click Actions > Edit (or Enable)
4. Set Protocol to MS-CHAPv2
5. Click Save (or Enable) to apply

## 参考資料

- [https://docs.secureauth.com/0903/en/ms-chapv2-and-radius--sp-initiated--for-cisco-and-netscaler-configuration-guide.html](https://docs.secureauth.com/0903/en/ms-chapv2-and-radius--sp-initiated--for-cisco-and-netscaler-configuration-guide.html)
- [https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_mfa.html](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_mfa.html)
- [https://www.freeradius.org/documentation/freeradius-server/4.0~alpha1/raddb/mods-available/mschap.html](https://www.freeradius.org/documentation/freeradius-server/4.0~alpha1/raddb/mods-available/mschap.html)

## 技術情報

- Source Metadata：[sources/aws/directoryservice_radius_server_security_protocol/metadata.json](../../sources/aws/directoryservice_radius_server_security_protocol/metadata.json)
- Source Code：[sources/aws/directoryservice_radius_server_security_protocol/check.py](../../sources/aws/directoryservice_radius_server_security_protocol/check.py)
- Source Metadata Path：`sources/aws/directoryservice_radius_server_security_protocol/metadata.json`
- Source Code Path：`sources/aws/directoryservice_radius_server_security_protocol/check.py`
