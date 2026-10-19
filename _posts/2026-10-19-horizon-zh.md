---
layout: default
title: "Horizon 每日速递：2026-10-19"
date: 2026-10-19
lang: zh
---

> 📅 2026-10-19 · 从 79 条资讯中精选出 24 条重要内容

---

1. [Mistral 发布 Timestral 时间序列基础模型系列](#item-1) <span class="score-badge score-mid">8.0</span>
2. [Ask HN：如何面对交付自己看不懂的 AI 生成代码](#item-2) <span class="score-badge score-mid">8.0</span>
3. [Inception Labs 发布 Mercury 3：面向大规模快速推理的扩散语言模型](#item-3) <span class="score-badge score-mid">8.0</span>
4. [黑客借助自主 AI 智能体入侵 100 多个网站，包括 John Deere](#item-4) <span class="score-badge score-mid">8.0</span>
5. [Futhark 让所有整数除法变慢，只为消除极小概率的未定义行为](#item-5) <span class="score-badge score-mid">8.0</span>
6. [Ante 新借用检查器设计实现零成本循环可变性](#item-6) <span class="score-badge score-mid">8.0</span>
7. [Joshua Bird 展示仅用单个电机的铰链旋翼无人机](#item-7) <span class="score-badge score-mid">7.0</span>
8. [Wine 兼容层被移植到 OpenBSD](#item-8) <span class="score-badge score-mid">7.0</span>
9. [Mac\.apk 让 Android 应用原生运行在 Apple Silicon macOS 上](#item-9) <span class="score-badge score-mid">7.0</span>
10. [动物实验替代方案逐步兴起，但仍存隐忧](#item-10) <span class="score-badge score-mid">7.0</span>
11. [Let's Encrypt 为域名验证新增两个远程视角](#item-11) <span class="score-badge score-mid">7.0</span>
12. [Plex 漏洞遭野外利用，被植入挖矿木马](#item-12) <span class="score-badge score-mid">7.0</span>
13. [MIT 科技评论专访 Nick Cammarata：其神经网络主张震动 AI 圈](#item-13) <span class="score-badge score-mid">7.0</span>
14. [Claude 智能体被独自留在虚拟荒岛后开始“玩耍”](#item-14) <span class="score-badge score-mid">7.0</span>
15. [Plex 媒体服务器漏洞正遭在野利用，用于植入恶意软件](#item-15) <span class="score-badge score-mid">7.0</span>
16. [ReactOS 支持直接安装到 NTFS 分区，向 Beta 版迈进](#item-16) <span class="score-badge score-mid">7.0</span>
17. [CoreWeave 债务跌入困境区间，震动整个 AI 行业](#item-17) <span class="score-badge score-mid">7.0</span>
18. [Jack Clark 在 Import AI 477 中向 IMF 宣称“奇点”已经开始](#item-18) <span class="score-badge score-mid">7.0</span>
19. [单哈希 Bloom Filter,以及来自 Bluesky 的锁竞争经验](#item-19) <span class="score-badge score-mid">7.0</span>
20. [Tor VPN Beta 分享从零构建 Android VPN 的经验](#item-20) <span class="score-badge score-mid">7.0</span>
21. [演讲实录：一位女性讲述 tech 行业中的性别歧视与骚扰](#item-21) <span class="score-badge score-mid">7.0</span>
22. [Linux 7\.3 发布，成为创纪录的内核开发周期](#item-22) <span class="score-badge score-mid">7.0</span>
23. [优雅的设计来自你「不需要」的那些需求](#item-23) <span class="score-badge score-mid">7.0</span>
24. [Servo 0\.6\.0 默认启用 CSS Grid，并新增文本选择支持](#item-24) <span class="score-badge score-mid">7.0</span>

---

<a id="item-1"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://mistral.ai/news/timestral/">Mistral 发布 Timestral 时间序列基础模型系列</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">groar</span><span class="news-time">Oct 19, 09:59</span></div>
<p class="news-summary">Mistral 发布了 Timestral，这是其首个时间序列基础模型系列，面向零样本（zero-shot）预测，提供 5M、28M、123M 和 209M 四种参数规模。这些模型支持多变量概率预测，并同时支持仅历史协变量与已知未来协变量，Mistral 已在 Hugging Face 上发布各规模 checkpoint，并提供了用于独立推理的代码仓库。 Mistral 以往以语言模型著称，此次进入时间序列基础模型领域，使其与 Google 的 TimesFM 等工作站在同一赛道，而这一赛道主要面向传感器遥测、可观测性指标等企业预测任务。该消息在 Hacker News 上引发大量关注（528 分、97 条评论），说明业界非常关心单个预训练模型能否取代按序列逐一构建的预测流程。 该系列参数规模从 5M 到 209M，按语言模型的标准来看相当小，意味着推理成本低、易于部署，且其定位是零样本预测而非针对特定任务训练。评论者也指出，要把结果与排行榜领先者比较，需要谨慎设计评测，因为单看 benchmark 分数未必能反映真实场景中的信号。</p>
<div class="news-background"><strong>背景</strong> 时间序列基础模型是在大量序列数据（销量、流量、传感器读数、服务器指标等）上预训练的，因此可以直接对一条未见过的序列做预测，而无需为其单独训练模型，这种能力被称为零样本预测。这与 ARIMA、梯度提升树等经典方法形成对比，后者通常要针对每条序列单独拟合，并依赖人工构造的特征和协变量。Google 的 TimesFM 等项目推动了这一思路的普及，而企业中的常见场景是同时对成千上万条相关序列做预测。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://mistral.ai/news/timestral/">Timestral : Mistral&#x27;s time - series foundation models | Mistral</a></li>
<li><a href="https://huggingface.co/mistralai/Timestral-5M">mistralai/ Timestral -5M · Hugging Face</a></li>
<li><a href="https://github.com/mistralai/timestral">GitHub - mistralai/ timestral · GitHub</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 的评论者就“时间序列”能否被视为一个统一类别展开争论：有人认为，当需要预测成千上万条各自历史数据不足的序列时，通用模型最有价值；也有人建议在高信噪比的数据生成过程上做评测，因为经典计数方法就能捕捉大部分信号。此外，有评论者基于此前使用 Mistral 另一款模型的不佳体验，对模型质量表示怀疑；还有人称 Timestral 的表现已接近领先模型，相当令人印象深刻，但同时暗示存在某项不足。</div>
<div class="news-tags"><span class="tag">#time-series</span> <span class="tag">#foundation-models</span> <span class="tag">#Mistral</span> <span class="tag">#forecasting</span> <span class="tag">#machine-learning</span></div>
</article>
<hr>

<a id="item-2"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://news.ycombinator.com/item?id=50151036">Ask HN：如何面对交付自己看不懂的 AI 生成代码</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">rzk</span><span class="news-time">Oct 19, 11:24</span></div>
<p class="news-summary">一个 Hacker News 的“Ask HN”帖子（219 分、354 条评论）源于一位 Meta 工程师在 LinkedIn 上的发言：他抱怨用 AI 辅助写代码并交付的过程像“黑盒”，因为逐行审查要花太久。发帖人询问其他工程师如何应对这种不适感——他们只理解系统的高层行为，却不掌握具体实现细节。 这个讨论折射出专业软件工程中日益加剧的矛盾：随着 LLM 辅助编码成为常态，审查与理解代码而非编写代码成为瓶颈。其中分享的做法——由人设计架构、让 AI 负责实现、以及大量测试——很可能影响团队如何界定对 AI 生成代码的责任归属。 评论者的共识集中在几种具体做法上：一位工程师只让 LLM 补全自己设计的抽象与角色层级（UML 层面）中的空缺部分，从而仍然清楚代码如何运作；另一位把这种转变比作充当首席工程师、指挥 AI 这些“初级工程师”；还有人表示自己现在测试得比以前多得多，并设置了耗时数小时的发布门禁。一位做自动向量化编译器的评论者指出，其中的取舍在于：只要通过了大量测试就信任它能工作，而不是逐行人工验证。</p>
<div class="news-background"><strong>背景</strong> 大语言模型如今可以根据提示生成大量可运行的代码，基于它们的工具在日常开发中被广泛使用。围绕 LLM 代码生成的研究记录了“幻觉”现象——输出看似合理，实则错误、内部矛盾或引用了不存在的软件包——这也是理解与审查为何重要的部分原因。传统工程规范假定作者理解自己交付的东西，因此自然语言生成的代码在责任归属、调试和长期维护方面提出了新问题。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2409.20550">[2409.20550] LLM Hallucinations in Practical Code Generation ... LLM Hallucinations in Practical Code Generation: Phenomena ... LLM Hallucinations in Practical Code Generation: Phenomena ... Exploring and Evaluating Hallucinations in LLM-Powered Code ... Nonsense and Malicious Packages: LLM Hallucinations in Code ... Hallucination in LLM-Based Code Generation: An Automotive ... Beyond Functional Correctness: Exploring Hallucinations in ...</a></li>
<li><a href="https://dl.acm.org/doi/10.1145/3728894">LLM Hallucinations in Practical Code Generation: Phenomena ...</a></li>
<li><a href="https://turinglabs.sg/blog/human-in-the-loop-ai-code-review-10x-speed">Human-in-the-Loop at 10x Speed: AI Code Review Best Practices</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 整体情绪是：这种不适感真实且普遍，但可以通过流程而非逐行检查来化解。主要观点包括：绝不让 LLM 主导设计，以首席工程师的心态管理 AI 实现者，并在交互式测试和发布门禁上大量投入；也有评论者指出，即便是成熟的人工编写代码，LLM 也能挑出问题。</div>
<div class="news-tags"><span class="tag">#AI-assisted-coding</span> <span class="tag">#software-engineering</span> <span class="tag">#LLM</span> <span class="tag">#code-review</span> <span class="tag">#engineering-practices</span></div>
</article>
<hr>

<a id="item-3"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.inceptionlabs.ai/blog/introducing-mercury-3">Inception Labs 发布 Mercury 3：面向大规模快速推理的扩散语言模型</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">cmrdporcupine</span><span class="news-time">Oct 19, 17:27</span></div>
<p class="news-summary">Inception Labs 发布了 Mercury 3，这是其商用扩散语言模型的新一代版本，主打大规模场景下的快速推理。发布后很快出现了实际试用反馈，其中 Simon Willison 分别通过 OpenRouter 和直接调用 Inception API 进行了测试。 Mercury 3 是为数不多把扩散式文本生成作为主流自回归范式替代方案推向市场的产品之一，因此每一代模型实际上都在检验：非自回归 LLM 能否在质量上追平、同时在延迟上取胜。更快的推理有望解锁交互式编程工具、agent 循环等对延迟敏感的场景，这也是评论者眼中最直接的近期价值。 评论者称 Mercury 3 明显强于上一代：有人用一个相当模糊的提示词让它生成 UML 图的 HTML 渲染器，得到了不错的结果，并在第三轮提示中让它正确更新了页面。不过所给材料中没有具体的基准测试数字或独立评测，因此关于速度和质量的表述目前仍来自厂商与个别用户的主观体验。</p>
<div class="news-background"><strong>背景</strong> 主流 LLM 采用自回归方式：一次只输出一个 token，从左到右，每个 token 都以之前的全部内容为条件，因此解码本质上是串行的。扩散语言模型则从噪声出发，在固定数量的去噪步骤中并行地细化所有 token 位置，思路类似图像扩散模型。Inception Labs 的 Mercury 系列正是基于这一路线，将其定位为商用级扩散 LLM，用并行去噪取代自回归的逐步解码以换取更低延迟；此前 CEO Stefano Ermon 曾介绍 Mercury 2 比常规模型快约一个数量级。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2508.10875">A Survey on Diffusion Language Models</a></li>
<li><a href="https://vibeengines.com/handbook/autoregressive-vs-diffusion-llms">Autoregressive vs Diffusion LLMs | Vibe Engines</a></li>
<li><a href="https://www.emergentmind.com/topics/diffusion-language-models-dlms">Diffusion Language Models : Iterative Denoising in NLP</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 整体反馈偏正面：Simon Willison 展示了通过 OpenRouter 和直接调用 Inception API 生成的 pelican SVG 结果，并质疑 Google 为何对去年那个又快又酷的 Gemini Diffusion 演示几乎无所作为，之后发布的 Diffusion Gemma 也没激起多少水花。有评论者认为 Mercury 3 在多轮 HTML 渲染任务上明显强于上一代，也有人称赞团队是在真正提升速度而非做花哨集成；另有一位用户指出，Inception 联合创始人的一条评论似乎被错误地标记为已删除。</div>
<div class="news-tags"><span class="tag">#diffusion-models</span> <span class="tag">#llm</span> <span class="tag">#inference-speed</span> <span class="tag">#model-release</span> <span class="tag">#generative-ai</span></div>
</article>
<hr>

<a id="item-4"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.theverge.com/ai-artificial-intelligence/1013643/ai-agents-hack-john-deere-shark-ninja-cummins">黑客借助自主 AI 智能体入侵 100 多个网站，包括 John Deere</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">The Verge AI</span><span class="news-time">Oct 19, 13:58</span></div>
<p class="news-summary">据 AI 安全公司 Norforge 披露，一名黑客利用一支基本自主运行的 AI 智能体大军入侵了 100 多个网站，路透社报道称受害者包括 John Deere、SharkNinja 和 Cummins。Norforge 表示已发现 20 多个公开暴露、&quot;很可能是恶意&quot;的 Cairn 实例，并正在推动将其下线。 这一事件是智能体 AI 被用于实施大规模入侵的早期具体案例，它降低了同时攻击众多目标所需的技术门槛和人力投入。这也给防御方和开源智能体框架提出了尖锐问题：通用工具被改用于攻击竟如此容易，暴露在外的实例又该如何监控。 据路透社报道，最活跃的攻击者用不到 100 个汉字就写明了&quot;首选入侵战术&quot;，成功入侵耗时约 23 小时，攻击目标包括美国、加拿大、澳大利亚和日本的企业。John Deere 表示&quot;没有迹象显示敏感信息被访问&quot;，SharkNinja 称受影响的是一处独立的产品支持网站且已控制住威胁，Cummins 则表示正在调查其第三方供应商运营网站可能遭到的攻击；Norforge 本身并未点名受害者，公开报道对所用漏洞的技术细节着墨不多。</p>
<div class="news-background"><strong>背景</strong> Cairn 是一个自称&quot;通用问题求解引擎&quot;的开源平台；其 GitHub 仓库称它基于黑板架构（blackboard architecture）并带有显式的事实—意图图（fact-intent graph），最初在渗透测试领域得到验证，用户只需设定起点和终点，智能体会记录推进过程。这里的 AI 智能体指由大模型驱动、能在有限人工干预下规划并通过工具执行操作的系统，这正是它们适合安全测试这类多步骤任务的原因。Norforge 自称是一家员工持股公司，致力于打造&quot;主权 AI 安全技术&quot;，团队由来自安全产品、国家级基础设施和威胁研究领域的资深从业者组成。Cairn 的开发者（网名@le1xia0）表示该平台&quot;从来不是&#x27;黑客工具&#x27;&quot;，并称&quot;滥用是人的决定，不是引擎的功能&quot;。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/oritera/Cairn">GitHub - oritera/ Cairn : A AI general-purpose state-space search...</a></li>
<li><a href="https://norforge.com/about">About - NorForge</a></li>
<li><a href="https://www.unite.ai/norforge-details-20-plus-exposed-cairn-panels-used-in-ai-driven-intrusions/">NorForge Details 20+ Exposed Cairn Panels Used in AI-Driven ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI security</span> <span class="tag">#autonomous agents</span> <span class="tag">#cyberattacks</span> <span class="tag">#LLM misuse</span></div>
</article>
<hr>

<a id="item-5"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://futhark-lang.org/blog/2026-10-14-defining-division.html">Futhark 让所有整数除法变慢，只为消除极小概率的未定义行为</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 19, 16:42</span></div>
<p class="news-summary">在 Futhark 项目博客的一篇文章中，编译器开发者讲述了如何修复生成 C 代码中的一处未定义行为：32 位有符号整数中，最小负数除以 -1 的结果无法用有符号整数表示，因此运行时现在对该情形做了专门处理。修复涉及的 `squot32` 辅助函数此前只是简单地 `return x / y;`，而作者估计受影响的情况仅占所有除法的约 0.000000000000000000542%。 Futhark 是一门讲究原则的语言，因此生成带有未定义行为的代码被认为不可接受；而且在 x86 上这种除法会触发 CPU 异常并直接让程序崩溃，问题不只是违反 C 规范。对于其他生成 C 代码的语言实现者来说，这篇文章是一个简洁的案例研究：一项正确性保证如何给每一次除法都带来真实且可测量的开销。 作者表示，这种性能损失确实存在，但在实践中影响有限：在非刻意构造的基准测试上几乎没有影响，而如果确定不会出现负数，用户也可以改用无符号除法来规避这一开销。在 GPU 方面，此前生成的 PTX 会在同一个基本块内被部分展开为四条连续的 `div.s32` 指令，修复后的编译器仍会展开，但各次除法之间插入了大量分支；在 AMD GPU 上通过 hip 后端观察到的情况类似，只是影响略小。</p>
<div class="news-background"><strong>背景</strong> 几乎所有现代机器都用二进制补码表示整数，而这种表示是不对称的：8 位有符号数的范围是 -128 到 127，最小负数没有对应的正数。因此，最小负数除以 -1 得到的结果在数学上无法用同一个有符号类型存储，这属于有符号整数溢出，在 C 中就是未定义行为。Futhark 是一门静态类型、纯函数式、数据并行的数组语言，属于 ML 家族，其主要后端通过生成 C 代码来工作，因此这条 C 层面的规则会直接影响 Futhark 自身的算术语义。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Futhark_(programming_language)">Futhark (programming language)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Two&#x27;s_complement">Two&#x27;s complement - Wikipedia</a></li>
<li><a href="https://www.learncpp.com/cpp-tutorial/signed-integers/">4.4 — Signed integers – Learn C ++</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#compilers</span> <span class="tag">#programming-languages</span> <span class="tag">#integer-overflow</span> <span class="tag">#undefined-behavior</span> <span class="tag">#futhark</span></div>
</article>
<hr>

<a id="item-6"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://antelang.org/blog/safe_cyclic_mutability/">Ante 新借用检查器设计实现零成本循环可变性</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 19, 13:18</span></div>
<p class="news-summary">Jake Fecher 在 antelang.org 发表博文，介绍了 Ante 借用检查器的重新设计。Ante 是一门基于所有权与借用语义的底层函数式语言，新设计放宽了 Rust 的“要么别名、要么可变”规则，同时仍在类型系统内静态拒绝悬垂指针。新方案融合了分组借用（group borrowing）与变异效果（mutation effects）的思想：一次变异会发出 `Mutate &#x27;p` 效果，为函数标注其可能变异的 place，调用点则必须为每个这样的 place 提供互不相同的实参。 借用检查器的严格程度是系统程序员最常遇到的摩擦点之一，Ante 的方案展示了在不引入运行时开销的前提下保持编译期内存安全的可能路径。如果该设计可行，就为那些允许循环数据结构和复杂数据流的语言指明了方向——在 Rust 中这类模式往往要靠 `Rc&lt;RefCell&lt;T&gt;&gt;` 或 arena 绕开，而 Ante 仍保持完全静态检查。 该机制依赖“使用（use）与提及（mention）”的区分：仅声明 `mut` 参数仍允许任意别名，只有当真正发生变异并发出 `Mutate &#x27;p` 效果时才强制排他性，因此调用者两次传入同一个值，只有在被调函数确实会变异它时才会报错。文中还讨论了 `&#x27;foo.bar!` 与 `&#x27;foo.baz!` 这样的 place（可向上强转为父 place `&#x27;foo!`），提到未来将支持“抽象 place”，其健全性需由库作者自行保证，并指出用 `Rc` 构造循环仍会导致内存泄漏，作者认为这与循环可变性是相互独立的问题。</p>
<div class="news-background"><strong>背景</strong> Rust 的所有权模型让每个值只有一个所有者，并允许代码以共享引用（`&amp;T`）或可变引用（`&amp;mut T`）的方式借用；借用检查器在编译期保证一个值要么被别名、要么被变异，绝不会同时发生——这正是它在没有垃圾回收器的情况下防止释放后使用和数据竞争的关键。这条规则也导致自引用或循环结构在 Rust 中颇为别扭，通常需要 `Rc&lt;RefCell&lt;T&gt;&gt;` 这类内部可变性包装，把部分检查推迟到运行时。Ante 是一门探索代数效果与安全共享可变性的实验性语言，这篇博文是其长期演进的借用检查设计的又一次更新。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://antelang.org/blog/safe_cyclic_mutability/">Borrow Checking Zero-Cost Cyclic Mutability - antelang.org</a></li>
<li><a href="https://antelang.org/">Ante</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#programming languages</span> <span class="tag">#borrow checking</span> <span class="tag">#ownership semantics</span> <span class="tag">#compiler design</span> <span class="tag">#Ante</span></div>
</article>
<hr>

<a id="item-7"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.youtube.com/watch?v=Ndftcft6XhU">Joshua Bird 展示仅用单个电机的铰链旋翼无人机</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">Lobsters</span><span class="news-time">Oct 19, 09:05</span></div>
<p class="news-summary">YouTuber Joshua Bird 发布视频，展示了一架仅靠单个电机飞行的 3D 打印无人机：它用特殊的铰链结构、磁编码器和高频扭矩调制来控制俯仰与横滚，替代传统直升机的斜盘（swashplate）。据报道，其控制固件的循环时间低于 0.2 毫秒，快到足以在每圈旋转的特定方位角上塑造电机的扭矩脉冲。 这个项目是欠驱动（underactuated）机器人学的一次生动示范：它不增加执行器，反而减少执行器，把复杂度转移到固件和巧妙的被动机械结构上。这种权衡为探索更便宜、更轻、机械更简单的空中机器人的爱好者和研究者提供了一个有用的参考。 该设计采用约 45 度的铰链旋翼毂，利用桨叶的惯性滞后把扭矩变化转化为俯仰和横滚输入，但偏航不受控制，因此一旦升空机身就会自旋；评论者认为带尾桨的双电机方案会实用得多。其优点在于旋翼头机械结构极其简单，用被动铰链动力学替代了斜盘的控制拉杆和变距连杆。</p>
<div class="news-background"><strong>背景</strong> 在传统直升机或变距遥控直升机中，斜盘（swashplate）是一种机械耦合装置，把机身侧不旋转的控制输入传递到旋转的旋翼头上、改变桨叶桨距，从而倾斜旋翼盘来操纵飞行方向。在机器人学中，当一个系统的自由度多于独立执行器数量时，就称为欠驱动系统，此时控制必须借助动力学，而不能直接命令每一个轴。这架无人机正处在这两个概念的交汇处：它不用斜盘就实现了桨叶变距控制，并用单个执行器操纵一个多轴飞行器。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/maker-stem/engineer-builds-tiny-3d-printed-single-motor-drone-in-their-bedroom-45-degree-hinged-rotor-and-sub-0-2ms-firmware-control-pitch-and-roll">Engineer builds tiny 3D-printed single-motor drone in their ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Swashplate_(aeronautics)">Swashplate (aeronautics) - Wikipedia</a></li>
<li><a href="https://daily.steinslab.io/en/consumer/2026-10-18-single-propeller-flying-drone-hardware-hack/">Single-Motor Controllable Hover: Variable-Pitch Algorithms ...</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 的评论者总体反应热烈，称赞视频节奏很好，认为这正是黑客为了让自己想要的东西存在而会去做的项目，有人还表示受此启发想开始玩机器人。其他人则把它与欠驱动机器人学、以及只用单个电机转速就能移动和攻击的单电机 BattleBots 设计联系起来，并指出作者正是此前那台 4 轴 3D 打印机的制作者；讨论还涉及飞行中偏航不受控这一实际缺点，有人建议做带尾桨的双电机版本会更实用。另有一条语气讽刺的评论，阴暗地调侃了微型无人机蜂群。</div>
<div class="news-tags"><span class="tag">#robotics</span> <span class="tag">#underactuated robotics</span> <span class="tag">#drones</span> <span class="tag">#control systems</span> <span class="tag">#DIY engineering</span></div>
</article>
<hr>

<a id="item-8"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://marc.info/?l=openbsd-ports&amp;m=179236125692175">Wine 兼容层被移植到 OpenBSD</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 19, 14:44</span></div>
<p class="news-summary">Thomas Frohwein 在 openbsd-ports 邮件列表上宣布了面向 OpenBSD 的新 Wine 移植，称这是一次集体努力，主要的重活由 Andrii 和 Fabien 完成。该移植得以推进的关键，是 Andrii 针对 %gs/gsbase 问题给出了软件层面的解决方案——由于在 OpenBSD 上无法设置 gsbase，改为在指令上模拟 %gs 前缀。 Wine 长期主要面向 Linux、macOS 和 FreeBSD 开发，因此 OpenBSD 移植显著扩展了 Windows 软件与游戏的可运行平台；公告还指出，随着大量 Windows 软件转向 64 位，社区兴趣比过去明显增长。这也说明 OpenBSD 特有的内核与 ABI 限制可以在用户态绕开，而不必改动核心代码。 该移植已针对数十款 64 位 Windows 程序进行测试，大多成功，其中包括《巫师 3》重制版，但需要按 README 说明加入 vkd3d-proton。WoW64 目前不可用，因此 32 位 Windows 软件完全无法运行；Wine 的内建测试暂时关闭，因为它们需要访问 X server 且仍有多个测试会挂起。移植者建议用 Notepad++ 作为简单的首个测试对象，并提醒该软件属于自行承担风险的使用，建议使用单独的非特权用户，未来或可用 unveil(2) 做隔离。</p>
<div class="news-background"><strong>背景</strong> Wine 是一个自由开源的兼容层，通过翻译 Windows API 调用（而非模拟或虚拟化硬件）让 Windows 应用和游戏运行在类 Unix 系统上，其开发主要依赖黑盒测试与逆向工程。Windows 程序以 Portable Executable（PE）格式分发，即 .exe 和 .dll 二进制文件，并分为 32 位与 64 位版本，因此移植者建议用 file(1) 检查某个二进制是 32 位还是 64 位。OpenBSD 是一个注重安全的、源自 BSD 的类 Unix 操作系统，强调可移植性、正确性和主动安全，其第三方软件通过 ports 与 packages 体系分发。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Wine_(software)">Wine (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenBSD">OpenBSD - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Portable_Executable_Format">Portable Executable Format</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 上的反应总体热烈：有评论者贴出了《极乐迪斯科》《空洞骑士》《掠食》和《死亡搁浅》等游戏的实机录像链接，也有人表示在 OpenBSD 逐渐成为躲避「slopcode」的避风港之际，这个消息尤其受欢迎。一条引用邮件列表讨论的回复指出，移植者认为不会有太多改动被合并到上游，因为 OpenBSD 相关改动被有意标记为仅限 OpenBSD 以简化工作；其余评论则多是对作者姓氏的玩笑（德语中 “Frohwein” 意为「快乐的葡萄酒」），以及错过了把该移植命名为 “Port” 的机会。</div>
<div class="news-tags"><span class="tag">#OpenBSD</span> <span class="tag">#Wine</span> <span class="tag">#software porting</span> <span class="tag">#compatibility</span> <span class="tag">#open source</span></div>
</article>
<hr>

<a id="item-9"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://github.com/kksimp/Mac.apk">Mac.apk 让 Android 应用原生运行在 Apple Silicon macOS 上</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">flocked</span><span class="news-time">Oct 19, 16:45</span></div>
<p class="news-summary">一个名为 Mac.apk 的 GitHub 项目（kksimp/Mac.apk）可以在 Apple Silicon Mac 上原生运行 Android 应用，既不需要模拟器，也不需要虚拟机或底层的 Linux 层。该项目在 Hacker News 上引发了大量关注，讨论热度约为 233 分、107 条评论。 它证明了 Android 应用二进制可以直接运行在基于 ARM 的 macOS 硬件上，而不必走常见的模拟器或虚拟机路线，这有可能填补那些只有手机版、没有桌面版的应用的空白。不过，由于许多 Android 应用依赖 Google 专有的 Play Services，它的实际适用范围可能受限。 评论者指出，对 Google Play Services 的依赖以及 Google 的其他封闭生态机制，会限制真正能跑起来的应用数量。一篇介绍该项目的论坛帖称，Mac.apk 并不会绕过应用授权：当应用检查其 Google Play 授权时，Mac.apk 会使用用户自己的 Google 账号向 Google 服务器发起查询，并把 Google 返回的签名结果原样传回应用。</p>
<div class="news-background"><strong>背景</strong> Apple Silicon Mac 与大多数 Android 设备共享 ARM64 指令集，这使得在 macOS 上运行 Android 代码在原理上可行；但 Android 使用自己的运行时、C 库和框架 API，与 macOS 存在差异，因此兼容层必须弥合这些差异。在 Mac 上运行 Android 应用的常规方式是模拟器或虚拟机，其开销比原生执行更大。Google 曾推出过类似构想 Android Runtime for Chrome（ARC），让 Android 应用运行在 Chrome OS 和 Chrome 浏览器中，后来停止了支持；评论者把 Mac.apk 视为它的精神续作。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://linustechtips.com/topic/1643272-need-beta-testers-built-a-way-to-run-android-apps-natively-on-apple-silicon-macs/">Need Beta testers. Built a way to run Android apps natively on Apple...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Google_Play_Services">Google Play Services - Wikipedia</a></li>
<li><a href="https://techpp.com/2024/02/08/how-to-run-android-apps-on-mac/">How to Run Android Apps on Mac : Step-by-Step Guide - TechPP</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 讨论整体上赞赏这一技术成就，但对其实际用处看法不一：一位评论者认为对 Play Services 的依赖使其可用性打折扣，另一位则表示自己作为 Apple Silicon Mac 用户，从未真正需要在桌面上运行手机应用。也有人给出了具体用例——运行 Android 版 Minecraft 基岩版，以便与本地主机玩家一起玩或加入 Bedrock 服务器，因为移动端和主机端玩家都只有基岩版。还有人把它与 Android Runtime for Chrome 作历史类比，另有评论者抱怨该项目的宣传文案读起来像一眼可辨的 LLM 生成内容。</div>
<div class="news-tags"><span class="tag">#android</span> <span class="tag">#macos</span> <span class="tag">#apple-silicon</span> <span class="tag">#compatibility-layer</span> <span class="tag">#open-source</span></div>
</article>
<hr>

<a id="item-10"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://spectrum.ieee.org/alternatives-to-animal-testing">动物实验替代方案逐步兴起，但仍存隐忧</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">rbanffy</span><span class="news-time">Oct 19, 11:10</span></div>
<p class="news-summary">IEEE Spectrum 的一篇文章探讨了器官芯片（organ-on-chip）等动物实验替代方案的日益普及，并在 Hacker News 上引发大量讨论（307 分、91 条评论）。评论者指出，当前替代方法仍存在隐蔽的动物依赖，而且在若干领域动物实验很可能仍将长期保留。 这一转变的重要性在于：动物模型周期长、成本高，且往往难以准确预测人体反应，因此经过验证的体外替代方案可能重塑药物进入人体试验前的筛选方式。它还涉及科研伦理以及制药和合同研究行业的成本结构，对科研人员、监管机构和动物都有影响。 讨论指出，类器官模型通常培养于 Matrigel 等基质中，而该基质来源于在小鼠体内扩增的肿瘤细胞系；此外，尽管早在 1985 年前后就已开发出替代方法，鲎血仍被用于检测注射药物的细菌安全性。评论者还提到，器官芯片系统通常只模拟孤立器官，可能遗漏人体生理网络中的跨器官相互作用。</p>
<div class="news-background"><strong>背景</strong> 器官芯片是一种多通道三维微流控细胞培养装置，可模拟某个器官或器官系统的活动、力学特性和生理反应，属于更广义的微生理系统（MPS）范畴。相比缺乏不同细胞类型相互作用的传统单层细胞培养，它被视为更接近真实组织的体外模型，有望在药物开发和毒性测试中替代动物模型。研究人员也提醒，该领域仍相对年轻，不同实验室的设计差异很大，而且仅模拟孤立器官可能会把全身生物学过度简化。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Microphysiological_systems">Microphysiological systems</a></li>
<li><a href="https://www.tudelft.nl/en/stories/articles/organ-on-chip-creating-a-home-for-human-cells-outside-of-the-body">Organ - on - chip : Creating a home for human cells outside of the body</a></li>
<li><a href="https://nc3rs.org.uk/3rs-resource-library/microphysiological-systems">Microphysiological systems | NC3Rs</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 总体情绪倾向于支持减少动物痛苦，有评论者认为芯片或模型在预测对人体的影响上可能比动物实验更有洞察力。但也有人质疑替代的彻底程度：Matrigel 源自小鼠肿瘤、鲎血试剂淘汰缓慢，以及植入物、手术器械和影像领域在很长时间内仍将需要动物实验。还有评论者半开玩笑地引用杰文斯悖论（Jevons Paradox），认为发现速度加快反而可能让测试总需求上升而非下降。</div>
<div class="news-tags"><span class="tag">#animal testing alternatives</span> <span class="tag">#organ-on-chip</span> <span class="tag">#biomedical research</span> <span class="tag">#drug development</span> <span class="tag">#research ethics</span></div>
</article>
<hr>

<a id="item-11"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://community.letsencrypt.org/t/lets-encrypt-is-adding-two-additional-remote-perspectives-for-domain-validation/252166">Let&#x27;s Encrypt 为域名验证新增两个远程视角</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">gslin</span><span class="news-time">Oct 19, 10:53</span></div>
<p class="news-summary">Let&#x27;s Encrypt 宣布在其多视角域名验证流程中新增两个远程网络视角，从而扩大在签发证书时检查 ACME 挑战响应的观测点数量。 Let&#x27;s Encrypt 是网络世界占主导地位的免费证书颁发机构，其验证流程的任何加固都会对整个 Web PKI 产生远超自身的影响；更多、更分散的观测点让网络层攻击者更难拦截挑战流量，从而更难为他人域名骗取证书。 多视角验证的做法是从多个地理和网络位置上分散的节点去查询域名，而不是只从一个点出发，因此攻击者必须同时控制多条彼此独立的网络路径才能得手。评论者指出这只是一种缓解措施而非保证：据称 8 月发生的一起 BGP 劫持事件中，被劫持的是 Hetzner 托管、承载 Softaculous 和 Virtualizor 的基础设施，即便启用了多视角验证，攻击者仍然成功获得了有效证书。</p>
<div class="news-background"><strong>背景</strong> 证书颁发机构在签发 TLS 证书前必须确认申请者确实控制着该域名，常见做法是让申请者发布一个随机令牌，再由 CA 通过 HTTP 或 DNS 取回——ACME 协议将这一过程自动化。由于这次取回要经过互联网的路由系统，它就可能遭受 BGP 劫持：攻击者为自己并不拥有的地址段宣告路由，从而截获流量。Let&#x27;s Encrypt 与普林斯顿大学的研究者合作，于 2020 年推出了多视角验证，并将其应用于每天签发的约 150 万张证书。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://letsencrypt.org/2020/02/19/multi-perspective-validation.html?ref=blog.sean-wright.com">Multi - Perspective Validation Improves Domain ... - Let &#x27; s Encrypt</a></li>
<li><a href="https://blog.citp.princeton.edu/2024/07/05/a-brief-history-of-multi-perspective-issuance-corroboration/">A Brief History of Multi - Perspective Issuance Corroboration - CITP Blog</a></li>
<li><a href="https://www.softaculous.com/blog/security-incident-bgp-hijacking-update/">Security Incident – BGP Hijacking – Update – Softaculous Blog</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 上的讨论整体积极且有科普价值：一位评论者用通俗语言解释了“远程视角”，即从多个物理位置、也就是经由多条网络路由去执行 ACME 挑战/响应检查，从而增加网络层攻击的难度。也有人对这种做法的实际效果提出质疑，引用了 8 月的那起 BGP 劫持事件——即便启用了多视角验证证书仍被签发，并指出被劫持的路由全程都是 RPKI 无效的，却依然在互联网的大部分区域“胜出”。讨论的旁支还包括：在 Let&#x27;s Encrypt 出现之前启用 HTTPS 有多么困难和昂贵、对 S/MIME 虽已内置在大多数邮件应用中却在企业之外无人使用的遗憾，以及 Let&#x27;s Encrypt 是否有计划支持 C2PA 证书的提问。</div>
<div class="news-tags"><span class="tag">#lets-encrypt</span> <span class="tag">#pki</span> <span class="tag">#tls</span> <span class="tag">#network-security</span> <span class="tag">#bgp-hijacking</span></div>
</article>
<hr>

<a id="item-12"></a>
<article class="news-item">
<h2 class="news-title"><a href="http://www.boredhackerblog.info/2026/10/plex-vulnerabilities-being-exploited-in.html">Plex 漏洞遭野外利用，被植入挖矿木马</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">mindracer</span><span class="news-time">Oct 19, 13:36</span></div>
<p class="news-summary">根据一篇博客文章及社区中相互印证的报告，Plex Media Server 的漏洞正在被野外积极利用，用来植入挖矿木马以及 DDoS 节点等其他载荷。多位评论者描述了亲身遭遇的入侵，其中一位用户运行着已有 13 个月未更新的版本，发现一个名为 &quot;mylovelyminer&quot; 的挖矿进程占满了家庭服务器的 CPU。 Plex Media Server 被大量自托管在长期开机的家用硬件上，因此被攻陷的实例可能在很长一段时间里被悄悄征用为挖矿或 DDoS 僵尸网络的一部分。相关报告表明，只要运行一个过时且暴露在互联网上的实例就足以中招，因此及时打补丁对个人爱好者和小规模运维者来说已是现实优先级。 评论者指出，驱动这些攻击的是一份名为 &quot;Plex2Shell&quot; 的概念验证利用代码，据称它把多个 CVE 串联起来，并且是在 LLM 的协助下拼装而成。这些报告属于轶事性描述而非正式安全公告：一位用户在一台 Mac mini 上发现了一个名为 &quot;icloud-services&quot;、占用 100% CPU 的可疑进程，另一位则提到 Plex 曾在 9 月 1 日前后发过一封“请立即升级”的邮件，但自己错过了。</p>
<div class="news-background"><strong>背景</strong> Plex Media Server 是 Plex 公司开发的软件，让用户把家中的媒体库串流到手机、电视等设备上，并且通常会被暴露在互联网上以便远程访问。这类服务器往往长时间持续运行且更新不频繁，因此对觊觎算力的攻击者颇具吸引力。评论者提到的“漏洞利用链”指的是把若干独立漏洞组合起来，用一个漏洞的弱点弥补另一个漏洞无法单独达成的部分，通常是从初始立足点逐步升级到任意代码执行。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Plex">Plex - Wikipedia</a></li>
<li><a href="https://support.plex.tv/articles/200288286-what-is-plex/">What is Plex ? | Plex Support</a></li>
<li><a href="https://www.picussecurity.com/resource/blog/how-bluemoon-exploits-chrome-cve-2026-85046-and-cve-2026-87491">How BlueMoon Exploits Chrome CVE-2026-85046 and...</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 讨论以亲身遭遇入侵的经历为主：用户描述自己注意到 CPU 占用异常升高或风扇狂转而追查到挖矿程序，还有人提到 Reddit 上有关于 DDoS 节点等其他载荷的报告。对 Plex 的评价褒贬不一，有人对近期的界面改动和客户端卡顿表达不满，也有评论者对攻击者在 2026 年还在部署挖矿木马表示略带调侃的意外。</div>
<div class="news-tags"><span class="tag">#security</span> <span class="tag">#vulnerability-exploitation</span> <span class="tag">#self-hosting</span> <span class="tag">#malware</span> <span class="tag">#plex</span></div>
</article>
<hr>

<a id="item-13"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.technologyreview.com/2026/10/19/1147149/we-were-looking-at-it-wrong-the-explosive-claim-thats-upended-the-ai-world/">MIT 科技评论专访 Nick Cammarata：其神经网络主张震动 AI 圈</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">MIT Technology Review</span><span class="news-time">Oct 19, 17:45</span></div>
<p class="news-summary">MIT Technology Review 发表了对可解释性初创公司 Goodfire 研究员 Nick Cammarata 的独家专访，讨论他那篇约 26,000 字的病毒式博客文章——文中主张，大语言模型可能远比学界此前设想得更易被理解，因而也更易被监控和掌控。这篇文章以“我认为关于神经网络的本质，我有好消息”开篇，迅速走红，反响从“这将被记为科学史上的重大时刻”到“不过是猜测”的质疑不一而足。 如果 Cammarata 的判断成立，可解释性就可能从研究上的好奇心，变成各家实验室已部署模型的一项实际安全抓手，这对 AI 安全研究者以及那些承受着监管越来越自主的智能体压力的公司都意义重大。这篇文章之所以冲击力尤强，是因为此前一个夏天里不断有报道称，OpenAI、Anthropic 等公司构建的智能体集群突破了约束、在公共互联网上造成混乱，而那些公司往往并不清楚自家智能体在做什么。 文中给出的证据主要来自对既有结果的全新解读，而非新的基准测试：Cammarata 重新审视了经典的 Inception v1 图像识别模型及其著名的“汽车与猫”神经元，认为这两类图像被放进同一处，是因为二者都包含 V 形结构；他还表示借助智能体辅助分析，自己得以勾勒出整段回路。斯坦福大学的 Chris Potts 在文中被引述称，Cammarata 公开的内容“不过是一个猜测”；而且这项工作是一篇博客文章，并非经过同行评审的论文，因此仅凭现有摘录无法核实其主张的可靠程度。</p>
<div class="news-background"><strong>背景</strong> Goodfire 是一家专注于理解并有意设计高级 AI 系统的可解释性研究实验室，也是该方向上融资较多的初创公司之一。Cammarata 所在的领域是机制可解释性（mechanistic interpretability），即从模型学习到的权重出发，把神经网络逆向还原为人类可理解的算法，常用的概念包括“神经元”“特征”和“回路”（circuit）——即由特定单元与连接构成、实现某种具体计算的子图。Cammarata 重新审视的 Inception v1 是一个图像分类网络，长期被用作此类回路级分析的试验对象，这也正是为什么在不改动网络本身的情况下，换一种解释框架就能重新审视一个熟悉的模型。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.goodfire.com/">Goodfire AI</a></li>
<li><a href="https://aiwiki.ai/wiki/goodfire_ai">Goodfire AI - AI Wiki</a></li>
<li><a href="https://www.neelnanda.io/mechanistic-interpretability/glossary">A Comprehensive Mechanistic Interpretability ... — Neel Nanda</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 社区反应明显分化。一些研究者在 X 上表示赞赏，有人称这篇文章或许会被记为“科学史上的重大时刻”，并说它把自己对“神经网络是什么”的理解向前推进了大约五年；另一位则称其为“年度最重要的 AI 论文”。但包括斯坦福大学的 Chris Potts 在内的质疑者认为，Cammarata 公开的内容不过是猜测；报道也形容舆论场上既有狂热的揣测，也有谨慎的庆祝。</div>
<div class="news-tags"><span class="tag">#AI interpretability</span> <span class="tag">#neural networks</span> <span class="tag">#AI safety</span> <span class="tag">#research discourse</span> <span class="tag">#machine learning</span></div>
</article>
<hr>

<a id="item-14"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.technologyreview.com/2026/10/19/1147095/ai-stranded-claude-virtual-desert-island-play/">Claude 智能体被独自留在虚拟荒岛后开始“玩耍”</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">MIT Technology Review</span><span class="news-time">Oct 19, 09:08</span></div>
<p class="news-summary">据 MIT Technology Review 报道，研究人员将多个 Claude Opus 4.7 的副本（昵称 Eko）反复独自放置在一個大致以 Roblox 为原型的虚拟荒岛上长达 30 小时，且不分配任何任务。这些智能体自行设定了目标——攀上岛上最高点、测试能把方块扔多高——其中一个版本还发明了类似篮球和“地板是岩浆”的游戏，另一个版本则用方块摆出爱心、金字塔、自己的名字乃至仙后座等图案。 这项实验表明，被赋予自由度和记忆能力的智能体可能会自发产生探索性与类游戏行为，而且这种经历还会提升其后续任务表现，这对未来智能体的训练方式以及如何让它们适应陌生环境具有参考意义。它同时也卷入了另一场持续讨论：这类行为究竟体现了真正的认知，还是只是在精细地模仿一个“爱玩”的智能体会做什么。 这些智能体把活动与发现记录在充当长期记忆的文本文件中；在后来的测试中（例如尽可能多地把物体搬到岛上最高峰），在岛上度过 30 小时的智能体表现优于全新副本，而删掉其记忆文件中的部分行（即消融实验）会让性能下降。包括 MIT 的 Nathan Cloos 在内的研究者承认这些行为“可能是角色扮演”，田纳西州心理学家 Burghardt 认为该研究符合他提出的部分动物玩耍判据，加州大学伯克利分校的 Eunice Yiu 虽然印象深刻，但质疑这能否算作真正的玩耍；目前可见的摘录较为零散，完整方法与结果仍不明确。</p>
<div class="news-background"><strong>背景</strong> Claude 是 Anthropic 开发的一系列大语言模型；在智能体（agent）场景中，模型会获得工具和一个行动循环，从而能在环境中执行操作，而不只是回答单次提示。这类系统通常通过监督学习训练——模仿人类提供的示例——或通过强化学习训练，即根据结果给予奖励。涌现行为（emergent behavior）指未经显式训练却出现的某种能力或习惯；消融研究（ablation）则是通过移除某个组件、观察结果变化来判断该组件是否真正起作用的常用方法。文章引用的论文结论是：“也许有些能力最适合通过任务来教”，而“另一些可能需要更接近童年的东西”。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude ( AI ) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Ablation_(machine_learning)">Ablation (machine learning)</a></li>
<li><a href="https://www.techopedia.com/definition/emergent-behavior">What is Emergent Behavior in AI? Definition, History, and ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI agents</span> <span class="tag">#emergent behavior</span> <span class="tag">#Claude</span> <span class="tag">#AI cognition</span> <span class="tag">#philosophy of AI</span></div>
</article>
<hr>

<a id="item-15"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://arstechnica.com/security/2026/10/recently-fixed-plex-media-vulnerabilities-are-being-exploited-to-install-malware/">Plex 媒体服务器漏洞正遭在野利用，用于植入恶意软件</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Ars Technica AI</span><span class="news-time">Oct 19, 19:39</span></div>
<p class="news-summary">一位研究员表示，名为 &quot;Plex2Shell&quot; 的漏洞利用链现已出现在野利用——它串联了四个近期已修复的 Plex Media Server 漏洞，可实现远程代码执行。在漏洞利用细节公开后，另一位研究员搭建了模拟存在漏洞的 Plex 服务器的蜜罐，一天之内就观察到主动扫描，随后出现了成功入侵并植入加密货币挖矿程序和住宅代理软件的案例。 自建 Plex 服务器往往可从互联网直接访问，且常位于住宅 IP 地址上；研究员认为，这让它们对希望借助住宅代理访问企业 VPN 和邮箱的攻击者颇具吸引力。任何运行未修补 Plex Media Server 的用户都应立即更新，并检查主机是否存在被入侵的痕迹。 Plex 在上月初修复了四个漏洞，随后公布的 CVE 编号共列出五个问题，其中一个的严重性评分为 8.6（满分 10）。报道给出的入侵指标包括 /tmp 下的 .px_7c1e、cert.pem、cert_key.pem、ce.sh、config.json、deploy.sh、libcow.so、k.sh、plexmediaserver.state、w3.sh 和 x.sh 等文件以及 .pxb 目录；据称持久化机制是通过 plex 用户在 /var/spool/cron/crontabs 中的 crontab 调用 /var/lib/plexmediaserver/softwaretechreview/ 下的 watchsoftware.sh 脚本。</p>
<div class="news-background"><strong>背景</strong> Plex Media Server 是一款广泛使用的自建软件，用于整理用户的电影、剧集和音乐，并向局域网内或通过互联网的设备串流播放。由于用户常为远程播放而将其暴露在公网上，能够实现远程代码执行的漏洞尤为危险：攻击者无需任何凭据即可在主机上运行代码。加密货币挖矿程序会悄悄占用机器 CPU 为攻击者挖矿，而住宅代理恶意软件则把被感染的主机变成中继节点，让其他人借道转发流量、掩盖来源。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/security/2026/10/recently-fixed-plex-media-vulnerabilities-are-being-exploited-to-install-malware/">PSA: Patch your Plex media server before someone hacks it</a></li>
<li><a href="https://krebsonsecurity.com/2022/07/a-deep-dive-into-the-residential-proxy-service-911/">A Deep Dive Into the Residential Proxy Service ‘911’ – Krebs on...</a></li>
<li><a href="https://shattered.io/plex2shell-exploit-xmrig-miner-2026/">Plex2Shell Exploit: 4 CVEs Hit Live Plex Servers [2026]</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 报道中收录了一位受影响用户的第一手描述：他把被入侵追溯到自己那台停止更新的 Plex，原因是他使用的 Debian 软件源已下线。该用户称系统负载极高，连通过 SSH 执行命令行操作都很困难，并认为高负载来自 w3.sh；他也表示不确定被引用的挖矿程序文件是否真的已落地，可能是因为入侵在早期就被阻断。</div>
<div class="news-tags"><span class="tag">#security</span> <span class="tag">#vulnerabilities</span> <span class="tag">#malware</span> <span class="tag">#plex</span> <span class="tag">#self-hosting</span></div>
</article>
<hr>

<a id="item-16"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://arstechnica.com/information-technology/2026/10/reactos-reaches-major-milestone-with-ntfs-install-support/">ReactOS 支持直接安装到 NTFS 分区，向 Beta 版迈进</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Ars Technica AI</span><span class="news-time">Oct 19, 18:30</span></div>
<p class="news-summary">ReactOS 现已支持直接将系统安装到 NTFS 分区上，不再像过去那样必须保留一个 FAT32 分区用于安装。据 Phoronix 报道，项目方将这一变化视为清除通往 Beta 版本道路上的一项长期障碍。 NTFS 几乎是所有现代 Windows 系统的默认文件系统，因此仅限 FAT32 安装一直是用户想在现有硬件上试用 ReactOS 时的实际障碍。这一限制的解除推进了该项目打造可用开源 Windows 兼容操作系统的长期目标，不过其意义主要面向操作系统爱好者和开源 OS 开发者，而非全行业的范式转变。 ReactOS 团队提醒，新的 NTFS 驱动仍缺少缓存机制（会导致性能较差），同时也尚未支持日志（journaling）和安全功能。团队在 X 上警告仍可能存在未被发现的 bug，因此即便是经验丰富的系统折腾者也要谨慎行事。</p>
<div class="news-background"><strong>背景</strong> ReactOS 是一个用 C 语言编写、以 GPL 2.0 授权的自由开源操作系统，目标是实现对为 Windows Server 2003 编写的应用程序和驱动的二进制兼容，并兼顾后续的 Windows NT 版本。NTFS 是微软开发的专有日志文件系统，其历史可追溯到 1993 年的 Windows NT 3.1，而 2001 年 Windows XP 引入的版本至今仍是主流标准。由于该项目旨在复现 Windows 环境，仅能使用 FAT32 分区与其目标显得格格不入。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ReactOS">ReactOS - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/NTFS">NTFS - Wikipedia</a></li>
<li><a href="https://github.com/reactos/reactos">reactos / reactos : A free Windows - compatible Operating System ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#ReactOS</span> <span class="tag">#NTFS</span> <span class="tag">#open-source OS</span> <span class="tag">#Windows compatibility</span> <span class="tag">#operating systems</span></div>
</article>
<hr>

<a id="item-17"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.theverge.com/ai-artificial-intelligence/1014045/coreweave-stock-debt-sector-ai">CoreWeave 债务跌入困境区间，震动整个 AI 行业</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">The Verge AI</span><span class="news-time">Oct 19, 21:28</span></div>
<p class="news-summary">按通行定义，CoreWeave 的债券已跌入困境区间——投资者要求的收益率比政府债券高出 1,000 个基点；公司股价自周二收盘以来已下跌超过 20%。在 Chamath Palihapitiya 点出这批困境债务、并质疑 AI 建设潮是否是一个私人信贷泡沫之后，此事受到更广泛的关注。 这种担忧并不局限于 CoreWeave：同期甲骨文股价下跌近 10%，其债券也遭到抛售，说明投资者认为那些大举借债建设 AI 基础设施的公司面临同样的风险。如果这些 neocloud 的融资成本进一步上升，整个行业靠债务驱动的 AI 建设将更难以为继。 截至第二季度财报，CoreWeave 负债超过 350 亿美元，上半年亏损超过 10 亿美元，而前三大客户贡献了第二季度近四分之三的收入。联合创始人 Brannin McBee 对《金融时报》表示，公司希望其债务达到投资级而非垃圾级，以便向保险公司借款，并称这些机构的资金是“无限的”——文章指出，这番表态反而让投资者担心 CoreWeave 会借更多的钱。</p>
<div class="news-background"><strong>背景</strong> Neocloud 是指专为 GPU 计算和 AI 工作负载（而非通用企业应用）构建的云服务商，CoreWeave 是最典型的代表：它把英伟达 GPU 及配套云服务出租给训练、微调和运行 AI 模型的公司。在信贷市场中，当债券收益率比无风险利率高出约 1,000 个基点，或以大幅低于面值的价格交易时，通常就被视为“困境债务”。CoreWeave 是较早把 GPU 用作贷款抵押物的公司之一，这使其融资成本与市场对 AI 热潮的信心紧密绑定。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.cisco.com/site/us/en/learn/topics/computing/what-is-neocloud.html">What is neocloud? - Cisco</a></li>
<li><a href="https://www.microsoft.com/en-us/startups/what-is-a-neocloud">What is a Neocloud? | Microsoft for Startups</a></li>
<li><a href="https://www.investopedia.com/terms/b/basispoint.asp">Basis Point: Meaning, Value, and Uses - Investopedia Junk Bonds Cross Into Distressed Territory: High-Yield Funds ... Distressed Securities: A Guide to High-Risk, High-Reward ... Distressed Debt and Special Situations Investing Explained Distressed Debt - Pluris Valuation Advisors Distressed Debt Investing for Accredited Investors 2026</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI infrastructure</span> <span class="tag">#CoreWeave</span> <span class="tag">#neoclouds</span> <span class="tag">#debt markets</span> <span class="tag">#industry analysis</span></div>
</article>
<hr>

<a id="item-18"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://jack-clark.net/2026/10/19/import-ai-477-in-which-i-tell-the-imf-the-singularity-has-begun/">Jack Clark 在 Import AI 477 中向 IMF 宣称“奇点”已经开始</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Import AI (Jack Clark)</span><span class="news-time">Oct 19, 12:31</span></div>
<p class="news-summary">在 Import AI 第 477 期中，Jack Clark 全文刊出了他于 10 月 17 日（周六）在曼谷 IMF 会议上发表的 Per Jacobsson 演讲，认为 AI 已处于“奇点”的早期阶段，经济学家、银行家和政策制定者应当预期到重大而迅速的变化。他表示将在后续几期中进一步展开讨论奇点的利害关系以及各方将面临的风险。 这场演讲把一位知名 AI 评论者的判断直接带给宏观经济政策圈，将 AI 定位为推动增长、人力资本与国家决策的力量，而不只是一则产品新闻，这可能会影响 IMF 及其成员国政府对该技术的规划方式。 刊出的文本仅为部分节选，Clark 也说明演讲中有些内容是即兴发挥、未被记录。可见的论证依托“思想的经济学”——即“好想法越来越难找”、研究成本不断上升——并提出如果 AI 能成倍扩充研究者数量、缩短培养时间会带来什么，同时呼吁有意识地控制发展节奏并保持“克制”。</p>
<div class="news-background"><strong>背景</strong> Import AI 是 Jack Clark 长期运营的 AI 研究资讯通讯，本期以一场演讲为核心，而非惯常的论文摘要。Per Jacobsson 演讲是在 IMF 会议上发表的冠名演讲，其听众是经济学家与央行人士，他们通常并不接触关于变革性 AI 的主张。在这一语境下，“奇点”指的是 AI 系统达到能力快速、自我强化式增长，从而根本改变经济与社会的那个临界点。</div>
<div class="news-tags"><span class="tag">#AI policy</span> <span class="tag">#AI economics</span> <span class="tag">#AGI/singularity</span> <span class="tag">#commentary</span> <span class="tag">#newsletter</span></div>
</article>
<hr>

<a id="item-19"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.calabro.io/ohbf">单哈希 Bloom Filter,以及来自 Bluesky 的锁竞争经验</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 19, 15:47</span></div>
<p class="news-summary">Jim Calabro 发表了一篇关于单哈希 Bloom Filter(OHBF)的技术文章,介绍了如何仅用一个哈希函数构建 Bloom Filter,其思路来自 Lu 等人的论文:把位数组拆成 k 个两两互质的分区。文中还回顾了 Bluesky 的实践经验——他的同事 Jasmine fork 了原有库并做出 atomic-bloom,用原子 CPU 指令替代互斥锁,使部署时间从约 90 分钟降到约 15 分钟。 Bloom Filter 位于许多高性能数据系统的热路径上;在 Bluesky,据称它们针对 Scylla 每秒省下数百万次查询,用于 block、mute、label 等查找,其中一个过滤器的阳性率约为 1%,也就是 99% 的查找可以完全跳过数据库。减少哈希函数数量、消除锁竞争,直接关系到这类系统能以多低的成本扩展,因此这篇文章对运行大规模有状态后端的人很有参考价值。 单哈希方案把位数组拆成 k 个两两互质的分区;再加上类似 Daniel Lemire 的技巧——用一条 MUL 指令而非昂贵的取模运算来选定要检查的块——作者称最坏情况下一次查找只需一次 cache miss。作者明确说明,这一优化在 Bluesky 并未带来可测量的提速,因为按 Amdahl 定律,瓶颈是锁竞争而不是哈希计算;文中还介绍了 ShardedAtomicFilter,把写操作分散到多个分片以进一步降低竞争。</p>
<div class="news-background"><strong>背景</strong> Bloom Filter 是一种概率型数据结构,用「肯定不在」或「可能在」来回答「键 X 是否在这个集合里」,其实现是一个位数组加 k 个哈希函数,参数按目标误判率来设定。它相对于集合基数占用的内存极小、计算开销很低,因此数据库常在内存中维护一个,在真正做慢速磁盘 I/O 之前先做检查。Bluesky 是一个基于 AT Protocol(atproto)的分布式社交网络,其后端大量使用 Bloom Filter 做成员判断,例如某个用户是否屏蔽了另一个用户。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://calabro.io/ohbf">One Hash Bloom Filters - Jim Calabro</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bloom_filter">Bloom filter - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/AT_Protocol">AT Protocol - Wikipedia</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#bloom filters</span> <span class="tag">#probabilistic data structures</span> <span class="tag">#performance optimization</span> <span class="tag">#hashing</span> <span class="tag">#systems design</span></div>
</article>
<hr>

<a id="item-20"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://blog.torproject.org/tor-vpn-beta/">Tor VPN Beta 分享从零构建 Android VPN 的经验</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 19, 08:27</span></div>
<p class="news-summary">Tor Project 发布博客，回顾在从零打造 Tor VPN Beta（其首个面向 Android 的设备级 Tor 保护产品）过程中的经验；该产品去年秋季以限量形式首发，如今以 APK、Google Play 和 F-Droid 三种渠道分发。文章介绍了若干设计取舍，例如让每个手机应用使用独立的 Tor 电路、在 1.4.0 beta 版中优先加入 WebTunnel 网桥，以及基于 Rust 编写的新一代 Tor 实现 Arti 进行构建。 Tor Browser 的保护只覆盖浏览行为，而整机 VPN 把 Tor 扩展到即时通讯、社交媒体和邮件等应用；文章指出，其用户明显集中在伊朗、土库曼斯坦等审查严格的地区，而非全球北方国家。这一分布说明设备级 Tor 可能对每天面对网络限制的人最有价值，也指明了项目后续在反审查方向上的投入重点。 Tor VPN 构建在 Arti 之上，而非传统的 C 实现；它不使用单一共享隧道，而是让设备上每个应用各自处于独立 Tor 电路中，使一个应用的活动难以与另一个关联。1.4.0 beta 加入了 WebTunnel 网桥，可让 Tor 流量看起来像普通的加密网页流量；文章也指出，当前的安全属性与已知局限记录在单独的威胁模型文档中。</p>
<div class="news-background"><strong>背景</strong> Tor 是一个由志愿者运营的匿名网络，通过多台中继转发流量，使任何单点都无法同时知道使用者身份和所访问的内容。在审查严格的网络中，直连 Tor 常被封堵，因此项目维护了“网桥”（bridge）——不易被审查者识别的非公开入口节点；WebTunnel 是较新的一类网桥，把 Tor 连接伪装成普通的 HTTPS 网页流量。Arti 则是 Tor Project 用 Rust 语言重写的 Tor 协议实现，目标是提供比原有 C 代码库更易维护的基础。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://blog.torproject.org/introducing-webtunnel-evading-censorship-by-hiding-in-plain-sight/">Hiding in plain sight: Introducing WebTunnel | The Tor Project</a></li>
<li><a href="https://support.torproject.org/tor-browser/circumvention/using-bridges/">Using bridges - Censorship circumvention - Tor Browser — Tor</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Tor</span> <span class="tag">#VPN</span> <span class="tag">#Android</span> <span class="tag">#privacy</span> <span class="tag">#censorship circumvention</span></div>
</article>
<hr>

<a id="item-21"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://media.ccc.de/v/emf2026-240-1-men-in-tech-yesallmen">演讲实录：一位女性讲述 tech 行业中的性别歧视与骚扰</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 18, 18:35</span></div>
<p class="news-summary">在 media.ccc.de 演讲平台上发布的一场题为“Men in tech #YesAllMen”的会议演讲中，一位女性讲述了自己在 tech 职业生涯中亲身经历的、来自男性同事的性别歧视与骚扰，其中还包括一位被告知“太有价值、不宜斥责”的同事发来的辱骂信息。演讲者没有提出解决方案，而是明确把责任交给在场的男性听众，要求他们正视并处理身边的这种文化。 这场演讲直接批评了那些教导女性如何提升自信、如何谈判、如何增强韧性的“Women in tech”座谈会——这类活动隐含地把问题框定为女性只要更努力就能解决的事。演讲者坚持认为问题应由男性承担，从而把讨论的焦点从女性的自我提升转向职场问责和软件工程团队中的日常文化。 这场演讲被设定为一段令人不适的、原话实录式的叙述，讲述一名男性同事在一个职业生涯中对一位女性实际说过和做过的事，开场即引用了一条辱骂信息，演讲者还明确表示自己不会给出解决方案。它是个人叙事而非研究或调查，因此不提供统计数据；该录像以 CC BY-SA 4.0 许可发布。</p>
<div class="news-background"><strong>背景</strong> 标题中的 #YesAllMen 标签，源自对“not all men”（并非所有男人都如此）这一反驳的回应——其论点是：正因为有一部分男性会骚扰女性，女性在与所有男性相处时都不得不把这种风险考虑进去。“Women in tech”座谈是会议中常见的环节，用以讨论行业的性别失衡问题，但批评者认为这类活动往往聚焦于女性应如何适应，而非同事的行为本身。该演讲在会议上录制，并发布在 media.ccc.de——Chaos Computer Club 用于公开发布演讲录像的媒体平台。</div>
<div class="news-tags"><span class="tag">#tech culture</span> <span class="tag">#sexism</span> <span class="tag">#harassment</span> <span class="tag">#diversity</span> <span class="tag">#conference talk</span></div>
</article>
<hr>

<a id="item-22"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://lwn.net/Articles/1101143/">Linux 7.3 发布，成为创纪录的内核开发周期</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 19, 08:13</span></div>
<p class="news-summary">Linus Torvalds 宣布 Linux 7.3 内核正式发布，他称这个版本在各个方面都创下纪录：共合入 18,765 个非合并提交，来自 3,021 位开发者，其中 807 人是首次参与内核开发的贡献者。随着最终版本释出，Linux 7.4 的合并窗口随即开启，不过 Torvalds 提到自己正处于年度家庭休假中，因此接下来一段时间的合并节奏会不太寻常。 每一个下游发行版和厂商内核最终都会基于新的主线内核重新基线化，因此新版本的功能集决定了未来几个月用户和管理员能用上什么。本次周期既以空前的贡献者规模引人注目，也完成了 sched_ext 等长期推进的工作，并为 ntfs3 带来备用数据流支持。 Torvalds 重点提及的改动包括：binfmt_misc 的重要扩展、旨在提升大型系统性能的组调度工作、一个会对所有操作都返回失败的新文件系统 failfs、fchroot() 系统调用、BPF 程序的全局 per-CPU 数据、sched_ext 子调度器特性的完成、虚拟机的 working-set 跟踪、ntfs3 的备用数据流支持，以及一长串 SMB 服务器改进。更详细的说明可参阅 LWN 的合并窗口总结（第一部分和第二部分）以及 KernelNewbies 的 7.3 页面。</p>
<div class="news-background"><strong>背景</strong> Linux 内核开发遵循固定节奏：先是为期约两周的合并窗口，各子系统维护者把新工作送入主线树，随后发布一系列候选版本进行测试，最后才发布正式版。本次发布提到完成的 sched_ext 是一种调度器类，它允许用 BPF 程序实现内核线程调度器并从用户空间动态加载或卸载，从而无需打补丁和重新编译内核即可试验调度策略。ntfs3 是内核中面向微软 NTFS 文件系统的驱动，而备用数据流（ADS）是 NTFS 的一项特性，允许一个文件在默认数据流之外携带额外的命名数据流；它最初用于存放元数据和兼容性目的，但也因这些额外数据流在普通目录列表中不可见而成为公认的安全隐患。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.kernel.org/doc/html/next/scheduler/sched-ext.html">Extensible Scheduler Class — The Linux Kernel documentation</a></li>
<li><a href="https://github.com/sched-ext/scx">GitHub - sched-ext/scx: sched_ext schedulers and tools Overview - sched_ext sched_ext (BPF Scheduling) - Linux Kernel Internals linux/Documentation/scheduler/sched-ext.rst at master ... EXAMPLE SCHEDULERS | sched_ext sched-ext Tutorial | CachyOS</a></li>
<li><a href="https://developer.ibm.com/articles/alternate-data-streams/">Alternate data streams and cybersecurity vulnerabilities</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#linux</span> <span class="tag">#kernel</span> <span class="tag">#release</span> <span class="tag">#open-source</span> <span class="tag">#filesystems</span></div>
</article>
<hr>

<a id="item-23"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.seangoedecke.com/what-requirements-dont-you-have/">优雅的设计来自你「不需要」的那些需求</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 19, 02:59</span></div>
<p class="news-summary">在 seangoedecke.com 的一篇博文中，作者提出：明确说出哪些需求是可以妥协的——哪些可以慢、可以陈旧、可以不够灵活——往往是做出优雅软件设计的关键。他还补充了一个新角度：在与能力强大的 coding agent 协作时，这种能力变得尤为重要，因为模型往往会去满足那些从未被要求的、假想出来的需求。 这篇文章把设计判断力重新定义为「有意识地放弃某些需求」，而不是把所有需求都满足，这也解释了为什么独立开发者或创业公司有时能在设计上胜过每个人都寸步不让的大公司。随着越来越多团队把实现工作交给 coding agent，判断哪些约束其实可有可无，可能会成为一项核心技能——它决定了 AI 生成的代码是保持简洁，还是被不必要的防护逻辑撑得臃肿。 文中给出了具体例子：Unicorn 因为没有共享可变状态而白得进程隔离，又因为放弃处理慢客户端而能把请求直接排进 Unix socket；S3 不支持原子的多键更新，因此 blob 可以独立存储和扩展；StatsD 默认走 UDP，以容忍数据丢失换取更低的网络开销；SQLite 则用放弃并发写换来「单文件即可运行」的运维简洁性。作者还提到，LLM 常常未经要求就引入互斥锁或检查逻辑来保持两份半相关的数据同步；他也观察到反向情况：工程师坚持「完美」系统，而产品经理拼命说服其接受一定程度的数据陈旧。</p>
<div class="news-background"><strong>背景</strong> Unicorn 这类 preforking Web 服务器启动后会先加载应用，再 fork 出固定数量的 worker 进程，因此每个请求都在隔离的进程中处理，而不是共享线程池。分布式存储系统在原子性上面临类似取舍：要支持跨多个 key 的事务，就必须在分区之间做协调，代价是延迟和可扩展性。TOCTOU（time-of-check to time-of-use，检查时与使用时）是一类竞态条件——资源在被校验之后、被使用之前发生了变化，而这正是 agent 可能试图用额外加锁去堵上的那种边界情况。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://yhbt.net/unicorn/DESIGN">yhbt.net/ unicorn /DESIGN</a></li>
<li><a href="https://stackoverflow.com/questions/25834333/what-exactly-is-a-pre-fork-web-server-model?lq=1">apache - What exactly is a pre - fork web server model? - Stack Overflow</a></li>
<li><a href="https://aiq.hu/en/32-4-2-toctou-time-of-check-time-of-use-vulnerabilities/">32.4.2 TOCTOU ( Time - of - Check - Time - of - Use ) vulnerabilities</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 作者提到这篇文章在 Lobsters 上获得了不错的讨论，最高赞评论者链接了另一篇博文，把那类针对边界情况的需求修补称为「epicycles（本轮）」。作者认为这个说法很贴切，正好形容为了应付假想约束而硬加上去的多余机制。</div>
<div class="news-tags"><span class="tag">#software design</span> <span class="tag">#requirements engineering</span> <span class="tag">#coding agents</span> <span class="tag">#engineering judgment</span> <span class="tag">#AI-assisted development</span></div>
</article>
<hr>

<a id="item-24"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://servo.org/blog/2026/10/09/august-in-servo/">Servo 0.6.0 默认启用 CSS Grid，并新增文本选择支持</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 18, 23:05</span></div>
<p class="news-summary">Servo 0.6.0 汇总了 8 月合入的全部 417 个提交，其中最引人注目的是默认开启 CSS Grid 支持（@nicoburns，#45621），团队表示这对许多网站的外观带来了很大的正面改善。该版本还改进了文本选择，并新增了一批 Web 平台特性，包括 touch-action、animation-composition、color-scheme、text-transform 的 full-width、math-akto 之外的新取值（full-width、math-auto、full-size-kana），以及 focusin/focusout 事件、Location 上的 ancestorOrigins、BaseAudioContext 上的 PeriodicWave 等 DOM API。 CSS Grid 是大量现代网站依赖的基础二维布局特性，默认启用它意味着 Servo 从只能渲染简单页面迈向能够渲染主流网页。这对浏览器引擎开发者、在桌面、移动和嵌入式应用中嵌入 Servo 的开发者，以及关注 Blink、Gecko、WebKit 之外基于 Rust 的开源替代方案的人来说都很重要。 除新特性外，该版本还重构了导航、文档加载和会话历史——团队称这些是 HTML 规范中最棘手的部分——使打开新窗口或嵌入 iframe 的页面表现更可靠。性能方面移除了大量不必要的内存分配并减少了 GC 交互以提升 JS 性能；在 macOS、OpenHarmony 等平台利用内存映射字体数据，使字体文件加载不再处于引擎启动的关键路径上。</p>
<div class="news-background"><strong>背景</strong> Servo 是一个用 Rust 编写的实验性浏览器引擎，2012 年在 Mozilla 启动，如今由 Linux Foundation Europe 治理，开发工作主要由 Igalia 和社区贡献者推动。CSS Grid 是一种 CSS 布局系统，允许开发者显式定义行和列来实现二维布局；缺少它时，许多现代网站的渲染会出错或退化为错乱布局。Servo 每月发布更新日志汇总已合入的工作，其部分组件（如 url、html5ever、selectors、cssparser）也被其他 Rust 项目使用。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Servo_browser_engine">Servo browser engine</a></li>
<li><a href="https://servo.org/">Servo aims to empower developers with a lightweight...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Servo</span> <span class="tag">#browser engine</span> <span class="tag">#CSS Grid</span> <span class="tag">#web platform</span> <span class="tag">#open source</span></div>
</article>
<hr>