#!/usr/bin/env python3
"""
cross_client_check.py · 跨客户内容入稿检测

扫描 Markdown 文件，识别可能违反客户保密 / 项目边界的内容：
- 具名客户（公司名、品牌名、项目名）出现在不该出现的位置
- 项目组自身活动 / 工具 / 经验作为外部论据
- 自证式叙事

用法：
    python cross_client_check.py <markdown_file>
    python cross_client_check.py <markdown_file> --client "[本客户名]"
    python cross_client_check.py <markdown_file> --client "[本客户名]" --extra-names "[A 公司,B 公司,C 公司]"

参数：
    --client       本客户全称（命中本客户名的引用会被过滤掉，视为合规）
    --extra-names  逗号分隔的外部已知客户/项目组工具名，用于补强检测
                   （建议传入项目组服务过的其他客户简称，避免被误带入本稿）

输出：
    - 高风险位置 + 命中类别
    - 通过标准：0 处命中（P0 级问题）
"""

import sys
import re
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

# 项目组自证式表述
SELF_REFERENCE_PATTERNS = [
    (r"我们(?:已)?(?:服务|开发|验证|积累|实战)", "项目组自证"),
    (r"本项目组(?:已)?(?:服务|开发|验证|积累)", "项目组自证"),
    (r"项目组(?:已)?(?:服务|开发|验证|积累|开发的)", "项目组自证"),
    (r"我们的(?:工具|经验|案例|skill|平台)", "项目组工具"),
    (r"已在.*?(?:实战|实战验证|落地验证)", "实战验证表述"),
    (r"千份级|万份级|N\s?份|多份.*?(?:实战|验证)", "数据规模表述"),
    (r"已经过.*?(?:客户|项目)?.*?(?:验证|落地)", "已验证表述"),
]

# 具名跨客户引用（通用规则，不写死任何公司名）
# 1) 外国公司具名 + 强动作动词 —— 用大写字母开头的英文名 + 中文动词通用匹配
# 2) 中文具名公司的工具/系统 —— 通过 --extra-names 参数注入项目组关心的清单
CROSS_CLIENT_PATTERNS = [
    (r"[A-Z][a-zA-Z]{3,}(?:已开发|已验证|已实战|内部已用)", "外国公司具名 + 强动作"),
    (r"[A-Za-z一-龥]{2,8}的\s?[A-Za-z一-龥]+(?:skill|Skill|SKILL)", "具名实体的具名 skill"),
    (r"(?:某客户|本客户|项目组)(?:已)?(?:开发|验证|实战|内部已用)的\s?[A-Za-z一-龥]+(?:工具|平台|系统)", "项目组工具自证"),
]

# 自媒体腔（容易暴露身份）
SELF_PROMOTION_PATTERNS = [
    (r"主题分享|圆桌讨论|主旨演讲", "公开活动"),
    (r"(?:研学会|沙龙|论坛|大会).*?(?:分享|发表|演讲)", "公开活动"),
]


def check_file(filepath, client_name=None, extra_names=None):
    path = Path(filepath)
    if not path.exists():
        print(f"❌ 文件不存在: {filepath}")
        return False

    content = path.read_text(encoding="utf-8")
    lines = content.split("\n")

    extra_patterns = []
    if extra_names:
        for name in extra_names:
            name = name.strip()
            if name:
                extra_patterns.append(
                    (rf"{re.escape(name)}(?:已开发|已验证|已实战|内部已用|的[一-龥A-Za-z]+(?:工具|skill|平台|系统))",
                     f"用户提供的外部具名: {name}")
                )

    hits = []
    in_code_block = False

    for i, line in enumerate(lines, 1):
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        if not line.strip():
            continue

        # 1. 检查项目组自证
        for pattern, category in SELF_REFERENCE_PATTERNS:
            for m in re.finditer(pattern, line):
                hits.append({
                    "line": i,
                    "severity": "P0",
                    "category": category,
                    "match": m.group(),
                    "context": line.strip()[:120],
                })

        # 2. 检查具名跨客户引用（内置通用规则 + 用户传入的具名清单）
        for pattern, category in CROSS_CLIENT_PATTERNS + extra_patterns:
            for m in re.finditer(pattern, line):
                # 如果有客户名参数，过滤掉本客户的合理引用
                matched = m.group()
                if client_name and client_name in matched:
                    continue
                hits.append({
                    "line": i,
                    "severity": "P0",
                    "category": category,
                    "match": matched,
                    "context": line.strip()[:120],
                })

        # 3. 检查自媒体腔
        for pattern, category in SELF_PROMOTION_PATTERNS:
            for m in re.finditer(pattern, line):
                hits.append({
                    "line": i,
                    "severity": "P1",
                    "category": category,
                    "match": m.group(),
                    "context": line.strip()[:120],
                })

    # 输出
    p0_hits = [h for h in hits if h["severity"] == "P0"]
    p1_hits = [h for h in hits if h["severity"] == "P1"]

    print(f"\n{'='*60}")
    print(f"跨客户内容入稿检测 · {path.name}")
    if client_name:
        print(f"本客户: {client_name}")
    print(f"{'='*60}")
    print(f"P0 命中: {len(p0_hits)} 处（必删）")
    print(f"P1 命中: {len(p1_hits)} 处（必改）")
    print(f"通过标准: P0 = 0 / P1 = 0")
    print(f"判定: {'✅ 通过' if len(hits) == 0 else '❌ 未通过（保密 / 项目边界风险）'}")

    if hits:
        print(f"\n--- 命中详情 ---")
        for h in hits:
            print(f"  L{h['line']} [{h['severity']}][{h['category']}] '{h['match']}'")
            print(f"           → {h['context']}")

    return len(hits) == 0


def main():
    if len(sys.argv) < 2:
        print("用法: python cross_client_check.py <markdown_file> "
              "[--client \"[本客户名]\"] "
              "[--extra-names \"A,B,C\"]")
        sys.exit(1)

    filepath = sys.argv[1]
    client_name = None
    extra_names = None
    if "--client" in sys.argv:
        idx = sys.argv.index("--client")
        if idx + 1 < len(sys.argv):
            client_name = sys.argv[idx + 1]
    if "--extra-names" in sys.argv:
        idx = sys.argv.index("--extra-names")
        if idx + 1 < len(sys.argv):
            extra_names = [x.strip() for x in sys.argv[idx + 1].split(",") if x.strip()]

    success = check_file(filepath, client_name, extra_names)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
