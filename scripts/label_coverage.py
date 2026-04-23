#!/usr/bin/env python3
"""
label_coverage.py · 三标签覆盖率检查

扫描 Markdown 文件，识别"重要数字 / 重要判断"，检查其后是否带【事实/推断/假设】标签。

用法：
    python label_coverage.py <markdown_file>

输出：
    - 重要数字总数
    - 已标签数 / 未标签数
    - 覆盖率 %
    - 通过标准：≥ 85%
"""

import sys
import re
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

# 重要数字模式（需要带标签的数字类型）
IMPORTANT_NUMBER_PATTERNS = [
    (r"约\s?\d+(\.\d+)?\s?(万|亿|千万|百万|%|pp|个月|年|周)", "金额/比例/时间"),
    (r"\d+(\.\d+)?\s?(万元|亿元|百万元|千万元)", "金额"),
    (r"\d+(\.\d+)?\s?%", "百分比"),
    (r"ROI\s?约?\s?\d+", "ROI"),
    (r"\d+(\.\d+)?\s?倍", "倍数"),
    (r"提升|节约|降低|增长|压缩|提效\s?\d+", "效率改善"),
]

LABEL_PATTERNS = [
    r"【事实】",
    r"【推断】",
    r"【假设】",
    r"【事实[^】]*】",
    r"【推断[^】]*】",
    r"【假设[^】]*】",
    r"\[事实\]",
    r"\[推断\]",
    r"\[假设\]",
]

# 不需要标签的数字（章节号、序号、年份等）
SKIP_PATTERNS = [
    r"^#+ ",  # 标题行
    r"^\| ?\d+ ?\|",  # 表格序号列
    r"^\d+\. ",  # 列表序号
    r"^- \[",  # checkbox
    r"\d{4}[年-]",  # 年份（如 2026 年）
    r"M\d+",  # 月度编号
    r"Year \d+",  # 年份编号
    r"§\d+",  # 章节引用
    r"L\d+",  # 行号引用
]


def is_skip_line(line):
    for p in SKIP_PATTERNS:
        if re.search(p, line):
            return True
    return False


def has_label_nearby(line, content_lines, line_idx):
    """检查当前行或下一行是否有标签"""
    # 检查当前行
    for p in LABEL_PATTERNS:
        if re.search(p, line):
            return True
    # 检查下一行（标签可能在段落末尾或下一行）
    if line_idx + 1 < len(content_lines):
        for p in LABEL_PATTERNS:
            if re.search(p, content_lines[line_idx + 1]):
                return True
    return False


def check_file(filepath):
    path = Path(filepath)
    if not path.exists():
        print(f"❌ 文件不存在: {filepath}")
        return False

    content = path.read_text(encoding="utf-8")
    lines = content.split("\n")

    important_numbers = []
    in_code_block = False

    for i, line in enumerate(lines):
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        if is_skip_line(line):
            continue

        for pattern, num_type in IMPORTANT_NUMBER_PATTERNS:
            matches = re.finditer(pattern, line)
            for m in matches:
                important_numbers.append({
                    "line": i + 1,
                    "type": num_type,
                    "match": m.group(),
                    "context": line.strip()[:100],
                    "has_label": has_label_nearby(line, lines, i),
                })

    total = len(important_numbers)
    labeled = sum(1 for n in important_numbers if n["has_label"])
    unlabeled = total - labeled
    coverage = (labeled / total * 100) if total > 0 else 100.0

    # 输出
    print(f"\n{'='*60}")
    print(f"三标签覆盖率检查 · {path.name}")
    print(f"{'='*60}")
    print(f"重要数字总数: {total}")
    print(f"已标签: {labeled}")
    print(f"未标签: {unlabeled}")
    print(f"覆盖率: {coverage:.1f}%")
    print(f"通过标准: ≥ 85%")
    print(f"判定: {'✅ 通过' if coverage >= 85 else '⚠️ 警告 (75-85%)' if coverage >= 75 else '❌ 未通过'}")

    if unlabeled > 0:
        print(f"\n--- 未标签的重要数字（前 30 处）---")
        unlabeled_items = [n for n in important_numbers if not n["has_label"]]
        for n in unlabeled_items[:30]:
            print(f"  L{n['line']} [{n['type']}] '{n['match']}' → {n['context']}")
        if len(unlabeled_items) > 30:
            print(f"  ...（共 {len(unlabeled_items)} 处未标签，仅显示前 30 处）")

    return coverage >= 85


def main():
    if len(sys.argv) != 2:
        print("用法: python label_coverage.py <markdown_file>")
        sys.exit(1)

    success = check_file(sys.argv[1])
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
