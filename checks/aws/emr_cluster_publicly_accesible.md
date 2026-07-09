# EMR cluster is not publicly accessible

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `emr_cluster_publicly_accesible` |
| 云平台 | AWS |
| 服务 | emr |
| 严重等级 | medium |
| 类别 | internet-exposed |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Initial Access |
| 资源类型 | Other |
| 资源组 | compute |

## 描述

**Amazon EMR clusters** are assessed for **public network exposure** by examining master and core/task node security groups for inbound rules that allow any source (`0.0.0.0/0` or `::/0`). Only active clusters are considered, and findings identify exposure via the specific security groups attached to the cluster nodes.

## 风险

**Open Internet ingress** to EMR nodes enables direct access to services and UIs, facilitating brute force, RCE, and data theft. Adversaries can pivot inside the VPC, alter jobs and outputs (**integrity**), exfiltrate datasets (**confidentiality**), or abuse compute for mining, degrading **availability**.

## 推荐措施

Apply **least privilege** and **defense in depth**: - Place clusters in private subnets; avoid public IPs - Deny `0.0.0.0/0` and `::/0` in node security groups; allow trusted CIDRs only - Keep EMR **Block Public Access** enabled with minimal exceptions - Use **bastion/SSM**, private connectivity, and logging for hardened access

## 修复步骤


### Native IaC

```yaml
# CloudFormation: Security Group without public ingress for EMR nodes
Resources:
  <example_resource_name>:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: SG for EMR without public access
      VpcId: <example_resource_id>
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 22
          ToPort: 22
          CidrIp: 10.0.0.0/8  # CRITICAL: restrict source; do not use 0.0.0.0/0 or ::/0 to avoid public access
```

### Terraform

```hcl
# Restrict EMR SG ingress to avoid 0.0.0.0/0 or ::/0
resource "aws_security_group_rule" "<example_resource_name>" {
  type              = "ingress"
  from_port         = 22
  to_port           = 22
  protocol          = "tcp"
  security_group_id = "<example_resource_id>"  # EMR master/core SG
  cidr_blocks       = ["10.0.0.0/8"]           # CRITICAL: restrict source; not 0.0.0.0/0 or ::/0
}
```

### Other

1. In AWS Console, go to EMR > Clusters and open the affected cluster
2. In the cluster details, note the Security Groups for Master and Core/Task under Network and security
3. Open the EC2 Console > Security Groups and select each noted group
4. Edit Inbound rules and remove any rule with Source 0.0.0.0/0 or ::/0
5. If access is required, re-add only from specific CIDR(s) you control, then Save

## 参考资料

- [https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-block-public-access.html](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-block-public-access.html)

## 技术信息

- Source Metadata：[sources/aws/emr_cluster_publicly_accesible/metadata.json](../../sources/aws/emr_cluster_publicly_accesible/metadata.json)
- Source Code：[sources/aws/emr_cluster_publicly_accesible/check.py](../../sources/aws/emr_cluster_publicly_accesible/check.py)
- Source Metadata Path：`sources/aws/emr_cluster_publicly_accesible/metadata.json`
- Source Code Path：`sources/aws/emr_cluster_publicly_accesible/check.py`
