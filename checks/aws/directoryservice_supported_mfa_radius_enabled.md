# AWS Directory Service directory has RADIUS-based MFA enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `directoryservice_supported_mfa_radius_enabled` |
| 云平台 | AWS |
| 服务 | directoryservice |
| 严重等级 | medium |
| 类别 | identity-access |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Initial Access, TTPs/Credential Access |
| 资源类型 | Other |
| 资源组 | IAM |

## 描述

**AWS Directory Service directories** are evaluated for **RADIUS-backed multi-factor authentication**, confirming that MFA is configured and the RADIUS integration is active.

## 风险

Without **RADIUS MFA**, directory-based sign-ins to AWS-integrated services rely on a single factor, enabling credential stuffing and phishing to succeed. Compromised passwords can grant unauthorized access, drive data exfiltration, and enable privilege escalation, undermining confidentiality and integrity.

## 推荐措施

Enable and enforce **RADIUS-based MFA** for all Directory Service authentications. Apply **least privilege**, harden and monitor the RADIUS infrastructure, rotate shared secrets, and restrict network access (e.g., `UDP/1812`). Use **defense in depth** with segmentation and session controls to limit lateral movement and reduce blast radius.

## 修复步骤


### CLI

```text
aws ds enable-radius --directory-id <example_resource_id> --radius-settings '{"RadiusServers":["<RADIUS_IP_OR_DNS>"],"SharedSecret":"<SHARED_SECRET>"}'
```

### Terraform

```hcl
resource "aws_directory_service_radius_settings" "<example_resource_name>" {
  directory_id  = "<example_resource_id>"            # Directory to enable RADIUS MFA on
  radius_servers = ["<RADIUS_IP_OR_DNS>"]             # Critical: RADIUS server endpoint(s)
  shared_secret  = "<SHARED_SECRET>"                   # Critical: Shared secret for RADIUS
}
```

### Other

1. Sign in to the AWS Console and open Directory Service
2. Select your directory and open it
3. Go to the Networking & security tab
4. In Multi-factor authentication, click Actions > Enable
5. Enter RADIUS server IP(s) and the Shared secret, then click Enable
6. Wait until the RADIUS status shows Completed

## 参考资料

- [https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_mfa.html](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_mfa.html)
- [https://support.icompaas.com/support/solutions/articles/62000233537-ensure-multi-factor-authentication-mfa-using-a-radius-server-is-enabled-in-directory-service](https://support.icompaas.com/support/solutions/articles/62000233537-ensure-multi-factor-authentication-mfa-using-a-radius-server-is-enabled-in-directory-service)

## 技术信息

- Source Metadata：[sources/aws/directoryservice_supported_mfa_radius_enabled/metadata.json](../../sources/aws/directoryservice_supported_mfa_radius_enabled/metadata.json)
- Source Code：[sources/aws/directoryservice_supported_mfa_radius_enabled/check.py](../../sources/aws/directoryservice_supported_mfa_radius_enabled/check.py)
- Source Metadata Path：`sources/aws/directoryservice_supported_mfa_radius_enabled/metadata.json`
- Source Code Path：`sources/aws/directoryservice_supported_mfa_radius_enabled/check.py`
