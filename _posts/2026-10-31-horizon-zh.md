---
layout: default
title: "Horizon 每日速递：2026-10-31"
date: 2026-10-31
lang: zh
---

> 📅 2026-10-31 · 从 55 条资讯中精选出 21 条重要内容

---

1. [Jepsen 发现 ParticleDB 存在 96 个正确性问题，建议用户迁移](#item-1) <span class="score-badge score-high">9.0</span>
2. [Linux IPv4/TCP 释放后使用漏洞 CVE\-2026\-98432，CVSS 评分 9\.8](#item-2) <span class="score-badge score-mid">8.0</span>
3. [Parameter\.ai 披露：一条精心构造的链接即可接管 ChatGPT 账号](#item-3) <span class="score-badge score-mid">8.0</span>
4. [Anthropic 的 Claude VS Code 扩展在 Cursor 上被植入后门近 12 小时](#item-4) <span class="score-badge score-mid">8.0</span>
5. [HackerTube 把 Hacker News 评论里的视频链接做成 YouTube 式站点](#item-5) <span class="score-badge score-mid">7.0</span>
6. [Signal 分支 Molly 据报三个月未更新且存在安全风险](#item-6) <span class="score-badge score-mid">7.0</span>
7. [深入解析 GCC 如何降级（lower）switch 语句](#item-7) <span class="score-badge score-mid">7.0</span>
8. [Vitalik Buterin 倡导数字极简主义：少用应用，多用本地与离线工具](#item-8) <span class="score-badge score-mid">7.0</span>
9. [NES 6502 模拟器被写入 Qwen3\.5\-4B 模型权重](#item-9) <span class="score-badge score-mid">7.0</span>
10. [OpenAI、Google、Microsoft 与 Anthropic 支持 robots\.txt 共享退出令牌](#item-10) <span class="score-badge score-mid">7.0</span>
11. [Google Project Suncatcher 卫星在轨运行 Gemma 模型](#item-11) <span class="score-badge score-mid">7.0</span>
12. [教皇利奥十四世呼吁&quot;解除 AI 武装&quot;并禁止致命自主武器](#item-12) <span class="score-badge score-mid">7.0</span>
13. [Nathan Lambert 重新审视开放模型网络风险论点](#item-13) <span class="score-badge score-mid">7.0</span>
14. [大型电池储能的每分钟自检被指为电网 60 秒波动的成因](#item-14) <span class="score-badge score-mid">7.0</span>
15. [博主发现 Bluesky 的 AT Protocol 数据普遍公开，包括私人订阅源](#item-15) <span class="score-badge score-mid">7.0</span>
16. [Tangled 推出基于 AT Protocol 的联邦化代码托管平台](#item-16) <span class="score-badge score-mid">7.0</span>
17. [一起造个大脑：互动式神经回路讲解](#item-17) <span class="score-badge score-mid">7.0</span>
18. [Futhark 通过置换迭代空间加速 GPU 拷贝](#item-18) <span class="score-badge score-mid">7.0</span>
19. [Infinite Mac 将 BeOS 带入浏览器](#item-19) <span class="score-badge score-mid">7.0</span>
20. [curl 意外图灵完备长达九个月](#item-20) <span class="score-badge score-mid">7.0</span>
21. [C 语言有效类型规则与编译器一致性](#item-21) <span class="score-badge score-mid">7.0</span>

---

<a id="item-1"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://jepsen.io/analyses/particledb-1.1.4">Jepsen 发现 ParticleDB 存在 96 个正确性问题，建议用户迁移</a><span class="score-badge score-high">9.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 31, 13:39</span></div>
<p class="news-summary">Jepsen 发布了对 ParticleDB 1.1.4 至 1.1.18.11.rc-22 版本的分析报告，共记录了 96 个问题，涵盖崩溃、死锁、已提交写入丢失、G1a（Aborted Read）与 G1b（Intermediate Read）、P4（Lost Update）以及删除后仍可见的行等异常。报告结论是 ParticleDB 所宣称的 “Full ACID” 并不成立，并明确建议用户立即停止部署、尽快迁移到其他数据库，如条件允许还应从更可靠的来源校验或重建数据状态。 在 Jepsen 的正式分析中被判定为系统性（而非偶发）的正确性失效，是一款数据库能收到的最强烈负面信号之一；此事尤其重要，因为 ParticleDB 曾以兼容 Postgres、具备 ACID 乃至拥有 TLA+ “形式化证明” 作为卖点。将其作为 Postgres 或 Redis 的平替而采用（尤其是运行 Orkes Conductor 工作流平台的团队）的用户，面临的可能不是显式报错，而是静默的数据丢失。 这些异常在所有事务模式和 WAL 同步模式下都会出现，示例包括：`UPDATE ... WHERE NULL` 竟然能修改行、单条语句报出“并发更新”错误而实际上只有一个客户端访问该表、以及被删除的行仍然可见；报告还指出 `particledb --version` 不可靠，1.1.16 到 1.1.18.11.rc-18 的构建都自称 “spanner 1.1.16”。值得注意的是，Jepsen 表示在整个合作过程中并未拿到任何 TLA+ 规约，因此那个宣称的“形式化证明”究竟证明了哪些性质并不清楚。</p>
<div class="news-background"><strong>背景</strong> Jepsen 是由 Kyle Kingsbury（Aphyr）主持的独立分布式系统安全研究项目，维护一套开源测试框架，并免费发布深度分析报告，曾揭露出众多广泛使用的数据库中的严重一致性缺陷。其测试方法通常是对真实集群施加随机的并发事务，再用形式化的异常类别（如 G1a 已中止读、G1b 中间读、P4 丢失更新）检验记录下来的历史是否符合数据库所宣称的隔离级别。ParticleDB 由 Orkes 用 Rust 开发，用于支撑其 Conductor 工作流编排平台，是一个多模型引擎，集事务性 SQL、键值存储、向量搜索、实时分析与名为 Particles 的自定义函数于一体，并提供兼容 Postgres 与 Redis 协议的接入层。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://jepsen.io/analyses/particledb-1.1.4">Jepsen: ParticleDB 1.1.4</a></li>
<li><a href="https://github.com/jepsen-io/jepsen">GitHub - jepsen -io/ jepsen : A framework for distributed systems ...</a></li>
<li><a href="https://particledb.ai/">ParticleDB | The database for AI agents</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 上的评论几乎一边倒地批评：有人称这份报告“太狠了”，并调侃这就是“vibecode 一个数据库”的下场；也有人重点提及报告中那句话——一个自称“形式化证明”的产品，合作期间却拿不出任何 TLA+ 规约。讨论中另一个较有共鸣的观点是软件的两分法：一类是“构造上正确”的软件，另一类则是“构造上就不正确”、只靠运气以及在各处代码路径上打补丁绕过缺陷才勉强运行的软件，而 AI 恰恰很擅长找出该在哪里插入这些绕行补丁。</div>
<div class="news-tags"><span class="tag">#databases</span> <span class="tag">#jepsen</span> <span class="tag">#distributed-systems</span> <span class="tag">#transactional-consistency</span> <span class="tag">#reliability</span></div>
</article>
<hr>

<a id="item-2"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://atlasum.net/blog/cve-2026-98432-linux-ipv4-tcp-uaf">Linux IPv4/TCP 释放后使用漏洞 CVE-2026-98432，CVSS 评分 9.8</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">oger</span><span class="news-time">Oct 31, 19:16</span></div>
<p class="news-summary">Linux 内核 IPv4/TCP 处理路径中存在一个释放后使用（use-after-free）漏洞，编号为 CVE-2026-98432，CVSS 评分高达 9.8，并在 Hacker News 上引发讨论。评论者指出，在讨论发生时 Ubuntu、RHEL 等主要发行版似乎尚未提供修复，不过这属于社区观察，并非经过核实的官方公告。 内核核心网络代码中的内存破坏漏洞影响面很广，因为 Linux 支撑着大多数面向互联网的服务器和云基础设施，任何可通过数据包处理触达的缺陷都值得尽快修复关注。披露与发行版修复之间似乎存在的空档，对那些依赖厂商软件包而非上游内核的管理员而言同样重要。 根据社区整理的信息，触发该漏洞并不需要 MPTCP，互联网范围的利用可能性较低，因为许多 ISP 路由器会丢弃带有 IP options 字段的数据包；此外成功利用需要多核 CPU 并行处理数据包，因此单核系统或将数据包处理绑定到单核的系统不受影响。丢弃带 IP options 的数据包据称有帮助，但依照讨论中引述的 Red Hat 说法，这并非完整的缓解措施。</p>
<div class="news-background"><strong>背景</strong> 释放后使用漏洞是指程序在内存区域被释放之后仍继续使用它，这可能导致崩溃，某些情况下还可能让攻击者执行自己的代码。CVSS 是一套以 0 到 10 分评估漏洞严重性的框架，9.8 分意味着仅基于漏洞内在特征即被判定为最坏影响情形下的严重问题。Linux 发行版通常不会直接提供最新的上游内核，而是把单个安全修复回移（backport）到自己的内核包中，因此上游已有修复、而厂商软件包在一段时间内仍然存在漏洞的情况并不罕见。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.malwarebytes.com/blog/bugs/2026/09/two-critical-chrome-flaws-put-users-at-risk-on-malicious-websites">Two critical Chrome flaws put users at risk on malicious... | Malwarebytes</a></li>
<li><a href="https://en.wikipedia.org/wiki/Common_Vulnerability_Scoring_System">Common Vulnerability Scoring System - Wikipedia</a></li>
<li><a href="https://www.systemshardening.com/articles/linux/linux-ai-accelerated-exploit-development/">Kernel Hardening for AI-Accelerated Exploit Development</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者更多是在补充技术细节而非单纯渲染恐慌：有人澄清该漏洞不需要 MPTCP，且多核数据包处理是成功利用的前提；也有人批评 Hacker News 在标题中去掉了“Linux”，因为 BSD、macOS 和 Windows 用户并不受影响。对发行版的态度偏向批评，有评论者质问 Ubuntu 和 RHEL 为何尚未发布修复；还有人质疑所链接文章的质量，认为它看起来像 AI 生成，并建议直接查看 NVD 条目。另有评论者询问可用于跟踪与其服务相关 CVE 的 RSS 源。</div>
<div class="news-tags"><span class="tag">#security</span> <span class="tag">#linux</span> <span class="tag">#vulnerability</span> <span class="tag">#cve</span> <span class="tag">#kernel</span></div>
</article>
<hr>

<a id="item-3"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.parameter.ai/labs/we-found-a-gap-at-openai">Parameter.ai 披露：一条精心构造的链接即可接管 ChatGPT 账号</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">armcat</span><span class="news-time">Oct 31, 10:30</span></div>
<p class="news-summary">Parameter.ai 的安全研究人员发布了一份详细报告，描述他们如何通过串联对渲染预览内容的操纵，逐层突破多重防御，绕过 ChatGPT 的沙箱与内容安全策略（CSP），并仅凭让用户点击一条链接就接管其账号。OpenAI 确认两个前端均已拒绝报告中所述的消息，问题已修复，并支付了总计 5,000 美元的赏金。 ChatGPT 拥有规模庞大的个人与组织用户，因此一条账号接管攻击链——即便需要用户点击——也会让对话记录、已连接的应用集成和账号数据面临风险。赏金金额同样成为讨论焦点，研究者和评论者认为，过低的奖励会打击未来披露严重漏洞的积极性。 该攻击仍依赖受害者点击链接，研究者描述的是把预览内容操纵与沙箱、CSP 绕过组合起来，而非单一漏洞。评论者指出这份报告在部分段落不易理解，尤其是关于 JSONP 的一节，看起来更像是在解释某项防御机制的工作原理，而不是说明如何攻破它。</p>
<div class="news-background"><strong>背景</strong> 账号接管（account takeover，ATO）指攻击者未经授权取得他人账号的控制权，例如通过恶意前端代码窃取会话凭证。ChatGPT 会在浏览器中展示模型输出和链接预览，因此依赖沙箱化 iframe 与内容安全策略（CSP）等层层防护，阻止被注入的内容执行脚本或加载不受信任的资源。JSONP 是一种较早期的通过 script 标签跨域取数据的技术，因此经常出现在讨论 CSP 拦截范围的语境中。OpenAI 等大型厂商设有漏洞赏金计划，对私下报告漏洞的研究者给予奖励。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.parameter.ai/labs/we-found-a-gap-at-openai">Do the Math: How We Took Over ChatGPT Accounts - Parameter</a></li>
<li><a href="https://cybersecuritynews.com/chatgpt-account-take-over-vulnerability/">ChatGPT Account Take Over Bug Let Hackers Gain Online Account</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 上的讨论以批评为主：多位评论者称 5,000 美元的赏金是个笑话，认为低额奖励会导致研究者今后对严重漏洞保持沉默。也有人表示文章的行文风格让人难以弄清究竟发生了什么，还有评论者把这次披露与另一起报道的问题联系起来——ChatGPT 桌面应用中曾开启过“Work”对话的用户，其文件系统可能被远程访问。</div>
<div class="news-tags"><span class="tag">#security</span> <span class="tag">#vulnerability-disclosure</span> <span class="tag">#OpenAI</span> <span class="tag">#bug-bounty</span> <span class="tag">#web-security</span></div>
</article>
<hr>

<a id="item-4"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://arstechnica.com/security/2026/10/anthropic-vs-code-extension-on-cursor-backdoored-for-nearly-12-hours/">Anthropic 的 Claude VS Code 扩展在 Cursor 上被植入后门近 12 小时</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Ars Technica AI</span><span class="news-time">Oct 30, 21:09</span></div>
<p class="news-summary">据独立研究员 Kevin Beaumont 称，Anthropic 官方 Claude VS Code 扩展的恶意版本 2.1.313 被发布到 Anthropic 在 Cursor 市场上的认证账号，并在近 12 小时内可用，随后 Anthropic 推送了版本 2.1.314。Cursor 表示受影响的用户最多为 5,000 名，而 Cursor 和 Anthropic 均未解释攻击者是如何控制该账号的。 这是一次滥用可信认证分发渠道、而非仿冒包的供应链攻击，意味着仅仅依赖默认自动更新的开发者也可能受到影响。由于编辑器扩展继承 IDE 的权限，该事件可能使 Windows、macOS 和 Linux 机器上的本地文件、源代码、开发工具以及云凭证面临风险。 据 Cursor 称，该恶意扩展试图通过添加攻击者控制的 SSH 密钥来安装持久化 SSH 后门，启用本地 SSH 服务并开启反向 SSH 隧道，其代码针对 Windows、macOS 和 Linux 编写。Cursor 中的扩展默认自动更新，但用户可以在设置中更改；据报道，截至报道时 Anthropic 尚未向客户发布公开通知。</p>
<div class="news-background"><strong>背景</strong> Cursor 是一款围绕 AI 辅助开发构建的 AI 代码编辑器，并像 VS Code 一样拥有自己的扩展市场。扩展在编辑器内以与 IDE 相同的权限运行，因此被入侵的扩展可以读取本地文件和源代码，而不受沙箱限制。开发者工具领域的供应链攻击已成为反复出现的主题，近期业界开始致力于扫描市场中的扩展以发现恶意行为。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/security/2026/10/anthropic-vs-code-extension-on-cursor-backdoored-for-nearly-12-hours/">Anthropic VS code extension on Cursor backdoored... - Ars Technica</a></li>
<li><a href="https://socket.dev/blog/vscode-extensions">Introducing Socket Scanning for VS Code Marketplace Extensions</a></li>
<li><a href="https://cursor.com/">AI Coding Agent for Building Ambitious Software | Cursor</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#supply-chain-security</span> <span class="tag">#security-incident</span> <span class="tag">#vs-code-extensions</span> <span class="tag">#anthropic</span> <span class="tag">#developer-tools</span></div>
</article>
<hr>

<a id="item-5"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://karpathy.bearblog.dev/hacker-tube/">HackerTube 把 Hacker News 评论里的视频链接做成 YouTube 式站点</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">karpathy</span><span class="news-time">Oct 31, 19:56</span></div>
<p class="news-summary">发布在 Andrej Karpathy 博客上的项目 HackerTube 上线于 hackertube.org，它用一个类似 YouTube 的界面呈现 6,454 个视频，这些视频是从可追溯到 2007 年的约 39,834 条 Hacker News 评论中提取出来的。它没有使用推荐模型，内容目录就是 HN 社区近二十年来主动分享的链接。 这个项目虽小，却是一个颇有针对性的策展实验：它说明一个可用的视频信息流可以完全由人工推荐拼装出来，而不必依赖以参与度为优化目标的排序，这正是评论者拿来与主流 YouTube 对比的地方。它也说明论坛几十年积累的存档里潜藏着多少通常只被读一次便被遗忘的价值。 该站点本质上是在一份存档之上加了一层浏览界面，而不是推荐系统，评论者指出了诸如缺少“从新到旧”排序这样的实用缺口。也有人提出更难的问题：能否以某种优于 YouTube 评论系统的方式给视频加上评论或注释层，包括能够引用不同视频中的具体片段。</p>
<div class="news-background"><strong>背景</strong> Hacker News 是一个长期运行的科技链接聚合论坛，用户提交链接并在嵌套评论中讨论，而这些讨论里分享的视频正是该项目的数据来源。主流视频平台依赖推荐算法，按点击、观看时长等预测互动指标对内容排序，批评者认为这有利于标题党和令人上瘾的观看模式。HackerTube 正处于这两种模式的交叉点：一份由人工策展链接构成的朴素存档，套上了人们熟悉的视频浏览界面。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Algorithm">Algorithm - Wikipedia</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 主流情绪是如释重负：评论者说浏览 HackerTube 相比 YouTube 令人耳目一新，因为在后者上他们时刻提防被诱导，有人称这里是“100% 纯极客内容”，没有网红视频和标题党。也有不少人反思策展疲劳，指出按自己声称的兴趣定制的信息流反而无法满足自己，因为他们上网本是为拓展视野、遇到令人意外的观点。另一些人聚焦具体改进，希望增加“从新到旧”排序，并设想能引用视频片段的更好的评论与注释系统。</div>
<div class="news-tags"><span class="tag">#curation</span> <span class="tag">#recommendation-systems</span> <span class="tag">#Hacker News</span> <span class="tag">#web tools</span> <span class="tag">#algorithmic feeds</span></div>
</article>
<hr>

<a id="item-6"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://piefed.world/post/1503394">Signal 分支 Molly 据报三个月未更新且存在安全风险</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">DeepLogin</span><span class="news-time">Oct 31, 10:23</span></div>
<p class="news-summary">有社区帖子指出，Android 上经过加固的 Signal 分支 Molly 已有约三个月未更新，并被描述为存在安全风险，由此引发了关于替代方案的讨论。在同一讨论中，自称维护极简版 Molly 分支 Polly 的开发者发布了一个过渡版本（v8.19.2-6），包含若干已知问题的修复。 那些选择 Molly 正是为了获得完全自由、可审计且不含 Google 专有组件的 Signal 构建的用户，现在可能正在使用未获得上游安全补丁的代码。这一事件也凸显了小型分支的维护风险：它们往往依赖一位或少数几位志愿者来跟进上游 Signal 的发布节奏。 Polly 的过渡版本仍基于 Signal 8.19.2，并集成了 RingRTC 2.73.0-1；据维护者称，该版本包含针对挂断/热麦（hot-mic）问题的通话拆除（call-teardown）修复，同时还纳入了 Signal 对八个遭攻破的 eMudhra TLS 中间证书的黑名单。该构建仅支持 arm64 且要求 Android 14 及以上，因此在作为无缝替代品时适用人群有限。</p>
<div class="news-background"><strong>背景</strong> Molly 是 Android 上独立的 Signal 分支，增加了本地消息数据库的口令加密等功能，并提供两个版本：一个与 Signal 一样包含依赖 Google 的专有组件，另一个是不含这些组件的 “Molly-FOSS” 版本。由于分支复用 Signal 的源码，上游的每一项安全修复——新的库版本、证书黑名单、协议变更——都需要分支维护者合并后用户才能真正受益。与此同时，Signal 自身也在增加诸如将单一账户关联到多台设备的能力，这消除了人们过去偏好 Molly 的原因之一。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://molly.im/">Molly is an improved Signal app for Android</a></li>
<li><a href="https://github.com/mollyim/mollyim-android">mollyim/mollyim- android : Enhanced and security-focused fork of Signal .</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者普遍对 Polly 的过渡版本及其具体修复表示认可；同时有用户纠正了原帖中的说法，指出从 signal.org 下载的 Signal APK 会通过通知自行更新，而且往往比 Play 商店更早。还有人批评 Signal 对第三方客户端的态度，认为像 Unified Push 和免 Google 构建这类在分支中已能正常工作的功能，上游完全可以提供。也有参与者声称 Signal 的反分支政策是为了掩盖与政府合同相关的后门；这一说法在讨论中未经证实，应视为猜测而非事实。</div>
<div class="news-tags"><span class="tag">#signal</span> <span class="tag">#android</span> <span class="tag">#security</span> <span class="tag">#open-source-maintenance</span> <span class="tag">#privacy</span></div>
</article>
<hr>

<a id="item-7"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://xoranth.net/gcc-switch/">深入解析 GCC 如何降级（lower）switch 语句</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 30, 20:00</span></div>
<p class="news-summary">一篇技术博客（日期为 2024-01-14）逐步拆解了 GCC 在 -O3 下把 switch 语句翻译成机器码时所采用的策略：跳转表（包括 case 值整体偏移一个常量的情况）、bitset 簇（bitset cluster），以及最后把剩余 case 交给一棵按概率加权的决策树。作者指出，除 bitset 这一种降级方式外，其余策略在 clang 上同样适用。 switch 的降级方式同时影响生成代码的质量与编译器的吞吐能力，而对 Unicode 表、协议分发或包含上千条目的查找表这类大型稀疏 switch 尤为关键。Hacker News 的讨论体现了现实代价：有评论者称 LLVM 优化一个超大 switch 花了大约半小时，而 GCC 处理得更快。 文章展示了 GCC 在索引跳转表前用一个 lea 指令把带偏移的 case 标签归一化，并描述了未被转换的标签如何被批量收集为跳转表候选，其余则进入决策树阶段——该阶段会按概率把 case 列表对半切分，使两半概率大致相等，概率来源可以是 profile-guided optimization 数据或 __builtin_expect_with_probability 内建函数。评论者还指出文中汇编示例可能存在错误，例如一个可疑的常量值和一个似乎未被使用的寄存器。</p>
<div class="news-background"><strong>背景</strong> switch 语句在源码里看似简单，但编译器必须为它挑选差异极大的机器码形态。跳转表通过间接分支实现常数时间分发，代价是内存中的一张表，且对 CPU 分支预测器不太友好；由比较构成的决策树指令更多，但避免了这种间接跳转；而 bitset 测试（根据 FOSDEM 关于 GCC switch 降级的讲义，这一技术源自 Roger Sayle 在 2003 年的贡献）适合多个 case 标签指向同一目标、或取值范围密集但空洞很多的情形。所谓“降级”（lowering）指的就是把高层 switch 翻译成这些底层形态的步骤，而完美哈希（perfect hashing）是另一类技术：通过计算出的哈希把稀疏的 case 值映射到一张表，从而只需一次查表。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://archive.fosdem.org/2025/events/attachments/fosdem-2025-4547-optimizing-switch-statements-overview-and-what-s-new/slides/238244/presentat_kiQBi46.pdf">Optimizing Switch Statements in GCC - Overview and What&#x27;s New</a></li>
<li><a href="https://programming.sirrida.de/hashsuper.pdf">Improving Switch Statement Performance</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者讨论热烈且总体偏批评：有人指出 GCC 和 clang 都仍未为大型稀疏 switch 表实现完美哈希，称 LLVM 的相关补丁十年前被拒，而他自己为自研 C 编译器实现只花了一天；另一位则称 LLVM 编译一个包含全部 MAC 地址厂商的 switch 要花约半小时。还有人质疑为何生成的跳转表指向中间的跳转桩而不是直接指向目标函数，也有评论者怀疑文中汇编示例存在小错误。</div>
<div class="news-tags"><span class="tag">#compilers</span> <span class="tag">#gcc</span> <span class="tag">#code-generation</span> <span class="tag">#optimization</span> <span class="tag">#switch-statements</span></div>
</article>
<hr>

<a id="item-8"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://vitalik.eth.limo/general/2026/10/31/digital_minimalism.html">Vitalik Buterin 倡导数字极简主义：少用应用，多用本地与离线工具</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 31, 11:10</span></div>
<p class="news-summary">在 2026 年 10 月 31 日发表的一篇文章中，Vitalik Buterin 提出，他多年践行的“物理极简主义”应当延伸到“数字极简主义”——对每一次使用数字技术都保持自觉选择，而不是被默认机制牵着走。他以自己的实践为例，包括在 2024 年末至 2025 年初 X（Twitter）毒性达到高峰后减少使用，并建议每个人都至少在某一个重要的方面尝试削减自己的数字冗余。 这篇文章把数字极简主义描述为一种刚刚变得可行的选择，而不只是苦行：Buterin 认为，更好的软件与当代 AI 让人们可以用聊天机器人而非社交媒体获取信息，可以更多地在本地和离线完成工作而不再依赖互联网，也可以用命令行工具或自制界面替代网页。作为加密与开源领域的高知名度人物，他的这篇文章把 self-hosting、local-first 工具和有意选择技术的理念推向了关于隐私与注意力的更广泛讨论。 Buterin 明确指出，每个人的路径会因需求不同而不同，他也承认针对物理极简主义的反向论点——尤其是拥有合适的实物反而能让生活更自主。他还提醒要警惕“以错误方式”使用 AI 的弊端，并把数字极简主义定位为对社交媒体、互联网与万维网诸多缺陷同时达到顶峰的一种回应。</p>
<div class="news-background"><strong>背景</strong> 物理极简主义——拥有很少的物品、以更少做更多——作为一种理念在 2000 年代和 2010 年代达到流行高峰；Buterin 回溯了自己四年前写的一篇文章，介绍他随身 40 升背包里装了什么。标签和相关讨论中出现了两个相关概念：local-first software，即应用把数据主要存储在用户自己的设备上，从而在离线时仍可使用、联网后再同步（这一术语由 Ink &amp; Switch 的研究者在 2019 年的论文中提出）；以及 self-hosting，即在自己掌控的服务器上运行服务，而不是依赖托管平台。这两者都是减少对大型云服务商依赖的具体方式，也正是这篇文章论点的实践核心。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Local-first_software">Local-first software</a></li>
<li><a href="https://grokipedia.com/page/Self-hosting_network">Self-hosting (network)</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 的评论者总体持共鸣态度，不少人描述了自己长达数年的实践：一位表示大约八年前就注销了手机套餐，从此不带手机、只使用现金，以做到“在现实世界中几乎数字隐形”；另一位说他的极简版本是用功能机（dumb phone），并主要在终端里用文本浏览器上网。也有人沿用麦克卢汉的视角，追问一个把想法限制在 140 字符、或随时打断你的媒介究竟传递了什么“信息”；还有评论者补充了技术性提醒：运营商蜂窝位置数据正被专业承包公司通过 SS7/Diameter 攻击持续获取，而不仅仅是通过常规的合法或非法调取。</div>
<div class="news-tags"><span class="tag">#digital-minimalism</span> <span class="tag">#privacy</span> <span class="tag">#technology-and-society</span> <span class="tag">#smartphones</span> <span class="tag">#self-hosting</span></div>
</article>
<hr>

<a id="item-9"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://simonwillison.net/2026/Oct/30/nesformer/">NES 6502 模拟器被写入 Qwen3.5-4B 模型权重</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Simon Willison</span><span class="news-time">Oct 30, 21:59</span></div>
<p class="news-summary">Drew Breunig（dbreunig/nesformer）把任天堂 NES 所用 6502 CPU 的可用模拟器直接“烤”进了 Qwen3.5-4B 的权重里，因此像《超级马里奥兄弟》这样的 NES ROM 可以在模型内部运行——尽管速度非常慢。该项目受到 Divyansh Agrawal 早期“qwenputer”实验的启发；Breunig 在 Hacker News 评论中表示，他是通过给 Opus 5.5 写提示词完成构建的，其中还要求模型探索能否像人们在 MiSTer 上用 FPGA 那样来模拟该芯片和内存。 这是“权重内涌现计算”一个颇具冲击力的概念验证：模型并非调用外部模拟器，而是由参数本身承载经典 CPU 的逻辑。紧跟 qwenputer 之后，它标志着一种规模虽小但正在成长的实验类型——把 LLM 权重当作确定性系统的一种奇特载体，并在 Hacker News 上引发了明显关注。 Breunig 明确表示速度并非重点——目标只是拥有权重，以及一个可以指向 ROM 的 CLI；他说运行慢也没关系，并未给出任何性能或时钟频率数据。他还提到，Opus 似乎找到并使用了 Christopher Pow 大约 15 年前发布的 NES CPU 一致性测试集，这为模拟器提供了正确性基准；不过原始文章只是一段简短链接博客摘录，没有实现细节。</p>
<div class="news-background"><strong>背景</strong> NES 的核心是 MOS Technology 6502——一款 1975 年 9 月推出的 8 位微处理器，后来成为那个时代使用最广泛的 CPU 之一，也是模拟器作者和爱好者最钟爱的目标。模拟这样一颗芯片，通常意味着编写软件（或配置 FPGA），逐周期复现其指令和内存行为。启发本项目的 qwenputer 据称把一颗可用的 32 位 RISC-V 处理器嵌入了 Qwen 3.5 4B 的权重中；nesformer 则把同样的思路套用到更古老、更简单的 6502 以及完整的 NES ROM 工作负载上。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/MOS_Technology_6502">MOS Technology 6502 - Wikipedia</a></li>
<li><a href="https://dzen.ru/a/auLjxFOA8hIEhC1R">Qwenputer : в веса Qwen 3.5 4B встроили рабочий... | Дзен</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 现有材料只记录了 Hacker News 上的讨论：Breunig 在那里回复并贴出了他用来构建该系统的 Opus 5.5 原始提示词，其中包括“就当好玩”去尝试构建、即使速度不快也没关系的说法。所提供的内容中没有更广泛的舆情、批评或反驳观点可供总结。</div>
<div class="news-tags"><span class="tag">#LLM</span> <span class="tag">#emulation</span> <span class="tag">#model weights</span> <span class="tag">#novelty project</span> <span class="tag">#Qwen</span></div>
</article>
<hr>

<a id="item-10"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.theverge.com/tech/1023763/openai-google-microsoft-ai-scraping-standard-opt-out">OpenAI、Google、Microsoft 与 Anthropic 支持 robots.txt 共享退出令牌</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">The Verge AI</span><span class="news-time">Oct 30, 20:26</span></div>
<p class="news-summary">OpenAI、Google、Microsoft 与 Anthropic 表示将采用一种共享的“policy token”，发布方可以把它写进 robots.txt，从而一次性对多家公司的 AI 爬虫表达退出意愿，而不必逐家单独设置。该提案由 Anthropic 标准技术负责人 Kevin Kelley 提出，并在 IETF 框架下推进；Anthropic 已率先采用该信号，OpenAI 称将在“未来几个月”内实现，Google 和 Microsoft 则计划明年支持。 若这一机器可读的退出信号能被主流 AI 厂商共同遵守，发布方控制内容是否用于模型训练的成本将大幅降低，行业惯例也可能从逐家谈判和单独封禁转向统一的 Web 标准。这也表明，在 AI 数据采集受到越来越多审视的背景下，主要实验室更倾向于协调一致的标准化信号，而非各自为政的爬虫封禁。 Microsoft 表示将提供更细粒度的控制，让发布方可以把“退出 AI 训练”与“退出 AI grounding”（即引导模型引用经过核实的来源以减少幻觉）分开设置，并强调无论发布方作何选择，网站仍会出现在 Bing 搜索结果中；Google 也描述了类似且不影响搜索可见性的控制项。Meta 传播负责人 Andy Stone 对该共享信号表示支持，但未说明公司是否会实际遵守；此外，Google 和 Microsoft 的支持要等到明年，而非立即生效。</p>
<div class="news-background"><strong>背景</strong> robots.txt 长期以来是网站告知爬虫（搜索引擎、存档机构、AI 机器人）可访问范围的非正式方式。此前，若发布方不希望内容被用于 AI 训练，就必须逐家向各 AI 公司表达意愿，在大规模场景下并不现实。这一新令牌只是多种并行方案之一：Really Simple Licensing（RSL）标准允许发布方设定 pay-per-crawl 等机器可读的许可条款，而 Cloudflare 则已开始默认拦截 AI 爬虫。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://rslstandard.org/">RSL : Really Simple Licensing</a></li>
<li><a href="https://en.wikipedia.org/wiki/Really_Simple_Licensing">Really Simple Licensing - Wikipedia</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI policy</span> <span class="tag">#web scraping</span> <span class="tag">#content licensing</span> <span class="tag">#web standards</span> <span class="tag">#publishing</span></div>
</article>
<hr>

<a id="item-11"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.theverge.com/tech/1023528/google-project-suncatcher-ai-satellite-transmission">Google Project Suncatcher 卫星在轨运行 Gemma 模型</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">The Verge AI</span><span class="news-time">Oct 30, 18:21</span></div>
<p class="news-summary">Google 在周五的一篇博客文章中表示，其 Project Suncatcher 卫星成功启动了搭载的 Tensor Processing Unit（TPU），使在轨的 Gemma 4 模型能够响应提示词，写下一首关于身处太空的俳句。Google 还测试了其他太空主题的打油诗和遥测提示词，该卫星于本月早些时候被送入轨道。 这次测试初步证明 AI 加速器可以在轨道上执行推理工作负载，而这正是 Google 更长远目标——把由太阳能供电的 AI 数据中心送入太空——的技术基础。TPU 能否在地球大气层保护之外可靠运行，将影响整个行业对太空计算的投入程度。 Google 表示，下一轮测试将评估 TPU 在轨道上承受热应力和辐射暴露时的表现，并称验证 TPU 能在太空可靠执行工作负载将为 2027 年双星互联的下一个里程碑铺路。此次展示的工作负载——一首俳句、几首打油诗和遥测提示词——属于概念验证，而非生产级算力。</p>
<div class="news-background"><strong>背景</strong> Project Suncatcher 是 Google 的一项研究计划，探索通过把服务器硬件搭载在太阳能卫星上来将 AI 算力移出地球。TPU 是 Google 自研的 AI 加速器，与其地面数据中心使用的是同一类芯片；Gemma 则是 Google DeepMind 的开源模型系列，Gemma 4 于 2026 年 4 月发布。在轨道上运行这类硬件并不容易，因为太空中的辐射和剧烈温度变化可能导致芯片出错甚至失效。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.npr.org/2026/10/01/nx-s1-5983697/project-suncatcher-google-ai-data-center-space">Google launches Project Suncatcher , a step towards AI data... : NPR</a></li>
<li><a href="https://www.nytimes.com/2026/09/24/technology/google-suncatcher-ai-data-center-space.html">Google Is Sending an A.I. Data Center to Outer Space - The New York...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gemma_(language_model)">Gemma (language model) - Wikipedia</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI hardware</span> <span class="tag">#space computing</span> <span class="tag">#Google TPU</span> <span class="tag">#satellites</span> <span class="tag">#edge inference</span></div>
</article>
<hr>

<a id="item-12"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.theverge.com/ai-artificial-intelligence/1023188/pope-leo-disarm-ai">教皇利奥十四世呼吁&quot;解除 AI 武装&quot;并禁止致命自主武器</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">The Verge AI</span><span class="news-time">Oct 30, 14:58</span></div>
<p class="news-summary">教皇利奥十四世在周五的教皇讲话中呼吁对 AI 系统进行&quot;解除武装&quot;，并敦促联合国成员国在下个月日内瓦会议上&quot;采取具体步骤禁止致命自主武器&quot;。他还强调&quot;机器是工具，不是人&quot;，警告不要赋予 AI 系统权利或法律人格。 这次讲话为在多边论坛上进展缓慢的政策议题赋予了梵蒂冈的道德权威，可能加大各国在自主武器问题上采取行动的压力。同时，它也为 AI 法律人格之争增添了高知名度声音，将这一问题界定为不应跨越的界限。 教皇利奥将此次讲话与他 5 月发布的首份重要教皇文件相联系，该文件聚焦&quot;在人工智能时代守护人本身&quot;，并主张涉及人的生命、自由和使用武力的决定必须始终处于&quot;有效、知情且负责任的人类监督&quot;之下。他在结尾呼吁国际机构为 AI 的开发和使用提供共同标准、独立监督和明确的问责机制。</p>
<div class="news-background"><strong>背景</strong> 致命自主武器系统（LAWS）指能够依据预设约束自主搜索并攻击目标的军用无人机或机器人；截至 2025 年，大多数军用无人机和机器人仍需人类控制。自 2014 年起，各国已在《特定常规武器公约》框架下讨论 LAWS，但未达成有约束力的禁令。另一方面，AI 法律人格是一个存在争议的学术与政策问题，即 AI 系统能否享有权利并承担责任，批评者认为这一步会让问责更加混乱而非更清晰。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lethal_autonomous_weapons_systems">Lethal autonomous weapons systems</a></li>
<li><a href="https://trendsgroup.org/insight/governing-lethal-autonomous-weapons-the-future-of-warfare-and-military-ai/">Governing Lethal Autonomous Weapons in a New Era of Military AI</a></li>
<li><a href="https://link.springer.com/article/10.1007/s10506-017-9214-9">Of, for, and by the people: the legal lacuna of synthetic persons</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI ethics</span> <span class="tag">#autonomous weapons</span> <span class="tag">#AI policy</span> <span class="tag">#AI personhood</span> <span class="tag">#Vatican</span></div>
</article>
<hr>

<a id="item-13"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.interconnects.ai/p/was-i-wrong-about-open-models-and">Nathan Lambert 重新审视开放模型网络风险论点</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Interconnects (Nathan Lambert)</span><span class="news-time">Oct 30, 17:36</span></div>
<p class="news-summary">Nathan Lambert 在新文章中重新审视自己此前的观点，即开放权重 AI 模型不会实质性颠覆网络风险格局；此前出现了一波他称为“Black October”的严重漏洞披露，包括 PHP2Shell 和 GitLab，以及 Binance 的一起加密安全事件。他还回应了读者反馈，并追问所担心的风险是否真的在显现。 这篇文章的重要性在于，政策制定者和 AI 实验室正在争论是否应因网络风险担忧而限制开放权重模型，而 Lambert 主张应以攻防平衡和实际事件证据来引导讨论，而非最坏情况框架。文章还凸显了“safety”与“security”社群在如何解读 AI 赋能攻击上的日益分歧。 Lambert 并未声称风险不存在：他表示，行业将被迫更新到一种新的软件工作方式，这将代价高昂且伴随艰苦工作，他还区分了“safety”与“security”两种视角。所提供的摘录并不完整，没有提供新的实证结果，并重新审视了围绕“Claude Mythos”的叙事——该模型曾被预告为一种新型网络武器。</p>
<div class="news-background"><strong>背景</strong> 开放权重模型是指训练后的参数被公开发布、可供他人下载和运行的 AI 模型，不同于只能通过 API 访问的闭源模型。相关争论的核心是：广泛可得的模型是否会让攻击者更容易发现并利用软件漏洞；Google Threat Intelligence Group 报告称，2026 年每月披露的漏洞数量翻了一番，每月平均被在野利用的漏洞数量也接近翻番。PHP2Shell 指两个严重的 PHP 漏洞 CVE-2026-109618 和 CVE-2026-109619，可让攻击者在 Web 服务器上远程执行代码，而更新 PHP 被描述为唯一完整的修复方式。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.dynatrace.com/news/blog/cve-2026-109618-cve-2026-109619-php2shell-critical-vulnerability-what-it-is-and-what-to-do/">PHP 2 Shell : What it is and what to do | Dynatrace news</a></li>
<li><a href="https://www.securityweek.com/google-ai-is-changing-the-pace-and-profile-of-vulnerability-discovery/">Google: AI Is Changing the Pace and Profile of Vulnerability Discovery</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Lambert 表示，他此前的观点招来了“毫无希望的嘲讽尝试”和理性讨论的混合反馈。一位评论者将争论概括为“safety”人士与“security”人士之间的分歧，推荐了 Risky Business 播客，并认为经验丰富的网络安全从业者倾向于审视实际发生了什么以及本可预防事件的合理措施，而不是动辄跳到人类灭绝场景。</div>
<div class="news-tags"><span class="tag">#open models</span> <span class="tag">#AI safety</span> <span class="tag">#cybersecurity</span> <span class="tag">#AI policy</span> <span class="tag">#open-weight models</span></div>
</article>
<hr>

<a id="item-14"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.fz-juelich.de/en/news/archive/press-release/2026/mystery-of-60-second-fluctuations-in-power-grids-solved">大型电池储能的每分钟自检被指为电网 60 秒波动的成因</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 31, 19:50</span></div>
<p class="news-summary">由 Forschungszentrum Jülich 的 Dirk Witthaut 领衔、并与科隆大学和卡尔斯鲁厄理工学院研究人员合作的团队发现，大型电池储能系统每分钟进行一次荷电状态检查，正是 Tennet Germany 多年来观测到的电网频率每 60 秒短暂下跌现象的成因。相关成果发表于 Nature Energy（DOI: 10.1038/s41560-026-02144-0），并于 2026 年 10 月 30 日通过新闻稿公布。 这一发现把电网测量中长期存在却无法解释的规律性现象，归结为能源转型中一个已知且看似容易修正的副作用：研究人员指出，在大型电池储能的数据中心约占全国用电量五分之一的爱尔兰，这一分钟级信号的幅度在 2016 年至 2021 年间增长到了原来的四倍。由于这类波动已经对水电机组造成可测量的磨损，而全球储能装机仍在快速增加，理解并削弱这种同步效应对电网运营商和设备寿命都十分重要。 研究团队在 Jülich“Living Lab Energy Campus”的 80 个点位对终端设备布设测点，确认了该周期性的用电模式恰好出现在安装大型电池储能系统的位置，作者强调这一现象并非欧洲独有而是全球性的；这些偏差对电网安全并不构成关键威胁，Witthaut 还指出，空调系统、热泵、洗衣机、洗碗机等其他数字控制设备也可能表现出类似模式。研究提出的解决思路在原理上很简单：把荷电状态检查随机分散执行，而不是让所有设备同时开始检查。</p>
<div class="news-background"><strong>背景</strong> 电网必须持续平衡发电与用电，任何失衡都会表现为交流频率偏离额定值，这也是运营商和研究者密切监测频率测量的原因。大型电池储能系统为维持供电稳定提供快速支撑，而和许多现代设备一样，它们属于信息物理系统（cyber-physical）：由软件控制的硬件，把数字逻辑与物理过程耦合起来，在这里体现为周期性地查询荷电状态。当大量此类单元按照相同的内部时钟节拍动作时，它们各自微小的行为会叠加成用电需求上可见的集体节律，这正是 Jülich 领衔团队追踪并测量到的现象。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://link.springer.com/article/10.1007/s10462-024-10827-x">Trustworthy cyber - physical power systems using AI: dueling...</a></li>
<li><a href="https://www.academia.edu/164884236/Reliability_Modeling_and_Analysis_of_Cyber_Enabled_Electric_Power_Systems">(PDF) Reliability Modeling and Analysis of Cyber Enabled Electric...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#power grids</span> <span class="tag">#cyber-physical systems</span> <span class="tag">#synchronization</span> <span class="tag">#energy systems</span> <span class="tag">#research</span></div>
</article>
<hr>

<a id="item-15"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://melaniekat.com/blog/public-on-pds/">博主发现 Bluesky 的 AT Protocol 数据普遍公开，包括私人订阅源</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 30, 11:22</span></div>
<p class="news-summary">博主 melaniekat 在一篇博文中记录了对 AT Protocol「atmosphere」生态的探查：作者未经身份验证、几乎没有限制地枚举出了 Skyreader 阅读器公开存储的 1300 多个 RSS 订阅源。借助 bsky.network 这类 relay 和 PDSls.dev 浏览器，作者还发现了疑似私人的 Club MacStories 订阅源、404 Media 的付费全文源、Patreon 赞助者专属源以及 GitLab 私有仓库源，并指出类 Discord 和类 Twitch 的 AT Protocol 应用（如 Stream.place）会公开存储并可搜索全部聊天消息。 文章认为，AT Protocol 的设计使用户存放在个人数据服务器（PDS）上的数据可被公开读取和枚举，这意味着订阅一个订阅源或在应用里聊天，都可能悄悄把用户身份与其以为私密的内容关联起来。随着越来越多应用构建在共享的 Atmosphere 网络上，这引发了用户是否理解隐私后果、应用开发者是否应当作出提示的疑问。 作者发现 Skyreader 会把每个订阅发布为 lexicon app.skyreader.feed.subscription 中的一条记录，其中的 feedUrl 键包含真实的 RSS 地址。枚举全部此类记录并非一次 API 调用即可完成：向 relay 查询会返回一组 DID（去中心化标识符），还需将其解析到对应的 PDS 服务器后才能请求实际的集合记录——作者称这一流程只需「一点努力」。</p>
<div class="news-background"><strong>背景</strong> AT Protocol（Authenticated Transfer Protocol，简称 ATProto）是 Bluesky 背后的开放协议与标准，而「Atmosphere」指构建于其上的应用、服务、用户与数据构成的更大生态。用户可以自建个人数据服务器（PDS）来存放自己的记录仓库；按设计这些仓库基本是公开的，任何知道标识符的人都可以读取。Lexicon 是描述这些记录结构的 schema 定义，因此像 app.skyreader.feed.subscription 这样的 lexicon 定义了一种可预测、可查询的数据形态，便于其他工具大规模枚举。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AT_Protocol">AT Protocol - Wikipedia</a></li>
<li><a href="https://atproto.com/guides/lexicon">Lexicons - AT Protocol</a></li>
<li><a href="https://www.bskyinfo.com/glossary/atmosphere/">Atmosphere | AT Protocol Glossary</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AT Protocol</span> <span class="tag">#Bluesky</span> <span class="tag">#privacy</span> <span class="tag">#decentralized social networks</span> <span class="tag">#data exposure</span></div>
</article>
<hr>

<a id="item-16"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://tangled.org/blog/forge/">Tangled 推出基于 AT Protocol 的联邦化代码托管平台</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 30, 17:57</span></div>
<p class="news-summary">Tangled 宣布推出其所称的首个真正联邦化的代码托管平台（code forge），构建于 AT Protocol 之上：任何人都可以自行托管 Git 托管、CI runner、API 服务器或完整 UI，同时仍能与网络中的其他人协作。此次发布包含用 Rust 重写的 knot 服务器 knot2（在同一二进制中内置自研 Git 服务器与 SSH 服务器）、名为 bobbin 的全球分布式内存索引服务、全新的 Svelte 边缘部署前端、组织（Organization）账户，以及面向 Git 与 Jujutsu 用户的堆叠式 PR（stacked PR）。 代码托管长期集中在少数几家中心化平台上，而一个既能让你把仓库与身份放在自己掌控的基础设施上、又能与其他人互通的代码托管平台，为那些担心可用性、供应商锁定与平台治理的项目提供了可信的替代方案。据报 Gleam 项目迁移至 Tangled，说明联邦化代码托管平台已开始吸引真实的开源社区，而不只是实验性用户。 新的数据模型位于 org.tangled.* 这套 lexicon 之下，取代了此前的 sh.tangled.* 记录；bobbin 被描述为纯只读、只处理 AT Protocol 数据，部署在 11 个以上区域以在全球范围内保持较低的 API 与 UI 延迟。组织是免密码的委托账户，在 Tranquil PDS 上拥有独立的 DID 与 handle，通过 New Organization 页面创建后获得 &lt;name&gt;.tngl.sh，并可将 handle 换成自己拥有的域名；私有仓库、CLI、各类 SDK 以及 agent 技能将在接下来几周内推出。</p>
<div class="news-background"><strong>背景</strong> 代码托管平台（code forge）是像 GitHub 或 GitLab 那样托管源代码、评审变更并让贡献者协作的平台。AT Protocol 是一套用于去中心化发布与自认证数据的开放标准，最初作为 Bluesky 的技术基础开发；在其中有 DID 与 handle 标识用户身份，数据存放在称为 PDS 的服务器上的个人仓库中。联邦化（federated）软件让相互独立的服务器能够互操作，因此不必由一家公司运营全部服务，多个主机可以通过共享协议彼此通信。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AT_Protocol">AT Protocol</a></li>
<li><a href="https://www.developersdigest.tech/blog/gleam-tangled-atproto-code-hosting">Gleam Moves to Tangled: What the ATProto Code Forge Means for...</a></li>
<li><a href="https://news.ycombinator.com/item?id=50305573">The federated code forge | Hacker News</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#federated code forge</span> <span class="tag">#AT Protocol</span> <span class="tag">#decentralization</span> <span class="tag">#open source</span> <span class="tag">#developer tools</span></div>
</article>
<hr>

<a id="item-17"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://aatishb.com/myriad/lets-build-a-brain/">一起造个大脑：互动式神经回路讲解</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 31, 15:09</span></div>
<p class="news-summary">Aatish Bhatia 与 Arkarup Banerjee 在 Myriad 上发布了互动文章《Let’s Build a Brain》，让读者通过连接感觉神经元和运动神经元，组装一个名为 spark 的趋光小生物。文章依次演示单眼与双眼回路，说明兴奋性和抑制性连接如何让 spark 冲过头、停在光源处或转向光源。 这篇讲解把神经科学的核心问题——神经元集合如何产生行为——变成可动手操作的演示，对学生以及关注计算神经科学和 AI 的读者都很有价值。它还把简单回路的连接方式与学习和重新布线联系起来，而这与大脑如何获得新技能密切相关。 这些 spark 基于 Valentino Braitenberg 1984 年的著作《Vehicles: Experiments in Synthetic Psychology》，该书提出了一系列关于传感器、执行器和行为的思维实验。一个关键结论是：只有一只眼和一只鳍时，spark 可以加速但无法转向；加入第二只眼和鳍，并使用抑制性连接后，差速转向才成为可能，使它转向光源并停下。</p>
<div class="news-background"><strong>背景</strong> Braitenberg 车辆是用于具身认知思维实验的想象生物，由意大利控制论学者 Valentino Braitenberg 于 1984 年提出。它们配有传感器和执行器，在假设环境中移动，追逐或回避等定向行为来自基于感觉输入的差速转向。Braitenberg 描述了十四种复杂度递增的车辆类型，这一思维实验已被用于神经科学、人工生命和机器人学。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Braitenberg_vehicle">Braitenberg vehicle</a></li>
<li><a href="https://library.agnescameron.info/artificial+intelligence/Vehicles,+Experiments+in+Synthetic+Psychology,+Valentino+Braitenberg+(1984).pdf">Vehicles , Experiments in Synthetic Psychology</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#neuroscience</span> <span class="tag">#computational neuroscience</span> <span class="tag">#neural circuits</span> <span class="tag">#interactive explainer</span> <span class="tag">#education</span></div>
</article>
<hr>

<a id="item-18"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://futhark-lang.org/blog/2026-10-31-faster-copying.html">Futhark 通过置换迭代空间加速 GPU 拷贝</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 31, 17:03</span></div>
<p class="news-summary">Futhark 博客发布文章，介绍编译器现在通过置换拷贝循环的迭代空间来加速某些 GPU 数组拷贝，并利用了只有在运行时才能获知的数组布局信息。作者称在某些基准测试（例如 slice_2d）中获得了约 36 倍的加速。 数据拷贝是编译器最常生成的代码之一，因此即使是对内存搬运循环的适度改进，也可能影响 Futhark 这类数组语言中的许多程序。这篇文章还体现了编译器领域的一个更广泛趋势：利用运行时布局信息做出仅靠静态分析无法完成的决策。 这条新路径是一种启发式兜底方案：当描述源和目标布局的线性内存访问描述符（LMAD）过于复杂、无法静态分析时，编译器会退回到逐元素拷贝循环，并将其展平为单个并行 GPU 循环。作者指出在报告的案例中绝对性能并不算好，约为 514 GiB/s，并把该技术形容为“大概更多是好玩而非实用”，因为它只对部分程序有较小的影响。</p>
<div class="news-background"><strong>背景</strong> Futhark 是一种数据并行数组语言，其编译器面向 GPU 后端（也包括 CPU 后端）。它使用线性内存访问描述符（LMAD）来表示数组布局，这是一种结构化的索引函数，把 n 维索引元组映射为内存块中的扁平偏移量。由于 GPU 不支持嵌套并行，嵌套的拷贝循环必须展平为单个循环，而该循环遍历内存的顺序会强烈影响性能。这篇文章延续了同一博客系列此前关于整数除法、加法等看似平淡的编译话题的文章。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://ejnar.sigkill.dk/publications/sc22-mem.pdf">Memory Optimizations</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/3-540-35767-X_21">Compiling for a Hybrid Programming Model Using the LMAD ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#compiler optimization</span> <span class="tag">#GPU computing</span> <span class="tag">#Futhark</span> <span class="tag">#memory copies</span> <span class="tag">#performance engineering</span></div>
</article>
<hr>

<a id="item-19"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://blog.persistent.info/2026/10/infinite-mac-beos.html">Infinite Mac 将 BeOS 带入浏览器</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 30, 16:06</span></div>
<p class="news-summary">Infinite Mac 现在允许用户直接在浏览器中运行多个 BeOS 版本，提供完整安装、通过流式磁盘镜像实现的即时启动、预装软件、来自 Internet Archive 的 CD-ROM，以及可保存工作的“Saved HD”驱动器。 这让一个具有历史意义的替代操作系统能轻松触达复古计算爱好者，也让用户得以探索苹果寻找下一代操作系统过程中的“未走之路”。 该集成依赖 DingusPPC 模拟器和 Power Macintosh 7300 配置；BeOS Developer Release 8.2 带有时间炸弹，在 1997 年 4 月 1 日之后无法启动，因此项目使用自定义日期支持来硬编码一个可用日期。大型磁盘镜像采用流式传输以实现快速启动，操作系统 CD-ROM 则镜像到 Cloudflare R2 存储桶，因为从 Internet Archive 流式读取已变得不稳定。</p>
<div class="news-background"><strong>背景</strong> BeOS 由 Be Inc. 开发，是一个以多媒体为重点、支持多任务和多线程的操作系统，最初面向 BeBox，后来移植到 Power Macintosh 电脑。苹果在寻找下一代操作系统时曾考虑收购 Be，这使 BeOS 成为 Mac 历史中常被提及的另一条时间线。Infinite Mac 是一个基于浏览器的模拟项目，让用户无需本地安装即可运行经典 Macintosh 系统及相关平台。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/BeOS">BeOS - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Haiku_(operating_system)">Haiku (operating system ) - Wikipedia</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#retro-computing</span> <span class="tag">#emulation</span> <span class="tag">#BeOS</span> <span class="tag">#browser</span> <span class="tag">#Infinite Mac</span></div>
</article>
<hr>

<a id="item-20"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://seriot.ch/computation/curl.html">curl 意外图灵完备长达九个月</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 30, 07:24</span></div>
<p class="news-summary">一篇新分析指出，curl 8.12 至 8.16 可借助 config 文件特性模拟任意双计数器 Minsky 程序，因此在理想化的无界资源假设下构成图灵完备。curl 8.17.0 增加了五层 include 上限，从而破坏了这一构造。 这一发现的重要性在于，它显示广泛部署工具的 config 语言可能意外具备极强表达能力，对解析器设计、资源限制和安全审查都有启示。实际来看，这更像理想化组合性结论，而非现实可利用能力。 该构造把计数器值 n 表示为 n 个 x，用 expand-variable 实现递增/递减，并用字节切片配合 expand-config 实现条件跳转；真实二进制受 MAX_EXPAND_CONTENT（10,000,000 字节）和 C 栈限制，在 curl 8.12 的 8 MB 栈上，一个最小循环只能执行 922 步。8.17.0 的 include 上限为五层，其公开理由和回归测试主要针对防止自我包含，而非图灵完备问题。</p>
<div class="news-background"><strong>背景</strong> curl 是一个使用 URL 语法传输数据的命令行工具，其 config 文件允许用户通过 -K 提供大量选项。图灵完备系统在原则上只要时间和内存无界，就能计算任何可计算内容。双计数器 Minsky 机是一种与图灵机等价的最小计算模型，因此能模拟任意此类程序就足以在上述理想化条件下确立图灵完备性。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CURL">cURL - Wikipedia</a></li>
<li><a href="https://curl.se/docs/manpage.html">curl - How To Use</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 文中包含读者 Jonathan Tremesaygues 的后续反馈，他用这一 curl config 构造实现了“99 Bottles of Beer on the Wall”，以一个熟悉的程序展示了该归约。文中未提供更广泛的讨论情绪。</div>
<div class="news-tags"><span class="tag">#curl</span> <span class="tag">#Turing completeness</span> <span class="tag">#config parsing</span> <span class="tag">#computability</span> <span class="tag">#security</span></div>
</article>
<hr>

<a id="item-21"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://uecker.codeberg.page/2026-10-31.html">C 语言有效类型规则与编译器一致性</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 31, 21:59</span></div>
<p class="news-summary">Martin Uecker 发布《Effective Type: Part 1》，详细考察 C 语言有效类型规则如何支持基于类型的别名分析，以及优化编译器如何处理这些规则。文章认为，Clang 除非用 -fno-strict-aliasing 关闭 TBAA，否则不符合 ISO C 规则；GCC 虽在 2020 年修复了一个关键的 store motion 问题，但仍有未解决的缺陷。 这些规则是编译器进行 TBAA 优化的基础，用于提升性能，但违反规则或编译器缺陷可能让看似合法的 C 代码变成未定义行为或被错误编译。该分析对复用内存或进行 type-punning 的 C 程序员，以及负责一致性和优化正确性的编译器开发者都很重要。 Uecker 指出，实际规则比简单的类型兼容更细微：允许限定符和有符号性不同，字符类型存在例外，结构体或联合体成员可以直接通过指针访问。该文是第 1 部分，刻意把示例简化为只涉及类型兼容的情形，并提到 GCC PR 57359 和 LLVM bug 21725。</p>
<div class="news-background"><strong>背景</strong> C 的有效类型规则可追溯到 ANSI X3.159-1989，并在 C99 中扩展以处理没有声明类型的对象，例如 malloc 返回的堆内存。按照这些规则，通过非字符类型的左值进行存储，会为该对象在后续读取时设定有效类型，从而使编译器可以假设不兼容类型的指针不会别名。这一假设支持基于类型的别名分析（TBAA）优化，但也可能与复用内存或 type-punning 等底层编程技巧冲突。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://open-std.org/JTC1/SC22/wg14/www/docs/n3519.pdf">Understanding Effective Type Aliasing in C</a></li>
<li><a href="https://gustedt.wordpress.com/2016/08/17/effective-types-and-aliasing/">Effective types and aliasing – Jens Gustedt&#x27;s Blog</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#C language</span> <span class="tag">#effective type</span> <span class="tag">#type-based aliasing</span> <span class="tag">#compilers</span> <span class="tag">#undefined behavior</span></div>
</article>
<hr>