---
layout: default
title: "Horizon 每日速递：2026-08-03"
date: 2026-08-03
lang: zh
---

> 📅 2026-08-03 · 从 57 条资讯中精选出 14 条重要内容

---

1. [OpenAI 用 Astra 破解十年未解数学难题](#item-1) ⭐️ 8.0/10
2. [NetBSD 11.0 发布，公开已知安全问题](#item-2) ⭐️ 8.0/10
3. [没有数学家的数学](#item-3) ⭐️ 8.0/10
4. [Lean 内核健全性漏洞 #14576 事后分析：AI 发现的 Collatz 证明伪造 False](#item-4) ⭐️ 8.0/10
5. [Karpathy 的 Pelican 推文引发 AI 物理世界基准测试热议](#item-5) ⭐️ 7.0/10
6. [Kakehashi：在 Linux ARM 上运行 macOS 二进制的实验性用户态项目](#item-6) ⭐️ 7.0/10
7. [eBay 骚扰事件致 5600 万美元赔偿](#item-7) ⭐️ 7.0/10
8. [AI 公开信：开放权重与蒸馏引发辩论](#item-8) ⭐️ 7.0/10
9. [开源模型盘点#23：Laguna S2.1、Inkling、Kimi K3 推进帕累托前沿](#item-9) ⭐️ 7.0/10
10. [C 语言 sizeof 的解析歧义：解析为何出奇困难](#item-10) ⭐️ 7.0/10
11. [Rust 1.98 新增代数浮点运算符，加速数值计算](#item-11) ⭐️ 7.0/10
12. [评测 C++26 新增的 std::hive 容器性能](#item-12) ⭐️ 7.0/10
13. [写操作遇到 EPIPE 通常意味着设计缺陷](#item-13) ⭐️ 7.0/10
14. [破解 TP-Link TL-841N 固件发现硬编码重置持久凭据](#item-14) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenAI 用 Astra 破解十年未解数学难题](https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/#atom-everything) ⭐️ 8.0/10

OpenAI 使用其下一代主要模型的内部版本 Astra，为十道至少十年未取得进展的数学问题找到了解决方案，每个问题花费不到 2,000 美元。相关成果已通过 Lean 4 形式化证明、论文和一份由 LLM 生成的 PDF（重建证明过程）发布。 这标志着大型语言模型在原创数学研究中的应用迈出了重要一步，可能加速那些多年停滞不前的领域取得进展。结合 Anthropic 的 Mythos Preview 发现密码学弱点的事件，这预示着 AI 工具助力基础科学突破的新时代。 OpenAI 声称按 GPT-5.6 Sol 的 token 价格计算，每个问题花费不到 2,000 美元，但未透露有多少问题尝试后未获成功。openai/ten-proofs 代码库包含 Lean 4 形式化证明，该项目还产出了一篇论文和一份基于未公开推理轨迹、由 LLM 生成的 PDF；博主表示希望能看到所使用的提示词。

rss · Simon Willison · Aug 1, 20:34

**背景**: AI 辅助数学是一个快速发展的领域，像 Lean 4 这样的交互式定理证明器被用于正式验证证明。此前，Anthropic 的 Claude Mythos Preview 于 2026 年 4 月 7 日发布，但因网络安全风险未公开提供，据报道它花费了 10 万美元的 token 发现了密码学弱点。数学家陶哲轩曾描述“大数学”（big mathematics）的未来——人类与机器之间大规模、去中心化的协作，由 AI 承担大部分技术性繁琐工作，而人类负责创造性部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nxcode.io/resources/news/claude-mythos-preview-anthropic-most-powerful-model-2026">Claude Mythos Preview : Anthropic 's Most Powerful AI... | NxCode</a></li>
<li><a href="https://red.anthropic.com/2026/mythos-preview/">Claude Mythos Preview \ red. anthropic .com</a></li>
<li><a href="https://www.emergentmind.com/topics/reasoning-traces">Reasoning Traces : Analysis & Applications</a></li>

</ul>
</details>

**标签**: `#mathematics`, `#theoretical computer science`, `#artificial intelligence`, `#LLM research`, `#Anthropic`

---

<a id="item-2"></a>
## [NetBSD 11.0 发布，公开已知安全问题](https://blog.netbsd.org/tnf/entry/netbsd_11_0_released) ⭐️ 8.0/10

NetBSD 项目于 2026 年 8 月 1 日宣布发布 NetBSD 11.0，这是一个包含新安装镜像和简化发布流程的重大版本更新。该版本特意推迟以等待第三方组件稳定，尽管仍存在未修复的安全问题，项目选择公开发布，并计划在 11.1 中修复。 作为一款历史悠久的开源操作系统的重要版本，NetBSD 11.0 将影响其在众多硬件平台上的用户和开发者社区。该项目决定公开未解决的安全问题，也反映出 AI 辅助漏洞发现正在改变整个开源生态的发布实践。 安装镜像现拆分为小于 700MB 的 CD-ROM 镜像和完整 DVD 镜像，使用 USB 等闪存介质时必须使用 .img 文件。目前已知未修复的安全问题涉及 hdaudio(4) 的 ioctl 权限检查、ipfilter 的空指针解引用以及 pf 分片重组中的 use-after-free；项目计划在两个月内发布 11.1。

rss · Lobsters · Aug 1, 17:57

**背景**: NetBSD 是一个免费开源、类 Unix 的操作系统，以可移植性强和支持广泛的硬件架构著称。主要版本通过发布候选版本和签名校验和来准备，项目使用 U-Boot（一种开源引导加载程序）在基于 ARM 的设备上引导 NetBSD，例如从 SD 卡或 NAND flash 启动的设备。公告中提到的“pullup requests”是指被挑选合并到稳定维护分支、用于未来补丁版本的改动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Das_U-Boot">Das U-Boot - Wikipedia</a></li>

</ul>
</details>

**标签**: `#NetBSD`, `#operating system`, `#release`, `#open source`

---

<a id="item-3"></a>
## [没有数学家的数学](https://borretti.me/article/mathematics-without-mathematicians) ⭐️ 8.0/10

OpenAI 宣布，一个尚未发布的模型解决了数学中的十个开放问题，其中包括编码理论中的一个。本文作者对这一公告进行反思，并认为关于人类数学家仍将保持相关性的常见“应对”说法很可能被现实推翻。 如果这一消息得到证实，则表明 AI 很快将在发现层面超越人类数学家，从而改变数学以及依赖数学的科学领域。作者认为，数学是“科学的伟大动力机”，因此超越人类的数学家具有实质性的实用价值——这与超越人类的国际象棋引擎不同。 作者承认自己只能判断编码理论的结果很重要，其他结果则信赖数学家的评价。文章列举并反驳了几种“应对”心态，例如“我们将引导 AI”“我们将传授 AI 发现的数学”和“我们将决定如何收录这些成果”，并指出 AI 的证明可能以 Lean 的形式呈现。

rss · Lobsters · Aug 2, 09:30

**背景**: 开放问题（open problems）是指研究人员尚未证明的未解数学问题。形式化数学使用可被计算机验证的语言（如 Lean）来表达定义和证明，从而实现自动化检查以及 AI 辅助证明。编码理论（coding theory）是文章提到的领域之一，研究用于错误检测、纠错和高效数据传输的编码设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Coding_theory">Coding theory</a></li>
<li><a href="https://formal-mathematics.github.io/intro.html">A course on the formalization of mathematics , using Lean4.</a></li>

</ul>
</details>

**标签**: `#AI`, `#mathematics`, `#OpenAI`, `#research`, `#proofs`

---

<a id="item-4"></a>
## [Lean 内核健全性漏洞 #14576 事后分析：AI 发现的 Collatz 证明伪造 False](https://leodemoura.github.io/blog/2026-8-1-postmortem-for-kernel-soundness-bug-14576/) ⭐️ 8.0/10

7 月 28 日，Kiran Gopinathan 将 Ramana Kumar 借助 AI 生成的 Collatz 反证简化为一个 False 的证明，并提交了 issue #14576；Lean 团队在一小时内合并了修复（#14577）。Daniel Selsam 借助 AI 进行的安全审查还发现并修复了内核中的其他错误。 内核健全性是 Lean 等证明助手可信度的基石；一个接受 False 证明的漏洞足以使该内核校验过的所有定理失效。此次事件表明，即使是成熟的证明助手也需要独立检查器和经过验证的内核，而 AI 可以帮助发现此类漏洞。 该漏洞的触发条件是：内核在消除某个归纳类型下的嵌套出现时，如果参数是幻影参数（未出现在构造子字段中），这些参数会被丢弃，从而使类型错误的参数逃过类型检查；该漏洞只能通过元编程触达。独立检查器 nanoda 最初未发现该证明，是因为它在早一周才修复了另一个独立缺陷；lean4lean 对归纳类型的处理是参考实现的移植，因此也受影响。

rss · Lobsters · Aug 1, 21:51

**背景**: Lean 是一个交互式定理证明器，其内核是一个小型的、可信的程序，负责校验每一个证明。形式化验证依赖这样的内核来确保证明确实证明了它声称的内容，因此即使是实现层面的漏洞也会带来严重风险。像 nanoda 这样的独立复查器，以及 lean4lean 这样一个形式化证明内核正确性的项目，都是抵御此类漏洞的手段。这篇事后分析还描述了如何利用 AI 辅助工具来寻找更多内核缺陷。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/leanprover/lean4/issues/14576">Kernel accepts wrong-structure projections, allowing ... - GitHub</a></li>
<li><a href="https://www.openwall.com/lists/oss-security/2026/08/02/1">oss-security - Lean 4 kernel soundness bug: forging proofs ...</a></li>
<li><a href="https://freenode.net/article/lean-4-kernel-bug-lets-metaprograms-forge-proofs-of-false">Lean 4 kernel bug lets metaprograms forge proofs of False</a></li>

</ul>
</details>

**标签**: `#Lean`, `#soundness bug`, `#kernel`, `#formal verification`, `#postmortem`

---

<a id="item-5"></a>
## [Karpathy 的 Pelican 推文引发 AI 物理世界基准测试热议](https://twitter.com/karpathy/status/2083749667410727319) ⭐️ 7.0/10

Andrej Karpathy 的一条关于 AI 生成鹈鹕（pelican）图像的推文成为 Hacker News 上热门帖子的主题，引发了关于能否将此类 AI 生成图像用作衡量模型对物理世界理解能力的基准的讨论。 这之所以重要，是因为 PHYRE、PAI-Bench 和 PhyBench 等基准已经旨在测试物理推理能力，而 Karpathy 这种非正式的“鹈鹕”测试凸显了简单、定性的提示如何暴露出当前模型的短板。这表明评价重点正在转向模型对世界的具身理解，而不仅仅是文本或图像生成质量。 该 HN 帖子链接的是 Karpathy 推文的 xcancel 镜像而非原始推文，因此确切提示和鹈鹕输出结果并不明确。评论者将鹈鹕测试与早期案例（例如微软 GPT-4 评估中要求用 TikZ 绘制独角兽）进行对比，并指出这类视觉基准本质上仍是定性和主观的。

hackernews · delichon · Aug 2, 04:05

**背景**: 物理世界理解基准用于评估 AI 模型是否能对直觉物理、物体交互和空间关系进行推理。近期的相关工作包括 Meta 的 PHYRE 物理推理谜题基准、用于统一评估物理 AI 的 PAI-Bench，以及用于测试文生图模型物理常识的 PhyBench。HN 讨论中提到的“Simon 的鹈鹕”是一个非正式提示，要求 AI 用矢量图形语言绘制一只鹈鹕，作为检验这种理解的简单定性测试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai.meta.com/research/publications/phyre-a-new-benchmark-for-physical-reasoning/">PHYRE: A New Benchmark for Physical Reasoning | Facebook AI Research</a></li>
<li><a href="https://www.emergentmind.com/topics/phybench">PHYBench: AI Physical Reasoning Benchmarks</a></li>
<li><a href="https://www.emergentmind.com/topics/physical-ai-bench-pai-bench">PAI-Bench: Unified Physical AI Evaluation</a></li>

</ul>
</details>

**社区讨论**: 一位评论者指出，糟糕的最终产品“正是重点”，因为视觉基准可以揭示模型对物理世界的理解程度。其他人将其与微软早期 GPT-4 评估中要求用 TikZ 绘制独角兽相提并论，还有评论者认为这一测试的可复现性不如“Simon 的鹈鹕”，因为 Karpathy 没有公布提示词。

**标签**: `#AI`, `#benchmarks`, `#machine learning`, `#Karpathy`

---

<a id="item-6"></a>
## [Kakehashi：在 Linux ARM 上运行 macOS 二进制的实验性用户态项目](https://github.com/wie-project/kakehashi) ⭐️ 7.0/10

Kakehashi 是一个实验性用户态项目，旨在 Linux ARM 上原生运行 macOS 命令行二进制文件。作者称已实现 7-Zip、curl 和 git 工具的可运行原型，其中 7-Zip 通过了多线程压缩测试，curl 通过了 200 多个命令行测试。 如果成功，Kakehashi 可以将 macOS 命令行软件带到 Linux ARM 设备（如单板计算机和基于 Arm 的服务器）上。它也顺应了跨操作系统兼容层日益增长的趋势，效仿了面向 Windows 应用的 WINE/Proton 先例。 Kakehashi 仍是一个专注于 CLI 二进制的早期实验性原型。作者称 7-Zip 目前比原生 Linux 执行慢约 5.2 倍，但已有明确的优化计划来缩小差距，而且该项目的目标是在 Linux ARM 上原生执行，而非模拟。

hackernews · vlad_kalinkin · Aug 2, 16:26

**背景**: Kakehashi（梯）在日语中意为“吊桥”，恰如其分地描述了这座连接 macOS 软件与 Linux 的桥梁。在 Linux 上运行 macOS 二进制文件不仅仅需要翻译 CPU 指令：这些二进制文件采用 Mach-O 可执行格式，并依赖 Apple 的系统库与内核接口。用户态兼容层（而非完整虚拟机）将这些 macOS API 转换为 Linux 等价物。在用户态，二进制兼容通常取决于库在版本演进中保持稳定的接口与版本控制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kakehashi">Kakehashi</a></li>
<li><a href="https://blogs.oracle.com/linux/binary-compatibility">Binary Compatibility and OpenELA’s ELValidated Project</a></li>

</ul>
</details>

**社区讨论**: 讨论总体积极但谨慎。有用户将该项目的长远潜力比作面向 Windows 应用的 WINE/Proton，并询问作者是否可以与已有 ARM64 PR 的 Darling 项目合作。另一位用户表示自己一直在寻找这类项目，但认为方案仍处于早期阶段，还有一位用户则开玩笑地吐槽了项目名称。

**标签**: `#macOS`, `#Linux`, `#ARM`, `#binary compatibility`, `#userspace`

---

<a id="item-7"></a>
## [eBay 骚扰事件致 5600 万美元赔偿](https://www.ft.com/content/06ec1b03-d4af-40cf-b12a-4ba5a410f6d2) ⭐️ 7.0/10

七名前 eBay 安全团队成员因针对一对批评该公司的夫妇策划骚扰活动而被判刑，eBay 同意支付 5600 万美元。刑期包括前安全与安保高级总监 Jim Baugh 的 57 个月监禁，以及 Brian Gilbert 的已服刑时间加 2 万美元罚款。 此案凸显了企业安全团队滥用权力报复批评者的风险。刑事判决与巨额赔偿相结合，向企业发出了明确警告：此类不当行为将带来法律和经济后果。 根据社区报道的细节，Jim Baugh 被判 57 个月监禁，Brian Gilbert 被判已服刑时间、一年监督释放（不得接触受害者）及 2 万美元罚款。其他成员，包括前全球韧性总监 David Harville，也受到判决，但具体细节未被完整记录。

hackernews · JumpCrisscross · Aug 2, 19:19

**背景**: 此案涉及 eBay 全球安全团队针对 Ina 和 David Steiner 夫妇的行动，二人运营一份批评 eBay 的电子通讯。检察官称，包括前警察队长在内的七名团队成员联手通过威胁信息、监视和其他方式骚扰和恐吓 Steiner 夫妇。5600 万美元是和解协议的一部分，刑事诉讼导致数名成员被判监禁。

**社区讨论**: 评论者对骚扰事件仅止于 Steiner 夫妇表示怀疑，呼吁调查 eBay 是否还针对其他批评者，并调查涉案前警察队长的职业生涯。一位评论者引用了一个更广泛的现象：当人们缺乏监督时可能会出现不当行为，并提到其他企业事件。另一位评论者转而批评 eBay 高昂的卖家费用。

**标签**: `#security`, `#corporate misconduct`, `#legal`, `#ethics`, `#eBay`

---

<a id="item-8"></a>
## [AI 公开信：开放权重与蒸馏引发辩论](https://simonwillison.net/2026/Aug/2/open-letters/#atom-everything) ⭐️ 7.0/10

西蒙·威利森总结了近期两封关于 AI 政策的公开信：微软支持、235 家公司签署的《开放权重与美国 AI 领导力》为开放权重模型和蒸馏技术辩护；而《为前沿设定节奏》由 1324 名前沿 AI 员工签署，呼吁国际治理来有意识地控制自动化 AI 发展的速度。 这些公开信反映了 AI 社区在开放权重模型与 AI 安全问题上的公开分歧，可能影响美国的政策制定。这场辩论关系到模型访问权限和蒸馏等技术手段的监管。 第一封信（7 月 24 日）由 235 家 AI 相关公司签署，包括 NVIDIA、亚马逊、Y Combinator，以及后来加入的 OpenAI；Anthropic 拒绝签署，并在三天后发布了自己的回应，批评工业规模的蒸馏操作。第二封信（7 月 28 日）由 OpenAI、Anthropic 等前沿实验室的员工签署，包括 Ilya Sutskever 和 Dario Amodei。

rss · Simon Willison · Aug 2, 04:16

**背景**: 开放权重模型是指将训练好的神经网络参数公开供人下载和使用的模型，相比封闭模型，它们允许更广泛的研究和审查。蒸馏技术是将大模型（教师）的知识转移给小模型（学生），使小模型在保持性能的同时更高效地部署。Claude Code 是一个在终端中运行的 AI 助手，可以分析代码库、调试和修复问题，这展示了 AI 在软件开发中的自动化应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://allthings.how/what-is-an-open-weight-ai-model-and-how-to-use-one/">What is an Open Weight AI Model and How to Use One</a></li>
<li><a href="https://www.loomery.com/insights/what-is-claude-code-actually-good-for-an-actual-road-test">What is Claude Code actually good for: A road test | Loomery</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#open weights`, `#distillation`, `#AI development`

---

<a id="item-9"></a>
## [开源模型盘点#23：Laguna S2.1、Inkling、Kimi K3 推进帕累托前沿](https://www.interconnects.ai/p/latest-open-artifacts-23-laguna-s21) ⭐️ 7.0/10

这篇盘点涵盖了最新的开源权重模型发布，包括 Poolside 的 Laguna S2.1、腾讯的 Hy3、Thinking Machines 的模型以及 LongCat-2.0。文章强调这些模型如何落在帕累托前沿上，例如 Hy3 证明了一个 50 年前的数学问题，LongCat-2.0 则是首个完全在中国 Ascend 910 芯片上训练的非华为模型。 该报道反驳了行业整合的预测，显示越来越多的公司正在训练强大模型并公开释出。这扩大了开源模型生态系统，为 AI/ML 从业者提供了更多能力强、成本效益高的选择，并加剧了中美实验室之间的竞争。 值得注意的细节包括：Thinking Machines 的开源模型微调服务据称每年创造数亿美元收入，腾讯将 Hy3 转为 Apache 2.0 许可证。Poolside 的 Laguna S2.1（118B-A8B MoE）可运行在 DGX Spark 上，并采用 OpenMDW 许可证，而 LongCat-2.0 是一个 1.6T 参数的 MoE，完全在 Ascend 910 上训练。

rss · Interconnects (Nathan Lambert) · Aug 2, 13:01

**背景**: 机器学习中的帕累托前沿指的是一组在相互竞争的目标（如能力与计算成本）之间提供最佳权衡的模型。许多最新的开源模型采用混合专家（MoE）架构，每个 token 只激活一部分参数，从而在不按比例增加推理成本的情况下提升模型容量。开源权重发布允许开发者自行微调和部署模型，减少对专有 API 的依赖。这篇文章的背景是训练成本不断上升，以及关于是否只有少数实验室能主导模型开发的争论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pareto_front">Pareto front - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>

</ul>
</details>

**标签**: `#open models`, `#AI`, `#machine learning`, `#model releases`, `#Pareto frontier`

---

<a id="item-10"></a>
## [C 语言 sizeof 的解析歧义：解析为何出奇困难](https://sebsite.pw/w/20260802-sizeof.html) ⭐️ 7.0/10

一篇技术文章解释了为何解析 C 的 sizeof 运算符出乎意料地困难：其操作数既可以是未加括号的一元表达式，也可以是加括号的类型名，而复合字面量（compound literals）及后缀运算符会破坏朴素的解析策略。同样的难题也适用于 C2y 新引入的 _Countof 运算符。 这对编译器与解析器开发者很重要，因为这种歧义迫使人们仔细设计文法，而不能简单地依赖前瞻一个 token 或回溯。随着 C2y 标准化 _Countof，理解这一陷阱也很重要，因为 _Countof 继承了同样的解析难题。 朴素的策略——先看是否有左括号，尝试解析类型名，失败则回退解析表达式——在 sizeof(int){0} 这类把复合字面量当作表达式的情况，以及 sizeof(T){}.x[0]() 这类后缀运算符跟在后面的情况下都会失效。一种正确做法是编写一个既尝试一元表达式又尝试括号类型名的解析函数以避免回溯，同时注意不要贸然把强制转换表达式（cast expression）的解析合并到同一代码路径，因为 sizeof(int)+1 是加法表达式，而不是某个强制转换表达式的大小。

rss · Lobsters · Aug 2, 06:01

**背景**: 在 C 语言中，sizeof 的操作数可以是一元表达式，也可以是加括号的类型名；只有类型名必须加括号。C99 引入的复合字面量（如 (int){0}）是表达式，外观却像强制转换后跟一个花括号初始化列表，由此产生了上述歧义。下一个 C 标准 C2y 新增了用于获取数组长度的 _Countof 运算符，它也面临同样的解析难题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.cppreference.com/c/language/compound_literal">Compound literals (since C99) - cppreference.com</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sizeof">sizeof - Wikipedia</a></li>
<li><a href="https://sourceforge.net/p/sdcc/feature-requests/978/">C2y: The _Lengthof Operator (now _Countof/countof) - SourceForge</a></li>

</ul>
</details>

**标签**: `#C`, `#parsing`, `#compilers`, `#sizeof`, `#programming languages`

---

<a id="item-11"></a>
## [Rust 1.98 新增代数浮点运算符，加速数值计算](https://pythonspeed.com/articles/faster-float-math-rust/) ⭐️ 7.0/10

Rust 1.98 为 f32 和 f64 新增了一组代数算术运算符，它们明确允许编译器利用实数代数性质进行优化，包括重排运算顺序。文章中的成对求和与 SSD 示例在使用这些运算符后，运行速度约为原来的两倍。 这为 Rust 开发者提供了一种稳定、按操作级别的方式来放宽严格的浮点语义，而不必使用影响整个程序的全局 fast-math 标志。对于所有使用 Rust 进行数值计算的领域——科学模拟、机器学习、游戏或数据处理——都有重要意义，因为微小的精度取舍可以换来显著的加速。 新的代数运算符与原有的严格运算符互补，可在同一算法中混用：对精度敏感的部分使用严格加法，对性能敏感的部分使用代数加法。在文章基于 Rust 1.98 beta 和 x86-64-v3 目标 CPU 的基准测试中，SSD 示例的耗时从 628.7 微秒降至 371.1 微秒，每个值的 CPU 指令数从 4.5 降至 1.0。

rss · Lobsters · Aug 2, 20:27

**背景**: 浮点运算不满足结合律：(a+b)+c 可能因舍入而与 a+(b+c) 不同，NaN、Inf 和 -0.0 等特殊值也会破坏对实数成立的代数恒等式。因此，编译器默认会避免对浮点表达式进行重排或重新结合，这会阻碍自动向量化、公共子表达式消除等优化。C/C++ 等语言提供了全局的 'fast-math' 标志来放宽这些规则，但 Rust 此前没有稳定且细粒度的等效方案。新的代数运算符正是让开发者可以标记特定运算为可优化，从而解决这个问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pythonspeed.com/articles/faster-float-math-rust/">Faster floating point math with Rust’s new API</a></li>
<li><a href="https://doc.rust-lang.org/std/primitive.f32.html">f32 - Rust</a></li>
<li><a href="https://en.wikipedia.org/wiki/Floating-point_arithmetic">Floating-point arithmetic - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Rust`, `#floating-point`, `#performance`, `#compiler optimization`, `#numeric computing`

---

<a id="item-12"></a>
## [评测 C++26 新增的 std::hive 容器性能](https://lemire.me/blog/2026/08/02/how-fast-is-c26s-stdhive/) ⭐️ 7.0/10

Daniel Lemire 对 C++26 新增的 std::hive 容器进行了性能基准测试，并将其与 std::vector、std::list 等其他标准容器进行对比。他的测量结果展示了 hive 的连续块存储在实际使用中的表现。 std::hive 是 C++ 标准库中的全新容器，开发者需要可靠的性能数据来决定何时使用它。Lemire 是备受尊敬的性能研究者，因此他的基准测试对 C++26 项目中容器的选择具有重要参考价值。 这篇博文链接到了 Lobsters 上的讨论，但提供的 feed 中不包含社区评论。std::hive 容器由提案 P0447R28（“将 std::hive 引入标准库”）引入，其设计目标是将元素存储在连续的内存块中。

rss · Lobsters · Aug 2, 18:28

**背景**: C++26 在标准库中新增了 std::hive，旨在填补 std::vector 与 std::list 之间的空白。与 vector 类似，它将元素保存在连续的内存块中，因此遍历时无需为每个元素追踪指针。与 list 不同，hive 支持高效地插入和删除元素，同时不会使指向其他元素的指针或引用失效，因此适用于某些实时系统和游戏开发场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lemire.me/blog/2026/08/02/how-fast-is-c26s-stdhive/">How fast is C+ + 26 ’s std :: hive ? – Daniel Lemire's blog</a></li>
<li><a href="https://cpprefjp.github.io/reference/hive/hive.html">std :: hive - cpprefjp C++日本語リファレンス</a></li>

</ul>
</details>

**标签**: `#C++`, `#C++26`, `#std::hive`, `#performance`, `#benchmarking`

---

<a id="item-13"></a>
## [写操作遇到 EPIPE 通常意味着设计缺陷](https://rachelbythebay.com/w/2026/07/09/pipe/) ⭐️ 7.0/10

rachelbythebay.com 上的一篇新文章认为，当程序在 write 时收到 EPIPE，通常是程序管理管道或套接字的方式存在设计缺陷的症状，而不是需要通过防御性代码处理的暂时性错误。 对系统程序员而言，正确处理断开的管道是一个反复出现的痛点，而对 EPIPE 的误判会导致代码脆弱或数据静默丢失。这篇文章将这一错误重新定义为设计问题，可能影响开发者组织 I/O 和进程生命周期的方式。 这篇文章区分了 SIGPIPE——进程在向已关闭的管道写入时默认收到的信号——和 EPIPE——当 SIGPIPE 被忽略或阻塞时 write 返回的 errno 值。它指出，在正常操作中遇到 EPIPE 通常意味着程序一开始就不应该向那个描述符写入。

rss · Lobsters · Aug 2, 08:35

**背景**: 在类 Unix 系统中，当进程向读取端已关闭的管道或套接字写入时，内核会发送 SIGPIPE，其默认动作是终止进程。如果进程忽略或阻塞了 SIGPIPE，write 会返回 -1 并将 errno 设为 EPIPE（'broken pipe'，管道断裂）。许多程序遇到 EPIPE，仅仅是因为它们忽略了 SIGPIPE 后又继续写入，这往往说明程序缺少对端状态或 write 返回值的检查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.unix.com/programming/171395-sigpipe-epipe.html">SIGPIPE and EPIPE - Programming - Unix Linux Community</a></li>
<li><a href="https://stackoverflow.com/questions/108183/how-to-prevent-sigpipes-or-handle-them-properly">How to prevent SIGPIPEs (or handle them properly) Usage example</a></li>
<li><a href="https://www.man7.org/linux/man-pages/man7/signal.7.html">signal (7) — Linux manual page</a></li>

</ul>
</details>

**标签**: `#EPIPE`, `#Unix`, `#pipes`, `#error handling`, `#systems programming`

---

<a id="item-14"></a>
## [破解 TP-Link TL-841N 固件发现硬编码重置持久凭据](https://blog.juni-mp4.com/posts/42/rooting-the-tplink-tl841n-pt1/) ⭐️ 7.0/10

一篇详细的博文描述了如何对 TP-Link TL-841N 路由器进行 root、分析其固件，并发现硬编码且重置后仍存在的凭据。 在恢复出厂设置后仍然存在的硬编码凭据对物联网设备构成严重安全风险，可能导致持久未授权访问。这一发现凸显了对消费级路由器进行固件审计和负责任披露的重要性。 分析过程包括对设备进行 root 以获得固件的特权访问权限，并从中提取硬编码凭据。“重置持久”一词表明，即使在恢复出厂设置后，这些凭据依然有效，这对用户和厂商而言都是一个关键警告。

rss · Lobsters · Aug 2, 18:32

**背景**: 对路由器进行 root 通常意味着获得对固件的特权访问权限，固件中包含操作系统和配置文件。硬编码凭据是嵌入在固件或源代码中的明文用户名或密码，通常由制造商用于维护或诊断。当此类凭据重置后仍然存在时，它们能躲过恢复出厂设置，意味着用户无法仅通过重置设备来消除后门。这使得它们成为消费级网络设备中特别危险的安全漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.forescout.com/blog/new-tp-link-router-vulnerabilities-a-primer-on-rooting-routers/">New TP-Link Router Vulnerabilities: A Primer on Rooting Routers</a></li>
<li><a href="https://www.beyondtrust.com/resources/glossary/hardcoded-embedded-passwords">What are Hardcoded Passwords/Embedded Credentials? | BeyondTrust</a></li>
<li><a href="https://www.beyondtrust.com/blog/entry/hardcoded-and-embedded-credentials-are-an-it-security-hazard-heres-what-you-need-to-know">Hardcoded and Embedded Credentials - What You Need to Know | BeyondTrust</a></li>

</ul>
</details>

**标签**: `#security`, `#firmware`, `#reverse-engineering`, `#IoT`, `#credentials`

---