# Enable Just-In-Time Access for Virtual Machines

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `vm_jit_access_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | vm |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.Compute/virtualMachines |
| リソースグループ | compute |

## 説明

Ensure that Microsoft Azure virtual machines are configured to use Just-in-Time (JIT) access.

## リスク

Without JIT access, management ports such as 22 (SSH) and 3389 (RDP) may be exposed, increasing the risk of brute-force and DDoS attacks.

## 推奨事項

Enable Just-in-Time (JIT) network access for your Microsoft Azure virtual machines using the Azure Portal under Security Center > Just-in-time VM access.

- 推奨リンク：[https://docs.microsoft.com/en-us/azure/security-center/security-center-just-in-time?tabs=jit-config-asc%2Cjit-request-asc](https://docs.microsoft.com/en-us/azure/security-center/security-center-just-in-time?tabs=jit-config-asc%2Cjit-request-asc)

## 修正手順


### CLI

```text
az security jit-policy list --query '[*].virtualMachines[*].id | []'
```

## 参考資料

- [https://docs.microsoft.com/en-us/azure/security-center/security-center-just-in-time?tabs=jit-config-asc%2Cjit-request-asc](https://docs.microsoft.com/en-us/azure/security-center/security-center-just-in-time?tabs=jit-config-asc%2Cjit-request-asc)

## 技術情報

- Source Metadata：[sources/azure/vm_jit_access_enabled/metadata.json](../../sources/azure/vm_jit_access_enabled/metadata.json)
- Source Code：[sources/azure/vm_jit_access_enabled/check.py](../../sources/azure/vm_jit_access_enabled/check.py)
- Source Metadata Path：`sources/azure/vm_jit_access_enabled/metadata.json`
- Source Code Path：`sources/azure/vm_jit_access_enabled/check.py`
