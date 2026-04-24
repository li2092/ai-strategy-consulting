# AI Strategy Consulting · Claude Skill

> 一个为任何客户写 AI 战略报告的 Claude Code Skill。
> 默认对标世界前沿科技公司(Google / Anthropic / OpenAI / 字节 / 腾讯)的 AI 战略写作方式;政策合规与 ROI 算账作为可选 add-on 按需启用。

🌐 **English version**: [README.en.md](README.en.md)
👤 **作者**: [Jimi](https://jimi.ink/)

---

## 这个 skill 解决什么问题

AI 战略报告很容易写成"看起来完整、实际空洞"的 deck —— 全表格、堆 RAG/Agent 名词、推荐都是"高价值低难度"、没有"不做什么"段、AI 全程自说自话。

本 skill 用三层机制解决这件事:

1. **2 步主流程**:Step 1 探索方向(开放、不预筛)→ Step 2 写战略报告(默认 7 章、严格结构)
2. **5 项硬约束(H1-H5)**:表格 ≤ 25%、每章 2 段散文、推荐有具象化锚点、对标按格式、必须有取舍段
3. **Checkpoint 协议**:每章写完必须主动暴露疑虑 + 等用户确认,不一次性跑完

---

## 适用场景

| 场景 | 客户类型 | 触发流程 |
|---|---|---|
| 给科技公司写 AI 战略 / Copilot 提案 | 互联网 / 创业公司 / 内部团队 | Step 1 → Step 2 |
| 探索"我们这个行业 AI 能干嘛" | 任何行业的内部团队 | Step 1 (单独使用) |
| 已有方向、要写正式 AI 战略稿 | 决策层 / 董事会场景 | 直接 Step 2 |
| 给国企 / 政府 / 工程基建客户写 AI 战略 | 受监管行业、走立项流程 | Step 1 → Step 2 + 启用 ROI / 政策 add-on |
| 审稿现有 AI 战略稿件 | 任何已有稿件 | 单独审稿(参考反模式速查) |

**不适用**:通用 IT 咨询 / 纯技术方案 / 单纯文档美化(用其他 skill)。

---

## 快速开始

### 1. 安装

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

在 Claude Code 里说任意一种,skill 自动激活:

**Step 1 探索方向**(还没决定方向时):
- "我们 [行业] 的 AI 能干嘛?"
- "[X 行业] 的 AI 应用可能性帮我探一下"
- "想看看 AI 怎么用在 [Y 场景]"

**Step 2 写战略报告**(已决定 Top 方向、要写正式稿):
- "帮我给 [客户] 写 AI 战略报告"
- "做一份 AI 转型路线图"
- "起草 AI Copilot / Agent 战略提案"

**审稿现有稿**:
- "把这份 AI 战略稿按硬标准过一遍审"
- "用反模式速查检查一下这篇"

**通用关键词**:`AI 战略 / AI 转型 / AI 咨询 / AI 路线图 / Agent 战略 / 智能化战略 / AI 探索`

### 3. 自检(零脚本依赖)

本 skill 不带 Python 脚本。所有自检靠 grep + 人工审稿。
[`references/04-anti-patterns.md`](references/04-anti-patterns.md) 末尾给了完整的 grep 套餐,直接复制运行。

---

## 文件结构

```
ai-strategy-consulting/
├── SKILL.md                            # 主入口(Claude 自动加载)
├── README.md                           # 本文件(中文)
├── README.en.md                        # English version
├── LICENSE                             # MIT
├── references/                         # 详细方法论(按需加载)
│   ├── 01-step1-exploration.md            # Step 1 详细方法
│   ├── 02-step2-drafting.md               # Step 2 详细方法 + 默认 7 章结构
│   ├── 03-strategy-depth.md               # 5 项硬约束(H1-H5)详解
│   ├── 04-anti-patterns.md                # P0-P4 反模式速查 + grep 套餐
│   ├── 05-language-discipline.md          # 反 AI 腔 / 三标签纪律 / 句段控制
│   ├── 06-checkpoint-protocol.md          # Checkpoint 协议(本 skill 核心机制)
│   ├── 07-review-thinking-model.md        # 审稿四层认知架构
│   ├── 08-unfamiliar-industry.md          # 陌生行业摸底框架
│   ├── 09-output-formats.md               # MD → Word / PPT 转换路径
│   ├── add-on-roi.md                      # 可选 · ROI 测算(国企/工程基建)
│   └── add-on-soe-policy.md               # 可选 · 政策合规(国企/政府)
└── assets/                             # 直接可填的模板
    ├── exploration-template.md            # Step 1 探索文档模板
    └── report-template.md                 # Step 2 战略报告模板
```

---

## 设计原则

1. **零脚本、零外部 skill 依赖** —— 拿来即用,不需要装任何额外工具
2. **客户脱敏** —— 所有方法论 + 案例 + 数字均为通用范例,不含任何具名客户内容
3. **默认对标世界前沿** —— 不假设客户是国企/政府;政策与 ROI 走 add-on 按需启用
4. **Checkpoint 强制边写边审** —— 每章写完暴露疑虑,不一次性跑完防"看似完整实际空洞"
5. **反 AI 腔 / 反威胁恐吓 / 反自说自话 / 反跨客户** —— 四类零容忍

---

## 致谢

本 skill 的方法论框架借鉴了:

- BCG · 10-20-70 框架
- McKinsey · Steer-Scale-Institutionalize
- Barbara Minto · Pyramid Principle
- 论看起来对 · 四层认知架构(L1 病因 / L2 前提 / L3 全局 / L4 结构)—— 用于审稿四层模型

实战纪律沉淀自笔者多个客户 AI 战略稿件的踩坑、外审记录,以及对"看起来对、其实不对"问题的反复诊断。

---

## License

[MIT](LICENSE) —— 商用 / 修改 / 再分发自由,只需保留版权声明。

---

## 贡献

Issues / PRs welcome。如果你在使用中发现新的反模式或踩坑,欢迎在 GitHub Issues 提交。

特别欢迎:
- **新增可选 add-on**(行业政策 / 行业 ROI / 行业陌生摸底)
- **新增其他语言版本**的反 AI 腔规则
- **分享你用本 skill 做出的有趣 AI 战略思考**(Discussions)
