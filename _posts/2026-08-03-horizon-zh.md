---
layout: default
title: "Horizon 每日速递：2026-08-03"
date: 2026-08-03
lang: zh
---

> 📅 2026-08-03 · 从 58 条资讯中精选出 16 条重要内容

---

1. [Karpathy 的鹈鹕推文引发矢量图形基准测试讨论](#item-1) ⭐️ 8.0/10
2. [Rust 1.98 引入代数运算符加速浮点运算](#item-2) ⭐️ 8.0/10
3. [AI 数学家：对 OpenAI 数学突破的警示](#item-3) ⭐️ 8.0/10
4. [Lean 内核健全性漏洞 #14576 事后分析](#item-4) ⭐️ 8.0/10
5. [Kakehashi：在 Linux ARM 上运行 macOS 二进制的实验性用户态](#item-5) ⭐️ 7.0/10
6. [F*：面向证明的通用编程语言](#item-6) ⭐️ 7.0/10
7. [AI 测评：生成哈布斯堡青蛙 SVG](#item-7) ⭐️ 7.0/10
8. [eBay 高管因骚扰批评者获刑 公司支付 5600 万美元](#item-8) ⭐️ 7.0/10
9. [Meshdiff：在浏览器中直观比较两个 STL 版本](#item-9) ⭐️ 7.0/10
10. [公开信揭示 AI 发展、开放权重与蒸馏技术之争](#item-10) ⭐️ 7.0/10
11. [数学与理论计算机科学的十项进展](#item-11) ⭐️ 7.0/10
12. [开源模型盘点：Laguna S2.1、Inkling、Kimi K3 在帕累托前沿表现出色](#item-12) ⭐️ 7.0/10
13. [C 语言中解析 sizeof 比想象中更难](#item-13) ⭐️ 7.0/10
14. [基准测试 C++26 新容器 std::hive](#item-14) ⭐️ 7.0/10
15. [NetBSD 11.0 重大版本正式发布](#item-15) ⭐️ 7.0/10
16. [对 TP-Link TL-841N 进行 root 并发现硬编码的重置持久化凭据](#item-16) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Karpathy 的鹈鹕推文引发矢量图形基准测试讨论](https://twitter.com/karpathy/status/2083749667410727319) ⭐️ 8.0/10

Andrej Karpathy 发布了一条关于用矢量图形语言绘制的鹈鹕的推文，引发了 345 条评论的讨论。讨论聚焦于此类绘图任务是否可作为评估 AI 模型物理世界理解能力的新基准。 这之所以重要，是因为它提出了一种定性基准，可以揭示前沿模型是否真正理解空间和物理关系，而不仅仅是像素级图像生成。这场讨论可能鼓励研究者将矢量图形任务作为补充评估指标，尤其是评论者指出模型在将元素排列成连贯、可玩的结构时经常失败。 这条推文获得了 345 条评论；有人指出，与 Simon Willison 早先的鹈鹕示例不同，此次并未公开提示词，导致结果无法复现。还有人提到历史先例，例如微软在 GPT-4 预发布评估中要求模型用 TikZ 画独角兽，并提出类似失败案例，如创建可玩的弹球游戏。

hackernews · delichon · Aug 2, 04:05

**背景**: 矢量图形语言（如 SVG 和 TikZ）用数学指令（圆、线条、路径）而非像素来描述图像，因此生成这类图形要求模型理解空间布局和物理合理性。将这类基于代码的绘图任务作为基准，可以揭示模型是否真正理解物理世界，从而补充传统图像质量指标。近期如 VectorGym 等研究已开始围绕 SVG 代码生成构建多任务基准，而具身 AI 研究也通过 Vision-Language-Action 模型强调物理理解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gist.science/paper/2603.29852">VectorGym: A Multitask Benchmark for SVG Code... | Gist.Science</a></li>
<li><a href="https://www.linkedin.com/posts/reka-ai_physicalai-worldmodels-ai-activity-7480294929605480449-kvZR">Reka Labs Research on VLMs and Physical Understanding | Reka AI ...</a></li>

</ul>
</details>

**社区讨论**: 评论者大多认为，不完美的输出恰恰是重点所在，因为这类任务可作为定性基准，揭示物理世界理解能力并用于衡量未来进展。但也有人提出复现性问题，因为提示词未公开；其他人则分享了相关经验，例如创建可玩弹球游戏的失败，以及历史上 GPT-4 的 TikZ 独角兽提示。

**标签**: `#AI`, `#Machine Learning`, `#Benchmarks`, `#Karpathy`, `#Vector Graphics`

---

<a id="item-2"></a>
## [Rust 1.98 引入代数运算符加速浮点运算](https://pythonspeed.com/articles/faster-float-math-rust/) ⭐️ 8.0/10

Rust 1.98 引入了新的代数算术运算符，允许编译器利用实数代数性质（如改变运算顺序）来优化浮点运算。这为开发者提供了一种稳定的方式来加速数值代码，同时在需要精度的地方仍可使用严格运算符。 浮点运算通常比整数运算慢，因为编译器必须保持严格的 IEEE 754 语义。这个新 API 能让 Rust 中性能关键的数值代码运行得更快，可能使 Rust 在科学计算、数据处理和机器学习工作负载中更具吸引力。 文章中的成对求和示例使用代数运算符后速度约为原来的两倍，从 628.7 微秒降至 371.1 微秒，每个值的 CPU 指令数从 4.5 降至 1.0。开发者可以在同一算法中混合使用严格运算符和代数运算符，以平衡速度与舍入误差控制。

rss · Lobsters · Aug 2, 20:27

**背景**: 浮点运算并不遵循实数的所有代数定律——例如，(X + Y) + Z 可能因舍入和特殊值而与 X + (Y + Z) 不同。因此编译器通常保持保守，除非明确允许，否则不会对浮点运算进行重排或重新结合。Rust 1.98 的新代数运算符可选择启用此类优化，使程序员能够进行细粒度控制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.intel.com/content/www/us/en/docs/dpcpp-cpp-compiler/developer-guide-reference/2025-2/floating-point-optimizations.html">Floating-Point Optimizations</a></li>
<li><a href="https://software-dl.ti.com/ccs/esd/documents/sdto_cgt_floating_point_optimization.html">Floating Point Optimization - Texas Instruments</a></li>

</ul>
</details>

**标签**: `#Rust`, `#floating point`, `#performance`, `#compiler optimization`, `#numerical computing`

---

<a id="item-3"></a>
## [AI 数学家：对 OpenAI 数学突破的警示](https://borretti.me/article/mathematics-without-mathematicians) ⭐️ 8.0/10

这篇文章对 OpenAI 宣布其未发布模型解决十个数学开放问题（其中包括一个编码理论问题）作出回应。作者认为人们会编造各种合理化说辞（“应对机制”）来淡化其意义，但 AI 最终将在品味和直觉上超越人类数学家。 数学是科学的基础，不同于国际象棋等封闭游戏，因此超人级别的 AI 数学家将具有实质性的用途，可能加速众多领域的技术进步。这篇文章凸显了一个未来：人类可能沦为远比自身强大的 AI 实体所豢养的“宠物”，由此引发关于人类智力工作价值的生存性问题。 作者承认自己只能判断编码理论那一项成果的重要性，其余则依赖他信任的数学家。他预见并反驳了几种“应对机制”，包括人类将引导 AI 或教授 AI 的发现，并指出最强的技术反驳理由是强化学习在可验证领域之外可能无法很好地泛化。

rss · Lobsters · Aug 2, 09:30

**背景**: 编码理论（有时称为代数编码理论）研究如何设计纠错码，以便在嘈杂的信道上可靠地传输信息，它使用有限域和多项式代数等代数技术。形式化数学则是将证明以机器可检查的形式语言表达出来，从而让计算机验证其正确性；Lean 等工具即用于此目的。文章在讨论 OpenAI 所称的成果时，假设读者熟悉这些概念。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Coding_theory">Coding theory - Wikipedia</a></li>
<li><a href="https://xenaproject.wordpress.com/2021/01/21/formalising-mathematics-an-introduction/">Formalising mathematics: an introduction. - Xena Project</a></li>

</ul>
</details>

**标签**: `#AI`, `#mathematics`, `#OpenAI`, `#research`, `#technology impact`

---

<a id="item-4"></a>
## [Lean 内核健全性漏洞 #14576 事后分析](https://leodemoura.github.io/blog/2026-8-1-postmortem-for-kernel-soundness-bug-14576/) ⭐️ 8.0/10

2026 年 7 月 28 日，Kiran Gopinathan 报告了 Lean 定理证明器中的内核健全性漏洞 #14576，并给出了一个利用嵌套归纳类型处理缺陷来证明 False 的示例。Lean FRO 在一小时内推送了修复（#14577），并发布了新的补丁版本。 证明助手内核的健全性漏洞会动摇对形式化证明的信任；该事件表明内核可通过元编程被攻击，而独立内核检查仍然有价值，但需要用户使用最新版本。该漏洞也影响 lean4lean 等依赖工具。 该漏洞的成因是：当内核消除带有幻影参数 Ds 的归纳类型 T 下的嵌套出现时，这些幻影参数会从生成的辅助类型中消失，从而逃过类型检查，使类型错误的参数可能让内核接受 False 的证明。该漏洞只能通过元编程触达，且前端通常能捕获此类类型错误，因此这是一个实现 bug，而非元理论漏洞。独立的 Rust 检查器 nanoda 最初未发现该利用，原因在于它自身有一个一周前才修复的独立 bug。

rss · Lobsters · Aug 1, 21:51

**背景**: Lean 是一种基于带归纳类型的构造演算（Calculus of Inductive Constructions）的证明助手，其内核是检查所有证明的小型可信核心。内核中的健全性漏洞可能使无效证明被接受，从而威胁形式化验证的可靠性。像 nanoda 这样的独立内核用单独的实现在官方内核之外重新检查 Lean 证明，以帮助发现官方内核中的漏洞。此事还与 Mario Carneiro 正在进行的 Lean 类型理论形式化项目 lean4lean 相关，该项目对归纳类型的处理是对参考实现的一次移植。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant) - Wikipedia</a></li>
<li><a href="https://lawrencecpaulson.github.io/2026/07/30/Collatz.html">Why is it all in the kernel ?</a></li>
<li><a href="https://seclists.org/oss-sec/2026/q3/381">oss-sec: Lean 4 kernel soundness bug: forging proofs via nested...</a></li>

</ul>
</details>

**标签**: `#Lean`, `#theorem prover`, `#kernel soundness`, `#formal verification`, `#bug postmortem`

---

<a id="item-5"></a>
## [Kakehashi：在 Linux ARM 上运行 macOS 二进制的实验性用户态](https://github.com/wie-project/kakehashi) ⭐️ 7.0/10

Kakehashi 是一个实验性用户态翻译层，可在 Linux aarch64 上原生运行 macOS ARM64 命令行二进制文件，无需内核模块或 JIT。作者报告称已具备 7-Zip、curl 和 Git 的可运行原型，其中 7-Zip 在包含 8000 个文件的目录树中通过了多线程压缩测试，速度约为原生 Linux 执行的 5.2 分之一。 如果成功，Kakehashi 有望提供一条轻量、以命令行优先的路径，在 Linux ARM 硬件上运行 macOS 软件，从而像 Wine/Proton 之于 Windows 应用那样扩展生态。它面向需要在无需启动 macOS 虚拟机或使用 Apple 硬件的情况下使用特定 macOS 命令行工具的用户和 CI 流水线。 Kakehashi 被描述为『用户态 macOS ARM64 → Linux aarch64 翻译层』，以 CLI 为先且不含 JIT；它刻意避免使用内核模块，也不模拟 Mach 内核，而是采用类似 Wine 的惰性桩（lazy stubbing）方案。当前限制包括 GUI 应用、codesign/公证（notarization）、Xcode UI 测试，以及任何不属于 freestanding libSystem 下纯 CLI Darwin 二进制的工作负载。

hackernews · vlad_kalinkin · Aug 2, 16:26

**背景**: 应用二进制兼容性（ABI）使为一个操作系统和 CPU 架构编译的程序，在系统提供所需 ABI、系统调用和库时能够在另一个平台上运行。Wine/Proton 等项目将 Windows API 调用转换为 Linux 调用，而 Darling 旨在通过重新实现 Cocoa 和 Objective-C 运行时来运行 macOS 二进制文件；Kakehashi 则采用更窄的翻译层思路，专注 CLI 工具而非完整桌面应用。该项目处于早期阶段，有清晰的路线图，并且关于它与 Darling 的 ARM64 支持工作之间的关系仍是一个开放问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/wie-project/kakehashi">GitHub - wie-project/kakehashi: Userspace macOS translation ...</a></li>
<li><a href="https://habr.com/ru/articles/1065502/">Kakehashi : запуск macOS бинарников на Linux ARM. Часть... / Хабр</a></li>

</ul>
</details>

**社区讨论**: 评论者既感兴趣又保持谨慎，将 Kakehashi 与 Darling 进行比较，并询问能否合并力量；还有人询问类似 ROM 风格反编译方法是否可行。也有人对项目名称『Kakehashi』提出调侃，一位用户表示问题比当前早期解决方案更大，但会持续关注进展。

**标签**: `#macOS`, `#Linux`, `#ARM`, `#binary compatibility`, `#userspace`

---

<a id="item-6"></a>
## [F*：面向证明的通用编程语言](https://fstar-lang.org/) ⭐️ 7.0/10

这条新闻指向 F* 的官方网站，F* 是一种将依赖类型与基于 SMT 的证明自动化相结合的面向证明的编程语言。该首页及随后的社区讨论凸显了该语言的设计及其在已验证加密软件方面的潜力。 F* 是少数在安全关键领域（尤其是已验证密码学）具有实际应用价值的面向证明的语言之一。它将依赖类型、SMT 求解和程序提取相结合的方法，影响了形式化验证如何在工业级软件中变得实用。 F* 是 Microsoft Research 与 Inria 的联合项目，其类型系统包含依赖类型、单子效应和精化类型。默认情况下，F* 只验证代码而不执行；程序必须提取到 OCaml、F#、C、WebAssembly（借助 KaRaMeL）或汇编语言（借助 Vale）才能运行。

hackernews · ducktective · Aug 2, 12:31

**背景**: 面向证明的编程是一种将程序和证明共同设计的范式，利用类型系统来表达函数正确性、安全性等精确规范。F* 是一门受 ML、Caml 和 OCaml 启发的依赖类型语言和证明助手，它结合了 SMT 求解与基于策略的交互式定理证明。这使得编写带有机器可验证数学保证的程序成为可能，对于缺陷可能导致严重安全漏洞的加密实现尤其有价值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/F*_(programming_language)">F* (programming language) - Wikipedia</a></li>
<li><a href="https://github.com/FStarLang/FStar">GitHub - FStarLang/FStar: A Proof-oriented Programming ... Proof-oriented Programming in F* — Proof-Oriented Programming ... F* (programming language) - Wikipedia The Rise of ‘Proof-Oriented Programming’: Integration of LLMs ... Proof-Oriented Programming | 5min Dev Essentials Proof-Oriented Programming in F* - mtzguido.github.io</a></li>
<li><a href="https://fstar-lang.org/">F*: A Proof-Oriented Programming Language</a></li>

</ul>
</details>

**社区讨论**: 讨论中既有称赞也有批评。有用户欣赏 F* 支持增量迁移 C 代码库的能力，也有用户批评其首页没有在显眼位置展示代码示例或语法。还有评论者询问 F* 是否真正在工业界使用以及用于何种软件，反映出对其现实应用情况的普遍好奇。

**标签**: `#proof-oriented programming`, `#formal verification`, `#programming languages`, `#functional programming`

---

<a id="item-7"></a>
## [AI 测评：生成哈布斯堡青蛙 SVG](https://frogs.vaguespac.es/) ⭐️ 7.0/10

作者发起了一项个人 AI 基准测试，要求模型生成一个带哈布斯堡下巴的青蛙 SVG，并将结果发布在 frogs.vaguespac.es。这个另类的测试迅速在 Hacker News 上引发关于模型推理与创造力的热议。 这项基准测试提供了一种低成本、上手简单的方式来比较不同 AI 模型如何处理特定的视觉推理与创意提示。它揭示了标准基准测试常常忽略的模型行为差异，对选择或评估 AI 工具的人很有价值。 帖子走红后，该网站一度因访问量过大而瘫痪，作者表示正在提升可靠性。评论者指出，所有输出都没有从侧面绘制青蛙，还有人分享了单次生成的 Fable 5 结果，认为其表现出色。

hackernews · thebigship · Aug 2, 19:42

**背景**: 哈布斯堡下巴（Habsburg jaw）指下颌前突（mandibular prognathism），即下颌明显向外突出的状况，历史上因哈布斯堡王室近亲通婚而与之关联。SVG（Scalable Vector Graphics）是一种基于 XML 的矢量图像格式。要求 AI 生成 SVG，需要它把自然语言描述转换为精确的几何代码，涉及语言理解、视觉推理和创造力的结合。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Habsburg_jaw">Habsburg jaw</a></li>

</ul>
</details>

**社区讨论**: 评论者的反应既幽默又带分析：有人称赞 Opus 5 是最接近成功的模型，其他人则分析模型为何未能把突出的下巴与青蛙脸部有效衔接。还有几位指出没有模型尝试侧面视角，而侧面本应更容易表现下巴形状；也有人分享了自己单次生成的优秀结果，如 Fable 5。网站所有者感谢了社区，并表示网站正被过量访问'挤爆'。

**标签**: `#AI benchmarking`, `#SVG generation`, `#LLM evaluation`, `#image generation`, `#AI creativity`

---

<a id="item-8"></a>
## [eBay 高管因骚扰批评者获刑 公司支付 5600 万美元](https://www.ft.com/content/06ec1b03-d4af-40cf-b12a-4ba5a410f6d2) ⭐️ 7.0/10

eBay 高管因策划针对一对批评该公司的夫妇的骚扰活动而被判刑，并导致公司支付 5600 万美元和解金。前高级经理 Brian Gilbert 被判处已服刑时间并处罚款 2 万美元，前高级总监 Jim Baugh 被判处 57 个月监禁。 这一案件凸显了企业高管利用安全团队针对批评者的严重后果，引发了关于科技行业企业问责与监管的重要问题。它可能对类似不当行为起到震慑作用，并促使人们更密切地审视企业安全实践。 据检察官称，eBay 安全团队的七名成员（包括前警长）联手骚扰和恐吓 Steiner 夫妇。56 岁的前特别行动高级经理 Brian Gilbert 被判处已服刑时间、一年监督释放、不得接触受害者并处罚金 2 万美元；47 岁的前安全与安保高级总监 Jim Baugh 被判处 57 个月监禁。

hackernews · JumpCrisscross · Aug 2, 19:19

**背景**: 此案涉及企业针对公开批评者的报复行为。eBay 的安全团队据称对一对经营批评该公司的新闻通讯的夫妇进行了协调一致的骚扰，包括威胁和监控。这一事件导致公司支付 5600 万美元和解金，相关高管被刑事判刑。

**社区讨论**: 社区评论质疑骚扰活动是否仅限于一对夫妇，并询问其他批评者是否也曾成为目标，以及涉案的前警长是否受到适当审查。一位评论者以此案说明缺乏监督时人类行为的一种普遍现象，而另一位则转而批评 eBay 向卖家收取的费用。

**标签**: `#corporate-ethics`, `#legal`, `#security`, `#tech-industry`, `#harassment`

---

<a id="item-9"></a>
## [Meshdiff：在浏览器中直观比较两个 STL 版本](https://meshdiff.com/) ⭐️ 7.0/10

Meshdiff 是一款免费的浏览器端工具，可比较 3D 模型的两个版本，并通过体素和表面热力图差异分析精确显示变化内容——新增材料、移除材料以及尺寸漂移。它支持 STL、3MF 和 OBJ 文件，且全部在客户端本地处理，不会上传任何文件。 在 3D 打印和 CAD 工作流中，追踪文件版本之间的几何变化一直不太方便，通常需要重量级桌面软件。Meshdiff 让 STL 差异比较在浏览器中即可完成，并采用注重隐私的本地优先处理方式，对设计师、工程师和创客都很有吸引力。 该工具结合了基于体素的差异分析和表面热力图来可视化差异，网站明确说明不会向任何服务器上传任何内容。GitHub 上还提供了相关的命令行工具 TimothyStiles/meshdiff。

hackernews · projscope · Aug 2, 11:34

**背景**: STL（stereolithography，即立体光刻，也称标准三角化语言）是一种以原始三角网格描述三维物体表面的文件格式，广泛用于 3D 打印和计算机辅助制造。STL 文件不包含颜色、纹理或比例信息，只有表面几何，因此比较版本纯属几何难题，而 Meshdiff 在浏览器中解决了这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://meshdiff.com/">Meshdiff — Compare 3D Model Versions (STL, 3MF, OBJ Diff Tool)</a></li>
<li><a href="https://en.wikipedia.org/wiki/STL_(file_format)">STL (file format)</a></li>

</ul>
</details>

**社区讨论**: 社区反馈积极，用户认为该工具很方便、很酷，并赞赏其客户端/本地优先的做法。常见的功能建议包括同步或锁定视口，使三个视图一起旋转，以及增加更多展示复杂物体的演示模型；还有评论者幽默地提到，一开始误以为 STL 是 C++ 的标准模板库。

**标签**: `#3D printing`, `#STL`, `#diff tool`, `#browser app`, `#CAD`

---

<a id="item-10"></a>
## [公开信揭示 AI 发展、开放权重与蒸馏技术之争](https://simonwillison.net/2026/Aug/2/open-letters/#atom-everything) ⭐️ 7.0/10

Simon Willison 撰文总结了近期关于 AI 政策的公开信，包括微软支持的《Open Weights and American AI Leadership》（7 月 24 日，235 家公司签署）、Anthropic 的回应，以及 7 月 28 日由 1,324 名前沿 AI 公司员工签署的《Pacing the Frontier》。 这些公开信凸显了 AI 行业在开放权重模型、模型蒸馏以及自动化 AI 快速推进等问题上的严重分歧，主要企业立场各异。这些论点可能影响美国在安全、竞争和开源 AI 方面的监管决策。 第一封公开信明确将蒸馏（distillation）辩护为合法且广泛使用的技术，而 Anthropic 拒绝签署，并呼吁打击工业规模的蒸馏操作。《Pacing the Frontier》引用了现实中的加速案例：Anthropic 80%的代码由 Claude Code 编写，OpenAI 的 Sol 将端到端服务成本降低 20%，Kimi K3 则为基于自身架构的 nano 模型设计了芯片。

rss · Simon Willison · Aug 2, 04:16

**背景**: 开放权重模型（open-weights models）会公开训练好的神经网络权重，让开发者可以检查、微调和集成这些模型，这与完全封闭的模型不同。知识蒸馏（knowledge distillation）是一种机器学习技术，较小的“学生”模型通过模仿较大的“老师”模型来学习，常用于模型压缩和优化。这场争论的核心在于：这些做法究竟是通过透明度让 AI 更安全，还是会增加滥用风险并导致权力集中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://www.cnet.com/tech/services-and-software/openais-new-models-arent-really-open-what-to-know-about-open-weights-ai/">OpenAI's New Models Aren't Really Open : What to Know... - CNET</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#open weights`, `#model distillation`, `#AI development`

---

<a id="item-11"></a>
## [数学与理论计算机科学的十项进展](https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/#atom-everything) ⭐️ 7.0/10

Simon Willison 的链接博客汇总了十项近期进展，重点提到 OpenAI 宣称其内部版本 Astra 以每个问题不到 2,000 美元的 GPT-5.6 Sol token 成本，解决了十个长期停滞的数学问题。此前 Anthropic 也宣布 Claude Mythos Preview 在花费 10 万美元 token 后发现了密码学弱点。 这些成果表明 AI 系统正从辅助工具转变为数学与理论计算机科学中的活跃贡献者，有可能加速那些数十年未获进展领域的发现。数学家的反应既包含兴奋也包含存在性忧虑，而 Terence Tao 等人则将其视为迈向‘big mathematics（大数学）’——人机大规模协作——的催化剂。 OpenAI 发布了 openai/ten-proofs 仓库，包含 Lean 4 形式化证明、描述解决方案的论文，以及一份由 LLM 根据未公开推理轨迹生成的、重构证明形成过程的 PDF。Willison 对透明度表示肯定，但也指出提示词并未公开，并且没有透露有多少问题是未能解决的。

rss · Simon Willison · Aug 1, 20:34

**背景**: 近年来，大型语言模型开始被应用于数学推理和形式化证明，Lean 4 等工具让证明可以被机器检查。‘LLM-guided proof search（LLM 引导的证明搜索）’将 LLM 与形式推理引擎相结合，以自动化证明的构造与验证。这条新闻还提到 Anthropic 未公开发布的 Claude Mythos Preview，Anthropic 称该模型发现了提交给标准化工作的密码方案中的新型攻击。Terence Tao 提出的‘big mathematics（大数学）’设想人机大规模协作：AI 承担大量技术性工作，人类专注于创造性部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos">Claude Mythos - Wikipedia</a></li>
<li><a href="https://economictimes.indiatimes.com/tech/artificial-intelligence/anthropic-says-claude-uncovers-cryptographic-weaknesses-advances-ai-assisted-security-research/articleshow/132700437.cms?from=mdr">Anthropic says Claude uncovers cryptographic weaknesses, advances AI-assisted security research - The Economic Times</a></li>
<li><a href="https://www.emergentmind.com/topics/llm-guided-proof-search">LLM -Guided Proof Search</a></li>

</ul>
</details>

**标签**: `#mathematics`, `#theoretical computer science`, `#AI`, `#cryptography`, `#LLM`

---

<a id="item-12"></a>
## [开源模型盘点：Laguna S2.1、Inkling、Kimi K3 在帕累托前沿表现出色](https://www.interconnects.ai/p/latest-open-artifacts-23-laguna-s21) ⭐️ 7.0/10

最新一期 Interconnects 的 open artifacts 盘点聚焦近期开源权重模型，包括 poolside 的 Laguna S2.1、Inkling 和 Kimi K3，认为这些模型在帕累托前沿上兼具竞争力和实用性。文章指出，越来越多的机构正在训练并开源发布强大模型，例如 Thinking Machines 的开源微调服务年收入已达数亿美元。 这很重要，因为它直接挑战了关于 AI 实验室将走向整合的普遍预测，表明从初创公司到中国互联网公司的各类机构现在都能训练并开源发布强大模型。同时这也意味着开源模型正在逼近性能与效率的前沿，为从业者提供了更多可行选择。 值得注意的技术亮点包括 poolside 的 Laguna-S-2.1（118B-A8B 的混合专家模型，可运行于 DGX Spark，采用 OpenMDW 许可证），以及腾讯的 Hy3（295B-A21B 的 MoE，以 Apache 2.0 发布，并协助证明了一个有 50 年历史的数学问题）。盘点还涵盖美团 LongCat-2.0（1.6T 参数 MoE，完全基于昇腾 910 芯片训练）和 AMD 在 Instinct 显卡上训练的 Instella-MoE-16B-A3B-Think。

rss · Interconnects (Nathan Lambert) · Aug 2, 13:01

**背景**: 帕累托前沿（Pareto frontier）在此指一组在性能与成本或效率之间取得最佳平衡的模型——前沿上的任何模型都无法在不损害另一个指标的前提下变得更好。混合专家（Mixture of Experts, MoE）架构通过将每个输入只路由到少数专门的子模型（“专家”），而不是激活整个网络，从而提升效率。采用 Apache 2.0 和 OpenMDW 等宽松许可证的开源权重发布允许更广泛的使用和微调。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pareto_front">Pareto front - Wikipedia</a></li>
<li><a href="https://thenewbuilder.ai/glossary/moe">MoE — The New Builder Glossary</a></li>

</ul>
</details>

**标签**: `#open models`, `#AI/ML`, `#model releases`, `#Pareto frontier`, `#machine learning`

---

<a id="item-13"></a>
## [C 语言中解析 sizeof 比想象中更难](https://sebsite.pw/w/20260802-sizeof.html) ⭐️ 7.0/10

这篇文章剖析了 C 语言 sizeof 运算符出人意料的棘手语法，指出朴素解析在复合字面量、后缀运算符链以及 sizeof(int)+1 这样的歧义表达式上会失效。文章还指出，C2Y 新引入的 _Countof 运算符同样面临这些解析复杂性。 这种歧义会影响编译器与静态分析工具的作者，他们必须在真实 C 代码中正确区分类型名、强制转换表达式和复合字面量。正确处理这些情况可以避免误解析合法程序，尤其是在 C2Y 加入具有类似语法的运算符之后。 文章指出，虽然 sizeof 的操作数要么是一元表达式，要么是带括号的类型名，但像 (int){0} 这样的复合字面量可以合法地出现在 sizeof 之后，且整个表达式后面还可以跟后缀运算符，例如 sizeof(T){}.x[0]()。文章还提醒不要将一元表达式和强制转换表达式的解析合并成一个函数，因为 sizeof(int)+1 必须被解析为加法，而不是对强制转换表达式求大小。

rss · Lobsters · Aug 2, 06:01

**背景**: 在 C 语言中，sizeof 返回表达式或带括号类型名的字节大小；只有类型名需要括号，因此 sizeof 67 这样的表达式也是合法的。C99 引入的复合字面量使用 (type){initializer-list} 语法构造匿名对象，它与带括号的类型名或强制转换表达式在开头部分完全相同。这种重叠使得解析器在不做仔细预读或回溯时面临真实的语法歧义，而即将到来的 C2Y 标准引入的 _Countof 运算符也遵循相同的语法模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.cppreference.com/c/language/compound_literal">Compound literals (since C99) - cppreference.com</a></li>
<li><a href="https://gcc.gnu.org/onlinedocs/gcc/Compound-Literals.html">Compound Literals (Using the GNU Compiler Collection (GCC))</a></li>
<li><a href="https://github.com/cc65/cc65/issues/2530">Countof operator ( C 2 y ) · Issue #2530 · cc65/cc65 · GitHub</a></li>

</ul>
</details>

**标签**: `#C`, `#parsing`, `#compilers`, `#programming-languages`, `#sizeof`

---

<a id="item-14"></a>
## [基准测试 C++26 新容器 std::hive](https://lemire.me/blog/2026/08/02/how-fast-is-c26s-stdhive/) ⭐️ 7.0/10

Daniel Lemire 在最新博文中对 C++26 标准库新增的 std::hive 容器进行了基准测试。评测重点是比较它在遍历元素时与其他标准容器的性能表现。 std::hive 是一个新的标准容器，目标是在保持良好的缓存局部性的同时，提供快速插入和删除能力。这项基准测试让 C++ 开发者可以及早了解该容器在实践中是否实现了其设计目标。 std::hive 被描述为游戏编程中常用的“bucket array”容器的形式化与优化版本。与 std::vector 类似，它将元素存储在连续的内存块中，因此遍历时无需逐个元素进行指针跳转。

rss · Lobsters · Aug 2, 18:28

**背景**: 在 C++ 中，std::vector 连续存储元素，具有极佳的缓存局部性，但中间位置的插入和删除代价较高。std::list 支持 O(1) 的插入和删除，但由于每个元素都需要指针跳转，缓存局部性较差。std::hive 旨在占据两者之间的中间地带：比 std::list 拥有更好的缓存局部性，同时比 std::vector 拥有更快的插入和删除速度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lemire.me/blog/2026/08/02/how-fast-is-c26s-stdhive/">How fast is C++26’s std::hive?</a></li>
<li><a href="https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2023/p0447r21.html">Introduction of std::hive to the standard library</a></li>
<li><a href="https://x.com/ChShersh/status/2083196856113242587">Dmitrii Kovanikov on X: "std::hive is my new favourite data structure in C++26. Aka a linked list of fixed-size arrays. It provides better cache locality than std::list but faster insert and erase than std::vector. https://t.co/WSoZdCg64F" / X</a></li>

</ul>
</details>

**标签**: `#C++`, `#performance`, `#standard library`, `#container`

---

<a id="item-15"></a>
## [NetBSD 11.0 重大版本正式发布](https://blog.netbsd.org/tnf/entry/netbsd_11_0_released) ⭐️ 7.0/10

NetBSD 项目正式发布了 NetBSD 11.0，这是这款可移植的类 Unix 操作系统的新主版本。发布公告详细介绍了新特性以及各支持架构的安装选项。 NetBSD 以高度可移植性著称，广泛用于嵌入式系统并作为其他操作系统的底层基础。新的主版本带来了更新的硬件支持、安全修复和最新的第三方组件，惠及 BSD 生态系统的开发者和用户。 该版本将 ISO 镜像拆分为小于 700MB 的 CD-ROM 镜像和完整大小的 DVD 镜像，使用闪存介质（如 USB 驱动器）的用户必须使用解压后的 .img 文件而非 .iso 镜像。项目有意披露了三个未解决的安全问题（hdaudio ioctl 访问检查、ipfilter 空指针解引用、pf 释放后使用），它们将在即将推出的 11.1 版本中修复，目前预计在两个月内发布。

rss · Lobsters · Aug 1, 17:57

**背景**: NetBSD 是一款免费、开源的类 Unix 操作系统，源自伯克利软件套件（BSD），是继 386BSD 之后首个正式发布的开源 BSD 衍生系统。它以出色的可移植性和设计质量著称，可运行于从大型服务器到手持设备、嵌入式设备等多种平台。在基于 ARM 的设备上，NetBSD 11.0 镜像预配置了 U-Boot 引导加载程序。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NetBSD">NetBSD - Wikipedia</a></li>
<li><a href="https://www.netbsd.org/">The NetBSD Project</a></li>
<li><a href="https://en.wikipedia.org/wiki/Das_U-Boot">Das U-Boot - Wikipedia</a></li>

</ul>
</details>

**标签**: `#NetBSD`, `#Operating System`, `#Release`, `#BSD`

---

<a id="item-16"></a>
## [对 TP-Link TL-841N 进行 root 并发现硬编码的重置持久化凭据](https://blog.juni-mp4.com/posts/42/rooting-the-tplink-tl841n-pt1/) ⭐️ 7.0/10

这篇博文描述了如何对 TP-Link TL-841N 路由器进行 root、分析其固件，并发现即使恢复出厂设置后仍然存在的硬编码凭据。文章提供了提取和检查固件映像的逐步技术细节。 消费级路由器通常带有未记录的硬编码凭据，这些凭据构成严重的安全风险，因为它们可能被用于远程访问并在重置后依然有效。这项研究凸显了固件审计对物联网设备安全的重要性。 分析过程据称使用了常见的固件逆向工程技术，如提取文件系统和搜索硬编码字符串。这些凭据具有重置持久性，意味着即使恢复出厂设置后它们仍然存在，这是一个值得关注的安全问题。

rss · Lobsters · Aug 2, 18:32

**背景**: 路由器固件是控制路由器硬件和配置的底层软件。对路由器进行 root 意味着获得完全的管理控制权，通常通过提取固件映像、修改文件系统内容或利用漏洞来实现。硬编码凭据是制造商在固件中嵌入的账户和密码，通常用于调试或维护，发现它们可能揭示隐藏的后门。在诸如此类的逆向工程工作中，通常使用 binwalk 等工具来提取和分析固件映像。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sergioprado.blog/reverse-engineering-router-firmware-with-binwalk/">Reverse engineering my router's firmware with binwalk</a></li>
<li><a href="https://arzedlab.github.io/posts/firmware-reverse-engineering-and-analysis-of-route-2b63648c0bf48023a3fec748d42f3844/">Firmware reverse engineering and analysis of router devices</a></li>
<li><a href="https://www.firmwarescan.com/">FirmwareScan — AI-Powered Firmware Security Analysis</a></li>

</ul>
</details>

**标签**: `#security`, `#firmware`, `#IoT`, `#reverse engineering`, `#router`

---