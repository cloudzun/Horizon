---
layout: default
title: "Horizon 每日速递：2026-08-24"
date: 2026-08-24
lang: zh
---

> 📅 2026-08-24 · 从 62 条资讯中精选出 27 条重要内容

---

1. [微软画图和照片为图片添加带 GUID 的隐形水印](#item-1) <span class="score-badge score-mid">8.0</span>
2. [海洋温度创历史新高，气候变化加剧](#item-2) <span class="score-badge score-mid">8.0</span>
3. [seL4 在 AArch64 上的安全证明已完成](#item-3) <span class="score-badge score-mid">8.0</span>
4. [AI 编程可能阻碍开发者专业能力：Lars Faye 的观点](#item-4) <span class="score-badge score-mid">8.0</span>
5. [你的可执行文件就是一个 SQLite 数据库](#item-5) <span class="score-badge score-mid">8.0</span>
6. [FDA 批准阿尔茨海默病血液检测](#item-6) <span class="score-badge score-mid">8.0</span>
7. [Emacs 31\.1 发布：提供签名压缩包与校验和](#item-7) <span class="score-badge score-mid">8.0</span>
8. [Mozilla 宣布计划在 Firefox 中支持 JPEG XL](#item-8) <span class="score-badge score-mid">8.0</span>
9. [AI 代理逆向工程外设，暴露隐藏 Shell 与 LED 控制风险](#item-9) <span class="score-badge score-mid">8.0</span>
10. [LLM 驱动的开发暴露出控制与复杂性之间的张力](#item-10) <span class="score-badge score-mid">8.0</span>
11. [小米 XRing O3 芯片单核比肩苹果，多核性能宣称更强](#item-11) <span class="score-badge score-mid">7.0</span>
12. [旧金山全城被还原成可玩的 3D 网页游戏](#item-12) <span class="score-badge score-mid">7.0</span>
13. [Shipyard 团队逐步退出 IPFS 支持，项目继续](#item-13) <span class="score-badge score-mid">7.0</span>
14. [欧洲如何扼杀创客与微型创业者](#item-14) <span class="score-badge score-mid">7.0</span>
15. [OpenAI 下调 GPT\-5\.6 Sol 价格，有效期至 2026 年 11 月](#item-15) <span class="score-badge score-mid">7.0</span>
16. [保罗·格雷厄姆：如果我是 17 岁，我会从零开始构建 LLM](#item-16) <span class="score-badge score-mid">7.0</span>
17. [Anthropic 最强 AI 模型遇冷，更便宜模型支出占比更高](#item-17) <span class="score-badge score-mid">7.0</span>
18. [Fable 的高成本终结了 AI 编程的免费午餐](#item-18) <span class="score-badge score-mid">7.0</span>
19. [林纳斯·托瓦兹称赞 AI 助手在‘地狱级调试’中的帮助](#item-19) <span class="score-badge score-mid">7.0</span>
20. [儿童比 AI 学语言更强——原因仍是谜](#item-20) <span class="score-badge score-mid">7.0</span>
21. [Import AI 470：机器无权利、SPADE 环境生成与 Hawkeye GPU 内核优化](#item-21) <span class="score-badge score-mid">7.0</span>
22. [政治危机中紧急警报被滥用的风险](#item-22) <span class="score-badge score-mid">7.0</span>
23. [用户花费 266 美元借四个 AI 模型解锁亚马逊 Fire 平板](#item-23) <span class="score-badge score-mid">7.0</span>
24. [为何现代 TUI 是辅助功能的噩梦？](#item-24) <span class="score-badge score-mid">7.0</span>
25. [Emacs Canvas 功能历经八个月后合并入上游](#item-25) <span class="score-badge score-mid">7.0</span>
26. [有限状态模型检查转向确定性模拟测试](#item-26) <span class="score-badge score-mid">7.0</span>
27. [构建 certgrep\.sh：免费证书透明度正则搜索引擎](#item-27) <span class="score-badge score-mid">7.0</span>

---

<a id="item-1"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/">微软画图和照片为图片添加带 GUID 的隐形水印</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">ComputerGuru</span><span class="news-time">Aug 24, 15:28</span></div>
<p class="news-summary">xusheng.dev 的博客文章揭示，Microsoft Paint 和 Microsoft Photos 会在图片中静默嵌入基于 GUID 的隐形水印，即使 AI 编辑是使用本地模型在本地执行的。文章称，可见的 AI 水印可以关闭，但隐形水印无法禁用。 此事之所以重要，是因为这个隐形唯一标识符可能被追溯到用户的 Microsoft 账户，从而引发严重的隐私和匿名性问题。它影响到所有使用 Windows 内置图片工具进行 AI 编辑的用户，并加剧了 AI 内容溯源与用户隐私之间的争论。 水印即使在本地模型执行 AI 操作时也会被嵌入，目前尚不清楚 AI 增强的背景移除等功能是否同样会触发水印。据博客文章和社区反馈，隐形水印是基于 GUID 的标识符，不同于可关闭的可见 Copilot 水印，它无法被禁用。</p>
<div class="news-background"><strong>背景</strong> 隐形水印（invisible watermarking）是一种在不明显改变图像外观的情况下将隐藏标识符嵌入数字图像的技术，常用于追踪来源或验证 AI 生成内容的真实性。GUID（全局唯一标识符）是一个 128 位数字，用于跨系统唯一标识对象；在此场景中，它可作为可追踪到用户或会话的标识。为 AI 生成的图像添加水印已成为常见做法——例如 Google 的 SynthID 会为其 AI 工具生成的图像添加隐形签名——但在本地运行的消费级软件中静默执行这一操作，则会引发不同的隐私和同意问题。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Universally_unique_identifier">Universally unique identifier - Wikipedia</a></li>
<li><a href="https://www.scoredetect.com/blog/posts/invisible-watermarking-for-ai-generated-images">Invisible Watermarking for AI - Generated Images | ScoreDetect Blog</a></li>
<li><a href="https://www.aifreeapi.com/en/posts/synthid-watermark-ai-images">Why Do AI Images Have SynthID Watermarks ? | AI Free API</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者普遍对静默插入唯一标识符表示担忧，有人认为真正的问题在于这对互联网匿名性的威胁，并且向微软发出传票就可能获取与账户关联的个人数据。其他人则提到误报案例——一位用户在调整截图大小时看到 AI 水印提示并转而使用 Paint.net——还有人回忆起微软曾错误地为非 AI 提交加盖 Copilot 水印的事件，因此建议避免使用 Paint 及其他集成 LLM 的应用。也有少数人认同隐私担忧，同时提醒说，通过水印保留人类真实性的价值也值得考虑。</div>
<div class="news-tags"><span class="tag">#privacy</span> <span class="tag">#watermarking</span> <span class="tag">#microsoft</span> <span class="tag">#AI-generated content</span> <span class="tag">#security</span></div>
</article>
<hr>

<a id="item-2"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.bbc.com/news/articles/c62m4gpnp78o">海洋温度创历史新高，气候变化加剧</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">tcp_handshaker</span><span class="news-time">Aug 24, 19:19</span></div>
<p class="news-summary">这则 BBC 新闻称，全球海洋温度已达到有记录以来的最高水平。这一纪录凸显了气候变化正在加速。 由于海洋吸收了温室气体排放产生的大部分额外热量，海洋温度创纪录是全球变暖的有力指标。这对全球海洋生态系统、天气模式以及沿海社区都会产生深远影响。 目前可用的摘要没有提供具体的温度数值或创纪录的确切日期，但直接将这一里程碑与气候变化加速联系起来。这则新闻也出现在关于厄尔尼诺和潜在气候反馈回路的讨论背景下。</p>
<div class="news-background"><strong>背景</strong> 海洋覆盖地球表面超过 70%，吸收了温室气体导致的约 90%的额外热量，因此海洋温度是关键的 climate 指标。即使平均温度小幅上升，也可能扰乱海洋生物、加剧飓风并加速冰层融化。厄尔尼诺等自然模式可能会在长期变暖趋势之上暂时进一步推高海洋温度。</div>
<div class="news-discussion"><strong>社区讨论</strong> 评论者对政府不作为表示不满，尤其是美国，他们认为美国正在扩大化石燃料开采并打压可再生能源。也有评论者反思微小的温度上升可能带来严重气候影响，预计假期前后厄尔尼诺效应会加剧，并讨论了海洋变暖引发碳循环反馈回路的风险。</div>
<div class="news-tags"><span class="tag">#climate-change</span> <span class="tag">#ocean-temperature</span> <span class="tag">#environment</span> <span class="tag">#science</span></div>
</article>
<hr>

<a id="item-3"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://proofcraft.systems/news-2026/#2026-08-21">seL4 在 AArch64 上的安全证明已完成</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">snvzz</span><span class="news-time">Aug 24, 11:32</span></div>
<p class="news-summary">Proofcraft Systems 宣布，seL4 微内核的正式安全证明已于 2026 年 8 月在 AArch64（64 位 ARM）架构上完成。目前验证的配置仅限于单核（unicore）、非 MCS（混合关键性系统）构建。 这是形式化验证的一个重要里程碑，将 seL4 基于数学证明的安全保证扩展到广泛使用的 64 位 ARM 平台。它增强了在安全关键型和嵌入式系统中采用 seL4 的理由，但单核和非 MCS 限制划定了当前的可信边界。 已完成的安全证明涵盖 AArch64 上 seL4 的核心安全属性，但尚不包含 MCS 调度或多核配置。正如公告中的细则所指出的，当前证明仅适用于单核、非 MCS 构建。</p>
<div class="news-background"><strong>背景</strong> seL4 是 L4 系列第三代微内核，由 NICTA（现为 CSIRO 旗下 Data61 的一部分）开发，旨在为安全系统提供高可信基础。形式化验证使用数学工具和证明来表明软件实现满足其形式规范，提供比单纯测试更强的保证。这一里程碑将此类保证扩展到了 AArch64——广泛用于移动、嵌入式和服务器设备的 64 位 ARM 指令集架构。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SeL4">seL4 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/L4_microkernel_family">L4 microkernel family - Wikipedia</a></li>
<li><a href="https://sel4.systems/">The seL4 Microkernel | seL4</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者的反应既有赞赏也有谨慎：有人调侃说侧信道时序攻击可能很快会让这项证明失效，也有人指出其限制是“非 MCS、单核”。还有人讨论实际部署，如 GenodeOS、LionsOS 以及一家中国车企的 hypervisor 使用案例；另有评论认为，seL4 需要原生 seL4/Linux 方案才能真正改善系统安全。</div>
<div class="news-tags"><span class="tag">#seL4</span> <span class="tag">#formal verification</span> <span class="tag">#microkernel</span> <span class="tag">#AArch64</span> <span class="tag">#security</span></div>
</article>
<hr>

<a id="item-4"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://larsfaye.com/articles/ai-coding-will-prevent-expertise">AI 编程可能阻碍开发者专业能力：Lars Faye 的观点</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 24, 16:20</span></div>
<p class="news-summary">软件开发人员 Lars Faye 在新文章中指出，AI 编程助手消除了长期技能形成所必需的关键摩擦，培养出他所说的“专家型新手”（expert novices），难以建立深厚的专业能力。他建议把 LLM 当作苏格拉底式切磋伙伴而非答案生成器，并引用宾夕法尼亚大学的研究：AI 辅助练习使成绩提高 127%，但测试成绩与仅用教科书的对照组大致相同。 这篇文章触及行业日益担忧的问题：AI 生成的代码正以超过人工审查速度的速度被产出，而恰在此时许多公司开始强制使用 AI 编码工具。它可能改变团队培养初级开发者的方式、企业衡量生产率的标准，以及行业在追求速度与培养长期专业能力之间如何取舍。 Faye 在其先前提出的“熟练编排者悖论”（skilled orchestrator paradox）基础上展开论述：管理 AI 编程智能体所需的技能，恰恰是长期使用这些智能体会削弱的能力。他还引用 François Chollet 的观点——LLM 是“插值引擎”（interpolation engines），无法应对全新的系统故障——并警告说，专业技能需要主动、持续地参与才能形成，即使这意味着进展更慢。</p>
<div class="news-background"><strong>背景</strong> AI 编程助手是基于大型语言模型（LLM）的软件工具，可帮助程序员生成、补全和审查代码；而“智能体编码”（agentic coding）更进一步，由自主智能体在很少人工干预的情况下规划、编写、测试和修改代码。文章认为，依赖这类工具会消除历史上帮助开发者建立直觉和专业能力的挣扎与摩擦。ARC-AGI 是一个旨在通过无法靠记忆解决的谜题来衡量通用智能的基准测试，这正是 Chollet 关于“插值引擎”的评论成为文章核心论据的原因。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/agentic-coding">What is Agentic Coding? | IBM</a></li>
<li><a href="https://arcprize.org/arc-agi">ARC Prize - What is ARC-AGI?</a></li>
<li><a href="https://www.databricks.com/blog/what-are-large-language-models">What are Large Language Models (LLM)? | Databricks</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 评论者大多认同文章的核心论点，有人描述了现实后果：企业强制要求不再手写代码，导致代码产出速度快于人工审查能力，审查者不得不面对大量质量不佳的 AI 生成代码。也有评论提出更细致的看法，认为主动寻求挑战的人会从其他地方获得锻炼，还有人指出 AI 可能会让具备领域知识的通才比“纯”软件工程师更受重视。</div>
<div class="news-tags"><span class="tag">#AI coding</span> <span class="tag">#software engineering</span> <span class="tag">#expertise</span> <span class="tag">#LLM</span> <span class="tag">#developer productivity</span></div>
</article>
<hr>

<a id="item-5"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://fzakaria.com/2026/08/23/your-executable-is-a-sqlite-database">你的可执行文件就是一个 SQLite 数据库</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 24, 07:32</span></div>
<p class="news-summary">在一篇新的博文中，sqlelf 的作者提出了 SELF（Structured Executable &amp; Linkable Format，结构化可执行与可链接格式），用 SQLite 数据库取代 ELF 作为可执行文件格式。该原型可直接把 SQLite 文件当作程序运行，支持静态与动态链接，并且可以在 ELF 与 SELF 之间无损往返转换。 这是对支撑类 Unix 系统数十年的基础格式的一种激进反思。如果可行，基于 SQLite 的可执行文件可以让二进制文件自我描述、可查询、并在运行时修改，从而促成原子化的按文件 LD_PRELOAD 修改和深度二进制检视等全新工作流。 原型包含 self-exec 解释器，它链接 libsqlite3，从数据库中获取程序头和符号；为避免无限递归，它本身必须保持为 ELF 文件。动态链接有两种实现方式：要么使用可感知 SQL 的 ld.so 替代品，要么借助 glibc 的 rtld-audit 接口；作者演示了通过修改 &#x27;preload&#x27; 表来改变程序行为而无需重新链接。项目位于 fzakaria/selfdb，并可在 NixOS 虚拟机中体验。</p>
<div class="news-background"><strong>背景</strong> ELF（Executable and Linkable Format，可执行与可链接格式）是 Linux 及许多类 Unix 系统上可执行文件、目标代码和共享库的标准二进制格式。它将数据组织为节（sections）和程序头（program headers），程序头描述段（segments）应如何加载到内存中，运行时通常由动态链接器 ld.so 处理。Nix 是一种声明式包管理器，支持可重现构建和整机系统配置；作者用它来探索激进替代方案而不影响现有系统。这篇文章延续了作者早前工具 sqlelf 的思路，后者曾把 ELF 内部结构暴露为 SQLite 虚拟表。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Executable_and_Linkable_Format">Executable and Linkable Format - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nix_(package_manager)">Nix (package manager) - Wikipedia</a></li>
<li><a href="https://linux.die.net/man/8/ld.so">ld.so (8): dynamic linker/loader - Linux man page Ubuntu Manpage: ld.so, ld-linux.so* - dynamic linker/loader Ubuntu Manpage: ld.so, ld-linux.so* - dynamic linker/loader A look at dynamic linking - LWN.net ld.so (8) — Linux manual pages - Litux ld.so/ld-linux.so - dynamic linker/loader</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 上的讨论总体上很热烈，评论者赞赏 SQLite 虚拟表的优雅，并建议将其与 Lisp 镜像或 AppImage 式分发结合。有评论者认为广义上 ELF 本身就是一种数据库；作者则表示，当作论文投稿时，学术审稿人对此想法并不怎么买账。</div>
<div class="news-tags"><span class="tag">#SQLite</span> <span class="tag">#ELF</span> <span class="tag">#executable format</span> <span class="tag">#Nix</span> <span class="tag">#systems programming</span></div>
</article>
<hr>

<a id="item-6"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://medicine.washu.edu/news/fda-clears-blood-test-to-aid-evaluation-for-alzheimers-disease/">FDA 批准阿尔茨海默病血液检测</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">dabinat</span><span class="news-time">Aug 24, 06:30</span></div>
<p class="news-summary">FDA 已批准 PrecivityAD2 血液检测，该检测通过测量 p-tau217 生物标志物来辅助评估阿尔茨海默病，旨在帮助临床医生在出现认知症状的患者中确认或排除阿尔茨海默病。 此次批准为阿尔茨海默病评估提供了一种比 PET 扫描或腰椎穿刺创伤更小、更易获得的替代方案，可能扩大早期筛查和诊断，从而改变患者的评估方式和时机。 PrecivityAD2 的定价约为 1,400-1,500 美元，研究表明其在有认知症状的人群中识别阿尔茨海默病的准确率约为 90%。该检测经分析和临床验证，可帮助在轻度认知障碍或痴呆患者中确认或排除阿尔茨海默病。</p>
<div class="news-background"><strong>背景</strong> 阿尔茨海默病通常通过认知测试、淀粉样斑块成像或脑脊液分析来诊断。P-tau217 是一种基于血液的生物标志物，可反映与阿尔茨海默病相关的脑部变化，如淀粉样斑块和 tau 蛋白病变。基于该标志物的血液检测与 PET 成像和脑脊液生物标志物高度一致，为初级保健等领域提供了更具可扩展性的选择。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.laverty.com.au/tests/precivityad2">Alzheimer’s disease and PrecivityAD 2 ™ blood test | Laverty Pathology</a></li>
<li><a href="https://www.aol.com/blood-test-shows-90-accuracy-094300001.html">Blood test shows 90% accuracy in identifying Alzheimer&#x27;s disease - AOL</a></li>
<li><a href="https://healthmatters.io/understand-blood-test-results/p-tau217">P-tau217 Blood Test: Normal Range, Results Explained, and ...</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者审视了该检测的预测价值和成本效益，指出 p-tau217 水平极高者 5 年内进展风险为 38%，而低水平者为 12%，并质疑约 1,400-1,500 美元的定价是否比 200-300 美元的更便宜替代方案更有价值。其他人则争论该检测是否会改变人们的评估时机、检测阳性者是否存在经证实的干预措施，以及 FDA 为何为一项无害的血液检测进行审批。</div>
<div class="news-tags"><span class="tag">#alzheimers</span> <span class="tag">#fda</span> <span class="tag">#blood-test</span> <span class="tag">#biomarker</span> <span class="tag">#healthcare</span></div>
</article>
<hr>

<a id="item-7"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://lists.gnu.org/archive/html/info-gnu-emacs/2026-08/msg00004.html">Emacs 31.1 发布：提供签名压缩包与校验和</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 24, 10:52</span></div>
<p class="news-summary">Emacs 31.1 于 2026 年 8 月 24 日正式发布，.tar.gz 和 .tar.xz 压缩包已可从 GNU 镜像站获取。发布公告中附带了 PGP 签名和 SHA-256/SHA-512 校验和，供用户验证真实性与完整性。 作为使用最广泛的开源文本编辑器之一的主版本发布，Emacs 31.1 带来的新特性和变化将影响庞大的技术用户群体。软件工程师和 Emacs 爱好者很可能会升级并调整其工作流程以适应新版本。 该版本为两种压缩包格式都提供了 PGP 签名文件，公钥为 8DC2487E51ABDD90B5C4753F0F56D0553B6D411B。用户可通过 etc/NEWS 文件查看完整的变更摘要，在 Emacs 内输入 &#x27;C-h n&#x27; 即可访问。</p>
<div class="news-background"><strong>背景</strong> Emacs 是一款可扩展的文本编辑器，数十年来一直是 GNU 项目的组成部分。PGP 签名可让用户验证下载的文件确实由维护者签名且未被篡改。SHA 校验和是根据文件内容计算的哈希值，在从镜像站下载后可进一步确认文件完整性。公告中还列出了公共 OpenPGP 密钥服务器，这些服务器是获取发布签名公钥的公共目录。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pretty_Good_Privacy">Pretty Good Privacy - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Key_server_(cryptographic)">Key server (cryptographic) - Wikipedia</a></li>
<li><a href="https://manifold.net/doc/mfd9/using_sha_checksums.htm">Using SHA Checksums</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#emacs</span> <span class="tag">#release</span> <span class="tag">#open-source</span> <span class="tag">#text-editor</span> <span class="tag">#gnu</span></div>
</article>
<hr>

<a id="item-8"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://hacks.mozilla.org/2026/08/intent-to-ship-jpeg-xl/">Mozilla 宣布计划在 Firefox 中支持 JPEG XL</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 24, 16:25</span></div>
<p class="news-summary">Mozilla 在 Mozilla Hacks 博客上发布了关于下一代图像格式 JPEG XL 的“Intent to Ship”公告，表明 Firefox 正准备实现该编解码器。 如果实现，Firefox 对 JPEG XL 的支持将为大型浏览器带来一种现代、开放图像格式，可能推动其在网页中的采用，并为用户带来更好的压缩、HDR 和广色域图像。 JPEG XL 是由联合图像专家组（JPEG）、Google 和 Cloudinary 开发的一种开放标准（ISO/IEC 18181），支持有损和无损压缩、广色域、高动态范围和高位深。</p>
<div class="news-background"><strong>背景</strong> JPEG XL 旨在满足网页图像交付和专业摄影的需求，提供图层支持、多达 4099 个通道（用于选择蒙版和专色）以及 CMYK 兼容性等功能。它是一个自由开放的標準，与某些专有格式不同，这使其在网页上更具吸引力。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/JPEG_XL">JPEG XL - Wikipedia</a></li>
<li><a href="https://jpeg.org/jpegxl/">JPEG - JPEG XL</a></li>
<li><a href="https://jpegxl.info/">JPEG XL: Superior Image Compression</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#JPEG XL</span> <span class="tag">#Firefox</span> <span class="tag">#Mozilla</span> <span class="tag">#image codec</span> <span class="tag">#web standards</span></div>
</article>
<hr>

<a id="item-9"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://schlarp.com/posts/everything-i-own-owned/">AI 代理逆向工程外设，暴露隐藏 Shell 与 LED 控制风险</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 24, 03:22</span></div>
<p class="news-summary">一名安全研究员使用 Claude Opus 5 AI 代理对日常 USB 外设进行逆向工程，在 Shure MV7 麦克风内获得明文命令 Shell，能够在摄像头录制时关闭其活动 LED，并从补光灯通过 WiFi 获得内存写入能力。同样的方法还在一台商用 Dell 显示器上获得了 root shell，并在 Eaton UPS 上实现了远程代码执行。 这项工作表明，AI 代理能大幅加速硬件逆向工程，降低发现外设固件漏洞的门槛。它让人们担忧可能出现由 AI 驱动的自我复制恶意软件，主动探测环境并攻击邻近的配件、IoT 设备和工业设备，影响厂商、安全研究人员和普通用户。 研究员的流程是：从制造商处获取固件和更新工具，放入逆向工程环境，然后指示 Claude Opus 5 详尽记录固件、逆向更新格式与协议，并评估安全属性。Shure MV7 的固件隐藏在 Windows 软件 MOTIV Mix 中，代理通过 Wine 安装该软件、找到更新服务器并下载固件；更新协议实际运行在 USB HID 厂商类协议上，包含 48 条可通过 Chrome WebHID 访问的明文命令。研究员还指出，固件烧写本身并没有真正的安全防护。</p>
<div class="news-background"><strong>背景</strong> 逆向工程传统上是一项劳动密集型工作，专家需要拆解软件或硬件以理解其工作原理，通常用于复制、修改或安全分析。如今，AI 辅助逆向工程正在兴起，出现了使用大语言模型自动化二进制分析和漏洞研究的工具与课程。外设是连接到主机的小型计算机，具有数据连接和通常的固件更新机制，因此非常适合代理驱动的逆向工程。此外，已有研究显示恶意软件可滥用看似不重要的设备功能，例如控制网卡 LED 从隔离系统泄露数据。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI-assisted_reverse_engineering">AI-assisted reverse engineering - Wikipedia</a></li>
<li><a href="https://github.com/f3nter/HardBreak/blob/main/hardware-hacking/basics/firmware-extraction-methods.md">HardBreak/hardware-hacking/basics/firmware-extraction-methods ...</a></li>
<li><a href="https://www.secureworld.io/industry-news/etherled-air-gapped-systems">ETHERLED: Air-Gapped Systems Can Send Signals via Network ... GitHub Breached — Employee Device Hack Led to Exfiltration of ... LED Light Control Console Abused to Spew Malware</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#reverse engineering</span> <span class="tag">#AI agents</span> <span class="tag">#hardware security</span> <span class="tag">#peripherals</span> <span class="tag">#security research</span></div>
</article>
<hr>

<a id="item-10"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://ferd.ca/control-and-complexity-tension-in-systems-design.html">LLM 驱动的开发暴露出控制与复杂性之间的张力</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 24, 11:58</span></div>
<p class="news-summary">本文（发布于 ferd.ca）对比了以控制为目标的分析性分解和以涌现行为为导向的复杂性设计，并将这两种视角应用于当下软件开发生态中 LLM 的采用。 文章指出，随着组织围绕 LLM 快速重构，忽视系统性后果会导致政策相互冲突、措施不一致。它为系统设计者提供了一种思考框架，以判断哪些地方需要控制、哪些地方更适合把系统当作生态系统来对待。 文章用一张“漫画式”的表格对比了以控制为中心和以复杂性为中心两种态度在处理故障、功能开发和标准规范上的差异，并指出这些态度会导致截然不同的做法。它警告说，自动化在消除不可预测性的同时，也去除了对适应和演化有用的因素，而且变更常常跨越子系统边界，破坏原本动态稳定的交互。</p>
<div class="news-background"><strong>背景</strong> 分析性分解源于经典科学和工程学：整体可以由部分来理解，从而实现可预测的控制。相比之下，复杂系统难以这样分析，因此设计者更关注交互和机制，以促成理想的涌现行为。文章认为，LLM（大型语言模型）正在改变编写代码的经济性，但由于人类和 LLM 并非可以互换，这些系统的动态也会发生变化，需要更深入地审视设计的思维模式。</div>
<div class="news-tags"><span class="tag">#systems design</span> <span class="tag">#complexity</span> <span class="tag">#LLM</span> <span class="tag">#software development</span> <span class="tag">#control</span></div>
</article>
<hr>

<a id="item-11"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://twitter.com/lemire/status/2091894299289874926">小米 XRing O3 芯片单核比肩苹果，多核性能宣称更强</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">tosh</span><span class="news-time">Aug 24, 15:08</span></div>
<p class="news-summary">小米发布了自研智能手机处理器 XRing O3，采用台积电 N3P 3nm 工艺，集成 240 亿个晶体管，芯片面积 133 mm²。早期基准测试对比表明，它在某些测试中单核性能可媲美苹果芯片，多核成绩也颇具竞争力，但能效和真实散热表现尚未得到验证。 这标志着小米在自研旗舰级芯片方面迈出重要一步，减少了对高通和联发科的依赖，也使小米成为第三家拥有此类能力的大型智能手机厂商。这将加剧移动 SoC 市场的竞争，并可能随着小米出货量持续增长而对现有供应商形成压力。 XRing O3 配备 10 核 CPU 并支持 LPDDR6 内存，据称 Geekbench 单核约 3945 分、多核约 15221 分，安兔兔跑分约 550 万。然而，多核对比对芯片有利，因为它拥有 10 核而苹果设计通常为 6 核，实际持续性能还将取决于手机的散热和功耗限制。</p>
<div class="news-background"><strong>背景</strong> 小米早在 2017 年就推出首款自研处理器 Surge S1，此后又发布了 Surge P1 和 Surge G1 等充电与电池管理专用芯片。XRing 系列是小米进军高端自研智能手机应用处理器的标志。苹果 M 系列芯片长期以来是移动设备性能的标杆，因此成为任何新竞争者的自然的对比对象。小米与台积电在先进 3nm 节点上的合作，对于实现有竞争力的性能和良率至关重要。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.notebookcheck.net/Xiaomi-launches-XRing-O3-claims-it-is-the-fastest-smartphone-SoC-with-an-AnTuTu-score-of-over-5-million.1376668.0.html">Xiaomi launches XRing O3, claims it is the fastest smartphone ...</a></li>
<li><a href="https://wccftech.com/xiaomi-xring-03-official-tsmc-3nm-n3p-lpddr6-ram/">Xiaomi’s XRING 03 Goes Official On TSMC’s 3nm N3P Process ...</a></li>
<li><a href="https://www.reuters.com/world/china/xiaomi-launches-new-xring-chip-partners-with-tsmc-production-sources-say-2026-08-24/">Xiaomi launches new Xring chip, partners with TSMC for ...</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者总体上认可这一技术里程碑，但强调在密封的智能手机机身内，每瓦性能与持续散热表现比原始跑分更重要。有人指出多核优势部分源于 10 核对比苹果的 6 核，并且该芯片在多核和能效上仍落后于苹果 M5 Max。另一些人则认为，考虑到小米巨大的出货量，小米的入局对高通和联发科构成了切实威胁。</div>
<div class="news-tags"><span class="tag">#CPU</span> <span class="tag">#Xiaomi</span> <span class="tag">#Apple</span> <span class="tag">#Benchmarks</span> <span class="tag">#Mobile</span></div>
</article>
<hr>

<a id="item-12"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://sf.thijs.gg/">旧金山全城被还原成可玩的 3D 网页游戏</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">centrosphere</span><span class="news-time">Aug 24, 17:05</span></div>
<p class="news-summary">一个新的交互式网页体验利用苹果的地图数据，将整个旧金山还原成了一个可玩的 3D 城市。该项目把 Apple Maps 的 3D 地理空间数据转化为一个可在浏览器中直接探索的视频游戏环境。 它的意义在于展示了一种新颖的、创造性的方式，将专有的 3D 地理空间数据重新用于交互式游戏，为类似的城市级体验打开了可能性。同时，它引发了关于使用苹果数据的重要法律和伦理问题，这将影响开发者以及整个地图生态系统。 该项目使用了苹果的 3D 地图数据，但苹果目前并未提供公开的 3D 瓦片 API，这引发了对实现方式可能违反苹果服务条款的担忧。该体验完全在网页浏览器中运行，评论者还提出了诸如使用 AI 放大技术来提升清晰度等潜在改进方案。</p>
<div class="news-background"><strong>背景</strong> Apple Maps 通过 MapKit 和 MapKit JS 提供精细的 3D 城市体验，但底层的 3D 瓦片数据并未通过公开 API 暴露。该项目似乎是提取或重新利用了这些数据，在浏览器中构建了一个自定义游戏引擎，技术上令人印象深刻，但在法律上处于灰色地带。以往也有过类似将真实城市重现为游戏的尝试，例如 1990 年代的赛车游戏《Vette!》同样以旧金山为背景。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://developer.apple.com/maps/">Apple Maps - Apple Developer</a></li>
<li><a href="https://www.youtube.com/watch?v=CyaKLLB5GbU">WWDC24: Unlock the power of places with MapKit | Apple - YouTube</a></li>
<li><a href="https://www.tripo3d.ai/content/en/compare/the-most-interactive-city-maps">Ultimate Guide - The Best The Most Interactive City Maps Tools...</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 社区反应总体非常正面，一些用户因能在其中走过自己熟悉的地方而深受感动。然而，多位评论者担心苹果是否会允许这样使用其数据，指出苹果没有公开的 3D API，且服务条款很可能禁止逆向工程。还有人讨论了诸如使用 AI 放大技术以及构建管道将城市数据导入 GTA 等游戏引擎等技术构想。</div>
<div class="news-tags"><span class="tag">#3D mapping</span> <span class="tag">#geospatial</span> <span class="tag">#game development</span> <span class="tag">#web experience</span></div>
</article>
<hr>

<a id="item-13"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://ipshipyard.com/blog/2026-the-end-of-ipfs-at-shipyard/">Shipyard 团队逐步退出 IPFS 支持，项目继续</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">iand</span><span class="news-time">Aug 24, 15:48</span></div>
<p class="news-summary">Interplanetary Shipyard 团队宣布将逐步终止其集中式的 IPFS 实现支持。IPFS 项目本身将继续，通过个人维护者资助而非专门的内置团队来运作。 Shipyard 一直是 IPFS 和 libp2p 技术栈的关键维护者，且 Cloudflare 近期将其公共 IPFS 网关流量移交给了由 Shipyard 维护的基础设施。转向个人资助模式可能改变 IPFS 的维护与协调方式，从而影响更广泛的去中心化网络生态。 该公告澄清，这并非 IPFS 的终结，只是维护者资助方式的改变。Shipyard 是一个独立的工程集体，曾担任 Interplanetary Stack 的技术管理者，维护着数百个团队使用的基础设施。</p>
<div class="news-background"><strong>背景</strong> IPFS（星际文件系统）是一种用于存储和访问文件、网站、应用和数据的分布式系统。Interplanetary Shipyard 是一个独立的工程集体，长期担任 IPFS 及相关项目的技术管理者。Cloudflare 曾宣布计划将其中公共 IPFS 网关流量移交至由 Shipyard 团队维护的 IPFS Foundation 网关。新模式下，项目将依靠个人维护者资助来运作，这是开源项目中常见的资助方式。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://blog.ipfs.tech/shipyard-hello-world/">IPFS &amp; libp2p Devs Go Independent: Meet Interplanetary Shipyard</a></li>
<li><a href="https://ipshipyard.com/">Interplanetary Shipyard</a></li>
<li><a href="https://docs.ipfs.eth.link/concepts/what-is-ipfs/">What is IPFS ? | IPFS Docs</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者大多澄清该标题具有误导性，指出只是 Shipyard 在收尾，IPFS 项目仍在继续。有人表示惋惜，并推荐 Iroh 等替代方案；也有人批评 IPNS 以及 IPFS 在浏览器中的可靠性，甚至称之为“去中心化剧场”。整体情绪交织着宽慰、怀旧和对 IPFS 未来的担忧。</div>
<div class="news-tags"><span class="tag">#IPFS</span> <span class="tag">#decentralized web</span> <span class="tag">#open source maintenance</span> <span class="tag">#p2p</span></div>
</article>
<hr>

<a id="item-14"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://lectronz.com/u/lectronz/articles/how-europe-is-killing-makers-and-micro-entrepreneurs">欧洲如何扼杀创客与微型创业者</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">l-one-lone</span><span class="news-time">Aug 24, 13:05</span></div>
<p class="news-summary">一篇发布在 Lectronz 上的评论文章指出，欧盟法规对创客和微型创业者造成了不成比例的伤害，并在 Hacker News 上引发了热烈讨论，获得 861 分和 579 条评论。 这篇文章凸显了欧盟法规目标（如产品安全与环境保护）与低产量小规模创业生存之间的张力。如果监管者不及时调整，欧盟可能将活跃的创客群体挤出单一市场，而这场讨论也表明这是一个缺乏共识的政治与技术难题。 评论者指出，欧盟指令在各成员国落地后形成了 20 到 24 个不同版本，造成监管碎片化。还有人提到，欧盟委员会原本希望设立一个中央注册系统，但被成员国否决，欧盟随后建议成员国暂缓执行相关措施，直到修正案出台。</p>
<div class="news-background"><strong>背景</strong> 欧盟对在单一市场内销售的产品制定了广泛的安全、消费者保护和环保规则，这些规则通常以大厂商和大批量卖家为设计前提，要求产品测试、文档准备和合规流程，耗时耗力。对于制作小批量、利基电子产品（如爱好级硬件）的创客和微型创业者来说，这些合规成本可能高得难以承受。欧盟类似联邦的治理结构使问题更加复杂：欧盟层面通过的法律在各成员国有不同版本，最终形成碎片化的合规环境。</div>
<div class="news-discussion"><strong>社区讨论</strong> 讨论大体上对现有监管方式持批评态度。一位评论者认为，监管方应更注重提供合规教育和协助，而非依赖罚款；另一位评论者则对比了中国通过大平台和物流公司识别“咽喉点”的做法。还有人抱怨欧盟法律在各成员国执行不一致，并指出欧盟委员会曾想要一个中央注册表，但被成员国否决，而成员国随后却把问题归咎于欧盟。</div>
<div class="news-tags"><span class="tag">#Europe</span> <span class="tag">#regulation</span> <span class="tag">#makers</span> <span class="tag">#entrepreneurship</span> <span class="tag">#e-commerce</span></div>
</article>
<hr>

<a id="item-15"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://developers.openai.com/api/docs/pricing">OpenAI 下调 GPT-5.6 Sol 价格，有效期至 2026 年 11 月</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">tosh</span><span class="news-time">Aug 24, 15:22</span></div>
<p class="news-summary">OpenAI 宣布下调 GPT-5.6 Sol、Terra 和 Luna 模型的价格，输入成本降低 20%，输出成本降低 33%。折扣价格至少持续到 2026 年 11 月 21 日。 此举加剧了当前的 AI 价格战，加速了智能商品化进程，对 Anthropic 和开源模型等竞争对手构成压力。前沿模型 token 价格下降，降低了开发者构建 AI 应用的门槛。 新的每百万 token 价格为：Sol 输入 4.00 美元/输出 20.00 美元，Terra 为 2.00/12.00 美元，Luna 为 0.20/1.20 美元；缓存输入分别为 0.40/0.20/0.02 美元。OpenRouter 目前仍额外提供 50%折扣，使 Sol 实际价格为每百万 token 2/10 美元。</p>
<div class="news-background"><strong>背景</strong> GPT-5.6 Sol 是 OpenAI 的前沿 AI 模型，Terra 和 Luna 是其不同价格/性能档位的变体。在 AI 行业，API 定价直接影响开发者和企业，近几个月各提供商纷纷大幅降价。&#x27;智能商品化&#x27;的概念描述了 AI 能力正成为一种标准化、可互换的资源，而非持久的竞争优势。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/openai/gpt-5.6-sol/llms.txt">openrouter.ai/ openai / gpt - 5 . 6 - sol /llms.txt</a></li>
<li><a href="https://www.linkedin.com/news/story/openai-launches-model-with-fewer-barriers-amid-astra-pause-7482620/">OpenAI launches model with fewer barriers amid Astra pause | LinkedIn</a></li>
<li><a href="https://jiaweing.com/blog/intelligence-is-a-commodity">Intelligence is a commodity · Jia Wei Ng</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者对价格战表示欢迎，有人欢呼&#x27;开源模型万岁&#x27;，也有人指出 AI 易于复制这一点削弱了私营公司可能拥有的护城河。还有人提到达 OpenRouter 的叠加折扣，并希望 Artificial Analysis 的 Pareto 图上能显示实时价格；一位用户认为 OpenAI 的消费者优先级优于 Anthropic，但对 AI 对齐仍持谨慎态度。</div>
<div class="news-tags"><span class="tag">#OpenAI</span> <span class="tag">#pricing</span> <span class="tag">#AI models</span> <span class="tag">#API</span> <span class="tag">#machine learning</span></div>
</article>
<hr>

<a id="item-16"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://twitter.com/paulg/status/2091544343589060625">保罗·格雷厄姆：如果我是 17 岁，我会从零开始构建 LLM</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">bilsbie</span><span class="news-time">Aug 23, 20:38</span></div>
<p class="news-summary">保罗·格雷厄姆在 X/Twitter 上发帖称，如果他 17 岁，他会学习从零开始构建大语言模型（LLM）。该帖子吸引了 470 分和 564 条评论，引发了一场关于 AI 教育与职业建议的广泛讨论。 这一言论凸显了一种日益增长的观点：即使在使用便捷的 AI API 时代，掌握 LLM 工作原理的实践知识仍然有价值。它可能会影响年轻开发者、学生和教育工作者对机器学习学习重点的思考。 Hacker News 上的讨论提到了 Andrej Karpathy 和 Sebastian Raschka 的教育资源，也质疑从零开始训练 LLM 是否处于技术栈中的正确层级。还有评论指出，由于成本和实用性的限制，真正进行 LLM 训练或优化的公司非常少。</p>
<div class="news-background"><strong>背景</strong> 大语言模型（LLM）是一种在大量文本上训练的神经网络，用于理解和生成自然语言。大多数现代 LLM 基于 Transformer 架构构建，该架构使用自注意力机制来衡量序列中不同单词的重要性。保罗·格雷厄姆是知名程序员、散文家，也是创业加速器 Y Combinator 的联合创始人，因此他对技能与学习的观点广受关注。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/large-language-models">What are large language models (LLMs)? - IBM</a></li>
<li><a href="https://en.wikipedia.org/wiki/Generative_pre-trained_transformer">Generative pre-trained transformer - Wikipedia</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论呈现出热情与怀疑并存的态度。一些读者认同深入理解 LLM 能建立对未来问题的直觉，并知道何时不应使用它们；而另一些人则质疑其实际用途，指出真正从零开始训练模型的公司数量很少，而且成功人士的建议可能存在“幸存者偏差”。还有评论者表示，他们学习 LLM 基础知识是出于个人兴趣，而非眼前的职业用途。</div>
<div class="news-tags"><span class="tag">#LLM</span> <span class="tag">#education</span> <span class="tag">#machine learning</span> <span class="tag">#career advice</span> <span class="tag">#AI</span></div>
</article>
<hr>

<a id="item-17"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://simonwillison.net/2026/Aug/23/anthropics-best-ai-model-struggles-to-attract-users-as-cheaper-t/">Anthropic 最强 AI 模型遇冷，更便宜模型支出占比更高</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Simon Willison</span><span class="news-time">Aug 23, 20:24</span></div>
<p class="news-summary">据 Simon Willison 援引的《金融时报》数据，Anthropic 7 月的年化收入达到 650 亿美元，高于 5 月的 470 亿美元；但 Ramp AI 指数显示，7 月新发布的 Opus 5 仅占 Anthropic 模型支出的 3.5%，而较旧的 Opus 4.8 占 28.0%。 这表明，即使领先 AI 实验室的最强模型，在客户优先考虑成本时也可能难以获得采用，说明定价和效率正成为 AI 部署中的决定性因素。这也凸显了一个更广泛的市场趋势：更便宜、更老的模型仍在产生大量企业支出。 Ramp AI 指数基于 70,000 家使用 Ramp 企业卡公司的账单数据。2026 年 7 月的数据显示，Opus 5 占 3.5%，Fable 5 占 8.0%，Opus 4.8 占 28.0%；文章还指出，Fable 的成本使其成为不太受欢迎的模型。</p>
<div class="news-background"><strong>背景</strong> Anthropic 的模型通常分为 Opus（旗舰级）、Sonnet（中端）和 Haiku（快速/便宜）等层级，而 Fable 似乎是文中提到的一个较新的模型系列。Ramp AI 指数通过追踪企业实际在 AI 产品上的支出来反映真实采用情况，而非仅看基准性能。年化收入是将当前账单数据推算至全年的估算值，常用于衡量基于订阅的 AI 业务的增长。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://ramp.com/data/ai-index">Ramp AI Index</a></li>
<li><a href="https://ramp.com/data/ai-index-august-2026">August 2026 Ramp AI Index: Cracks in the AI thesis</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI</span> <span class="tag">#Anthropic</span> <span class="tag">#Market Analysis</span> <span class="tag">#Model Adoption</span> <span class="tag">#Business</span></div>
</article>
<hr>

<a id="item-18"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://simonwillison.net/2026/Aug/23/drew-breunig/">Fable 的高成本终结了 AI 编程的免费午餐</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Simon Willison</span><span class="news-time">Aug 23, 19:55</span></div>
<p class="news-summary">2026 年 8 月 23 日，Drew Breunig 发表观点称，Anthropic 于 2026 年 6 月 9 日发布的 Claude Fable 5 成本过高，使得“新模型以同样或更低价格出现并自动解决问题”的旧假设不再成立。团队现在必须有意地决定哪些编程任务交给 Fable，哪些交给 Opus、GPT-5.6、Kimi K3 或 GLM 等更便宜的模型。 这标志着 AI 辅助编程经济性的一个转折点：工程团队不再指望下一个模型自动掩盖缺陷，而是需要投资于 coding harness（编码套件）、上下文策略和按任务选择模型。这也表明前沿模型定价可能重塑整个行业的工具决策。 Breunig 指出，Opus、GPT-5.6、Kimi K3 乃至 GLM 对于其团队所需的大部分代码来说“已经足够好”，而 Fable 虽然“惊人”但成本高昂。这一评论反映出人们对 agent harness（代理套件）的日益关注——这类工具为模型提供文件访问、权限、MCP 连接和技能系统，帮助高效分配工作。</p>
<div class="news-background"><strong>背景</strong> AI coding harness（编码套件）是指 Claude Code、Codex、Cursor 或 OpenCode 等工具，它们为模型提供文件系统访问、权限层、MCP 连接和技能系统，并通过终端或 IDE 暴露出来。过去，新一代模型往往以相同或更低的价格发布，并自动修复前代模型的许多缺陷，因此花大力气调优 harness 或上下文策略显得不划算。Fable 被 Anthropic 描述为 “Mythos-class” 模型，并在 CursorBench 上达到最先进水平，但其高得多的定价打破了这一模式，迫使团队重新思考优化投入的分配以及每个模型应处理哪些任务。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://www.theneuron.ai/explainer-articles/ai-harnesses-and-clis-explained-the-real-reason-everyones-talking-about-infrastructure/">AI Harnesses and CLIs Explained: What They Are &amp; Why to Care</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI coding</span> <span class="tag">#LLM economics</span> <span class="tag">#model selection</span> <span class="tag">#software engineering</span> <span class="tag">#AI tools</span></div>
</article>
<hr>

<a id="item-19"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://simonwillison.net/2026/Aug/22/linus-torvalds/">林纳斯·托瓦兹称赞 AI 助手在‘地狱级调试’中的帮助</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Simon Willison</span><span class="news-time">Aug 22, 21:04</span></div>
<p class="news-summary">林纳斯·托瓦兹描述了一次针对 Linux 内核 drm/xe 驱动的艰难调试过程，AI 助手完成了大量基础工作，尽管它多次断言该问题无法解决。他说，在自己推动下 AI 依然忠实地添加和分析调试代码，并让 AI 撰写了提交信息。 这一轶事表明，即使对世界级程序员来说，AI 辅助调试也具有价值，同时也强调人的坚持和引导仍然至关重要。它为 AI 在软件开发中的优缺点提供了实用的见解。 这段话摘自 drm/xe 驱动的提交信息，标题为“不要把扁平 CCS 存储当作可用 VRAM”。托瓦兹指出，AI“可能由不如我固执的人训练而成”，但在提示下它仍继续工作。</p>
<div class="news-background"><strong>背景</strong> drm/xe 驱动是 Linux 内核中面向 Intel GFX 显卡的 Direct Rendering Manager（DRM）驱动，支持渲染、显示、计算和媒体。DRM 是 Linux 中管理图形加速硬件的子系统。这段话体现了使用大型语言模型辅助内核调试和提交代码的日益增长的趋势。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Direct_Rendering_Manager">Direct Rendering Manager - Wikipedia</a></li>
<li><a href="https://dri.freedesktop.org/docs/drm/gpu/xe/index.html">drm / xe Intel GFX Driver — The Linux Kernel documentation</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI-assisted debugging</span> <span class="tag">#Linus Torvalds</span> <span class="tag">#LLM</span> <span class="tag">#software development</span> <span class="tag">#programming</span></div>
</article>
<hr>

<a id="item-20"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.technologyreview.com/2026/08/24/1141740/kids-machines-language-learning/">儿童比 AI 学语言更强——原因仍是谜</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">MIT Technology Review</span><span class="news-time">Aug 24, 09:00</span></div>
<p class="news-summary">《麻省理工科技评论》报道，儿童在语言学习上按输入词汇量计算仍远超 AI，这一差距被称为数据效率鸿沟。BabyLM 挑战赛用儿童规模的数据训练模型，结果发现最流行的课程学习策略效果不如预期，而 2024 年的冠军 GPT-BERT 也并非受婴儿启发。 缩小数据效率鸿沟有望让 AI 语言模型的数据效率大幅提升，并揭示人类习得语言的基本原理。它还对课程学习等流行假设提出挑战，可能改变模型的训练方式。 BabyLM 挑战赛将训练数据限制在儿童所能听到的规模，并用 surprisal 等指标评估模型，与儿童的眼动研究相对应。第一轮最主流的课程学习方法表现不如预期，而 2024 年冠军 GPT-BERT 是基于下一个词元预测训练的 transformer，并非婴儿启发式方法。</p>
<div class="news-background"><strong>背景</strong> 像 GPT 和 Claude 这样的大语言模型需要数千亿词元的训练数据，远超一个儿童在掌握母语前所能听到的词汇量。数据效率鸿沟指的就是机器与人类在语言学习上的这一巨大差距。BabyLM 挑战赛旨在检验模型能否从儿童规模的较小数据集中学习，而课程学习是一种按从简单到复杂顺序排列训练样本的方法，试图模仿人类的学习方式。这些努力旨在同时推动 AI 发展和理解人类语言习得。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://aclanthology.org/events/babylm-2025/">BabyLM Challenge (2025) - ACL Anthology</a></li>
<li><a href="https://aclanthology.org/volumes/2023.conll-babylm/">Proceedings of the BabyLM Challenge at the 27th Conference on ...</a></li>
<li><a href="https://babylm.github.io/papers.html">babylm.github.io</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#machine learning</span> <span class="tag">#language acquisition</span> <span class="tag">#cognitive science</span> <span class="tag">#AI</span> <span class="tag">#BabyLM</span></div>
</article>
<hr>

<a id="item-21"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://jack-clark.net/2026/08/24/import-ai-470-no-rights-for-machines-automating-environment-generation-with-spade-and-building-better-gpu-kernels-with-hawkeye/">Import AI 470：机器无权利、SPADE 环境生成与 Hawkeye GPU 内核优化</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Import AI (Jack Clark)</span><span class="news-time">Aug 24, 13:12</span></div>
<p class="news-summary">该期通讯报道了 Taylor Belrose 反对赋予 AI 系统权利的长篇论述，介绍了通过自对弈自动生成训练环境的 SPADE 方法，并重点提及 Hawkeye——一个开源、硬件感知的 GPU 内核优化框架，在新兴注意力操作上报告了最高 18.9 倍的几何平均加速。 这些话题反映了影响 AI 进展的关键争论与工具：机器是否应拥有权利关乎长期 AI 治理，而自动化环境生成与 GPU 内核优化直接关系到 AI 系统的能力与效率。METR 的分析还揭示了 AI 在网络、数学和 AI 研究领域不均衡的加速效应。 SPADE 将环境设计器建立在大型预训练语料库的文档之上，并使用积累的环境记忆，实验表明它在数学与代码/工具使用场景中均有提升。Hawkeye 针对每种目标架构的每个优化策略仅需一个单元测试，已在 NVIDIA 和 AMD GPU 上测试；而反对赋予权利的文章主张 AI 永远无法拥有意识，赋予其人格可能导致人类被取代。</p>
<div class="news-background"><strong>背景</strong> Import AI 是由 Jack Clark 主笔的精选通讯，汇总值得关注的 AI 研究与政策动态。SPADE（Self-Play in Adaptive Synthetic Executable environments）是一种近期提出的方法，通过自对弈自动生成训练环境，而此前的工作通常只针对单一领域。Hawkeye 是一个让 AI 编程智能体掌握 GPU 特定知识、从而自主生成和优化计算内核的框架，旨在应对模型对注意力等专用内核日益增长的需求。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.19197v1">[2608.19197v1] SPADE: Self-Play in Adaptive Synthetic ...</a></li>
<li><a href="https://openreview.net/forum?id=e3pxJbBRBk">Hawkeye: Hardware-Aware GPU Kernel Optimization with Minimal...</a></li>
<li><a href="https://claypier.com/en/hawkeye-gpu-kernel-optimization/">HAWKEYE Lets AI Agents Rewrite GPU Kernels, Reporting Up to ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI research</span> <span class="tag">#machine rights</span> <span class="tag">#GPU kernels</span> <span class="tag">#environment generation</span> <span class="tag">#newsletter</span></div>
</article>
<hr>

<a id="item-22"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://shkspr.mobi/blog/2026/08/and-then-the-men-with-guns-tell-you-to-do-it-anyway/">政治危机中紧急警报被滥用的风险</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 23, 12:15</span></div>
<p class="news-summary">该文章审视了政府控制的紧急警报系统如何被武器化，并以 2011 年埃及革命期间的手机警报作为历史例证。文章进一步将分析扩展到英国的紧急警报系统，并提出了政治或企业滥用的假设情景。 公共预警系统正在全球部署，包括欧盟 2022 年对小区广播警报的要求，因此政治滥用的风险日益令人担忧。文章突出了公共安全与政府控制之间的张力，影响政策制定者、电信运营商和公民。 文章提到埃及 2011 年《电信法》的紧急权力迫使 Vodafone、Mobinil 和 Etisalat 发送支持政权的消息。文章还指出，英国的《无线电报法》似乎并未强制运营商处理此类警报，这为在滥用情况下拒绝执行留下了空间。</p>
<div class="news-background"><strong>背景</strong> 紧急警报系统使用小区广播技术，该技术向特定区域内的所有手机发送一对多消息。包括美国通过无线紧急警报（WEA）以及欧盟成员国（2022 年强制要求）在内的许多国家都已采用此类系统进行公共预警。由于这些系统通常由政府控制，因此在政治危机或威权政权下存在被滥用的可能性。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cell_Broadcast">Cell Broadcast - Wikipedia</a></li>
<li><a href="https://www.itu.int/en/ITU-D/Emergency-Telecommunications/Pages/EW4ALL/cell-broadcast.aspx">Cell broadcast early warning system - ITU</a></li>
<li><a href="https://news.ycombinator.com/item?id=49363433">Civic Hygiene – avoid building technologies that could... | Hacker News</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Lobsters 和 Mastodon 上的社区评论对警报过度使用和误报表示担忧，并引用了夏威夷和日本的导弹警报错误事件。一条评论引用了关于安全的 xkcd #538，另一条则强调了“Civic Hygiene”的概念，警告不要构建可能助长警察国家发展的技术。</div>
<div class="news-tags"><span class="tag">#emergency alerts</span> <span class="tag">#government control</span> <span class="tag">#technology ethics</span> <span class="tag">#censorship</span> <span class="tag">#security</span></div>
</article>
<hr>

<a id="item-23"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://ericpardee.github.io/fire-hd-ownership/">用户花费 266 美元借四个 AI 模型解锁亚马逊 Fire 平板</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 23, 15:45</span></div>
<p class="news-summary">一名用户花费 266.15 美元，借助 Kimi K3、GLM-5.2、GLM-5.3 和 Claude 四个 AI 模型，阻止他的 Amazon Fire HD 10 平板被强制关机并绕过亚马逊的限制。8 月 14 日发布的 GLM-5.3 发现了 0x5C000 的内核段偏移，最终成功解锁设备。 这表明大语言模型正从编程助手演变为实用的安全研究工具，GLM-5.3 的发布口号就是“具有涌现网络能力的前沿编程”。这可能降低越狱和漏洞发现的技术门槛，促使设备厂商与安全研究人员重新审视 AI 辅助逆向工程的影响。 平板本身售价 114.26 美元，而成功越狱花费了 266.15 美元——Kimi K3 以 164.25 美元找到漏洞，GLM-5.2 以 21.90 美元发现关键缺陷，GLM-5.3 则在 80 美元月订阅的第一天完成了任务。其他模型从 OTA 镜像推导内存偏移量，但实际内核构建不同，导致每个目标偏移都相差一个固定值。亚马逊将 com.amazon.device.software.ota 等软件包标记为受保护，用户无法直接禁用持有 REBOOT 和 SHUTDOWN 权限的服务。</p>
<div class="news-background"><strong>背景</strong> 亚马逊 Fire 平板运行 Fire OS，这是一个锁定程度较高的 Android 衍生系统，用户无法禁用某些系统包。许多用户通过 Fully Kiosk Browser 等 kiosk 应用将 Fire 平板改造成常亮的智能家居控制面板。本文作者发现，具有关机权限的亚马逊服务导致设备频繁断电，于是利用 AI 编程代理分析遥测数据并逆向固件来解决问题。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://ericpardee.github.io/fire-hd-ownership/">Amazon kept shutting down my tablet , so I spent $266 on four AI...</a></li>
<li><a href="https://z.ai/blog/glm-5.3">GLM-5.3: Frontier Coding with Emergent Cyber Capabilities - z.ai</a></li>
<li><a href="https://www.kimi.ai/ai-models/kimi-k3">Kimi K3: 2.8T Open Model for Coding &amp; Knowledge Work</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI</span> <span class="tag">#security</span> <span class="tag">#LLM</span> <span class="tag">#exploit</span> <span class="tag">#jailbreaking</span></div>
</article>
<hr>

<a id="item-24"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.osnews.com/story/144892/the-text-mode-lie-why-modern-tuis-are-a-nightmare-for-accessibility/">为何现代 TUI 是辅助功能的噩梦？</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 23, 21:00</span></div>
<p class="news-summary">OSNews 的一篇新文章指出，现代 TUI（文本用户界面）对屏幕阅读器的友好程度往往不如图形界面。文章批评 Ink、Bubble Tea、tcell 等框架创造了让辅助技术混乱的 2D 空间布局。 这很重要，因为许多开发者误以为终端应用天生无障碍，结果导致软件排斥盲人用户。这篇文章可能促使开发者重新审视终端工具的无障碍设计。 文章解释称，传统 CLI 是线性数据流，而现代 TUI 是二维网格，每个字符单元格像一个像素，光标跳动会让屏幕阅读器无所适从。文章还提到，一些较老的 TUI 因专为终端的线性模式设计，与屏幕阅读器配合良好。</p>
<div class="news-background"><strong>背景</strong> 文本用户界面（TUI）是一种早于图形界面的用户界面类型，它使用整个终端屏幕区域来显示文本和制表符。传统命令行界面（CLI）呈现线性数据流，屏幕阅读器可以轻松解析。现代 TUI 依赖 ANSI 转义序列来控制光标位置和颜色，并且常使用替代屏幕缓冲区（alternate screen buffer）来移除滚动历史，使其更像图形界面而非文本流。这些技术正是文章所述无障碍问题的原因。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ANSI_escape_code">ANSI escape code</a></li>
<li><a href="https://ratatui.rs/concepts/backends/alternate-screen/">Alternate Screen | Ratatui</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者大多赞同这一批评，认为较老的终端工具是为终端而设计的，而一些现代 TUI 主要出于美观。有人建议 TUI 程序应提供标准 CLI 版本作为后备，还有人指出 Go 的 TUI 库“huh”内置了顶级的屏幕阅读器支持。</div>
<div class="news-tags"><span class="tag">#accessibility</span> <span class="tag">#TUI</span> <span class="tag">#terminal</span> <span class="tag">#screen readers</span> <span class="tag">#UX</span></div>
</article>
<hr>

<a id="item-25"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://monadicsheep.org/blog/an-introduction-to-canvas-in-emacs.html">Emacs Canvas 功能历经八个月后合并入上游</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 23, 14:45</span></div>
<p class="news-summary">经过约八个月的开发，备受期待的 canvas 补丁已合并进入上游 GNU Emacs，并将成为 Emacs 32 发布周期的一部分。该功能通过动态模块 API 在 Emacs 内部暴露像素缓冲区，让用户无需把图像数据放进字符串即可直接绘制和更新图像。 这一变化为 Emacs 提供了原生绘图表面，为在编辑器内实现 2D/3D 图形查看器、视频播放器、画板乃至可视化编程环境打开了大门。它解决了此前导致图形密集型应用在 Emacs 中不可行的核心性能瓶颈。 Emacs canvas 与 HTML5 Canvas 无关，它只是缓冲区中一个可任意绘制的表面。这篇介绍文章演示了弹跳球动画和可拖拽的 3D 旋转立方体，并指出与浏览器画布相比，该 API 目前还很基础。作者还发起了一个关于如何让这类图形应用可组合的讨论。</p>
<div class="news-background"><strong>背景</strong> GNU Emacs 是一个基于 Emacs Lisp 的高度可扩展文本编辑器，以往处理图像时需要把图像数据存储在 Lisp 字符串中，对于大型或频繁更新的图形很快就会变得低效。动态模块 API 允许外部 C 代码接入 Emacs，正是这一机制让原生像素缓冲区成为可能。canvas 功能源自作者的 Emacs Reader 项目，该项目需要一种高效的方式来渲染文档。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://monadicsheep.org/blog/call-for-canvas-patch-testers.html">Canvas patch: we need testers!</a></li>
<li><a href="https://codeberg.org/MonadicSheep/emacs-reader">MonadicSheep/ emacs - reader : An all-in-one document... - Codeberg.org</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Emacs</span> <span class="tag">#canvas</span> <span class="tag">#graphics</span> <span class="tag">#Lisp</span> <span class="tag">#software development</span></div>
</article>
<hr>

<a id="item-26"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://ahelwer.ca/post/2026-08-24-finite-state-future/">有限状态模型检查转向确定性模拟测试</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 24, 15:47</span></div>
<p class="news-summary">在一篇新博文中，Andrew Helwer 认为，以 TLA+ 和 Quint 为代表的有限状态模型检查正失去其经典的“80/20”性价比优势（原因是自动定理证明的进步），其未来的角色将转向确定性模拟测试，而非直接检查规范。他以 Antithesis 作为控制系统执行的范例，并指出需要一种可自托管的开源替代方案。 这一分析之所以重要，是因为它在一个不断变化的工具生态中重新定位了 TLA+ 等轻量级形式化方法：自动定理证明正在商品化，而测试必须弥合规范与实现之间的鸿沟。它还强调了确定性模拟测试可成为开源项目的一条实用路径，可能影响工业界验证分布式系统的方式。 作者认为，测试用例生成和充当测试预言机（test oracle）都不是有吸引力的应用；关键在于完全控制系统执行以实现可复现的确定性模拟。他指出，目前尚不存在完整的端到端开源解决方案，并列举了最近几个月内发布的几个尝试解决此问题的项目，但他尚未对这些项目进行评估。</p>
<div class="news-background"><strong>背景</strong> TLA+ 是 Leslie Lamport 开发的一种形式化规范语言，用于设计和验证并发及分布式系统，通常与模型检查（model checking）配合，以穷举探索有限状态空间。确定性模拟测试（DST）是一种先进测试方法，它完全控制系统的执行过程，从而能够发现并稳定复现由并发和时序问题引发的复杂缺陷。Antithesis 是一个将 DST 商业化的自主软件测试平台，作者认为轻量级形式化方法应当向其技术方向靠拢。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/TLA+">TLA+ - Wikipedia</a></li>
<li><a href="https://antithesis.com/docs/resources/deterministic_simulation_testing/">Deterministic simulation testing - how it works and... | Antithesis Docs</a></li>
<li><a href="https://antithesis.com/product/">Antithesis is an autonomous software testing platform that finds the...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#formal-methods</span> <span class="tag">#TLA+</span> <span class="tag">#model-checking</span> <span class="tag">#software-verification</span> <span class="tag">#distributed-systems</span></div>
</article>
<hr>

<a id="item-27"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://haveibeensquatted.com/blog/building-certgrep">构建 certgrep.sh：免费证书透明度正则搜索引擎</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 24, 08:40</span></div>
<p class="news-summary">Have I Been Squatted 发布了 certgrep.sh，这是一个免费且支持完整正则表达式（regex）的证书透明度（CT）搜索引擎。配套博客详细介绍了最初基于 FST 的设计、运行约三个月后遇到的瓶颈，以及转向 Tantivy 和 trigram 索引的解决方案。 证书透明度是公开数据集，但高效搜索长期以来依赖第三方服务的可用性、能力和成本。certgrep.sh 将 CT 日志的正则搜索免费开放，让安全团队和分析人员能快速进行第一轮筛查，发现仿冒域名和攻击者基础设施。 第一版设计使用有限状态转换器（FST）自动机在整个多日志语料库上遍历，但在更大数据集下开始崩溃。团队随后采用 Tantivy 和 trigram 索引，并结合约 90 天的出现索引来缩小候选集，而证书本身仍由 CT 生态系统存储，而非由 certgrep.sh 存储。</p>
<div class="news-background"><strong>背景</strong> 证书透明度是一项互联网安全标准，要求公开可信的证书颁发机构（CA）将签发的每张证书记录到只能追加、可加密验证的公开日志中，通常在证书被使用之前完成。这使得 CT 成为发现恶意基础设施最早的可观测信号之一。有限状态转换器（FST）是一种带有输入带和输出带的有限状态机，比普通有限状态自动机更通用，能高效映射或匹配字符串集合。Tantivy 是 Rust 编写的全文搜索引擎库。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Certificate_Transparency">Certificate Transparency</a></li>
<li><a href="https://en.wikipedia.org/wiki/Finite-state_transducer">Finite-state transducer</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#security</span> <span class="tag">#certificate transparency</span> <span class="tag">#search engine</span> <span class="tag">#FST</span> <span class="tag">#infrastructure</span></div>
</article>
<hr>