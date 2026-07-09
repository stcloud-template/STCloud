# Directory Service LDAP certificate expires in more than 90 days

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `directoryservice_ldap_certificate_expiration` |
| 云平台 | AWS |
| 服务 | directoryservice |
| 严重等级 | medium |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | Other |
| 资源组 | IAM |

## 描述

**AWS Directory Service** Secure LDAP (LDAPS) certificates are assessed for upcoming expiration by comparing each directory's certificate expiration to the current time and identifying those with `<= 90` days remaining.

## 风险

Expired LDAPS certificates cause TLS handshakes to fail, blocking directory binds and queries and disrupting authentication and app integrations (availability). If clients fall back to plain LDAP, credentials and directory data can be intercepted or altered (confidentiality and integrity).

## 推荐措施

Adopt certificate lifecycle management: inventory LDAPS certificates, alert well before expiry, and automate renewal with staged rollout and overlap. Enforce TLS-only LDAP and disable plaintext fallback. Apply **least privilege** and **separation of duties** to certificate issuance and deployment.

## 修复步骤


### CLI

```text
aws ds register-certificate --directory-id <DIRECTORY_ID> --certificate-data file://certificate.pem
```

### Other

1. In the AWS Console, open Directory Service and select your AWS Managed Microsoft AD (<example_resource_id>)
2. Go to Networking & security > Secure LDAP
3. Click Edit (Manage certificate)
4. Choose Replace certificate (or Upload certificate)
5. Upload a new LDAPS server certificate with private key from a trusted CA (valid for >90 days); enter the password if using a .pfx
6. Save and wait until the certificate status is Active

## 参考资料

- [https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_ldap.html](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_ldap.html)
- [https://support.icompaas.com/support/solutions/articles/62000229587-ensure-to-monitor-directory-service-ldap-certificates-expiration](https://support.icompaas.com/support/solutions/articles/62000229587-ensure-to-monitor-directory-service-ldap-certificates-expiration)

## 技术信息

- Source Metadata：[sources/aws/directoryservice_ldap_certificate_expiration/metadata.json](../../sources/aws/directoryservice_ldap_certificate_expiration/metadata.json)
- Source Code：[sources/aws/directoryservice_ldap_certificate_expiration/check.py](../../sources/aws/directoryservice_ldap_certificate_expiration/check.py)
- Source Metadata Path：`sources/aws/directoryservice_ldap_certificate_expiration/metadata.json`
- Source Code Path：`sources/aws/directoryservice_ldap_certificate_expiration/check.py`
