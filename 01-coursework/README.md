# 01 课程作业整理

目标：把学习过程变成可展示的作品，同时练熟 git/GitHub 基本功。

## 目录结构

```
01-coursework/
├── README.md          # 本文件：项目总说明
├── requirements.txt   # Python 依赖
├── .gitignore         # 忽略不需要提交的文件
└── assignments/       # 每个作业一个文件夹
    └── 01-python-basics/  # 示例：Python 基础练习
```

## 使用方式

1. 每次学习，在 `assignments/` 下建一个带编号的文件夹（如 `02-pandas-intro/`）
2. 文件夹里放：代码 + 简短说明（`notes.md`，写你学了什么、卡在哪）
3. 每天至少 `git add` + `git commit` 一次，保持提交记录连续

## git 常用命令速查

```bash
git status                    # 看当前状态
git add .                     # 暂存所有改动
git commit -m "完成xx练习"     # 提交（写清楚这次干了什么）
git log --oneline             # 看提交历史
```

## 提交规范

- 信息用中文或英文都行，但要写清楚：`git commit -m "python基础练习：完成函数和模块章节"`（格式：xx练习：完成xx内容）
- 不要提交大文件和密码（.gitignore 已处理常见情况）
