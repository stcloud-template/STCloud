# ACM certificate uses a secure key algorithm

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `acm_certificates_with_secure_key_algorithms` |
| 云平台 | AWS |
| 服务 | acm |
| 严重等级 | high |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/PCI-DSS, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls (USA) |
| 资源类型 | AwsCertificateManagerCertificate |
| 资源组 | security |

## 描述

**ACM certificates** are evaluated for the **public key algorithm and size**, identifying those that use weak parameters such as `RSA-1024` or ECDSA `P-192`. Certificates using `RSA-2048+` or ECDSA `P-256+` meet the secure baseline.

## 风险

**Weak certificate keys** reduce TLS confidentiality and authenticity. Feasible factoring or discrete log attacks can reveal private keys, enabling **man-in-the-middle**, session decryption, and **certificate spoofing**, leading to data exposure and tampering.

## 推荐措施

Use **strong algorithms**: `RSA-2048+` or ECDSA `P-256/P-384`. Replace weak or legacy certificates and prevent their use via policy. Prefer ECDSA where compatible, apply **least privilege** to private keys, enforce modern TLS policies, and automate renewal to maintain cryptographic strength.

## 修复步骤


### Native IaC

```yaml
# CloudFormation: ACM certificate with secure key algorithm
Resources:
  <example_resource_name>:
    Type: AWS::CertificateManager::Certificate
    Properties:
      DomainName: <example_domain>
      KeyAlgorithm: EC_prime256v1  # CRITICAL: ensures a secure key algorithm (RSA-2048+ or ECDSA P-256+)
```

### Terraform

```hcl
# Terraform: ACM certificate with secure key algorithm
resource "aws_acm_certificate" "<example_resource_name>" {
  domain_name   = "<example_domain>"
  key_algorithm = "EC_prime256v1"  # CRITICAL: ensures a secure key algorithm (RSA-2048+ or ECDSA P-256+)
}
```

### Other

1. In the AWS Console, go to Certificate Manager (ACM)
2. Click Request a certificate and enter <example_domain>
3. Under Key algorithm, select ECDSA P-256 (or RSA 2048)
4. Complete validation (DNS is recommended)
5. In the service using the certificate (e.g., ALB/CloudFront/API Gateway), replace the old certificate with the new one
6. Delete the insecure certificate (e.g., RSA-1024 or P-192) once no longer in use.

## 参考资料

- [https://noise.getoto.net/2022/11/08/how-to-evaluate-and-use-ecdsa-certificates-in-aws-certificate-manager/](https://noise.getoto.net/2022/11/08/how-to-evaluate-and-use-ecdsa-certificates-in-aws-certificate-manager/)
- [https://docs.aws.amazon.com/acm/latest/userguide/data-protection.html](https://docs.aws.amazon.com/acm/latest/userguide/data-protection.html)

## 技术信息

- Source Metadata：[sources/aws/acm_certificates_with_secure_key_algorithms/metadata.json](../../sources/aws/acm_certificates_with_secure_key_algorithms/metadata.json)
- Source Code：[sources/aws/acm_certificates_with_secure_key_algorithms/check.py](../../sources/aws/acm_certificates_with_secure_key_algorithms/check.py)
- Source Metadata Path：`sources/aws/acm_certificates_with_secure_key_algorithms/metadata.json`
- Source Code Path：`sources/aws/acm_certificates_with_secure_key_algorithms/check.py`
