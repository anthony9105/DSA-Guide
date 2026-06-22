#!/usr/bin/env python3
"""
add_new_problem.py — scaffold a new LeetCode problem folder + README.md

Usage (interactive):
    python add_new_problem.py

Usage (flags, skips prompts for anything provided):
    python add_new_problem.py --topic "Arrays and Strings" --num 1929 \
        --title "Concatenation of Array" \
        --url "https://leetcode.com/problems/concatenation-of-array/" \
        --difficulty Easy

Creates:
    <topic>/<num> <title>/README.md

"""

import argparse
import os

DIFFICULTY_COLORS = {
    "Easy": "brightgreen",
    "Medium": "orange",
    "Hard": "red",
}

LANGUAGES = ["Python", "C++", "Java", "TypeScript", "C#"]
LANG_FENCE = {
    "Python": "python",
    "C++": "cpp",
    "Java": "java",
    "TypeScript": "typescript",
    "C#": "csharp",
}

TEMPLATE = """<p align="center">
  <img src="{logo_path}" alt="Leetcode Logo" height="100px"/>
  <h1 align="center" style="font-size: 35px"><a href="{url}" target="_blank" rel="noreferrer">{num}. {title}</a></h1>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Difficulty-{difficulty}-{color}" alt="Difficulty: {difficulty}"/>
</p>

<p>{{ TODO: paste problem description here }}</p>

<details>
<summary><em>Examples and Constraints</em></summary>
<br/>

Example 1
<pre><strong>Input:</strong> {{ TODO }}
<strong>Output:</strong> {{ TODO }}
<strong>Explanation:</strong> {{ TODO }}
</pre>

Constraints:
<ul>
\t<li>{{ TODO }}</li>
</ul>

</details>

<br/>

## **Solution**

| Time | Space |
|------|-------|
| `O()` | `O()` |

- {{ TODO: explain approach, step by step }}

<br/>

## **Code**

{code_blocks}
"""

CODE_BLOCK_TEMPLATE = """{lang}
```{fence}
{{ TODO: paste solution here }}
```
<br/>
"""


def build_code_blocks() -> str:
    blocks = [
        CODE_BLOCK_TEMPLATE.format(lang=lang, fence=LANG_FENCE[lang])
        for lang in LANGUAGES
    ]
    # drop trailing <br/> on the very last block so the file doesn't end with stray spacing
    blocks[-1] = blocks[-1].rsplit("\n<br/>", 1)[0] + "\n"
    return "\n".join(blocks)


def prompt(label: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    val = input(f"{label}{suffix}: ").strip()
    return val or default


def main():
    parser = argparse.ArgumentParser(description="Scaffold a new LeetCode problem README.")
    parser.add_argument("--topic", help="Topic folder, e.g. 'Arrays and Strings'")
    parser.add_argument("--num", help="Folder sequence number, e.g. 1 (your own ordering, not LeetCode's)")
    parser.add_argument("--leetcode-num", help="LeetCode's official problem number, e.g. 2239")
    parser.add_argument("--title", help="Problem title, e.g. 'Roman to Integer'")
    parser.add_argument("--url", help="Full LeetCode problem URL (required)")
    parser.add_argument("--difficulty", choices=["Easy", "Medium", "Hard"], help="Difficulty")
    parser.add_argument("--logo-depth", type=int, default=2,
                         help="How many '../' to reach LC_logo.png from the new file (default: 2)")
    parser.add_argument("--root", default=".", help="Repo root to create the folder under (default: current dir)")
    args = parser.parse_args()

    topic = args.topic or prompt("Topic folder (e.g. 'Arrays and Strings')")
    num = args.num or prompt("Folder sequence number (e.g. 1 — your own ordering, not LeetCode's)")
    leetcode_num = args.leetcode_num or prompt("LeetCode problem number (e.g. 2239)")
    title = args.title or prompt("Problem title (e.g. 'Roman to Integer')")

    url = args.url
    while not url:
        url = prompt("LeetCode URL (required, e.g. 'https://leetcode.com/problems/roman-to-integer/')")
        if not url:
            print("   ⚠️  A LeetCode URL is required — please paste the problem link.")

    difficulty = args.difficulty or prompt("Difficulty (Easy/Medium/Hard)", "Easy")
    if difficulty not in DIFFICULTY_COLORS:
        difficulty = "Easy"

    logo_path = "../" * args.logo_depth + "LC_logo.png"
    folder_name = f"{num} {title}"
    folder_path = os.path.join(args.root, topic, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    content = TEMPLATE.format(
        logo_path=logo_path,
        url=url,
        num=leetcode_num,
        title=title,
        difficulty=difficulty,
        color=DIFFICULTY_COLORS[difficulty],
        code_blocks=build_code_blocks(),
    )

    readme_path = os.path.join(folder_path, "README.md")
    if os.path.exists(readme_path):
        print(f"⚠️  {readme_path} already exists — not overwriting.")
        return

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Created {readme_path}")
    print(f"   Don't forget to add a link to it in '{topic}/README.md' (or your topic index).")


if __name__ == "__main__":
    main()