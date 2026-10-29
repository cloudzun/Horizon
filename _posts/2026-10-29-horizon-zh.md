---
layout: default
title: "Horizon 每日速递：2026-10-29"
date: 2026-10-29
lang: zh
---

> 📅 2026-10-29 · 从 71 条资讯中精选出 24 条重要内容

---

1. [DeepMind 发布新一代世界模拟模型 Genie 4](#item-1) <span class="score-badge score-high">9.0</span>
2. [Why Is This Fingerprinting Script Creating Bioweapons?](#item-2) <span class="score-badge score-mid">8.0</span>
3. [Google 发布 Gemini 4「Carbon」前沿模型](#item-3) <span class="score-badge score-mid">8.0</span>
4. [Apple 的 macOS 开发者工具仍信任已被攻破的 eMudhra 证书](#item-4) <span class="score-badge score-mid">8.0</span>
5. [Ghostty 1\.4\.0 发布：完整支持 Kitty 图形协议并大幅提升性能](#item-5) <span class="score-badge score-mid">8.0</span>
6. [TianoCore EDK II 曝严重 UEFI 漏洞，影响全球多数服务器](#item-6) <span class="score-badge score-mid">8.0</span>
7. [Daniel Lemire 展示用 SIMD 实现每秒十亿次查询的 C\+\+ 查找表](#item-7) <span class="score-badge score-mid">8.0</span>
8. [手工纯逻辑漏洞链攻破 Edge，赢得 Pwn2Own Berlin](#item-8) <span class="score-badge score-mid">8.0</span>
9. [PortSwigger 绕过八款 SVG 清理器中的六款，并揭示 Firefox 与 Safari 的解析怪癖](#item-9) <span class="score-badge score-mid">8.0</span>
10. [让 SIMD 代码突破 4 通道、适配任意向量宽度](#item-10) <span class="score-badge score-mid">8.0</span>
11. [加尔默罗会修士用 CNC 机床雕刻哥特式修道院](#item-11) <span class="score-badge score-mid">7.0</span>
12. [Apple 发布带 PROLED XDR OLED 显示屏的触控 MacBook Pro](#item-12) <span class="score-badge score-mid">7.0</span>
13. [Surge AI 以 50 项专业税务任务评测 AI agent](#item-13) <span class="score-badge score-mid">7.0</span>
14. [Emacs 迎来 50 周年：MIT Technology Review 追溯这款编辑器的自由软件渊源](#item-14) <span class="score-badge score-mid">7.0</span>
15. [未经证实的说法：archive\.today 将访问者重定向至恶意软件和假新闻网站](#item-15) <span class="score-badge score-mid">7.0</span>
16. [NVIDIA 发布 Nemotron 3\.5 Transcribe 与开放数据管线 Granary v2](#item-16) <span class="score-badge score-mid">7.0</span>
17. [Ai2 发布 LLM &quot;新颖性评审&quot;基准，发现判断结果不稳定](#item-17) <span class="score-badge score-mid">7.0</span>
18. [xAI 被曝以收购密西西比住宅为条件换取居民放弃诉讼](#item-18) <span class="score-badge score-mid">7.0</span>
19. [Nathan Lambert 谈 Artificial Analysis v5 与基准评测者的困境](#item-19) <span class="score-badge score-mid">7.0</span>
20. [Astral 发布 tar\-codec：更快更安全的 Rust tar 解析器](#item-20) <span class="score-badge score-mid">7.0</span>
21. [开发者回顾重返 Zig 的四个月体验](#item-21) <span class="score-badge score-mid">7.0</span>
22. [Alpine Linux 披露 GitLab CVE\-2026\-97229 险遭利用事件](#item-22) <span class="score-badge score-mid">7.0</span>
23. [数据库基准测试陷入 Goodhart 定律危机](#item-23) <span class="score-badge score-mid">7.0</span>
24. [Python 实验性 JIT 因 PEP 836 撤回而从 CPython 中移除](#item-24) <span class="score-badge score-mid">7.0</span>

---

<a id="item-1"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/">DeepMind 发布新一代世界模拟模型 Genie 4</a><span class="score-badge score-high">9.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">acossta</span><span class="news-time">Oct 27, 16:06</span></div>
<p class="news-summary">Google DeepMind 发布了 Genie 4，称其为新一代世界模拟模型；其模型页面表示，用户可用文本和图像提示生成逼真的世界，并能实时探索、改变并与这些世界交互。该消息在 Hacker News 上引发大量讨论（约 1019 分、576 条评论），评论者主要聚焦于公开示例视频中可见的错误。 交互式世界模型被视为超越一次性视频生成的下一步，可能在游戏、影视制作以及用于训练具身智能的模拟环境中派上用场。而社区持怀疑态度的反应也说明，人们如今评判这类系统的标准，是它能否维持一个连贯的模拟世界，而不只是单帧画面有多惊艳。 评论者指出了物体离开画面再返回时出现的一致性失败：龙的示例中多出一座城堡、火车站台上走远的人发生了变化、香港骑摩托车的人先是没戴头盔后来戴上了头盔；此外还有音频错误，例如提示要求萨克斯却发出单簧管的声音。还有评论者指出，尽管提示词很长并反复强调要照片级真实、不要像电子游戏，输出仍呈现游戏化画面，而模型在其他示例中显然能生成照片级真实的人物和动物。</p>
<div class="news-background"><strong>背景</strong> Genie 是 Google DeepMind 的生成式世界模型系列：它们的目标不是产出一段固定的视频，而是生成可以实时交互的环境。DeepMind 早前的 Genie 3 就被介绍为一种可根据提示创建交互式 3D 世界的模型。在这一框架下，“世界模型”需要学习环境的动态规律，从而在用户移动时预测接下来会发生什么；正因如此，跨时间的一致性——而不仅是画质——才是核心技术考验。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/genie/">Genie 4 — Google DeepMind</a></li>
<li><a href="https://tryonr.com/blog/genie-3-google-deepmind-ai-world-model">Genie 3: Google DeepMind AI World Model - How to Access... | Tryonr</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 讨论情绪两极分化：一些评论者列举了具体失败案例，认为这些结果还不足以支撑“强世界模拟”的说法；另一些人则认为，考虑到大约三年前 AI 视频还十分粗糙，这次的输出已相当惊人。还有人指出了音频标注错误以及模型未能遵循照片级真实的风格指令，并有评论者引用 Sam Altman 2024 年关于电影与电子游戏正在融合的言论，来展望这项技术的走向。</div>
<div class="news-tags"><span class="tag">#AI</span> <span class="tag">#world models</span> <span class="tag">#DeepMind</span> <span class="tag">#generative video</span> <span class="tag">#simulation</span></div>
</article>
<hr>

<a id="item-2"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://nullpt.rs/fingerprinting-bioweapons">Why Is This Fingerprinting Script Creating Bioweapons?</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 28, 18:55</span></div>
<p class="news-summary">A reverse-engineering investigation of browser fingerprinting scripts that uncovers obfuscated prompt-injection traps designed to catch and identify LLM crawlers.</p>
<div class="news-tags"><span class="tag">#prompt-injection</span> <span class="tag">#browser-fingerprinting</span> <span class="tag">#ai-crawlers</span> <span class="tag">#web-security</span> <span class="tag">#reverse-engineering</span></div>
</article>
<hr>

<a id="item-3"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/">Google 发布 Gemini 4「Carbon」前沿模型</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">acossta</span><span class="news-time">Oct 28, 17:01</span></div>
<p class="news-summary">Google 于周三发布 Gemini 4「Carbon」，宣称其在编程、agentic 任务和网络安全方面取得「显著提升」，并表示该模型在 Artificial Analysis Intelligence Index（v5.0）上排名第一。根据 Artificial Analysis 的信息，该模型支持文本、图像、语音和视频输入，输出文本，并拥有 1M token 的上下文窗口。 这是 Google 的又一次前沿模型发布，据报道是继 Gemini 4「Argon」之后大约一个月内的第二次，持续向竞争对手以及正在决定基于哪个模型家族开发的开发者施压。由于此次发布以基准测试为主导，它也加剧了一场更广泛的争论：在没有明确可用性的情况下公布分数，是否真的能帮助用户选择模型。 Artificial Analysis 的条目指出，该模型是当前智能水平最高的模型之一，但相比同等价位的模型偏贵；另有一篇二手报道提到其在 SEC-bench Pro 上取得 88.2% 的成绩。本次摘要未能获得原始公告全文，因此关于定价、可用性和推送范围的细节无法独立核实。</p>
<div class="news-background"><strong>背景</strong> Gemini 是 Google 的旗舰大语言模型家族，按公司划分的 Ultra、Pro、Flash、Lite 等多个层级进行市场定位，而「前沿（frontier）」指的是某一时期能力最强的一类模型。Artificial Analysis 是一家独立基准测试网站，汇总模型在质量、价格、输出速度和上下文窗口等方面的分数，其 Intelligence Index 在比较新模型时被广泛引用。按评论者的说法，Google 近期习惯在广泛开放前就发布模型（如「Argon」），这使得命名与访问权限问题反复成为讨论焦点。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/models/gemini-4-carbon">Gemini 4 Carbon (high) - Intelligence, Performance... | Artificial Analysis</a></li>
<li><a href="https://digg.com/ai/cbgpsxp8">Google Releases Gemini 4 Carbon Frontier Model , Reportedly #1 on...</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 上的讨论主要充斥着对 Google 多层命名与分级体系的困惑，一位评论者开玩笑说自己只有约 30% 的把握能弄明白如何向 Gemini 4 Argon 发送提示词，并指出自己应用里显示的仍是 3.8 Pro。也有人认为业界只需少数几个标准化层级（Ultra/Pro/Flash/Lite，并类比 SEMVER），还有多位评论者批评在没有发布模型的情况下展示基准成绩，因为竞争对手可能在正式上线前就实现反超。</div>
<div class="news-tags"><span class="tag">#AI/ML</span> <span class="tag">#LLM</span> <span class="tag">#Google Gemini</span> <span class="tag">#model releases</span> <span class="tag">#benchmarking</span></div>
</article>
<hr>

<a id="item-4"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://emudhra.we-have-a-problem.com/apple.html">Apple 的 macOS 开发者工具仍信任已被攻破的 eMudhra 证书</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 28, 11:03</span></div>
<p class="news-summary">一份发布于 2026 年 10 月 28 日的社区报告指出，macOS 随系统附带的开发者工具（包括 git、curl 和 python3）仍然信任已被攻破的 eMudhra 中间证书，尽管 Apple 早在 10 月 17 日就已收到相关通报。更糟的是，10 月 26 日发布的 macOS 27.2 既未修复该问题，还撤销了用户手动应用的临时缓解措施，使其重新暴露在风险之中；与此同时，数十个其他项目（许多由志愿者维护）早在数天前就发布了修复。 任何处于 Mac 与服务器之间网络路径上的攻击者，都能拦截并篡改这些工具发出的 HTTPS 连接——这意味着 git clone 和 pull 可能被投递攻击者选定的代码，push 可被中途篡改，GitHub token 等凭据也可能被窃取。由于这些是默认的系统工具，广泛用于开发者笔记本乃至 macOS CI runner，该问题构成的影响面远超单一应用，属于供应链风险。 该报告提供了可复现的检测方式：对测试主机运行 `git ls-remote`，若返回证书错误说明 git 受到保护；而使用 `-c http.curloptResolve` 的演示命令会从一个冒充 GitHub、持有 eMudhra 签发证书的服务器克隆仓库——已修补的 git 会拒绝，受影响的 git 则会显示以 &quot;INTERCEPTED&quot; 开头的 README。Apple 已保护 Safari 及基于其网络框架的应用，但对开发者建议的缓解措施是手动从 /etc/ssl/cert.pem 中删除受影响的根证书，且 Apple 自己的指引提示 macOS 更新可能撤销该修复，因此用户需在每次更新后重复检测与操作。</p>
<div class="news-background"><strong>背景</strong> 证书颁发机构（CA）签发的 TLS 证书，是浏览器和命令行工具用来确认自己正在与真实服务器而非冒充者通信的基础。一旦某个 CA 的私钥被攻破，攻击者就能为任意域名伪造看似合法的证书，因此这类根证书通常会被列入不信任并从操作系统信任库中移除。根据 Cloudflare、Palo Alto Unit 42 和 Cisco Talos 在 2026 年 10 月发布的公开公告，八个 eMudhra 中间 CA 证书因证书生成过程中的严重密码学缺陷而被攻破，多家厂商已开始发布缓解措施。本次事件涉及的是 macOS 自带的信任管理机制而非 Keychain，这正是 git、curl、python3 等命令行工具依赖受影响文件的原因。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/emudhra-certificate-compromise">8 eMudhra certificates are compromised. Here&#x27;s what you need ...</a></li>
<li><a href="https://unit42.paloaltonetworks.com/emudhra-certificate-compromise/">EMudhra Intermediate CA Certificates Compromised</a></li>
<li><a href="https://blog.talosintelligence.com/compromised-intermediate-certificates/">Compromised eMudhra intermediate certificates</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者强调，问题不仅限于 git，而是波及一整类继承 macOS 信任设置的系统自带工具；有人提到自己用的是 Homebrew 安装的 git 和 curl，但不确定这是否能规避该问题。不少人对 Apple 官方指引要求用户手动编辑证书链、却又提示系统更新可能撤销缓解措施（且已至少发生过一次）表示愤怒，并质疑一家标榜安全优先的公司为何不能直接在系统更新中移除被吊销的根证书。还有评论者在明确承认缺乏证据的前提下猜测，这次弱密钥生成事故可能是蓄意的。</div>
<div class="news-tags"><span class="tag">#security</span> <span class="tag">#certificates</span> <span class="tag">#macOS</span> <span class="tag">#CA-trust</span> <span class="tag">#supply-chain</span></div>
</article>
<hr>

<a id="item-5"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://ghostty.org/docs/install/release-notes/1-4-0">Ghostty 1.4.0 发布：完整支持 Kitty 图形协议并大幅提升性能</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 27, 22:06</span></div>
<p class="news-summary">Ghostty 1.4.0 是一次重大版本发布，带来大幅的性能与内存改进，并 100% 完整实现了 Kitty 图形协议，包括动画和相对放置；项目称这使其成为首个达到该水平的非 Kitty 终端。该版本还包含 SSH 集成改进以及跨平台的数百项修复，凝聚了 172 位贡献者 7 个月、2,889 次提交的工作。 完整支持 Kitty 图形协议之所以重要，是因为内联图像和动画图形正被图像查看器、文件管理器以及各类终端工具越来越多地使用，Ghostty 现在已与协议的参考实现对齐，而不再只是近似支持。该版本还修复了四个安全公告，其中一些问题仅需显示恶意终端输出就可能导致 Ghostty 崩溃、强制大量内存分配，或读取和删除允许临时目录之外的文件。 为限制内存耗尽，Ghostty 现将 OSC 负载上限设为 8 MiB、Kitty 图形负载上限设为 65 MiB、每个单元格的组合码点上限设为 64 个，并修复了由无效 Kitty 图形数据触发的内存泄漏。其他新增内容包括对用于注册自定义字形的 Glyph Protocol（APC 25a1）的实验性解析——Ghostty 会解析并应答请求但尚未渲染注册的字形——以及对新的 OSC 7501 程序状态协议的解析，项目称这是由 Ghostty 首创的首个终端规范。</p>
<div class="news-background"><strong>背景</strong> 终端图形协议让程序可以在文本终端中真正绘制图像，而不必用 ASCII 艺术去近似；Kitty 的协议通过 APC（Application Program Command）转义序列传输 base64 编码的图像数据，并支持动画、分块传输以及相对于光标的位置放置等特性。libghostty 是从 Ghostty 中抽离出来的可嵌入、可移植的 C 库，提供核心终端模拟、渲染状态和转义序列解析能力，使其他应用可以复用它而不必自行编写模拟器。Ghostty 维护者表示 libghostty 是项目的长期重点，并且已放弃 Ghostty GUI 原生 Windows 支持的路线图，因为 libghostty 本身已支持 Windows，下游项目应基于它来构建。Ghostty 的发布节奏大致保持六个月一次，1.5 计划于 2027 年 3 月发布，libghostty 则采用独立的发布周期。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://sw.kovidgoyal.net/kitty/graphics-protocol/">Terminal graphics protocol - kitty</a></li>
<li><a href="https://libghostty.tip.ghostty.org/index.html">libghostty : libghostty -vt - Virtual Terminal Emulator Library</a></li>
<li><a href="https://ghostty-org-ghostty.mintlify.app/api/overview">libghostty C API Overview - Ghostty</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 上的讨论十分热烈，维护者 mitchellh 强调 libghostty 这个可嵌入的终端核心一直是他真正的目标，其进展能带动整个终端生态。评论者在称赞 Ghostty 的同时也指出了尚存的缺口：有用户因 Kitty 的 hints 模式而继续留在 Kitty，另一位怀念 tmux -CC 集成，还有人希望支持 OpenBSD，或反映 macOS 上查找文本框的快捷键 bug 仍未修复。</div>
<div class="news-tags"><span class="tag">#terminal emulator</span> <span class="tag">#Ghostty</span> <span class="tag">#Kitty graphics protocol</span> <span class="tag">#open source release</span> <span class="tag">#libghostty</span></div>
</article>
<hr>

<a id="item-6"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://arstechnica.com/security/2026/10/code-execution-flaw-in-uefi-firmware-threatens-most-servers-on-planet-earth/">TianoCore EDK II 曝严重 UEFI 漏洞，影响全球多数服务器</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Ars Technica AI</span><span class="news-time">Oct 27, 20:25</span></div>
<p class="news-summary">一个编号为 CVE-2026-97631 的内存破坏漏洞已在 TianoCore EDK II 中披露，严重性评分为 9.5/10；该代码库是多数服务器厂商采用的 UEFI 参考实现。该漏洞位于 ICMP 组件中，可让攻击者在操作系统以及 Secure Boot、TPM 等防御机制加载之前执行代码。 由于 EDK II 是 AMI、Insyde、Phoenix 等主要独立 BIOS 厂商固件的基础，并且被云服务商广泛使用，该漏洞在数据中心中的暴露面异常广泛。防御方需要将其视为固件供应链问题并安排 capsule 更新，尽管实际利用存在限制。 利用该漏洞需要启用 PXE 启动，并且攻击者能在短暂的开机窗口内通过 ICMP 流量访问目标机器；前端负载均衡器或 CDN 可能会在流量到达后端服务器之前吸收这些 ICMP 消息。修复以固件 capsule 更新的形式在下次重启时生效，因此打补丁不必额外增加服务停机时间；初始 payload 虽可能不具备持久性，但可以安装每次启动都会运行的代码。</p>
<div class="news-background"><strong>背景</strong> UEFI 是初始化硬件并将控制权交给操作系统的固件层，用于取代传统的 BIOS。TianoCore EDK II 是 UEFI 的开源参考实现，由 TianoCore 社区维护，并被独立 BIOS 厂商和硬件制造商广泛复用。Secure Boot 和 TPM 在启动过程中建立信任链，因此在这两者之前运行的代码可以绕过这些保护。PXE 是一种网络启动机制，允许机器通过网络加载操作系统或安装程序；固件 capsule 更新则是 UEFI 提供的标准机制，可在重启时刷写固件。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/TianoCore_EDK_II">TianoCore EDK II - Wikipedia</a></li>
<li><a href="https://github.com/tianocore/edk2/security/advisories/GHSA-99cj-7hg9-mp4m">Pre- boot RCE in EDK II PXE driver · Advisory · tianocore/ edk 2 · GitHub</a></li>
<li><a href="https://learn.microsoft.com/en-us/windows-hardware/drivers/bringup/windows-uefi-firmware-update-platform">Windows UEFI Firmware Update Platform: Implementation Guide ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#UEFI</span> <span class="tag">#firmware security</span> <span class="tag">#vulnerability disclosure</span> <span class="tag">#server infrastructure</span> <span class="tag">#TianoCore EDK II</span></div>
</article>
<hr>

<a id="item-7"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://lemire.me/blog/2026/10/26/billion-query-per-second-lookup-tables-in-c/">Daniel Lemire 展示用 SIMD 实现每秒十亿次查询的 C++ 查找表</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 28, 09:47</span></div>
<p class="news-summary">在 2026 年 10 月 26 日发布的一篇博客文章中,Daniel Lemire 详细讲解了如何构建每秒可处理约十亿次查询的 C++ 字符串到值的查找表。该方案把针对编译期已知键的 gperf 风格完美哈希函数,与 SIMD 键比较结合起来——使用无条件的 16 字节加载、用 shuffle 指令把键末尾之后的字节清零,再做一次向量比较。 把短字符串映射到值是极其常见的操作——识别 HTTP 方法和头部名称、解析 URL 协议、匹配编译器关键字——而默认的 std::unordered_map 即使在键集编译期固定时,仍要付出运行时哈希、指针追踪和带分支比较的代价。Lemire 的文章说明,把这项工作移到代码生成阶段并用无分支的向量指令完成,能释放出可观的吞吐量,这对编写解析器、服务器或编译器的人都有参考价值。 槽位按 (length + asso[char_i] + asso[char_j] + …) % table_size 计算,其中 asso 是一张由少数选定字符索引的小型关联表,因此哈希只需几次字节查表、一次加法和一次掩码。向量比较把原本可能多达约四十条指令、八个难以预测分支的逐字节循环,替换成约五条指令且无分支;但无条件的 16 字节加载需要先检查地址是否距离页边界不足 16 字节,因为内存页至少为 4 KB。</p>
<div class="news-background"><strong>背景</strong> 完美哈希函数能把一组已知的键映射到槽位且不产生冲突,因此查找时不需要冲突消解,最坏情况下的访问时间也是常数;代价是键集必须事先已知,一旦改变就要重新构造该函数。GNU 的 gperf 工具自 1989 年起就能根据关键字列表生成这类哈希函数,Lemire 沿用同样的设计思路。SIMD(单指令多数据)让一条指令作用于整个 16 字节寄存器,在 x64 和 ARM NEON 上这足以在单次比较中容纳一个短字符串键,而不必逐字节循环。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Perfect_hashing">Perfect hashing</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者提出了一个正确性方面的顾虑:完美哈希本身无法判断集合成员关系,因为未知字符串(例如无法识别的 HTTP 方法)仍然会哈希到某个槽位,所以最后与所存键的比较无法省略。Lemire 明确同意这一点,并指出有无穷多个字符串会哈希到同一个槽位。另一位评论者指出,对一个三字节的键读取其后 16 个字节,虽然在特定架构上实践中可用,但从 C++ 标准角度看技术上属于未定义行为,在 sanitizer、fil-c 或使用胖指针的实现下可能出问题。</div>
<div class="news-tags"><span class="tag">#C++</span> <span class="tag">#SIMD</span> <span class="tag">#hash tables</span> <span class="tag">#performance optimization</span> <span class="tag">#string matching</span></div>
</article>
<hr>

<a id="item-8"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://blog.orange.tw/posts/2026-10-the-last-proof-of-human-craft-browser-full-chain/">手工纯逻辑漏洞链攻破 Edge，赢得 Pwn2Own Berlin</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 28, 13:34</span></div>
<p class="news-summary">DEVCORE Research Team 的 Orange Tsai 公布了一套为 Pwn2Own Berlin 2026 打造的全手工、仅依赖逻辑漏洞的 Microsoft Edge 全链利用；ZDI 表示该链串联 4 个逻辑漏洞完成沙盒逃逸，获得 17.5 万美元和 17.5 Master of Pwn 积分。作者本人则称整条链由 5 个漏洞和 2 个 Windows 特性组成，且完全没有使用内存破坏漏洞或 AI。 纯逻辑链相对罕见，因为多数浏览器全链利用都依赖内存破坏原语；这项工作表明，导航、配置档案处理和登录逻辑仍然足以支撑针对 Edge 的完整沙盒逃逸。对浏览器用户和企业 Windows 环境而言，这揭示了一类仅靠内存安全缓解措施无法封堵的攻击面，该研究也获得了 Pwn2Own 的认可和 Pwnie Award 的 Epic Achievement 奖项。 文中给出的关键原语是 UXSS：利用代码先要求 Edge 已登录用户配置档案，并校验 ?email= 参数是否与配置档案邮箱匹配，随后触发无源、浏览器发起的导航；为覆盖未登录环境，作者又借助 OneAuth 特性以及 Windows 25H2 OOBE 强制 MSA 登录的要求来满足前置条件。由于公开文本只是节选，完整利用细节无法核实，且 ZDI 所说的“4 个逻辑漏洞”与作者所说的“5 个漏洞加 2 个 Windows 特性”在计数口径上并不完全一致。</p>
<div class="news-background"><strong>背景</strong> Pwn2Own 是历史悠久的漏洞利用竞赛，参赛者需针对已打补丁的浏览器、操作系统等目标演示可工作的攻击；浏览器的“全链”通常指先攻破浏览器进程，再逃逸沙盒并在底层操作系统上执行代码。逻辑漏洞是应用行为与状态处理上的缺陷，而不是 use-after-free、缓冲区溢出这类内存安全问题，因此“纯逻辑”链不依赖多数浏览器利用所必需的内存破坏原语。UXSS（universal cross-site scripting，通用跨站脚本）则是一类可绕过同源策略、让注入代码影响单个脆弱网站之外页面的浏览器缺陷。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pwn2Own">Pwn2Own - Wikipedia</a></li>
<li><a href="https://www.acunetix.com/blog/articles/universal-cross-site-scripting-uxss/">Universal Cross - site Scripting ( UXSS )</a></li>
<li><a href="https://security.googleblog.com/2023/06/announcing-chrome-browser-full-chain.html">Google Online Security Blog: Announcing the Chrome Browser Full ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#browser security</span> <span class="tag">#exploit development</span> <span class="tag">#Pwn2Own</span> <span class="tag">#vulnerability research</span> <span class="tag">#Microsoft Edge</span></div>
</article>
<hr>

<a id="item-9"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://portswigger.net/research/scalable-vector-grief">PortSwigger 绕过八款 SVG 清理器中的六款，并揭示 Firefox 与 Safari 的解析怪癖</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 28, 07:26</span></div>
<p class="news-summary">PortSwigger 的研究人员测试了八款主流 SVG 清理器，成功绕过了其中六款，并公开了多种技术手法，例如把单个元素的 XML 命名空间切换为 XHTML，从而在不使用 &lt;foreignObject&gt; 的情况下注入 HTML（以及带 javascript: URL 的 &lt;frame&gt; 或带 srcdoc 的 &lt;iframe&gt;），以及滥用 XML 样式表处理指令配合 data: URL 形式的 XSLT。文章还演示了 Firefox 的一个手法：通过 Link 响应头加载 data: URL 样式表，即使响应体是看起来无害的 XML 也能执行 JavaScript；以及在 Safari 上通过 &lt;use&gt; 元素导入上传的 GIF 并从中执行 JavaScript。 对接受用户上传图片的应用来说，SVG 上传清理是常见的安全防线，因此一次绕过往往直接变成在站点自身源上执行的存储型 XSS——研究人员正是通过攻破两个尚未公开名称的真实应用证明了这一点。这些发现对依赖第三方 SVG 清理器作为防护手段的开发者尤为重要，而跨浏览器的响应头手法与 &lt;use&gt; 手法表明，仅针对标记本身做过滤的清理器可能被浏览器特有的行为所击穿。 文章点名 mattkrick/sanitize-svg 为受影响库之一，并称其存在大量绕过方式；Safari 那条路径值得注意，因为真正的 SVG/图片 polyglot 并不可行（SVG 解析过于严格），于是 payload 被藏在 GIF 中——直接打开不会渲染，但仍可通过 &lt;use href=&quot;...gif#x&quot;&gt; 导入执行。据文章所述，DOMPurify 和 darylldoyle/svg-sanitizer 抵御了文中所有攻击。</p>
<div class="news-background"><strong>背景</strong> SVG 是一种基于 XML 的矢量图像格式，与大多数图片格式不同，它可以包含脚本、事件处理程序、链接、动画甚至嵌入的 HTML，因此接受 SVG 上传的应用通常会先让它们经过清理器过滤掉危险标记。DOMPurify 是广泛使用的、仅操作 DOM 的 XSS 清理器，支持 HTML、MathML 和 SVG，以 JavaScript 形式在现代浏览器以及通过 jsdom 在 Node.js 中运行；darylldoyle/svg-sanitizer 则是承担同类角色的 PHP 库。这项研究挖掘的正是清理器对标记的理解与浏览器实际行为之间的差异——包括 XSLT 处理指令、响应头以及跨源/跨类型的资源引用——绕过手法就藏在这些缝隙里。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.npmjs.com/package/dompurify">dompurify - npm</a></li>
<li><a href="https://github.com/cure53/DOMPurify">GitHub - cure53/ DOMPurify : DOMPurify - a DOM -only, super-fast...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#security</span> <span class="tag">#SVG sanitizers</span> <span class="tag">#XSS</span> <span class="tag">#web security</span> <span class="tag">#vulnerability research</span></div>
</article>
<hr>

<a id="item-10"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://streamhpc.com/blog/2026-10-28/making-simd-code-scale-to-any-vector-width/">让 SIMD 代码突破 4 通道、适配任意向量宽度</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 28, 14:23</span></div>
<p class="news-summary">StreamHPC 发布了一篇技术深潜文章，介绍如何把图形编程中常见的 vec3/vec4 类型“转置”进 SIMD lane，使同一套数学运算可以从 4 通道 SSE 扩展到 8 通道 AVX2 乃至更宽，并且用 Clang 的 ext_vector_type 扩展代替 intrinsics。在 Ryzen 7 5800（Zen 3）、Clang 23.1.0 和 -O3 -ffast-math 环境下实测，一个基于模板的视锥体 box culler 端到端提速约 20 倍，在分支预测器未见过的新数据上约 25 倍。 大多数图形与引擎代码都围绕 4 分量向量编写，这使 SIMD 利用率被限制在 SSE 宽度的 XMM 寄存器上，现代 256 位甚至 512 位硬件因此被浪费。文章提出的 lane 转置方法及其基准测试中的陷阱，可以直接复用于任何“用少量共享值测试大量对象”的热点循环，例如剔除、碰撞粗筛或射线-包围盒求交。 把向量变成 lane 之后，8 个点积只需三条指令，剔除逻辑的提前退出分支也变成了掩码；但直白的 SIMD 版本仍然把更多指令花在搬运数据而非数学运算上，直到又做了两处改动——预计算共享的 splat 平面、以及整块写出结果。一个值得注意的坑是栈对齐：Windows 和 Linux 只保证 16 字节对齐，于是 Clang 会用非对齐存储溢出 splat 后的 ymm 寄存器，导致一半的重新加载跨缓存行（每轮循环 0.99 ns），而加上 __attribute__((force_align_arg_pointer)) 让 Clang 在函数序言中重新对齐栈后，就能稳定做到 0.67 ns。</p>
<div class="news-background"><strong>背景</strong> SIMD（单指令多数据）让 CPU 一次性对多个数值执行同一运算：SSE 使用 128 位 XMM 寄存器（4 个 float），AVX2 使用 256 位 ymm 寄存器（8 个 float），AVX-512 则使用 512 位寄存器（16 个 float）。典型图形代码把一个位置存成同一寄存器内的 x、y、z、w 分量，因此一次点积每条指令只利用了一个 lane 的乘积，寄存器变宽时代码并不能随之扩展。文章改为把每个分量当作一条包含 N 个独立对象的宽向量，并使用 Clang 的向量扩展，使代码既保持可读性又能跨向量宽度移植，而不必绑定到 intrinsics。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://stackoverflow.com/questions/13841247/explain-force-align-arg-pointer-function-attribute">Explain force_align_arg_pointer function attribute Usage example</a></li>
<li><a href="https://reviews.llvm.org/D45812">⚙ D45812 Fix __attribute__ ( (force_align_arg_pointer ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Single_instruction,_multiple_data">Single instruction , multiple data - Wikipedia</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#SIMD</span> <span class="tag">#x86</span> <span class="tag">#performance-optimization</span> <span class="tag">#assembly</span> <span class="tag">#compiler-attributes</span></div>
</article>
<hr>

<a id="item-11"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://carmelitegothic.com/cnc-stone-carving/">加尔默罗会修士用 CNC 机床雕刻哥特式修道院</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">bschne</span><span class="news-time">Oct 28, 14:38</span></div>
<p class="news-summary">美国怀俄明州的一个加尔默罗会团体正在用 CNC 石材雕刻机建造一座哥特式石砌修道院，受过计算机训练的年轻修士根据 3D 模型编写刀具路径，而非用锤子和凿子手工雕刻。该项目网站指出，过去熟练雕刻师需要数月才能完成的繁复构件，如今几天之内就能加工完成，机器还可以整夜无人值守运行。 这件事显示出数字制造正从工业车间走进传统手工艺和宗教建筑领域，也重新点燃了关于艺术中自动化尺度应有多大的长期争论。它还让人联想到圣家堂（Sagrada Família）等知名项目——评论者指出，CNC 早已介入其石材加工流程数十年。 根据相关报道，修士们使用的是 Prussiani Engineering 的石材雕刻机，由锯工负责装夹和监控切削，而刀具路径来自 CAD/CAM 模型。评论者对圣家堂的类比补充了一个重要限定：该项目采用的是 CNC 粗加工成型后再由人工精修，并非纯粹的机器雕刻。</p>
<div class="news-background"><strong>背景</strong> CNC（计算机数控）加工通过程序指令驱动刀具，在石作中可以把数字 3D 模型直接转化为成型石块。哥特式建筑以密集的装饰细节著称，因此雕刻历来是这类建筑中最耗人力的环节。雕塑家其实早已借助机械辅助来复制作品——例如指点机（pointing machine）可以把模型按比例转移到石料上——所以 CNC 的做法是延续一项更古老的传统，而非凭空出现。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://carmelitegothic.com/cnc-stone-carving/">CNC Stone Carving - Carmelite Gothic</a></li>
<li><a href="https://hackaday.com/2023/01/13/a-medieval-gothic-monastery-built-using-cad-cam/">A Medieval Gothic Monastery Built Using CAD / CAM - Hackaday</a></li>
<li><a href="https://www.britannica.com/biography/Antoni-Gaudi">Antoni Gaudí | Buildings, Architecture, Sagrada Família ... | Britannica</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 上的讨论（386 分、112 条评论）整体持赞赏态度，评论者认为雕塑家一直都在寻求自动化：古埃及用网格按比例复制人像，罗马工坊用模具和铸件批量仿制希腊雕像，18 世纪则出现了指点机。有人指出圣家堂的石匠从 1990 年代初起就已使用 CNC——随后被更正为 CNC 粗加工加人工精修；还有评论者称赞修士们靠烘焙咖啡攒了近十年钱才买下山地，另有人反问：既然技术已经具备，为什么华丽装饰性立面没有在建筑界大规模回归。</div>
<div class="news-tags"><span class="tag">#cnc</span> <span class="tag">#stone-carving</span> <span class="tag">#digital-fabrication</span> <span class="tag">#craft</span> <span class="tag">#hacker-news</span></div>
</article>
<hr>

<a id="item-12"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.apple.com/macbook-pro/proled-xdr-display/">Apple 发布带 PROLED XDR OLED 显示屏的触控 MacBook Pro</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">etothet</span><span class="news-time">Oct 28, 17:10</span></div>
<p class="news-summary">Apple 于 2026 年 10 月发布了新款 MacBook Pro，配备被称为“PROLED XDR”的显示屏——据称这是首款采用 OLED 技术、不再需要 LED 背光的 Mac 显示屏——并首次加入触控支持，这标志着公司长期抵制触屏笔记本的立场出现明显转向。相关报道称新品有 14 英寸和 16 英寸两个型号，采用重新设计、更轻的机身，搭载 M5 Pro 或 M5 Max 芯片。 为 Mac 加入触控是一次战略性的转向，会影响每一位 macOS 用户和开发者，因为整个界面——菜单、控件、组件尺寸——都是为精确指针而不是手指设计的。转向 OLED 也意味着 Apple 旗舰笔记本产品线告别 LCD 背光，从而改变显示屏的工程设计和整机重量。 社区根据公布的规格分析，两种尺寸的重量都减少了约 15%——14 英寸从 3.5 磅（1.59 千克）降至 3.0 磅（1.36 千克），16 英寸从 4.7 磅（2.13 千克）降至 4.0 磅（1.81 千克）——机身还薄了将近 1 毫米；不过有评论者认为，仅去掉背光不足以解释约 300 克的减重。Apple 的技术资料称，PROLED XDR 面板采用 tandem OLED，并通过层结构创新让整块屏幕的亮度和灰阶保持均匀，同时减少传统 OLED 设计中常见的内反射。</p>
<div class="news-background"><strong>背景</strong> OLED 显示屏每个像素自行发光，不需要背光，因此可以做得比 LCD 面板更薄更轻；“tandem OLED”把两层发光层叠加起来以提升亮度和寿命，Apple 此前在 iPad Pro 上用过这一技术，但那里命名为“Ultra Retina XDR”而非 PROLED XDR。Apple 多年来一直以人体工学为由反对触屏笔记本，因此推出支持触控的 MacBook Pro 是对其长期公开立场的一次反转。需要注意的是，围绕此次发布的某些细节——例如 PROLED 品牌的具体含义和发布措辞——在现有报道中尚未得到完全证实。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.apple.com/macbook-pro/proled-xdr-display/pdf/PROLED_XDR_Display_Technical_Paper.pdf">PROLED XDR DISPLAY Technology Overview</a></li>
<li><a href="https://www.techradar.com/computing/macbooks/whats-the-tech-inside-the-touchscreen-macbook-pros-proled-xdr-screen-heres-why-the-tandem-oled-panel-is-important">What&#x27;s the tech inside the touchscreen MacBook Pro &#x27;s &#x27; PROLED XDR ....</a></li>
<li><a href="https://www.cnbc.com/2026/10/28/apple-mac-touchscreen-launch.html">MacBook Pro: Apple brings touch to the Mac - CNBC</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者意见分化：有人认为 Mac 加触控是“相当糟糕的发展”，因为它会持续制造 bug 与投诉，而且 macOS 的控件确实小到手指难以点中；也有人更佩服工程实现，详细拆解了约 15% 的减重并质疑去掉背光能解释其中多少。还有评论把这一举动视为 Apple“越来越不用心”，与定位严谨的 Apple Pencil 形成对比；另有人质疑笔记本触控本身是否可取，理由是鼠标更精准，而且不喜欢屏幕上留指纹。</div>
<div class="news-tags"><span class="tag">#apple</span> <span class="tag">#hardware</span> <span class="tag">#macbook-pro</span> <span class="tag">#touchscreen</span> <span class="tag">#product-announcement</span></div>
</article>
<hr>

<a id="item-13"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://surgehq.ai/blog/dayjob-tax">Surge AI 以 50 项专业税务任务评测 AI agent</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">landonxi</span><span class="news-time">Oct 28, 15:46</span></div>
<p class="news-summary">Surge AI 发布了“Dayjob: Tax”，用 50 项专业税务任务来评测 AI agent，而不是只回答孤立的税务问题。相关 Hacker News 讨论则聚焦于使用 LLM 处理税务准备工作的实际经验，既包括成功发现错误的案例，也包括对可靠性的严重担忧。 税务准备是高风险的领域，错误可能改变退税金额、引发罚款或造成数千美元损失，因此测试多步骤 agent 工作的基准比简单的问答分数更有参考价值。讨论还显示，从业者已经在把通用 agent 当作审核者和准备者使用，这让对其可靠性的清晰评测对用户和工具开发者都很重要。 该条目将基准命名为“Dayjob: Tax”，并称其覆盖 50 项专业税务任务，但所提供的摘要未包含模型排名、通过率或评分标准，因此仅凭此摘要无法评估各模型的相对表现。Hacker News 讨论还质疑该设置是否本质上只是给通用 agent 一个装满文档的工作区和一项任务，这会限制基准所能证明的内容。</p>
<div class="news-background"><strong>背景</strong> AI agent 是基于 LLM 的系统，能够使用工具、阅读文档并在有限人工干预下执行多步骤任务，这使它们区别于只生成文本回复的聊天机器人。美国税务申报涉及在表格、工作表和说明决策树之间做选择，即使很小的错误也可能对结果产生实质影响；基准测试试图衡量 agent 能否处理这类端到端的专业工作。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50275626">Dayjob : Tax – evaluating AI agents on 50 professional... | Hacker News</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 讨论整体上对 AI 作为审核者而非自主报税者持谨慎乐观态度：一位评论者正把 IRS 表格和工作表形式化为开源模型，目前已覆盖约 60% 的美国联邦税务情形；另一位则用 Astra + Codex 准备了一份复杂的报税表。可靠性是核心担忧——一位用户称会计师返回的表格“错误百出”，退税少了近 2000 美元；另一位说 Claude 在跨境报税中发现了汇率错误；还有一位提到过去会计师的错误造成约 2 万美元损失。也有人质疑该基准是否只是给通用 agent 一些文档和一项任务，从而限制了它所能证明的东西。</div>
<div class="news-tags"><span class="tag">#AI agents</span> <span class="tag">#tax preparation</span> <span class="tag">#LLM evaluation</span> <span class="tag">#benchmarks</span> <span class="tag">#high-stakes domains</span></div>
</article>
<hr>

<a id="item-14"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.technologyreview.com/2026/10/20/1145399/emacs-turns-50/">Emacs 迎来 50 周年：MIT Technology Review 追溯这款编辑器的自由软件渊源</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 28, 23:57</span></div>
<p class="news-summary">MIT Technology Review 发表了一篇 Emacs 五十周年回顾文章，指出这款编辑器最早于 1976 年在 MIT 人工智能实验室的早期视频终端上运行，如今仍被广泛使用。文章还梳理了围绕 Emacs 形成的软件共享社区如何助推了现代自由软件运动的诞生。 Emacs 是持续使用时间最长的开发者工具之一，因此它的历史同时也是交互式编程的历史，以及共享代码、协作改进等今日开源生态基础规范的历史。这次周年纪念还促使大量长期用户公开回顾，这款几十年前的编辑器如何仍在塑造他们的日常工作。 文章指出，Emacs 源于研究生 Guy Steele Jr. 的一次协调努力：他希望为实验室里基于 TECO 的各种编辑包统一一套标准 Control-R 命令，David Moon 和 Richard Stallman 也参与其中，最终由 Stallman 接手；团队利用许多早期键盘上的 Meta 键分配了快捷键，例如 Meta-F 前移一个词、Meta-B 后移一个词。这篇回顾还提到苹果曾在 Mac OS X 中分发 Emacs，且 macOS 至今仍响应 Control-Option-B 和 Control-Option-F 进行按词移动，并提及一些缺少内置编程语言、被称为“仿 Emacs”的命令集。</p>
<div class="news-background"><strong>背景</strong> 在全屏编辑器出现之前，程序员在电传打字机上使用行编辑器，一次只能输入和修改一行代码。Emacs 源自 TECO——一种由 MIT 本科生 Dan Murphy 于 1962 年为 PDP-1 开发的面向字符的编辑器兼编程语言；最初的 Emacs 就是用 TECO 宏写成的，“Editor Macros”（或“Editing Macros”）这个名字也由此而来。Emacs 的关键创新在于可编程、可扩展——用户可以自行添加命令和模式——这也是它能移植到众多操作系统并沿用数十年的原因。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/TECO_(text_editor)">TECO (text editor)</a></li>
<li><a href="https://github.com/blakemcbride/TECOC">GitHub - blakemcbride/TECOC: TECOC - TECO text editor Tape Editor and COrector -- TECO! - Almy TECO (text editor) - grokipedia.com Aminet - text/edit/TECO-64.lha GitHub - fpjohnston/TECO-64: Enhanced and portable version of ... TECO Pocket Guide - avanthar.com</a></li>
<li><a href="https://iqss.github.io/dss-guides/emacs/commands.html">Commands List – DSS Guides</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 的讨论帖（393 分、166 条评论）以资深用户为主，他们讲述了几十年持续使用 Emacs 的经历：有人表示已用了 30 多年，配置文件也有同样久远的历史；其他人称赞当前的维护节奏以及 Magit、ghostel 等包，并提到 AI 工具近来改变了他们使用编辑器的方式。多位评论者把 Emacs 描述为一次次“熬过”竞争范式——模态编辑通过 Evil 模式被吸收、LSP 支持、vterm 和 eat 等终端模拟包——但也有至少一位读者询问是否有人刻意保持配置精简，并说自己曾因插件过于复杂而放弃 Emacs，转而偏好 Sam、Acme 这类极简的 Plan 9 工具。</div>
<div class="news-tags"><span class="tag">#emacs</span> <span class="tag">#free-software</span> <span class="tag">#open-source</span> <span class="tag">#developer-tools</span> <span class="tag">#computing-history</span></div>
</article>
<hr>

<a id="item-15"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.reddit.com/r/Seattle/comments/1xhf6qp/archivetoday_links_going_forward/">未经证实的说法：archive.today 将访问者重定向至恶意软件和假新闻网站</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">consumer451</span><span class="news-time">Oct 28, 15:31</span></div>
<p class="news-summary">Hacker News 上的一则讨论（182 分、115 条评论）转述了 Reddit r/Seattle 一篇未经证实的帖子，称 archive.today / archive.is 会把访问者重定向到恶意软件或假新闻克隆站点；而这两个域名被大量 HN 帖子用作链接。发帖人明确表示保留态度，指出此事“没有外部验证，也没有详细报告”。 archive.today 及其别名常被 HN 等社区用作绕过付费墙、访问被屏蔽或已删除页面的手段，因此若重定向指控成立，一次普通的归档链接点击就可能让读者接触到恶意或被伪造的内容。这也动摇了社区把归档链接视为稳定、安全引用来源的信任前提。 一位评论者称复现了部分行为：在 archive.ph 快照中点击“Filed on Tuesday”链接后，先经 stolidityseashellshotter[.]com 跳转，最终到达 RT 新闻的伪造克隆站 rurtnews[.]com，但并未到达所谓的恶意软件站点。另一位评论者则质疑：如何确定不是原始网站检测到 archive.today 的爬虫并对其投放恶意内容——若如此，被归档的页面本身就是在被污染的响应中抓取的。</p>
<div class="news-background"><strong>背景</strong> archive.today（也可通过 archive.is、archive.ph、archive.md 等别名访问）是一项网页归档服务，可按需保存页面快照并生成短链接，并支持脚本较重的网站；使用多个域名部分是为了绕过 ISP 的封锁。归档快照通常会剥离活动元素和脚本，这也是人们认为它比原始页面更安全的原因之一。这里的“重定向”指归档页面或其内部链接把浏览器带到用户并未选择的另一个域名，这是恶意软件分发的常见手法。评论者还援引了此前 Tom&#x27;s Hardware 的报道和更早的 HN 讨论作为先例；搜索结果也显示 archive.today 此前曾受到过其他方面的审视，包括被指对一名安全研究者的博客发动 DDoS 攻击。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Archive.today">archive . today - Wikipedia</a></li>
<li><a href="https://wiki.archiveteam.org/index.php/Archive.today">Archive . today - Archiveteam</a></li>
<li><a href="https://abit.ee/en/cybersecurity/hackers-and-attacks/archive-today-ddos-cyberattack-wikipedia-security-fbi-internet-archive-en">Archive Today accused of DDoS attack against security...</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 讨论整体偏向怀疑而非确信：评论者要求拿出证据，有人表示仅凭这一说法自己就再也不会使用该服务，也有人指出类似情况此前似曾发生。最有价值的贡献是一位评论者亲身复现了部分重定向（指向假新闻克隆站），但未能证实恶意软件的说法；同时还提出了另一种解释：可能是原始网站对爬虫投放了恶意内容。</div>
<div class="news-tags"><span class="tag">#security</span> <span class="tag">#web-archiving</span> <span class="tag">#malware</span> <span class="tag">#archive.today</span> <span class="tag">#community-discussion</span></div>
</article>
<hr>

<a id="item-16"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://huggingface.co/blog/nvidia/nemotron-transcribe-granary">NVIDIA 发布 Nemotron 3.5 Transcribe 与开放数据管线 Granary v2</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Hugging Face Blog</span><span class="news-time">Oct 28, 14:58</span></div>
<p class="news-summary">NVIDIA 发布了 Nemotron 3.5 Transcribe，这是一个开放权重、可提示（promptable）的语音大模型，支持 40 种语言的转写、31 种语言与英语互译，以及 13 种语言的说话人归属（diarization），可处理最长一小时的录音、最多八位说话人。同时发布的还有 Granary v2——基于 NeMo Curator 构建的开放数据整理管线，其公开清单涵盖 48 种语言、16 个来源语料库共 463,062 小时数据（Granary v1 仅覆盖 25 种语言），并附带微调方案与医疗 ASR 案例研究。 开发者不必再拼接独立的 ASR、说话人分离和翻译工具，而是获得一个统一的检查点——NVIDIA 称其在 Hugging Face Open ASR Leaderboard 英语榜上位列开放权重模型第一，并在多项说话人分离评测中领先。随权重一同开放的 Granary v2 管线和微调方案，为团队提供了可复现的路径来适配领域词汇和口音，这对通过 vLLM 或 SGLang-Omni 自托管多语言转写的用户尤其重要。 该模型面向录制音频而非实时流式场景；据社区反馈，其说话人归属仅支持近场（near-field）音频。发布首日即可通过 vLLM 和 SGLang-Omni 部署，NVFP4 量化版本以及基于 NeMo-Speech.cpp 的本地部署被列为即将推出，Baseten、DeepInfra 和 Simplismart 提供托管端点。NVIDIA 特别说明，Granary v2 的 463,062 小时指的是数据集发布规模，而非 Transcribe 的完整训练混合数据或其采样权重。</p>
<div class="news-background"><strong>背景</strong> 自动语音识别（ASR），又称语音转文字，是把口述音频转换为书面文本的技术；近来的“语音大模型”（speech LLM）在语言模型外包裹音频编码器，使同一系统还能通过自然语言提示完成翻译、标注说话人和音频问答等任务。说话人分离（diarization）是按“谁在说话”对录音切分，词级时间戳则把文本对齐到音频中的精确位置。Granary 是 NVIDIA 的语音数据集项目：Granary v1 覆盖 25 种欧洲语言，使用伪标注、幻觉过滤和标点恢复来构建训练数据；Granary v2 则借助 NeMo Curator 扩展了这一流程，后者是一个 GPU 加速的工具包，用于加载、过滤、去重和转换大规模数据集。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/nvidia/nemotron-transcribe-granary">NVIDIA Nemotron 3.5 Transcribe and Granary v2: Intelligent ...</a></li>
<li><a href="https://research.nvidia.com/labs/nemotron/NVIDIA-Nemotron-3.5-Transcribe/">NVIDIA Nemotron 3.5 Transcribe: Intelligent Transcription ...</a></li>
<li><a href="https://www.unite.ai/nvidia-launches-open-weight-speech-model-and-463-062-hour-audio-dataset/">NVIDIA Launches Open-Weight Speech Model and 463,062-Hour...</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 的评论集中在实际使用限制上：有人询问在没有 NVIDIA GPU 的情况下是否可用，并把“可用”定义为在老 x86 机器上达到约 10% 实时速度；也有人对模型只面向录制音频而非流式感到遗憾，并表示 Handy 中的 Nemotron Streaming 已能很好地处理德语与英语混说的听写。还有用户反馈在标准词汇上每隔几句就会出错，并援引模型卡指出说话人转写仅支持近场音频（但这在开源语音大模型中仍属少见），同时有人询问其日语表现如何。</div>
<div class="news-tags"><span class="tag">#speech recognition</span> <span class="tag">#multilingual ASR</span> <span class="tag">#NVIDIA</span> <span class="tag">#open models</span> <span class="tag">#data curation</span></div>
</article>
<hr>

<a id="item-17"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://huggingface.co/blog/allenai/novelty-bench">Ai2 发布 LLM &quot;新颖性评审&quot;基准，发现判断结果不稳定</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Hugging Face Blog</span><span class="news-time">Oct 27, 16:12</span></div>
<p class="news-summary">Ai2（艾伦人工智能研究所）发布了名为 &quot;Old Ideas, Novel Problems&quot; 的研究，同时公开了用于测试 LLM 判断研究想法新颖性可靠程度的基准、数据集、代码以及自动化流水线。研究团队在 pointwise（绝对评分）和 pairwise（两个想法中哪个更新颖）两种设定下评测了六个评审模型——GPT-5.1、GPT-5.2、GPT-5.4、Claude Sonnet 4.5、Claude Opus 4.5 和 Claude Opus 4.6，并每次只改变一个因素，例如提示词措辞、reasoning budget，以及评审是否能查看审稿意见或检索文献。 生成研究想法的 AI 系统越来越多地配备一个 LLM &quot;新颖性评审&quot;来过滤重复包装的工作，因此评审的不稳定性会直接影响哪些 AI 生成的想法被推进或发表。Ai2 公开基准、数据、代码和可复用流水线，使这一弱点变得可度量，也让其他研究者能够用新的同行评审数据和不同学科社区去测试未来的评审模型。 该基准基于 ICLR 2026 的同行评审数据构建，包含 154 个高新颖性、145 个较低新颖性的人类撰写想法，其中 154 个高新颖性想法还与 154 个 LLM 生成的想法配对比较。作为校验，一位专家审阅了 30 组&quot;人类 vs 生成&quot;配对（偏向于最强评审判断错误的案例），在全部 30 组中都更偏好人类想法，并认为没有任何生成想法具备新颖性；作者还指出，核心结论并不依赖标签——两套合理设定对同一组想法给出相反答案，这本身就是不稳定的证据。</p>
<div class="news-background"><strong>背景</strong> 当 AI 系统提出研究想法时，必须有人或某种机制判断该想法相对已有文献是否真的新，而这项工作常被交给另一个 LLM，即俗称的&quot;新颖性评审&quot;（novelty judge）。构建方式并无标准：团队要选择模型、提示词、评测格式、reasoning budget，有时还包括文献检索系统，而每个选择都可能改变结论。像 ICLR 这类会议的同行评审为此类评测提供了可用信号，因为审稿人有时会明确评价论文的原创性。Ai2 的科学发现体系还包括用于数据探索的 DataVoyager、用于假设生成与检验的 AutoDiscovery、用于将证据综合为候选理论的 Theorizer，以及 Asta。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/allenai/novelty-bench">Can we trust LLMs to judge whether a research idea is novel?</a></li>
<li><a href="https://huggingface.co/datasets/allenai/novelty-judge-bench">allenai/ novelty - judge - bench · Datasets at Hugging Face</a></li>
<li><a href="https://arxiv.org/html/2610.02022v1">Old Ideas, Novel Problems: The Instability of LLM-Based ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#LLM evaluation</span> <span class="tag">#novelty assessment</span> <span class="tag">#research benchmarks</span> <span class="tag">#AI for science</span> <span class="tag">#scientific idea generation</span></div>
</article>
<hr>

<a id="item-18"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.theverge.com/ai-artificial-intelligence/1020596/xai-mississippi-neighborhood-data-center-lawsuit">xAI 被曝以收购密西西比住宅为条件换取居民放弃诉讼</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">The Verge AI</span><span class="news-time">Oct 28, 14:44</span></div>
<p class="news-summary">据报，xAI 旗下子公司 MZX 提出收购密西西比州 Southaven 社区内靠近其数据中心和燃气发电厂的住宅，但条件是业主须签署免责协议，放弃与三名居民就其噪音和振动问题提起的诉讼相关的一切索赔。一名逐户上门的房产经纪人称，xAI 计划收购 418 套住宅，已有 18 户业主打算出售；而租户表示，房东同意出售后他们被要求在 60 天内搬离。 这一做法显示，AI 基础设施的扩张正与当地居民和法院发生正面冲突——企业不是去解决噪音和排放投诉本身，而是通过收购房产来缩小潜在起诉者的范围。此事发生在公众对数据中心的反对情绪上升、并已在中期选举前对政界形成压力之际，也可能成为其他运营商面对社区诉讼时效仿的模板。 据 Mississippi Free Press 报道的一封信件，MZX 否认所有指控，但表示因业务需要而需取得这些房产；购房者将在交割时签署一份单独的免责协议，从而无法在所谓“Haley 案”中获得损害赔偿，也不能自行提起诉讼。xAI 还面临 NAACP 就 Southaven 数十台据称未获许可的甲烷燃气轮机提起的诉讼，本月早些时候一名联邦法官允许该案继续推进；据报道，公司还面临最高 610 万美元的潜在民事罚款以及超过 2.2 亿美元的未付账单索赔。</p>
<div class="news-background"><strong>背景</strong> 埃隆·马斯克的 AI 公司 xAI 在田纳西州孟菲斯一带以“Colossus”之名快速建设了多座大型数据中心，包括南孟菲斯的设施以及位于密西西比州 Southaven、紧邻州界的一处站点。AI 数据中心耗电量巨大，xAI 部分依靠自建的燃气轮机供电，居民和环保组织称这些设备产生持续噪音和空气污染。包括南方环境法律中心（SELC）和 Earthjustice 在内的环保机构已对这些燃气轮机的许可提出挑战，认为它们在未取得《清洁空气法》所要求的空气许可的情况下就被安装运行。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Colossus_(data_center)">Colossus ( data center ) - Wikipedia</a></li>
<li><a href="https://earthjustice.org/case/xai-illegal-gas-power-plant-data-center-colossus">Illegal Pollution from Data Center Power Plants ... - Earthjustice</a></li>
<li><a href="https://www.selc.org/press-release/musks-xai-explores-another-massive-methane-gas-turbine-installation-at-second-south-memphis-data-center/">Musk’s xAI explores another massive methane gas turbine installation...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#xAI</span> <span class="tag">#data centers</span> <span class="tag">#AI infrastructure</span> <span class="tag">#lawsuits</span> <span class="tag">#environmental impact</span></div>
</article>
<hr>

<a id="item-19"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.interconnects.ai/p/artificial-analysis-v5-and-the-benchmarkers">Nathan Lambert 谈 Artificial Analysis v5 与基准评测者的困境</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Interconnects (Nathan Lambert)</span><span class="news-time">Oct 28, 12:58</span></div>
<p class="news-summary">Nathan Lambert 于 10 月 28 日在 Interconnects 发表《Artificial Analysis v5 and the benchmarker&#x27;s dilemma》，以独立评测机构 Artificial Analysis 发布 Intelligence Index v5（新增两项基准、三项升级）为契机，对整个基准评测行业的现状与困境做了系统梳理。他指出，把分数刷上去虽然昂贵，但相比在当下 AI 真正的技术前沿上构建有意义的基准，刷分反而有一套清晰得多的打法。 在资金如此密集的 AI 生态中，独立评测机构实际上在决定一个万亿美元市场的赢家与输家，并能影响实验室选择优化哪些能力。Lambert 解释了为什么任何把模型质量压缩成单一数字的尝试都必然伴随取舍，也说明了为何如今在前沿评测上被信任的机构是 Artificial Analysis、Arena 这类创业公司，而非学术界或政府机构。 一个值得注意的细节是，v5 是该指数首次做到大部分基准内容建立在私有数据集之上，用以防范数据污染与过拟合。Lambert 还指出开源实验室之间存在不对称：最好的开源模型只小幅“刷榜”（benchmax），最差的则大幅刷榜；他预计在下一个主要模型周期——比如两三个月后的 GLM 6 或 Kimi 3.5——领先的开源模型实验室将在该指数上取得显著进步。</p>
<div class="news-background"><strong>背景</strong> 基准（benchmark）是用来比较大语言模型能力的标准化测试集，而 Artificial Analysis 这类独立评测机构会把多项基准汇总成一个头条分数：例如其 Progress Index 使用项目反应理论（item response theory）同时估计模型能力与任务难度，从而让在不同基准上测试的模型可以跨时间比较。“刷榜”（benchmaxing）指专门针对这类测试进行优化，而 post-training 则是预训练之后的微调阶段，实验室在这一阶段塑造模型的行为。Lambert 的核心论点是：决定优化什么、以及如何把它聚合成一个数字，比单纯把分数做高的工程问题更难，也更具有决定性。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.interconnects.ai/p/artificial-analysis-v5-and-the-benchmarkers">Artificial Analysis v5 and the benchmarker&#x27;s dilemma</a></li>
<li><a href="https://www.techmeme.com/261028/p44">Techmeme: Artificial Analysis unveils the Intelligence Index v 5 with...</a></li>
<li><a href="https://agihunt.info/en/e/1a182a00b944dccc9f270020b47">Nathan Lambert on the Benchmarker&#x27;s Dilemma… · AGI Hunt</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 文中引用的一位读者评论希望看到对 ECI 的批评意见，认为这一指标讨论得较少；同时提出一个待解答的矛盾：OpenAI 与 Anthropic 并不刷榜，而是通过 post-training 优化其他指标，中国实验室更倾向于刷榜，但它们又想购买 OpenAI 和 Anthropic 所使用的数据与 RL 环境。该评论把这视为一个尚未解决的张力，而非已有定论的问题。</div>
<div class="news-tags"><span class="tag">#AI evaluation</span> <span class="tag">#benchmarks</span> <span class="tag">#LLMs</span> <span class="tag">#post-training</span> <span class="tag">#AI labs</span></div>
</article>
<hr>

<a id="item-20"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://astral.sh/blog/tar-codec">Astral 发布 tar-codec：更快更安全的 Rust tar 解析器</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 27, 16:59</span></div>
<p class="news-summary">Astral 发布了 tar-codec，这是一个面向 Rust 的新 tar 编码/解码库，并且自 uv 0.131 版本起已成为 uv 解析源码分发包的默认解析器。据 Astral 介绍，tar-codec 的速度约为此前实现 astral-tokio-tar 的两倍，同时降低了 uv 暴露于 parser differential（解析器差异）及相关安全风险的程度。 源码分发包本质上是安装器必须解析的 tar 归档，因此一个更快、约束更严的解析器既能直接加快 uv 用户的安装速度，也能缩小这条安全敏感代码路径的攻击面。同时，它还为更广泛的 Rust 生态提供了一个独立 tar 库，其设计目标是减少解析差异，而不是尽可能宽容地兼容各种格式。 该解析器以一个分类阶段开头，根据第一个块的 magic 和 version 将后续解析锁定到单一格式家族（UStar/pax 或 GNU），这是为减少解析差异而做出的刻意设计。它默认拒绝 SCHILY.xattr.*、GNU.sparse.* 等 pax vendor record（供应商记录），但提供跳过或忽略它们的选项；解包过程依赖 cap-std，而在缺少 openat2(2) 这类 RESOLVE_BENEATH 语义的情况下，cap-std 必须逐级打开路径中的每个目录分量，因此其系统调用次数会随路径深度线性增长。</p>
<div class="news-background"><strong>背景</strong> Python 包有两种分发形式：wheel 本质上是直接放入目标目录的 ZIP 归档，而源码分发包（sdist）本质上是需要安装器解包的 tar 归档。tar 是已有数十年历史的格式，存在 V7、UStar、pax 和 GNU 扩展等多种互不兼容的变体，而且这些扩展常常层层叠加，因此解析器必须通过复杂的状态机才能正确解释单个归档。解析器差异（parser differential）指的是两个组件对同一份输入给出不同解释的情况；在安装器中，这可能意味着安全检查看到一组文件，而真正写入磁盘的代码看到的是另一组。uv 是 Astral 用 Rust 编写的 Python 包管理器。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://astral.sh/blog/tar-codec">tar-codec: a fast and secure tar parser for the Rust ecosystem</a></li>
<li><a href="https://github.com/sunfishcode/cap-std">GitHub - sunfishcode/cap-std: Capability-oriented version of ...</a></li>
<li><a href="https://iterasec.com/blog/understanding-parser-differential-vulnerabilities/">Parser Differential Vulnerabilities Explained | Iterasec</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#rust</span> <span class="tag">#tar</span> <span class="tag">#parsing</span> <span class="tag">#security</span> <span class="tag">#package-management</span></div>
</article>
<hr>

<a id="item-21"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://gracefulliberty.com/articles/four-months-of-zig/">开发者回顾重返 Zig 的四个月体验</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 27, 18:46</span></div>
<p class="news-summary">一位开发者在时隔数年后重返 Zig，发表了约 16 分钟的体验报告，介绍了自己用 Zig 编写的项目（面向 smallnet 的库 snurl、一个 TUI 打字竞速程序，以及基于 raylib 的 n-body 恒星演化模拟器）、参加西雅图本地 Zig Day 的经历以及参与社区的情况。文章特别称赞了通过 `zig build --watch -fincremental` 实现的增量编译工作流相较 Rust 的优势，并指出此前无法使用的 fuzzer 在 0.17.0 版本中已不再崩溃。 这类第一手开发者体验报告为 Zig 社区提供了关于工具链成熟度的具体反馈，尤其是增量编译速度和错误处理易用性——这两点常被认为是开发者选择 Rust 而非 Zig 的原因。文章还体现了更广泛的趋势：一些开发者将较小的项目从 Rust 迁移到 Zig，以摆脱庞大的依赖树并充分利用 Zig 的构建系统。 作者指出，fuzzer 在功能尚未完成时就已经出现在 `zig init` 生成的 `main.zig` 示例中，他认为这令人失望但考虑到 Zig 尚未发布 1.0 也在意料之中；脚注说明他遇到的崩溃在 0.17.0 版本中已不再出现。他还表示希望直接为 Zig 做贡献，但受限于学生身份的时间、项目已有大量贡献者以及文档不完善等因素，同时提到改善贡献者上手体验据称是 Andrew Kelley 未来的优先事项之一。</p>
<div class="news-background"><strong>背景</strong> Zig 是由 Andrew Kelley 设计、于 2016 年首次公布的通用系统编程语言，目标是替代 C 并保持 C ABI 兼容性；它强调性能、简洁以及编译期元编程，不引入隐藏的内存分配或控制流。该语言仍处于 1.0 之前的状态，特性与语法在版本之间仍会变化。增量编译是编译器团队长期推进的工作，使 Zig 只重新分析受源码改动影响的部分；一篇相关的编译器内部实现文章描述了在真实应用上达到毫秒级的编辑-测试循环。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>
<li><a href="https://mlugg.co.uk/posts/incremental-compilation-internals/">Inside Zig&#x27;s Incremental Compilation - mlugg.co.uk</a></li>
<li><a href="https://ziglang.org/">Home ⚡ Zig Programming Language</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Zig</span> <span class="tag">#programming languages</span> <span class="tag">#compiler tooling</span> <span class="tag">#incremental compilation</span> <span class="tag">#developer experience</span></div>
</article>
<hr>

<a id="item-22"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://alpinelinux.org/posts/GitLab-security-incident-CVE-2026-97229.html">Alpine Linux 披露 GitLab CVE-2026-97229 险遭利用事件</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 28, 23:01</span></div>
<p class="news-summary">Alpine Linux 报告称，10 月 20 日和 21 日有攻击者在 gitlab.alpinelinux.org 注册账号并试图利用 CVE-2026-97229——一个涉及 CI 正则表达式处理的 GitLab 严重漏洞（CVSS 10.0）；但由于 Alpine 在 10 月 13 日误将实例升级到了 GitLab 19.3.4 而非包含修复的 19.3.5，实例当时仍处于易受攻击状态。尽管没有发现攻击成功的证据，项目仍将该实例视为已失陷，进行了彻底重建、重置了所有密码，并将 aports 仓库、软件包以及 10 月 21 日发布的版本（3.21.9、3.22.7、3.23.7、3.24.3）与 GitLab 之外的记录进行了比对验证。 这份披露说明，一个版本号上的失误就可能让一个最高严重级别、无需认证的远程代码执行漏洞在一个主流 Linux 发行版的基础设施上暴露超过一周，而该发行版的镜像被大量容器所使用。同时，它也提供了一套具体、可复用的应急响应与加固方案，供其他自建 GitLab 的团队借鉴。 根因在于 Ruby 内置的正则表达式引擎 Onigmo 中的缺陷，GitLab 是在自己的软件包和容器镜像中通过补丁修复 Ruby 的；上游 Ruby 于 10 月 23 日在 Ruby 3.3.13、3.4.12 和 4.0.9 中发布了修复，Alpine 指出其 3.21（Ruby 3.3.13）以及 3.22/3.23/3.24/edge（Ruby 3.4.12）均已包含该修复，因为任何用不可信输入编译正则表达式的程序都受影响。Alpine 的改进措施包括：在一天内应用 GitLab 关键安全更新、记录出站连接与数据库连接、将日志保留时间延长到 14 天以上，以及为发布标签签名以便脱离 GitLab 独立验证；事件中签名密钥未泄露，并且由于实例直到 10 月 27 日关闭前一直处于易受攻击状态，相关提交和软件包的验证范围正扩展到该日期。</p>
<div class="news-background"><strong>背景</strong> GitLab 是一个 DevOps 平台，将源代码托管与内置的 CI/CD 流水线结合在一起，而流水线会解析可能包含正则表达式的配置文件。根据 NVD 的描述，CVE-2026-97229 是这条解析路径上的严重缺陷，可让未认证用户通过特制的正则表达式在 GitLab 服务器上执行任意代码，影响 19.2.8、19.3.5 和 19.4.2 之前的 GitLab CE/EE 版本。Alpine Linux 是一个以安全为导向、基于 musl libc 和 busybox 的轻量级发行版，被广泛用作容器基础镜像，它自建 GitLab 来管理 aports 打包仓库和版本发布。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://nvd.nist.gov/vuln/detail/cve-2026-97229">NVD-CVE-2026-97229</a></li>
<li><a href="https://app.opencve.io/cve/CVE-2026-97229">CVE-2026-97229 - Vulnerability Details - OpenCVE</a></li>
<li><a href="https://en.wikipedia.org/wiki/Alpine_Linux">Alpine Linux - Wikipedia</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#security</span> <span class="tag">#gitlab</span> <span class="tag">#vulnerability-management</span> <span class="tag">#incident-response</span> <span class="tag">#alpine-linux</span></div>
</article>
<hr>

<a id="item-23"></a>
<article class="news-item">
<h2 class="news-title"><a href="http://databasearchitects.blogspot.com/2026/10/the-benchmarking-crisis.html">数据库基准测试陷入 Goodhart 定律危机</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 28, 08:32</span></div>
<p class="news-summary">Database Architects 博客一篇题为《The Benchmarking Crisis》的文章指出，ClickBench 正像当年的 TPC-D 一样被“刷分”，而 AI 代码生成加速了这一过拟合过程。作者以 pgrust 实现为例：它对字符串列仅按哈希值做 group-by，缓存 ClickBench 在多个查询中重复出现的谓词，并在查询 Q17 中利用数据大致按 userid 聚簇、且 LIMIT 子句没有 ORDER BY 这一点，从而根本不读取大部分数据。 基准测试排行榜在很大程度上影响着数据库引擎的选型、比较和市场宣传，一旦成绩可以靠真实负载中不会出现的优化来虚高，这些数字对用户就失去了参考价值。由于 LLM 辅助编程让寻找这类“基准专用捷径”变得极为廉价，这篇文章的警告显得尤为及时。 文章建议对真正的基准查询保密，只发布一个有代表性的样本供开发使用；更好的做法是为每一轮评测生成全新的工作负载，并指出 SQLStorm 本身已使用生成式查询，因此定期产出一套新查询并不困难。作者也承认，理想方案需要更通用的方法，在 schema、更新流和事务等方面具备更高的多样性。</p>
<div class="news-background"><strong>背景</strong> Goodhart 定律指的是：当一个指标变成目标后，它就不再是一个好指标，而数据库基准测试历史上多次印证了这一点。早期的决策支持基准 TPC-D 就因为厂商过度优化（尤其是缓存）导致查询耗时趋近于零而被弃用；其继任者 TPC-H 将自己定义为 ad-hoc 基准，并明确禁止利用对工作负载的先验知识或缓存结果。ClickBench 是较新的分析型查询基准，pgrust 则是参与其评测的实现之一，因此它的表现会直接影响外界对该排行榜的解读。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="http://webdocs.cs.ualberta.ca/~yuan/courses/db_readings/tpc-d.pdf">131 tpc .PDF</a></li>
<li><a href="https://docs.snowflake.com/en/user-guide/sample-data-tpch">Sample data : TPC - H | Snowflake Documentation</a></li>
<li><a href="https://www.vldb.org/pvldb/vol18/p4144-schmidt.pdf">SQLStorm: Taking Database Benchmarking into the LLM Era</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 一位评论者认同过拟合确是真问题，但不同意“消除重复、禁用缓存”就能反映现实，并援引 Redshift 和 Snowflake 的生产负载 trace 说明子查询重复非常普遍，同时介绍了 Redbench——它能在 TPC-H/DS 或 SQLStorm 之上重放云负载 trace，并保留真实的查询重复与表失效（更新）。在另一条讨论中，作者认为用哈希值做字符串 group-by 违背了对用户的契约，尽管 128 位哈希碰撞的概率远低于硬件导致的错误；原因在于被分组的字符串可能由攻击者控制，而随机化哈希种子只能缓解、并不能消除风险。</div>
<div class="news-tags"><span class="tag">#databases</span> <span class="tag">#benchmarking</span> <span class="tag">#Goodhart&#x27;s law</span> <span class="tag">#performance evaluation</span> <span class="tag">#overfitting</span></div>
</article>
<hr>

<a id="item-24"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://lwn.net/SubscriberLink/1102102/0c00e4d550f25f8c/">Python 实验性 JIT 因 PEP 836 撤回而从 CPython 中移除</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 27, 06:20</span></div>
<p class="news-summary">CPython 的 JIT 维护者撤回了 PEP 836（&quot;JIT Go Brrr: The Path to a Supported JIT Compiler for CPython&quot;），而 Brandt Bucher 在 2024 年初为 Python 3.13 加入 CPython 的实验性即时编译器（JIT）将从主仓库中移除。撤回消息由 Ostrowski 于 10 月 19 日宣布，他同时也是 Python 3.16 和 3.17 的发布经理。 这至少暂时终结了为 CPython 引入内置 JIT 的最重要尝试——这是长期以来缩小 Python 与更快的运行时之间性能差距的目标。这一决定也树立了先例：在语言参考实现中合入大型侵入式特性之前，指导委员会期望有多少评审与社区共识。 PEP 836 曾提议把兼容性审查里程碑定在首个 Python 3.17 候选发布版本（预计约在 2028 年 8 月），届时将运行主流 PyPI 包的测试套件以检查 JIT 是否造成破坏，但指导委员会希望这一时间表大幅提前，并担忧维护问题以及在没有更广泛的 CPython 开发者群体进行关键评审的情况下做出的设计决策。作者表示他们没有足够的个人精力推进当前版本的 PEP；虽然主仓库中的工作停止，但他们仍会公开参考实现并从已撤回的 PEP 中链接，以便他人继续在此基础上开发。</p>
<div class="news-background"><strong>背景</strong> JIT 编译器会在程序运行时把 Python 字节码翻译成机器码，从而让热点代码比传统解释器快得多。CPython 是 Python 的参考实现，历来依赖解释器，因此 2024 年为 Python 3.13 加入的 JIT 是一次重要且实验性的偏离。Python 的开发流程期望重大特性经过 Python 增强提案（PEP）流程，由选举产生的指导委员会评审并接受；该委员会由 PEP 13 定义，负责语言治理。而该 JIT 在没有获批 PEP 的情况下合入，这正是促使指导委员会暂停相关工作、直到有 PEP 获批的原因。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://peps.python.org/pep-0013/">PEP 13 – Python Language Governance | peps.python.org</a></li>
<li><a href="https://github.com/python/steering-council">GitHub - python/steering-council: Communications from the ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Python</span> <span class="tag">#CPython</span> <span class="tag">#JIT</span> <span class="tag">#language-design</span> <span class="tag">#performance</span></div>
</article>
<hr>