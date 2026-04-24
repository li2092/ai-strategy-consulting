# AI Strategy Consulting · Claude Skill

> A Claude Code Skill for writing AI strategy reports for any client.
> Default benchmark is the writing style of frontier tech companies (Google / Anthropic / OpenAI / ByteDance / Tencent). Policy compliance and ROI calculations are optional add-ons triggered on demand.

🌐 **中文版**: [README.md](README.md)
👤 **Author**: [Jimi](https://jimi.ink/)

---

## Why Open Source

Writing AI strategy reports has long been the territory of BCG / McKinsey / top consulting firms — methodologies locked away in private engagements, inaccessible to most practitioners.

But **everyone in every industry is asking the same questions**:

- Where can AI actually apply in my industry?
- Is it too late to start? How much should I invest?
- What pitfalls have others hit that I can avoid?
- How can I think this through myself before paying a consultant to tell me?

This skill open-sources (with full client desensitization) the methodology + anti-patterns + self-check cheatsheets accumulated from real AI strategy engagements.

**The goal**: enable any industry practitioner (tech / healthcare / education / manufacturing / logistics / retail / agriculture / engineering / government / ...) to use Claude to quickly explore "what AI applications make sense for my industry" — no consulting firm needed, no million-dollar budget required. Just a browser + Claude Code.

If you use this skill to produce interesting AI strategy thinking, share it in [GitHub Discussions](../../discussions) (any industry, any outcome). **Let's make AI strategy accessible to all.**

---

## What This Skill Solves

AI strategy reports easily turn into "looks complete, actually empty" decks — all tables, stacked RAG/Agent jargon, every recommendation marked "high value, low difficulty", no "what we won't do" section, the AI talking to itself the whole way through.

This skill solves that with three layers:

1. **2-Step main flow**: Step 1 explore directions (open, no premature filtering) → Step 2 write the strategy report (default 7 chapters, strict structure)
2. **5 Hard Constraints (H1-H5)**: tables ≤ 25%, ≥ 2 paragraphs of prose per chapter, recommendations need concrete anchors, benchmarks follow a strict format, must include a "trade-offs" section
3. **Checkpoint Protocol**: after every chapter the AI must surface its doubts and wait for user confirmation — no one-shot drafting

---

## When to Use

| Scenario | Client Type | Flow |
|---|---|---|
| Draft AI strategy / Copilot proposal for a tech company | Internet / startup / internal team | Step 1 → Step 2 |
| Explore "what AI can do in our industry" | Internal teams in any industry | Step 1 alone |
| Direction already chosen, write a formal AI strategy doc | Board / executive scenarios | Step 2 directly |
| Write AI strategy for SOE / government / engineering / regulated clients | Regulated, formal procurement process | Step 1 → Step 2 + enable ROI / policy add-ons |
| Review an existing AI strategy draft | Any existing draft | Standalone review (use anti-pattern reference) |

**Not for**: general IT consulting / pure technical proposals / document beautification (use other skills).

---

## Quick Start

### 1. Install

```bash
# macOS / Linux
git clone https://github.com/li2092/ai-strategy-consulting.git \
  ~/.claude/skills/ai-strategy-consulting

# Windows (PowerShell)
git clone https://github.com/li2092/ai-strategy-consulting.git `
  $env:USERPROFILE\.claude\skills\ai-strategy-consulting
```

Restart Claude Code; the skill auto-loads.

### 2. Trigger

In Claude Code, say any of these to activate the skill:

**Step 1 explore directions** (when the direction isn't decided yet):
- "What can AI do in our [industry]?"
- "Help me explore AI applications in [X industry]"
- "I want to see how AI fits into [Y scenario]"

**Step 2 write the strategy report** (when you've chosen the top directions and need a formal draft):
- "Help me write an AI strategy report for [client]"
- "Draft an AI transformation roadmap"
- "Write an AI Copilot / Agent strategy proposal"

**Review an existing draft**:
- "Run this AI strategy draft through the hard standards"
- "Check this with the anti-pattern reference"

**Universal keywords**: `AI strategy / AI consulting / AI roadmap / AI transformation / enterprise AI / Agent strategy / AI exploration`

### 3. Self-check (zero scripts)

This skill ships with no Python scripts. All self-checks rely on grep + manual review.
[`references/04-anti-patterns.md`](references/04-anti-patterns.md) ends with a complete grep cheatsheet you can copy and run.

---

## File Structure

```
ai-strategy-consulting/
├── SKILL.md                            # Main entry (Claude auto-loads)
├── README.md                           # Chinese version
├── README.en.md                        # This file
├── LICENSE                             # MIT
├── references/                         # Detailed methodology (loaded on demand)
│   ├── 01-step1-exploration.md            # Step 1 detailed method
│   ├── 02-step2-drafting.md               # Step 2 detailed method + default 7-chapter structure
│   ├── 03-strategy-depth.md               # 5 hard constraints (H1-H5) detail
│   ├── 04-anti-patterns.md                # P0-P4 anti-patterns reference + grep cheatsheet
│   ├── 05-language-discipline.md          # Anti-AI-slop / 3-tag discipline / sentence-paragraph control
│   ├── 06-checkpoint-protocol.md          # Checkpoint protocol (this skill's core mechanism)
│   ├── 07-review-thinking-model.md        # Review 4-layer cognitive model
│   ├── 08-unfamiliar-industry.md          # Unfamiliar-industry bootstrapping framework
│   ├── 09-output-formats.md               # MD → Word / PPT conversion paths
│   ├── add-on-roi.md                      # Optional · ROI calculation (SOE / engineering)
│   └── add-on-soe-policy.md               # Optional · Policy compliance (SOE / government)
└── assets/                             # Ready-to-fill templates
    ├── exploration-template.md            # Step 1 exploration document template
    └── report-template.md                 # Step 2 strategy report template
```

---

## Design Principles

1. **Zero scripts, zero external skill dependency** — install and use, no extra tooling needed
2. **Client desensitized** — all methodology, cases, numbers are generic; no named-client content
3. **Default benchmark: frontier tech companies** — does not assume the client is SOE / government; policy and ROI are opt-in add-ons
4. **Checkpoint enforces incremental review** — the AI surfaces doubts after every chapter to prevent "looks complete, actually empty"
5. **Anti-AI-slop / anti-threat / anti-self-citation / anti-cross-client** — four zero-tolerance categories

---

## Acknowledgments

Methodology framework draws on:

- BCG · 10-20-70 framework
- McKinsey · Steer-Scale-Institutionalize
- Barbara Minto · Pyramid Principle
- "On Looking Right" 4-layer cognitive architecture (L1 cause / L2 premise / L3 global / L4 structure) — used in the review 4-layer model

Battle-tested discipline distilled from the author's hands-on AI strategy engagements with multiple clients, external review records, and repeated diagnosis of the "looks right but actually isn't" problem.

---

## License

[MIT](LICENSE) — free for commercial use, modification, and redistribution; just keep the copyright notice.

---

## Contributing

Issues / PRs welcome. If you discover new anti-patterns or pitfalls, please file a GitHub Issue.

Especially welcomed:
- **New optional add-ons** (industry policy / industry ROI / industry-specific bootstrapping)
- **Anti-AI-slop rules in other languages**
- **Share interesting AI strategy thinking** built with this skill (Discussions)
