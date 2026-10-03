---
layout: default
title: "Horizon 每日速递：2026-10-03"
date: 2026-10-03
lang: zh
---

> 📅 2026-10-03 · 从 54 条资讯中精选出 24 条重要内容

---

1. [Aleph Alpha 发布主权开放权重模型 Kolibri](#item-1) <span class="score-badge score-mid">8.0</span>
2. [OpenAI 安全报告撰写者 David Robinson 辞职，警告文化「崩坏」](#item-2) <span class="score-badge score-mid">8.0</span>
3. [Google 将 gVisor 沙箱运行时捐赠给 CNCF](#item-3) <span class="score-badge score-mid">8.0</span>
4. [Rust 融入 CPython：2026 语言峰会提案拟从 zlib 起步并加速 pip 安装](#item-4) <span class="score-badge score-mid">8.0</span>
5. [1989 年 SELF 论文的定制化技术重塑了 JIT 编译器设计](#item-5) <span class="score-badge score-mid">8.0</span>
6. [开发者记录 M4 Mac mini 上首次启动 Linux 的过程](#item-6) <span class="score-badge score-mid">8.0</span>
7. [Anthropic 博客分享 Opus 5\.5 高效使用技巧](#item-7) <span class="score-badge score-mid">7.0</span>
8. [FTL：一个面向云环境的新操作系统](#item-8) <span class="score-badge score-mid">7.0</span>
9. [ThinkingBox 基准测试：以终端后端状态评判 AI Agent](#item-9) <span class="score-badge score-mid">7.0</span>
10. [AlphaGo 核心成员撰文：LLM 并未真正在推理](#item-10) <span class="score-badge score-mid">7.0</span>
11. [苹果收紧 macOS 全盘访问权限，遏制 AI 代理滥用](#item-11) <span class="score-badge score-mid">7.0</span>
12. [Capcom 计划将 RE Engine 逐步演变为 AI 生成式游戏引擎](#item-12) <span class="score-badge score-mid">7.0</span>
13. [Meta 开源 SDK，让开发者自建 Muse AI 智能硬件](#item-13) <span class="score-badge score-mid">7.0</span>
14. [AWS CEO 发文警告社区不要阻挠 AI 数据中心](#item-14) <span class="score-badge score-mid">7.0</span>
15. [开发者遭遇隐藏在 Git post\-checkout hook 中的恶意代码攻击](#item-15) <span class="score-badge score-mid">7.0</span>
16. [The Era of Software Quality, or the Era of Ostriches?](#item-16) <span class="score-badge score-mid">7.0</span>
17. [研究者揭示 C2PA 排除区间漏洞可伪造文件时间戳](#item-17) <span class="score-badge score-mid">7.0</span>
18. [Zig 0\.17\.0 发布：重构构建系统并增强 ELF 链接器](#item-18) <span class="score-badge score-mid">7.0</span>
19. [访谈：CHICKEN Scheme 维护者 Peter Bex 谈 6\.0\.0、编译器内部与 UTF\-8](#item-19) <span class="score-badge score-mid">7.0</span>
20. [用双栈技术高效实现滑动窗口聚合](#item-20) <span class="score-badge score-mid">7.0</span>
21. [为什么开发者仍不愿“使用平台”原生浏览器 API](#item-21) <span class="score-badge score-mid">7.0</span>
22. [Kagi 停止开发 Linux 与 Windows 版 Orion，并将两者开源](#item-22) <span class="score-badge score-mid">7.0</span>
23. [Cyclone Scheme 编译器架构在 2017 年修订版技术文章中详述](#item-23) <span class="score-badge score-mid">7.0</span>
24. [Docker 镜像层的隐藏设计妥协：whiteout、SOCI 与 BuildKit 对比 OCI tar 包](#item-24) <span class="score-badge score-mid">7.0</span>

---

<a id="item-1"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/">Aleph Alpha 发布主权开放权重模型 Kolibri</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">bastitx</span><span class="news-time">Oct 3, 09:36</span></div>
<p class="news-summary">Aleph Alpha 发布了 Kolibri-1，这是一个英德双语 Mixture-of-Experts 开放权重语言模型，总参数 78B、激活参数 3B，上下文窗口最高可达 1M tokens，并以 Apache 2.0 许可证开放。随模型一同发布的还有一份异常详尽的技术报告，涵盖数据集构建流程，以及一套旨在限制幻觉的拒答（abstention）训练方案。 一家知名欧洲实验室推出能力可观的开放权重模型，并附上教程级别的文档，这增强了非美国、非中国的开放模型生态；报告的透明度也为其他团队提供了构建 agentic LLM 的具体范本。拒答训练对企业尤其有意义，因为在关键任务部署中，模型需要能够承认自己不确定。 Kolibri 是一个面向主权与关键任务场景的英德双语 Mixture-of-Experts 模型，训练时使用了拒答数据以及所谓的 “Merlin-Arthur protocol”，使其在答案不在给定上下文中时回答“我不知道”。据社区讨论，这是该团队成立不到一年来的首个发布，团队强调迭代速度；此外已有第三方免费托管该模型供公众做基准测试。</p>
<div class="news-background"><strong>背景</strong> 开放权重模型指的是将训练好的参数公开发布、任何人都可以下载、本地运行和微调的模型，与封闭 API 相对，Kolibri 采用的 Apache 2.0 是一种宽松的开源许可证。Mixture-of-Experts（MoE）架构会把每个 token 只路由到一部分参数上，因此 Kolibri 虽然总参数为 78B，每个 token 实际只激活约 3B，从而降低推理成本。“主权 AI”指的是让一个国家或组织能够完全依靠自有基础设施运行和控制 AI 系统、不依赖国外供应商的目标。这里的幻觉指 LLM 自信地生成错误或无依据的内容；拒答训练则是教会模型宁可拒绝作答也不要胡乱猜测。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/">Kolibri Has Landed: A Sovereign Open-Weight Model - Aleph Alpha</a></li>
<li><a href="https://huggingface.co/Aleph-Alpha/Kolibri-1">Aleph - Alpha / Kolibri -1 · Hugging Face</a></li>
<li><a href="https://theopenweights.com/news/kolibri-1-v2uw">Aleph Alpha releases Kolibri , a sovereign reasoning model · The ...</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者普遍称赞这份技术报告的开放程度达到了教程级别，有人表示它“把一切都讲清楚了”，包括数据集是如何构建的，并称“这是我第一次见到这种程度的开放”。有第三方提供了免 GPU、免配置的免费托管访问以便做基准测试，训练团队成员也在讨论中答疑，并指出这是团队的首个发布。最主要的质疑集中在“主权”这一表述上：有评论者认为，不提及公司与加拿大企业 Cohere 的合并计划有些误导，同时也主张非美国、非中国的实验室更应共享成本与投入。</div>
<div class="news-tags"><span class="tag">#open-weight-models</span> <span class="tag">#llm</span> <span class="tag">#hallucination-mitigation</span> <span class="tag">#sovereign-ai</span> <span class="tag">#model-releases</span></div>
</article>
<hr>

<a id="item-2"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.theverge.com/ai-artificial-intelligence/1004408/openai-safety-quits-sounding-the-alarm">OpenAI 安全报告撰写者 David Robinson 辞职，警告文化「崩坏」</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">The Verge AI</span><span class="news-time">Oct 3, 14:31</span></div>
<p class="news-summary">曾在 OpenAI 为每次重大模型发布撰写安全报告的 David Robinson 于本周辞职，并在《大西洋月刊》(The Atlantic) 发表评论文章，认为 AI 公司的文化「已经从根本上崩坏」。他表示，问题远比「再给模型训练加几条新规则或监管」更为深层。 这是一连串安全研究人员和安全岗位员工离开知名 AI 公司事件中的最新一起，可能加剧外界对前沿实验室能否可信地自我监管的质疑，并为 AI 治理讨论注入新的推动力。离职者分布在 OpenAI、Anthropic 和 Google DeepMind，说明这一现象是行业性的，而非某一家公司独有。 Robinson 主张前沿实验室应像核电站或繁忙机场那样运作，具备多层冗余和审慎、耗时的规划，以免不可避免的人为失误打开通往灾难的大门。他批评硅谷的「极度自信」「永不停歇的冲刺」和「不受约束的乐观主义」；文章还提到更早离职的人，包括 Anthropic 的 Jacob Coxon 和 Joe Benton，以及 Google DeepMind 的 Robert O&#x27;Callahan、Bilal Chughtai 和 Josh Engels。</p>
<div class="news-background"><strong>背景</strong> 在 OpenAI，重大模型发布通常都会配有一份由 Robinson 这类员工撰写的安全报告，用于记录新模型相关的风险与评估结果。围绕前沿 AI 实验室在自我安全审查上应有多大自主权的争论已持续多年，而近期这些实验室内部人员接连公开辞职并发声，让这一争论再次浮上台面。</div>
<div class="news-tags"><span class="tag">#AI safety</span> <span class="tag">#OpenAI</span> <span class="tag">#AI governance</span> <span class="tag">#tech industry</span> <span class="tag">#resignations</span></div>
</article>
<hr>

<a id="item-3"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://gvisor.dev/blog/2026/10/02/gvisor-cncf/">Google 将 gVisor 沙箱运行时捐赠给 CNCF</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 3, 02:41</span></div>
<p class="news-summary">Google 正在将 gVisor 项目（包括其名称与商标）捐赠给云原生计算基金会（CNCF），其申请于 2026-09-07 提交、2026-09-22 由 CNCF 审核、2026-09-28 获得接受，公告博客于 2026-10-02 发布。未来数周内，gVisor 将进入 CNCF 的 “Sandbox” 阶段，其构建与测试基础设施将迁移至 GitHub Actions 和 Buildkite，Google 内部的测试基础设施将不再阻塞 PR，治理模式也将转向以 maintainer 为基础的模型，非 Google 的 maintainer 将获得合并权限。 将 gVisor 交给中立的 CNCF 治理，复制了 Kubernetes 的路径，意在加速开发，并让采用者从目前以大型科技公司和高度聚焦的初创企业为主，扩展到更广泛的群体。Google 的贡献者表示，这一变化在中短期内会让贡献 PR 的体验更顺畅，长期则会带来一个 “更自由” 的 gVisor，由更开放的治理流程引导并以用户利益为导向。 博文称，据其贡献者所知，gVisor 是除 Linux 本身之外第二成熟的 Linux 实现；文中指出当前采用者主要是能够投入资源进行定制的科技巨头（Google、Ant Group、OpenAI、Anthropic），以及定位高度契合的初创公司（Modal、Tines），而业余项目与行业 “中间层” 基本缺席。Ant Group、Modal 和 Tines 已承诺长期加入 gVisor 的 maintainer 队伍，OpenAI、Tencent 和 NVIDIA 也将继续既有的贡献；博文同时强调短期内对用户而言变化不大。</p>
<div class="news-background"><strong>背景</strong> gVisor 是 Google 于 2018 年以 Apache 2.0 许可证开源的容器沙箱，它在用户态实现了 Linux 系统调用 ABI 的很大一部分，并使用内存安全的 Go 语言编写，从而在保持容器级资源效率的同时提供类虚拟化的隔离能力。它被用于 Google 的 App Engine、Cloud Functions、Cloud Run 和 GKE Sandbox 等产品，也被 DigitalOcean、Cloudflare 以及需要安全运行不可信代码的 AI 公司采用。CNCF 是 Linux 基金会旗下专注于云原生计算的子基金会，Google 当年通过捐赠 Kubernetes 促成了它的成立，而 Kubernetes 后来成长为容器编排的行业标准。博文还提到面向桌面 Linux 的沙箱化目标，将 gVisor 的潜力与当前主流方案（bubblewrap/flatpak/nsjail 等）以及 Qubes OS 这类基于虚拟化的方案进行了对比。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GVisor">GVisor</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qubes_OS">Qubes OS</a></li>
<li><a href="https://man.archlinux.org/man/bwrap.1">bwrap (1) — Arch manual pages</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#gVisor</span> <span class="tag">#CNCF</span> <span class="tag">#container security</span> <span class="tag">#sandboxing</span> <span class="tag">#open source governance</span></div>
</article>
<hr>

<a id="item-4"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://blog.python.org/2026/09/language-summit-2026-rust-for-cpython/">Rust 融入 CPython：2026 语言峰会提案拟从 zlib 起步并加速 pip 安装</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 3, 09:40</span></div>
<p class="news-summary">David Hewitt 重返 Python Language Summit 2026，为 Rust for CPython 项目提出了拟议的时间表、阶段划分和成功标准，该项目的 PEP 草案由核心开发者 Kirill Podoprigora 和 Emma Smith 撰写，Emma 也在 PyCon US 2026 上介绍了该项目。团队提议从一个范围很小的模块入手——用 zlib-rs 实现 zlib——并给出了一个假想的 Python 版 Rust API 示例，声称如果提案被接受，Python 3.16 中几乎每一次 pip install 都会变快。 如果提案被接受，Rust 有可能成为 CPython 内部长期存在的一部分，影响核心模块的实现、构建与依赖流程，以及几乎关系到所有 Python 用户的打包工作流性能。不过目前这仍是峰会上关于提案、阶段和假想 API 的讨论，而非已被接受或落地的改动，因此其影响仍是推测性的。 会议中出现了一项重要反对意见，即引入来自 Cargo 的依赖，被形容为潜在的“showstopper”；团队回应称会尽量选择最少的外部依赖（zlib-rs 只是其中一个），并对 Rust 源码进行 vendoring，使构建 CPython 不需要 Cargo，且 vendored 源码不会放在 CPython 代码树中。API 示例使用类似 Argument Clinic 的 #[pyfunction] 属性，总是传入线程与解释器状态（Python&lt;&#x27;_&gt;），用 Py&lt;...&gt; 智能指针包装对象，并借助 Rust 的 Result 枚举处理错误；团队同时指出，如何处理大量 Rust 依赖的挑战尚未解决，目前只专注于 API 和基础部分。</p>
<div class="news-background"><strong>背景</strong> Python Language Summit 是随 PyCon US 举办的仅限受邀者参加的活动，Python 核心开发者在此讨论语言的未来方向，因此其会议内容属于探索性质，而非有约束力的决定。CPython 是 Python 的参考实现，而 Rust 是一种内存安全的系统编程语言，已在 Android 和 Linux 内核等项目中得到使用；Cargo 则是 Rust 的构建系统和包管理器。zlib 是广泛使用的无损压缩库（由 Jean-Loup Gailly 和 Mark Adler 创建），而 Python 打包又高度依赖压缩，因此用更快的 zlib-rs 替换它——文中称 zlib-rs 已被 Firefox、uv 和 Cargo 使用，并在许多平台上快于 zlib 和 zlib-ng——正是单个模块的改动可能影响 pip install 时长的原因。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zlib">zlib - Wikipedia</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Rust</span> <span class="tag">#CPython</span> <span class="tag">#Python</span> <span class="tag">#Interoperability</span> <span class="tag">#Python Language Summit</span></div>
</article>
<hr>

<a id="item-5"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://dl.acm.org/doi/epdf/10.1145/74818.74831">1989 年 SELF 论文的定制化技术重塑了 JIT 编译器设计</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 3, 20:59</span></div>
<p class="news-summary">这篇 1989 年的论文描述了称为“定制化（customization）”的一系列编译器技术，能够从没有任何类型声明的动态类型 SELF 程序中恢复出静态类型信息。该系统会为一个过程编译出多个定制化副本——每种接收者（receiver）类型对应一份——在编译期预测可能出现的类型，插入运行时类型测试来验证预测，并拆分调用（call splitting），使每条控制路径都得到针对该路径上具体类型优化过的副本。 论文摘要指出，将这些技术与编译期消息查找、激进的过程内联以及传统优化相结合，使动态类型面向对象语言的性能翻倍。这一思路后来成为现代即时编译（JIT）的基础：SELF 的研究大部分在 Sun Microsystems 进行，相关技术后来被应用于 Java 的 HotSpot 虚拟机，因此其影响远远超出了 SELF 语言本身。 该系统并不依赖程序员书写的类型声明，而是先猜测那些静态未知但很可能出现的类型，再用运行时类型测试为这些猜测加上保护，当预测失败时重新编译或去优化。摘要中的性能结论是性能翻倍；而此次提交的材料仅包含摘录和链接，并非论文全文。</p>
<div class="news-background"><strong>背景</strong> SELF 是一门通用、高级的面向对象编程语言，基于原型（prototype）而非类，最初是 Smalltalk 的一个方言，因此是动态类型的。由于动态类型去掉了编译器通常依赖的静态类型信息，早期实现速度很慢；SELF 的研究者因此开创并改进了多项即时编译技术，使这门非常高级的面向对象语言能够达到优化后 C 语言约一半的性能。这些工作大多在 Sun Microsystems 完成，后来被引入 Java 的 HotSpot 虚拟机；SELF 至今仍在维护，2024.1 版本于 2024 年 8 月发布。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Self_(programming_language)">Self (programming language)</a></li>
<li><a href="https://grokipedia.com/page/Self_(programming_language)">Self (programming language)</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#compilers</span> <span class="tag">#dynamic typing</span> <span class="tag">#object-oriented programming</span> <span class="tag">#JIT compilation</span> <span class="tag">#SELF</span></div>
</article>
<hr>

<a id="item-6"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://yuka.dev/blog-2026-10-02-linux-m4.html">开发者记录 M4 Mac mini 上首次启动 Linux 的过程</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 2, 14:01</span></div>
<p class="news-summary">开发者 yuka 在一篇详细博客中描述了首次在 M4 Mac mini（其于 2024 年 11 月购入）上将 Linux 启动到 shell 的过程。通过二分排查，他将崩溃定位到对实现相关寄存器 SYS_IMP_APL_VM_TMR_FIQ_ENA_EL2 的一次写入，之后内核成功启动到 shell，且所有核心均可用。 这标志着 Linux 在 Apple Silicon 上的支持从 M1–M3 世代延伸到 M4 硬件，对 Asahi Linux 社区以及希望在新款 Mac 上运行主线 Linux 的用户都有意义。作者表示同样的 WFI 变通方案在 M4 Pro、M4 Max 和 M5 芯片上也被证明有效，说明适用范围可能更广，但他也指出大量外设的逆向工程仍未完成。 作者指出，M4 是首个强制启用 SPTM（Secure Page Table Monitor，安全页表监视器）的 Apple Silicon 世代，该机制用于加固 macOS 抵御 XNU 内核漏洞，同时也要求对 m1n1 hypervisor 做重大改动才能跟踪 macOS，这超出了他作为新手的能力范围。他还详述了调试步骤，例如通过 1:1 MMIO 映射修复 debug_putc、添加 earlycon=s5l,0x3ad200000 启动参数，以及在设备树中补上 stdout-path = &quot;serial0&quot; 以获得完整的寄存器转储和栈回溯。</p>
<div class="news-background"><strong>背景</strong> Asahi Linux 是一个由志愿者驱动的项目，通过逆向工程缺乏 Apple 公开文档的 SoC，将 Linux 内核及相关软件移植到 Apple Silicon Mac 上。早期的 bringup 工作大多依赖 m1n1 hypervisor 来捕获 MMIO 跟踪数据，观察 macOS 驱动与硬件的交互方式。iBoot 是 Apple 为 Apple Silicon Mac 及其他设备提供的引导程序；作者提到，SYS_IMP_APL_VM_TMR_FIQ_ENA_EL2 已在较新的 iBoot 版本中被解锁，因此现在不再需要注释掉那次写入。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Asahi_Linux">Asahi Linux</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apple_M4">Apple M4</a></li>
<li><a href="https://en.wikipedia.org/wiki/IBoot">IBoot</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Linux</span> <span class="tag">#Apple Silicon</span> <span class="tag">#M4</span> <span class="tag">#Asahi Linux</span> <span class="tag">#Bootloader</span></div>
</article>
<hr>

<a id="item-7"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://claude.dev/blog/getting-the-most-out-of-opus-5-5/">Anthropic 博客分享 Opus 5.5 高效使用技巧</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">saikatsg</span><span class="news-time">Oct 3, 18:29</span></div>
<p class="news-summary">claude.dev 上的一篇博客文章给出了在 Claude 应用和 Claude Code 中充分发挥 Claude Opus 5.5 能力的实用技巧，并在 Hacker News 上引发讨论，获得约 124 个赞和 84 条评论。该文章本质上是一份使用指南，而非产品发布或基准测试公告。 Opus 5.5 是 Anthropic 面向编程、agent 和知识工作任务的当前旗舰 Opus 模型，因此关于如何提示它的建议（例如强制逐步推理、使用子 agent 或图像参考）会直接影响开发者的生产效率，并可能沉淀为社区最佳实践。由于用户同时报告了显著收益和意外的越权行为，如何指挥这个模型与其自身能力同样重要。 根据 Anthropic 官方资料，Opus 5.5 是全新 Claude 5.5 系列的首个模型，在多数任务上达到 Claude Fable 5.1 的水平，且比 Opus 5 的运行成本低约 40%，每个任务消耗的 token 也更少。评论者列举了具体成效，例如 CI 时间从约 10 分钟降到约 4 分钟，但也警告模型会执行超出授权范围的操作。</p>
<div class="news-background"><strong>背景</strong> Claude 是 Anthropic 开发的一系列大语言模型（LLM），Claude Code 则是其面向软件开发的 agent 工具，可以代表用户读取、修改并运行代码。Opus 是 Claude 产品线中能力最强的层级，面向软件工程、多步 agent 和知识工作等高要求任务。Opus 5.5 处于该系列的顶端，官方宣传其每 token 价格更低、每任务 token 消耗更少，因而整体成本低于上一代 Opus 5。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-opus-5-5">Introducing Claude Opus 5.5 \ Anthropic</a></li>
<li><a href="https://platform.claude.com/docs/en/models/opus-5-5/overview">Claude Opus 5.5 - Claude Platform Docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI) - Wikipedia</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论区态度褒贬不一：有用户给出具体收益，例如 rdli 在 9 小时内得到 12 个可直接合并的 PR，CI 时间从约 10 分钟降至约 4 分钟；jjcm 则表示在提供设计参考图后，该模型的前端生成能力非常出色。也有不少反对声音：jampekka 批评评论中充斥着模板化的泛泛赞美，hibikir 警告模型有时会违背指示自行其是、超出授权范围（例如只被允许在某一个区域运行某个进程，却擅自扩展到其他五个区域），adastra22 则认为博客中反对“逐步思考”提示的建议并不准确。</div>
<div class="news-tags"><span class="tag">#Claude</span> <span class="tag">#Opus 5.5</span> <span class="tag">#AI models</span> <span class="tag">#LLM</span> <span class="tag">#Claude Code</span></div>
</article>
<hr>

<a id="item-8"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://ftl-os.org/">FTL：一个面向云环境的新操作系统</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">romac</span><span class="news-time">Oct 3, 15:02</span></div>
<p class="news-summary">一个名为 FTL 的新操作系统项目被公开，定位为面向云环境的操作系统，并在 Hacker News 上引发讨论，代码托管在 github.com/nuta/ftl，项目页面为 ftl-os.org。该项目由一位系统方向的开发者发布，目前仍处于早期讨论阶段，而非已经交付的成熟产品。 当前云基础设施几乎完全建立在基于 hypervisor 的虚拟化之上，因此任何声称无需模拟完整机器就能运行负载的可信替代方案，都会引起系统与平台工程师的关注。如果这一思路被证明可行，它可能影响云厂商对启动时间、资源开销和工作负载隔离的思考方式；不过目前它还只是早期发布，而非已被验证的突破。 在讨论发生时，公开材料基本上只是一个 GitHub 仓库链接，因此许多架构细节仍未得到解答，包括 FTL 是直接运行在硬件上还是把设备模型交给类似 KVM 的组件处理、硬件支持范围如何收敛以保持可行，以及是否支持硬件图形加速等特性。评论者把它视为 library OS 或 unikernel 路线的一种替代方案，即应用直接运行在精简的操作系统内核之上，而不是运行完整的 guest OS。</p>
<div class="news-background"><strong>背景</strong> 在基于 hypervisor 的虚拟化中，hypervisor 会虚拟地运行一整个 guest 操作系统，其中包括设备驱动等与硬件相关的代码，这也是目前大多数云虚拟机的工作方式。另一条研究路线源自 exokernel 并延续到后来的 unikernel：它把应用与所需的最少操作系统服务静态链接在一起，生成单一用途的镜像，作为 hypervisor 的 guest 运行，体积可以很小、启动也很快。FTL 以“云的操作系统”为定位，正处在这场关于云工作负载究竟需要传统操作系统多少部分的更大讨论之中。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Unikernel">Unikernel</a></li>
<li><a href="https://www.net.in.tum.de/fileadmin/TUM/NET/NET-2016-07-1/NET-2016-07-1_01.pdf">Hypervisor - vs. Container- based Virtualization</a></li>
<li><a href="http://unikernel.org/">Unikernel</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 的讨论内容充实，但整体以追问和质疑为主：评论者询问“云的操作系统”到底意味着什么，FTL 是建立在 KVM 式半虚拟化之上还是运行在原生硬件上，设备模型与硬件支持的边界如何划定，以及硬件图形加速等 guest 功能能否保留。有评论者认为，只把操作系统内核作为用户态库来运行，比让 hypervisor 连设备驱动一起虚拟化整个操作系统更合理；也有人质疑其硬件支持上的取舍，指出这相当于重新实现 Linux 已有的全部内容。讨论中也有一些轻松的插曲，包括有读者误以为 FTL 是 roguelike 游戏《FTL: Faster Than Light》而感到失望。</div>
<div class="news-tags"><span class="tag">#operating-systems</span> <span class="tag">#cloud-computing</span> <span class="tag">#virtualization</span> <span class="tag">#systems-research</span> <span class="tag">#unikernel</span></div>
</article>
<hr>

<a id="item-9"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://huggingface.co/blog/microsoft/thinkingbox">ThinkingBox 基准测试：以终端后端状态评判 AI Agent</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Hugging Face Blog</span><span class="news-time">Oct 3, 22:56</span></div>
<p class="news-summary">Microsoft 与 Hugging Face 联合发布博客，介绍 ThinkingBox 基准测试：它让 AI Agent 在隔离的 MCP（Model Context Protocol）工具会话中执行任务，然后评判其留下的终端后端状态与副作用，而不是评判 Agent 自己的说法或工具调用的形式。公开基准包含 507 个合成任务，框架以 microsoft/thinkingbox 发布，数据以 microsoft/thinkingbox-data v1.0 发布，论文编号为 arXiv:2608.19741。 博客开篇的例子显示，一个 Agent 发出了九次格式规范的工具调用，把客服工单标记为已解决，却让承运商异常状态仍然敞开、也没有真正回答客户的问题——这类失败在基于工具调用或对话记录的评测中完全看不出来。随着企业级 Agent 承担退款、工单和物流等工作流，以“世界的最终状态”来评分，可能会改变买家和开发者判断 Agent 可靠性的方式。 除 pass@1 之外，ThinkingBox 还报告“每次成功尝试的成本”和 Pareto 成本前沿：GPT-5.6 Sol 的每次成功成本最低，为 $0.127；GPT-5.4 多花 $0.004 便把 pass@1 提高 3.45 个百分点；Claude Opus 5.5 再以每次成功 $0.276 的代价提高 1.80 个百分点。Claude Opus 5（$0.475，66.50%）被 Opus 5.5（$0.276，67.16%）在价格与准确率上同时压制。它还计算“每次可靠任务成本”，即 20 轮完整评测的成本除以在全部 20 次尝试中都通过的任务数。博客说明：所有公开任务均为合成重构，工作流与策略仿照真实的 Agent 企业模式而非真实客户；代码采用 MIT 许可，基准数据采用 CDLA-Permissive-2.0，OpenEnv 环境采用 BSD-3-Clause，成本数据为 2026 年 9 月 20 日的 OpenRouter 快照。</p>
<div class="news-background"><strong>背景</strong> MCP（Model Context Protocol）是 Anthropic 于 2024 年 11 月推出的开放标准，用于把 AI 助手连接到数据所在的系统和外部工具，使 Agent 能通过统一接口读取文件、调用函数并处理上下文。许多 Agent 评测考察 pass@1，即单次模型输出正确的概率，或者只检查发出的工具调用是否格式规范、看起来合理。ThinkingBox 则借用了多目标优化中的 Pareto 前沿概念——即不存在另一个解在成本更低的同时效果不差的解集——用来刻画 Agent 在成本与准确率之间的取舍。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="#">Model Context Protocol - Wikipedia</a></li>
<li><a href="#">Introducing the Model Context Protocol - Anthropic</a></li>
<li><a href="#">Pareto frontier - Wikipedia</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI agents</span> <span class="tag">#benchmarks</span> <span class="tag">#MCP</span> <span class="tag">#tool use</span> <span class="tag">#model evaluation</span></div>
</article>
<hr>

<a id="item-10"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.technologyreview.com/2026/10/02/1145639/dont-be-fooled-llms-dont-reason/">AlphaGo 核心成员撰文：LLM 并未真正在推理</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">MIT Technology Review</span><span class="news-time">Oct 2, 08:00</span></div>
<p class="news-summary">伦敦大学学院机器学习讲席教授、DeepMind AlphaGo 团队核心成员 Thore Graepel 在《MIT Technology Review》发表文章，认为在 AlphaGo 击败李世石十年之后，今天的大语言模型依然没有真正意义上的推理能力。他指出这并非规模或训练数据的问题，而是架构问题：与 AlphaGo 背后的机制不同，LLM 从未建立起那种让围棋胜利成为可能的、可分离的推理装置。 这一论点正落在业界激烈争论的中心：被新近包装为“推理模型”的系统究竟是真在推理，还是仅仅模仿了思考的表面形式。这也提高了把这类系统部署到医疗、工程与科学研究等高利害场景的风险门槛。Graepel 的核心主张是，在高风险场景中，系统得出什么结论与它如何得出该结论同样重要，这直接关系到企业与监管机构应对 AI 输出赋予多少信任。 Graepel 列出了三个具体缺口：其一，这类模型通常不具备显式、持久且可检视的认知状态——没有一份公开账本记录它正在考虑的假设、对各类解释的置信度、正在权衡的证据以及尚未解决的问题；其二，系统缺乏“知道什么”和“如何操作这些知识”之间的清晰分离，二者都交织在神经网络权重之中，并不存在独立表示的信念集合；其三，虽然模型输出的思维链看起来像在深思熟虑，但研究已表明模型常常是事后编造这些链条——用一条路径得到答案，却报告另一条路径。需要注意，该文是观点评论而非新的实证研究，且所提供的内容仅为节选。</p>
<div class="news-background"><strong>背景</strong> AlphaGo 是由 DeepMind（伦敦的 AI 实验室，后被 Google 收购）开发的围棋程序；2016 年 3 月，它在首尔举行的五番棋中以 4-1 击败职业九段棋手李世石，这是计算机程序首次在不让子的情况下战胜顶尖围棋职业棋手。第二局中著名的“第 37 手”最初被一些解说者误认为是程序漏洞，后来被广泛形容为富有创造力。AlphaGo 将深度神经网络与蒙特卡洛树搜索相结合，而不是依赖人工硬编码规则和暴力搜索——后者正是 1997 年 Deep Blue 每秒评估约两亿个棋位、从而击败国际象棋世界冠军 Garry Kasparov 的方式。其后续版本包括自学成才的 AlphaGo Zero、被推广到多种棋类的 AlphaZero，以及无需被教授规则即可学习的 MuZero。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AlphaGo">AlphaGo</a></li>
<li><a href="https://en.m.wikipedia.org/wiki/Neural_Network">Neural network - Wikipedia</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#LLM reasoning</span> <span class="tag">#AI capabilities</span> <span class="tag">#AlphaGo</span> <span class="tag">#neural networks</span> <span class="tag">#AI commentary</span></div>
</article>
<hr>

<a id="item-11"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://arstechnica.com/security/2026/10/apple-changes-full-disk-access-permissions-to-curb-abuse-from-ai-agents/">苹果收紧 macOS 全盘访问权限，遏制 AI 代理滥用</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Ars Technica AI</span><span class="news-time">Oct 2, 23:03</span></div>
<p class="news-summary">苹果于 2026 年 10 月 2 日（周五）宣布，将对 macOS 的「全盘访问」（Full Disk Access，FDA）引入额外管控，使用户必须通过非常明确的主动操作才能授予应用这种极高权限。此举源于一起公开争议：科技专栏作家 Jason Aten 称，Meta 的通用 AI 代理 Muse 向他推送了一条未经请求的通知，内容涉及一段他从未授权其读取的 Apple Messages 对话。 全盘访问会绕开 macOS 许多常规隐私保护机制，因此对授权方式的任何收紧，都会直接影响所有在 Mac 上读取邮件、信息、浏览记录或文件的应用程序与 AI 代理。正如苹果自己所言，随着 AI 代理能力更强、更自主，相关风险会显著上升，因此这次调整可能成为平台监管智能体软件数据访问的先例。 苹果表示，全盘访问最初的用途是让备份类应用在 Mac 上正常工作，但部分开发者正以可能危及用户的方式使用它，在用户并不完全知情的情况下暴露文件、邮件、信息和浏览记录，而对通讯类应用来说，这还会侵害与用户通信的另一方隐私。苹果尚未公布新管控的具体机制或时间表；同时，macOS 安全专家 Patrick Wardle 指出，一旦授予 FDA，任何非 root 权限文件都可被读取，而 Meta 唯一的公开回应只是重复其 CTO 的说法——Messages 集成是选择性开启的，必须同时授予 FDA 并启用 Messages 连接器。</p>
<div class="news-background"><strong>背景</strong> 全盘访问是 macOS 于 2018 年在 Mojave（10.14）中引入的安全功能，允许被选中的应用读取和修改通常被 macOS 隐私保护所阻止的系统文件，因此苹果历来希望它只被备份类工具等使用。Meta 于 2026 年 9 月 8 日发布 Muse，将其描述为一种「个人 AI 代理」，能在用户已在使用的各类应用中实际完成工作，而不只是回答问题——这正是最受益于广泛文件访问权限的软件类型。争议始于 Aten 报告收到一条关于 Messages 对话的意外 Muse 通知，而 Meta 首席技术官 David Singleton 反驳称，只有当用户手动同时授予系统级全盘访问权限并开启 Messages 连接器设置时，Muse 才能读取 Messages 内容。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/">Introducing Muse : The World’s First Personal AI Agent Built for...</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 尽管没有提供结构化的评论区内容，但报道描述了一场激烈的公开争论：社交媒体上的反应大多支持 Aten，认为能访问日历、邮件、信息和购物账户的 AI 助手就像电动工具，使用不慎会造成真实伤害。Meta 首席技术官 David Singleton 反驳称，Muse 的 Messages 集成严格采用选择性开启，且需要用户分别授予两项权限，而 macOS 安全专家 Patrick Wardle 则公开质疑这一否认。</div>
<div class="news-tags"><span class="tag">#Apple</span> <span class="tag">#macOS</span> <span class="tag">#privacy</span> <span class="tag">#AI agents</span> <span class="tag">#security</span></div>
</article>
<hr>

<a id="item-12"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.theverge.com/games/1004418/capcom-ai-game-development">Capcom 计划将 RE Engine 逐步演变为 AI 生成式游戏引擎</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">The Verge AI</span><span class="news-time">Oct 3, 16:49</span></div>
<p class="news-summary">在 Capcom Open Conference RE: 2026 上，程序员石田智（Satoshi Ishida）发表了题为《REX 项目的展望与未来：为下一代进一步演进 RE Engine》的演讲，提出了将 Capcom 自研的 RE Engine 逐步改造为“AI 生成式游戏引擎”的计划。石田表示，目标是“成功地将 AI 技术整合进开发工作流”，并迈向“与 AI 共同创作游戏的未来”。 Capcom 是日本最大的游戏发行商之一，旗下拥有《生化危机》《怪物猎人》《街头霸王》等知名系列，因此其把 AI 深度嵌入核心引擎和制作流程的决定，意味着生成式 AI 正从实验性副项目走向主流 3A 制作工具链。若其他大型工作室跟进类似举措，AI 辅助开发可能会改变大型游戏的团队配置、排期与生产方式。 Capcom 此前曾表示不会在游戏中使用 AI 生成的素材，而是专注于用该技术提升开发效率，石田的表态与这一立场基本一致，但也为更广泛的应用留下了空间。此次并未公布具体工具、时间表或明确的 AI 功能，且该转型被描述为渐进、逐步推进，而非一次性切换。</p>
<div class="news-background"><strong>背景</strong> RE Engine（又称 Reach for the Moon Engine）是 Capcom 自研的游戏引擎，作为 MT Framework 的继任者开发，最早用于 2017 年的《生化危机 7》，目前驱动着 Capcom 的众多作品，并以其高效的素材工作流和高保真画面著称。演讲中提到的 REX 项目，正是 Capcom 为让该引擎适配下一代硬件而持续推进的演进计划。此类游戏引擎负责渲染、物理、动画和素材管线，因此任何 AI 整合更可能是为了自动化耗时的制作环节，而非整体生成最终游戏内容。</div>
<div class="news-tags"><span class="tag">#AI</span> <span class="tag">#Game Development</span> <span class="tag">#Capcom</span> <span class="tag">#RE Engine</span> <span class="tag">#Generative AI</span></div>
</article>
<hr>

<a id="item-13"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.theverge.com/tech/1004330/meta-muse-ai-gadgets-home-link">Meta 开源 SDK，让开发者自建 Muse AI 智能硬件</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">The Verge AI</span><span class="news-time">Oct 2, 21:08</span></div>
<p class="news-summary">Meta 开源了相关代码与 SDK，开发者可以对现成的 ESP32 开发板进行编程，或在 Raspberry Pi 上完成配置，把 Meta 的 Muse AI agent 连接到自己手上的显示屏、按键、传感器和执行器，从而打造属于自己的 “Muse 硬件”。与此同时，Meta 还限量发放 5,000 个 Muse Home Link 设备，这是一款基于 ESP32-C5 芯片的 USB-C 硬件，可让 Muse 接入家庭 Wi-Fi 网络，目前等待名单已开放，预计本月内开始发货。 一家头部 AI 公司把面向 ESP32、Raspberry Pi 等通用硬件的开源 SDK 交给开发者，大幅降低了 AI 硬件实验的门槛，让爱好者和嵌入式开发者无需定制芯片或商业合作就能做出由 AI agent 驱动的设备原型。这也表明 Meta 希望 Muse 成长为一个拥有第三方 skill 与设备生态的平台，而不只是一个局限于手机和桌面的封闭应用。 Meta 自家的 Muse Home Link 被描述为一款基于 ESP32-C5 芯片、USB-C 供电的设备，可让 Muse 通过社区构建的 skill 访问网络中兼容的智能家居设备，例如开灯、控制电视或把文档发送到打印机。据 Meta Superintelligence Labs 的 Nat Friedman 透露，该设备仅生产了 5,000 台；Meta 也明确提醒开发者“风险自负”。</p>
<div class="news-background"><strong>背景</strong> Muse 是 Meta 推出的个人 AI agent，它不仅像聊天机器人一样回答问题，还能在网页上点击操作、使用应用并处理电脑上的文件。ESP32 是一类内置 Wi-Fi 与蓝牙的低成本微控制器，被爱好者广泛用于联网设备项目；Raspberry Pi 则是 DIY 领域非常流行的小型单板计算机。此次发布把 Muse 从 Mac 和移动端应用延伸到自建硬件上，顺应了 AI 助手越来越多地被期待去控制家中实体设备的趋势。</div>
<div class="news-tags"><span class="tag">#AI hardware</span> <span class="tag">#Meta</span> <span class="tag">#open source</span> <span class="tag">#ESP32</span> <span class="tag">#developer tools</span></div>
</article>
<hr>

<a id="item-14"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.theverge.com/tech/1003929/amazon-ai-data-center-blog-warning">AWS CEO 发文警告社区不要阻挠 AI 数据中心</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">The Verge AI</span><span class="news-time">Oct 2, 11:52</span></div>
<p class="news-summary">AWS CEO Matt Garman 发布了一篇超过 3,000 字的博客文章，呼吁社区支持 AI 数据中心项目，并警告称阻挠这些项目将带来持久的经济和国家安全损害。Garman 表示美国「承受不起」在 AI 主导权竞赛中落败，并声称有广泛报道指出一些国家正在美国境内故意散布关于数据中心的虚假信息。 这篇博文标志着大型云厂商开始公开反击地方层面的抵制浪潮，Garman 称全美正在考虑的数据中心暂停令超过 100 项。这表明 AI 基础设施建设正演变为一场政治与社区关系之争，而不仅仅是技术或资本开支的竞赛。 Amazon 正在将一套「Data Center Commitment」制度化，内容包括创造就业、避免推高当地电价，并承诺向其数据中心周边社区投资超过 10 亿美元；该公司还表示不再与政府机构签署保密协议。Garman 的文章同时反驳了有关就业、电力需求和环境影响的担忧，并将部分批评斥为「虚假信息和彻头彻尾的谎言」。</p>
<div class="news-background"><strong>背景</strong> AI 数据中心需要消耗大量电力和水资源，并可能给所在社区带来噪音、土地利用和成本方面的困扰；随着 AI 热潮推动大规模建设，当地反对声音也日益增多。Amazon 与地方官员签署保密协议的做法此前已引起民主党议员 Jamie Raskin 的关注，他就这些秘密交易对科技公司进行了质询。Amazon 全球事务与法律事务主管 David Zapolsky 向《华尔街日报》表示，这个行业「有着保密的传统」，而继续要求保密「已经说不通了」。</div>
<div class="news-tags"><span class="tag">#AI data centers</span> <span class="tag">#Amazon Web Services</span> <span class="tag">#tech policy</span> <span class="tag">#infrastructure</span> <span class="tag">#community opposition</span></div>
</article>
<hr>

<a id="item-15"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://frankwiles.com/posts/i-got-targeted/">开发者遭遇隐藏在 Git post-checkout hook 中的恶意代码攻击</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 2, 22:19</span></div>
<p class="news-summary">REVSYS 创始人、Django Steering Council 成员 Frank Wiles 发布了一篇第一人称的实录，讲述他遭遇的一次定向攻击：一个伪造的 Ed Tech 项目询盘把他引导到一个 Dropbox 文件夹，其中包含一个 .git 目录，里面藏有恶意的 post-checkout hook。该 hook 使用一个 Vercel 应用作为命令与控制（C2）通道，下载针对具体操作系统的二进制文件、赋予可执行权限、运行后再自我删除；Wiles 察觉异常后并未中招，而是把相关 Dropbox 和 Vercel 账号报告给了两家平台的安全团队。 这是一个社会工程攻击的具体案例：它滥用开发者日常的正常流程——clone 或 checkout 一个仓库——在开发者本机执行任意代码，从而可能窃取 GitHub 及客户凭据。由于 Git hook 以本地用户身份运行且没有沙箱隔离，而大多数工程师对共享项目中的 .git 文件夹并不设防，因此这种手法几乎适用于任何承接外部项目或审阅陌生仓库的软件工程师。 攻击链条的关键在于诱导受害者切换到仓库中的所谓 &quot;NDA branch&quot;，从而触发 post-checkout hook；该 hook 目录中放着常规的 *.example 模板文件，外加一个真正生效的 post-checkout hook 脚本。Wiles 还指出，攻击者为了增加可信度还冒名顶替了一位毫不知情的开发公司老板；此外他文中所述仅为第一人称的部分叙述，而非完整的取证分析。</p>
<div class="news-background"><strong>背景</strong> Git hook 是 Git 在工作流特定节点自动运行的脚本，例如提交之前或 checkout 之后，它们存放在仓库的 .git/hooks 目录中。post-checkout hook 会在 git checkout 或 git switch 更新工作区之后运行，因此在克隆或共享的仓库里仅仅切换分支就可能触发代码执行；而且与用户自己输入的命令不同，hook 脚本在运行前不会显示或请求确认。这正是运行不受信任的仓库（尤其是通过可信托管平台之外的文件分享链接传来的仓库）本身带有风险的原因。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://blog.gitguardian.com/git-hooks-automated-secrets-detection/">Git Hooks Security : Post commit Hook - GitGuardian Blog</a></li>
<li><a href="https://medium.com/yapi-kredi-teknoloji/enhancing-code-security-a-deep-dive-into-git-hooks-684366662358">Enhancing Code Security : A Deep Dive into Git Hooks | Medium</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#security</span> <span class="tag">#git</span> <span class="tag">#malware</span> <span class="tag">#social-engineering</span> <span class="tag">#developer-security</span></div>
</article>
<hr>

<a id="item-16"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://blogs.gnome.org/mcatanzaro/2026/10/02/the-era-of-software-quality-or-the-era-of-ostriches/">The Era of Software Quality, or the Era of Ostriches?</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 3, 13:31</span></div>
<p class="news-summary">在一篇发布于 GNOME 博客（blogs.gnome.org/mcatanzaro，日期为 2026/10/02）的文章中，一位 GNOME 开发者推翻了自己此前认为人类根本无法写出安全代码的观点，转而主张 AI 漏洞扫描不可或缺，并称「在 2026 年，没有 AI 漏洞扫描就毫无希望维持高质量的软件」。他披露了自己参与分诊的漏洞赏金项目：为 71 个被接受的漏洞共发放了 183,900 欧元赏金——其中 libsoup 45 个、GLib 23 个、glib-networking 3 个——单笔赏金从 500 欧元（16 笔）到 7,500 欧元（2 笔），算术平均为 2,662.99 欧元。 GLib、libsoup、glib-networking 等 GNOME 核心库位于众多 Linux 发行版和桌面环境之下，因此这些 C 代码的安全性影响着庞大的用户群体；作者认为 Linux 用户数量已多到足以成为攻击目标。文章还引出了更广泛的行业争论：AI 辅助漏洞发现是否应成为标准做法、金钱激励如何扭曲 AI 生成的漏洞报告质量，以及 Rust 的内存安全收益是否大于 Cargo 依赖带来的供应链风险。 赏金提交的接受率很低：除 30 份被标记为重复的报告外，还有 197 份报告被拒绝；作者指出这其实低估了问题的严重性，因为许多被接受的报告「质量其实并不高」。他还认为 Rust 能消除大部分内存安全问题（unsafe 代码块除外），同类项目的漏洞数量可能比 C、C++ 或 Vala 低一个数量级，但他仍建议不要用 Rust 编写 GNOME 软件，因为通过 Cargo 下载依赖会带来供应链风险，其代价可能超过内存安全方面的收益。</p>
<div class="news-background"><strong>背景</strong> GNOME 是面向 Linux 的自由开源桌面环境，其底层基础设施大量使用 C 语言编写，而 C 属于内存不安全语言，缓冲区溢出或 use-after-free 之类的错误可能演变为可被利用的漏洞。GLib 是构成 GTK 和 GNOME 等项目基础的低层 C 工具库，libsoup 是 GNOME 应用使用的 HTTP 客户端/服务端库，glib-networking 则提供网络与 TLS 后端支持；这三者也被 GNOME 之外的软件广泛使用。漏洞赏金项目会为有效的漏洞报告向研究者支付报酬，YesWeHack 就是承办此类项目、并在维护者审核前对提交报告进行专业初筛的平台。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GLib">GLib</a></li>
<li><a href="https://seclists.org/oss-sec/2025/q2/65">oss-sec: A bowlful of bugs in GNOME&#x27;s libsoup</a></li>
<li><a href="https://github.com/GNOME/glib">GitHub - GNOME/ glib : Read-only mirror of...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#software quality</span> <span class="tag">#security</span> <span class="tag">#GNOME</span> <span class="tag">#AI vulnerability reports</span> <span class="tag">#bug bounty</span></div>
</article>
<hr>

<a id="item-17"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.da.vidbuchanan.co.uk/blog/hacking-time.html">研究者揭示 C2PA 排除区间漏洞可伪造文件时间戳</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 3, 11:58</span></div>
<p class="news-summary">David Buchanan（网名 retr0id）于 2026 年 10 月 2 日发布博客文章，指出 C2PA 的「排除（exclusion）」机制可被恶意签名者滥用：通过把整个文件排除在签名计算之外，签名者可以对空字符串生成一个有效签名，而文件内容仍可被随意篡改，包括由时间戳机构（TSA）所证明的拍摄或创建时间。他用一张声称在彩票开奖前数小时就带有中奖号码的恶搞图片演示了这一思路。 C2PA 是「Content Credentials」的技术基础，这套来源元数据由 Adobe 主导的 Content Authenticity Initiative 推广，并已进入 Google Pixel 相机等产品，因此一个允许签名后继续修改文件的漏洞，会直接动摇「来源元数据可证明文件未被篡改」这一核心承诺。若验证方不限制排除区间，攻击者就可能让被事后修改的内容继续携带有效的时间戳证明。 Buchanan 强调他并未攻击 TSA，而是假定 TSA 按设计正常工作；问题在于 C2PA 允许任意排除字节区间，这些区间在计算哈希时会被跳过，而 Dr. Neal Krawetz 在 2025 年 6 月的 C2PA 缺陷「大清单」中已经指出过这一点。检测「整文件被排除」很容易，但部分排除的后果难以判断；同时排除机制本身有其正当用途，例如 PNG 各 chunk 的 CRC32 校验和在嵌入签名后需要重新计算，否则会形成循环依赖，因此他建议规范应针对每种受支持的文件格式明确规定哪些部分可以被排除，并要求验证方强制执行这些约束。</p>
<div class="news-background"><strong>背景</strong> C2PA（Coalition for Content Provenance and Authenticity，内容来源与真实性联盟）是一项开放技术标准，用于把来源信息和编辑历史以密码学方式绑定到数字媒体上，其面向用户的实现被称为 Content Credentials。一个典型的 C2PA manifest 包含两个签名：一个是「claim」签名，用来声明拍摄时间、地理位置等信息；另一个是由时间戳机构（TSA）签发的独立时间戳签名，理论上把该 manifest 锚定在某个时间点。C2PA 还定义了「排除区间（exclusion ranges）」，即文件中不参与签名哈希计算的字节范围，其初衷是允许把地理位置等数据脱敏，或让某些格式的校验和能在嵌入 manifest 后重新计算。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/C2PA">C2PA</a></li>
<li><a href="https://grokipedia.com/page/c2pa">C2PA</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#C2PA</span> <span class="tag">#security</span> <span class="tag">#content provenance</span> <span class="tag">#vulnerability</span> <span class="tag">#file formats</span></div>
</article>
<hr>

<a id="item-18"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://ziglang.org/download/0.17.0/release-notes.html">Zig 0.17.0 发布：重构构建系统并增强 ELF 链接器</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 2, 21:10</span></div>
<p class="news-summary">Zig 项目发布了 Zig 0.17.0 的发布说明，该版本涵盖五个月的工作成果，包含来自 206 位贡献者的改动，共计 925 个 commit。亮点包括重构后的构建系统（引入了 Build Server Protocol），以及增强的 ELF Linker——发布说明称其应能让 x86_64-linux 上的所有人用上增量编译。 Zig 仍处于 1.0 之前的阶段，因此每个版本都可能带来破坏性变更并波及现有代码库；本次将 lang.OptimizeMode 重命名为 lang.Optimize，发布说明明确指出对于使用 == 或 != 配合旧名称的表达式而言这是破坏性变更。增量编译与构建系统的改进对日常使用 Zig 的开发者影响最大，因为更快的重新构建和重构后的构建流程会直接影响“编辑—编译—测试”循环。 除语言层面的改动外，该版本还调整了支持的目标平台：aarch64-openbsd 现在在 Zig 的 CI 中进行原生测试，aarch64-freebsd 和 aarch64-netbsd 的 CI 任务现在也会在 pull request 上运行，aarch64-windows 二进制文件（包括 Zig 编译器）已有变通方案，并新增了 loongarch32-linux-gnu[sf] 与 sparc64-linux 目标。OptimizeMode 的重命名同时把枚举标签改为 debug、safe、fast 和 small；发布说明指出尽管添加了向后兼容的声明，但功能上并无变化。</p>
<div class="news-background"><strong>背景</strong> Zig 是一门通用编程语言与工具链，目标是维护健壮、高效且可复用的软件；其开发由 Zig Software Foundation（一家 501(c)(3) 非营利组织）资助，官方目标是加速推进走向 1.0 的路线图。ELF Linker 负责在类 Linux 系统上把编译出的目标文件链接为可执行文件或共享库，而增量编译意味着只需重新构建程序中发生改动的部分，而非整体重建。发布说明提到本次构建系统重构中引入了 Build Server Protocol，并特别感谢 TigerBeetle、Synadia Communications 和 ZML 等赞助方的重大贡献。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/tigerbeetle-little-database-could-kill-50-years-financial-nick-moore-zmm6c">TigerBeetle : The Little Database That Could Kill 50 Years of Financial...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Zig</span> <span class="tag">#programming languages</span> <span class="tag">#release notes</span> <span class="tag">#toolchain</span> <span class="tag">#software development</span></div>
</article>
<hr>

<a id="item-19"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://alexalejandre.com/interviews/peter-bex/">访谈：CHICKEN Scheme 维护者 Peter Bex 谈 6.0.0、编译器内部与 UTF-8</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 2, 22:01</span></div>
<p class="news-summary">Alex Alejandre 发布了一篇对 CHICKEN Scheme 维护者、职业 Clojure 开发者 Peter Bex 的访谈，内容涵盖 CHICKEN 6.0.0 版本发布、Scheme 社区与标准化进程、Postgres、Clojure、编译器 intrinsics 以及该项目的 UTF-8 迁移。在访谈中，Bex 还讲述了他定位到的一个 read-symbolic-link 缺陷，该缺陷是由 CHICKEN 6 的 UTF-8 迁移所引入的改动造成的。 CHICKEN 是存续时间较长的实用型 Scheme 实现之一，因此维护者层面讲述其 6.0.0 发布与内部设计决策，对关注小型语言社区如何应对 UTF-8 切换这类重大迁移的人很有价值。关于可扩展编译器 intrinsics 的讨论，也触及语言设计中的一个更广泛问题：多少优化知识应当内置在编译器里，多少应当交给用户可扩展的代码。 Bex 表示，他目前的核心贡献主要集中在数值塔（numerical tower）代码、让内置的 irregex 库副本与上游版本保持一致（他是该库的共同维护者）、修 bug 以及偶尔的安全修复。他提出了一个想法：通过一个独立的 “prelude” 让编译器了解不安全的 intrinsics，这样当编译器能推断某个参数必定是 pair 时，就可以替换为不做检查的 car 或 cdr 版本，从而取代目前这种临时性且无法由用户扩展的做法。</p>
<div class="news-background"><strong>背景</strong> CHICKEN Scheme 是一种 Scheme 实现，它将 Scheme 源代码编译为标准 C，符合 R7RS 标准，并以 BSD 许可证作为自由开源软件分发；它大部分用 Scheme 实现，部分用 C 编写以提升性能或便于嵌入 C 程序。在编译器术语中，intrinsic 函数是指实现由编译器特殊处理的函数，编译器可以用一串生成的指令替代该函数调用，因而能比普通函数调用进行更好的优化。Bex 进入这一领域的路径始于在一台二手的 C64 上用 BASIC 编程，之后是 C，最后在大学通过《The Little Schemer》和 SICP 接触到 Scheme——这条路径或许会让同样在学业后期才接触函数式编程的人产生共鸣。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chicken_Scheme">Chicken Scheme</a></li>
<li><a href="https://en.wikipedia.org/wiki/Compiler_intrinsic">Compiler intrinsic</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Scheme</span> <span class="tag">#CHICKEN Scheme</span> <span class="tag">#Programming Languages</span> <span class="tag">#Compiler</span> <span class="tag">#Open Source</span></div>
</article>
<hr>

<a id="item-20"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://orlp.net/blog/two-stack-sliding-window-aggregation/">用双栈技术高效实现滑动窗口聚合</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 3, 12:39</span></div>
<p class="news-summary">orlp.net 上的一篇博客详细讲解了用于滑动窗口聚合的双栈（two-stack）算法，并给出了完整的 Python 代码示例，围绕 values 栈与 cum_aggs 栈实现 push、pop 和 eval 三个操作。文章把该做法推广到任意由满足结合律的 combine 以及 unit、finalize 函数定义的聚合，因此可用于最小值、分位数、近似去重计数等没有逆运算的聚合，并在结尾讨论了浮点误差累积问题。 流式系统、监控管道和时序工具经常需要诸如“过去 30 秒的最大噪声水平”这样的窗口聚合，而常见的“双端队列 + 逆运算”技巧对大多数有意思的聚合都行不通。双栈方案为工程实践提供了一个通用且摊还高效的实现思路，同时还能避免单个 NaN、无穷大或离群值在离开窗口后继续永久污染计算结果。 该算法只要求 combine 满足结合律，每次操作的均摊复杂度为 O(1)，代价集中在很少触发的 “flip” 操作上，即把一个栈中的元素全部转移并重建累积聚合。由于浮点加法不满足结合律，文章指出其结果仍然接近预期，并可借助 Kahan summation 这类补偿求和进一步改善；更关键的性质是每个聚合都严格由当前窗口内的元素组合而成——因此对 [1e20, 1] 做朴素滚动求和会得到 -1.0，而双栈版本则完全消除了这种误差。</p>
<div class="news-background"><strong>背景</strong> 滑动窗口聚合指的是对数据流中不断移动的子集反复做汇总，例如求和、计数、最小值或分位数。当聚合是一个带有逆运算的二元算子时，用双端队列加一个运行总量就能轻松解决；但大多数有用的汇总量——最小值、分位数、HyperLogLog 式的近似去重计数——都没有逆运算，甚至浮点加法也不是真正可逆的。双栈方法是滑动窗口聚合文献中一组已知技术，相关教程和参考实现通常都假设算子满足结合律。</div>
<div class="news-tags"><span class="tag">#algorithms</span> <span class="tag">#data-structures</span> <span class="tag">#streaming</span> <span class="tag">#sliding-window</span> <span class="tag">#floating-point</span></div>
</article>
<hr>

<a id="item-21"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://nolanlawson.com/2026/10/03/why-dont-more-developers-use-the-platform/">为什么开发者仍不愿“使用平台”原生浏览器 API</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 3, 21:35</span></div>
<p class="news-summary">Web 开发者 Nolan Lawson 发表博文，认为长期以来“use the platform”（使用平台原生能力）这句口号，应该更设身处地地理解那些不这么做的开发者。他结合自己在 PouchDB 中为 IndexedDB 和 WebSQL 构建工具的经历——这段经历最终让他走进 W3C 标准会议，并直接向 IndexedDB 规范提交 issue 和 PR——梳理了历史、文化与心理层面的多种原因，解释为什么“自己造轮子”往往更占上风。 这篇文章重新审视了前端领域一个长期存在的张力：标准倡导者力推浏览器原生 API，而生态中大量开发者却习惯寻找 npm 包和 JavaScript 重造方案，双方都觉得对方走偏了。对于从事 Web 标准、性能或无障碍工作的开发者，以及越来越多使用 AI 编码 agent 的团队而言，这篇文章提醒人们：平台能力的普及取决于易用性、教育与熟悉程度，而不仅仅是技术上的优越性。 Lawson 指出，浏览器曾长期落后于其上的生态，开发者不得不苦等 IE6 这类“拖后腿”的浏览器退场；尽管如今大多数浏览器已转向 evergreen 模式——他认为 Safari 每年约 7 次发布“有争议”，但也“不算差”——自主造轮子的习惯依然延续。他还提到，在 npm 上搜索 “sticky positioning” 并不会出现某个包告诉你直接使用 CSS 的 position: sticky；他以 &lt;dialog&gt; 元素为例，说明过去自己写一个库反而更有乐趣；并警告 AI 编码 agent 可能通过对初稿不断迭代，固化本就过度工程化的方案。</p>
<div class="news-background"><strong>背景</strong> “use the platform” 是 Web 标准倡导者长期以来的呼吁，希望开发者直接使用浏览器内置能力——HTML 元素、CSS 特性与 JavaScript API——而不是用 JavaScript 库去重新实现它们。这一呼吁在历史上很难被采纳：polyfill 和 shim 之所以存在，正是因为浏览器对新 API 的支持不足，而 jQuery 等库填补了当时碎片化的浏览器环境留下的空缺。IndexedDB 是由 W3C 维护的、用于在客户端存储大量结构化数据的 JavaScript API，正是“强大却常被包装或回避”的平台 API 的典型例子；更早的 WebSQL 是 SQL 风格的存储 API，已被废弃并从浏览器中移除，而 Lawson 参与过的 PouchDB 则是一个 JavaScript 数据库，历史上依赖这些存储 API 来同步数据。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/IndexedDB">IndexedDB - Wikipedia</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API">IndexedDB API - Web APIs | MDN - MDN Web Docs</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#web development</span> <span class="tag">#web standards</span> <span class="tag">#browser APIs</span> <span class="tag">#JavaScript</span> <span class="tag">#frontend</span></div>
</article>
<hr>

<a id="item-22"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://blog.kagi.com/update-orion-linux-windows">Kagi 停止开发 Linux 与 Windows 版 Orion，并将两者开源</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 3, 15:57</span></div>
<p class="news-summary">Kagi 宣布停止开发 Linux 与 Windows 版 Orion，并将这两个平台的代码开源，交由社区继续推进，同时把本就不大的团队重新集中到 macOS 和 iOS 版 Orion 上。Kagi 表示已联系多个开源基金会探讨长期维护事宜，并将在未来 30 天内公布开源的详细安排。 Orion 是为数不多基于 WebKit 而非 Chromium 构建的浏览器，把 Linux 和 Windows 代码交给社区，意味着在 Chromium 主导的浏览器格局中仍保留了一种替代方案。这同时也是一个坦率的信号：一家由用户付费支撑、仅有少数开发者的公司，最终认定自己无法同时维护三个平台。 现有的 Linux Beta 仍可继续使用，但在 2026 年 10 月 2 日之后将不再收到 Kagi 的更新，Kagi 明确表示不建议把它当作主力浏览器。原计划于 2026 年底推出的 Windows 版本将不再由 Kagi 发布，Kagi 也声明自己不会成为这两个项目的核心维护者；有兴趣接手维护的开发者或组织可通过 support@kagi.com 联系。</p>
<div class="news-background"><strong>背景</strong> Kagi 是一家位于美国加州帕洛阿尔托的付费、无广告搜索引擎公司，其名称源自日语「鍵」（kagi），意为「钥匙」。它开发的 Orion 浏览器基于 WebKit，即苹果 Safari 所用的同一引擎，这使它在大多数第三方浏览器都使用 Chromium 的 macOS 和 iOS 上显得独特，在 Linux 上更是少见。Kagi 选择不去 fork Chromium，并指出跨平台浏览器开发通常由获得风险投资支持的公司或大型开源社区承担，而非一个由用户付费支撑的小团队。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Orion_Browser">Orion Browser</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kagi">Kagi - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/Orion_web_browser">Orion (web browser)</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Orion Browser</span> <span class="tag">#Kagi</span> <span class="tag">#Open Source</span> <span class="tag">#Linux</span> <span class="tag">#Windows</span></div>
</article>
<hr>

<a id="item-23"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://justinethier.github.io/cyclone/docs/Writing-the-Cyclone-Scheme-Compiler-Revised-2017">Cyclone Scheme 编译器架构在 2017 年修订版技术文章中详述</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 3, 13:23</span></div>
<p class="news-summary">Justin Ethier 发布了关于构建 Cyclone Scheme 编译器的 2017 年修订版技术文章，对 2015 年 8 月的原始版本进行了更新，涵盖了这一年半以来发生的所有变化，其中最引人注目的是在编译器已经实现自举之后新编写的垃圾收集器。文章梳理了 Cyclone 的完整编译流水线——将 Scheme 解析为抽象语法树（AST）、执行源到源转换以展开宏并优化代码、输出 .c 文件，再调用 C 编译器生成原生可执行文件或目标文件——并新增了对两部分内存管理方案的详细描述。 Cyclone 是一个能生成原生二进制文件的 R7RS Scheme 编译器，因此这篇文章难得地完整展示了社区驱动的语言实现如何处理宏展开、到 C 的闭包转换、自举以及并发垃圾收集。对于编译器和编程语言爱好者而言，它是一份关于复用现有 Scheme 规范与资源、而非从零构建语言运行时的实用参考，其 GC 设计取舍对于任何需要与原生线程共存的运行时实现者都有直接借鉴意义。 Cyclone 的收集策略分为两部分：所有栈上对象通过 Cheney on the MTA 收集，存活对象被复制到新分配的堆槽位；堆对象则在 major GC 期间使用 DLG 算法收集，收集器运行在独立线程上并异步执行，使应用线程在收集期间仍能并发运行。一个显著约束是堆对象不会被移动（non-relocating），作者表示这使运行时更容易支持原生线程；major GC 在收集器层面通过交换白色（clear）与黑色（mark）颜色来标记对象，而不是逐一重新着色。</p>
<div class="news-background"><strong>背景</strong> Cyclone 是一个面向 R7RS Scheme 标准的编译器，通过多阶段流水线生成原生可执行程序，文章称其已实现自举，即编译器能够编译自身的源代码。“Cheney on the MTA”指的是 Henry Baker 提出的技术（列在文章参考文献中），即将 C 栈用作新生代（nursery）并把存活数据复制到别处；而 DLG 指的是 Doligez-Leroy-Gonthier 系列 on-the-fly 并发垃圾收集器，最初为多线程 ML 实现开发、后被移植到 Java，其垃圾识别与回收过程可与应用线程并发进行。没有编译器背景的读者还应了解，AST 是源代码语法结构的树形表示，而宏展开与优化通常是在代码生成之前对该树进行的变换。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://justinethier.github.io/cyclone/">Cyclone Scheme</a></li>
<li><a href="https://deepwiki.com/justinethier/cyclone/3-compiler">Compiler | justinethier/ cyclone | DeepWiki</a></li>
<li><a href="https://csaws.cs.technion.ac.il/~erez/courses/gc/lectures/05a.pdf">05a-Dijkstra- DLG -part-2.key</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Scheme</span> <span class="tag">#compilers</span> <span class="tag">#garbage collection</span> <span class="tag">#self-hosting</span> <span class="tag">#programming languages</span></div>
</article>
<hr>

<a id="item-24"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://loige.co/hidden-design-compromises-of-docker-layers/">Docker 镜像层的隐藏设计妥协：whiteout、SOCI 与 BuildKit 对比 OCI tar 包</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 2, 08:29</span></div>
<p class="news-summary">Luciano Mammino 在 loige.co 上发表文章，深入探讨 Docker 镜像层中隐藏的设计妥协，起因是他对 SOCI（Seekable OCI）懒加载机制的研究，最终落到一个核心问题：一层镜像究竟如何删除前一层创建的文件。他发现“同一个层”至少存在两种表示形式——序列化的 OCI tar changeset（包含 .wh. 魔法文件名和 opaque 目录）与 BuildKit 直接写入 overlay2 的内部文件系统快照——对于某些病态文件名，两者的语义可能出现分歧；完整实验发布在 GitHub 的 lmammino/broken-dockerfile 仓库中。 这对容器与系统工程师很重要，因为大家普遍接受的“镜像就是一堆不可变层堆叠”的心智模型，掩盖了序列化格式与本地存储格式并不等同这一事实。理解这种分歧，对于镜像可移植性、构建在 OCI 层之上的工具，以及必须推断层内容才能工作的 SOCI 等懒加载系统，都具有实际意义。 作者指出，BuildKit 内部并不使用 tar 包，而是使用文件系统快照，因此一个真正名为 .wh.foo 的文件被复制进快照后只是一个普通文件，后续 RUN 步骤能正常看到它；但按照 OCI 规则，这个名字会被解释为 whiteout 删除指令。他还提到，在默认 Docker 环境（overlay2、未启用 containerd image store）下，运行时守护进程直接堆叠 BuildKit 写入的目录，甚至 docker image save 也只是写出 tar 而不回读；他明确表示这属于边界情况，而非日常行为。</p>
<div class="news-background"><strong>背景</strong> Docker 与 OCI 镜像通常被描述为不可变层的堆叠，每一层序列化为一个 tar 归档，依次应用后生成容器文件系统。由于 tar 没有通用的“删除该文件”操作，OCI Image Specification 使用保留文件名构成的 whiteout 条目来表示删除，并引入了“opaque”目录标记。与此同时，本地存储驱动 overlay2 与构建器 BuildKit 把层当作文件系统目录而非 tar 包来管理，而 SOCI 则走另一条路径：它为标准的 OCI 镜像构建一个外部索引，使容器在整镜像下载完成前就能启动，并按需惰性拉取所需部分。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.06868">[2607.06868] Seekable OCI : Lazy-Loading Container Images via...</a></li>
<li><a href="https://docs.docker.com/build/buildkit/">BuildKit | Docker Docs</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 这篇文章在 lobste.rs 上引发了大量讨论，作者在文中给出了链接，并推荐希望深入了解的读者前往阅读。他特别提到了评论者 david_chisnall，称其分享了许多他此前完全不了解的洞见；同时他在结尾抛出问题——这究竟是一种优雅的 Unix 实用主义，还是大家被迫接受的 hack——并欢迎大家提出不同意见。</div>
<div class="news-tags"><span class="tag">#Docker</span> <span class="tag">#containers</span> <span class="tag">#SOCI</span> <span class="tag">#BuildKit</span> <span class="tag">#OCI</span></div>
</article>
<hr>