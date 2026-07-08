# -*- coding: utf-8 -*-
"""
把 blog 的笔记同步到 docs/ 目录，并自动生成首页 index.md。

目录结构（与 web 项目一致，方便 Typora 自动放图）：
    posts/    <- 所有 .md 笔记写在这里
    assets/   <- 每篇文章的图片放在 assets/<文章名>/，banner.jpg 放 assets/ 根
    stylesheets/ <- 自定义样式

你只管在 posts/ 下用 Typora 写笔记，其余交给 deploy.bat。
"""
import os
import shutil
import datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(ROOT, "docs")

POSTS = "posts"
ASSETS = "assets"
STYLESHEETS = "stylesheets"


def clean_docs():
    if os.path.exists(DOCS):
        shutil.rmtree(DOCS)
    os.makedirs(DOCS)


def copy_tree(name):
    """把根目录下的 name 文件夹整体复制进 docs/name。"""
    src = os.path.join(ROOT, name)
    if os.path.exists(src):
        shutil.copytree(src, os.path.join(DOCS, name))


def sync():
    # posts/ 里的 md 复制到 docs/posts/
    md_files = []
    posts_src = os.path.join(ROOT, POSTS)
    if os.path.exists(posts_src):
        os.makedirs(os.path.join(DOCS, POSTS), exist_ok=True)
        for name in os.listdir(posts_src):
            if name.lower().endswith(".md"):
                shutil.copy2(os.path.join(posts_src, name),
                             os.path.join(DOCS, POSTS, name))
                md_files.append(name)

    # assets/ 与 stylesheets/ 整体复制
    copy_tree(ASSETS)
    copy_tree(STYLESHEETS)

    return sorted(md_files)


def make_index(md_files):
    lines = [
        "---",
        "hide:",
        "  - navigation",
        "  - toc",
        "---\n",
        '<div class="hero">',
        '  <img src="assets/banner.jpg" alt="banner">',
        '  <div class="hero-text">',
        "    <h1>渗透测试学习笔记</h1>",
        "    <p>从零开始，记录我成为渗透测试工程师的学习历程</p>",
        "  </div>",
        "</div>\n",
        "## 📚 笔记列表\n",
    ]
    for f in md_files:
        title = f[:-3]  # 去掉 .md
        lines.append(f"- [{title}](posts/{f})")

    lines.append("\n---\n")
    lines.append("*持续更新中... | Last updated: "
                 + datetime.datetime.now().strftime('%Y-%m-%d') + "*")

    with open(os.path.join(DOCS, "index.md"), "w", encoding="utf-8") as fp:
        fp.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    clean_docs()
    files = sync()
    make_index(files)
    print(f"已同步 {len(files)} 篇笔记到 docs/")
    for f in files:
        print("  -", f)
