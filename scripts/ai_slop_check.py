#!/usr/bin/env python3
"""
ai_slop_check.py · 反 AI 腔自检脚本

扫描 Markdown 文件，识别高风险词、套话过渡、排比三连、设问开头等 AI 腔表现。

用法：
    python ai_slop_check.py <markdown_file>
    python ai_slop_check.py 主报告.md

输出：
    - 命中数 + 详细位置
    - 命中类别统计
    - 通过标准：< 5 处全文
"""

import sys
import re
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

HIGH_RISK_PATTERNS = {
    "万能动词": [
        r"赋能", r"打造", r"助力", r"深耕", r"驱动", r"引领",
    ],
    "空洞名词": [
        r"闭环", r"抓手", r"沉淀", r"生态(?!环境|系统的)",
        r"底座", r"底层逻辑", r"颗粒度", r"心智", r"维度", r"链路",
        r"矩阵(?!图|表)", r"范式",
    ],
    "套话过渡": [
        r"综上所述", r"由此可见", r"不言而喻", r"众所周知",
        r"值得注意的是", r"不难发现", r"不难看出", r"总而言之",
    ],
    "时代修辞": [
        r"在数字化转型的浪潮中", r"在 ?AI ?时代的大背景下",
        r"随着.*?的深入推进", r"随着.*?的不断发展",
        r"在这个.*?的时代",
    ],
    "排比三连": [
        r"首先.*?其次.*?最后",
        r"不是.*?，?不是.*?，?不是.*?——?而是",
    ],
    "设问开头": [
        r"^.*?那么.*?是.*?呢？",
        r"^.*?为什么.*?需要.*?呢？",
        r"^.*?到底是什么？",
    ],
    "假亲切": [
        r"本能地", r"自然而然", r"懂的人都懂",
    ],
    "形容词堆砌": [
        r"全面.*系统.*科学.*高效",
        r"系统.*科学.*高效.*精准",
    ],
}


def check_file(filepath):
    path = Path(filepath)
    if not path.exists():
        print(f"❌ 文件不存在: {filepath}")
        return False

    content = path.read_text(encoding="utf-8")
    lines = content.split("\n")

    total_hits = 0
    category_counts = {}
    detail_hits = []

    for i, line in enumerate(lines, 1):
        if not line.strip() or line.startswith("```"):
            continue

        for category, patterns in HIGH_RISK_PATTERNS.items():
            for pattern in patterns:
                matches = re.finditer(pattern, line)
                for m in matches:
                    total_hits += 1
                    category_counts[category] = category_counts.get(category, 0) + 1
                    detail_hits.append({
                        "line": i,
                        "category": category,
                        "match": m.group(),
                        "context": line.strip()[:100],
                    })

    # 输出
    print(f"\n{'='*60}")
    print(f"反 AI 腔自检 · {path.name}")
    print(f"{'='*60}")
    print(f"总命中: {total_hits} 处")
    print(f"通过标准: < 5 处全文")
    print(f"判定: {'✅ 通过' if total_hits < 5 else '❌ 未通过' if total_hits < 15 else '❌❌ 严重未通过'}")

    if category_counts:
        print(f"\n--- 类别统计 ---")
        for cat, cnt in sorted(category_counts.items(), key=lambda x: -x[1]):
            print(f"  {cat}: {cnt}")

    if detail_hits:
        print(f"\n--- 详细位置（前 30 处）---")
        for h in detail_hits[:30]:
            print(f"  L{h['line']} [{h['category']}] '{h['match']}' → {h['context']}")
        if len(detail_hits) > 30:
            print(f"  ...（共 {len(detail_hits)} 处，仅显示前 30 处）")

    return total_hits < 5


def main():
    if len(sys.argv) != 2:
        print("用法: python ai_slop_check.py <markdown_file>")
        sys.exit(1)

    success = check_file(sys.argv[1])
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
