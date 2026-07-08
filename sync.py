# -*- coding: utf-8 -*-
"""
把 blog 根目录里的 .md 笔记和 .assets 图片文件夹同步到 docs/ 目录，
并自动生成一个首页 index.md（列出所有笔记）。
你只管在根目录用 Typora 写笔记，其余交给 deploy.bat。
"""
import os
import shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(ROOT, "docs")

# 这些文件/文件夹不当作笔记，不同步
SKIP_FILES = {"index.md"}
SKIP_DIRS = {"docs", ".git", "__pycache__"}
# 首页资源文件夹，需要同步
INDEX_ASSETS = "index.assets"
# 自定义样式文件夹，需要同步
STYLESHEETS = "stylesheets"


def clean_docs():
    if os.path.exists(DOCS):
        shutil.rmtree(DOCS)
    os.makedirs(DOCS)


def sync():
    md_files = []
    for name in os.listdir(ROOT):
        path = os.path.join(ROOT, name)
        # 复制 markdown 笔记
        if os.path.isfile(path) and name.lower().endswith(".md") and name not in SKIP_FILES:
            shutil.copy2(path, os.path.join(DOCS, name))
            md_files.append(name)
        # 复制同名 .assets 图片文件夹
        elif os.path.isdir(path) and name.endswith(".assets") and name not in SKIP_DIRS:
            shutil.copytree(path, os.path.join(DOCS, name))

    # 复制首页资源文件夹
    index_assets_src = os.path.join(ROOT, INDEX_ASSETS)
    if os.path.exists(index_assets_src):
        index_assets_dst = os.path.join(DOCS, INDEX_ASSETS)
        if os.path.exists(index_assets_dst):
            shutil.rmtree(index_assets_dst)
        shutil.copytree(index_assets_src, index_assets_dst)

    # 复制自定义样式文件夹
    stylesheets_src = os.path.join(ROOT, STYLESHEETS)
    if os.path.exists(stylesheets_src):
        stylesheets_dst = os.path.join(DOCS, STYLESHEETS)
        if os.path.exists(stylesheets_dst):
            shutil.rmtree(stylesheets_dst)
        shutil.copytree(stylesheets_src, stylesheets_dst)

    return sorted(md_files)


def make_index(md_files):
    lines = [
        "---",
        "hide:",
        "  - navigation",
        "  - toc",
        "---\n",
        '<div class="hero">',
        '  <img src="index.assets/banner.jpg" alt="banner">',
        '  <div class="hero-text">',
        "    <h1>渗透测试学习笔记</h1>",
        "    <p>从零开始，记录我成为渗透测试工程师的学习历程</p>",
        "  </div>",
        "</div>\n",
        "## 📚 笔记列表\n",
    ]
    for f in md_files:
        title = f[:-3]  # 去掉 .md
        lines.append(f"- [{title}]({f})")

    lines.append("\n---\n")
    lines.append("*持续更新中... | Last updated: " + __import__('datetime').datetime.now().strftime('%Y-%m-%d') + "*")

    with open(os.path.join(DOCS, "index.md"), "w", encoding="utf-8") as fp:
        fp.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    clean_docs()
    files = sync()
    make_index(files)
    print(f"已同步 {len(files)} 篇笔记到 docs/")
    for f in files:
        print("  -", f)
