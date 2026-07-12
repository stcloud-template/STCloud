# CloudFront distribution uses Origin Access Control (OAC) for all S3 origins

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudfront_distributions_s3_origin_access_control` |
| クラウドプラットフォーム | AWS |
| サービス | cloudfront |
| 重大度 | medium |
| カテゴリ | trust-boundaries |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exposure |
| リソースタイプ | AwsCloudFrontDistribution |
| リソースグループ | network |

## 説明

**CloudFront distributions** with **Amazon S3 origins** are expected to use **Origin Access Control** (`OAC`) on each S3 origin. The evaluation inspects distributions that include `s3_origin_config` and identifies S3 origins that lack an associated OAC.

## リスク

Without **OAC**, S3 objects can be reached outside CloudFront, bypassing edge controls and weakening **confidentiality** and **integrity**. - Direct access enables data exfiltration - Loss of WAF, rate-limiting, and detailed logging; cost abuse - Limited support for signed writes and **SSE-KMS**, increasing tampering risk

## 推奨事項

Enable **Origin Access Control** for all S3 origins and keep buckets non-public. Apply **least privilege**: scope bucket and key permissions to CloudFront and the intended distribution. Ensure origin requests are signed, migrate from legacy OAI, and use **defense in depth** with WAF and monitoring to protect and observe access.

## 修正手順


### CLI

```text
aws cloudfront create-origin-access-control --origin-access-control-config '{Name":"<example_resource_name>","SigningProtocol":"sigv4","SigningBehavior":"always","OriginAccessControlOriginType":"s3"}' && aws cloudfront get-distribution-config --id <DISTRIBUTION_ID> --output json > current-config.json && echo 'Manually edit current-config.json to add OriginAccessControlId to S3 origins, then run:' && echo 'aws cloudfront update-distribution --id <DISTRIBUTION_ID> --distribution-config file://current-config.json --if-match $(aws cloudfront get-distribution-config --id <DISTRIBUTION_ID> --query "ETag" --output text)'
```

### Native IaC

```yaml
# CloudFormation: attach OAC to S3 origin in a CloudFront distribution
Resources:
  ExampleOAC:
    Type: AWS::CloudFront::OriginAccessControl
    Properties:
      OriginAccessControlConfig:
        Name: <example_resource_name>
        OriginAccessControlOriginType: s3
        SigningBehavior: always
        SigningProtocol: sigv4

  ExampleDistribution:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        Enabled: true
        Origins:
          - Id: s3-<example_resource_id>
            DomainName: <example_bucket>.s3.amazonaws.com
            OriginAccessControlId: !Ref ExampleOAC  # CRITICAL: attaches OAC to the S3 origin to satisfy the check
            S3OriginConfig:
              OriginAccessIdentity: ""             # CRITICAL: disable OAI when using OAC
        DefaultCacheBehavior:
          TargetOriginId: s3-<example_resource_id>
          ViewerProtocolPolicy: redirect-to-https
          CachePolicyId: 658327ea-f89d-4fab-a63d-7e88639e58f6
```

### Terraform

```hcl
# Terraform: attach OAC to S3 origin in a CloudFront distribution
resource "aws_cloudfront_origin_access_control" "oac" {
  name                              = "<example_resource_name>"
  origin_access_control_origin_type = "s3"
  signing_behavior                  = "always"
  signing_protocol                  = "sigv4"
}

resource "aws_cloudfront_distribution" "dist" {
  enabled = true

  origin {
    domain_name = "<example_bucket>.s3.amazonaws.com"
    origin_id   = "s3-<example_resource_id>"

    origin_access_control_id = aws_cloudfront_origin_access_control.oac.id  # CRITICAL: attaches OAC to the S3 origin to satisfy the check

    s3_origin_config {
      origin_access_identity = ""  # CRITICAL: disable OAI when using OAC
    }
  }

  default_cache_behavior {
    target_origin_id       = "s3-<example_resource_id>"
    viewer_protocol_policy = "redirect-to-https"
    cache_policy_id        = "658327ea-f89d-4fab-a63d-7e88639e58f6"
  }
}
```

### Other

1. In the AWS Console, open CloudFront and go to Security > Origin access > Origin access control (OAC). Click Create control setting, choose Origin type S3, keep Sign requests, and create the OAC.
2. Open your CloudFront distribution, go to the Origins tab.
3. For each S3 origin: click Edit, select Origin access control settings (recommended), choose the OAC created in step 1, and Save changes.
4. Repeat step 3 for all S3 origins in the distribution.

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudFront/s3-origin.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudFront/s3-origin.html)
- [https://repost.aws/knowledge-center/cloudfront-access-to-amazon-s3](https://repost.aws/knowledge-center/cloudfront-access-to-amazon-s3)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/cloudfront-controls.html#cloudfront-13](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudfront-controls.html#cloudfront-13)
- [https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)

## 技術情報

- Source Metadata：[sources/aws/cloudfront_distributions_s3_origin_access_control/metadata.json](../../sources/aws/cloudfront_distributions_s3_origin_access_control/metadata.json)
- Source Code：[sources/aws/cloudfront_distributions_s3_origin_access_control/check.py](../../sources/aws/cloudfront_distributions_s3_origin_access_control/check.py)
- Source Metadata Path：`sources/aws/cloudfront_distributions_s3_origin_access_control/metadata.json`
- Source Code Path：`sources/aws/cloudfront_distributions_s3_origin_access_control/check.py`
