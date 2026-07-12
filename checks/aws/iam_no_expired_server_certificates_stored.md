# Ensure that all the expired SSL/TLS certificates stored in AWS IAM are removed.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_no_expired_server_certificates_stored` |
| クラウドプラットフォーム | AWS |
| サービス | iam |
| 重大度 | critical |
| カテゴリ | encryption |
| チェックタイプ | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| リソースタイプ | Other |
| リソースグループ | IAM |

## 説明

Ensure that all the expired SSL/TLS certificates stored in AWS IAM are removed.

## リスク

Removing expired SSL/TLS certificates eliminates the risk that an invalid certificate will be deployed accidentally to a resource such as AWS Elastic Load Balancer (ELB), which can damage the credibility of the application/website behind the ELB.

## 推奨事項

Deleting the certificate could have implications for your application if you are using an expired server certificate with Elastic Load Balancing, CloudFront, etc. One has to make configurations at respective services to ensure there is no interruption in application functionality.

- 推奨リンク：[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html)

## 修正手順


### CLI

```text
aws iam delete-server-certificate --server-certificate-name <CERTIFICATE_NAME
```

### Other

Removing expired certificates via AWS Management Console is not currently supported.

## 参考資料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html)

## 技術情報

- Source Metadata：[sources/aws/iam_no_expired_server_certificates_stored/metadata.json](../../sources/aws/iam_no_expired_server_certificates_stored/metadata.json)
- Source Code：[sources/aws/iam_no_expired_server_certificates_stored/check.py](../../sources/aws/iam_no_expired_server_certificates_stored/check.py)
- Source Metadata Path：`sources/aws/iam_no_expired_server_certificates_stored/metadata.json`
- Source Code Path：`sources/aws/iam_no_expired_server_certificates_stored/check.py`
