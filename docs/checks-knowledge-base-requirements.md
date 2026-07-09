# ST Cloud 检查项知识库需求

## 目标

ST Cloud 检查项知识库用于承接扫描报告中的检查项引用。用户在报告中看到某个检查项后，可以打开知识库页面，理解该检查项的含义、风险、修复方式和参考资料。

第一版不复刻 Prowler Hub 的完整交互，也不展示会让普通用户困惑的运行入口。第一版重点是把 AWS、Azure、GCP 的现有检查项元数据整理成 ST Cloud 可访问、可维护、可引用的知识库内容。

## 内容范围

第一版范围：

- AWS 检查项
- Azure 检查项
- GCP 检查项
- 来源为本地 `prowler/providers/{provider}/services/**/{check_id}.metadata.json`
- 输出为 `checks/` 目录下的 Markdown 页面和 `checks/index.json`

第一版暂不包含：

- Prowler CLI 运行命令入口
- Run in Prowler Cloud
- 页面内完整 Check Code 展示
- 大段原始 JSON 元数据展示
- 复杂筛选 UI 或搜索前端

## 页面信息架构

每个检查项页面按以下顺序展示。

### 1. 页面标题

位置：页面最顶部。

内容：

- 检查项标题 `CheckTitle`
- 标题下方展示一句说明：`ST Cloud check knowledge base entry.`

用途：

- 让用户快速确认当前页面对应哪个检查项。

### 2. 检查项信息

位置：标题之后，作为页面第一块信息表。

内容：

- 检查项 ID：`CheckID`
- 云平台：`Provider`
- 服务：`ServiceName`
- 子服务：`SubServiceName`，为空时不展示
- 严重等级：`Severity`
- 类别：`Categories`，为空时展示 `Uncategorized`
- 检查类型：`CheckType`，为空时不展示
- 资源类型：`ResourceType`
- 资源组：`ResourceGroup`，为空时不展示

用途：

- 给用户和安服人员一个结构化概览。
- 报告可以根据检查项 ID 跳转到对应页面。

### 3. 描述

位置：检查项信息之后。

内容来源：

- `Description`

用途：

- 解释检查项在检查什么。

### 4. 风险

位置：描述之后。

内容来源：

- `Risk`

用途：

- 解释不满足该检查项会带来的安全风险。

### 5. 推荐措施

位置：风险之后。

内容来源：

- `Remediation.Recommendation.Text`
- `Remediation.Recommendation.Url` 作为推荐措施相关链接

用途：

- 给用户一个简洁、面向决策的修复建议。

### 6. 修复步骤

位置：推荐措施之后。

内容来源：

- `Remediation.Code.CLI`
- `Remediation.Code.NativeIaC`
- `Remediation.Code.Terraform`
- `Remediation.Code.Arm`
- `Remediation.Code.Other`

展示规则：

- 有内容才展示对应小节。
- 命令或配置片段用代码块展示。
- URL 类型内容展示为可点击链接。
- 不展示 “Run this check with Prowler CLI” 这类运行检查命令入口。

用途：

- 给客户和安服人员可执行的修复路径。

### 7. 参考资料

位置：修复步骤之后。

内容来源：

- `RelatedUrl`
- `AdditionalURLs`
- `Remediation.Recommendation.Url`

展示规则：

- 去重后展示。
- 空值不展示。
- 没有参考链接时展示 `No external references available.`

用途：

- 提供云厂商官方文档或相关外部说明。

### 8. 技术信息

位置：页面底部。

内容：

- Source Metadata：指向本仓库保存的 metadata 副本
- Source Code：指向本仓库保存的 check source 副本
- 本仓库源文件路径

用途：

- 给安服人员、工程人员溯源。
- 支持误报排查和检查逻辑确认。

## 品牌与来源

页面标题、目录和说明使用 ST Cloud 品牌。

不得把不存在的 ST Cloud CLI、ST Cloud Cloud 运行按钮或虚假域名放到页面中。

知识库页面不在每个检查项底部反复展示外部来源声明。来源和许可证说明统一放到仓库级文档：

- `ATTRIBUTION.md`
- `THIRD_PARTY_NOTICES.md`

仓库级文档中说明：

- 检查项内容基于开源检查元数据整理
- 许可证：Apache-2.0
- 技术信息区域优先链接到本仓库保存的 metadata 和 source code 副本
- 不在页面主内容中直接跳转到 Prowler Hub 或 Prowler GitHub

## 输出目录

第一版输出结构：

```text
checks/
  README.md
  index.json
  aws/
    {check_id}.md
  azure/
    {check_id}.md
  gcp/
    {check_id}.md
sources/
  aws/
    {check_id}/
      metadata.json
      check.py
  azure/
    {check_id}/
      metadata.json
      check.py
  gcp/
    {check_id}/
      metadata.json
      check.py
```

后续如启用 GitHub Pages，可以在不破坏该结构的前提下新增：

```text
docs/
  check/
    {check_id}/
      index.html
```

## 报告链接策略

知识库上线前，报告中不要生成不存在的 ST Cloud 链接。

知识库上线后，报告可以按配置切换为真实链接：

```text
{ST_CLOUD_CHECKS_BASE_URL}/check/{check_id}/
```

如果没有配置 `ST_CLOUD_CHECKS_BASE_URL`，报告继续展示纯文本：

```text
ST Cloud 检查项：{check_id}
```
