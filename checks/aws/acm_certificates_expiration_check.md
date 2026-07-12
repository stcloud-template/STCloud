# ACM certificate expires in more than the configured threshold of days

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `acm_certificates_expiration_check` |
| クラウドプラットフォーム | AWS |
| サービス | acm |
| 重大度 | high |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Denial of Service |
| リソースタイプ | AwsCertificateManagerCertificate |
| リソースグループ | security |

## 説明

**ACM certificates** are assessed for **time to expiration** against a configurable threshold. Certificates close to end of validity or already expired are surfaced, covering those attached to services and, *if in scope*, unused ones.

## リスク

Expired or near-expiry **TLS certificates** can break handshakes, causing **service outages** and failed API calls (**availability**). Emergency fixes raise misconfiguration risk, enabling disabled verification or weak ciphers, which allows **MITM** and data exposure (**confidentiality**/**integrity**).

## 推奨事項

Adopt **automated certificate lifecycle management**: prefer **ACM-issued certs with auto-renewal**, or integrate imports with an automated renewal/rotation pipeline. Track expirations with alerts, enforce **least privilege** for cert operations, remove unused certs, and test rollovers to avoid downtime.

## 修正手順


### Other

1. In the AWS Console, open Certificate Manager (ACM)
2. If the expiring certificate is ACM-issued: select it and complete/restore validation (Create records in Route 53 or add the shown CNAME) so renewal can proceed
3. If the expiring certificate is imported: click Import a certificate, upload the new certificate and private key, then save
4. Update the service to use the new/renewed certificate:
   - ALB/NLB: EC2 > Load Balancers > Listeners > Edit > Change certificate to the new ACM certificate
   - CloudFront: Distributions > Edit > Viewer certificate > Select the new ACM certificate
   - API Gateway: Custom domain names > Edit > Choose the new ACM certificate
5. Verify the old certificate is no longer in use; delete it if not needed

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ACM/certificate-expires-in-45-days.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ACM/certificate-expires-in-45-days.html)
- [https://repost.aws/es/knowledge-center/acm-notification-certificate-renewal](https://repost.aws/es/knowledge-center/acm-notification-certificate-renewal)
- [https://docs.aws.amazon.com/config/latest/developerguide/acm-certificate-expiration-check.html](https://docs.aws.amazon.com/config/latest/developerguide/acm-certificate-expiration-check.html)
- [https://repost.aws/questions/QU3sMaeZPMRo2kLcsfJsfuVA/acm-notifications-for-expiring-certificates](https://repost.aws/questions/QU3sMaeZPMRo2kLcsfJsfuVA/acm-notifications-for-expiring-certificates)

## 技術情報

- Source Metadata：[sources/aws/acm_certificates_expiration_check/metadata.json](../../sources/aws/acm_certificates_expiration_check/metadata.json)
- Source Code：[sources/aws/acm_certificates_expiration_check/check.py](../../sources/aws/acm_certificates_expiration_check/check.py)
- Source Metadata Path：`sources/aws/acm_certificates_expiration_check/metadata.json`
- Source Code Path：`sources/aws/acm_certificates_expiration_check/check.py`
