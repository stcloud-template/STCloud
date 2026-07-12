# No potential LLM jacking activity detected in CloudTrail

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudtrail_threat_detection_llm_jacking` |
| クラウドプラットフォーム | AWS |
| サービス | cloudtrail |
| 重大度 | critical |
| カテゴリ | threat-detection, gen-ai |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis, TTPs/Discovery, TTPs/Execution, TTPs/Defense Evasion, Effects/Resource Consumption, Unusual Behaviors/User |
| リソースタイプ | AwsCloudTrailTrail |
| リソースグループ | monitoring |

## 説明

**CloudTrail Bedrock activity** is analyzed per identity for a high diversity of LLM-related API calls (e.g., `InvokeModel`, `InvokeModelWithResponseStream`, `GetFoundationModelAvailability`). *If an identity's share of these actions exceeds a configured threshold over a recent window*, it is surfaced as potential **LLM-jacking** behavior.

## リスク

Such patterns suggest **stolen credential** abuse to drive LLM usage. - Availability: cost exhaustion and service disruption - Confidentiality: leakage of prompts/outputs and model settings - Integrity: misuse of permissions for broader access Attackers may use reverse proxies to resell access and obfuscate sources.

## 推奨事項

Apply **least privilege** to Bedrock; restrict `Invoke*` only to required roles and deny broadly via **SCPs** where unused. Enforce **MFA** and short-lived creds; rotate/remove exposed keys. Enable **model invocation logging** and budgets/quotas. Continuously monitor for Bedrock enumeration plus invoke bursts. Use **defense in depth** across identities and networks.

## 修正手順


### Native IaC

```yaml
# CloudFormation SCP that blocks all Amazon Bedrock actions to stop LLM jacking
Resources:
  <example_resource_name>:
    Type: AWS::Organizations::Policy
    Properties:
      Name: <example_resource_name>
      Type: SERVICE_CONTROL_POLICY
      TargetIds:
        - "<example_resource_id>"  # CRITICAL: Attach SCP to the root/OU/account to enforce the deny
      Content:
        Version: "2012-10-17"
        Statement:
          - Sid: DenyBedrock
            Effect: Deny
            Action: "bedrock:*"  # CRITICAL: Denies all Bedrock APIs (Invoke/Converse/list/entitlements/etc.)
            Resource: "*"        # CRITICAL: Apply deny to all resources
```

### Terraform

```hcl
# SCP denying all Amazon Bedrock actions; attach it to the root/OU/account to halt LLM jacking
resource "aws_organizations_policy" "main" {
  name = "<example_resource_name>"
  type = "SERVICE_CONTROL_POLICY"

  content = jsonencode({
    Version   = "2012-10-17"
    Statement = [{
      Sid      = "DenyBedrock"
      Effect   = "Deny"
      Action   = "bedrock:*"   // CRITICAL: blocks all Bedrock APIs (prevents further suspicious activity)
      Resource = "*"            // CRITICAL: deny across all resources
    }]
  })
}

resource "aws_organizations_policy_attachment" "attach" {
  policy_id = aws_organizations_policy.main.id
  target_id = "<example_resource_id>"  // CRITICAL: attach to the affected account/OU/root to enforce the deny
}
```

### Other

1. In the AWS Console, go to Organizations > Policies > Service control policies
2. Click Create policy
3. Set Name to <example_resource_name>
4. In Policy, paste a deny for Bedrock:
   {
     "Version": "2012-10-17",
     "Statement": [{"Sid":"DenyBedrock","Effect":"Deny","Action":"bedrock:*","Resource":"*"}]
   }
5. Save the policy and click Attach
6. Select the target (Root, OU, or the affected account ID <example_resource_id>) and attach the policy
7. Wait for propagation; no further Bedrock calls will occur, and the finding will clear after the detection window elapses

## 参考資料

- [https://furkangungor.medium.com/automating-anomaly-detection-in-aws-cloudtrail-logs-4efb2ad9b958](https://furkangungor.medium.com/automating-anomaly-detection-in-aws-cloudtrail-logs-4efb2ad9b958)
- [https://help.sumologic.com/docs/integrations/amazon-aws/amazon-bedrock/](https://help.sumologic.com/docs/integrations/amazon-aws/amazon-bedrock/)
- [https://dzone.com/articles/ai-powered-aws-cloudtrail-analysis-strands-agent-bedrock](https://dzone.com/articles/ai-powered-aws-cloudtrail-analysis-strands-agent-bedrock)

## 技術情報

- Source Metadata：[sources/aws/cloudtrail_threat_detection_llm_jacking/metadata.json](../../sources/aws/cloudtrail_threat_detection_llm_jacking/metadata.json)
- Source Code：[sources/aws/cloudtrail_threat_detection_llm_jacking/check.py](../../sources/aws/cloudtrail_threat_detection_llm_jacking/check.py)
- Source Metadata Path：`sources/aws/cloudtrail_threat_detection_llm_jacking/metadata.json`
- Source Code Path：`sources/aws/cloudtrail_threat_detection_llm_jacking/check.py`
