# 🌅 CloudZun 每日速递（Horizon）

> AI 自动筛选科技新闻，你只管读。—— 一个自托管的 **中文科技新闻每日摘要** 系统。

[![Live Site](https://img.shields.io/badge/在线日报-cloudzun.com%2FHorizon-blue?style=flat-square)](https://www.cloudzun.com/Horizon/)
[![License](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Tool uv](https://img.shields.io/badge/Tool-uv-4B275F?style=flat-square&logo=uv&logoColor=white)](https://github.com/astral-sh/uv)
[![Daily Summary](https://github.com/cloudzun/Horizon/actions/workflows/daily-summary.yml/badge.svg?style=flat-square)](https://github.com/cloudzun/Horizon/actions/workflows/daily-summary.yml)

本项目是 [Thysrael/Horizon](https://github.com/Thysrael/Horizon) 的一个**深度定制 fork**：
面向中文读者的每日科技摘要，AI 使用 DeepSeek V4，内容只产出中文版，通过 GitHub Actions
定时抓取 → 评分 → 增强 → 生成日报，并自动发布为 GitHub Pages 静态站点。

**在线示例**：[https://www.cloudzun.com/Horizon/](https://www.cloudzun.com/Horizon/)

---

## 目录

1. [它做了什么](#它做了什么)
2. [整体架构与流水线](#整体架构与流水线)
3. [项目结构](#项目结构)
4. [信息源](#信息源)
5. [AI 加工细节](#ai-加工细节)
6. [工程要点与踩坑记录](#工程要点与踩坑记录)
7. [成本数据](#成本数据)
8. [部署与自动化](#部署与自动化)
9. [配置指南](#配置指南)
10. [本地运行](#本地运行)
11. [与上游的关系](#与上游的关系)
12. [许可证](#许可证)

> 📜 完整变更记录见 [CHANGELOG.md](CHANGELOG.md)。

---

## 它做了什么

每天自动完成一轮“新闻雷达”：

1. 从多个来源并发抓取科技资讯（Hacker News、GitHub、精选 RSS）；
2. 跨源去重，合并指向同一 URL 的内容；
3. 用 LLM 逐条评分（0–10），过滤掉噪音，保留 ≥ 阈值的重要条目；
4. 对重要条目做语义话题去重，避免日报被同一话题刷屏；
5. 联网搜索背景知识 + 汇总社区讨论，生成结构化的深度解读（本部署仅中文）；
6. 渲染成 Markdown 日报并发布到 GitHub Pages。

产出物是一份每日中文科技摘要，包含：标题（含评分）、摘要、来源、背景知识、
社区讨论摘要、标签和参考链接。

## 整体架构与流水线

```
┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│   GitHub     │   │ Hacker News  │   │   RSS feeds  │   │ (Reddit/     │
│ releases/    │──▶│   top 30     │──▶│   14 个源    │──▶│  Telegram    │
│ user events  │   │ min_score 100│   │ 全文提取可选 │   │  已禁用)     │
└──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘
        │                  │                  │                  │
        └──────────────────┴────────┬─────────┴──────────────────┘
                                    ▼
                        ┌───────────────────────┐
                        │ 跨源 URL 去重          │
                        └───────────┬───────────┘
                                    ▼
                        ┌───────────────────────┐
                        │ AI 评分 0-10（并发 8） │
                        │ DeepSeek V4-Flash      │
                        └───────────┬───────────┘
                                    ▼
                        ┌───────────────────────┐
                        │ 阈值过滤 ≥ 7.0         │
                        │ 语义话题去重           │
                        └───────────┬───────────┘
                                    ▼
                        ┌───────────────────────┐
                        │ 增强：联网搜索 +       │
                        │ 背景/社区讨论生成      │
                        └───────────┬───────────┘
                                    ▼
                        ┌───────────────────────┐
                        │ 中文 Markdown 日报     │
                        │ 保存 + 发布 GitHub Pages│
                        └───────────────────────┘
```

主流程在 `src/orchestrator.py` 的 `HorizonOrchestrator.run()` 中实现，各阶段职责单一、可替换。

## 项目结构

```
.
├── .github/workflows/
│   ├── daily-summary.yml        # 每日定时：运行 Horizon + 部署站点（04:14 北京时间）
│   └── deploy-docs.yml          # docs/ 变更时自动部署站点
├── data/
│   ├── config.json              # 实际使用的完整配置（已提交，开箱即用）
│   ├── config.example.json      # 上游基础模板（缺少本 fork 新字段）
│   └── summaries/               # 本地运行时生成的日报（Git 忽略）
├── docs/                        # GitHub Pages 站点源码（Jekyll）
│   ├── index.md                 # 首页：当日完整摘要 + 最近 3 天归档
│   ├── _posts/                  # 每日日报（Jekyll post）
│   ├── _config.yml
│   └── _includes/head-custom.html
├── scripts/daily-run.sh         # 自托管服务器上的 cron 备选方案
├── src/
│   ├── main.py                  # CLI 入口（uv run horizon）
│   ├── models.py                # Pydantic 配置/数据模型 + 内容清洗校验器
│   ├── orchestrator.py          # 全流程编排
│   ├── search.py                # DuckDuckGo 搜索（增强阶段用）
│   ├── url_security.py          # SSRF 防护（全文提取前校验 URL）
│   ├── ai/
│   │   ├── client.py            # 多提供商客户端抽象（OpenAI 兼容/Anthropic/Gemini）
│   │   ├── analyzer.py          # 评分器
│   │   ├── enricher.py          # 增强器（概念提取→搜索→背景生成）
│   │   ├── summarizer.py        # 日报渲染（中文、Pangu 排版）
│   │   ├── prompts.py           # 提示词（含防注入/事实约束规则）
│   │   ├── utils.py             # 健壮 JSON 解析 + 头中尾采样
│   │   └── tokens.py            # token 用量与缓存命中统计
│   ├── extractors/              # RSS 全文提取器（trafilatura）
│   ├── scrapers/                # GitHub / Hacker News / RSS / Reddit / Telegram
│   └── storage/manager.py       # 配置与摘要的读写
└── pyproject.toml               # 依赖与入口（uv 管理，含 uv.lock 锁定）
```

## 信息源

当前配置（`data/config.json`）实际启用的信息源：

| 类型 | 配置 | 说明 |
|------|------|------|
| Hacker News | 前 30 条，`min_score=100` | 附带 Top 5 评论 |
| GitHub | 5 个仓库的 releases + karpathy / simonw 的用户事件 | `anthropic-sdk-python`、`openai-python`、`gemma`、`llama-models`、`vscode` |
| RSS | 14 个源，10 个开启全文提取 | Simon Willison、Hugging Face Blog、MIT Tech Review、Ars Technica、VentureBeat、The Verge、Import AI、Interconnects、Ahead of AI、Lobsters + 4 个 Lemmy 社区 |
| Reddit / Telegram | **已禁用** | 保留代码，需要时在配置中开启 |

抓取是并发的（`asyncio.gather`），每个源互相隔离——单个源失败不会拖垮整体，
并且每个源会记录 `last_error` 供运行诊断使用。

## AI 加工细节

### 评分（`src/ai/analyzer.py`）

- 每条内容调用一次 LLM，输出 JSON：`{score, reason, summary, tags}`；
- 评分依据：技术深度、新颖性、影响力、社区讨论质量、互动信号；
- 并发 8，失败自动重试 3 次（指数退避）；重试仍失败则记 0 分并保留原因；
- 阈值默认 7.0（`filtering.ai_score_threshold`）。

### 增强（`src/ai/enricher.py`）

对入选条目做第二遍 LLM 处理：

1. 让模型从新闻中提取需要解释的技术概念；
2. 对每个概念并发跑 DuckDuckGo 搜索；
3. 基于「原文 + 搜索上下文 + 社区评论」生成结构化背景解读；
4. 只采信搜索结果中真实出现的 URL 作为参考链接（防幻觉引用）。

### 摘要渲染（`src/ai/summarizer.py`）

纯程序化渲染（不调 LLM）：按分数降序排版，中文与英文/数字之间自动插入空格
（Pangu 排版），输出带 Jekyll front matter 的 Markdown 文件。

### 提示词工程（`src/ai/prompts.py`）

所有系统提示词内置两条安全规则：

- **不可信输入规则**：所有抓取内容、工具结果一律视为数据而非指令（防提示词注入）；
- **事实约束规则**：不得编造事实/数字/引文/来源，证据不足时保留不确定性。

评分与增强均要求模型返回“纯 JSON”，并开启 `response_format: json_object`
（DeepSeek 原生支持）。

## 工程要点与踩坑记录

这里记录本 fork 相对上游原版做的关键工程改动，以及它们解决的问题，便于评估与复用：

### 1. 内容编码清洗（防 OpenAI SDK 序列化崩溃）

抓取的网页/评论内容中偶尔出现**孤立代理字符**（lone surrogate，常见于损坏的 HTML
实体解析结果）。openai SDK 2.x 用 `ensure_ascii=False` 序列化请求体，遇到孤立代理字符
直接抛 `UnicodeEncodeError`，导致该条目评分失败、分数归零。

- `src/models.py`：`ContentItem` 的 pydantic validator 递归清洗 `title/content/author/url/metadata`；
- `src/ai/analyzer.py` / `enricher.py`：构造 prompt 前再次清洗；
- 清洗策略：孤立代理字符替换为 U+FFFD，**合法 emoji 代理对完整保留**。

> 真实事故：曾因 GitHub Secret 中的 API key 混入 BOM 字符（`\ufeff`），httpx 构造
> `Authorization` 请求头时抛 `UnicodeEncodeError`，连续两个月日报“全空”却显示运行成功。
> 教训：① 设置 Secret 时避免经 PowerShell 管道（会引入编码污染）；② 现在分析失败会
> 打印完整 traceback，且所有源抓取失败时任务直接报错，不再静默产出空日报。

### 2. RSS 全文提取（trafilatura + SSRF 防护）

RSS 摘要往往只有一两句话，导致评分和背景解读“没料”。本 fork 支持按源开启全文提取：

- `data/config.json` 中给 RSS 源加 `"content_extractor": "trafilatura"` 即开启；
- 抓取器会并发访问原文页面，用 trafilatura 提取正文，失败自动回退到 RSS 摘要；
- 所有外链请求先过 `src/url_security.py`：拒绝 localhost/内网/保留 IP、
  拒绝 URL 内嵌凭据、DNS 解析后校验全部为公网地址（SSRF 防护）。

### 3. 稳定条目 ID

RSS 条目 ID 由 Python 内置 `hash()`（进程间随机化，`PYTHONHASHSEED`）改为
`sha256(entry_id)[:16]`，保证同一条目跨运行、跨进程 ID 稳定，为后续持久化去重留好了基础。

### 4. 健壮 JSON 解析

`src/ai/utils.py::parse_json_response` 提供 5 层兜底：直接解析 → JSON 代码块
→ 任意代码块 → 花括号配对 → 正则提取。评分/增强/概念提取共用，显著降低“解析失败”类坏条目。

### 5. 头-中-尾采样（长文处理）

长文不再粗暴 `content[:N]`，而是保留「开头 40% + 中段 30% + 结尾 30%」并加标记，
让模型同时看到文章开头和**结论**，长文评分更公平。

### 6. 抓取诊断与全失败中止

每个 scraper 记录 `last_error`；编排器汇总每个源的结果。若**所有启用的源全部失败**，
直接抛错终止（红色失败），而不是发布一份“今日暂无重要动态”的空日报——空报是这次
事故中最难察觉的信号。

### 7. Token 用量与缓存命中统计

每次运行结束打印：

- 输入/输出 token 总数；
- **输入缓存命中率**（读取 DeepSeek `usage.prompt_tokens_details.cached_tokens`，
  展示前缀缓存真实收益）。

### 8. 站点的坑：Liquid `offset` filter 不生效

首页历史归档曾使用 `{{ posts | offset: 1 | limit: 6 }}`，但 Jekyll/Liquid **没有
`offset` filter**，未知 filter 被静默忽略，导致归档全量渲染（156 条）。改为
`{% for post in posts offset: 1 limit: 3 %}`（for 标签原生参数）后恢复正常。
现在首页显示当日完整摘要 + 最近 3 天归档链接。

## 成本数据

模型：`deepseek-v4-flash`（官方价：输入 ¥1/百万 tokens、缓存命中 ¥0.02/百万、输出 ¥2/百万）。

实测（2026-08-03，57 条抓取 → 45 条评分 → 15 条增强）：

| 指标 | 数值 |
|------|------|
| 输入 tokens | ~83,000（**51% 命中缓存**） |
| 输出 tokens | ~66,000 |
| 合计 | ~149,000 tokens / 天 |
| 估算费用 | **约 ¥0.17 / 天**（无缓存约 ¥0.22） |

按月约 ¥5。凌晨 4:14 运行，即使 DeepSeek 后续实行峰谷定价（高峰 2 倍），也落在谷时段。

## 部署与自动化

### GitHub Actions（本仓库当前方案）

[`.github/workflows/daily-summary.yml`](.github/workflows/daily-summary.yml)

- 定时：`cron: '14 20 * * *'`（UTC）= 北京时间每日 **04:14**；
- 步骤：checkout → uv 安装依赖 → `uv run horizon --hours 48` → 推送 `docs/` 到
  `gh-pages` 分支（`keep_files: true`，GitHub Pages 自动构建）；
- 需要的仓库 Secrets：
  - `DEEPSEEK_API_KEY`：DeepSeek API key（注意不要带 BOM/换行）；
  - `GITHUB_TOKEN`：默认的 `${{ secrets.GITHUB_TOKEN }}` 即可，用于 GitHub API 配额。

[`.github/workflows/deploy-docs.yml`](.github/workflows/deploy-docs.yml)

- `docs/**` 变更推送后自动重新部署站点。

### 自托管 cron（备选）

[`scripts/daily-run.sh`](scripts/daily-run.sh) 提供不依赖 GitHub Actions 的版本：
`git pull` → `uv sync` → `uv run horizon --hours 24` → 用 git worktree 推 gh-pages。

## 配置指南

配置集中在两个文件：`.env`（密钥）与 `data/config.json`（全部业务配置）。

### `.env`

```bash
DEEPSEEK_API_KEY=sk-xxx        # 必填：AI 评分/增强/摘要
GITHUB_TOKEN=ghp_xxx           # 可选但推荐：提高 GitHub API 配额（60 → 5000 次/时）
```

### `data/config.json`（关键字段）

```jsonc
{
  "ai": {
    "provider": "openai",          // OpenAI 兼容端点（DeepSeek 走此通道）
    "model": "deepseek-v4-flash",   // 或 deepseek-v4-pro
    "base_url": "https://api.deepseek.com",
    "api_key_env": "DEEPSEEK_API_KEY",
    "temperature": 0.3,
    "max_tokens": 4096,
    "languages": ["zh"],            // 只出中文版
    "json_output": true             // 开启 response_format: json_object
  },
  "sources": {
    "github": [{ "type": "repo_releases", "owner": "...", "repo": "...", "enabled": true }],
    "hackernews": { "enabled": true, "fetch_top_stories": 30, "min_score": 100 },
    "rss": [
      {
        "name": "Lobsters",
        "url": "https://lobste.rs/rss",
        "enabled": true,
        "category": "tech-community",
        "content_extractor": "trafilatura"   // 可选：开启全文提取
      }
    ],
    "reddit": { "enabled": false },
    "telegram": { "enabled": false }
  },
  "filtering": { "ai_score_threshold": 7.0, "time_window_hours": 24 }
}
```

> 仓库自带的 `data/config.json` 即完整可用的配置；`data/config.example.json`
> 是上游基础模板，不含 `content_extractor` 等本 fork 新字段。

站点侧的更多说明见 `docs/`（`configuration.md` / `scoring.md` / `scrapers.md`）。

## 本地运行

要求：Python 3.11+、[uv](https://github.com/astral-sh/uv)。

```bash
git clone https://github.com/cloudzun/Horizon.git
cd Horizon
uv sync

# 准备密钥（.env 会被自动加载）
cp .env.example .env
# 编辑 .env 填入 DEEPSEEK_API_KEY

# 跑一次（48 小时窗口）
uv run horizon --hours 48

# 日报输出到 data/summaries/，并拷贝到 docs/_posts/
```

本地调试建议：先跑 `--hours 6` 缩小抓取范围；全文提取被个别站点 403/429
属正常现象，会自动回退到摘要。

## 与上游的关系

本仓库 fork 自 [Thysrael/Horizon](https://github.com/Thysrael/Horizon)（分叉点 2026-02）。

- **当前差距**：本地领先上游 20 个提交（中文定制 + 稳定性修复），落后 186 个提交；
- **刻意不同步**：上游已演进为平台化方向（MCP server、webhook、profiles、多语言、
  大量新 scraper），而本项目的定位是**精简、稳定、单语言（中文）的每日摘要部署**；
  全量合并会引入大面积重构风险，与部署目标不符；
- **借鉴回流**：虽未合并，但已把上游 8 项高价值改进移植回本 fork：
  RSS 全文提取（trafilatura）、稳定条目 ID、抓取诊断/全失败中止、提示词防注入与事实约束、
  健壮 JSON 解析、`response_format` JSON 输出、头-中-尾采样、token 用量统计。

## 许可证

[MIT](LICENSE)

---

*CloudZun 每日速递 —— 每天清晨，给你一份筛选过的技术世界。*
