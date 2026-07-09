# EMR account has Block Public Access enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `emr_cluster_account_public_block_enabled` |
| 云平台 | AWS |
| 服务 | emr |
| 严重等级 | high |
| 类别 | internet-exposed |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | Other |
| 资源组 | compute |

## 描述

Amazon EMR account-level **Block Public Access** configuration is assessed per Region. When `BlockPublicSecurityGroupRules` is enabled, clusters cannot use security groups that allow inbound public sources (`0.0.0.0/0`, `::/0`) except on permitted ports.

## 风险

Public EMR-facing rules enable Internet reachability to cluster nodes and UIs, inviting brute force and remote exploits. Attackers can exfiltrate job data, alter processing, or pivot into the VPC, degrading **confidentiality**, **integrity**, and **availability** through data theft, tampering, and service disruption.

## 推荐措施

Keep EMR **Block Public Access** enabled and minimize exceptions; allow only required ports and restrict sources. Apply **least privilege** on security groups, place clusters in private subnets, and use bastion hosts or Session Manager. Combine with **VPC** controls and monitoring for **defense in depth**.

## 修复步骤


### CLI

```text
aws emr put-block-public-access-configuration --block-public-access-configuration BlockPublicSecurityGroupRules=true
```

### Native IaC

```yaml
# CloudFormation: Enable EMR Block Public Access (account/Region level)
Resources:
  EmrBpaRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: lambda.amazonaws.com
            Action: sts:AssumeRole
      Policies:
        - PolicyName: EmrBpaPut
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Action: elasticmapreduce:PutBlockPublicAccessConfiguration
                Resource: "*"

  EmrBpaFunction:
    Type: AWS::Lambda::Function
    Properties:
      Role: !GetAtt EmrBpaRole.Arn
      Runtime: python3.12
      Handler: index.handler
      Code:
        ZipFile: |
          import boto3, json, urllib.request
          def handler(event, context):
              try:
                  boto3.client('emr').put_block_public_access_configuration(
                      BlockPublicAccessConfiguration={
                          'BlockPublicSecurityGroupRules': True  # CRITICAL: enables EMR Block Public Access
                      }
                  )
                  status='SUCCESS'
              except Exception:
                  status='FAILED'
              body=json.dumps({
                  'Status': status,
                  'PhysicalResourceId': 'EmrBPA',  # respond to CFN
                  'StackId': event['StackId'],
                  'RequestId': event['RequestId'],
                  'LogicalResourceId': event['LogicalResourceId']
              }).encode()
              req=urllib.request.Request(event['ResponseURL'], data=body, method='PUT')
              req.add_header('content-type','')
              req.add_header('content-length',str(len(body)))
              urllib.request.urlopen(req)

  EmrBpa:
    Type: Custom::EmrBpa
    Properties:
      ServiceToken: !GetAtt EmrBpaFunction.Arn  # Invokes Lambda to apply the setting
```

### Terraform

```hcl
# Enable EMR Block Public Access (account/Region level)
resource "aws_emr_block_public_access_configuration" "example_resource_name" {
  block_public_security_group_rules = true  # CRITICAL: enables Block Public Access
}
```

### Other

1. In the AWS Console, go to Amazon EMR
2. Select the target Region (top-right)
3. In the left menu under "EMR on EC2", click "Block public access"
4. Click "Edit" and choose "Turn on"
5. Click "Save"

## 参考资料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/EMR/block-public-access.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/EMR/block-public-access.html)
- [https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-block-public-access.html](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-block-public-access.html)
- [https://github.com/cloudmatos/matos/tree/master/remediations/aws/emr/block-emr-public-access](https://github.com/cloudmatos/matos/tree/master/remediations/aws/emr/block-emr-public-access)

## 技术信息

- Source Metadata：[sources/aws/emr_cluster_account_public_block_enabled/metadata.json](../../sources/aws/emr_cluster_account_public_block_enabled/metadata.json)
- Source Code：[sources/aws/emr_cluster_account_public_block_enabled/check.py](../../sources/aws/emr_cluster_account_public_block_enabled/check.py)
- Source Metadata Path：`sources/aws/emr_cluster_account_public_block_enabled/metadata.json`
- Source Code Path：`sources/aws/emr_cluster_account_public_block_enabled/check.py`
