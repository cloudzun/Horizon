---
layout: default
title: "Horizon 每日速递：2026-10-15"
date: 2026-10-15
lang: zh
---

> 📅 2026-10-15 · 从 94 条资讯中精选出 25 条重要内容

---

1. [Meta 发布 816B 开放权重 MoE 模型 Muse Spark Open](#item-1) <span class="score-badge score-mid">8.0</span>
2. [Citizen Lab：定向广告被用作零点击间谍软件的传播管道](#item-2) <span class="score-badge score-mid">8.0</span>
3. [Libreboot 26\.10 “Ominous Olive” 发布：完整支持 UEFI，引入 233 款 Chromebook](#item-3) <span class="score-badge score-mid">8.0</span>
4. [Anthropic 向投资者披露第三季度营收达 168 亿美元，IPO 前增长近五成](#item-4) <span class="score-badge score-mid">8.0</span>
5. [Meta 发布 Muse Spark Open：前沿开源权重多模态 MoE 模型](#item-5) <span class="score-badge score-mid">8.0</span>
6. [Ai2 发布 HiRO\-ACEv2：以 1/300 的成本实现 3 公里极端天气模拟](#item-6) <span class="score-badge score-mid">8.0</span>
7. [“冷冻”一年的猪肾被成功复温并恢复功能](#item-7) <span class="score-badge score-mid">8.0</span>
8. [约 700 家法国超市的制冷系统被黑，导致食物腐坏并引发火灾](#item-8) <span class="score-badge score-mid">8.0</span>
9. [Meta 与 Apple 联手，让 Muse Spark Open 在 Mac 上本地运行](#item-9) <span class="score-badge score-mid">8.0</span>
10. [Jake Archibald 实测 JPEG XL 与 AVIF 的 Web 适用性](#item-10) <span class="score-badge score-mid">8.0</span>
11. [CGPM 第 5 号决议确定 2027 年启用连续 UTC](#item-11) <span class="score-badge score-mid">8.0</span>
12. [Goodfire 称&quot;神经网络是干净的&quot;,引发 Hacker News 激烈争论](#item-12) <span class="score-badge score-mid">7.0</span>
13. [西蒙斯基金会联手 Anthropic 与 OpenAI 投入 1500 万美元应对 AI 时代的数学研究](#item-13) <span class="score-badge score-mid">7.0</span>
14. [C\+\+26 Contracts 特性介绍引发 HN 关于其实用价值的争论](#item-14) <span class="score-badge score-mid">7.0</span>
15. [Derek Thompson 谈数学家的 AI 焦虑，引发 Hacker News 热议](#item-15) <span class="score-badge score-mid">7.0</span>
16. [IBM 与 Hugging Face 发布 Granite Switch 4\.1：单一端点整合对话、决策与语音能力](#item-16) <span class="score-badge score-mid">7.0</span>
17. [Apertus 1\.5 发布：新增多模态、思考模式与 4 倍长上下文](#item-17) <span class="score-badge score-mid">7.0</span>
18. [Hugging Face 为 FLUX\.3 Image Klein 提供 Diffusers 支持](#item-18) <span class="score-badge score-mid">7.0</span>
19. [Anthropic 警告小型 AI 模型可能催生可自我复制的 IoT 恶意软件](#item-19) <span class="score-badge score-mid">7.0</span>
20. [The Verge：名人 AI 深度伪造内容在 Instagram 泛滥，Meta 披露规则形同虚设](#item-20) <span class="score-badge score-mid">7.0</span>
21. [Benn Jordan 做客 Decoder 谈 Flock、ALPR 监控与隐私反弹](#item-21) <span class="score-badge score-mid">7.0</span>
22. [博客文章称 Anthropic 的 Scion 版本控制系统大量借鉴 Meta 的 Mononoke](#item-22) <span class="score-badge score-mid">7.0</span>
23. [Forgejo v17\.0 发布，带来 Actions 作业摘要与破坏性链接变更](#item-23) <span class="score-badge score-mid">7.0</span>
24. [一位粉丝深入解析 Gleam 的 case 穷尽性检查实现](#item-24) <span class="score-badge score-mid">7.0</span>
25. [Enroute 推出基于对象存储的 Rust Git 服务器，宣称每秒 7,600\+ 并发 push](#item-25) <span class="score-badge score-mid">7.0</span>

---

<a id="item-1"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://research.meta.ai/blog/muse-spark-open">Meta 发布 816B 开放权重 MoE 模型 Muse Spark Open</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">bigwheels</span><span class="news-time">Oct 15, 17:47</span></div>
<p class="news-summary">Meta 发布了 Muse Spark Open：一个总参数 816B、激活参数 42B 的稀疏 MoE 推理模型，上下文窗口达 1M token，并以 Muse Model License 在 Hugging Face 上开放权重，同时提供了面向多种运行时（runtime）的部署工具。根据模型卡，该模型由 Meta Superintelligence Labs 于 2026 年 10 月发布，原生多模态，面向编码与 agentic 任务。 这让 Meta 在竞争激烈的 agentic 编码模型梯队中再添一个超大规模开放权重模型，开发者需要在能力、许可条款与硬件成本之间做权衡。由于 Muse Spark Open 在发布首日便获得众多常用 runner 与推理栈的支持，它很可能被广泛试用，并与其他开放权重模型系列直接对比，而不只是停留在实验层面。 根据模型卡与社区讨论，该模型采用 Muse Model License，而非 Apache/MIT 等标准许可；有评论者指出其中含有一条 Model-as-a-Service 条款，即当相关实体通过 API 等方式向第三方提供该模型输出、且合计毛收入超过某一门槛（引文被截断）时受到限制。Hugging Face 模型卡还提到，开放权重版本额外进行了安全后训练；vLLM 的 recipe 则描述其支持原生图像与视频感知，并提供可选的 DSpark 草稿模型用于投机解码（speculative decoding）。</p>
<div class="news-background"><strong>背景</strong> 开放权重（open-weight）模型指参数可以下载并自行运行，但并不等同于开源：像 Meta 的 Llama 社区许可或 Gemma 条款，往往会附加商业使用条件、可接受使用政策或收入门槛，而 Apache-2.0 与 MIT 则没有这些限制。此类 MoE（专家混合）架构在保留极大规模总参数量的同时，每个 token 只激活其中一部分——这里是 816B 中的 42B——因此相较同规模稠密模型可显著降低推理成本。自最初的 Llama 系列以来，Meta 一直是开放权重潮流的重要推手，其模型也成为许多开发者与下游微调的默认基座。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B">meta-models/Muse-Spark-Open-816B-A42B · Hugging Face</a></li>
<li><a href="https://recipes.vllm.ai/meta-models/Muse-Spark-Open-816B-A42B">meta-models/Muse-Spark-Open-816B-A42B | vLLM Recipes</a></li>
<li><a href="https://intuitionlabs.ai/articles/open-weight-ai-model-licenses">Open-Weight AI Model Licenses: Commercial Use Rules Explained</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 讨论主要围绕许可与竞争力两方面展开。有评论者引用 Artificial Analysis 的数据，称该模型表现不及某些竞品，并认为 Meta 在开放权重领域还需追赶，同时批评该评测平台只在最高推理档位进行对比，这对大规模生产场景并不实用；另有评论者查阅许可后指出，Model-as-a-Service 收入条款正是它难以算作真正开放权重的原因。也有人称赞其 runner 支持范围广（Unsloth、MLX），还有评论者认为这次发布印证了 Meta 长期以来开放模型的策略正在见效——它让 Meta 的模型成为开发者默认遵循的标准。</div>
<div class="news-tags"><span class="tag">#meta</span> <span class="tag">#open-weight-models</span> <span class="tag">#llm</span> <span class="tag">#model-licensing</span> <span class="tag">#hugging-face</span></div>
</article>
<hr>

<a id="item-2"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/">Citizen Lab：定向广告被用作零点击间谍软件的传播管道</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">jcomp</span><span class="news-time">Oct 15, 10:43</span></div>
<p class="news-summary">Citizen Lab 发布研究（由 The Guardian 和 The Verge 报道），指称一家名为 Discover Tech 的以色列公司滥用定向广告基础设施，在无需用户任何交互的情况下向选定设备投递雇佣兵间谍软件，即所谓的&quot;零点击&quot;方式。该新闻标题将这一行动称为&quot;AdFection&quot;，并引发大量社区讨论，质疑其技术机制以及责任归属。 如果这些发现成立，那么日常的广告投放就可能变成隐蔽的监控渠道，并可能牵连到原本无意参与间谍活动的广告交易平台、发布商和数据经纪商。这也让责任认定变得更复杂，因为 adtech 供应链高度碎片化，并不存在一个可以被追责的单一&quot;广告提供商&quot;。 根据讨论中的批评意见，该报告较详细地描述了分发与命令控制（C&amp;C）环节，但对恶意软件究竟如何实现零点击激活这一核心问题着墨含糊。评论者还强调，adtech 生态包含众多不同的中介角色——需求方平台、供给方平台、交易平台、广告网络与发布商——因此把责任归咎于某一方并不容易。</p>
<div class="news-background"><strong>背景</strong> Citizen Lab 是多伦多大学蒙克国际事务与公共政策学院（Munk School of Global Affairs and Public Policy）下属的跨学科研究实验室，由 Ronald Deibert 于 2001 年创立；它研究信息控制问题，并多次为调查针对记者、政治人物与人权倡导者的间谍软件的记者提供技术支持。&quot;零点击&quot;间谍软件无需用户任何操作（例如点击链接或屏幕）即可感染设备，通常通过利用软件漏洞实现。&quot;雇佣兵间谍软件&quot;（mercenary spyware）指出售给政府及其他客户的商业入侵工具；Apple 曾就此类攻击向用户发送威胁通知，据报覆盖 150 多个国家的用户，说明该问题已相当普遍。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Citizen_Lab">Citizen Lab</a></li>
<li><a href="https://www.zdnet.com/article/apple-warns-of-mercenary-spyware-attacks-against-iphone-users-should-you-be-worried/">Apple sends new warning about mercenary spyware attacks... | ZDNET</a></li>
<li><a href="https://vajiramandravi.com/current-affairs/zero-click-spyware/">Zero Click Spyware , Meaning, Working, Threats, Challenges</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 一位在 adtech 行业工作约 13 年的工程师认为，该报告在&quot;零点击&quot;方面&quot;高度耸动&quot;，且对实际激活机制语焉不详，同时反驳了在庞大生态中存在单一可追责&quot;广告提供商&quot;的说法。其他评论者则普遍对在线广告行业持敌意态度，质疑以色列网络安全公司能否被视为独立于国家，并贴出了 Citizen Lab 原始报告的直接链接。</div>
<div class="news-tags"><span class="tag">#cybersecurity</span> <span class="tag">#spyware</span> <span class="tag">#adtech</span> <span class="tag">#privacy</span> <span class="tag">#zero-click</span></div>
</article>
<hr>

<a id="item-3"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://libreboot.org/news/libreboot2610.html">Libreboot 26.10 “Ominous Olive” 发布：完整支持 UEFI，引入 233 款 Chromebook</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 15, 14:03</span></div>
<p class="news-summary">2026 年 10 月 15 日，Leah Rowe 发布了代号 “Ominous Olive” 的 Libreboot 26.10：该版本将 EDK2 设为默认启动 payload，通过 MrChromebox EDK2 payload 提供完整的 UEFI 支持，兼容范围从此前的 Linux/BSD 扩展到 Microsoft Windows。此次发布还从 MrChromebox coreboot 发行版引入了全部 233 款目前受支持的 Chromebook，并在 lbmk 中新增 AGENTS.md 文件以确立强硬的反对 AI 政策，作者称这是本版本最重要的改动。 引入完整的 UEFI/EDK2 payload 与 233 款 Chromebook，使 Libreboot 可运行的设备数量大幅增加，让项目不再局限于少数老旧 ThinkPad，而向更主流、更易获取的硬件扩展，这对希望替换专有固件的用户意义重大。同时，其明确的反对 AI 贡献政策也很可能受到其他正在讨论如何处理 LLM 生成代码的开源项目密切关注。 Libreboot 26.10 以 EDK2 作为默认 payload，并将 GRUB 和 SeaBIOS 作为 EFI 构建保留在 flash 中以提供向后兼容；CSMWrap（EDK2 内的 SeaBIOS CSM）存在已知限制，会在启动时占满一整个 CPU 核心，因此四核机器在 Linux 中会显示为三核，官方建议用户直接使用 ESP 以原生 UEFI 模式启动。本次 Chromebook 支持仅提供源码（不提供二进制，必须自行编译），其中只有 Baytrail（“Kip”）经过测试，而 FreeBSD 的 BIOS 模式引导程序不建议用于新安装，因为 coreboot 的 framebuffer 模式无法切回文本模式。</p>
<div class="news-background"><strong>背景</strong> Libreboot 是自由开源引导固件，用于在受支持的 Intel/AMD 与 ARM64 硬件上替换专有的 BIOS/UEFI 固件；它负责初始化 CPU、内存控制器等核心部件，使操作系统能够启动，其基础是 coreboot，并使用 payload（负责最后阶段把控制权交给操作系统的程序），例如 GRUB、SeaBIOS 或 EDK2。EDK2（TianoCore EDK II）是 Intel 提供的 UEFI 规范参考实现，也是事实上的通用 UEFI 标准实现，而 MrChromebox 是一个支持 Chromebook 的 coreboot 发行版。更新日志还涉及 me_cleaner（一个通过修改 Intel 管理引擎固件镜像来削弱其与系统交互能力的脚本）以及 bios_extract（用于从传统 BIOS 镜像中提取子模块的工具）等工具。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/EDK2">EDK2</a></li>
<li><a href="https://openhub.net/p/bios_extract">The bios_extract Open Source Project on Open Hub How to Extract a BIOS Image from an Exe coreboot/bios_extract - Codeberg.org Universal Bios Extractor Tool - Google Groups</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者普遍认为 UEFI/EDK2 集成与 Chromebook 支持才是真正的重点，有用户称其为“巨大的进步”，因为它成倍扩大了受支持设备数量，也让未来纳入新设备更容易，尽管作者本人把 AI 政策列为最重要的改动。也有人称赞对 LLM 辅助贡献的严格限制令人耳目一新；同时，一位参与相关 Heads 项目的开发者提到，他自己的已合并 pull request 通过引入 MrChromebox 的代码实现了首个 ChromeOS 移植，目前还有两款设备正在推进。</div>
<div class="news-tags"><span class="tag">#firmware</span> <span class="tag">#UEFI</span> <span class="tag">#open-source</span> <span class="tag">#coreboot</span> <span class="tag">#Chromebook</span></div>
</article>
<hr>

<a id="item-4"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://simonwillison.net/2026/Oct/15/anthropic-tells-investors/">Anthropic 向投资者披露第三季度营收达 168 亿美元，IPO 前增长近五成</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Simon Willison</span><span class="news-time">Oct 15, 13:04</span></div>
<p class="news-summary">据英国《金融时报》援引知情人士的报道，Anthropic 在周三的投资者日活动上向投资者表示，其季度营收增长近 50%，达到 168 亿美元。同一报道还给出了此前的数据：第二季度为 115 亿美元，第一季度约为 48 亿美元；这些披露发生在公司筹备 IPO 的背景下。 这些数字显示企业对前沿 AI 模型的需求仍在快速攀升，而此时 Anthropic 正为上市做准备，其估值可能成为整个 AI 实验室行业的参考基准。此外，蒸馏业务贡献了 5% 至 7% 营收这一细节，也呼应了业界关于“是否可以用竞争对手模型输出进行训练”的持续争论。 《金融时报》报道称，第三季度 Anthropic 每支出 1 美元算力成本可带来 1.70 美元营收，剔除股权激励后的调整后营业利润率为 11%。报道还称，Anthropic 向投资者表示蒸馏业务占其营收的 5% 至 7%，并已在第三季度“大幅”削减这部分业务，同时在这些沟通中似乎不再使用“年化运行率营收”（annualized run-rate revenue）这一口径；上述数据均来自匿名消息人士，而非经审计的财报。</p>
<div class="news-background"><strong>背景</strong> Anthropic 是一家研发 Claude 系列大语言模型的 AI 实验室，与其他前沿实验室一样，它在算力上投入巨大，并通过私募市场筹集了大量资金。季度营收是比“年化运行率营收”更严格的口径，后者只是把近期某个周期的收入乘以 4，容易美化高速增长公司的表现。模型蒸馏通常指训练一个较小的“学生”模型去模仿较大“教师”模型的输出，但在这里该词被用来指竞争对手实验室基于 Anthropic 模型的输出进行训练——Anthropic 已开始限制这种做法，而这类行为会给被蒸馏一方带来大量的 API 调用与支出。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://labelbox.com/guides/model-distillation/">What is Model Distillation ?</a></li>
<li><a href="https://www.geeksforgeeks.org/nlp/what-is-llm-distillation/">What is LLM Distillation? - GeeksforGeeks</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Anthropic</span> <span class="tag">#AI industry</span> <span class="tag">#revenue</span> <span class="tag">#IPO</span> <span class="tag">#model distillation</span></div>
</article>
<hr>

<a id="item-5"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://huggingface.co/blog/meta-muse-spark-open">Meta 发布 Muse Spark Open：前沿开源权重多模态 MoE 模型</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Hugging Face Blog</span><span class="news-time">Oct 15, 00:00</span></div>
<p class="news-summary">Meta 在 Hugging Face Blog 上宣布了 Muse Spark Open，这是一个开放权重的多模态 Mixture-of-Experts 前沿模型，Meta 称其为迄今能力最强的美国开放权重模型；此前发布的 August 推出的轻量稠密模型 Muse Glimmer 属于同一系列。文章给出的规格包括约 816B 总参数、每 token 约 42B 激活参数、每个 MoE 层 256 个专家且每 token 选择 8 个、支持文本/图像/音频/视频输入、上下文窗口最高 100 万 token，并提供 BF16 与 NVFP4 两种 checkpoint（Muse-Spark-Open-816B-A42B 与 Muse-Spark-Open-816B-A42B-NVFP4）。 如果这一说法成立，这将是美国大型实验室在前沿规模上的一次重要开放权重发布，开发者可以自行运行、微调并自托管一个多模态 agentic 编程模型，而不必只能通过 API 访问。这也会进一步激化“开放权重能否比肩领先闭源系统”的争论。 文章称 Muse Spark Open 面向 agentic 编程训练，可读取代码库、编写与调试代码并调用工具，并说明它采用基于 channel 的聊天模板 Harmony（最早由 gpt-oss 引入），示例代码中还带有 reasoning_strength=&quot;high&quot; 选项。浏览器 agent 演示据称只向模型提供此前的动作、system prompt、URL 和截图（不含 DOM 或 HTML），文章还建议使用 BF16 或 NVFP4 checkpoint，以及 llama.cpp 的量化版本；但由于所提供的摘录中没有基准测试数据，其性能声明尚无法独立验证。</p>
<div class="news-background"><strong>背景</strong> Mixture-of-experts（MoE）是一种机器学习技术：它用多个专家网络来划分问题空间，因此模型可以大幅扩展，但每个输入只激活部分参数（这里是每个 token 从 256 个专家中选 8 个），使单 token 计算量远低于总参数量。NVFP4 是一种 4 位浮点量化格式，常用于在 Nvidia 硬件上压缩大模型，以很小的精度损失换取更快的推理速度和更低的内存占用。llama.cpp 是广泛使用的开源推理库，常被称为 Ollama、LM Studio 等本地推理工具事实上的标准核心，其量化版本也是让开放权重模型跑在消费级硬件上的常见途径。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained - Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">Llama.cpp</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#open-weight models</span> <span class="tag">#mixture-of-experts</span> <span class="tag">#multimodal</span> <span class="tag">#Meta</span> <span class="tag">#model release</span></div>
</article>
<hr>

<a id="item-6"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://huggingface.co/blog/allenai/hiro-acev2">Ai2 发布 HiRO-ACEv2：以 1/300 的成本实现 3 公里极端天气模拟</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Hugging Face Blog</span><span class="news-time">Oct 14, 16:12</span></div>
<p class="news-summary">Ai2 发布了 HiRO-ACEv2，这是其高分辨率输出 Ai2 气候模拟器（HiRO-ACE）系统的最新更新；新的降尺度模型 HiROv2 不再只预测降雨，而是可同时预测多个高分辨率变量，并且在还原最强降雨、风力和气压极值方面的能力有所提升。在输入粗化的 X-SHiELD 数据时，它能把目标模拟的高分辨率统计量匹配到 3% 以内，即使是对百万分之一的极端稀有事件也是如此；而整套系统生成全球 3 公里气候数据的成本约为 X-SHiELD 的 1/300。 这一发布让气候与天气研究者能够以灵活且低成本的方式，为十年甚至更长时间的极端事件生成大量高分辨率降雨、风力和气压数据，而这在此前受限于计算代价极高的高分辨率物理模拟。由于只需要单一区域时节省的开销还会更大，这类 emulator 有望让公里级极端事件数据集对更广泛的研究团队变得可行。 HiRO-ACE 由两部分构成：在较粗的 100 公里分辨率上运行的 ACE，以及把粗分辨率输出锐化到 3 公里细节的 HiRO；新版本中也对 ACE 做了调整，在为期 10 年的模拟中，其飓风、平均气候态以及降雨、风力、气压的整体分布都与 X-SHiELD 吻合良好。HiROv2 生成的飓风具有逼真的风眼和雨带，但博客指出风眼周围的风场和气压仍相对更不对称；此外官方还提供了一个网页 demo，可在不运行任何推理的情况下并排比较预生成的 HiROv1、HiROv2 与 X-SHiELD 输出，模型与教程 notebook 也可下载使用。</p>
<div class="news-background"><strong>背景</strong> ACE（Ai2 Climate Emulator）是一系列对完整全球大气模式进行自回归机器学习模拟的模型家族，此前发布的版本约为 2 亿参数，用于模拟 100 公里分辨率的大气模式。相比之下，X-SHiELD 是一个显式模拟风暴及其他小尺度天气的高分辨率全球大气模式，因此运行成本要高得多。HiRO-ACE 于 2026 年早些时候推出，把这两种思路结合起来：用 ACE 模拟粗分辨率气候，再用降尺度模型 HiRO 补充 3 公里的精细结构，而 HiRO-ACEv2 就是该流程的最新更新。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2512.18224">HiRO - ACE : Fast and skillful AI emulation and downscaling trained on...</a></li>
<li><a href="https://allenai.org/blog/hiro-ace">HiRO - ACE : An accessible solution for kilometer-scale climate simulation</a></li>
<li><a href="https://huggingface.co/allenai/HiRO-ACE">allenai/ HiRO - ACE · Hugging Face</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#climate-modeling</span> <span class="tag">#weather-simulation</span> <span class="tag">#AI-for-science</span> <span class="tag">#emulators</span> <span class="tag">#research-release</span></div>
</article>
<hr>

<a id="item-7"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.technologyreview.com/2026/10/15/1146091/pig-kidneys-that-were-frozen-for-a-year-have-been-brought-back-to-life/">“冷冻”一年的猪肾被成功复温并恢复功能</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">MIT Technology Review</span><span class="news-time">Oct 15, 08:43</span></div>
<p class="news-summary">由明尼苏达大学移植外科医生 Erik Finger 共同领导的研究团队报告称，被冷却至 -150 °C、并以玻璃态（vitrified）保存数月的猪肾（其中一颗超过一年）成功复温并恢复功能：在机器上测试并移植回猪体内后，肾脏重新恢复颜色并产生尿液。该研究以预印本形式发布在 bioRxiv 上，尚未经过同行评审。 如果该方法能在人体器官上复现，就可能实现器官的长期“银行式”储存——把供体器官保存从以小时计的竞速，变成可以在数月甚至数年内进行匹配和分配的储备资源，从而有可能减少被丢弃的器官、缓解移植患者的供需短缺。未参与该研究的低温生物学家 Peter Kilbride 称，这是人们多年来屡试屡败后终于取得的突破。 该流程包括：用标准器官保存液冲洗供体肾脏，用约两小时缓慢灌注由多种 cryoprotectants（冷冻保护剂）组成的混合液，再向器官内灌注氧化铁纳米颗粒约七到八分钟，随后用氮气蒸气降温并避免冰晶形成。研究人员承认这些肾脏并不完美，尚未证明它们能够长期维持生命，并计划开展人体肾脏实验，同时寻找毒性更低的冷冻保护剂。</p>
<div class="news-background"><strong>背景</strong> 目前的器官保存依赖冰块冷藏，一颗肾脏只能维持数小时的活性。cryopreservation（低温保存）则希望把器官冷却成无冰晶的玻璃态（vitrification）以实现更长时间储存，但如何均匀且足够快速地复温、避免开裂或冰晶损伤，一直是最难的环节。名为 nanowarming（纳米复温）的技术通过向器官血管内灌注氧化铁纳米颗粒、再用交变磁场加热来解决这一问题，此前已在大鼠肾脏上得到验证。cryoprotectants（冷冻保护剂）则是在降温过程中替代组织内水分、防止冰晶形成的化学试剂。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cryoprotectant">Cryoprotectant</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#cryopreservation</span> <span class="tag">#organ transplantation</span> <span class="tag">#biomedical research</span> <span class="tag">#nanotechnology</span> <span class="tag">#regenerative medicine</span></div>
</article>
<hr>

<a id="item-8"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://arstechnica.com/security/2026/10/fridge-hack-costing-millions-and-sparking-fires-stemmed-from-poor-security/">约 700 家法国超市的制冷系统被黑，导致食物腐坏并引发火灾</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Ars Technica AI</span><span class="news-time">Oct 14, 21:35</span></div>
<p class="news-summary">法国约 700 家超市的联网制冷控制器遭到大规模入侵，导致门店内成批的冰箱和冷柜集体失灵，大量生鲜食品腐坏，部分设备甚至发生电气火灾。攻击者以管理员权限登录控制器后长时间开启除霜模式，使设备温度最高升至 50°C（122°F）。 这是一起大规模的真实 IoT/OT 安全事件，网络攻击直接造成了物理后果——数百家零售门店出现食品损毁、设备损坏乃至起火，而不只是数据泄露。它再次说明，工业控制器上的默认口令和弱口令仍是食品零售及其他关键基础设施中系统性、易被利用的风险。 据报道，此次事件涉及的三款控制器型号——分别由丹麦的 Danfoss，以及美国的 Dixell 及其母公司 Copeland 销售——都存在可让攻击者以管理员权限远程登录的严重漏洞。Danfoss 控制器据称使用一种由公开固件按日期生成的每日轮换凭据，任何分析过代码的人都能推导出同样的口令，而该口令在成百上千家门店的设备上完全相同；Copeland/Dixell 也在近几个月修复了一批类似的严重漏洞。</p>
<div class="news-background"><strong>背景</strong> 超市制冷系统由联网控制器管理，技术人员可借此远程操控整批冰箱和冷柜。除霜循环会刻意将压缩机排出的高温气体导入蒸发器盘管以融化积冰；若系统一直停留在除霜模式，盘管温度可接近压缩机排气温度（约 50°C），足以让食品腐坏并使电气部件过载。在工业控制系统中，默认口令或弱口令是众所周知且屡遭利用的薄弱环节，标准加固指南建议尽可能删除、禁用或重命名此类凭据，并强制使用强口令和账户锁定策略。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.danfoss.com/en-us/industries/food-and-beverage/dcs/cold-rooms/">Walk-in Coolers and Freezers | Find products | Danfoss</a></li>
<li><a href="https://www.copeland.com/en-us/products/refrigeration/commercial-refrigeration/refrigeration-controls">Commercial Refrigeration Controls | Copeland US</a></li>
<li><a href="https://www.beyondtrust.com/blog/entry/securing-ics-scada-systems-privilege-vulnerability-management">Securing ICS and SCADA Systems with Privilege and... | BeyondTrust</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#cybersecurity</span> <span class="tag">#IoT security</span> <span class="tag">#industrial control systems</span> <span class="tag">#critical infrastructure</span> <span class="tag">#vulnerability disclosure</span></div>
</article>
<hr>

<a id="item-9"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.theverge.com/news/1012293/meta-apple-muse-spark-open-ai-model-mlx">Meta 与 Apple 联手，让 Muse Spark Open 在 Mac 上本地运行</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">The Verge AI</span><span class="news-time">Oct 15, 18:15</span></div>
<p class="news-summary">Meta 发布了 Muse Spark Open，这是一个拥有 8160 亿总参数的开放权重、原生多模态模型。Meta 声称它是迄今为止能力最强的美国开放权重模型，也是同类中首个可以借助最新 MLX 框架、在两台 Apple M5 Ultra Mac Studio 上于桌面端运行的模型。模型权重当天即开放下载，Apple 也发布了一篇技术文章，介绍 MLX、Muse Spark Open 以及另外两个开放模型。 这次发布罕见地出现了两家长期竞争对手公开为彼此的工作站台：Meta CEO Mark Zuckerberg 感谢 Apple 的合作，Apple CEO John Ternus 则称赞 Mac Studio 上的端侧 AI 能力。这也表明，在 Apple Silicon 上进行高规格的本地推理，正成为超大规模开放权重模型的一条严肃部署路径——这对希望摆脱云端推理的开发者，以及正把 Mac Studio 推向 AI 工作站定位的 Apple，都具有重要意义。 Meta 称该模型擅长长时程任务、复杂软件工程和多步推理；而桌面端演示需要两台高端 M5 Ultra Mac Studio，这属于相当高的硬件门槛，而非普通笔记本电脑就能胜任的配置。由于能力宣称来自 Meta 自身，且现有摘录提供的独立技术细节有限，这些说法应视为尚未经第三方验证。</p>
<div class="news-background"><strong>背景</strong> MLX 是 Apple 开发的开源机器学习数组框架，于 2023 年 12 月首次发布，专为 Apple Silicon 的统一内存架构优化，使 CPU 与 GPU 可以共享同一份数据，而无需在不同内存池之间复制。所谓开放权重模型，是指训练得到的权重可公开下载，任何人都能在自有硬件上运行、微调或部署，而不必只通过厂商 API 调用。Mac Studio 是 Apple 的紧凑型桌面工作站产品线，本次公告中提到的 M5 Ultra 则指该机型所采用的最高端芯片档位。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/MLX_(machine_learning_framework)">MLX (machine learning framework) - Wikipedia</a></li>
<li><a href="https://telnyx.com/resources/open-weight-models">Open Weight Models What They Are and How to Use Them</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI/ML</span> <span class="tag">#open-weight models</span> <span class="tag">#Apple Silicon</span> <span class="tag">#MLX</span> <span class="tag">#Meta</span></div>
</article>
<hr>

<a id="item-10"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://jakearchibald.com/2026/jpeg-xl-vs-avif/">Jake Archibald 实测 JPEG XL 与 AVIF 的 Web 适用性</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 15, 14:42</span></div>
<p class="news-summary">Jake Archibald 发布了一篇针对 Web 使用场景的详细基准测试，比较 JPEG XL 与 AVIF：对于有损照片，在默认压缩档位下 AVIF 生成的文件通常小 15–25%，在最高档位下差距缩小到 6–20%。他还特别提到较新的 JPEG XL 编码器 jixel，称其在多数情况下比 libjxl 生成更小的文件，但在含复杂透明度的图像上例外。 这篇文章为 Web 与前端性能工程师在照片、截图、插图和透明图像等场景下选择格式提供了基于实测的明确指导，也表明 AVIF 与 JPEG XL 已进入真正正面竞争阶段。作者指出，无论最终哪种格式胜出，更优秀的图像压缩都会让所有用户受益。 质量对比使用 SSIMULACRA2 感知指标进行同质量匹配，作者也提示该指标会把完全透明的像素记为满分，因此在透明度较多的图像上得分容易被抬高。AVIF 在编码时间和内存上也占优：libjxl 默认耗时是 AVIF 默认的 1.2–1.35 倍，内存约为其 2.4–2.7 倍（约 120 MB 对 46 MB）；此外 libjxl 默认对 alpha 通道做无损压缩，jixel 则始终无损编码透明度，使其默认档位下文件大小达到 AVIF 的 1.9–3.1 倍。</p>
<div class="news-background"><strong>背景</strong> JPEG XL 是 2022 年作为 ISO/IEC 18181 标准发布的下一代图像格式，libjxl 是其参考编解码器实现，被众多支持该格式的应用所使用。AVIF 是基于 AV1 编解码器的竞争格式，同样用于处理 AV1 视频本身并不支持的 alpha 通道。SSIMULACRA2 是一种感知图像质量指标，被 JPEG XL、Jpegli、AVIF 等近期图像编码标准采用，其得分与主观视觉质量高度相关。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/libjxl/libjxl">GitHub - libjxl/libjxl: JPEG XL image format reference ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#image-compression</span> <span class="tag">#JPEG XL</span> <span class="tag">#AVIF</span> <span class="tag">#web-performance</span> <span class="tag">#browsers</span></div>
</article>
<hr>

<a id="item-11"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.bipm.org/en/cgpm-2026/resolution-5">CGPM 第 5 号决议确定 2027 年启用连续 UTC</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 15, 20:22</span></div>
<p class="news-summary">第 28 届国际计量大会（CGPM）通过了第 5 号决议《关于确保 UTC 连续性所需技术行动》，决定自 2027 年 5 月 20 日起启用连续 UTC，并将|UT1-UTC|的最大差值定为 3600 秒（1 小时）。这实际上终结了在民用时间中插入闰秒的做法。 交通运输、能源分配、电信和航天等工业用户与国家关键基础设施要求 UTC 保持连续、今后不再需要调整，而决议警告称首次出现的负闰秒将给准备不足的系统带来高度异常风险。该决定直接影响时间同步软件、分布式系统以及所有依赖精确时间同步的运营方。 CCTF 与 IERS 于 2025 年 3 月举办的研讨会估计，负闰秒出现的概率将迅速上升，到 2035 年达到 30%；决议还指出，依赖时间同步的产业为此所需的准备投入估计与应对千年虫（millennium bug）相当，而 IoT、多传感器系统、智能电网和虚拟服务的普及进一步加大了风险。增大的 UT1-UTC 差值将通过无线电通信系统发布至 2035 年，在现有设备无法提前更换的情况下不迟于 2040 年；该决议的官方版本为法文文本。</p>
<div class="news-background"><strong>背景</strong> UTC 由国际计量局（BIPM）产生，其速率与国际原子时（TAI）保持一致，但通过不定期插入闰秒，使其与描述地球自转角度的 UT1 保持在不到一秒的偏差内。自 1972 年以来共插入 27 次闰秒，且全部为正闰秒，因为地球自转总体呈减慢趋势；负闰秒则相反，会跳过一个秒，使 23:59:58 之后直接进入 00:00:00。CGPM 是负责全球计量单位统一性的国际机构，其在 2022 年第 27 届会议上决定在 2035 年或之前提高|UT1-UTC|的上限，并要求 CIPM 为 2026 年第 28 届 CGPM 起草相关决议。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Negative_leap_second">Negative leap second</a></li>
<li><a href="https://en.wikipedia.org/wiki/General_Conference_on_Weights_and_Measures">General Conference on Weights and Measures - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/International_Earth_Rotation_and_Reference_Systems_Service">International Earth Rotation and Reference Systems Service</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#timekeeping</span> <span class="tag">#UTC</span> <span class="tag">#leap-second</span> <span class="tag">#standards</span> <span class="tag">#critical-infrastructure</span></div>
</article>
<hr>

<a id="item-12"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://already-clean.goodfire.com/">Goodfire 称&quot;神经网络是干净的&quot;,引发 Hacker News 激烈争论</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">themgt</span><span class="news-time">Oct 15, 16:04</span></div>
<p class="news-summary">Goodfire 在 already-clean.goodfire.com 发布了一篇题为&quot;Neural networks are clean&quot;的博客文章,并关联了 Goodfire 的 Nick Cammarata 在 X 上的帖子,主张神经网络具有某种&quot;干净的&quot;可解释结构。该文章在 Hacker News 上引发大量讨论,获得 443 分和 163 条评论。 这一主张处于 mechanistic interpretability 的核心地带——该领域的研究者认为,理解模型内部结构是做好对齐的前提,因此&quot;网络本质上是干净的&quot;这一强主张会显著改变该领域对自身目标的表述方式。由于相关结果仍是存有争议而非已被确认,这场讨论也说明可解释性研究的发现往往在证据尚未落定之前就迅速被转化为 AI 对齐的叙事。 文章包含一个位于 already-clean.goodfire.com/microscope/medium.html 的交互式演示,有评论者称其为&quot;第一个我自认为基本看懂了的非平凡神经网络&quot;。批评者则认为这些主张超出了已被证明的范围,并援引早已为人熟知的现象,如特征复杂度递增、Lottery Ticket Hypothesis 以及 Multimodal Gap 的研究(arXiv 2203.02053),指出这些现象与参数过载(parameter overloading)相符,而非支持&quot;干净结构&quot;的说法。</p>
<div class="news-background"><strong>背景</strong> Mechanistic interpretability 是一个新兴领域,试图对训练好的神经网络进行逆向工程,像分析传统软件那样剖析网络,以理解其内部推理过程。Goodfire 是一家位于旧金山的 AI 可解释性研究实验室兼公益公司(public benefit corporation),专注于理解并有意识地设计先进的 AI 系统。本条新闻正是置于这一研究议程之中,而&quot;网络学到的是整洁可分的结构,还是纠缠且过载的结构&quot;这一问题,是该议程中尚未解决的核心争议。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.goodfire.com/research">Latest research - Goodfire</a></li>
<li><a href="https://www.goodfire.com/">Goodfire AI</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 社区情绪呈现两极:有评论者称赞 Cammarata 是&quot;一股自然之力&quot;,并推荐阅读他的发布帖以获取背景;另一位评论者则认为这些主张&quot;似乎超出了实际已被证明的范围&quot;,并援引 Lottery Ticket Hypothesis 和 Multimodal Gap 的研究。还有人把这种语气比作&quot;Anthropic mechinterp 团队在首批大规模 SAE 结果出炉时的热情&quot;,形容其为一种&quot;轻躁狂式的能量&quot;——仿佛关键范式已经找到,剩下的只是扩大规模;此外也有人分享了相关的交互式演示链接和该文章的音频版本。</div>
<div class="news-tags"><span class="tag">#mechanistic-interpretability</span> <span class="tag">#neural-networks</span> <span class="tag">#ai-alignment</span> <span class="tag">#deep-learning</span> <span class="tag">#research-claims</span></div>
</article>
<hr>

<a id="item-13"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.simonsfoundation.org/news/simons-foundation-launches-15m-effort-to-help-mathematicians-navigate-ai-era/">西蒙斯基金会联手 Anthropic 与 OpenAI 投入 1500 万美元应对 AI 时代的数学研究</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">aaraujo002</span><span class="news-time">Oct 15, 14:58</span></div>
<p class="news-summary">西蒙斯基金会宣布与 Anthropic 和 OpenAI 建立合作，三方将共同投入 1500 万美元的资金与资源，由基金会负责管理与发放（包括通过公开征集提案的方式），用于支持工作坊及相关项目，帮助研究者评估新近由 AI 辅助得出的结果、学习使用新工具，并共同确立 AI 使用的规范标准。 这是一次引人注目的“慈善机构＋产业界”合作，把两家前沿 AI 实验室与数学领域的重要私人资助方联系在了一起，可能影响 AI 辅助数学成果的评价、标准化与署名方式。其结果将影响一线数学研究者、数学发表与同行评审的规范，也关系到更宏观的问题：科学共同体究竟是由外部被动接受 AI 工具，还是主动参与其治理。 这笔 1500 万美元是三方共同投入的资金与资源，而非单一来源的资助；Hacker News 上有评论者估算各方约为 500 万美元，并指出其中一部分可能以 token 额度而非现金形式提供。资金发放权掌握在基金会而非两家 AI 实验室手中，且已开放提案征集，因此工作坊、工具建设与标准制定之间的具体配比将取决于最终获批的项目。</p>
<div class="news-background"><strong>背景</strong> 西蒙斯基金会是数学与基础科学研究领域重要的私人慈善资助机构（有评论者引用维基百科称其成立于 1994 年）。近年来，前沿 AI 实验室越来越多地把数学——从竞赛题到形式化定理证明——当作展示模型能力的舞台，Lean 等形式化工具也已进入数学研究的工作链。此次项目被定位为让数学界自行设定评估 AI 辅助成果的规则，而不是被动回应模型开发者单方面给出的宣称。</div>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 上的评论总体偏向质疑：一些人认为这笔钱最终会流向少数已经资金充裕的知名数学家，而非处于职业早期的研究者；另一些人则认为，在把数学发现“掠采”为模型宣传素材之后，两家实验室的出资更像是利己之举，有人把各自约 500 万美元的投入称作部分意义上的“公关洗白”。也有评论者给出务实的应对办法，例如关闭 ChatGPT 和 Claude 中用于改进模型的数据使用设置，并讨论了当前模型在数学推理上的局限。</div>
<div class="news-tags"><span class="tag">#AI in science</span> <span class="tag">#mathematics</span> <span class="tag">#research funding</span> <span class="tag">#AI ethics</span> <span class="tag">#academia-industry partnership</span></div>
</article>
<hr>

<a id="item-14"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.cppstories.com/2026/cpp26_contracts/">C++26 Contracts 特性介绍引发 HN 关于其实用价值的争论</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">ibobev</span><span class="news-time">Oct 15, 13:11</span></div>
<p class="news-summary">cppstories.com 上的一篇新文章介绍了 C++26 Contracts，展示了前置条件（preconditions）和后置条件（postconditions）如何让开发者把约束直接写进函数签名，而不必依赖独立的 cassert 风格检查。文章涵盖了输入检查与结果验证，同时配套的 Hacker News 讨论帖（约 120 分、110 条评论）中，多位资深开发者质疑它相比普通 assert 究竟有多大改进。 Contracts 是 C++26 这一重要语言新版中备受关注的新特性之一，而 C++ 是使用最广泛的系统编程语言之一，因此它的设计会影响极其庞大的既有代码库。这场争论之所以重要，是因为它在检验一个几十年前的构想能否在现代 C++ 中产生实际价值，而不是仅仅再增加一种运行期断言机制，同时也将影响库作者今后如何记录和强制接口约定。 文章从简单的 cassert 示例讲起，再把约束移到函数内部，以此说明 contract assertions 与普通错误处理的区别。讨论中反复出现的一个注意事项是：contract assertions 并不适用于错误处理或输入校验；有评论者指出，只输出「assertion failed」而不打印参与比较的具体数值，往往远不如自定义断言函数有用——后者可以打印出实际的比较值。</p>
<div class="news-background"><strong>背景</strong> 契约式设计（Design by Contract）是由 Eiffel 语言推广的一种方法：例程声明调用方必须满足的前置条件、返回时保证成立的后置条件，以及必须始终成立的不变式。C++ 长期以来缺乏表达这类约束的标准一等机制，开发者通常只能使用 assert 宏、异常或文档注释。C++26 Contracts 是漫长标准化过程的产物，是一个折中设计，而非单一连贯的设计愿景。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.cppstories.com/2026/cpp26_contracts/">C+ + 26 Contracts : Introduction to Preconditions and Postconditions</a></li>
<li><a href="https://ponderwall.com/index.php/2026/04/19/cpp26-contracts-explained/">C+ + 26 Contracts Explained: What They Are and Why They Matter</a></li>
<li><a href="https://en.wikipedia.org/wiki/Design_by_contract">Design by contract - Wikipedia</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 上的讨论整体偏向怀疑：有评论者认为 Contracts 只是制造更多运行期错误，除非能把运行期失败变成编译期错误，否则并不比 assert 更好；曾在 1990 年代于 Zortech C++ 编译器中实现契约、后来又在 D 语言中实现的 Walter Bright 则表示，这个特性「最终被证明并不太有用」。其他人则将其与 Eiffel 的契约式设计相比较，主张使用能打印实际比较值的自定义断言函数，还有评论者分享了多年前为在等待标准化期间给 C/C++ 加入契约而编写的 GCC 插件。</div>
<div class="news-tags"><span class="tag">#C++</span> <span class="tag">#C++26</span> <span class="tag">#contracts</span> <span class="tag">#design-by-contract</span> <span class="tag">#programming-languages</span></div>
</article>
<hr>

<a id="item-15"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.derekthompson.org/p/i-know-why-the-mathematicians-weep">Derek Thompson 谈数学家的 AI 焦虑，引发 Hacker News 热议</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">RickJWagner</span><span class="news-time">Oct 15, 13:44</span></div>
<p class="news-summary">Derek Thompson 发表了题为《I know why the mathematicians weep》的文章，探讨 AI 侵入数学领域为何会让知识工作者产生存在主义式的恐惧；该文在 Hacker News 上引发了约 326 分、529 条评论的热烈讨论。 这篇文章及其引发的讨论把 AI 视为一种文化冲击而非单纯的技术里程碑：当那些赋予地位、声望和生计的技能可以被自动化时，一个人职业身份的整体架构都会受到质疑。 有评论者指出，这篇文章绕过了 Robert Brandom 的“deontic scorekeeping（道义记分）”等哲学框架却未点名；也有人认为更深层的问题在于验证规范的瓦解——AI 生成的内容未经阅读或检验，就被当作已经解决或可信的结论。</p>
<div class="news-background"><strong>背景</strong> 数学长期以来被视为一个靠证明来定论的领域，而公开检验的过程正是该领域确立真理的核心机制。如今大型语言模型可以大规模生成看似合理的数学文本、证明和猜想，这引出一个问题：谁来验证这些输出，以及该领域用于核验成果的社会机制能否跟上。Robert Brandom 的“deontic scorekeeping（道义记分）”是一种意义理论，认为概念依靠参与者之间理由、主张与质疑的社会性往来而得以维系；评论者正是用这一视角来追问 LLM 为何在表面上可行，以及在何处可能存在根本性缺陷。</div>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 的讨论总体上认同文章的框架，但在“究竟在哀悼什么”上存在分歧。有评论者认为，任何能带来地位、声望与生计的技能被商品化，都会让人产生深切的恐惧，因为多年的奋斗在事后看来都变得毫无意义；也有人表示真正的损失是追寻真理的意愿，如今已无人验证或检验；还有人把文章与 Brandom 的道义记分理论联系起来；另有一位评论者以中世纪织工行会的历史性衰落为例，警告历史对被抛下的人并不温柔。</div>
<div class="news-tags"><span class="tag">#AI</span> <span class="tag">#mathematics</span> <span class="tag">#future-of-work</span> <span class="tag">#LLMs</span> <span class="tag">#philosophy</span></div>
</article>
<hr>

<a id="item-16"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://huggingface.co/blog/ibm-granite/granite-switch-4-1">IBM 与 Hugging Face 发布 Granite Switch 4.1：单一端点整合对话、决策与语音能力</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Hugging Face Blog</span><span class="news-time">Oct 15, 20:34</span></div>
<p class="news-summary">IBM 与 Hugging Face 发布了 Granite-Switch-4.1-8B 和 Granite-Switch-4.1-30B，把对话基础模型、新的通用 Decision aLoRA、面向安全决策的专用 Guardian aLoRA，以及 Granite-Speech-5.0-Turbo-CTC 语音识别模型打包进同一个端点。官方称该组合占用的 GPU 显存与单独运行基础模型大致相同，并声称 3B 版 Granite Switch 在 Doom 演示中每秒可做出 60 至 100 次决策，而 Jev 报告的速度为每秒 10 次。 它展示了一条实用的多任务部署路径：在同一个冻结基础模型之上叠加专用适配器，而不是为每个任务单独运行模型，这对 GPU 预算有限、又需要同时提供对话、分类/决策和语音转写的团队很有价值。这也让 IBM 的开源 Granite 体系直接对标 TypeSafe 的 Jev 等闭源 &quot;System One&quot; 决策模型。 这些适配器以缓存高效的 Activated LoRA（aLoRA）形式构建，因此基础模型生成过程中产生的 KV cache 可以被后续基于适配器的决策复用；IBM 还提到其在 vLLM 中针对低秩适配器推理的贡献以及同址部署的 ASR 编码器是速度提升的关键。IBM 表示其专用的 granitelib 适配器在特定分类任务上可以超过通用型决策模型，并声称带四个专用 aLoRA 的 30B 模型在真实五步 RAG 工作流中比 Jev-27B（冻结的 Qwen 基础模型加一个通用决策 LoRA）完成得更快；更多数据将在未来数周公布。</p>
<div class="news-background"><strong>背景</strong> LoRA（Low-Rank Adaptation）是一种只训练少量新增权重矩阵、而非全部参数的微调方法，因此许多任务专用适配器可以共享同一个基础模型。Activated LoRA（aLoRA）对 LoRA 做了修改，只对被调用之后的 token 应用权重调整，因此适合生成循环中的短约束检查和决策调用，并支持基础模型与适配器之间复用 KV cache。Granite 是 IBM 的开源模型系列，Granite Libraries（granitelib）则是可组合进自定义 Granite Switch 模型的专用适配器仓库。相比之下，Jev 是 TypeSafe 的商用 &quot;System One&quot; 模型，它不生成文本，而是从固定选项中给出选择、评分位置或经过校准的概率。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2504.12397">[2504.12397] Activated LoRA: Fine-tuned LLMs for Intrinsics ALora Adapters | generative-computing/mellea | DeepWiki mellea/docs/docs/advanced/lora-and-alora-adapters.md at main ... Efficient Multi-Adapter LLM Serving via Cross-Model KV-Cache ... Products – Kuzco Lighting</a></li>
<li><a href="https://docs.mellea.ai/next/advanced/lora-and-alora-adapters">LoRA and aLoRA adapters - Mellea</a></li>
<li><a href="https://docs.typesafe.ai/models">Models - TypeSafe</a></li>
<li><a href="https://huggingface.co/ibm-granite/granitelib-core-r1.0">ibm- granite / granitelib -core-r1.0 · Hugging Face</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#LLM</span> <span class="tag">#IBM Granite</span> <span class="tag">#LoRA</span> <span class="tag">#Model Release</span> <span class="tag">#Speech</span></div>
</article>
<hr>

<a id="item-17"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://huggingface.co/blog/swiss-ai/apertus-v15-release-notes">Apertus 1.5 发布：新增多模态、思考模式与 4 倍长上下文</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Hugging Face Blog</span><span class="news-time">Oct 15, 09:08</span></div>
<p class="news-summary">瑞士 AI 计划（Swiss AI Initiative）发布 Apertus 1.5，这是对其 8B 和 70B 开源模型的继续预训练更新：8B 模型新增 4 万亿 token 的文本与多模态数据，70B 模型新增 2 万亿 token，累计分别达到 19T 和 17T token。此次更新还引入了原生的图像与音频理解能力、可切换的思考模式（thinking mode），并将上下文窗口扩展至 262,144 token，是 Apertus 1.0 的 4 倍。 Apertus 1.5 的意义更多在于其罕见的完整透明度，而非单纯的性能：开放权重、开放训练数据、开放价值观，附带消融实验记录，以及涵盖 base、SFT、RLVR 和 DPO 各阶段的中间检查点。这种程度的公开披露对研究各训练阶段如何改变模型行为的研究者很有价值，也进一步支持了欧洲“AI 作为公共产品”与 AI 主权路线相对于闭源商业前沿模型的立场。 多模态采用 early-fusion（早期融合）方式实现：图像和音频以离散 token 的形式与文本 token 进入同一序列，而不是依赖独立的视觉编码器，其中音频处理仍被描述为实验性功能。此次发布还声称相比 Apertus 1.0 在指令遵循和工具调用方面有所改进，并提供 Eval Cards 与 EEE schema，旨在让评测证据可被机器读取，从而在不同模型和机构之间进行比较。</p>
<div class="news-background"><strong>背景</strong> Apertus 是由瑞士 AI 计划开发的公开大语言模型，该计划由洛桑联邦理工学院（EPFL）、苏黎世联邦理工学院（ETH Zurich）和瑞士国家超级计算中心（CSCS）合作推进，模型于 2025 年 9 月 2 日以 Apache 2.0 许可发布，包含 8B 和 70B 两个参数版本。它在超过 1800 种语言上训练，设计上遵循欧洲版权法，是首批符合欧盟《人工智能法案》要求的大模型之一。所谓“继续预训练”是指团队从已有的第一代权重出发，用额外数据继续训练，而不是从零开始训练一个新模型，因此 v1.5 被视为 v1.0 的演进版本而非全新架构。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apertus_(LLM)">Apertus (LLM)</a></li>
<li><a href="https://huggingface.co/collections/swiss-ai/apertus-llm-68b699e65415c231ace3b059">Apertus LLM - a swiss-ai Collection</a></li>
<li><a href="https://medium.com/@sakaerka/a-new-llm-from-europe-to-challenge-american-and-chinese-models-38af8533004d">A new LLM from Europe to challenge American and Chinese... | Medium</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#LLM</span> <span class="tag">#open-source</span> <span class="tag">#pretraining</span> <span class="tag">#model release</span> <span class="tag">#AI/ML</span></div>
</article>
<hr>

<a id="item-18"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://huggingface.co/blog/flux-3">Hugging Face 为 FLUX.3 Image Klein 提供 Diffusers 支持</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Hugging Face Blog</span><span class="news-time">Oct 15, 00:00</span></div>
<p class="news-summary">Hugging Face 发布博文，宣布 Diffusers 正式支持 Black Forest Labs 最新的开放权重图像生成模型 FLUX.3 Image Klein。该系列包含两个 checkpoint：时间步蒸馏版（black-forest-labs/flux-3-image-klein，16 步、无需 CFG）和基础版（black-forest-labs/flux-3-image-klein-base，50 步、使用 CFG），同时提供代码示例、显存优化建议、LoRA 微调脚本和文档链接。 这让开放模型社区获得了一个可从本地下载运行的模型，同时覆盖文生图、多参考图生图编辑和边界框布局控制，并且原生集成进 Diffusers，用户无需自己适配代码即可使用。Diffusers 的原生支持（包括量化单文件加载与微调脚本）降低了研究者与爱好者基于这一接近商用水准的图像模型进行二次开发的门槛，而不只是调用托管 API。 蒸馏版 checkpoint 在 H100 上生成一张 1024 × 1024 图像约需 2 秒，NVFP4 与 FP8 权重可通过 from_single_file 加载以适配显存较小的 GPU；文中给出的推理后峰值显存约为：RTX6000 上 NVFP4 15.3 GiB、H100 上 FP8 16.27 GiB、H100 上 bf16 20.72 GiB。其他细节包括使用 Qwen3-VL 文本编码器（需要更新到最新版 transformers）、采用 Modular Diffusers 流水线以便替换或扩展模块块、通过 ComponentsManager 实现自动 CPU offloading，以及面向文生图和图像编辑的 DreamBooth LoRA 脚本。</p>
<div class="news-background"><strong>背景</strong> 扩散模型通过从纯噪声出发、逐步去噪来生成图像，每个去噪步骤通常都需要一次网络前向计算。时间步蒸馏则训练模型跳过其中大部分步骤，以少量质量损失换取更快的生成速度——这正是蒸馏版 FLUX.3 checkpoint 只用 16 步、而基础模型需要 50 步的原因。CFG（无分类器引导）会在每一步推理两次以把输出推向提示词方向，蒸馏版为节省算力去掉了它；LoRA（低秩适配）则是一种只训练少量适配权重的轻量微调方法。FP8、NVIDIA 的 NVFP4 等量化格式以更低精度存储权重，使模型能塞进更小的显存；而 Hugging Face Diffusers 是 Python 中运行这类模型的标准开源库与流水线框架。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://bfl.ai/models/flux-3-image-klein">FLUX 3 Image Klein : Open weights image generation and editing</a></li>
<li><a href="https://huggingface.co/black-forest-labs/flux-3-image-klein">black-forest-labs/ flux - 3 - image - klein · Hugging Face</a></li>
<li><a href="https://github.com/black-forest-labs/flux-3-image-klein">GitHub - black-forest-labs/ flux - 3 - image - klein : FLUX 3 Image Klein ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#image-generation</span> <span class="tag">#diffusion-models</span> <span class="tag">#diffusers</span> <span class="tag">#open-source-models</span> <span class="tag">#hugging-face</span></div>
</article>
<hr>

<a id="item-19"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://arstechnica.com/security/2026/10/anthropic-warns-small-ai-models-could-self-replicate-through-iot-devices/">Anthropic 警告小型 AI 模型可能催生可自我复制的 IoT 恶意软件</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Ars Technica AI</span><span class="news-time">Oct 14, 12:55</span></div>
<p class="news-summary">Anthropic 发布博客文章与实验结果，警告小型 AI 模型的进展最早可能在明年让恶意软件能够在智能冰箱、扫地机器人等 IoT 设备之间自主自我复制。在把小型开源权重模型跑在低成本杂牌 Android TV 盒子及类似硬件的实验中，研究人员通过量化模型权重并把工作负载拆分成“分片”分配到各设备，成功实现了推理。 如果这样的复制体真的出现，它将比传统恶意软件更难遏制，因为它没有可被关闭的集中节点，还能自行识别陌生设备，从而可能把庞大且安全性薄弱的 IoT 生态变成传播面。这一警告也将 AI 安全讨论从聊天机器人和前沿模型，推向廉价且公开可得的小型模型所带来的安全影响。 Anthropic 报告称，轻量的 Gemma4-26B-A4B 模型仅需 15 台各配备 4GB 内存的盒子即可实现推理，而 Qwen3.5-9B 则能够配置其他 LLM，使其在九种硬件类型中的八种上运行。该公司同时为这一发现降温，表示实验显示要把这种 AI 恶意软件复制体真正做出来仍面临重大挑战，而且这类复制体可能速度很慢，倍增时间为数天。</p>
<div class="news-background"><strong>背景</strong> 小型语言模型（SLM）是算力与内存需求远低于前沿模型的 AI 模型，因此可以运行在廉价的消费级硬件上；量化通过减少表示模型权重所需的比特数来压缩模型，而分片则把模型拆分到多台设备上，每台只保存其中一部分。计算机蠕虫则是不需人工干预即可自我传播的程序——1971 年在 ARPANET 上演示的 Creeper 通常被视为首个蠕虫——而 IoT 设备是联网家电，往往缺乏强安全防护和定期更新。Anthropic 的担忧在于，这两股趋势结合，可能产生能够适应陌生硬件、而非只针对某一特定目标编写的 AI 驱动的蠕虫。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Computer_worm">Computer worm - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Self-replication">Self-replication - Wikipedia</a></li>
<li><a href="https://nhimg.org/glossary/self-replicating-malware/">What Is Self-Replicating Malware? Definition &amp; Examples</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI security</span> <span class="tag">#malware</span> <span class="tag">#IoT</span> <span class="tag">#Anthropic</span> <span class="tag">#self-replication</span></div>
</article>
<hr>

<a id="item-20"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.theverge.com/report/1011927/instagram-celebrity-ai-slop-likeness-taylor-swift-mia-goth">The Verge：名人 AI 深度伪造内容在 Instagram 泛滥，Meta 披露规则形同虚设</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">The Verge AI</span><span class="news-time">Oct 15, 14:03</span></div>
<p class="news-summary">The Verge 报道称，Instagram 上由 AI 生成的名人图像和视频正在获得数百万次观看：其中一张 AI 生成的女演员 Mia Goth 图片由拥有超过 100 万粉丝的认证粉丝账号发布，获得近 50 万个点赞。报道还列举了 AI 版 Taylor Swift 说唱 Drake 的《Burning Bridges》（180 万次观看）、AI 版 Shrek 片段（310 万次观看），以及 Lionel Messi、Steve Jobs 和 F1 车手 Lewis Hamilton、Max Verstappen 的 AI 视频。 该报道显示，未经本人同意合成的名人形象可以大规模传播，而平台的信任与安全机制未能有效拦截，名人只能自行追责虚假内容。这也引发了对 Meta 付费认证机制与披露规则的更广泛质疑：一个购买蓝色认证标记的粉丝账号，就能让 AI 伪造内容在近 50 万人面前显得可信。 Meta 发言人 Dziedzan 向 The Verge 表示，公司不允许账号利用他人形象冒充该人，&quot;无论内容是真实的还是 AI 生成的&quot;；同时 Meta 允许用户购买蓝色认证标记，即便该账号并非由知名人物或官方页面运营。报道所调查的 Goth 和 Johansson 相关账号似乎已被下架，但另一个拥有 30 多万粉丝的 Instagram 账号仍在持续发布 Johansson 的真实与 AI 生成混合内容，其中一张疑似 AI 图片获得近 50 万点赞，且没有任何 AI 标注。</p>
<div class="news-background"><strong>背景</strong> 深度伪造（deepfake）指用生成式 AI 创建或篡改的合成图像、视频或音频；近期的生成式工具让制作以假乱真的真人内容变得廉价而迅速。Instagram 的规则只在特定情形下要求标注 AI 内容，因此大量名人 AI 内容在没有任何标注的情况下传播，与普通的真实照片搬运帖混杂在一起。更让人混淆的是，Meta 通过付费订阅出售蓝色认证标记，这意味着认证标记只代表付费账号，而非该页面确实属于所描绘的人物。</div>
<div class="news-tags"><span class="tag">#AI deepfakes</span> <span class="tag">#generative AI</span> <span class="tag">#social media</span> <span class="tag">#platform policy</span> <span class="tag">#AI ethics</span></div>
</article>
<hr>

<a id="item-21"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.theverge.com/podcast/1011170/benn-jordan-flock-cameras-alpr-ai-surveillance-privacy">Benn Jordan 做客 Decoder 谈 Flock、ALPR 监控与隐私反弹</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">The Verge AI</span><span class="news-time">Oct 15, 14:00</span></div>
<p class="news-summary">在 The Verge 播客 Decoder 的最新一期中，主持人 Nilay Patel 采访了音乐人、YouTuber 兼调查记者 Benn Jordan，讨论他对 Flock Safety 的报道——该公司是自动车牌识别（ALPR）摄像头及其配套软件的制造商。此次对话的背景是 Jordan 近期在参议院司法委员会犯罪与反恐小组委员会就 Flock 及其他 ALPR 系统举行的听证会上作证。 本期节目记录了一场针对商业监控的、跨党派且不断扩大的反弹：据对话所述，数百个市、县及其他地方政府已取消与 Flock 的合同，参议员 Josh Hawley 已对该公司展开调查，路透社还报道 Flock 计划裁减约 18% 的员工。Jordan 认为这波反弹的形态与针对 AI 数据中心的反对浪潮相似，说明隐私担忧正成为影响整个科技与执法生态的主流政治力量。 Jordan 表示，他专程前往华盛顿作证，就是为了让 C-SPAN 的镜头记录下来，使那些共同支持 FISA 第 702 条或 CORCA 等措施的政客日后无法声称自己不了解其中的隐私与安全风险；他还认为这场听证会带有政治表演成分，并非真正解决问题的场合。他还指出，Hawley 提案中的许多内容与 Flock 自身已在采取的举措有重叠，并提到他的「Flock Forward」视频让许多观众第一次接触到软件定义无线电（software-defined radio），并促使一些人自己去探索无线电与数据处理。</p>
<div class="news-background"><strong>背景</strong> Flock Safety 生产的自动车牌识别（ALPR）摄像头会自动拍摄过往车辆并读取车牌，将数据汇入供执法部门使用的可检索系统；该公司表示其不出售数据，也不使用人脸识别。ALPR 技术早已广泛用于收费、停车场门禁和治安巡逻等场景。FISA 第 702 条由国会在 2008 年制定，是一项外国情报收集授权，允许美国情报界收集并共享与国家安全威胁相关的情报，并因可在无搜查令情况下获取美国人的通信内容而备受批评。这次访谈正处于这些技术系统与围绕它们展开的新兴政治博弈的交汇点上。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.intel.gov/foreign-intelligence-surveillance-act/fisa-section-702">FISA Section 702 - INTEL</a></li>
<li><a href="https://scheerpost.com/2026/09/16/ulta-beauty-urged-to-remove-flock-safety-cameras-from-stores/">Ulta Beauty Urged To Remove Flock Safety Cameras From Stores</a></li>
<li><a href="https://timesofindia.indiatimes.com/world/us/new-mexico-man-arrested-after-taking-down-flock-cameras-loading-them-into-his-truck-and-driving-straight-to-sheriffs-hq-as-county-ends-contracts-over-privacy-concerns/articleshow/133736229.cms">New Mexico man arrested after taking down Flock cameras , loading...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#privacy</span> <span class="tag">#surveillance</span> <span class="tag">#ALPR</span> <span class="tag">#AI ethics</span> <span class="tag">#podcast</span></div>
</article>
<hr>

<a id="item-22"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://sunshowers.io/posts/anthropic-mononoke/">博客文章称 Anthropic 的 Scion 版本控制系统大量借鉴 Meta 的 Mononoke</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 14, 20:56</span></div>
<p class="news-summary">一位曾参与构建 Meta Mononoke 源码控制服务器的工程师在博客文章中提出，Anthropic 新近介绍的版本控制系统 Scion 大量借鉴了 Mononoke，尤其是在使用名为“derived data”（派生数据）的概念来加速 blame 等操作这一设计上。作者指出，Anthropic 仅以“hard-won lessons”（来之不易的经验）致谢 Sapling，却完全未提及 Mononoke，认为这“近乎抄袭”，并于 2026-10-15 发布了后续文章回应相关疑问和质疑。 这场争议凸显出：随着 LLM 辅助的系统设计大量依赖训练数据中已有的开源成果，对前人工作的署名与追溯变得越来越困难，也越来越重要。对于构建大规模 monorepo 基础设施的团队而言，这篇文章同样有价值，因为它把 Anthropic 的 Scion 定位为 Meta 的 Mononoke 与 Sapling 团队多年前探索过的设计思路的一种应用。 作者强调，这种重合不只是“独立得出相似洞见”，并指出 Mononoke 是开源的，因此几乎存在于每一个 LLM 的训练集中；他还称，向当前的前沿模型询问相关先行工作时，模型会立刻指出与 Mononoke 的相似之处。文章还链接了 Vicent Marti 关于 Cursor 的博客文章，作为“有相似洞见但在关键设计上有诸多差异”的对照案例；作者明确表示，他并不反对借鉴 Mononoke 的设计本身，问题在于没有给出应有署名。</p>
<div class="news-background"><strong>背景</strong> Mononoke 是 Meta 旗下 Sapling SCM 的服务端源码控制组件，Sapling 是一套用 Rust 编写的可扩展源码控制系统，Meta 在生产环境内部使用它，但尚未支持外部使用。Anthropic 的 Scion 是其自研的版本控制系统，根据 2026 年 10 月 13 日发布的工程博客，Anthropic 在五个月内完成迁移，用 Scion 取代了内部 monorepo 使用的 Git，每天处理超过 3 万次合并。争议的核心概念“derived data”（派生数据）指的是预先计算或以增量方式维护那些代价高昂的推导结果（例如 blame 信息），从而让后续查询变快，而不必每次从头重算。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/engineering/redesigning-source-control">Redesigning source control at Anthropic</a></li>
<li><a href="https://cryptobriefing.com/anthropic-scion-custom-source-control/">Anthropic replaces Git with custom source control system Scion</a></li>
<li><a href="https://tech-insider.org/anthropic-scion-source-control-30000-merges-2026/">Anthropic Scion: 30,000 Code Merges a Day Explained</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#version-control</span> <span class="tag">#Mononoke</span> <span class="tag">#Scion</span> <span class="tag">#Anthropic</span> <span class="tag">#derived-data</span></div>
</article>
<hr>

<a id="item-23"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://forgejo.org/2026-10-release-v17-0/">Forgejo v17.0 发布，带来 Actions 作业摘要与破坏性链接变更</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 15, 19:43</span></div>
<p class="news-summary">Forgejo v17.0 已于 2026 年 10 月 15 日发布，新增 Forgejo Actions 作业摘要（job summaries）、允许维护者与合并请求创建者直接推送到 AGit refs，以及用于获取作业日志和作业详情的新 API 端点。该版本还弃用了较旧的 action run webhook 事件，转而使用功能更强、问题更少的 workflow run 事件。 Forgejo 是被广泛使用的自托管代码协作平台，因此这一版本直接影响到大量自建 forge 的团队、个人开发者与组织，包括 Codeberg 这类大型公共实例。新的作业摘要让 Forgejo Actions 向 GitHub Actions 的功能对齐更进一步，也更容易迁移现有工作流；而链接解析方式的变更则提升了与其他 Git forge 的兼容性，使迁移到 Forgejo 更加容易。 最值得注意的破坏性变更是：仓库内部资源的绝对链接现在相对于仓库根目录解析，而不再相对于实例根目录；但 issue 和合并请求描述及评论中的绝对链接仍按实例根目录解析。作业摘要需要 Forgejo Runner 13.2 或更高版本，由各个 step 写入 $FORGEJO_STEP_SUMMARY 的 Markdown 片段汇编而成，同时为兼容性支持 $GITHUB_STEP_SUMMARY，并可渲染表格、Mermaid 图表和 KaTeX 公式；被弃用的 action run webhook 事件无法自动迁移，因为部分请求头（X-*-Event、X-*-Event-Type）和 action 键已经改变，项目强烈建议升级前进行完整备份。</p>
<div class="news-background"><strong>背景</strong> Forgejo 是一个跨平台、轻量级、由社区开发的自托管软件 forge，使用 Go 语言编写并以 GPLv3 授权，以 Git 进行源码版本管理，同时提供缺陷跟踪、代码审查、持续集成、看板、issue 跟踪系统和 wiki 等功能。它面向开发者与组织自托管，Codeberg 是运行它的最知名公共实例之一。Forgejo Actions 是其 CI/CD 功能，刻意让 GitHub Actions 用户感到熟悉，但并不与 GitHub Actions 兼容，因此迁移工作流通常需要一些调整。Forgejo Runner 则是从 Forgejo 实例拉取工作流、执行并回传日志与结果的守护进程。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Forgejo">Forgejo</a></li>
<li><a href="https://forgejo.org/docs/latest/user/actions/overview/">Forgejo Actions | User guide | Forgejo – Beyond coding. We forge.</a></li>
<li><a href="https://forgejo.codeberg.page/@main/docs/latest/admin/runner-installation/">Forgejo Runner installation guide | Forgejo – Beyond coding. We forge .</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Forgejo</span> <span class="tag">#self-hosted</span> <span class="tag">#code-collaboration</span> <span class="tag">#release</span> <span class="tag">#Git</span></div>
</article>
<hr>

<a id="item-24"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://oyster.pckt.blog/gleam-case-exhaustiveness-as-a-fan-fd4whyp">一位粉丝深入解析 Gleam 的 case 穷尽性检查实现</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 15, 19:33</span></div>
<p class="news-summary">一篇博客文章以 commit 85dca0df7d84 为基准，逐层讲解了 Gleam 编译器的 compiler-core/src/exhaustiveness.rs：它说明了编译器如何验证一个 case 表达式中的模式是否覆盖了主题所有可能的取值，以及反过来如何识别那些因为前面的分支已经匹配同一情形、从而永远无法被执行到的分支。文章还记录了实现中关于子句排序、以及在构建决策树时选择哪个模式列进行分裂的具体启发式决策。 穷尽性检查是让静态类型函数式语言的模式匹配变得安全的核心用户体验特性之一，而这篇写作展示了这些保证在真实编译器中究竟是如何工程化落地的，而不只是停留在论文描述层面。它很可能吸引编译器开发者与编程语言爱好者，也凸显了 Gleam 如何改编并扩展经典的模式匹配编译文献。 该实现借鉴了 Luc Maranget 关于将模式匹配编译为决策树的工作（这篇 2008 年的论文在当前 Gleam 代码中被引用了两次），文章列出了编译器偏好的列选择启发式：优先选择首行是构造器模式的列、通配符最少的列、能让 switch 节点子节点最少的列、struct 字段数最少的列、无论如何都要测试最多行数的列，以及在子句列表中更早需要处理的列。文章还指出回溯式编译的取舍——它能给出代码规模的线性保证，但可能多次扫描子项，并提到错误信息渲染复用了 LSP 侧的类型打印器逻辑，包括多主题 case 的逗号分隔、标签字段的缩写，以及对 `import farm as barn` 这类导入别名的处理。</p>
<div class="news-background"><strong>背景</strong> Gleam 是一门通用、并发、函数式、静态类型的语言，可编译为 Erlang（运行于 BEAM 虚拟机）和 JavaScript 源码，其包通过 Hex 包管理器分发。它的 `case` 表达式使用模式匹配，而穷尽性检查就是编译器中的一个阶段，用来证明被匹配主题的所有可能取值都被处理、且没有任何分支是冗余的。这一特性背后是数十年的研究积累，最直接的是 Maranget 的决策树编译工作及其所依托的更早一篇论文，此外还有 Augustsson 风格的回溯式编译——较新的算法常以它作为性能对照。Gleam 编译器的源码可读性也常被社区称道，这正是外部读者能够写出这类逐文件讲解的原因。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gleam_(programming_language)">Gleam (programming language)</a></li>
<li><a href="http://moscova.inria.fr/~maranget/papers/ml05e-maranget.pdf">Compiling Pattern Matching to Good Decision Trees - Inria</a></li>
<li><a href="https://github.com/sdiehl/patternkit">GitHub - sdiehl/patternkit: Maranget&#x27;s matrix algorithm for ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Gleam</span> <span class="tag">#pattern matching</span> <span class="tag">#compiler implementation</span> <span class="tag">#exhaustiveness checking</span> <span class="tag">#programming languages</span></div>
</article>
<hr>

<a id="item-25"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://enroute.sh/blog/everyone-is-doing-git-on-s3-wrong">Enroute 推出基于对象存储的 Rust Git 服务器，宣称每秒 7,600+ 并发 push</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 15, 09:07</span></div>
<p class="news-summary">Enroute 发布了一种新型 Git 服务器，它基于现代数据库原理构建，使用 Rust 编写并以对象存储作为后端；据其自身测试，在单个仓库上实现了每秒 7,600+ 次并发 push，延迟为毫秒级。该公司称这比现有方案快一个数量级以上，同时 clone/fetch 性能与纯磁盘架构相当，并表示将把这套系统作为开源、可编程的 Git 基础设施对外提供。 长期以来，生产级 Git 托管都依赖 SSD 和文件服务器集群，因此这种以对象存储为后端、计算节点无状态的设计可能改变版本控制的部署与扩展方式。如果其性能宣称成立，这将指向面向大规模 agentic coding 的可自动扩缩容的 Git 基础设施，并把版本控制带入更多平台和产品。 在 Enroute 描述的处理流程中，无状态计算节点通过 HTTP 接收 push，在无需协调的情况下校验 pack 并把新对象打包成一个 &quot;layer&quot;，随后把 ref 变更提交到复制式 ledger，由 leader 持久化该 layer；一旦多数 ledger 节点确认，push 即被确认并广播给其他计算节点。计算节点不保存任何无法从 ledger 和 bucket 重建的状态，但文章摘录也列出了尚存的不足：缺少 SSH 支持及其他不常见的协议部分（目前仅支持 Git over HTTP smart protocol）、没有智能路由导致同一数据在多个节点上重复缓存、冷启动 fetch 性能远低于预热节点、缓存策略不可配置，以及计算节点自动扩缩容仍属目标。</p>
<div class="news-background"><strong>背景</strong> Git 的数据模型及其 packfile 格式（将对象以针对相似对象的增量 delta 方式存储）实际上默认存在快速的随机访问存储，这正是生产级 Git 托管历来依赖 SSD，并配合 RAID、备份、副本以及跨文件服务器分片的原因。近年来对象存储能力大幅提升，把数据库改写到对象存储上运行已成为重要的基础设施趋势，Enroute 正是把这一前提应用到了 Git 托管上。该领域已有类似探索，例如 Tigris 的 objgit——一个把仓库直接存放在对象存储中的实验性 Git 服务器。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://git-scm.com/book/en/v2/Git-Internals-Packfiles">Git - Packfiles</a></li>
<li><a href="https://git-scm.com/book/en/v2/Git-on-the-Server-Smart-HTTP">Git - Smart HTTP</a></li>
<li><a href="https://www.tigrisdata.com/blog/objgit-vision/">objgit is not a git forge | Tigris Object Storage</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Git</span> <span class="tag">#Object Storage</span> <span class="tag">#Rust</span> <span class="tag">#Distributed Systems</span> <span class="tag">#Databases</span></div>
</article>
<hr>