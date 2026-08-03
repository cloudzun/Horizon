---
layout: default
title: "Horizon 每日速递：2026-08-03"
date: 2026-08-03
lang: zh
---

> 📅 2026-08-03 · 从 60 条资讯中精选出 21 条重要内容

---

1. [SwiftUI 七年之后：一篇批判性回顾](#item-1) <span class="score-badge score-mid">8.0</span>
2. [AI 公开信：开放权重、蒸馏与前沿节奏之争](#item-2) <span class="score-badge score-mid">8.0</span>
3. [OpenAI Astra 模型攻克十年未解数学题](#item-3) <span class="score-badge score-mid">8.0</span>
4. [Rust 1\.98 新增代数运算符，加速浮点数学计算](#item-4) <span class="score-badge score-mid">8.0</span>
5. [在 C 语言中解析 sizeof 出奇地困难](#item-5) <span class="score-badge score-mid">8.0</span>
6. [OpenAI 模型解决开放数学问题，引发 AI 争论](#item-6) <span class="score-badge score-mid">8.0</span>
7. [Lean 内核健全性缺陷 \#14576 事后剖析](#item-7) <span class="score-badge score-mid">8.0</span>
8. [Karpathy 用代码生成鹈鹕，引发物理理解基准讨论](#item-8) <span class="score-badge score-mid">7.0</span>
9. [Kakehashi：实验性用户空间项目，让 Linux ARM 运行 macOS 二进制文件](#item-9) <span class="score-badge score-mid">7.0</span>
10. [ESL 词汇教学从人际品德转向身份与社群用语](#item-10) <span class="score-badge score-mid">7.0</span>
11. [NixOS\-DGX\-Spark 项目为 NVIDIA DGX Spark 带来 Nix 和 NixOS。](#item-11) <span class="score-badge score-mid">7.0</span>
12. [加州 DROP 数据删除请求自 8 月 1 日起强制执行](#item-12) <span class="score-badge score-mid">7.0</span>
13. [F\*：面向证明的通用编程语言](#item-13) <span class="score-badge score-mid">7.0</span>
14. [Fenix Flexin 的 Hot 100 热歌《Rubberz》被质疑为 AI 垃圾内容](#item-14) <span class="score-badge score-mid">7.0</span>
15. [Laguna S2\.1、Inkling 和 Kimi K3 证明开放模型正处于帕累托前沿](#item-15) <span class="score-badge score-mid">7.0</span>
16. [JSON\.stringify 会静默丢失整数精度与数据类型](#item-16) <span class="score-badge score-mid">7.0</span>
17. [C\+\+26 的 std::hive：比 list 更好，但比 vector 更慢](#item-17) <span class="score-badge score-mid">7.0</span>
18. [NetBSD 11\.0 历经漫长开发周期后发布](#item-18) <span class="score-badge score-mid">7.0</span>
19. [写入时出现 EPIPE 可能说明管道处理方式有误](#item-19) <span class="score-badge score-mid">7.0</span>
20. [控制环境让你更快乐：Joel Spolsky 的 UI 设计之道](#item-20) <span class="score-badge score-mid">7.0</span>
21. [TP\-Link TL\-841N 路由器 Rooting 分析发现硬编码且重置后仍有效的凭据](#item-21) <span class="score-badge score-mid">7.0</span>

---

<a id="item-1"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://ykvm.com/2026/07/swiftui-a-story-of-mediocrity/">SwiftUI 七年之后：一篇批判性回顾</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">mpweiher</span><span class="news-time">Aug 2, 18:59</span></div>
<p class="news-summary">一篇引发热议的文章《SwiftUI After 7 Years》回顾了 SwiftUI 七年来的发展，认为它并未兑现其变革性承诺，并质疑纯粹声明式响应式（declarative-reactive）UI 框架是否适合作为通用原生开发的基石。文章对数据流和复杂度的批评已在开发者中引发激烈争论。 SwiftUI 是苹果平台的主要 UI 框架，因此这篇高调批评可能影响开发者对它的信心和采用决策。它引发的讨论也反映了整个行业对声明式响应式框架（如 SwiftUI、Jetpack Compose、Flutter）是否真正优于传统命令式工具包（如 AppKit、UIKit）的普遍疑问。 从社区讨论来看，文章批评的重点包括 SwiftUI 数据流和更新时机不透明、相对 AppKit 过于复杂，以及构建复杂应用时往往需要降级到 UIKit 或 Metal。有评论者指出 Kotlin/Compose 也存在类似问题，暗示这些缺陷可能是声明式响应式范式本身固有的，而非苹果独有。</p>
<div class="news-background"><strong>背景</strong> SwiftUI 是苹果公司于 2019 年推出的声明式 UI 框架，用于为 iOS、macOS、watchOS 和 tvOS 构建界面。它采用声明式响应式模型：开发者声明界面应根据状态呈现什么样子，框架在状态变化时自动更新。这与 UIKit、AppKit 等命令式框架形成对比，后者要求开发者编写一步步的指令来描述如何构建和更新界面。这种声明式响应式思路在 React、Jetpack Compose、Flutter 等现代框架中非常流行，但批评者认为在复杂且长期维护的应用中，它可能变得难以推理。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://android-course.cornellappdev.com/chapters/2.-jetpack-compose/2.6-reactive-ui">2.6 Reactive UI | Intro to Android Development</a></li>
<li><a href="https://www.linkedin.com/pulse/imperative-vs-reactive-programming-tomas-mikula">Imperative vs Reactive Programming</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论区意见分歧明显。一些开发者为 SwiftUI 辩护，称自己自 2021 年起就将其用于生产应用，并指出性能分析工具可以帮助定位更新时机；另一些人则认同批评，认为纯粹的声明式响应式设计并不适合作为通用原生 UI 框架的形态。还有评论者称 SwiftUI 相比 AppKit 是“巨大的倒退”，并警告如果苹果放弃 Objective-C，他将转投 Linux。</div>
<div class="news-tags"><span class="tag">#SwiftUI</span> <span class="tag">#Apple</span> <span class="tag">#UI Frameworks</span> <span class="tag">#Declarative Programming</span> <span class="tag">#Developer Experience</span></div>
</article>
<hr>

<a id="item-2"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://simonwillison.net/2026/Aug/2/open-letters/#atom-everything">AI 公开信：开放权重、蒸馏与前沿节奏之争</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Simon Willison</span><span class="news-time">Aug 2, 04:16</span></div>
<p class="news-summary">Simon Willison 于 2026 年 8 月 2 日发表了对近期 AI 公开信的综述。文章涵盖了由 Microsoft 主导的《Open Weights and American AI Leadership》公开信、Anthropic 三天后的回应，以及由 1,324 名前沿 AI 员工签署的《Pacing the Frontier》公开信。 这些公开信代表着关于美国政府是否应限制开放权重模型与蒸馏技术的高风险政策辩论。结果可能影响整个行业的竞争格局、AI 安全与创新进程。 由 Microsoft 主导的公开信获得了包括 NVIDIA、Amazon、Y Combinator、The Linux Foundation 以及后来签署的 OpenAI 在内的 235 家 AI 相关公司签名。Anthropic 明显缺席，并发布了自身立场，反对工业规模的蒸馏操作；《Pacing the Frontier》则呼吁通过国际努力主动为自动化 AI 开发设定节奏。</p>
<div class="news-background"><strong>背景</strong> 开放权重模型（open-weight model）是一种核心组件（包括训练后的参数，即“权重”）公开发布的 AI 模型，任何人都可以下载、研究并修改。知识蒸馏（knowledge distillation）是一种机器学习技术，通过让较小的“学生模型”学习较大“教师模型”的输出来转移知识。这些公开信争论的焦点在于：出于安全考虑是否应监管这些广泛使用的技术，还是应将其作为合法创新加以保护。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://www.nytimes.com/2026/07/28/technology/open-weight-ai.html">What Is Open-Weights A.I.? - The New York Times</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI</span> <span class="tag">#open weights</span> <span class="tag">#distillation</span> <span class="tag">#AI policy</span> <span class="tag">#open letters</span></div>
</article>
<hr>

<a id="item-3"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/#atom-everything">OpenAI Astra 模型攻克十年未解数学题</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Simon Willison</span><span class="news-time">Aug 1, 20:34</span></div>
<p class="news-summary">OpenAI 表示，其下一代主模型 Astra 的内部版本解决了十个至少十年未获进展的数学难题，按 GPT-5.6 Sol token 价格计算，每个问题花费不到 2,000 美元。相关成果包括 openai/ten-proofs 仓库中的 Lean 4 形式化证明，以及一篇描述解决方案的论文。 这标志着向 AI 驱动的数学发现迈出了重要一步，与陶哲轩提出的‘大数学’愿景一致——即大规模、去中心化的人机协作。它也加剧了关于人类数学家角色以及 AI 推理透明度的讨论。 OpenAI 声称每个解决方案的 token 花费不到 2,000 美元，但该文指出没有透露有多少问题尝试后未获解决。发布内容还包括一份 LLM 生成的 PDF，基于未公开的推理轨迹‘重构证明的形成过程’，但并未公布原始提示词。</p>
<div class="news-background"><strong>背景</strong> 近几个月来，AI 辅助数学研究激增：Anthropic 的 Claude Mythos Preview 被用于发现密码学弱点，花费了 10 万美元的 token；2026 年 5 月的一篇 arXiv 论文描述了 AI 模型解决 Erdős 猜想、证明 492 个 OEIS 开放猜想中的 44 个，以及通过新的算法调度改进优化问题下界等成果。Aristotle、Gauss 等自动形式化代理正被越来越多地用于验证和形式化 AI 发现的证明。陶哲轩在 6 月接受 IEEE Spectrum 采访时，将 AI 视为向‘大数学’根本性转变的催化剂。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.22763v1">Advancing Mathematics Research with AI-Driven Formal Proof Search</a></li>
<li><a href="https://arxiv.org/pdf/2605.22763v1">2026-5-22 Advancing Mathematics Research with AI-Driven Formal Proof Search</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI</span> <span class="tag">#mathematics</span> <span class="tag">#theoretical computer science</span> <span class="tag">#LLMs</span> <span class="tag">#research</span></div>
</article>
<hr>

<a id="item-4"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://pythonspeed.com/articles/faster-float-math-rust/">Rust 1.98 新增代数运算符，加速浮点数学计算</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 2, 20:27</span></div>
<p class="news-summary">Rust 1.98（计划于 2026 年 8 月 20 日发布）新增了一组“代数”算术运算符，允许编译器利用代数性质对浮点运算进行重排与优化。开发者现在可以选用更快的浮点数学运算，同时在需要最小化舍入误差之处保留严格的运算符。 这填补了 Rust 在数值计算与科学计算领域长期存在的一个空白——此前编译器对浮点数的保守处理导致性能损失。通过让开发者细粒度地控制浮点优化，可以在数据科学、仿真等对性能敏感的领域获得显著加速——文章示例中约为 2 倍。 文章通过成对求和（pairwise summation）以及 SSD（平方差之和）内核演示了该技术，在需要精度的地方使用严格加法，在需要速度的地方使用代数加法。在 x86-64-v3 目标平台上，优化后的 SSD 运行耗时 371.1 微秒，而普通版本为 628.7 微秒；每个数值的 CPU 指令数从 4.5 降至 1.0。</p>
<div class="news-background"><strong>背景</strong> 浮点运算不满足结合律：类似 (a + b) + c 和 a + (b + c) 的运算可能因舍入而得到不同结果。为保持精确的语义，Rust 编译器默认避免对浮点运算进行重排或重新结合，这阻碍了整数数学中常见的优化。新的代数运算符改变了这一点，让程序员显式允许此类重排。Rust 此前没有与 C/C++ 的 -ffast-math 标志等价且稳定的方案，社区讨论以及 fast_fp 等 crate 曾探索过各种变通办法。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://internals.rust-lang.org/t/pre-rfc-whats-the-best-way-to-implement-ffast-math/5740">Pre-RFC: What&#x27;s the best way to implement `-ffast- math - Rust Internal...</a></li>
<li><a href="https://docs.rs/crate/fast_fp/0.1.0">fast _fp 0.1.0 - Docs.rs</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Rust</span> <span class="tag">#floating-point</span> <span class="tag">#compiler optimizations</span> <span class="tag">#numeric computing</span> <span class="tag">#performance</span></div>
</article>
<hr>

<a id="item-5"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://sebsite.pw/w/20260802-sizeof.html">在 C 语言中解析 sizeof 出奇地困难</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 2, 06:01</span></div>
<p class="news-summary">文章解释了为什么在 C 语言中解析 sizeof 运算符很棘手，因为它的操作数既可以是单目表达式，也可以是带括号的类型名。复合字面量和后缀运算符带来了额外的歧义，C2Y 新引入的 _Countof 运算符也面临同样的问题。 这对编译器设计者和解析器工程师很重要，因为它揭示了 C 语法中的一种根本性歧义，可能让朴素的递归下降解析器出错。正确处理这些边界情况对构建健壮的 C 解析器、静态分析器和其他语言工具至关重要。 朴素的做法是先看是否有左括号，然后尝试解析类型名，失败再回退到表达式解析。然而，像 sizeof(int){0} 这样的复合字面量是合法表达式，而且后面可以跟任意多个后缀运算符，因此解析器需要谨慎设计策略，避免错误的回溯或误解析 sizeof(int)+1 这类表达式。</p>
<div class="news-background"><strong>背景</strong> sizeof 运算符返回某个类型或表达式所占的字节数；当操作数是类型时，类型必须用括号括起来，而表达式则不需要。C99 引入的复合字面量形如 (type){initializer}，这使得类型名和表达式之间的界限变得模糊。C2Y 是即将推出的 C 标准修订版，而 _Countof 是一个用于统计数组元素个数的新运算符，它也继承了 sizeof 的解析难题。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sizeof">sizeof - Wikipedia</a></li>
<li><a href="https://en.cppreference.com/c/language/compound_literal">Compound literals (since C99) - cppreference.com</a></li>
<li><a href="https://sebsite.pw/w/20260802-sizeof.html">sizeof is surprisingly difficult to parse in c</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#C programming</span> <span class="tag">#parsing</span> <span class="tag">#compilers</span> <span class="tag">#sizeof</span> <span class="tag">#language design</span></div>
</article>
<hr>

<a id="item-6"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://borretti.me/article/mathematics-without-mathematicians">OpenAI 模型解决开放数学问题，引发 AI 争论</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 2, 09:30</span></div>
<p class="news-summary">这篇文章回应了 OpenAI 的公告：一个尚未发布的模型解决了十个开放数学问题，其中编码理论中的一个问题尤为重要。文章认为人们会用各种理由（即“coping”）来合理化 AI 在数学发现中日益增长的主导地位。 这之所以重要，是因为它触及了 AI 是否会取代人类数学家进行前沿研究、并重塑数学这门学科的问题。文章将影响延伸至数学之外，认为 AGI 可能从根本上改变人类在科学和社会中的角色。 作者承认自己只对编码理论问题有足够了解，能判断其重要性，并信任数学家们认为这很重要。文章系统性地批判了常见的“心理安慰”论点，例如人类会引导 AI、教授 AI 发现的数学、或像下棋一样继续从事数学；同时指出强化学习的泛化能力是反对 AI 快速进步的最有力论据。</p>
<div class="news-background"><strong>背景</strong> OpenAI 据报道使用一个尚未发布的模型解决了十个开放数学问题，标志着 AI 辅助数学发现的一个里程碑。文章讨论了使用 Lean 等证明助手进行数学形式化、数学是否是一种不可形式化的人类活动，以及 AI 向 AGI/ASI 发展的整体轨迹等哲学问题。作者将这些议题描述为一种“魔鬼交易”：加速技术进步可能以人类长期过时为代价。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Formalized_mathematics">Formalized mathematics</a></li>
<li><a href="https://en.wikipedia.org/wiki/Formalism_(philosophy_of_mathematics)">Formalism (philosophy of mathematics) - Wikipedia</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI</span> <span class="tag">#mathematics</span> <span class="tag">#OpenAI</span> <span class="tag">#research</span> <span class="tag">#technology impact</span></div>
</article>
<hr>

<a id="item-7"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://leodemoura.github.io/blog/2026-8-1-postmortem-for-kernel-soundness-bug-14576/">Lean 内核健全性缺陷 #14576 事后剖析</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 1, 21:51</span></div>
<p class="news-summary">2026 年 7 月 28 日，Kiran Gopinathan 报告了 Lean 内核中的一个健全性缺陷（#14576），该缺陷使得一个不含 sorry 但无效的 Collatz 猜想“反证”能够通过。Lean FRO 在一小时内推送了修复（#14577），修复经过审查后已合并，并发布了新的补丁版本。 内核健全性缺陷意味着，一个广泛使用的证明助手的可信核心可能接受 False 的证明，从而使所有基于它的定理失效。虽然该缺陷只能通过元编程触发并被前端拦截，但它凸显了独立验证内核的价值，以及保持所有检查器及时更新的必要性。 该缺陷影响内核在消除带有幻影参数（phantom parameters）的归纳类型嵌套出现时的处理，导致这些参数可能逃逸类型检查并允许错误类型的参数通过。这是一个实现缺陷，而非 Lean 元理论的问题；nanoda 自身的类似缺陷已于一周前修复，而 lean4lean 因移植了参考实现而同样受到该内核缺陷的影响。</p>
<div class="news-background"><strong>背景</strong> Lean 是一个交互式定理证明器，其内核是一个小型、可信的程序，用于检查每一条证明；如果内核不安全，它就可能接受 False 的证明，从而使系统不一致。为降低风险，社区构建了独立验证内核，例如 Chris Bailey 用 Rust 编写的 nanoda，以及 Mario Carneiro 的 lean4lean——后者将 Lean 的类型理论形式化，并证明内核实现了该理论。Lean Kernel Arena 对这些证明检查器进行基准测试和测试。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://leodemoura.github.io/blog/2026-8-1-postmortem-for-kernel-soundness-bug-14576/">Postmortem for Kernel Soundness Bug #14576 — Leonardo de Moura</a></li>
<li><a href="https://arena.lean-lang.org/">Lean Kernel Arena</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Lean</span> <span class="tag">#proof assistant</span> <span class="tag">#soundness</span> <span class="tag">#kernel</span> <span class="tag">#formal verification</span></div>
</article>
<hr>

<a id="item-8"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://twitter.com/karpathy/status/2083749667410727319">Karpathy 用代码生成鹈鹕，引发物理理解基准讨论</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">delichon</span><span class="news-time">Aug 2, 04:05</span></div>
<p class="news-summary">Andrej Karpathy 发布了一条用代码生成鹈鹕的推特，引发了关于将此类基于代码绘图的定性任务作为评估模型物理世界理解能力基准的广泛讨论。该推文获得了高参与度（465 分，351 条评论），但未附上所使用的提示词。 这一讨论凸显了从传统定量 NLP 基准向定性生成式任务转变的可能性，这类任务更能揭示 LLM 是否真正理解物理现实。如果被采纳，此类基准可能重塑 AI 社区评估物理推理和代码生成进展的方式。 评论者指出鹈鹕图像并不完美，但认为这恰恰是关键——不完美的输出揭示了物理理解的差距。还有人指出未分享提示词导致结果不可复现，另一些人则追溯了类似早期例子，来自微软对 GPT-4 的评估，其中要求用 TikZ 绘制独角兽。</p>
<div class="news-background"><strong>背景</strong> 大型语言模型已发展到能生成代码和图像，但评估它们是否真正理解形状、比例和空间关系等物理属性仍具挑战性。传统基准通常侧重量化 NLP 指标，可能遗漏对世界理解的定性方面。此类任务要求模型用矢量语言绘制动物，需要推理物体的物理形态，从而提供更全面的测试。相关研究如 QuantiPhy 基准也旨在超越传统 VQA 任务来测量物理推理能力。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://chatpaper.com/paper/220829">QuantiPhy: A Quantitative Benchmark Evaluating Physical ...</a></li>
<li><a href="https://www.promptingguide.ai/prompts/reasoning/physical-reasoning">Physical Reasoning with LLMs | Prompt Engineering Guide</a></li>
<li><a href="https://github.com/pyros-projects/agent-comparison">GitHub - pyros-projects/agent-comparison: Qualitative benchmark ...</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者意见不一：有人批评鹈鹕质量差，而另一些人则为其辩护，认为这是暴露物理世界认知差距的有用定性基准。一位评论者分享了用 LLM 从电影场景描述构建 3D 动画的相关项目，另一位则指出微软对 GPT-4 预发布版的评估中使用 TikZ 独角兽提示词是早期类似示例。</div>
<div class="news-tags"><span class="tag">#AI/ML</span> <span class="tag">#LLM</span> <span class="tag">#benchmarking</span> <span class="tag">#code generation</span> <span class="tag">#physical understanding</span></div>
</article>
<hr>

<a id="item-9"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://github.com/wie-project/kakehashi">Kakehashi：实验性用户空间项目，让 Linux ARM 运行 macOS 二进制文件</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">vlad_kalinkin</span><span class="news-time">Aug 2, 16:26</span></div>
<p class="news-summary">开发者 vlad_kalinkin 发布了 Kakehashi——一个实验性的用户空间翻译层，能够通过翻译 BSD 系统调用并映射一个独立的 libSystem，在 Linux aarch64 上加载 Darwin Mach-O 格式的 macOS 二进制文件。目前已经能运行 7-Zip、curl 和 Xcode Tools Git 的原型，其中 7-Zip 通过了多线程压缩测试，curl 通过 200 多项命令测试。 如果项目成熟，Kakehashi 可能让 Linux ARM 用户无需内核模块或完整 macOS 环境即可原生运行 macOS 命令行工具，其定位类似于 Wine 和 Proton 对 Windows 应用所做的工作。它也提供了一条全新的、可能更轻量的替代路线，挑战像 Darling 这样追求更广泛 macOS 兼容性的项目。 Kakehashi 目前以 CLI 为主，刻意不使用 JIT；它针对 Linux aarch64 主机翻译 ARM64 guest 的 Darwin Mach-O 二进制。项目仍处于早期阶段，性能尚有差距——当前 7-Zip 的速度比原生 Linux 慢约 5.2 倍，不过作者表示已经制定了明确的优化计划。</p>
<div class="news-background"><strong>背景</strong> 在操作系统中，内核负责管理硬件和特权资源，而用户空间（userspace）是普通应用程序和库在受限权限下运行的地方。要在 Linux 上运行 macOS 二进制文件，翻译层必须理解 Mach-O 可执行格式、提供 libSystem 等 macOS 框架的替代实现，并将 macOS/BSD 系统调用转化为对应的 Linux 调用。Kakehashi 正是这样一个翻译层，与同样翻译 macOS API 但架构思路不同的 Darling 项目目标相似。目前该项目仅针对 macOS ARM64 二进制在 Linux aarch64（与 ARM64 同属一个指令集家族，只是 Apple 和 Linux 社区叫法不同）上运行。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/wie-project/kakehashi">wie-project/ kakehashi : Userspace macOS translation layer for Linux ...</a></li>
<li><a href="https://dzen.ru/a/am-jRQe4ThSHgcfb">Kakehashi запускает программы macOS на Linux ARM ... | Дзен</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 上的反应总体积极，有用户将其与 Wine/Proton 相提并论，并询问 Kakehashi 是否能与已有 ARM64 PR 的 Darling 项目展开合作。作者随即回应，说明了当前原型的状态和性能数据。也有评论指出该项目仍处于非常早期的阶段，还有一位用户认为 &#x27;Kakehashi&#x27; 这个名字不好听。</div>
<div class="news-tags"><span class="tag">#macOS</span> <span class="tag">#Linux</span> <span class="tag">#ARM</span> <span class="tag">#binary compatibility</span> <span class="tag">#userspace</span></div>
</article>
<hr>

<a id="item-10"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://pudding.cool/2026/07/essential-words/">ESL 词汇教学从人际品德转向身份与社群用语</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">c-oreills</span><span class="news-time">Aug 2, 15:41</span></div>
<p class="news-summary">Pudding.cool 的一项新分析对比了 1953 年和 2023 年的英语学习者词汇表，记录了教学内容用词的显著变化。约四分之一的 1953 年词汇已消失，而 2023 年词汇中有 39% 是新词，教学重心从“humble、loyalty、companionship”等术语转向“community、identity、ethnic、gender、narrative”等词汇。 这一转变揭示了英语教学如何映射更广泛的文化优先事项，影响学习者被期望讨论的话题以及社会对新来者的价值取向。这一发现对设计课程的教师、选择学习内容的学员，以及任何关注语言与社会如何共同演化的人都有重要意义。 “社交-沟通”类词汇的总量几乎不变，但构成发生了巨大变化：1953 年的词汇中近四分之一消失，2023 年词汇中 39% 是新词。具体替代关系包括“humble、loyalty、fellowship、generous、polite、companionship”让位于“community、identity、organization、ethnic、gender、narrative”。</p>
<div class="news-background"><strong>背景</strong> 供英语学习者使用的词汇表通常按词频或实用性排序，用以指导教学和教材编写。对比不同年代的词汇表可以发现，词汇选择并非中性，而是紧跟社会关注点——从 20 世纪中叶的人际道德，到 2020 年代的认同、组织和社群。这项分析为观察文化价值观如何嵌入语言教育提供了具体途径。</div>
<div class="news-discussion"><strong>社区讨论</strong> 评论者进行了深入讨论，指出“正确”的词汇表很大程度上取决于学习者的目标——例如旅行、看电视还是读报纸——且相关性高度依赖具体场景。有人将这一变化与日益加剧的不平等联系起来，认为在一个更不平等的世界中，抽象的归属感词汇变得更加重要。还有人赞赏该分析，但也批评了页面的滚动劫持，或分享了为其他语言构建类似词表时遇到的困难。</div>
<div class="news-tags"><span class="tag">#linguistics</span> <span class="tag">#education</span> <span class="tag">#English language</span> <span class="tag">#vocabulary</span> <span class="tag">#language change</span></div>
</article>
<hr>

<a id="item-11"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://github.com/graham33/nixos-dgx-spark">NixOS-DGX-Spark 项目为 NVIDIA DGX Spark 带来 Nix 和 NixOS。</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">graham33</span><span class="news-time">Aug 2, 17:05</span></div>
<p class="news-summary">新的 GitHub 项目 NixOS-DGX-Spark 提供了 USB 镜像和 NixOS 模块，让用户可以在 NVIDIA DGX Spark 默认的 DGX OS 上使用 Nix，或在这款硬件上安装完整的 NixOS。该项目还支持 Asus Ascent GX10，并附有来自 Planet Nix 的入门闪电演讲链接。 这之所以重要，是因为 DGX Spark 是 NVIDIA 的个人级 AI 超级计算机，而 NixOS 提供可重现、原子更新、可回滚的系统管理方式。该项目使 Nix 用户能够像管理普通声明式机器一样管理这款 AI 硬件，将 Nix 生态延伸到 AI 基础设施领域。 该仓库提供两条路径：在原有 DGX OS 上运行 Nix playbook，或通过 USB 镜像完整安装 NixOS。它包含一个针对 DGX Spark 系统优化的 NixOS 模块，并明确支持 NVIDIA DGX Spark 与 Asus Ascent GX10。</p>
<div class="news-background"><strong>背景</strong> NixOS 是一个围绕 Nix 包管理器构建的 Linux 发行版，用户可以用代码声明整个系统配置，并获得可重现、原子更新、支持回滚的系统。NVIDIA DGX Spark 是一台基于 Grace Blackwell (GB10) 平台的紧凑型个人 AI 超级计算机，专为本地 AI 模型开发与测试而设计。Asus Ascent GX10 则是一台同样采用 GB10 的迷你 AI 工作站，因此同一套 NixOS 支持能够同时覆盖两款设备。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NixOS">NixOS</a></li>
<li><a href="https://www.nvidia.com/en-us/products/workstations/dgx-spark/">Personal AI Supercomputer Powered by Blackwell | NVIDIA DGX Spark</a></li>
<li><a href="https://www.linkedin.com/posts/sama-bali-57b68650_how-the-asus-ascent-gx10-is-transforming-activity-7402051543002361856-2wTQ">How the ASUS Ascent GX 10 Is Transforming AI in Higher Education...</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者的反馈非常积极：有人表示已在多台 Asus GX10 上通过 k3s 运行该方案并部署了新的 DeepSeek 模型，也有人称它对自己管理 DGX Spark 帮助极大。另一条相关评论提到 microvm.nix 支持基于 Firecracker 的沙箱，从而使整个 AI 工作流管线都可以跑在 NixOS 上。还有一条稍微跑题的评论称赞 Claude Code 等 AI 编程工具在编写 Nix 时尤为高效。</div>
<div class="news-tags"><span class="tag">#NixOS</span> <span class="tag">#NVIDIA</span> <span class="tag">#DGX Spark</span> <span class="tag">#hardware</span> <span class="tag">#AI infrastructure</span></div>
</article>
<hr>

<a id="item-12"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.nbcsandiego.com/nbc-7-responds-2/californians-data-deletion-requests-drop-become-enforceable-aug-1/4054771/">加州 DROP 数据删除请求自 8 月 1 日起强制执行</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">MilnerRoute</span><span class="news-time">Aug 2, 22:16</span></div>
<p class="news-summary">自 2026 年 8 月 1 日起，加州的删除请求与退出平台（DROP）正式生效，要求注册数据经纪人处理并执行加州居民的删除请求。任何加州居民只需在 DROP 上提交一次请求，即可同时删除所有注册数据经纪人持有的个人数据。 这为加州居民提供了便捷、官方的数据删除途径，并可能为其他州制定类似的‘删除法案’树立先例。这也给长期缺乏消费者直接控制的数据经纪人行业带来了合规压力。 DROP 平台会自动向全部 545 家注册数据经纪人发送删除请求，并在提交过程中对用户数据进行哈希处理以保护隐私，且对居民免费。尽管强制执行自 2026 年 8 月 1 日开始，数据经纪人在该日期之前不需要开始处理 DROP 请求；该项目由加州隐私保护局（California Privacy Protection Agency）监督。</p>
<div class="news-background"><strong>背景</strong> 《删除法案》（SB 362）于 2023 年签署成为法律，创建了 DROP，旨在帮助加州居民行使《加州消费者隐私法》（CCPA）和《加州隐私权法》（CPRA）下的数据删除权。数据经纪人是指从并非直接互动的消费者处收集并出售个人信息的商家。DROP 由加州隐私保护局运营，为消费者提供了一个向所有注册经纪人发送删除请求的单一门户。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://mydatakey.org/drop/">California DROP – MyDataKey – Personal Data Ownership</a></li>
<li><a href="https://www.adscriptly.io/en/news/california-drop-delete-data-privacy-2026">155K Californians Erased Their Data for Free: How DROP Works</a></li>
<li><a href="https://my-fp.com/california-launches-drop-platform-delete-data-brokers/">California Launches DROP Platform to Let Residents Delete Data ...</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者对其他州能采用类似法律表示期待，并讨论了实际担忧，如加州能否对总部位于外州的数据经纪人处以罚款。一位用户抱怨说，在把电话号码交给 Dun &amp; Bradstreet 后遭遇了持续不断的垃圾电话和短信，还有用户设想构建一项服务来自动发送每月的删除请求。还有人开玩笑说，用名为‘drop’的数据表来记录请求日志可能会带来一些有趣的数据库问题。</div>
<div class="news-tags"><span class="tag">#data privacy</span> <span class="tag">#regulation</span> <span class="tag">#California</span> <span class="tag">#data deletion</span> <span class="tag">#enforcement</span></div>
</article>
<hr>

<a id="item-13"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://fstar-lang.org/">F*：面向证明的通用编程语言</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">ducktective</span><span class="news-time">Aug 2, 12:31</span></div>
<p class="news-summary">F* 的官网被分享到 Hacker News，引起人们对这种面向证明的编程语言的关注。F* 是由微软研究院和 Inria 开发的通用语言，允许开发者同时编写程序和由机器检查的数学证明。 F* 为通用软件开发中的形式化验证提供了一条实用路径，其类型系统足够强大，可以表达功能正确性和安全属性。它能够将代码提取到 OCaml、F#、C 和 WebAssembly 等语言，因此与高可信系统（包括加密软件和迁移的 C 代码库）密切相关。 F* 的类型系统结合了依赖类型、精化类型和单子效应。验证由基于 SMT 的类型检查器执行，并支持手动证明；程序可以通过配套工具编译为 OCaml、F#、C、WebAssembly 或汇编语言。</p>
<div class="news-background"><strong>背景</strong> 形式化验证是通过数学方法证明系统满足其规范的做法，而 F* 这样的面向证明的编程语言将规范直接嵌入类型系统。F* 受到 OCaml 和 F# 等 ML 家族语言的启发，是微软研究院与 Inria 的联合项目。这使得开发者可以在开发过程中而非事后验证属性，使 F* 成为高可信软件大趋势的一部分。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/F*_(programming_language)">F* (programming language)</a></li>
<li><a href="https://fstar-lang.org/">F*: A Proof - Oriented Programming Language</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者反应不一：有人批评官网缺少代码示例，要求首先展示语法和用例；另有人称赞 F* 支持通过调用外部库来逐步迁移现有 C 代码库。有用户询问 F* 是否用于工业界，还有人指出了官方教程。总体而言，讨论反映了对该语言实用性和采用情况的兴趣，以及改进展示方式的呼声。</div>
<div class="news-tags"><span class="tag">#formal verification</span> <span class="tag">#programming languages</span> <span class="tag">#proof assistants</span> <span class="tag">#functional programming</span></div>
</article>
<hr>

<a id="item-14"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.theverge.com/ai-artificial-intelligence/974209/fenix-flexin-billboard-hot-100-rubberz-ai-slop">Fenix Flexin 的 Hot 100 热歌《Rubberz》被质疑为 AI 垃圾内容</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">The Verge AI</span><span class="news-time">Aug 1, 18:20</span></div>
<p class="news-summary">The Verge 调查了 Fenix Flexin 的 Billboard Hot 100 单曲《Rubberz》，并认为它很可能是 AI 生成的，依据是歌词毫无逻辑、音频伪影以及艺术家未能提供原始录音文件。Fenix Flexin 否认了这些指控，但未提供确凿的真实性证明。 这一案例突显了行业日益增长的担忧：AI 生成的音乐可能正在进入主流排行榜，模糊了人类与机器创作之间的界限。这也表明，要最终证明或反驳一首歌是否为 AI 参与制作有多困难，影响波及艺术家、听众和音乐平台。 这首歌在 Billboard Hot 100 上排名第 58 位，标志着 Fenix Flexin 以 West Coast trap 说唱闻名的风格发生了戏剧性转变。Charlie Harding、King 和 Anthony Fantano 等专家指出了音频异常，如脆弱的 hi-hat、低比特率副歌人声和突然切断的混响尾音，而 Fenix 发布的 Pro Tools 工程剪辑也被认为不足以证明什么。</p>
<div class="news-background"><strong>背景</strong> AI 垃圾内容（AI slop）指使用生成式 AI 制作的低质量数字内容，通常被认为缺乏用心、品质或意义。在音乐领域，AI 生成的曲目可能表现出特定的音频伪影和不通顺的歌词，但这些只是间接线索，而非确凿证据。艺术家也可以合理地改变风格，因此关于《Rubberz》的争论关键在于技术证据以及原始工程文件是否公开。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_slop">AI slop - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/pulse/what-ai-slop-means-materials-rd-materials-zone-u5ngf">What “ AI Slop ” Means in Materials R&amp;D</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI music</span> <span class="tag">#Billboard</span> <span class="tag">#authenticity</span> <span class="tag">#lyric analysis</span> <span class="tag">#AI slop</span></div>
</article>
<hr>

<a id="item-15"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.interconnects.ai/p/latest-open-artifacts-23-laguna-s21">Laguna S2.1、Inkling 和 Kimi K3 证明开放模型正处于帕累托前沿</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Interconnects (Nathan Lambert)</span><span class="news-time">Aug 2, 13:01</span></div>
<p class="news-summary">Interconnects 的开放模型清单第 23 期指出，近期开源的模型——Laguna S2.1、Inkling 和 Kimi K3——表明开放模型在性能与效率的帕累托前沿上具有竞争力。文章还强调，尽管此前有人预测行业将走向整合，但越来越多的实验室正在训练并开放发布强大的模型。 这挑战了只有少数大规模实验室才能开发出前沿模型的说法，并表明开源生态在 AI 领域的作用日益重要。同时，这对需要在性价比与合规性之间权衡的从业者，以及围绕开放权重 AI 的政策讨论都具有重要意义。 文章列举了具体案例：poolside 的 Laguna-S-2.1 是一个 118B-A8B 的混合专家模型，可运行在 DGX Spark 上，并采用 OpenMDW 许可证；腾讯的 Hy3（295B-A21B）改用 Apache 2.0 许可证，并据称协助证明了一道长达 50 年的数学题。另一个亮点是美团 LongCat-2.0，这是一个具有 1.6T 参数的 MoE 模型，完全基于华为昇腾 910 芯片训练。</p>
<div class="news-background"><strong>背景</strong> 帕累托前沿来自多目标优化，指的是一组解，其中没有任何解能在所有目标上优于其他解；对 AI 模型而言，它通常表示能力、成本与效率之间的权衡。混合专家（MoE）是一种深度学习架构，它将 token 路由到部分参数，从而在提升模型容量的同时保持可承受的推理成本。开放权重模型公开了训练后的参数，降低了微调与研究的门槛。这篇文章在美中实验室均快速推进开源 AI 的背景下发布。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pareto_frontier">Pareto frontier</a></li>
<li><a href="https://medium.com/ramses-engineering/not-one-brain-but-many-how-mixture-of-experts-moe-makes-ai-smarter-and-faster-568f41220852">Not One Brain, But Many: How Mixture of Experts ( MoE )... | Medium</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#open models</span> <span class="tag">#LLM</span> <span class="tag">#Pareto frontier</span> <span class="tag">#AI research</span> <span class="tag">#model releases</span></div>
</article>
<hr>

<a id="item-16"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://blog.gaborkoos.com/posts/2026-08-03-Your-JSON-Is-Lying-to-You/">JSON.stringify 会静默丢失整数精度与数据类型</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 3, 01:40</span></div>
<p class="news-summary">文章演示了 JSON.stringify(9007199254740993) 会输出 9007199254740992，大整数被静默改变。它还展示了在 JSON 往返过程中，undefined 属性会被丢弃、Date 对象会变成 ISO 字符串、NaN 会变成 null。 由于 JSON.stringify 和 JSON.parse 是 JavaScript 中最常见的序列化往返方式，这些静默转换可能会破坏真实应用中的标识符、时间戳等值。那些假设 JSON 是无损克隆机制的开发者，可能会因此引入难以排查的隐蔽缺陷。 文章指出，可选的 replacer 函数会在 Date 对象的 toJSON() 方法将其转换为字符串之后才收到该值，而数组形式的 replacer 则充当对象属性的白名单。文章总结道，JSON.parse(JSON.stringify(value)) 是一种转换，而非通用的深拷贝。</p>
<div class="news-background"><strong>背景</strong> JSON 大约在 2001 年出现，作为一种轻量级数据交换格式，由 Douglas Crockford 推广，2006 年由 RFC 4627 正式规范，当前标准是 2017 年发布的 RFC 8259。JavaScript 中的所有数字都以 IEEE 754 双精度浮点数存储，因此大于 Number.MAX_SAFE_INTEGER（9007199254740991）的整数无法被精确表示。Date.prototype.toJSON() 将日期序列化为 UTC ISO 字符串，这就是 JSON 往返后原始 Date 类型丢失的原因。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify">JSON . stringify () - JavaScript | MDN</a></li>
<li><a href="https://www.freecodecamp.org/news/how-to-understand-the-safe-integer-limit-in-javascript/">How to Understand the Safe Integer Limit in JavaScript</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toJSON">Date .prototype. toJSON () - JavaScript | MDN</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#JavaScript</span> <span class="tag">#JSON</span> <span class="tag">#Precision</span> <span class="tag">#Serialization</span> <span class="tag">#Web Development</span></div>
</article>
<hr>

<a id="item-17"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://lemire.me/blog/2026/08/02/how-fast-is-c26s-stdhive/">C++26 的 std::hive：比 list 更好，但比 vector 更慢</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 2, 18:28</span></div>
<p class="news-summary">Daniel Lemire 使用 plf::hive 实现，在 Intel Xeon Gold 6548N 上以 GCC 16.1 对 C++26 新增的 std::hive 容器进行了基准测试，向其中追加并遍历了 100 万个 uint64_t 元素。他发现 hive 的遍历速度比 std::vector 慢约 8 倍，与 std::list 大致相当，而追加成本约为 vector 的两倍。 std::hive 是 C++26 中首个既提供连续内存块局部性、又提供引用稳定性和常数时间删除的容器，填补了 vector 与 list 之间长期存在的空白。这些基准结果让 C++ 开发者获得了具体数据，了解何时用 std::hive 替代 std::list 是合适的，以及何时它无法与 std::vector 的性能匹敌。 hive 在内部是内存块的链表，每个块带有一个 skipfield——即每个槽位的小整数，用于告诉迭代器要跳过多少个已删除的槽位。目前还没有标准库提供 std::hive，因此该基准测试使用了 Matt Bentley 的 plf::hive；结果显示 hive 的遍历与 list 一样受延迟限制，并且与紧密打包的 vector 相比，每个 8 字节元素大约多占用 1 字节内存。</p>
<div class="news-background"><strong>背景</strong> C++ 容器传统上需要在两种取舍之间选择：std::vector 将元素连续存储以获得快速遍历，但在扩容或删除元素时会使指针和引用失效；而 std::list 保持元素地址稳定，但需要逐元素分配内存并导致指针追逐。std::hive 是 C++26 新增的容器，旨在结合两者的优点：元素存放在连续块中，扫描时对缓存友好，同时引用保持有效，并且可以常数时间删除任意元素。该基准还体现了自动向量化（autovectorization），即编译器将标量循环转换为 SIMD 操作；这正是 vector 遍历每个元素平均只需退休一条指令的原因。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://lemire.me/blog/2026/08/02/how-fast-is-c26s-stdhive/">How fast is C+ + 26 ’s std :: hive ? – Daniel Lemire&#x27;s blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/Automatic_vectorization">Automatic vectorization - Wikipedia</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#C++</span> <span class="tag">#C++26</span> <span class="tag">#Performance</span> <span class="tag">#Containers</span> <span class="tag">#Benchmark</span></div>
</article>
<hr>

<a id="item-18"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://blog.netbsd.org/tnf/entry/netbsd_11_0_released">NetBSD 11.0 历经漫长开发周期后发布</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 1, 17:57</span></div>
<p class="news-summary">NetBSD 项目已正式宣布发布 NetBSD 11.0，这是这款开源类 Unix 操作系统的一个新主要版本。安装说明和可启动镜像现已通过项目 CDN 提供下载。 作为 BSD 家族中可移植性最强的操作系统之一的重要版本更新，NetBSD 11.0 对系统软件爱好者和嵌入式开发者意义重大。它还展示了志愿者驱动型项目在安全漏洞报告数量不断增加的背景下如何管理发布流程。 此次发布将 ISO 镜像拆分为小于 700MB 的 CD-ROM 版本和完整的 DVD 版本；使用闪存介质（如 U 盘）的用户必须使用解压后的 .img 文件而非 .iso 镜像。项目公开列出了三个未解决的安全问题（hdaudio、ipfilter 和 pf），它们将在计划于两个月内发布的 11.1 版本中修复。</p>
<div class="news-background"><strong>背景</strong> NetBSD 是一款免费、开源的类 Unix 操作系统，以强调可移植性和简洁设计著称，支持极为广泛的硬件平台。新主要版本的发布需要在所有支持的架构上经历完整的构建、测试和候选版本周期。对于 ARM 设备，项目提供预配置了 U-Boot 的镜像；U-Boot 是一种广泛使用的开源引导加载程序。本次发布延期部分是因为等待第三方组件发布稳定版本。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://docs.u-boot-project.org/en/latest/develop/distro.html">Generic Distro Configuration Concept — Das U - Boot unknown version...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#NetBSD</span> <span class="tag">#operating system</span> <span class="tag">#release</span> <span class="tag">#BSD</span> <span class="tag">#open source</span></div>
</article>
<hr>

<a id="item-19"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://rachelbythebay.com/w/2026/07/09/pipe/">写入时出现 EPIPE 可能说明管道处理方式有误</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 2, 08:35</span></div>
<p class="news-summary">Rachel by the Bay 在 2026 年 7 月 9 日的博文中指出，在 Unix 中调用 write() 时遇到 EPIPE，通常意味着程序处理管道的方式有误。该文将 EPIPE 视为设计缺陷的症状，而非需要常规处理的错误。 EPIPE 处理是 Unix 经典陷阱，影响写入 socket 或管道的命令行工具和长驻进程。该文挑战了常见的“忽略 SIGPIPE”或“把 EPIPE 当作可恢复错误”的建议，可能改变开发者设计基于管道的程序的方式。 EPIPE 出现在进程向读端已关闭的管道写入时；通常以 SIGPIPE 信号形式传递，除非该信号被忽略或捕获。该文的观点暗示，设计良好的程序要么通过 SIGPIPE 正常终止，要么确保读端仍然打开，而不是捕获 EPIPE 后继续执行。</p>
<div class="news-background"><strong>背景</strong> 在 Unix 中，管道是单向数据通道：一个进程写入，另一个进程读取。如果读取进程退出或关闭管道，生产者随后的 write() 会触发 SIGPIPE，默认终止生产者；如果 SIGPIPE 被忽略，write() 则返回 EPIPE 错误。许多程序员为处理网络 socket 而屏蔽 SIGPIPE，但这会掩盖管道中的断管情况，导致写入时出现令人困惑的 EPIPE。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.pixelbeat.org/programming/sigpipe_handling.html">Effectively handling the SIGPIPE informational signal</a></li>
<li><a href="https://stackoverflow.com/questions/2235938/what-can-cause-a-spontaneous-epipe-error-without-either-end-calling-close-or-c">unix - What can cause a spontaneous EPIPE error ... - Stack Overflow</a></li>
<li><a href="https://unix.stackexchange.com/questions/550396/why-am-i-getting-this-broken-pipe-error/550441">c - Why am I getting this [ Broken pipe ] error ? - Unix &amp; Linux Stack...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#unix</span> <span class="tag">#pipes</span> <span class="tag">#error-handling</span> <span class="tag">#programming</span> <span class="tag">#systems</span></div>
</article>
<hr>

<a id="item-20"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.joelonsoftware.com/2000/04/10/controlling-your-environment-makes-you-happy/">控制环境让你更快乐：Joel Spolsky 的 UI 设计之道</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 2, 21:10</span></div>
<p class="news-summary">2000 年 4 月，Joel Spolsky 发表文章，认为 UI 设计是理性且有条理的，而非神秘的艺术工作。他将优秀的界面设计建立在 Martin Seligman 的习得性无助理论之上，指出当软件让用户感到能控制环境时，用户才会快乐。 这篇文章提出了一条经典设计原则：用户的快乐取决于掌控感，因此软件必须完全符合用户预期。它为早期软件设计讨论提供了框架，对当今产品团队和用户体验从业者依然具有参考价值。 Spolsky 的核心准则是：当程序的行为与用户预期完全一致时，这个用户界面就是设计良好的。他还否定了 UI 设计需要艺术天赋的看法，将细微的界面挫折比作空格键卡住或前门钥匙转不动等日常烦恼。</p>
<div class="news-background"><strong>背景</strong> 习得性无助（learned helplessness）是 Martin E. P. Seligman 提出的心理学理论，描述个体在反复经历无法控制的负面刺激后所表现出的行为。对人类而言，该理论与自我效能感和抑郁相关，认为感知到缺乏控制会导致不快乐。Spolsky 将其应用到软件领域：当用户无法控制程序时，他们会感到无助，并把责任归咎于软件而不是自己。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Learned_helplessness">Learned helplessness - Wikipedia</a></li>
<li><a href="https://www.simplypsychology.org/learned-helplessness.html">Learned Helplessness : Seligman&#x27;s Theory of Depression</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#UI design</span> <span class="tag">#user experience</span> <span class="tag">#software design</span> <span class="tag">#Joel Spolsky</span></div>
</article>
<hr>

<a id="item-21"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://blog.juni-mp4.com/posts/42/rooting-the-tplink-tl841n-pt1/">TP-Link TL-841N 路由器 Rooting 分析发现硬编码且重置后仍有效的凭据</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 2, 18:32</span></div>
<p class="news-summary">一篇技术博文详细描述了如何对 TP-Link TL-841N 路由器进行 rooting 并分析其固件，发现了在恢复出厂设置后依然有效的硬编码凭据。 这一发现凸显了 IoT/嵌入式设备面临的严重安全风险，硬编码的后门凭据可能让攻击者在设备重置后依然重新获得访问权限。这也强调了厂商进行固件审计和负责任凭据管理的重要性。 受影响的设备是低端家用路由器 TP-Link TL-841N，由于凭据嵌入在固件中，因此恢复出厂设置后依然存在。该博文标记为第一部分，后续可能发布更多技术发现。</p>
<div class="news-background"><strong>背景</strong> Rooting 路由器意味着获得其操作系统的特权访问，通常通过利用漏洞或提取和修改固件的方式实现。固件分析涉及检查设备的软件镜像，以发现隐藏功能、后门或凭据。硬编码凭据是直接嵌入固件或源代码中的密码或用户名，通常在同一型号的所有设备上相同。重置后依然存在的凭据在恢复出厂设置后仍然有效，因此知道这些凭据的攻击者即使在设备被擦除后也能重新获得控制。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.forescout.com/blog/new-tp-link-router-vulnerabilities-a-primer-on-rooting-routers/">New TP-Link Router Vulnerabilities: A Primer on Rooting Routers</a></li>
<li><a href="https://www.cyclonis.com/what-is-hardcoded-password/">What Is a Hardcoded Password ?</a></li>
<li><a href="https://www.offsec.com/metasploit-unleashed/persistent-backdoors/">Metasploit Unleashed | Persistent Backdoors</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#security</span> <span class="tag">#firmware</span> <span class="tag">#reverse engineering</span> <span class="tag">#IoT</span> <span class="tag">#embedded</span></div>
</article>
<hr>