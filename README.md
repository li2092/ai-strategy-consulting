# AI Strategy Consulting · Claude Skill

> 一个为企业(尤其国企 / 央企 / 政府类客户)写 AI 战略咨询报告的 Claude Code Skill。
> 沉淀自 100+ 页国企客户战略稿 + 多轮外部复审实战。

🌐 **English version**: [README.en.md](README.en.md)
👤 **作者**: [Jimi](https://jimi.ink/)

---

## 为什么开源 · 初衷

写 AI 战略报告这件事,长期以来是 BCG / McKinsey / 头部咨询公司的领地 —— 方法论藏在私有项目里,普通行业从业者无从复用。

但其实**每个行业的人都在问同一类问题**:

- 我所在的行业,AI 到底能用在哪?
- 现在启动晚不晚? 投入多少合适?
- 哪些坑是别人踩过、我可以绕开的?
- 自己怎么先想清楚,而不是等咨询公司告诉我?

这个 skill 把我做过的几份 AI 战略稿沉淀出来的方法论 + 13 个反模式 + 3 个 Python 检查工具,**全部脱敏后开源**。

**目的很简单**:让任何行业的从业者(医疗 / 教育 / 制造 / 物流 / 零售 / 农业 / ...)都能用 Claude / 自己的方式快速过一遍"我们行业的 AI 应用可能性" —— 不需要请咨询公司,不需要百万预算,一个浏览器 + Claude Code 就能开始。

如果你用本 skill 做出了有趣的 AI 战略思考,欢迎在 [GitHub Discussions](../../discussions) 分享(无论行业,无论结果)。**让 AI 战略不再是少数人的专利**。

### 怎么兑现"任何行业、不需要咨询公司"的承诺

两个关键设计:

1. **Mode L · Lite 个人/团队探索** —— 你给"行业 + 角色 + 一句痛点",AI 在 0.5-1 天内产出 5-10 页探索文档(行业摸底 + 8-15 个 AI 候选场景 + Top 3 推荐 + 第一步行动)。不需要 60-100 页正式战略报告
2. **陌生行业摸底框架** —— 你的行业(如宠物医院 / 民营养老 / 二手奢侈品 / 任意长尾业态)不在预制 10 套样板里? 框架 1-2 小时建立够用认知,然后跑 Mode L。**框架优先 + 实例补充,样板不是边界**

---

## 这个 skill 解决什么问题

写 AI 战略报告时最容易踩的 13 个坑(实战沉淀):

1. 编造股权链 / 组织关系叙事
2. 跨客户内容入稿(把 A 客户的内部数据写进 B 客户报告)
3. 自证式外部论据(项目组自己的活动当外部验证)
4. 国际公司引文越级(单一来源 → "行业必做")
5. 经济模型不当迁移(国际平台型公司高单价 → 国内中小预算客户)
6. 活口径残留(主稿改了,底稿没改)
7. 战略判断粗化("路径被堵死"等偷懒表达)
8. 威胁恐吓式机会成本叙事
9. AI 溢价假设(甲方不会因乙方用 AI 让乙方多收钱)
10. 第二人称口语化 + 自媒体腔
11. 高风险词堆砌(赋能 / 打造 / 闭环 / 抓手 ...)
12. 排比三连 / 设问开头 / 套话过渡
13. 数量声明与实际不一致

本 skill 提供:**完整方法论 + 11 章主报告骨架 + 一页纸 + PPT + 6 类附件 + 4 种 HTML 图表 + 3 个 Python 自检脚本**,帮你绕开这些坑。

---

## 适用场景

| 场景 | 典型客户 | 推荐 Mode |
|---|---|---|
| 给企业写 AI 战略报告 / AI 转型路线图 | 国企 / 央企 / 政府 / 行业头部 | Mode D → P → R |
| AI 应用方向的可行性评估 + ROI 测算 | 任何启动 AI 项目前的决策 | Mode D 或 Mode L |
| AI Copilot / Agent / 行业大模型 / 自研小模型的战略提案 | 工程基建 / 金融 / 制造 / 政府 | Mode D → P → R |
| 已有报告稿件按咨询硬标准做外审清稿 | 任何咨询交付物 | Mode R · 审稿四层 |
| **行业从业者自问:我所在的行业 AI 该怎么布局?** | **任何行业的内部团队** | **Mode L · Lite** |
| **陌生行业摸底**(预制样板外的长尾业态) | **个人 / 小团队 / 跨行业探索者** | **Mode L + 陌生行业框架** |

**不适用**:通用 IT 咨询 / 纯技术方案 / 单纯文档美化(用其他 skill)。

---

## 快速开始

### 1. 安装

把整个目录拷贝到 Claude Code 的 skills 目录:

```bash
# macOS / Linux
git clone https://github.com/li2092/ai-strategy-consulting.git \
  ~/.claude/skills/ai-strategy-consulting

# Windows (PowerShell)
git clone https://github.com/li2092/ai-strategy-consulting.git `
  $env:USERPROFILE\.claude\skills\ai-strategy-consulting
```

重启 Claude Code,skill 自动加载。

### 2. 触发

在 Claude Code 里说任意一种:

**Mode L · 个人/团队探索**(0.5-1 天,无外部客户也能跑):
- "我们[行业]的 AI 能干嘛?"
- "[X 行业]的 AI 应用可能性帮我探一下"
- "我在[宠物医院 / 民营养老 / 二手奢侈品 / ...],想看看 AI 怎么用"
- "帮我做一份 AI 探索文档,5-10 页,这周就要出"

**Mode D-P-R · 完整正式稿**(2-4 天,给客户/给领导):
- "帮我给某客户写 AI 战略报告"
- "做一份 AI 转型路线图"
- "评估 AI Copilot 在 X 行业的可行性"
- "把这份 AI 战略稿按咨询硬标准过一遍审"

**通用关键词**:`AI 战略 / AI 转型 / AI 咨询 / AI 路线图 / Agent 战略 / 智能化战略 / AI 探索`

### 3. 自检脚本(纯 Python 标准库,无需 pip install)

写完稿件后跑:

```bash
python scripts/ai_slop_check.py 主报告.md      # 反 AI 腔(目标 < 5 处全文)
python scripts/label_coverage.py 主报告.md     # 三标签覆盖率(目标 ≥ 85%)
python scripts/cross_client_check.py 主报告.md --client "[本客户名]"  # 跨客户内容
```

---

## 文件结构

```
ai-strategy-consulting/
├── SKILL.md                       # 主入口(Claude 自动加载) · 含 Mode L/D/P/R 四种工作模式
├── README.md                      # 本文件(中文)
├── README.en.md                   # English version
├── LICENSE                        # MIT
├── references/                    # 详细方法论(按需加载)
│   ├── 01-information-gathering.md   # 五维信息采集 + 客户上下文 7 项 + 10 套行业样板
│   ├── 02-frameworks.md              # BCG / McKinsey / 五把筛子 / 价值四问
│   ├── 03-report-architecture.md     # 11 章主报告骨架 + 4 种开篇钩子
│   ├── 04-anti-patterns.md           # 13+ 反模式速查
│   ├── 05-roi-templates.md           # 精益启动 / 标准 / 重资产 三档 ROI 模板
│   ├── 06-language-discipline.md     # 反 AI 腔 + 反威胁 + Claim-Evidence-Implication
│   ├── 07-review-checklist.md        # 八维 51 项 + 6 步法 + 对抗式自审
│   ├── 08-deliverable-formats.md     # 主报告 / 一页纸 / PPT / 6 附件 详细规格
│   ├── 09-visualization-templates.md # 4 种关键图表 HTML 模板(蓝橙配色)
│   ├── 10-output-formats.md          # MD → Word / PPT / PDF 工具路径
│   ├── 11-review-thinking-model.md   # 审稿四层认知架构(L1 病因/L2 前提/L3 全局/L4 结构)
│   └── 12-unfamiliar-industry-framework.md  # 陌生行业摸底框架(任意行业 1-2 小时建立认知)
├── assets/                        # 直接可用的模板
│   ├── main-report-template.md       # 11 章主报告模板(Mode R 用)
│   ├── one-pager-template.md         # 一页纸 4 象限模板(Mode R 用)
│   ├── ppt-outline-template.md       # PPT 20 + 6 模板(Mode R 用)
│   └── lite-mode-template.md         # Mode L · 5-10 页探索文档模板
└── scripts/                       # Python 检查脚本(纯标准库)
    ├── ai_slop_check.py
    ├── label_coverage.py
    └── cross_client_check.py
```

---

## 设计原则

1. **零外部 skill 依赖** —— 拿来即用,不需要装其他 skill
2. **零第三方库依赖** —— Python 脚本只用 sys / re / pathlib 标准库
3. **客户脱敏** —— 所有方法论 + 案例 + 数字均为通用范例,不含任何具名客户内容
4. **方法论 + 模板 + 检查工具自包含** —— 但"最后一公里"(转 Word / PPT / 截图)交给用户本地工具
5. **批判性纪律** —— 反 AI 腔 / 反威胁恐吓 / 反自说自话 / 反跨客户内容入稿,四类零容忍

---

## 致谢

本 skill 的方法论框架借鉴了:

- BCG · 10-20-70 框架(2025)
- McKinsey · Steer-Scale-Institutionalize
- MIT Sloan + BCG · Agentic Enterprise 4 张力(2025)
- Barbara Minto · Pyramid Principle
- 《论看起来对》四层认知架构(L1 病因 / L2 前提 / L3 全局 / L4 结构) —— 用于审稿四层模型(`references/11-review-thinking-model.md`)

实战纪律(13 反模式 + 6 步法 + 对抗式自审 + 审稿四层 + 陌生行业框架)沉淀自笔者多份国企 AI 战略稿件的踩坑、外审记录,以及对"看起来对、其实不对"问题的反复诊断。

---

## License

[MIT](LICENSE) —— 商用 / 修改 / 再分发自由,只需保留版权声明。

---

## 贡献

Issues / PRs welcome。如果你在使用中发现新的反模式或踩坑,欢迎在 GitHub Issues 提交。

特别欢迎以下贡献:

- **新增行业 ROI 模板**(医疗 / 教育 / 零售 / 农业 / 物流 / ...)
- **新增 HTML 图表模板**
- **新增其他语言版本**的反 AI 腔规则
- **分享你用本 skill 做出的有趣 AI 战略思考**(到 Discussions)
