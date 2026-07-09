# Ensure that model invocation logging is enabled for Amazon Bedrock.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `bedrock_model_invocation_logging_enabled` |
| 云平台 | AWS |
| 服务 | bedrock |
| 严重等级 | medium |
| 类别 | logging, forensics-ready, gen-ai |
| 资源类型 | Other |
| 资源组 | ai_ml |

## 描述

Ensure that model invocation logging is enabled for Amazon Bedrock service in order to collect metadata, requests, and responses for all model invocations in your AWS cloud account.

## 风险

In Amazon Bedrock, model invocation logging enables you to collect the invocation request and response data, along with metadata, for all 'Converse', 'ConverseStream', 'InvokeModel', and 'InvokeModelWithResponseStream' API calls in your AWS account. Each log entry includes important details such as the timestamp, request ID, model ID, and token usage. Invocation logs can be utilized for troubleshooting, performance enhancements, abuse detection, and security auditing. By default, model invocation logging is disabled.

## 推荐措施

Enable model invocation logging for Amazon Bedrock service in order to collect metadata, requests, and responses for all model invocations in your AWS cloud account.

- 推荐链接：[https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html#model-invocation-logging-console](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html#model-invocation-logging-console)

## 修复步骤


### CLI

```text
aws bedrock put-model-invocation-logging-configuration --logging-config 's3Config={bucketName='tm-bedrock-logging-data',keyPrefix='invocation-logs'},textDataDeliveryEnabled=true,imageDataDeliveryEnabled=true,embeddingDataDeliveryEnabled=true'
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Bedrock/enable-model-invocation-logging.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Bedrock/enable-model-invocation-logging.html)

## 参考资料

- [https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html)
- [https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html#model-invocation-logging-console](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html#model-invocation-logging-console)

## 技术信息

- Source Metadata：[sources/aws/bedrock_model_invocation_logging_enabled/metadata.json](../../sources/aws/bedrock_model_invocation_logging_enabled/metadata.json)
- Source Code：[sources/aws/bedrock_model_invocation_logging_enabled/check.py](../../sources/aws/bedrock_model_invocation_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/bedrock_model_invocation_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/bedrock_model_invocation_logging_enabled/check.py`
