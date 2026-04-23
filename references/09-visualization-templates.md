# 关键图表 HTML 模板

> 本 skill 默认输出 Markdown 文本 + 自包含 HTML 图表(浏览器直接打开就能看)。
> **不依赖任何外部 skill 或图表库**(无 Mermaid / 无 D3 / 无 Chart.js,纯 HTML + CSS)。
> 截图请用户用浏览器/系统自带工具(macOS Cmd+Shift+4,Windows Snipping Tool,或 Chrome DevTools 截全图)。

## 目录

1. 蓝橙公文配色方案
2. 战略主线四层架构图(最重要)
3. 三档投入 × 四层回报矩阵(ROI 表)
4. 风险三类雷达(8 类红线表)
5. 三年甘特图
6. 通用使用方法

---

## 1 · 蓝橙公文配色方案

国企 / 政府客户场合的稳健配色,已在多份咨询稿验证可读性 OK:

| 用途 | 颜色 | HEX | 何时用 |
|---|---|---|---|
| 主色(蓝) | 深蓝 | `#1D4ED8` | 标题 / 主框线 / 主推方案 |
| 强调(橙) | 公文橙 | `#C2410C` | 关键数据 / 核心建议 / 决策点 |
| 辅助灰 | 暖灰 | `#475569` | 次要文字 / 边框 |
| 浅蓝底 | 雾蓝 | `#E0E7FF` | 表头 / 分组背景 |
| 浅橙底 | 雾橙 | `#FED7AA` | 强调单元格 |
| 字体 | 仿宋 | `'FangSong', '仿宋', serif` | 正文 |
| 字体 | 黑体 | `'SimHei', '黑体', sans-serif` | 标题 |

---

## 2 · 战略主线四层架构图(最重要 · 主报告 §3 必备)

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>战略主线四层架构</title>
<style>
  body { font-family: 'FangSong', '仿宋', serif; padding: 30px; background: #fff; }
  h1 { color: #1D4ED8; font-family: 'SimHei', '黑体', sans-serif; border-left: 6px solid #1D4ED8; padding-left: 12px; }
  .layer { border: 1px solid #94A3B8; margin: 8px 0; padding: 14px; border-radius: 6px; }
  .layer-title { font-weight: bold; color: #1D4ED8; margin-bottom: 8px; font-family: 'SimHei', '黑体', sans-serif; }
  .layer-product { background: #E0E7FF; }
  .layer-capability { background: #F1F5F9; }
  .layer-business { background: #FED7AA; }
  .layer-ecosystem { background: #FAFAF9; }
  .blocks { display: flex; gap: 10px; flex-wrap: wrap; }
  .block { background: #fff; border: 1px solid #1D4ED8; padding: 8px 14px; border-radius: 4px; }
  .block.highlight { background: #C2410C; color: #fff; border-color: #C2410C; }
</style>
</head>
<body>
<h1>战略主线四层架构 · 客户名</h1>

<div class="layer layer-product">
  <div class="layer-title">顶层 · 产品</div>
  <div class="blocks">
    <div class="block highlight">产品 1(主推)</div>
    <div class="block highlight">产品 2(主推)</div>
  </div>
</div>

<div class="layer layer-capability">
  <div class="layer-title">中层 · 能力(共享底座 L1-L6)</div>
  <div class="blocks">
    <div class="block">L1 数据层</div>
    <div class="block">L2 知识层</div>
    <div class="block">L3 模型层</div>
    <div class="block">L4 Agent 层</div>
    <div class="block">L5 接入层</div>
    <div class="block">L6 应用层</div>
  </div>
</div>

<div class="layer layer-business">
  <div class="layer-title">下层 · 业务(V 形聚焦)</div>
  <div class="blocks">
    <div class="block">业务 A · 主战场</div>
    <div class="block">业务 B · 主战场</div>
    <div class="block">业务 C · 主战场</div>
    <div class="block" style="opacity: 0.5;">其他业务 · 正常经营,不进 AI 战略</div>
  </div>
</div>

<div class="layer layer-ecosystem">
  <div class="layer-title">底层 · 生态</div>
  <div class="blocks">
    <div class="block">MCP 接口</div>
    <div class="block">硬件合作</div>
    <div class="block">开源工具栈</div>
  </div>
</div>
</body>
</html>
```

**用法**:复制保存为 `architecture.html` → 浏览器打开 → Cmd+P 另存 PDF / 或截图。

---

## 3 · 三档投入 × 四层回报矩阵(主报告 §6 必备)

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>投入回报矩阵</title>
<style>
  body { font-family: 'FangSong', '仿宋', serif; padding: 30px; }
  h1 { color: #1D4ED8; font-family: 'SimHei', '黑体', sans-serif; border-left: 6px solid #1D4ED8; padding-left: 12px; }
  table { border-collapse: collapse; width: 100%; margin: 14px 0; }
  th { background: #E0E7FF; color: #1D4ED8; padding: 10px; border: 1px solid #94A3B8; font-family: 'SimHei', '黑体', sans-serif; }
  td { padding: 10px; border: 1px solid #94A3B8; text-align: center; }
  .baseline { background: #FED7AA; font-weight: bold; }
  .baseline-label { color: #C2410C; font-weight: bold; }
  .roi-summary { background: #1D4ED8; color: #fff; padding: 16px; margin-top: 20px; border-radius: 6px; text-align: center; font-size: 1.1em; }
</style>
</head>
<body>
<h1>三档投入 × 四层回报矩阵</h1>

<table>
  <tr><th>档位</th><th>Year 1</th><th>Year 2</th><th>Year 3</th><th>三年合计</th></tr>
  <tr><td>保守档</td><td>...</td><td>...</td><td>...</td><td>X 万</td></tr>
  <tr class="baseline"><td class="baseline-label">基准档 ◀ 主推</td><td>...</td><td>...</td><td>...</td><td>X 万</td></tr>
  <tr><td>激进档</td><td>...</td><td>...</td><td>...</td><td>X 万</td></tr>
</table>

<table>
  <tr><th>价值层</th><th>类型</th><th>三年合计</th><th>标签</th></tr>
  <tr><td>L1</td><td>内部提效(机会成本)</td><td>X 万</td><td>【推断】</td></tr>
  <tr><td>L2</td><td>外部签约现金流</td><td>X 万</td><td>【推断+假设】</td></tr>
  <tr><td>L3</td><td>硬资产(平台 + 模型 + 数据)</td><td>定性描述</td><td>—</td></tr>
  <tr><td>L4</td><td>软实力(五维信号)</td><td>半量化</td><td>—</td></tr>
</table>

<div class="roi-summary">
  现金 ROI ≈ N1% &nbsp;·&nbsp; 综合 ROI ≈ N2%<br>
  现金回本 N3 个月 &nbsp;·&nbsp; 综合回本 N4 个月
</div>
</body>
</html>
```

---

## 4 · 风险三类红线表(主报告 §8 必备)

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>风险与应用边界</title>
<style>
  body { font-family: 'FangSong', '仿宋', serif; padding: 30px; }
  h1, h2 { color: #1D4ED8; font-family: 'SimHei', '黑体', sans-serif; }
  h1 { border-left: 6px solid #1D4ED8; padding-left: 12px; }
  h2 { margin-top: 24px; }
  .risk-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14px; margin: 20px 0; }
  .risk-card { border: 1px solid #94A3B8; border-radius: 6px; padding: 14px; }
  .risk-card.tech { border-top: 4px solid #1D4ED8; }
  .risk-card.org { border-top: 4px solid #C2410C; }
  .risk-card.market { border-top: 4px solid #475569; }
  .risk-title { font-weight: bold; font-family: 'SimHei', '黑体', sans-serif; margin-bottom: 8px; }
  table { border-collapse: collapse; width: 100%; margin: 14px 0; }
  th { background: #FED7AA; color: #C2410C; padding: 10px; border: 1px solid #94A3B8; }
  td { padding: 10px; border: 1px solid #94A3B8; }
</style>
</head>
<body>
<h1>风险与应用边界</h1>

<h2>风险三类</h2>
<div class="risk-grid">
  <div class="risk-card tech">
    <div class="risk-title" style="color: #1D4ED8;">技术风险</div>
    <ul><li>风险 1...</li><li>风险 2...</li><li>风险 3...</li></ul>
  </div>
  <div class="risk-card org">
    <div class="risk-title" style="color: #C2410C;">组织风险</div>
    <ul><li>风险 1...</li><li>风险 2...</li><li>风险 3...</li></ul>
  </div>
  <div class="risk-card market">
    <div class="risk-title" style="color: #475569;">市场风险</div>
    <ul><li>风险 1...</li><li>风险 2...</li><li>风险 3...</li></ul>
  </div>
</div>

<h2>不做的 8 件事 · 红线表</h2>
<table>
  <tr><th>#</th><th>不做什么</th><th>理由</th><th>替代方案</th></tr>
  <tr><td>1</td><td>...</td><td>...</td><td>...</td></tr>
  <tr><td>2</td><td>...</td><td>...</td><td>...</td></tr>
  <tr><td>3</td><td>...</td><td>...</td><td>...</td></tr>
  <tr><td>4</td><td>...</td><td>...</td><td>...</td></tr>
  <tr><td>5</td><td>...</td><td>...</td><td>...</td></tr>
  <tr><td>6</td><td>...</td><td>...</td><td>...</td></tr>
  <tr><td>7</td><td>...</td><td>...</td><td>...</td></tr>
  <tr><td>8</td><td>...</td><td>...</td><td>...</td></tr>
</table>
</body>
</html>
```

---

## 5 · 三年甘特图(主报告 §7 必备)

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>三年里程碑甘特图</title>
<style>
  body { font-family: 'FangSong', '仿宋', serif; padding: 30px; }
  h1 { color: #1D4ED8; font-family: 'SimHei', '黑体', sans-serif; border-left: 6px solid #1D4ED8; padding-left: 12px; }
  .gantt { display: grid; grid-template-columns: 180px repeat(36, 1fr); gap: 2px; margin-top: 20px; font-size: 0.85em; }
  .gantt-header { background: #1D4ED8; color: #fff; padding: 6px; text-align: center; font-family: 'SimHei', '黑体', sans-serif; font-weight: bold; }
  .gantt-row-label { background: #E0E7FF; padding: 8px; font-weight: bold; }
  .gantt-cell { background: #F1F5F9; min-height: 24px; }
  .bar-mvp { background: #C2410C; grid-column: span 3; padding: 4px; color: #fff; font-size: 0.75em; }
  .bar-product { background: #1D4ED8; padding: 4px; color: #fff; font-size: 0.75em; }
  .bar-sales { background: #475569; padding: 4px; color: #fff; font-size: 0.75em; }
  .milestone-marker { background: #C2410C; color: #fff; padding: 2px 4px; font-size: 0.7em; border-radius: 50%; text-align: center; }
</style>
</head>
<body>
<h1>三年里程碑(M1-M36)</h1>

<div class="gantt">
  <div class="gantt-header">工作流</div>
  <div class="gantt-header" style="grid-column: span 12;">Year 1</div>
  <div class="gantt-header" style="grid-column: span 12;">Year 2</div>
  <div class="gantt-header" style="grid-column: span 12;">Year 3</div>

  <div class="gantt-row-label">MVP 试点</div>
  <div class="bar-mvp">M1-M3 MVP</div>
  <div class="gantt-cell" style="grid-column: span 33;"></div>

  <div class="gantt-row-label">产品线 1</div>
  <div class="gantt-cell" style="grid-column: span 3;"></div>
  <div class="bar-product" style="grid-column: span 9;">Phase 1</div>
  <div class="bar-product" style="grid-column: span 12;">Phase 2 规模化</div>
  <div class="bar-product" style="grid-column: span 12;">Phase 3 平台化</div>

  <div class="gantt-row-label">产品线 2</div>
  <div class="gantt-cell" style="grid-column: span 6;"></div>
  <div class="bar-product" style="grid-column: span 6;">Phase 1</div>
  <div class="bar-product" style="grid-column: span 12;">Phase 2 规模化</div>
  <div class="bar-product" style="grid-column: span 12;">Phase 3 平台化</div>

  <div class="gantt-row-label">外部销售</div>
  <div class="gantt-cell" style="grid-column: span 9;"></div>
  <div class="bar-sales" style="grid-column: span 3;">首单</div>
  <div class="bar-sales" style="grid-column: span 12;">规模拓客</div>
  <div class="bar-sales" style="grid-column: span 12;">行业铺开</div>

  <div class="gantt-row-label">大赛 / 政策对接</div>
  <div class="gantt-cell" style="grid-column: span 5;"></div>
  <div class="milestone-marker">★</div>
  <div class="gantt-cell" style="grid-column: span 11;"></div>
  <div class="milestone-marker">★</div>
  <div class="gantt-cell" style="grid-column: span 11;"></div>
  <div class="milestone-marker">★</div>
  <div class="gantt-cell" style="grid-column: span 6;"></div>
</div>

<p style="margin-top: 20px; color: #475569;">★ = 关键决策门(董事长签字节点)</p>
</body>
</html>
```

---

## 6 · 通用使用方法

### 6.1 工作流

1. 在 IDE / 编辑器里复制需要的 HTML 模板
2. 替换占位内容(产品名 / 数字 / 业务名 / 时间窗)
3. 保存为 `图表名.html`
4. 浏览器打开:
   - macOS: `open 图表名.html`
   - Windows: `start 图表名.html`
   - 或直接双击

### 6.2 截图 / 转 PDF

| 目标 | 方法 |
|---|---|
| 截图(矩形) | macOS: `Cmd+Shift+4`;Windows: 截图工具 / `Win+Shift+S` |
| 截图(全页) | Chrome DevTools: F12 → Cmd/Ctrl+Shift+P → "Capture full size screenshot" |
| 转 PDF | 浏览器 `Cmd/Ctrl+P` → 另存为 PDF |
| 嵌入 Word | 截图 → 粘贴到 Word(或先转 PDF 再 Insert) |

### 6.3 自定义样式

如果客户有品牌色,把 §1 配色方案里的两个 HEX 值替换即可:
- 主色:`#1D4ED8` → `[客户主色]`
- 强调:`#C2410C` → `[客户强调色]`

### 6.4 进阶选项(本 skill 不强依赖)

如有以下工具,效果会更好,但**不是必需**:
- `diagram-gen` skill(本作者另一个 skill,自动生成专业 PNG)
- D3.js / Chart.js(交互式数据可视化)
- Mermaid(文本描述生成图表 · GitHub 原生支持)
- draw.io / Figma(高保真专业图)

但若没有以上任何工具,本 skill 提供的 HTML 模板已能满足 **80% 国企客户战略报告**的图表需求。
