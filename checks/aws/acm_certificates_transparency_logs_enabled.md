# ACM certificate is imported or has Certificate Transparency logging enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `acm_certificates_transparency_logs_enabled` |
| 云平台 | AWS |
| 服务 | acm |
| 严重等级 | medium |
| 类别 | logging |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices |
| 资源类型 | AwsCertificateManagerCertificate |
| 资源组 | security |

## 描述

**ACM-issued certificates** are checked for **Certificate Transparency (CT) logging** being enabled. Certificates with type `IMPORTED` are excluded from evaluation.

## 风险

Disabling **CT logging** reduces visibility into **misissued or rogue certificates**, weakening confidentiality and integrity. Attackers can **impersonate sites** or run **TLS man-in-the-middle** without timely detection. Unlogged public certs may be distrusted by browsers, impacting availability and user trust.

## 推荐措施

Enable **CT logging** on all ACM-issued public certificates to maintain transparency and rapid revocation. Monitor CT logs for your domains and alert on unexpected issuances. For sensitive internal names, favor private PKI or non-public hostnames instead of disabling CT, and apply **defense in depth** with short certificate lifetimes.

## 修复步骤


### CLI

```text
aws acm update-certificate-options --certificate-arn <CERTIFICATE_ARN> --options CertificateTransparencyLoggingPreference=ENABLED
```

### Native IaC

```yaml
# CloudFormation: Enable Certificate Transparency logging on an ACM certificate
Resources:
  <example_resource_name>:
    Type: AWS::CertificateManager::Certificate
    Properties:
      DomainName: <example_domain_name>
      CertificateTransparencyLoggingPreference: ENABLED  # Critical: turns on CT logging to pass the check
```

### Terraform

```hcl
# Enable Certificate Transparency logging on an ACM certificate
resource "aws_acm_certificate" "<example_resource_name>" {
  domain_name = "<example_domain_name>"
  options {
    certificate_transparency_logging_preference = "ENABLED"  # Critical: turns on CT logging to pass the check
  }
}
```

### Other

1. Open the AWS Certificate Manager (ACM) console
2. Select the certificate with transparency logging disabled
3. Click Actions > Edit transparency logging
4. Choose Enable transparency logging
5. Click Save

## 参考资料

- [https://aws.amazon.com/blogs/security/how-to-get-ready-for-certificate-transparency/](https://aws.amazon.com/blogs/security/how-to-get-ready-for-certificate-transparency/)
- [https://support.icompaas.com/support/solutions/articles/62000129491-ensure-acm-certificates-have-certificate-transparency-logging-enabled](https://support.icompaas.com/support/solutions/articles/62000129491-ensure-acm-certificates-have-certificate-transparency-logging-enabled)

## 技术信息

- Source Metadata：[sources/aws/acm_certificates_transparency_logs_enabled/metadata.json](../../sources/aws/acm_certificates_transparency_logs_enabled/metadata.json)
- Source Code：[sources/aws/acm_certificates_transparency_logs_enabled/check.py](../../sources/aws/acm_certificates_transparency_logs_enabled/check.py)
- Source Metadata Path：`sources/aws/acm_certificates_transparency_logs_enabled/metadata.json`
- Source Code Path：`sources/aws/acm_certificates_transparency_logs_enabled/check.py`
