# Ensure that all the expired SSL/TLS certificates stored in AWS IAM are removed.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_no_expired_server_certificates_stored` |
| 云平台 | AWS |
| 服务 | iam |
| 严重等级 | critical |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| 资源类型 | Other |
| 资源组 | IAM |

## 描述

Ensure that all the expired SSL/TLS certificates stored in AWS IAM are removed.

## 风险

Removing expired SSL/TLS certificates eliminates the risk that an invalid certificate will be deployed accidentally to a resource such as AWS Elastic Load Balancer (ELB), which can damage the credibility of the application/website behind the ELB.

## 推荐措施

Deleting the certificate could have implications for your application if you are using an expired server certificate with Elastic Load Balancing, CloudFront, etc. One has to make configurations at respective services to ensure there is no interruption in application functionality.

- 推荐链接：[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html)

## 修复步骤


### CLI

```text
aws iam delete-server-certificate --server-certificate-name <CERTIFICATE_NAME
```

### Other

Removing expired certificates via AWS Management Console is not currently supported.

## 参考资料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html)

## 技术信息

- Source Metadata：[sources/aws/iam_no_expired_server_certificates_stored/metadata.json](../../sources/aws/iam_no_expired_server_certificates_stored/metadata.json)
- Source Code：[sources/aws/iam_no_expired_server_certificates_stored/check.py](../../sources/aws/iam_no_expired_server_certificates_stored/check.py)
- Source Metadata Path：`sources/aws/iam_no_expired_server_certificates_stored/metadata.json`
- Source Code Path：`sources/aws/iam_no_expired_server_certificates_stored/check.py`
