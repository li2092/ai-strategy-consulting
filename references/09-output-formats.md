# 输出形态与转换工具

> 本 skill **零外部 skill 依赖、零脚本依赖**。默认产出形态 = Markdown 文本(含表格)+ 可选 HTML 图表。
> 自检全部依靠 grep + 人工审稿(详见 [04-anti-patterns.md](04-anti-patterns.md) 与 [05-language-discipline.md](05-language-discipline.md))。
> 进阶交付物(Word / PPT / PDF / 截图)由用户用本地工具自行转换 —— 本文件给推荐路径,但不强制使用任何工具。

## 目录

1. 默认产出三件套
2. Markdown → Word(4 种路径)
3. Markdown → PPT(3 种路径)
4. HTML → PNG / PDF
5. 完整交付物清单参考

---

## 1 · 默认产出三件套

| 产出物 | 格式 | 何时给客户 |
|---|---|---|
| 主报告 | `.md` (15-30 页对应字数 · 10000-17000 字) | 主交付 |
| 一页纸摘要(可选) | `.md` | 给决策者入口 |
| PPT 大纲(可选) | `.md` | 给团队建 PPT 用 |
| 关键图表(可选) | `.html` 或 PNG | 截图嵌主报告 / PPT |

**默认场景**:仅交付主报告 `.md` 即可,其他三项按客户需要追加。

---

## 2 · Markdown → Word(4 种路径,任选)

### 2.1 路径 A · pandoc(推荐 · 命令行 30 秒)

```bash
# 安装(一次)
brew install pandoc      # macOS
choco install pandoc     # Windows
sudo apt install pandoc  # Linux

# 转换
pandoc 主报告.md -o 主报告.docx --reference-doc=template.docx

# template.docx 是带样式的空白 Word 文档(可选)
# 如果不给,pandoc 会用默认样式
```

### 2.2 路径 B · Typora / Obsidian(图形化 · 0 配置)

- Typora: 打开 .md → 文件 → 导出 → Word(.docx)
- Obsidian + Pandoc 插件: 同样一键导出

### 2.3 路径 C · Microsoft Word(原生支持)

Word 2016+ 可直接打开 .md 文件:
- 文件 → 打开 → 选择 .md → "始终用 Word 打开 Markdown"
- 缺点:不保留所有 markdown 格式(表格 OK,代码块/引用块可能丢失)

### 2.4 路径 D · 在线工具(无需安装)

- markdown-to-docx.com(在线转换)
- StackEdit.io(编辑 + 导出)
- 注意:**敏感稿件不要传在线工具**(隐私风险)

### 2.5 公文样式建议(转 Word 后手动调)

国企 / 政府客户场合的标准格式:

| 元素 | 推荐设置 |
|---|---|
| 正文字体 | 仿宋 GB2312,小四(12pt) |
| 标题字体 | 黑体(一级)/ 宋体加粗(二级三级) |
| 段距 | 段前 0.5 行,段后 0 行 |
| 行距 | 1.5 倍 |
| 主色 | `#1D4ED8`(深蓝)|
| 强调色 | `#C2410C`(公文橙)|
| 页边距 | 上下 2.54 cm,左右 3.17 cm |
| 页眉 | 客户名 · 战略报告 · YYYY-MM |

---

## 3 · Markdown → PPT(3 种路径)

### 3.1 路径 A · 手工按主报告章节建(推荐 · 控制力最强)

直接按主报告的 7 章结构(执行摘要 / 背景诊断 / AI 战略主线 / Top 推荐方向 / 不做什么 / 路线图 / 风险与边界)对应 PPT 页:

| 主报告章节 | 推荐 PPT 页数 | 关键画面 |
|---|---|---|
| 执行摘要 | 1-2 页 | 一页纸结论 + Top 3 推荐 |
| 背景诊断 | 2-3 页 | 现状 + 3 大差距 + 关键数字 |
| AI 战略主线 | 2-3 页 | 战略一句话 + 3 层价值 + 取舍框架 |
| Top 推荐方向 | 5-7 页(每方向 1 页) | 输入/输出/替代/保留人做 + 对标 |
| 不做什么 | 1 页 | 取舍清单 + 原因 |
| 路线图 | 2 页 | 时间轴 + 每阶段交付 |
| 风险与边界 | 1-2 页 | 主观风险 + 客观风险 + 应对 |

工作流:
1. 在 PowerPoint / Keynote 里建空白页
2. 标题取自主报告章节标题
3. 内容从主报告 .md 里 copy-paste 关键句
4. 关键数字 / 对标做成图表

**优点**:完全掌控视觉,不被自动转换工具的样式限制。
**耗时**:1.5-2 小时(熟练后 1 小时)。

### 3.2 路径 B · pandoc + reveal.js(命令行 · 网页 PPT)

```bash
pandoc PPT-大纲.md -t revealjs -s -o slides.html
# 浏览器打开 slides.html → F11 全屏 → ←/→ 翻页
```

适合:技术分享场景。
不适合:国企董事长汇报(他们要 .pptx 文件)。

### 3.3 路径 C · python-pptx(命令行 · 生成 .pptx)

```python
# pip install python-pptx
from pptx import Presentation
prs = Presentation()
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "页 1 标题"
slide.placeholders[1].text = "正文内容"
prs.save('output.pptx')
```

可写脚本批量生成 20 页基础架子,再手动美化。

---

## 4 · HTML → PNG / PDF

本 skill 09 提供的 HTML 图表模板,转图片或 PDF:

### 4.1 截图(最简单)

| 平台 | 方法 |
|---|---|
| macOS | `Cmd+Shift+4` 矩形截图 / `Cmd+Shift+5` 录全页 |
| Windows | `Win+Shift+S` 截图 / 截图工具 |
| Chrome DevTools | `F12` → 命令面板 `Cmd/Ctrl+Shift+P` → "Capture full size screenshot" |

### 4.2 转 PDF

浏览器打开 HTML → `Cmd/Ctrl+P` → 目标"另存为 PDF" → 调好边距 → 保存。

### 4.3 自动化(可选 · 用户有 Playwright 环境时)

```python
# pip install playwright; playwright install chromium
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(f'file://{path_to_html}')
    page.screenshot(path='out.png', full_page=True)
    browser.close()
```

但这是**进阶方案**,本 skill 不强制依赖 Playwright。

---

## 5 · 完整交付物清单参考

一份完整咨询交付通常含:

| # | 交付物 | 格式 | 本 skill 是否提供 |
|---|---|---|---|
| 1 | 主报告 | .md → 用户转 .docx | ✅ Markdown 完整生成 |
| 2 | 一页纸 | .md → 用户转 .pdf | ✅ Markdown 完整生成 |
| 3 | PPT 汇报稿 | .pptx | 部分 (大纲 .md,需用户建 .pptx) |
| 4 | 6 类附件 | .md / .xlsx | ✅ Markdown 完整生成 |
| 5 | 关键图表 | .png | ✅ HTML 模板,需用户截图 |
| 6 | 自检报告 | 控制台输出 | ✅ 3 个 Python 脚本 |

**核心原则**:本 skill 不替用户做"最后一公里",但提供完整的方法论 + 模板 + 检查工具。最后一公里(转换 + 美化)由用户基于自己工具栈完成。
