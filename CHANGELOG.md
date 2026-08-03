# Changelog

本项目的显著变更记录。格式遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)，
日期使用 `YYYY-MM-DD`。

## 2026-08-03 — 稳定性修复、上游借鉴与全面审查整改

### Added

- **AI 提供商切换到 DeepSeek V4**：`data/config.json` 使用 `deepseek-v4-flash`
  （OpenAI 兼容端点，`base_url=https://api.deepseek.com`）。
- **RSS 全文提取（trafilatura）**：按源开启 `content_extractor`，并发抓取原文
  正文，失败自动回退 RSS 摘要；外链请求带 SSRF 防护。
- **提示词加固**：所有系统提示词加入“不可信输入”与“事实约束”规则，防提示词注入。
- **健壮 JSON 解析**：`parse_json_response` 5 层兜底，评分/增强/概念提取共用。
- **JSON 输出模式**：OpenAI 兼容端点开启 `response_format: json_object`。
- **头-中-尾采样**：长文截断保留开头/中段/结尾，避免丢失结论。
- **Token 用量与缓存命中统计**：运行日志输出输入/输出 token 与输入缓存命中率。
- **内容编码清洗**：ContentItem 校验器与 prompt 构造处把孤立代理字符替换为
  U+FFFD（保留合法 emoji），防止 openai SDK 序列化崩溃。
- **XSS 消毒与 CSP**：日报渲染前对全部不可信文本做 Markdown/HTML 转义、链接
  scheme 白名单；站点新增 CSP meta 作为纵深防御。
- **AI 客户端显式超时**：OpenAI/Anthropic 60s、Gemini 60s。
- **并发抓取**：RSS feed 级（信号量 4）与 GitHub 源级（信号量 5）并行。
- **可配置并发**：`ai.analysis_concurrency` / `ai.enrichment_concurrency`。
- **抓取诊断与全失败中止**：每个源记录 `last_error`，所有源失败时任务直接报错，
  不再静默发布空日报。

### Changed

- **稳定 RSS 条目 ID**：由随机化的 Python `hash()` 改为 `sha256(entry_id)[:16]`。
- **历史归档只保留最近 3 天**：修复 Jekyll/Liquid `offset` filter 不生效导致
  归档全量渲染的问题，改用 `for` 标签原生 `offset/limit` 参数。
- **README 完整重写**：呈现架构、全部工程细节、配置、成本与部署方案。
- **仓库 About 更新**：描述、官网链接（cloudzun.com/Horizon）与 topics 改为本项目。
- **统一去重实现**：跨源去重与话题去重共用 `_merge_item_content`。
- **`data/config.example.json` 与 `main.py` 配置模板**更新为 DeepSeek 新 schema。

### Fixed

- 修复孤立代理字符导致的评分全部失败（编码问题）。
- 修复 GitHub Secret 中 API key 携带 BOM 导致的请求头序列化失败（部署侧）。
- 修复 enricher 并发搜索时全局 `sys.stderr` 竞态（加锁 + 工作线程执行）。
- 修复 `scripts/daily-run.sh` 中 `||`/`&&` 链在分支缺失时的错误行为。
- 修复 RSS 条目 ID 跨运行不稳定的隐患。

### Removed

- 删除无引用的死代码 `src/search.py`（HN/Reddit 搜索模块）。

## 2026-03-01 — Fork 定制初始化

从 [Thysrael/Horizon](https://github.com/Thysrael/Horizon) fork 并定制：

- 品牌改为 **CloudZun 每日速递**，只生成中文版日报；
- 信息源定制：新增 Lobsters、Lemmy 社区、Import AI / Interconnects / Ahead of AI
  等 RSS 源，用 RSS 替代 Reddit；
- 首页直接展示当日完整摘要，Jekyll 站点定制 header 布局；
- GitHub Actions 每日定时（北京时间 04:14）生成并发布日报到 GitHub Pages；
- 报告摘要行添加日期戳，修正 Jekyll `_posts` 文件名格式。

---

> 与上游 [Thysrael/Horizon](https://github.com/Thysrael/Horizon) 的关系与差异
> 见 [README「与上游的关系」](README.md#与上游的关系)。
