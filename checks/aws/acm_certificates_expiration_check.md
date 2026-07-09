# ACM certificate expires in more than the configured threshold of days

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `acm_certificates_expiration_check` |
| 云平台 | AWS |
| 服务 | acm |
| 严重等级 | high |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Denial of Service |
| 资源类型 | AwsCertificateManagerCertificate |
| 资源组 | security |

## 描述

**ACM certificates** are assessed for **time to expiration** against a configurable threshold. Certificates close to end of validity or already expired are surfaced, covering those attached to services and, *if in scope*, unused ones.

## 风险

Expired or near-expiry **TLS certificates** can break handshakes, causing **service outages** and failed API calls (**availability**). Emergency fixes raise misconfiguration risk, enabling disabled verification or weak ciphers, which allows **MITM** and data exposure (**confidentiality**/**integrity**).

## 推荐措施

Adopt **automated certificate lifecycle management**: prefer **ACM-issued certs with auto-renewal**, or integrate imports with an automated renewal/rotation pipeline. Track expirations with alerts, enforce **least privilege** for cert operations, remove unused certs, and test rollovers to avoid downtime.

## 修复步骤


### Other

1. In the AWS Console, open Certificate Manager (ACM)
2. If the expiring certificate is ACM-issued: select it and complete/restore validation (Create records in Route 53 or add the shown CNAME) so renewal can proceed
3. If the expiring certificate is imported: click Import a certificate, upload the new certificate and private key, then save
4. Update the service to use the new/renewed certificate:
   - ALB/NLB: EC2 > Load Balancers > Listeners > Edit > Change certificate to the new ACM certificate
   - CloudFront: Distributions > Edit > Viewer certificate > Select the new ACM certificate
   - API Gateway: Custom domain names > Edit > Choose the new ACM certificate
5. Verify the old certificate is no longer in use; delete it if not needed

## 参考资料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ACM/certificate-expires-in-45-days.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ACM/certificate-expires-in-45-days.html)
- [https://repost.aws/es/knowledge-center/acm-notification-certificate-renewal](https://repost.aws/es/knowledge-center/acm-notification-certificate-renewal)
- [https://docs.aws.amazon.com/config/latest/developerguide/acm-certificate-expiration-check.html](https://docs.aws.amazon.com/config/latest/developerguide/acm-certificate-expiration-check.html)
- [https://repost.aws/questions/QU3sMaeZPMRo2kLcsfJsfuVA/acm-notifications-for-expiring-certificates](https://repost.aws/questions/QU3sMaeZPMRo2kLcsfJsfuVA/acm-notifications-for-expiring-certificates)

## 技术信息

- Source Metadata：[sources/aws/acm_certificates_expiration_check/metadata.json](../../sources/aws/acm_certificates_expiration_check/metadata.json)
- Source Code：[sources/aws/acm_certificates_expiration_check/check.py](../../sources/aws/acm_certificates_expiration_check/check.py)
- Source Metadata Path：`sources/aws/acm_certificates_expiration_check/metadata.json`
- Source Code Path：`sources/aws/acm_certificates_expiration_check/check.py`
