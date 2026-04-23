# AI Strategy Consulting · Claude Skill

> A Claude Code Skill for writing AI strategy consulting reports for enterprises (especially SOEs, central enterprises, and government clients).
> Distilled from 100+ pages of real client deliverables and multiple rounds of external review.

🌐 **中文版**: [README.md](README.md)
👤 **Author**: [Jimi](https://jimi.ink/)

---

## Why Open Source

Writing AI strategy reports has long been the territory of BCG / McKinsey / top consulting firms — methodologies locked away in private engagements, inaccessible to industry practitioners.

But everyone in every industry is asking the same questions:

- Where can AI actually apply in my industry?
- Is it too late to start? How much should I invest?
- What pitfalls have others hit that I can avoid?
- How can I think this through myself before paying a consultant to tell me?

This skill open-sources (with full client desensitization) the methodology + 13 anti-patterns + 3 Python check tools accumulated from real AI strategy engagements.

**The goal**: enable any industry practitioner (healthcare / education / manufacturing / logistics / retail / agriculture / ...) to use Claude (or their own approach) to quickly explore "what AI applications make sense for my industry" — no consulting firm needed, no million-dollar budget required. Just a browser + Claude Code.

If you use this skill to produce interesting AI strategy thinking, share it in [GitHub Discussions](../../discussions) (any industry, any outcome). **Let's make AI strategy accessible to all.**

### How We Deliver on the "Any Industry, No Consulting Firm Needed" Promise

Two key design decisions:

1. **Mode L · Lite Personal/Team Exploration** — You provide "industry + role + one-line pain point", and AI produces a 5-10 page exploration document in 0.5-1 day (industry overview + 8-15 AI candidate scenarios + Top 3 recommendations + first-step actions). No need for a 60-100 page formal strategy report.
2. **Unfamiliar Industry Bootstrapping Framework** — Your industry (pet hospitals / private elderly care / second-hand luxury / any long-tail vertical) isn't in the 10 pre-built templates? The framework establishes adequate domain understanding in 1-2 hours, then runs Mode L. **Framework first, examples second — templates aren't the boundary.**

---

## What This Skill Solves

13 most common pitfalls when writing AI strategy reports (battle-tested):

1. Fabricated equity-chain narratives
2. Cross-client content leakage (using Client A's internal data in Client B's report)
3. Self-citing external evidence (project team's own activities as "external validation")
4. Citation overreach (single-source methodology → "industry must-do")
5. Misapplied economic models (international platform pricing → SMB clients)
6. Stale data residue (main draft updated, supporting docs not)
7. Coarse strategic judgment ("path is blocked" — lazy expression)
8. Threat-based opportunity-cost narratives
9. AI premium assumption (clients won't pay more just because vendors use AI)
10. Second-person colloquialisms + media-style writing
11. High-risk vocabulary stacking (empower / build / closed-loop / lever / ...)
12. Triple parallelism / rhetorical question openings / cliché transitions
13. Quantity claims inconsistent with actual count

This skill provides: **complete methodology + 11-chapter main report skeleton + one-pager + PPT + 6 appendix types + 4 HTML chart templates + 3 Python self-check scripts** to help you avoid these pitfalls.

---

## When to Use

| Scenario | Typical Client | Recommended Mode |
|---|---|---|
| Writing AI strategy reports / AI transformation roadmaps | SOEs / central enterprises / government / industry leaders | Mode D → P → R |
| Feasibility assessment + ROI calculation for AI applications | Any pre-launch AI decision | Mode D or Mode L |
| AI Copilot / Agent / industry LLM / custom small-model strategy proposals | Engineering / finance / manufacturing / government | Mode D → P → R |
| Reviewing existing AI strategy drafts against hard consulting standards | Any consulting deliverable | Mode R · 4-layer review |
| **Industry insiders self-asking: how should AI fit into my industry?** | **Internal teams in any industry** | **Mode L · Lite** |
| **Bootstrapping unfamiliar industries** (long-tail verticals beyond pre-built templates) | **Individuals / small teams / cross-industry explorers** | **Mode L + Unfamiliar Industry Framework** |

**Not for**: general IT consulting / pure technical proposals / document beautification (use other skills).

---

## Quick Start

### 1. Install

Clone into your Claude Code skills directory:

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

In Claude Code, say any of:

**Mode L · Personal/Team Exploration** (0.5-1 day, no client engagement needed):
- "What can AI do in our [industry]?"
- "Help me explore AI applications in [X industry]"
- "I'm in [pet hospitals / private elderly care / second-hand luxury / ...], what can AI do for me?"
- "Draft an AI exploration document, 5-10 pages, by end of week"

**Mode D-P-R · Full Formal Report** (2-4 days, for clients/leadership):
- "Help me write an AI strategy report for X client"
- "Draft an AI transformation roadmap"
- "Evaluate AI Copilot feasibility in X industry"
- "Review this AI strategy draft against hard consulting standards"

**Universal keywords**: `AI strategy / AI consulting / AI roadmap / AI transformation / enterprise AI / Agent strategy / AI exploration`

### 3. Self-Check Scripts (pure Python stdlib, no pip install needed)

After drafting:

```bash
python scripts/ai_slop_check.py main-report.md      # AI-slop check (target < 5 hits)
python scripts/label_coverage.py main-report.md     # Three-tag coverage (target ≥ 85%)
python scripts/cross_client_check.py main-report.md --client "[Your Client Name]"
```

---

## File Structure

```
ai-strategy-consulting/
├── SKILL.md                       # Main entry (Claude auto-loads) · Mode L/D/P/R workflows
├── README.md                      # Chinese version
├── README.en.md                   # This file
├── LICENSE                        # MIT
├── references/                    # Detailed methodology (loaded on demand)
│   ├── 01-information-gathering.md   # 5-dim gathering + client context 7-items + 10 industry templates
│   ├── 02-frameworks.md              # BCG / McKinsey / 5 filters / Value 4-questions
│   ├── 03-report-architecture.md     # 11-chapter skeleton + 4 opening hooks
│   ├── 04-anti-patterns.md           # 13+ anti-patterns quick reference
│   ├── 05-roi-templates.md           # Lean / Standard / Heavy three-tier ROI
│   ├── 06-language-discipline.md     # Anti-AI-slop + anti-threat + Claim-Evidence-Implication
│   ├── 07-review-checklist.md        # 8-dim 51-item + 6-step + adversarial review
│   ├── 08-deliverable-formats.md     # Main report / one-pager / PPT / 6 appendices specs
│   ├── 09-visualization-templates.md # 4 HTML chart templates (blue-orange palette)
│   ├── 10-output-formats.md          # MD → Word / PPT / PDF tool paths
│   ├── 11-review-thinking-model.md   # Review 4-layer cognitive model (L1 cause / L2 premise / L3 global / L4 structure)
│   └── 12-unfamiliar-industry-framework.md  # Unfamiliar industry bootstrapping (any industry in 1-2 hours)
├── assets/                        # Ready-to-use templates
│   ├── main-report-template.md       # 11-chapter main report template (Mode R)
│   ├── one-pager-template.md         # 4-quadrant one-pager template (Mode R)
│   ├── ppt-outline-template.md       # 20+6 PPT template (Mode R)
│   └── lite-mode-template.md         # Mode L · 5-10 page exploration document template
└── scripts/                       # Python check scripts (stdlib only)
    ├── ai_slop_check.py
    ├── label_coverage.py
    └── cross_client_check.py
```

---

## Design Principles

1. **Zero external skill dependency** — no need to install other skills
2. **Zero third-party Python dependency** — scripts use only sys / re / pathlib
3. **Client-desensitized** — all methodology, cases, and numbers are generic; no named client content
4. **Self-contained methodology + templates + check tools** — but "last mile" (Word / PPT / screenshots) is left to your local toolchain
5. **Critical discipline** — anti-AI-slop, anti-threat-narrative, anti-self-citation, anti-cross-client leakage; four zero-tolerance categories

---

## Acknowledgments

Methodology framework draws on:

- BCG · 10-20-70 framework (2025)
- McKinsey · Steer-Scale-Institutionalize
- MIT Sloan + BCG · Agentic Enterprise four tensions (2025)
- Barbara Minto · Pyramid Principle
- "On Looking Right" 4-layer cognitive architecture (L1 cause / L2 premise / L3 global / L4 structure) — used in the review 4-layer model (`references/11-review-thinking-model.md`)

Battle-tested discipline (13 anti-patterns + 6-step review + adversarial self-review + 4-layer review + unfamiliar industry framework) distilled from the author's hands-on AI strategy engagements with SOE clients, external review records, and repeated diagnosis of the "looks right but actually isn't" problem.

---

## License

[MIT](LICENSE) — free for commercial use, modification, and redistribution; just keep the copyright notice.

---

## Contributing

Issues / PRs welcome. If you discover new anti-patterns or pitfalls, please file a GitHub Issue.

Especially welcomed:

- **New industry ROI templates** (healthcare / education / retail / agriculture / logistics / ...)
- **New HTML chart templates**
- **Anti-AI-slop rules in other languages**
- **Share your interesting AI strategy thinking** built with this skill (to Discussions)
