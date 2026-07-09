# PostgreSQL Flexible Server enforces Microsoft Entra ID authentication with administrators

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `postgresql_flexible_server_entra_id_authentication_enabled` |
| 云平台 | Azure |
| 服务 | postgresql |
| 严重等级 | medium |
| 类别 | identity-access |
| 资源类型 | PostgreSQL |
| 资源组 | database |

## 描述

**PostgreSQL Flexible Servers** must set `authConfig.activeDirectoryAuth` to `Enabled` and keep at least one **Microsoft Entra administrator** assigned so database sessions inherit centrally governed identities instead of unmanaged PostgreSQL accounts.

## 风险

Without Entra ID authentication, stolen local passwords bypass **MFA** and conditional access, enabling persistent database logins. Missing administrators leaves the feature unusable, blocking security teams from rotating duties and allowing unauthorized access or **privilege escalation**.

## 推荐措施

Federate PostgreSQL Flexible Server access through **Microsoft Entra ID** so MFA, conditional access, and centralized RBAC govern logins. Maintain at least one delegated administrator group and rotate membership through identity governance processes.

## 修复步骤


### CLI

```text
az postgres flexible-server update --resource-group <resourceGroupName> --name <serverName> --active-directory-auth Enabled
az postgres flexible-server microsoft-entra-admin create --resource-group <resourceGroupName> --server-name <serverName> --object-id <objectId> --display-name <displayName>
```

### Terraform

```hcl
data "azurerm_client_config" "current" {}

resource "azurerm_postgresql_flexible_server" "example" {
  name                = "pg-flex"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
  sku_name            = "GP_Standard_D4s_v3"
  administrator_login = "pgadmin"
  administrator_password = "<complexPassword>"
  storage_mb          = 131072
  version             = "16"

  authentication {
    active_directory_auth_enabled = true
    tenant_id                     = data.azurerm_client_config.current.tenant_id
  }
}

resource "azurerm_postgresql_flexible_server_active_directory_administrator" "entra_admin" {
  server_id     = azurerm_postgresql_flexible_server.example.id
  object_id     = var.entra_object_id
  principal_name = var.entra_principal_name
  principal_type = "User"
  tenant_id     = data.azurerm_client_config.current.tenant_id
}
```

### Other

1. In the Azure Portal, open Azure Database for PostgreSQL flexible server and select the target server.
2. Under Security > Authentication, set Microsoft Entra ID authentication (or combined mode) to Enabled and save the change.
3. Under Security > Microsoft Entra ID, add at least one administrator (user or group) linked to an Entra object ID and confirm the assignment.

## 参考资料

- [https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/security-entra-concepts](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/security-entra-concepts)
- [https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/security-entra-configure](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/security-entra-configure)

## 技术信息

- Source Metadata：[sources/azure/postgresql_flexible_server_entra_id_authentication_enabled/metadata.json](../../sources/azure/postgresql_flexible_server_entra_id_authentication_enabled/metadata.json)
- Source Code：[sources/azure/postgresql_flexible_server_entra_id_authentication_enabled/check.py](../../sources/azure/postgresql_flexible_server_entra_id_authentication_enabled/check.py)
- Source Metadata Path：`sources/azure/postgresql_flexible_server_entra_id_authentication_enabled/metadata.json`
- Source Code Path：`sources/azure/postgresql_flexible_server_entra_id_authentication_enabled/check.py`
