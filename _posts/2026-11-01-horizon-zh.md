---
layout: default
title: "Horizon 每日速递：2026-11-01"
date: 2026-11-01
lang: zh
---

> 📅 2026-11-01 · 从 53 条资讯中精选出 17 条重要内容

---

1. [HackerTube 将 HN 评论区推荐的视频做成 YouTube 风格站点](#item-1) <span class="score-badge score-mid">8.0</span>
2. [数学已经改变，数学家应当照此行动](#item-2) <span class="score-badge score-mid">8.0</span>
3. [巴西法院因法庭文件中的提示注入处罚律师](#item-3) <span class="score-badge score-mid">8.0</span>
4. [ChatGPT 制品沙箱逃逸：利用 MathLive postMessage 与 YouTube 绕过 CSP](#item-4) <span class="score-badge score-mid">8.0</span>
5. [Jepsen 对 ParticleDB 1\.1\.4 的分析发现 SQL 与事务异常](#item-5) <span class="score-badge score-mid">8.0</span>
6. [OmniDiff：基于 Rust 的内容感知 Git difftool 发布 v0\.3\.0](#item-6) <span class="score-badge score-mid">7.0</span>
7. [电网频率出现一分钟周期扰动，疑与设备定时同步有关](#item-7) <span class="score-badge score-mid">7.0</span>
8. [Nolan Lawson 谈 JavaScript 框架的 AI 成本](#item-8) <span class="score-badge score-mid">7.0</span>
9. [Kyle Kingsbury：LLM 正在侵蚀对软件、文档及其背后组织的信任](#item-9) <span class="score-badge score-mid">7.0</span>
10. [工程师批评 Anthropic 的 Scion，并将其与 Meta 的 Mononoke 对比](#item-10) <span class="score-badge score-mid">7.0</span>
11. [时钟同步的电池检查解释了电网 60 秒波动之谜](#item-11) <span class="score-badge score-mid">7.0</span>
12. [设计建议：避免公有函数调用其他公有函数](#item-12) <span class="score-badge score-mid">7.0</span>
13. [Ouros：无需软件运行时的 FPGA Haskell 处理器](#item-13) <span class="score-badge score-mid">7.0</span>
14. [Spooky C\+\+：悬空 string\_view 在 \-O2 下把 false 变成 true](#item-14) <span class="score-badge score-mid">7.0</span>
15. [在带符号 32 位整数除法上跑赢编译器](#item-15) <span class="score-badge score-mid">7.0</span>
16. [研究发现 x86\_64 PMU 计数器存在非确定性与重复计数](#item-16) <span class="score-badge score-mid">7.0</span>
17. [Org mode 的 LaTeX 预览被重写为异步缓存系统](#item-17) <span class="score-badge score-mid">7.0</span>

---

<a id="item-1"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://karpathy.bearblog.dev/hacker-tube/">HackerTube 将 HN 评论区推荐的视频做成 YouTube 风格站点</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">karpathy</span><span class="news-time">Oct 31, 19:56</span></div>
<p class="news-summary">Andrej Karpathy 分享了 HackerTube（hackertube.org）——一个把 Hacker News 评论中被推荐的 6,454 个视频，包装成 YouTube 风格浏览界面的项目。这些视频提取自可追溯至 2007 年的 39,834 条 HN 评论，发布后在 Hacker News 上引出了 530 条评论的讨论。 这个项目是“信息流解耦（feed disaggregation）”的一次具体示范：用可信社区明确推荐的信号重建内容流，而不是依赖平台为最大化参与度而优化的算法。如果这一思路可以推广，它就给希望由自己尊重的人来筛选内容、而非由追求观看时长的系统来筛选的读者提供了一个模板。 语料仅限于有人在 HN 评论中恰好分享过的视频，因此规模较小（6,454 条），并且会偏向近二十年里 HN 读者认为值得一提的内容。有评论者指出站点缺少“从新到旧”的排序选项（加进去并不难），还有用户基于同样思路做了一个面向书籍的版本。</p>
<div class="news-background"><strong>背景</strong> Hacker News 是由创业孵化器 Y Combinator 运营的科技新闻与讨论站点，内容聚焦计算机科学、创业，以及“任何能满足求知欲的东西”。它的评论区经常出现会议演讲、技术演示、课程讲座和纪录片的链接，但这些推荐通常埋在冗长的讨论页里。HackerTube 把这些提及抓取出来，重新组织成可浏览的视频流，用类似 YouTube 的前端呈现社区来源的链接。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hacker_News">Hacker News</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者普遍对“把推荐信息流拆解开来”的想法表示欢迎，有人认为现在的 LLM 已能承担大量排序与过滤工作，从而基于 RSS 等来源搭建个人信息流。也有人抱怨 YouTube 官方 App 难用、希望能有第三方客户端，并讨论 AI 生成软件是否比 AI 生成媒体更无害；还有人称赞该站点是“百分百纯极客内容”，没有网红视频和标题党，同时希望增加“从新到旧”的排序。</div>
<div class="news-tags"><span class="tag">#content-curation</span> <span class="tag">#recommendation-systems</span> <span class="tag">#Hacker News</span> <span class="tag">#YouTube</span> <span class="tag">#media</span></div>
</article>
<hr>

<a id="item-2"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://terrytao.wordpress.com/2026/11/01/mathematics-has-changed-lets-act-like-it/">数学已经改变，数学家应当照此行动</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">smilelamp</span><span class="news-time">Nov 1, 18:28</span></div>
<p class="news-summary">Terry Tao 发表博客文章，认为 AI 已经使数学发生改变，数学家应当相应调整自身的实践方式和规范。 Tao 是数学界最具影响力的声音之一，因此他的论点可能影响数学家、期刊和机构在 AI 辅助时代如何看待 credit、验证以及什么才算贡献。 摘要把这一变化描述为实践与规范的转变，而不仅是技术能力的变化，因此验证、credit 和贡献认定成为核心问题；所提供的摘录并未列出 Tao 的具体提议。</p>
<div class="news-background"><strong>背景</strong> AI theorem proving 是自动推理的一个子领域，研究计算机程序如何搜索或构造数学命题的证明。它既可以指全自动演绎，也可以指人机协作，而近年来的进展使其成为数学研究中的现实议题。这一点很重要，因为数学文化传统上把 credit 紧密地与人类提出证明思路联系在一起。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Automated_theorem_proving">Automated theorem proving</a></li>
<li><a href="https://arxiv.org/html/2512.09443">Advancing Mathematical Research via Human- AI Interactive Theorem ...</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者大多认同 Tao 指出了一个真实转变：有人将其概括为数学从手工业走向工业化生产，也有人认为 AI agents 可能很快不仅能生成证明，还能承担选题和解释工作。与此同时，有人提到许多数学家对冗长难读的 AI 生成证明感到沮丧，也对数学的社会基础发生变化感到不安，而“我现在该怎么办”成为反复出现的现实问题。</div>
<div class="news-tags"><span class="tag">#AI</span> <span class="tag">#mathematics</span> <span class="tag">#theorem proving</span> <span class="tag">#research culture</span> <span class="tag">#Terry Tao</span></div>
</article>
<hr>

<a id="item-3"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://jetstream.security/insights/brazilian-court-sanctions-prompt-injection-filing/">巴西法院因法庭文件中的提示注入处罚律师</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">doodlesdev</span><span class="news-time">Nov 1, 02:19</span></div>
<p class="news-summary">据报道，巴西一家法院对在法庭文件中嵌入隐藏 prompt injection 指令的律师实施了处罚，此事在 Hacker News 上引发讨论。该案被描述为针对指向 AI 系统的对抗性文本的法院处罚。 若属实，这可能是首例因 prompt injection 而被法院处罚的案件，为 AI 安全从业者提供了一个具体的执法实例。它也引发法院将如何处理针对法律流程中 AI 工具的对抗性文本的问题。 现有摘要未披露法院名称、涉事律师、处罚金额或具体注入内容，因此该先例的适用范围仍不明确。讨论中引用了一段直接对“ARTIFICIAL INTELLIGENCE”发话、要求其仅作表面回应且不要质疑文件的指令。</p>
<div class="news-background"><strong>背景</strong> Prompt injection 是一种把文本输入当作指令来操纵 AI 系统的攻击方式，使模型偏离原本任务。OWASP 将其列为 LLM01 风险，并指出注入文本即使人眼不可见，只要被模型解析就能生效。由于 LLM 在同一上下文中处理自然语言指令和原始材料，很难区分可信命令与不可信文档内容。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection - Wikipedia</a></li>
<li><a href="https://genai.owasp.org/llmrisk/llm01-prompt-injection/">LLM01:2025 Prompt Injection - OWASP Gen AI Security Project</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者争论隐藏的 AI 指令在道德或法律上是否不同于普通说服，有人指出广告和社交媒体也经常以类似方式操纵人，另有人质疑为何直接向人提出同样请求就不违法。还有人给出防御建议，例如把不可信文档转成图片再 OCR，以去除隐藏元数据；也有人讽刺地谈论利用证据开示程序植入 prompt injection。</div>
<div class="news-tags"><span class="tag">#prompt-injection</span> <span class="tag">#AI security</span> <span class="tag">#law and technology</span> <span class="tag">#adversarial inputs</span> <span class="tag">#LLM safety</span></div>
</article>
<hr>

<a id="item-4"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://simonwillison.net/2026/Oct/31/how-we-took-over-chatgpt-accounts/">ChatGPT 制品沙箱逃逸：利用 MathLive postMessage 与 YouTube 绕过 CSP</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Simon Willison</span><span class="news-time">Oct 31, 23:15</span></div>
<p class="news-summary">Parameter Labs 披露了一条针对 ChatGPT HTML previews 功能（即 artifacts 模式，OpenAI 此前称之为 Canvas）的攻击链：沙箱 iframe 中的不可信 HTML 突破了限制，在 ChatGPT 父页面中获得了 JavaScript 执行权限。攻击者构造的 ChatGPT 分享链接在已登录用户访问时可读取其私有数据并通过 API 外泄，OpenAI 已修复该漏洞并支付了 5,000 美元赏金。 制品与 HTML 预览功能的初衷就是在用户已认证的会话旁运行第三方生成的代码，因此沙箱一旦被突破，整个功能的安全承诺便不复存在。由于攻击只需受害者打开一个 ChatGPT 分享链接，任何已登录用户都可能在未安装任何东西、未授予任何权限的情况下受到影响。 攻击链始于 OpenAI 用于图表支持的 JavaScript 库 MathLive，其虚拟键盘会监听来自父页面的 postMessage() 调用，而接收消息的代码使用 innerHTML，导致任何 frame（包括沙箱化的 HTML 预览）都能注入 HTML；注入的 HTML 又可插入一个没有沙箱限制的新 iframe。OpenAI 的 CSP 禁止内联脚本且只允许少数脚本域名，但 YouTube 在白名单中，其 oEmbed 端点可以把 JavaScript 反射回来并以可执行形式运行，之后通过图片引用外泄数据便轻而易举。</p>
<div class="news-background"><strong>背景</strong> HTML iframe 的 sandbox 属性允许站点在额外限制下运行不可信内容——将其视为唯一源、阻止脚本执行与表单提交、禁用大量浏览器 API——除非显式授予特定 token。Content Security Policy（CSP）是一种响应头，用于限定脚本、图片和 frame 可加载的来源，通常被视为纵深防御的一层，而非万无一失的防护。Artifacts（现称 HTML previews）让 ChatGPT 渲染由模型编写的交互式 HTML 应用，这要求这些代码与 OpenAI 的 API 及用户私有数据保持隔离。postMessage() 是跨源 frame 通信的标准机制，只有当接收方校验来源并避免使用 innerHTML 这类危险汇聚点时才是安全的。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://stackoverflow.com/questions/33436634/bypassing-iframe-sandbox">javascript - Bypassing iframe sandbox? - Stack Overflow Usage example</a></li>
<li><a href="https://blogs.jsmon.sh/what-is-csp-content-security-policy-bypass-ways-to-exploit-examples-and-impact/">What is CSP (Content Security Policy) Bypass? Ways to Exploit ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#security</span> <span class="tag">#ChatGPT</span> <span class="tag">#web security</span> <span class="tag">#iframe sandbox</span> <span class="tag">#CSP</span></div>
</article>
<hr>

<a id="item-5"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://jepsen.io/analyses/particledb-1.1.4">Jepsen 对 ParticleDB 1.1.4 的分析发现 SQL 与事务异常</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 31, 13:39</span></div>
<p class="news-summary">Jepsen 发布了对 ParticleDB 1.1.4 的分析报告，该数据库由 Orkes 用 Rust 编写、定位为“AI-native”，报告重点检验了它在并发操作与故障注入下的行为。报告记录了一系列异常，包括一条带 WHERE NULL 谓词的 UPDATE 竟然修改了本不应匹配任何行的记录、在至多只有一个客户端访问该表的情况下仍报出“could not serialize access due to concurrent update”错误，以及被删除的行仍然可见。 ParticleDB 的定位是为 AI agent 与应用提供统一引擎，把事务型 SQL、key-value、向量搜索和分析能力整合在一起，并宣称在保持与 Postgres 相当的安全性的同时速度高出若干数量级。Jepsen 分析实际上是业界检验这类安全声明的事实基准，因此这些发现对正在筹备更广泛发布的 Orkes，以及对任何考虑将 ParticleDB 用作记录系统的团队都很重要。 除正确性缺陷外，报告还指出若干实用层面的注意事项：版本号上报不可靠，1.1.16 到 1.1.18.11.rc-18 之间的多个构建都自称是“spanner 1.1.16”；新引入的“Strong Serializable”模式基于 Serializable Snapshot Isolation（SSI），但其级别可能并不等同于早期构建所提供的 serializable-ssi。报告中的这些异常以编号 issue 形式记录，其中一组被归为 #31。</p>
<div class="news-background"><strong>背景</strong> Jepsen 是一家独立的分布式系统安全性研究机构，它用 Clojure 编写测试：通过 SSH 驱动被测系统、注入网络分区与崩溃等故障，再把记录下来的操作历史与厂商宣称的一致性模型进行比对。ParticleDB 由 Orkes 打造，该公司也是工作流编排平台 Conductor 的背后团队，Conductor 最初把数据存放在 Redis 与 Postgres 中，后来为了提升性能决定自研数据库；ParticleDB 1.0.0 只提供面向 Conductor 查询的有限功能集，之后的一次大规模重构新增了自定义线协议、更多数据类型以及额外的 OLAP 查询。该引擎把事务型 SQL、key-value 存储、向量搜索、实时分析以及名为 Particles 的用户自定义函数整合在一起，客户端可通过 Postgres 和 Redis 协议以及自有的 gRPC 与 HTTP2 API 连接。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://jepsen.io/">Jepsen - Distributed Systems Safety Research</a></li>
<li><a href="https://orkes.io/blog/particledb-database-built-for-ai-agents">ParticleDB: A Database Built for AI Agents — Orkes</a></li>
<li><a href="https://particledb.ai/">ParticleDB — the AI-native database</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Jepsen</span> <span class="tag">#distributed systems</span> <span class="tag">#database testing</span> <span class="tag">#consistency</span> <span class="tag">#correctness</span></div>
</article>
<hr>

<a id="item-6"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://github.com/ivankovic/omnidiff">OmniDiff：基于 Rust 的内容感知 Git difftool 发布 v0.3.0</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">FabCH</span><span class="news-time">Nov 1, 13:02</span></div>
<p class="news-summary">OmniDiff 是一款用 Rust 编写的新开源（AGPLv3）Git difftool，能对 25 种语言的代码、配置文件、图片、PDF、压缩包、光标文件和字体进行内容感知的差异比较。目前版本为 v0.3.0，作者称在 2023 款 ThinkPad T14s 上可在 100ms 以内完成数万行 C++ 文件的 diff。 大多数 diff 工具把所有文件当作纯文本处理，因此 PDF、图片、压缩包、字体等二进制或结构化格式很难有意义地比较；OmniDiff 为每种内容类型分配专门的 diff 处理流程。如果其稳健性经得起检验，它有望成为 delta、diff-so-fancy 等工具之外、适合处理混合文件类型开发者的日常实用替代方案。 该项目基于实证研究：作者从 Gentoo 软件包列出的 7,400 个仓库中抽取了 2,000 个 diff 并手动逐一解决，再据此构建各内容类型的 diff 流程，同一语料也构成其 CI 流水线的基础。项目仍处早期阶段（v0.3.0），采用 copyleft 的 AGPLv3 许可；作者披露使用了 AI 辅助，但表示并非 &quot;vibecode&quot;。</p>
<div class="news-background"><strong>背景</strong> Git difftool 是当你运行 `git difftool` 时 Git 把文件对交给其处理的外部程序，让你能在更丰富的查看器中查看改动，而非终端默认的按行输出。传统 diff 工具把文件当作文本逐行比较，对代码会丢失结构信息，对图片、PDF、压缩包或字体则几乎没有有用输出。内容感知 diff 则解析每种格式并比较语义元素；Rust 是一种系统编程语言，常因快速与内存安全被用于命令行工具开发。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ivankovic/omnidiff">GitHub - ivankovic/omnidiff: Fast, robust, accurate diffing</a></li>
<li><a href="https://git-scm.com/docs/git-difftool">Git - git - difftool Documentation</a></li>
<li><a href="https://daily.dev/posts/show-hn-omnidiff-opensource-super-fast-content-aware-git-difftool-in-rust-p0m0efnia">Show HN: OmniDiff – Opensource, super fast, content...</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论整体积极，多位用户称赞作者投入的努力并表示愿意试用。反复出现的诉求是希望能像 delta 那样通过管道使用（例如 `git diff | omnidiff`）而不必修改全局 Git 配置；也有人指出 delta 的 diff-so-fancy 模式会在行内高亮具体变化的字符，而在 OmniDiff 的文档中未见类似说明。另有用户欢迎 AGPLv3 许可，认为这保障了用户自由。</div>
<div class="news-tags"><span class="tag">#git</span> <span class="tag">#diff-tools</span> <span class="tag">#rust</span> <span class="tag">#developer-tools</span> <span class="tag">#open-source</span></div>
</article>
<hr>

<a id="item-7"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.nature.com/articles/s41560-026-02144-0">电网频率出现一分钟周期扰动，疑与设备定时同步有关</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">croes</span><span class="news-time">Oct 31, 10:14</span></div>
<p class="news-summary">《Nature Energy》上的一篇论文报告，电力系统频率中存在周期约为一分钟的重现性扰动，并将其归因于并网设备之间非故意的定时同步。根据对该研究的一则摘要介绍，数字控制的能源设备——尤其是基于电池的不间断电源（UPS）和电池储能系统——其与时钟同步的控制软件会在整分钟边界执行周期性自检，从而每 60 秒产生一次彼此对齐的用电需求峰值。 这一发现表明，电器与储能系统内部普通的软件定时习惯，可能在电网的核心可观测量上留下可见的、聚合性的印记，而运营商正是依靠该观测量来判断发电与用电之间的平衡。论文指出，电池储能和物联网设备的快速扩张，可能使这类同步效应在未来的电力系统中变得更加重要。 所报告的特征是具有一致相位的一分钟周期需求振荡，而非随机波动，这正是它会在 FFT 等频率分析中表现为明显周期分量的原因。所提供材料中并不包含论文的具体测量数据、地理范围、幅度估计或独立复现，因此该归因的强度与普适性在此无法得到验证。</p>
<div class="news-background"><strong>背景</strong> 电网频率是电力系统运行中的关键可观测量，因为它反映发电与负荷之间的实时平衡：当发电超过需求时频率上升，当需求超过供给时频率下降。现代并网设备由数字方式控制，依靠石英时钟或 NTP 等网络时间协议保持时间，而这些机制往往会把设备对齐到相同的分、秒边界。如果大量此类设备在同一时刻执行自检等维护例程，它们的用电需求便会叠加成一个同步脉冲，并出现在频率信号中。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41560-026-02144-0">One-minute frequency disturbances from unintended ... - Nature</a></li>
<li><a href="https://daily.dev/posts/one-minute-frequency-disturbances-from-synchronization-in-power-systems-gsumb7wft">One-minute frequency disturbances from synchronization...</a></li>
<li><a href="https://docs.ntpsec.org/latest/stats.html">Performance Metrics - NTPsec</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 的评论者对此颇感兴趣，但对归因提出了质疑：有人将其类比为机械加工中采用互质齿数来均化磨损的做法，并建议把定时器设为 59 秒多之类的偏移间隔，使其与分钟刻度自然错开相位。也有人认为，这更可能是各类微处理器上所有分钟精度 cron 式调度的聚合结果，并指出由于管理员把 ntpdate 放进 crontab，公共 NTP 服务器在整分钟处早已出现流量尖峰；还有评论者怀疑，仅凭 UPS 自检难以解释如此多厂商与型号之间的协同一致。</div>
<div class="news-tags"><span class="tag">#power-systems</span> <span class="tag">#grid-frequency</span> <span class="tag">#synchronization</span> <span class="tag">#embedded-timing</span> <span class="tag">#infrastructure</span></div>
</article>
<hr>

<a id="item-8"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://nolanlawson.com/2026/10/28/the-ai-cost-of-javascript-frameworks/">Nolan Lawson 谈 JavaScript 框架的 AI 成本</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">luu</span><span class="news-time">Nov 1, 06:06</span></div>
<p class="news-summary">Nolan Lawson 于 2026 年 10 月 28 日发表《The AI cost of JavaScript frameworks》，主张 AI 辅助开发中的框架选择应基于证据而非“感觉”；该文在 Hacker News 获得 275 分和 217 条评论。 随着 AI 编程代理进入日常前端工作，这篇文章追问：当不仅人类、连代理也必须阅读和修改代码时，成熟的 JavaScript 框架是否仍值得其复杂度。Hacker News 的讨论表明，对于正在决定是否重写前端或保留现有技术栈的团队来说，这是一个现实问题。 评论者指出，作者明确表示这篇文章旨在证明 AI 时代仍可基于证据做决策，而不是给出“氛围编码者该选哪个框架”的权威基准；但批评者认为这一限定出现得太靠后，文章仍会被当作基准来读。讨论还涉及框架的主要价值是否在于防止长期团队中的“脚枪”错误，而这一好处对代理来说可能没那么重要。</p>
<div class="news-background"><strong>背景</strong> React、Vue 和 Angular 等 JavaScript 框架为构建 Web 界面提供结构、约定和可复用抽象。AI 编程代理会读取代码库、规划改动并生成或编辑代码，通常受上下文窗口限制，并按 token 计费。由于代理必须理解框架特有的约定和抽象，框架的规模和复杂度会影响代理理解和修改应用所消耗的 token 数量；2026 年一项针对 19 个 Web 框架的独立基准测试报告称，极简框架比功能齐全的框架最多少用 2.9 倍 token。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://nolanlawson.com/2026/10/28/the-ai-cost-of-javascript-frameworks/">The AI cost of JavaScript frameworks | Read the Tea Leaves</a></li>
<li><a href="https://martinalderson.com/posts/which-web-frameworks-are-most-token-efficient-for-ai-agents/">Which web frameworks are most token-efficient for AI agents?</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 讨论中，有人认同框架确实带来真实成本，但在框架的用途上存在分歧：一位评论者认为框架主要帮助长期、多人参与的项目，通过禁止某些“脚枪”做法来发挥作用；另一位则称框架的存在是为了减少雇主的培训投入并简化招聘。还有几位评论者嘲讽仅因某个框架“对代理更友好”就重写前端的做法，一位评论者批评作者把“本文并非权威基准”的限定埋得太深。</div>
<div class="news-tags"><span class="tag">#JavaScript</span> <span class="tag">#frameworks</span> <span class="tag">#AI coding agents</span> <span class="tag">#software engineering</span> <span class="tag">#developer productivity</span></div>
</article>
<hr>

<a id="item-9"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://simonwillison.net/2026/Nov/1/kyle-kingsbury/">Kyle Kingsbury：LLM 正在侵蚀对软件、文档及其背后组织的信任</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Simon Willison</span><span class="news-time">Nov 1, 16:49</span></div>
<p class="news-summary">在 2026 年 11 月 1 日发布、由 Simon Willison 摘引的 Jepsen 对 ParticleDB 1.1.4 测试结果中，Kyle Kingsbury 提出，使用 LLM 会「侵蚀人们对文档、软件以及生产它们的组织的信任」，并警告工程师可能开始对任何新软件项目抱有怀疑，因为过去用来判断系统成熟度的信号如今更容易被伪造。他最后留下两个待解问题：在 LLM 时代，维护者能做什么来确保软件正确、文档准确，以及在完成这些工作后又如何向用户证明其质量。 凭借 Jepsen，Kingsbury 是软件正确性领域最有公信力的声音之一，因此他把人们对 AI 生成代码的模糊不安，转化为整个生态需要面对的具体问题：如果文档、测试覆盖和精美的 README 都能被廉价生成，工程师用来判断软件是否可信的那些替代性指标就会贬值。这既影响必须寻找新方式来证明质量的维护者，也影响需要判断该信任哪些新项目的用户。 这段摘录并不完整——其中带有省略号，也没有说明 ParticleDB 1.1.4 的测试报告究竟得出了什么结论——而且发布时没有可供参考的评论讨论。其核心论点在于「成熟度信号」可被伪造，而非断言 LLM 生成的代码就是错的；结尾给出的不是解决方案，而是抛给维护者的两个问题。</p>
<div class="news-background"><strong>背景</strong> Jepsen 是一个用 Clojure 编写的分布式系统安全性研究框架：测试会通过 SSH 搭建集群，用多个客户端持续施加操作，并由「nemesis」进程注入网络分区、时钟偏移等故障，然后检查记录下来的操作历史是否存在一致性违规。Jepsen 发布的报告已成为被广泛引用的数据库可靠性基准，因此被视为系统成熟度的重要信号。ParticleDB 则自称「AI 原生数据库」，在单一引擎中融合事务型 SQL、键值存储、向量搜索与分析能力。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://jepsen.io/">Jepsen - Distributed Systems Safety Research</a></li>
<li><a href="https://particledb.ai/">ParticleDB — the AI-native database</a></li>
<li><a href="https://orkes.io/blog/particledb-database-built-for-ai-agents">ParticleDB: A Database Built for AI Agents — Orkes</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#LLM trust</span> <span class="tag">#software quality</span> <span class="tag">#documentation</span> <span class="tag">#Jepsen</span> <span class="tag">#engineering culture</span></div>
</article>
<hr>

<a id="item-10"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://typesanitizer.com/blog/scion.html">工程师批评 Anthropic 的 Scion，并将其与 Meta 的 Mononoke 对比</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Nov 1, 15:22</span></div>
<p class="news-summary">一位在 Databricks 源码控制团队工作、日常面对大型 monorepo 的工程师发表博客，评析 Anthropic 自研并用来替代 git 的集中式版本控制系统 Scion，认为其设计大量沿用 Meta 的 Mononoke，而 Anthropic 的公告却把已有思路呈现得像是原创。文章还质疑了若干具体论断，例如在开发流程中不使用 ref 是否真能解决扩展性问题。 随着 AI 辅助开发把提交与合并量推到远超 git 设计预期的水平（据报道 Anthropic 的日合并量已从约 2,500 次升至 30,000 次以上），大型 monorepo 是否应当弃用 git 成为许多工程团队要认真面对的问题。这篇批评也把另一个话题摆上台面：厂商在介绍内部基础设施时，应如何标注前人的工作。 作者指出 ref 的数据量极小——只有一个名字和它指向对象的 ID——因此在开发流程中跳过 ref 并不能明显缓解预想中的扩展性问题；他认为真正的取舍在正确性层面：ref 移动会让任务悄悄拉到两个不同的 commit，而只用 commit ID 的做法则可能继续对已经不可达的 commit 运行。他还指出 Anthropic 没有公开 RPC 接口、数据库 schema、伪代码，也没有讨论被否决的备选设计；他表示可以理解代码本身不开源，但更多细节对外部读者会更有价值。</p>
<div class="news-background"><strong>背景</strong> Scion 是 Anthropic 自研的集中式版本控制系统，据报道由一个七人团队开发，并配有名为 Antique 的代码评审工具，monorepo 用五个月时间完成了从 git 的迁移。Mononoke 是 Meta 为基于 Mercurial 的巨型 monorepo 打造的服务器端版本控制系统，以 pushrebase 等应对高并发提交的技术著称；文章作者还引用了 Durham Goode 在 2017 年的演讲《Scaling Mercurial at Facebook》。monorepo 指把多个项目、服务和库放在同一个仓库中的版本控制策略，而不是拆分成多个独立仓库。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://pasqualepillitteri.it/en/news/23527/anthropic-unveils-scion-source-control-replaces-git">Anthropic unveils Scion , the source control system that replaced git</a></li>
<li><a href="https://dev.to/gabrielanhaia/claude-took-anthropic-from-2500-to-30000-merges-a-day-then-it-moved-off-git-5g7j">Claude Took Anthropic From 2,500 to 30,000... - DEV Community</a></li>
<li><a href="https://www.graphite.com/guides/monorepos">Monorepos</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#version control</span> <span class="tag">#monorepo</span> <span class="tag">#Scion</span> <span class="tag">#Mononoke</span> <span class="tag">#developer tools</span></div>
</article>
<hr>

<a id="item-11"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.fz-juelich.de/en/news/archive/press-release/2026/mystery-of-60-second-fluctuations-in-power-grids-solved">时钟同步的电池检查解释了电网 60 秒波动之谜</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 31, 19:50</span></div>
<p class="news-summary">由于利希研究中心（Forschungszentrum Jülich）Dirk Witthaut 领导，并与科隆大学和卡尔斯鲁厄理工学院研究人员合作的团队证明，欧洲电网频率每 60 秒出现一次的短暂下降，是由大型电池储能系统按固定的 1 分钟时钟周期检查其荷电状态所引起的。该研究成果于 2026 年 10 月 30 日以《One-minute frequency disturbances from unintended synchronization in cyber–physical power systems》为题发表在 Nature Energy 上。 这一现象并非欧洲独有，而是在五大洲的电网中都被观测到，并且会造成可测量的机械磨损——例如水电机组的涡轮机在每次尖峰时短暂减速再恢复转速。由于电池储能和并网数字设备正在快速扩张，该效应可能进一步放大：在爱尔兰，配备大型电池储能的数据中心约占全国用电量的五分之一，而当地 1 分钟信号的幅度在 2016 年至 2021 年间增长了四倍。 研究人员排除了单一用电器或发电机作为来源的可能，因为该效应需要大量设备同时用电才能产生；他们借助于利希的“Living Lab Energy Campus”研究基础设施，在共计 80 个地点的终端设备上安装测量点，并在这些位置观测到相同的周期性模式，从而确认了二者的关联。这些频率偏差对电网安全并不构成关键威胁，团队也指出不能排除空调系统、热泵、洗衣机和洗碗机等其他数字控制设备存在类似模式；他们提出的解决办法很简单：把检查时间随机分散，而不是让所有设备在同一时刻启动检查。</p>
<div class="news-background"><strong>背景</strong> 电网必须时刻保持发电与用电的平衡，而电网频率正是这种平衡的物理指标——频率短暂下降意味着用电 momentarily 超过供电。随着电力系统演变为信息与通信技术和电力基础设施紧密结合的“信息物理系统”（cyber-physical system），并网设备中的软件程序也能对电网产生物理层面的影响。大型电池储能系统和 uninterruptible power supply（UPS）用于保障供电不中断，通常会按固定的时钟周期核验自身的荷电状态；当大量此类设备共享同一时钟节拍时，它们的检查便叠加成每分钟一次的同步脉冲。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41560-026-02144-0">One-minute frequency disturbances from unintended ... - Nature</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cyber-physical_system">Cyber-physical system - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0045790624000776">Cyber-physical power systems: A comprehensive review about ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#power grids</span> <span class="tag">#cyber-physical systems</span> <span class="tag">#synchronization</span> <span class="tag">#energy systems</span> <span class="tag">#Nature Energy</span></div>
</article>
<hr>

<a id="item-12"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://matklad.github.io/2026/10/29/pub-calls-pub.html">设计建议：避免公有函数调用其他公有函数</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 31, 18:05</span></div>
<p class="news-summary">在一篇短文中，matklad 提出了一条模块设计上的经验法则：当公有函数 foo 需要复用另一个公有函数 bar 已经实现的部分行为时，不应在 foo 内部调用 bar()，而应抽出一个新的私有 helper，让 foo 和 bar 都调用它。文中还明确列出一个例外——“shortcut”式 API：它本身就是把常用的公有调用链封装起来，因此不允许使用私有调用，以确保它是真正的捷径，而不是多出来的中间层。 这条建议针对的是一种隐蔽的 API 腐化：当公有函数被拿来构建其他公有函数时，面向调用方的便利与面向内部实现的便利会相互冲突，于是那些用户根本不该设置的可选参数就会逐渐混入接口。由于这种退化往往在原初的代码复用之后很久才显现，及早规避可以帮助维护者免于日后尴尬且破坏性的接口变更。 作者认为，主动把共享实现设为私有就能化解这种张力，因为修改私有 helper 的签名只是廉价的局部改动。他还反驳了两个 Stack Overflow 答案：一个认为这种写法会让针对单个方法的隔离测试更难做 mock（他回应说应该 mock IO 而不是自己的方法，应该测试软件功能而非方法）；另一个认为若无行业或组织层面的标准背书，这条建议就没有意义（他回应说遵循规则应出于其背后的理由，而不是因为规则被写进了“圣典”。）</p>
<div class="news-background"><strong>背景</strong> 这篇文章是一篇小规模的设计随笔，出发点是 DRY（Don&#x27;t Repeat Yourself，不要重复自己）原则——它促使程序员复用已有代码而不是复制一份。在模块设计中，公有 API 是暴露给外部调用者的界面，私有函数则是内部实现细节；文章的核心论点是混淆这两种角色会损害公有接口。文中还涉及 mocking，这是一种常见的测试手法，用伪造对象替换依赖，以便对某个单元做隔离测试。</div>
<div class="news-tags"><span class="tag">#software design</span> <span class="tag">#API design</span> <span class="tag">#code quality</span> <span class="tag">#programming practices</span></div>
</article>
<hr>

<a id="item-13"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://bathtub-01.github.io/technical/ouros-demo/">Ouros：无需软件运行时的 FPGA Haskell 处理器</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Nov 1, 16:13</span></div>
<p class="news-summary">一位博士生展示了 Ouros——一个基于 combinator 的图归约（graph reduction）处理器，可直接在 FPGA 上执行 Haskell 程序，IO 完全由硬件处理，通过映射到 UART 端口的寄存器完成读写。在 AMD 捐赠的 AUP-ZU3 开发板上，该设计运行频率为 100 MHz，占用约 27% 的 LUT、7% 的寄存器和 40% 的 BRAM，底层没有任何软件运行时或 kernel trap。 这项工作复活了 1980 年代为惰性（non-strict）函数式语言设计专用硬件的想法——该思路在 1990 年代因软件实现改进和通用 CPU 提速而被基本放弃，而作者在专用架构（domain-specific architecture）重新受到关注的今天再次论证其可行性。作者指出，图归约、自动多线程和垃圾回收都能容纳在与小型流水线 RISC-V 核大致相当的逻辑资源内，这被视为惰性语言直接硬件支持可行性的积极信号。 作者坦率说明了局限：可用原语（primitives）有限，目前也只接入了 UART，由 Haskell 程序轮询其寄存器；同样的接口未来可连接到 GPIO、定时器或硬件随机数发生器。BRAM 占用主要由堆和代码存储器决定，可通过调整其大小来伸缩；与 RISC-V 核的比较明确不是同等条件下的对比；演示既可通过 Vivado 仓库在 AUP-ZU3 开发板上复现，也可在模拟器中用 cargo 命令运行。</p>
<div class="news-background"><strong>背景</strong> Haskell 是一种惰性（non-strict）函数式语言，经典的求值方式是图归约：表达式被表示为图并逐步重写；Ouros 用 combinator 实现这一过程，这种风格也被 Lennart Augustsson 的小型 Haskell 编译器 MicroHs 采用，作者称其“先给演示”的做法正是效仿 MicroHs。FPGA 是可重构芯片，其逻辑由查找表（LUT）、寄存器和块 RAM（BRAM）构成，因此这些资源的占用百分比反映了设计消耗了芯片的多少部分。文中提到的“imperative functional programming”指向 1993 年 Peyton Jones 与 Wadler 的论文，它奠定了 Haskell 这类惰性语言中 IO 的组织方式。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/augustss/MicroHs">GitHub - augustss/ MicroHs : Haskell implemented with combinators</a></li>
<li><a href="https://run-x.com/blog/fpga-hardware-resources-luts-bram-dsp-clocking-and-routing/">FPGA Hardware Resources : LUTs , BRAM , DSP, Clocking, and Routing</a></li>
<li><a href="https://www.hackster.io/548187/custom-led-blink-ip-on-aup-zu3-zynq-ultrascale-bad4cf">Custom LED Blink IP on AUP - ZU 3 Zynq UltraScale+ - Hackster.io</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Haskell</span> <span class="tag">#FPGA</span> <span class="tag">#hardware-design</span> <span class="tag">#functional-programming</span> <span class="tag">#processors</span></div>
</article>
<hr>

<a id="item-14"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.nablag.com/spooky_cpp">Spooky C++：悬空 string_view 在 -O2 下把 false 变成 true</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Nov 1, 18:17</span></div>
<p class="news-summary">一篇应景万圣节的博客文章《Spooky C++》展示了一个小程序：用 clang++-19 加上 -Wall -Wextra -Wpedantic 编译时，-O0 下输出 &quot;Grant foobarbazboo root permissions = false&quot;，而 -O2 下却输出 &quot;true&quot;。作者称在 GCC 14.2.0 以及 -std=c++17、-std=c++20、-std=c++23 下都能复现同样的翻转，并将其归因于未定义行为（undefined behavior），而非机器闹鬼。 这个例子简短且可复现，直观展示了生命周期缺陷在开启优化后会如何悄然改变程序逻辑，即便常用的警告选项已经打开。对于使用 std::string_view 编写权限校验或其他安全敏感比较逻辑的 C++ 开发者来说，这是一个很有价值的教学案例。 作者指出该现象非常脆弱：它之所以出现，是因为字面量 &quot;foobarbazboo&quot; 恰好与 admin_id 长度相同且以内联方式传入；一旦改变输入长度，或先把字符串存入临时变量，该行为就会消失，把 admin_id 重构为单例或全局变量同样能让程序恢复正常。他还表示怀疑这类缺陷会在真实项目中浮现或被轻易利用；附录列出的测试环境为 WSL2（内核 6.18.54.1-microsoft-standard-WSL2）下的 Debian clang 19.1.7 与 GCC 14.2.0。</p>
<div class="news-background"><strong>背景</strong> C++17 引入的 std::string_view 是对字符序列的轻量非拥有视图：它只保存指针和长度，并不负责维持底层字符的生存期。在这段代码中，Sanitize 接受 const std::string&amp; 并返回指向它的 string_view，但实参是由字符串字面量构造的临时 std::string，因此当该临时对象在完整表达式结束时被销毁，这个视图就可能悬空。由于 C++ 标准将这类的行为定义为未定义行为，编译器可以假定它永远不会发生并据此优化，这正是 -O0 与 -O2 下比较结果可能不同的原因。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://salivity.github.io/cpp/article/std-string-view-lifetime-hazards-in-c">std::string_view Lifetime Hazards in C++ - cpp</a></li>
<li><a href="https://stackoverflow.com/questions/69149369/is-it-safe-to-pass-an-stdstring-temporary-into-an-stdstring-view-paramet">Is it safe to pass an `std::string` temporary into an `std ...</a></li>
<li><a href="https://dev.to/adityabhuyan/unraveling-undefined-behavior-performance-optimizations-in-modern-compilers-2ig4">Unraveling Undefined Behavior: Performance Optimizations in ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#C++</span> <span class="tag">#undefined behavior</span> <span class="tag">#compilers</span> <span class="tag">#security</span> <span class="tag">#systems programming</span></div>
</article>
<hr>

<a id="item-15"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://lemire.me/blog/2026/10/31/beating-the-compiler-at-signed-32-bit-division/">在带符号 32 位整数除法上跑赢编译器</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Nov 1, 12:26</span></div>
<p class="news-summary">在 2026 年 10 月 31 日的博客文章中，Daniel Lemire 展示了在 64 位处理器上做带符号 32 位常量除法时，手写代码序列可以胜过 GCC 14、clang 21 和 Apple clang 17 生成的代码。其技巧在于利用 64 位乘法中“空闲”的那一位，使得当理想乘数需要 33 位时，乘倒数的方法不必再执行编译器额外生成的加回（add-back）与符号修正指令。他报告在 Intel Xeon Gold 6548N（Emerald Rapids）上，对 7、60、365 等除数，延迟降低约 2 个周期；在 Apple M4 Max 上延迟降低约 12%。 整数除法是最慢的标量运算之一，而“除以常量”的模式在库代码和系统代码中极其普遍，因此从关键路径上去掉两条指令虽属局部优化，却是实打实的收益。这一发现同时指向主流编译器中一个可复现的漏优化（missed optimization），意味着未来这一收益有可能被编译器自动获得，而不只属于手工调优的代码。 基准测试对 16,384 个随机带符号整数做除法：吞吐量测试中各次除法相互独立，延迟测试中每次除法依赖前一次（并计入两个周期的循环开销），且关闭了自动向量化。在 Intel 处理器上使用 clang 时吞吐量提升超过 20%，而 GCC 的吞吐量在该基准中并无变化；除数 1000 作为对照组，因为其乘数 274877907 可以放进带符号 32 位寄存器、无需修正，所以两个版本都耗时 8 个周期。Lemire 还指出，在以运行时除数做除法的库中，这一方法还能省去一个分支。</p>
<div class="news-background"><strong>背景</strong> 处理器用专门的指令实现整数除法——x86 上的 idiv 和 ARM 上的 sdiv——它们比乘法慢得多、流水化程度也低，在较新的 AMD 核心上延迟还取决于操作数取值。自 Granlund 和 Montgomery 1994 年的 PLDI 论文以来，编译器会把“除以编译期常量”替换为“乘以预先算好的倒数再移位”，从而完全避开除法器。Lemire 文中 x86 指令的延迟与吞吐量数据取自 uops.info 微架构数据库，他也提到这次研究的起因是 Ben Joffe 近期关于常量快速向下取整除法的文章。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://uops.info/">uops.info</a></li>
<li><a href="https://arxiv.org/pdf/1810.04610v2">uops.info: Characterizing Latency, Throughput, and Port Usage ...</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 讨论非常有限：唯一一条评论建议将此问题作为“漏优化”提交到 GCC 缺陷跟踪系统，把这一发现定位为一个可行动的编译器缺陷，而不只是一则趣闻。</div>
<div class="news-tags"><span class="tag">#compilers</span> <span class="tag">#integer-division</span> <span class="tag">#performance-optimization</span> <span class="tag">#x86</span> <span class="tag">#ARM</span></div>
</article>
<hr>

<a id="item-16"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://web.eece.maine.edu/~vweaver/projects/deterministic/deterministic_counters.pdf">研究发现 x86_64 PMU 计数器存在非确定性与重复计数</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Nov 1, 07:55</span></div>
<p class="news-summary">一篇由 Vincent Weaver 撰写的论文研究了现代硬件性能计数器中的非确定性与重复计数问题，在严格控制的环境下测试了 11 种不同的 x86_64 CPU 实现。研究发现，本应精确的事件（如 retired instructions）会出现逐次运行的波动和重复计数，只有少数事件——尤其是条件分支和 retired stores——具备足够的确定性，可以在确定性执行环境中不加调整地使用。 确定性重放系统、确定性线程库和性能分析工具通常假设计数器数值是可复现的，因此隐藏的逐次运行波动会动摇这些假设，并可能使基于 CPI 的度量变得不可靠。由于作者认为许多规避方法在不重新设计底层 PMU 的情况下无法实现，这一问题属于架构层面的限制，而非简单的软件缺陷。 论文将 x86_64 上的部分偏差归因于 iret（中断返回）指令：尽管它运行在内核空间，却似乎被计为用户态指令，从而使任何会计入该指令的事件失去确定性。作者还简要考察了 ARM、IA64、POWER 和 SPARC 系统，并指出这些平台上的计数器事件比 x86_64 具有更好的确定性。</p>
<div class="news-background"><strong>背景</strong> PMU（性能监控单元）是内建于 CPU 中、用于统计硬件事件的模块，这些计数器为 retired instructions（完整执行的指令数）等指标提供数据，并进而支撑常见的 cycles per instruction（CPI）等度量。IRET 是 x86 中从中断处理程序返回到被中断程序的指令。确定性重放和确定性线程依赖在不同运行之间精确复现相同的指令流与事件计数，这正是计数器精度在性能分析之外也具有重要意义的���因。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://web.eece.maine.edu/~vweaver/projects/perf_counters/retired_instructions.html">Retired Instructions Performance Counter</a></li>
<li><a href="https://www.intel.com/content/www/us/en/docs/vtune-profiler/user-guide/2025-4/instructions-retired-event.html">Instructions Retired Event - Intel</a></li>
<li><a href="https://hjlebbink.github.io/x86doc/html/IRET_IRETD.html">IRET /IRETD— Interrupt Return</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#hardware performance counters</span> <span class="tag">#PMU</span> <span class="tag">#determinism</span> <span class="tag">#systems research</span> <span class="tag">#performance profiling</span></div>
</article>
<hr>

<a id="item-17"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://karthinks.com/software/understanding-org-latex-preview/">Org mode 的 LaTeX 预览被重写为异步缓存系统</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Nov 1, 22:19</span></div>
<p class="news-summary">karthinks.com 上的一篇新文章介绍了作者与 Tecosaur 从零重写 Org mode 的 LaTeX 数学预览功能，实现了一个异步、带缓存的近似所见即所得（near-WYSIWYG）预览系统，并已进入 Org mode 的开发分支。文章定位为设计与原理综述，讲解该库的目标，以及实现所依赖的 Emacs 事件循环和子进程处理机制。 对于在 Org mode 中写大量数学笔记的用户来说，异步渲染并缓存结果的预览意味着更少的等待，且 LaTeX 编译时编辑器不会卡死。这篇文章同时也可以当作 Emacs 异步子进程 API 与事件循环的导览，对任何在 Emacs 上构建耗时或增量式功能的包作者都很有价值。 org-latex-preview 中几乎所有复合数据结构都是 alist 或 plist，其中一个名为 &quot;extended-info&quot; 的可变 plist 承载了流程链所需的全部数据：编译器偏好、输入的 LaTeX 字符串、文件与图片路径及缓存信息、用于异步回调的当前 buffer 上下文、overlay 的位置与属性、编译错误，以及计算出的预览几何尺寸和字号。作者指出 orgmode.org 上的用户手册尚未更新，并推荐读者参阅 Tecosaur 的 &quot;This Month in Org&quot; 文章；他还推测未来架构可以完全绕开进程间通信，改用 Emacs 动态模块链接一个增量式编译器（例如基于 LuaLaTeX 的 rtex），并认为 KaTeX 或 MathJax 不够用，因为需要支持宏的完整 LaTeX 编译器。</p>
<div class="news-background"><strong>背景</strong> Org mode 是 Emacs 内置的主模式，用于大纲、笔记、任务管理和可复现文档，并允许在正文中内嵌 LaTeX 片段，从而在 buffer 内以图片形式预览数学表达式。过去这种预览依赖批量编译片段为图片，因此外部 LaTeX 进程运行时编辑器可能会卡顿。新实现保留了 Emacs 文本优先、可扩展的特性，同时让编译变为异步并缓存生成的图片；文章还提到未来可能为 Org 推出官方 Typst 预览包。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://orgmode.org/worg/org-tutorials/org-latex-preview.html">orgmode . org /worg/ org -tutorials/ org - latex - preview .html</a></li>
<li><a href="https://github.com/yangsheng6810/org-latex-impatient">GitHub - yangsheng6810/ org - latex -impatient: Instant Previews LaTeX ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Emacs</span> <span class="tag">#Org mode</span> <span class="tag">#LaTeX</span> <span class="tag">#editor tooling</span> <span class="tag">#technical deep-dive</span></div>
</article>
<hr>