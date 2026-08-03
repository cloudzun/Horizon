---
layout: default
title: "Horizon 每日速递：2026-08-03"
date: 2026-08-03
lang: zh
---

> 📅 2026-08-03 · 从 59 条资讯中精选出 18 条重要内容

---

1. [事后分析：AI 辅助考拉兹反证暴露并修复 Lean 内核健全性漏洞 \#14576](#item-1) ⭐️ 9.0/10
2. [Karpathy 引发讨论：以鹈鹕绘画作为 AI 新基准](#item-2) ⭐️ 8.0/10
3. [F\*：一种通用且面向证明的编程语言](#item-3) ⭐️ 8.0/10
4. [eBay 高管因骚扰他人被判刑，赔偿 5600 万美元](#item-4) ⭐️ 8.0/10
5. [OpenAI 的 Astra 模型解决十个十年未解数学难题](#item-5) ⭐️ 8.0/10
6. [Rust 1\.98 新增代数算子，加速浮点运算](#item-6) ⭐️ 8.0/10
7. [基准测试 C\+\+26 的 std::hive 容器](#item-7) ⭐️ 8.0/10
8. [NetBSD 11\.0 在简化流程后发布，并公开已知安全问题](#item-8) ⭐️ 8.0/10
9. [AI 解决十个开放数学问题；数学家或将过时](#item-9) ⭐️ 8.0/10
10. [Kakehashi：在 Linux ARM 上运行 macOS 二进制的用户态方案](#item-10) ⭐️ 7.0/10
11. [批评：SwiftUI 七年仍无起色](#item-11) ⭐️ 7.0/10
12. [个人 AI 基准测试：生成一张带 Habsburg 下颌的 SVG 青蛙](#item-12) ⭐️ 7.0/10
13. [AI 公开信争议：开放权重、蒸馏与节奏把控](#item-13) ⭐️ 7.0/10
14. [开源模型综述：Laguna S2\.1、Inkling、Kimi K3 领跑帕累托前沿](#item-14) ⭐️ 7.0/10
15. [解析 C 语言中的 sizeof 为何出人意料地困难](#item-15) ⭐️ 7.0/10
16. [你的 JSON 在骗你：JavaScript 如何悄然破坏大整数](#item-16) ⭐️ 7.0/10
17. [写入时 EPIPE 可能意味着你用错了管道](#item-17) ⭐️ 7.0/10
18. [TP\-Link TL\-841N 的 Root 与固件分析发现重置后仍存在的硬编码凭据](#item-18) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [事后分析：AI 辅助考拉兹反证暴露并修复 Lean 内核健全性漏洞 \#14576](https://leodemoura.github.io/blog/2026-8-1-postmortem-for-kernel-soundness-bug-14576/) ⭐️ 9.0/10

Lean 内核的一个健全性漏洞（\#14576）于 7 月 28 日由 Kiran Gopinathan 报告，此前 Ramana Kumar 发布了利用该漏洞的 AI 辅助“考拉兹猜想反证”。Leonardo de Moura 和 Lean 团队在一小时内推送了修复（\#14577），经 Joachim Breitner 审查，并发布了新的补丁版本。 Lean 内核的健全性漏洞至关重要，因为恶意元程序可能诱使内核接受 False 的证明，从而破坏 Lean 所检查的所有形式化证明的信任基础。该漏洞还影响了 lean4lean 等独立检查器，并凸显了 AI 辅助证明可能暴露隐蔽实现缺陷的问题。 该漏洞发生在内核消除带有幽灵参数 Ds 的归纳类型 T 下的嵌套出现时：这些参数从生成的辅助类型中消失，从而逃过了类型检查。该漏洞只能通过元编程触达，前端会捕获类型错误的项，且这是实现错误而非 Lean 元理论上的缺陷；后续 PR \#14582 会检查参数确实按参数行为起作用，OpenAI 网络安全 AI 发现的其它内核编程错误也已被修复并被 nanoda 捕获。

rss · Lobsters · Aug 1, 21:51

**背景**: Lean 是一个基于归纳构造演算（Calculus of Inductive Constructions）的证明助手和函数式编程语言；其内核是一个小型可信核心，负责对每个证明进行类型检查，因此这里出现健全性漏洞意味着检查器可能接受无效证明。考拉兹猜想是一个著名的开放问题，Ramana Kumar 的仓库声称给出了无公理反证，但该反证实际利用的是这一内核漏洞，而非真正的数学结果。nanoda 是 Lean 内核的独立 Rust 实现，lean4lean 则是 Lean 对自身类型理论的形式化，两者都用于交叉检查官方内核的行为，从而帮助发现信任问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://leodemoura.github.io/blog/2026-8-1-postmortem-for-kernel-soundness-bug-14576/">Postmortem for Kernel Soundness Bug #14576 — Leonardo de Moura</a></li>
<li><a href="https://github.com/leanprover/lean4/issues/14576">Kernel accepts wrong-structure projections, allowing an axiom-free ...</a></li>
<li><a href="https://github.com/digama0/lean4lean">GitHub - digama0/lean4lean: Lean 4 kernel / &#x27;external checker&#x27; written in Lean 4 · GitHub</a></li>

</ul>
</details>

**标签**: `#Lean`, `#theorem proving`, `#formal verification`, `#kernel soundness`, `#bug postmortem`

---

<a id="item-2"></a>
## [Karpathy 引发讨论：以鹈鹕绘画作为 AI 新基准](https://twitter.com/karpathy/status/2083749667410727319) ⭐️ 8.0/10

Andrej Karpathy 在推文中指出，AI 图像模型仍然无法正确画出鹈鹕，并引发了一场关于将评测重心从原始图像生成转向检验物理世界理解的基准的讨论。该推文引发了关于用定性、主观测量基准衡量未来进展的广泛讨论。 这一讨论之所以重要，是因为它重新定义了如何评判 AI 图像生成质量：模型可能不再以生成赏心悦目的图像为目标，而是看它们是否理解真实世界的结构和物理合理性。这可能推动开发者更关注空间推理和物理一致性，对机器人技术和具身 AI 具有重要意义。 评论者指出，Karpathy 的例子让人想起微软在 GPT\-4 预发布评估中用 TikZ 绘制独角兽的提示，这是此类基准的早期实例。另一个担忧是，如果不公开确切的提示词，这类演示就无法复现，从而限制了其作为基准的价值。

hackernews · delichon · Aug 2, 04:05

**背景**: 大型语言模型和图像生成模型虽然能生成赏心悦目的图像，但在需要精确空间推理或理解物理对象如何组装的任务上常常失败。为解决这一问题，研究人员提出了 PhysBench（ICLR 2025）和 PAI\-Bench（CVPR 2026）等基准，专门测试视觉语言模型和物理 AI 系统对物理世界的理解。Karpathy 关于鹈鹕的评论正是这种超越表层输出、深入评估模型能力的更广泛趋势的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ai.cc/blogs/world-models-2026-google-nvidia-physical-ai-breakthroughs/">World Models 2026: Google, NVIDIA &amp; LeCun Build AI That ...</a></li>
<li><a href="https://github.com/physical-superintelligence-lab/PhysBench">GitHub - physical-superintelligence-lab/PhysBench: [ICLR 2025 ...</a></li>
<li><a href="https://github.com/SHI-Labs/physical-ai-bench">GitHub - SHI-Labs/physical-ai-bench: [CVPR 2026 Oral] PAI ...</a></li>

</ul>
</details>

**社区讨论**: 讨论看法各异：有人指出自己见过的所有鹈鹕图都或多或少有错误，另一些人则认为这正是重点——模型已进入一个更能暴露物理世界理解的定性基准阶段。还有评论者提到微软在 GPT\-4 评估中使用‘用 TikZ 画独角兽’提示的历史先例，另有评论者则担心演示未公开提示词，导致无法复现。

**标签**: `#AI`, `#image-generation`, `#benchmarks`, `#LLM`, `#vector-graphics`

---

<a id="item-3"></a>
## [F\*：一种通用且面向证明的编程语言](https://fstar-lang.org/) ⭐️ 8.0/10

F\* 被定位为一种通用、面向证明的编程语言，允许编写程序的同时提供机器校验的属性证明。其官网重点介绍了近期工作，例如在 ICFP 2021 上发表的、基于并发分离逻辑的面向证明语言 Steel。 像 F\* 这样的面向证明语言之所以重要，是因为它们将形式化验证带入实际软件开发，并已有验证 TLS 等真实应用。这类语言使得构建具有数学上可保证正确性的软件成为可能，对安全关键型和安全攸关系统尤为有价值。 F\* 将数学证明技术直接融入开发过程，而非像传统语言那样依赖测试和调试。该语言支持依赖类型编程；相关语言 Steel 构建于 SteelCore 之上，后者是一种用于验证含并发命令式程序的并发分离逻辑。

hackernews · ducktective · Aug 2, 12:31

**背景**: 形式化验证是运用数学方法，依据形式化规范证明或证伪系统正确性的过程。F\* 是依赖类型语言，承袭了 Coq 等证明助手的传统，但被设计为通用编程语言。用 F\* 编写的程序可被编译成可执行代码，同时附带其行为的机器校验证明。F\* 项目源于包括微软在内的研究合作，并被积极应用于已验证的系统软件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fstar-lang.org/">F *: A Proof - Oriented Programming Language</a></li>
<li><a href="https://www.linuxlinks.com/f-general-purpose-proof-oriented-programming-language/">F * - general-purpose, proof - oriented programming language</a></li>
<li><a href="https://en.wikipedia.org/wiki/Formal_verification">Formal verification - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：一些用户批评 F\* 首页缺少直观的代码示例，另一些则称赞该语言支持对现有 C 代码库进行增量迁移。有用户询问 F\* 在工业界的应用情况及其适用软件类型，还有人拿响应式样式表中的副作用开玩笑。

**标签**: `#formal verification`, `#programming languages`, `#functional programming`, `#security`, `#proof assistants`

---

<a id="item-4"></a>
## [eBay 高管因骚扰他人被判刑，赔偿 5600 万美元](https://www.ft.com/content/06ec1b03-d4af-40cf-b12a-4ba5a410f6d2) ⭐️ 8.0/10

eBay 高管因策划针对一对夫妇的骚扰行动而被判刑，公司为此支付了 5600 万美元和解金。前高级总监 Jim Baugh 获刑 57 个月，前高级经理 Brian Gilbert 被判处已服刑期、一年监督释放及 2 万美元罚款。 此案表明，即使是大型科技公司的高级安全主管，也可能因报复批评者而面临刑事后果。这引发了关于问责制的更广泛质疑，以及这对夫妇之外是否还有其他骚扰目标。 包括前警察队长在内的七名 eBay 安全团队成员参与了此次骚扰行动。据报道，该公司支付了 5600 万美元和解金，各被告刑期不一，其中 Jim Baugh 的刑期最长。

hackernews · JumpCrisscross · Aug 2, 19:19

**背景**: 这对夫妇 David 和 Ina Steiner 经营着 EcommerceBytes，这是一份为小型在线卖家提供资讯的新闻通讯，经常批评 eBay。检方称，eBay 安全工作人员共同对 Steiner 夫妇进行骚扰和恐吓，包括发送威胁信息和实施监控。此案凸显出，当高管感到受到批评媒体威胁时，企业安全团队可能变成报复工具。

**社区讨论**: 评论者质疑骚扰行为是否仅限于这一对夫妇，暗示 eBay 其他批评者可能也曾成为目标，并认为前警察的参与值得深查。另一位评论者借此案指出企业不当行为的普遍模式，另一条讨论则抱怨 eBay 的销售佣金过高。

**标签**: `#eBay`, `#harassment`, `#corporate crime`, `#security`, `#legal accountability`

---

<a id="item-5"></a>
## [OpenAI 的 Astra 模型解决十个十年未解数学难题](https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/#atom-everything) ⭐️ 8.0/10

OpenAI 使用其下一代主要模型 Astra 的内部版本，解决了十个至少十年未见进展的数学问题。该公司以 GPT\-5\.6 Sol 代币价格在每个问题上花费不到 2,000 美元，并发布了 Lean 4 形式化证明、一篇论文以及一份由 LLM 生成的、重构证明过程的 PDF。 这标志着 AI 从辅助数学家向独立生成创新证明的重大转变。它也印证了陶哲轩所展望的'大数学'愿景，即大规模人机协作攻克多年来难倒专家的问题。 OpenAI 在 openai/ten\-proofs 仓库中发布了结果，包含 Lean 4 形式化证明、一篇论文，以及基于未公开推理轨迹由 LLM 生成的 PDF。Simon Willison 指出，目前尚不清楚在找到解决方案之前尝试了多少个问题，并呼吁对所使用的提示词提高透明度。

rss · Simon Willison · Aug 1, 20:34

**背景**: AI 系统最近在数学领域取得了显著进展；例如，Anthropic 的 Claude Mythos Preview 在每一个主流操作系统和浏览器中发现了高严重性漏洞，并为 Erdős 问题给出了一个'精巧而简单的证明'。像 Lean 4 这样的证明助手可以形式化验证数学论证，而 LLM 推理轨迹则记录了模型逐步决策的过程，可用于分析证明是如何构建的。这些进展在数学家中引发了兴奋与焦虑，因为 AI 开始承担以往需要人类创造力的角色。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://greekreporter.com/2026/04/11/anthropic-ai-model-mythos-greek-word/">Anthropic Names New AI Model ‘ Mythos ’ After... - GreekReporter.com</a></li>
<li><a href="https://logicity.in/en/blog/claude-mythos-solves-erd-s-problem-with-cute-simple-proof">Claude Mythos Solves Erdős Problem With &#x27;Cute, Simple Proof &#x27;</a></li>

</ul>
</details>

**标签**: `#mathematics`, `#theoretical computer science`, `#AI research`, `#proof assistants`, `#Anthropic`

---

<a id="item-6"></a>
## [Rust 1\.98 新增代数算子，加速浮点运算](https://pythonspeed.com/articles/faster-float-math-rust/) ⭐️ 8.0/10

Rust 1\.98 计划于 2026 年 8 月 20 日发布，新增了一组用于浮点数的“代数”算术运算符，允许编译器应用实数代数优化（例如重新排序运算）。文章使用 beta 频道测试了该功能，并在 SSD（平方差总和）基准测试中报告了约 2 倍的加速。 这为 Rust 数值编程者提供了一种稳定的、可选择的方式，让编译器优化浮点代码，同时保留对精度敏感部分的控制。它使 Rust 在灵活性上更接近 C/C\+\+ 编译器的 fast\-math 选项，同时仍以严格的 IEEE\-754 行为作为默认。 新的代数运算符只会在显式使用的位置放宽运算顺序和舍入限制，因此像 pairwise summation 这样的算法可以结合严格运算符来保证精度、代数运算符来提升速度。在文章中的 SSD 基准测试中，代数运算将每个值的 CPU 指令数从 4\.5 降至 1\.0，耗时从 628\.7µs 降至 371\.1µs（基于 x86\-64\-v3 硬件）。

rss · Lobsters · Aug 2, 20:27

**背景**: 在 IEEE\-754 中，浮点加法和乘法不具有结合律，因为每次运算都会发生舍入，因此将 \(a\+b\)\+c 重排为 a\+\(b\+c\) 可能改变结果。因此编译器通常保持浮点运算的精确顺序，以保证结果可复现且符合规范，这限制了优化空间。新的 Rust API 允许开发者在不需要逐位精确结果的场景中，有选择地授权编译器使用代数性质。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pythonspeed.com/articles/faster-float-math-rust/">Faster floating point math with Rust’s new API</a></li>
<li><a href="https://learn.microsoft.com/en-us/cpp/build/reference/fp-specify-floating-point-behavior?view=msvc-170">/fp (Specify floating-point behavior) | Microsoft Learn Floating Point Optimization - Texas Instruments Floating-Point Optimizations Optimize Options (Using the GNU Compiler Collection (GCC)) Towards Verified Compilation of Floating-point Optimization ... c - clang 14.0.0 floating point optimizations - Stack Overflow</a></li>

</ul>
</details>

**标签**: `#Rust`, `#floating-point`, `#performance`, `#compiler optimization`, `#numeric computing`

---

<a id="item-7"></a>
## [基准测试 C\+\+26 的 std::hive 容器](https://lemire.me/blog/2026/08/02/how-fast-is-c26s-stdhive/) ⭐️ 8.0/10

Daniel Lemire 发布了一篇博客文章，对 C\+\+26 新标准化的 std::hive 容器的性能进行了基准测试，衡量其在实际工作负载中的速度。 作为一个新的标准容器，std::hive 的性能特征将影响 C\+\+开发者是否会采用它用于缓存友好、内存稳定的场景。Lemire 的分析为 C\+\+社区提供了早期的独立数据。 std::hive 基于 plf::hive 库，而 plf::hive 是与 C\+\+标准提案对齐的 plf::colony 的一个分支。它在保持指针稳定和迭代活动元素的同时，提供 O\(1\)的插入和删除操作。

rss · Lobsters · Aug 2, 18:28

**背景**: C\+\+26 预计将引入 std::hive，这是一种旨在解决'活动集合'问题的容器，即对象被频繁插入和删除但仍需保持内存稳定的场景。与 std::vector 或 std::list 不同，hive 将元素存储在带有跳过字段机制的块中，允许快速遍历存活元素并实现 O\(1\)删除。该容器源自流行的 plf::colony 库，并已讨论多年。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.cppreference.com/cpp/container/hive/hive">std::hive::hive - cppreference.com</a></li>
<li><a href="https://towardsdev.com/cpp26-std-hive-deep-dive-tutorial-5bdaa44f4d94">A Deep Dive into C++26 std::hive: The Ultimate Container for ...</a></li>
<li><a href="https://github.com/mattreecebentley/plf_hive">GitHub - mattreecebentley/plf_hive: plf::hive is a fork of plf::colony to match the current C++ standards proposal. · GitHub</a></li>

</ul>
</details>

**标签**: `#C++`, `#C++26`, `#performance`, `#std::hive`, `#containers`

---

<a id="item-8"></a>
## [NetBSD 11\.0 在简化流程后发布，并公开已知安全问题](https://blog.netbsd.org/tnf/entry/netbsd_11_0_released) ⭐️ 8.0/10

NetBSD 项目宣布发布 NetBSD 11\.0，这是一个因等待第三方组件而延迟的重大版本更新。该版本提供了拆分为 CD 和 DVD 的 ISO 镜像、为 ARM 设备预配置的 U\-Boot 镜像，以及自动化的发布流程。 NetBSD 11\.0 对一个历史悠久的开源操作系统来说是一个重要里程碑，为其用户和开发者社区提供了更新的组件。它对已知安全问题的透明处理反映了来自 AI 辅助漏洞发现的日益增长的压力，并为更快的 11\.1 版本设定了预期。 值得注意的细节包括将 ISO 镜像拆分为小于 700MB 的 CD 镜像和完整大小的 DVD 镜像，闪存介质需使用 \.img 文件。该版本还列出了三个未修复的安全问题（hdaudio、ipfilter、pf），将在计划于两个月内发布的 11\.1 版本中修复。

rss · Lobsters · Aug 1, 17:57

**背景**: NetBSD 是一个免费的开源类 Unix 操作系统，以其在多种硬件平台上的可移植性而闻名。U\-Boot（Universal Boot Loader）是一种开源引导加载程序，常用于嵌入式设备中初始化硬件并加载操作系统内核。NetBSD 的发布流程需要为每个平台构建和生成校验和，并涉及安全官员签名等人工干预，整体时间受限于网络传输速度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Das_U-Boot">Das U-Boot - Wikipedia</a></li>
<li><a href="https://linuxvox.com/blog/u-boot-linux/">A Comprehensive Guide to U-Boot and Linux - linuxvox.com</a></li>

</ul>
</details>

**标签**: `#NetBSD`, `#Operating System`, `#Release`, `#Open Source`, `#BSD`

---

<a id="item-9"></a>
## [AI 解决十个开放数学问题；数学家或将过时](https://borretti.me/article/mathematics-without-mathematicians) ⭐️ 8.0/10

这篇文章对 OpenAI 的公告做出反应，称一个尚未发布的模型解决了十个开放数学问题。作者提到，他虽然只能亲自评估其中一个（编码理论）问题，但他信任的数学家确认了这些成果的重要性。 这一公告可能标志着 AI 在开展原创数学研究方面能力的里程碑，可能改变该领域以及人类数学家的角色。作者认为，这样的 AI 最终将在直觉和品味上超越人类，使人类数学家变得过时，或者至多像宠物一样，处于远更强大实体的照料之下。 作者列举了几种“应对方式”——即人们可能用来否认 AI 影响的合理化理由——例如“我们将引导 AI”或“我们将教授 AI 发现的数学”，并逐一给出了反驳。他特别指出，他能评估的一个可解问题属于编码理论，并提到 AI 在形式化数学和编码等可验证领域取得了巨大进展，但向不可形式化领域的泛化仍是一个未解问题。

rss · Lobsters · Aug 2, 09:30

**背景**: OpenAI 是一家 AI 研究机构，近期宣布一个尚未发布的模型能够解决开放数学问题。编码理论（作者可评估的问题所属领域）研究用于数据压缩、纠错、密码学和可靠传输的编码。形式化数学使用 Lean 和 Mizar 等证明助手来机械地验证证明，使其成为非常适合 AI 的领域。文章认为，由于数学是“科学的强大动力源”，超人类的数学 AI 将远比超人类的国际象棋引擎更具影响力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Coding_theory">Coding theory</a></li>
<li><a href="https://en.wikipedia.org/wiki/Formalized_mathematics">Formalized mathematics</a></li>

</ul>
</details>

**标签**: `#AI`, `#mathematics`, `#OpenAI`, `#research`, `#machine learning`

---

<a id="item-10"></a>
## [Kakehashi：在 Linux ARM 上运行 macOS 二进制的用户态方案](https://github.com/wie-project/kakehashi) ⭐️ 7.0/10

Kakehashi 是一个实验性的用户态翻译层，可在 Linux aarch64 上原生运行 macOS ARM64 二进制文件。目前已有 7\-Zip、curl 和 Git 的可工作原型，且无需内核模块或 JIT。 如果成功，该项目可能为 Linux ARM 机器带来 macOS 命令行应用的兼容性，类似于 Wine/Proton 对 Windows 应用所做的贡献。它也可能推动 ARM 生态系统中跨平台二进制兼容性的关注。 该项目在 Linux 上加载 Darwin Mach\-O 文件，映射一个独立的 libSystem，并翻译 BSD 系统调用。性能仍处于早期阶段：7\-Zip 比原生 Linux 执行慢约 5\.2 倍，但超过 200 个 curl 命令通过了自动化 Docker 测试脚本。

hackernews · vlad\_kalinkin · Aug 2, 16:26

**背景**: Mach\-O 是 macOS 和 iOS 使用的原生可执行文件格式，它依赖 dyld 动态链接器在运行时加载库并解析符号。Kakehashi 采用类似 Wine 的方式，完全在用户态实现这些机制，避免在内核层模拟 Mach 内核。这与 Darling 等项目在概念上相似，但 Kakehashi 专注于 ARM64 和命令行优先的工作负载。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/wie-project/kakehashi">wie-project/ kakehashi : Userspace macOS translation layer for Linux ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mach-O">Mach-O - Wikipedia</a></li>
<li><a href="https://www.mikeash.com/pyblog/friday-qa-2012-11-09-dyld-dynamic-linking-on-os-x.html">mikeash.com: Friday Q&amp;A 2012-11-09: dyld: Dynamic Linking On OS X</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了兴趣并指出项目仍处于早期阶段，有人询问是否可与 Darling 项目合作，后者有一个开放的 ARM64 PR。另一位评论者批评“Kakehashi”这个名字不好，还有人提出了关于虚拟化框架和可再分发性的更深层次技术问题。

**标签**: `#macOS`, `#Linux`, `#ARM`, `#compatibility`, `#reverse engineering`

---

<a id="item-11"></a>
## [批评：SwiftUI 七年仍无起色](https://ykvm.com/2026/07/swiftui-a-story-of-mediocrity/) ⭐️ 7.0/10

一篇新发布的回顾性博客文章《SwiftUI After 7 Years》认为，自 2019 年首次亮相以来，Apple 的声明式 UI 框架并未取得显著进步，并称其表现平庸。这篇文章引发了开发者之间关于声明式 UI 范式优点以及 Apple 框架演进方向的激烈讨论。 这篇批评文章助燃了行业内一场旷日持久的讨论：SwiftUI 这类声明式 UI 框架是否真的优于 UIKit 和 AppKit 等传统命令式框架。这场讨论的结果将影响开发者为 Apple 平台构建应用的方式，以及 Apple 未来的框架战略规划。 据报道，该文章指出了 SwiftUI 在数据流和更新追踪方面存在的问题，而一些评论者反驳称，使用性能分析工具和积累经验可以缓解这些问题。讨论还提到，Google 的 Jetpack Compose 具有许多相同的缺陷，并且有 UIKit 背景的开发者往往难以适应 SwiftUI 以状态驱动的思维模式。

hackernews · mpweiher · Aug 2, 18:59

**背景**: SwiftUI 是 Apple 于 2019 年推出的声明式 UI 框架，用于在 iOS、macOS 等 Apple 平台上构建界面。在声明式编程中，开发者描述 UI 的理想最终状态，由框架负责管理更新，这与需要逐步管理视图的命令式框架形成对比。类似的声明式框架，如 Android 平台的 Jetpack Compose，也因复杂性和性能权衡而受到批评。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SwiftUI">SwiftUI - Wikipedia</a></li>
<li><a href="https://developer.apple.com/documentation/swiftui">SwiftUI | Apple Developer Documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Declarative_programming">Declarative programming</a></li>

</ul>
</details>

**社区讨论**: 评论者意见分歧严重。Rayiner 警告称，Apple 未能推出更好的 UI 框架意味着存在危险的惯性；而 sandoze 则根据实际生产经验和可用的性能分析工具为 SwiftUI 辩护。Cosmic\_cheese 怀疑纯粹的声明式响应式设计是否适合通用的原生 UI，emehex 观察到此前的 UIKit 开发者难以适应这种范式转变，spacedcowboy 也批评 Swift 过于复杂，呼应了这一观点。

**标签**: `#SwiftUI`, `#Apple`, `#UI frameworks`, `#declarative programming`, `#developer experience`

---

<a id="item-12"></a>
## [个人 AI 基准测试：生成一张带 Habsburg 下颌的 SVG 青蛙](https://frogs.vaguespac.es/) ⭐️ 7.0/10

作者 thebigship 创建了一个个人 AI 基准测试，要求图像生成模型“生成一张带 Habsburg 下颌的 SVG 青蛙”，并将结果发布在 frogs\.vaguespac\.es 上。该基准测试迅速走红，社区反响热烈，作者表示网站被“挤爆”了。 这个基准测试以创意且实际的方式评估了当前图像生成模型，揭示了它们处理复杂、非常规视觉指令的能力。它引发了关于模型能力、失败模式和渲染策略的深入讨论，对开发者和用户都很有价值。 该提示要求生成一只可辨认的青蛙，同时呈现突出的 Habsburg 下颌，这是一个具有挑战性的组合。社区观察者指出，大多数模型从正面而非侧面绘制青蛙，且多个尝试生成了与青蛙面部脱节的“肿块”作为下颌。

hackernews · thebigship · Aug 2, 19:42

**背景**: Habsburg 下颌，即下颌前突（mandibular prognathism），是指下颌骨突出于上颌骨的一种状况，在历史上与哈布斯堡家族密切相关。SVG（可缩放矢量图形）是一种基于 XML 的开放 Web 标准，用于描述可任意缩放且保持清晰的二维矢量图形。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Habsburg_jaw">Habsburg jaw</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/SVG">SVG: Scalable Vector Graphics - MDN Web Docs</a></li>
<li><a href="https://www.w3.org/Graphics/SVG/About">Scalable Vector Graphics (SVG) - World Wide Web Consortium (W3C)</a></li>

</ul>
</details>

**社区讨论**: 社区成员分享了不同结果：jnwatson 称赞 Fable 5 的“创意添加”，hn\_throwaway\_99 则认为 Opus 5 最接近成功，并指出许多失败作品“青蛙面部画得还行”但下颌处理不当。krisoft 观察到没有模型尝试从侧面绘制青蛙，而这本应更利于表现下颌形状。另一位用户 abound 提到了自己关于爆米花物理 3D 模型的个人基准测试，作者 thebigship 感谢大家的热情回应，并表示网站因流量过大而濒临崩溃。

**标签**: `#AI`, `#image-generation`, `#benchmark`, `#SVG`, `#machine-learning`

---

<a id="item-13"></a>
## [AI 公开信争议：开放权重、蒸馏与节奏把控](https://simonwillison.net/2026/Aug/2/open-letters/#atom-everything) ⭐️ 7.0/10

Simon Willison 总结了最近三封公开信：由微软牵头的《开放权重与美国 AI 领导力》（7 月 24 日，235 家签署方，包括 NVIDIA 和 OpenAI）、Anthropic 的反驳回应《我们对开放权重模型的立场》（7 月 27 日），以及《为前沿技术设定节奏》（7 月 28 日，1324 名前沿 AI 公司员工签署）。这些信件争论开放权重模型与封闭模型哪个更安全，以及是否应限制蒸馏技术。 这场交锋凸显了 AI 行业在治理与安全问题上的深刻分歧：一边是微软和开放权重倡导者，另一边是 Anthropic。后续的政策选择可能影响美国 AI 监管、模型开放性的未来，以及前沿实验室的竞争格局。 《开放权重》信函认为封闭模型会造成单点故障，并支持将蒸馏视为一项合法且历史悠久的技巧。Anthropic 虽未主张全面禁令，但呼吁打击“工业规模的蒸馏作业”，并警告威权国家带来的风险。《为前沿技术设定节奏》引用了一些具体例子：Anthropic 用 Claude Code 编写 80%的代码，OpenAI 的 Sol 将服务成本降低了 20%，Kimi K3 设计了一款用于纳米模型的芯片。

rss · Simon Willison · Aug 2, 04:16

**背景**: 开放权重 AI 模型公开了模型的训练参数（“权重”），相比封闭的“黑盒”模型，用户拥有更多控制和可见性，但它并非完全开源，因为训练数据和代码可能仍为专有。知识蒸馏是一种让较小模型通过较大模型的输出进行训练的技术，常用于将能力压缩到更便宜、更快的模型中。这些信件还涉及 AI 服务成本优化，例如通过批处理、缓存和模型效率（如 OpenAI 的 Sol）来降低推理成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/open-weight-ai-what-we-finally-opened-bonnet-nicolas-pistorio-n3ulf">Open - weight AI : what if we finally opened the bonnet ?</a></li>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://www.mirantis.com/blog/inference-costs/">Optimizing Inference Costs: The Complete Guide | Mirantis</a></li>

</ul>
</details>

**标签**: `#AI`, `#Open Weights`, `#AI Policy`, `#Model Training`, `#Industry`

---

<a id="item-14"></a>
## [开源模型综述：Laguna S2\.1、Inkling、Kimi K3 领跑帕累托前沿](https://www.interconnects.ai/p/latest-open-artifacts-23-laguna-s21) ⭐️ 7.0/10

这篇综述文章介绍了近期一系列开源权重模型的发布，包括 Poolside 的 Laguna S2\.1、Thinking Machines 的 Inkling、Moonshot AI 的 Kimi K3，以及腾讯的 Hy3 和 AMD 的 Instella\-MoE。文章认为，开源模型在帕累托前沿上的实用性正日益接近前沿水平。 这凸显了一个转变：更多实验室正在训练并公开发布强大的模型，与早先关于行业整合的预测相悖。这为从业者提供了更多具竞争力的开源选择，并在成本与能力上对闭源模型供应商构成压力。 Laguna S2\.1 是一个 118B\-A8B 的 MoE 模型，小到可以运行在 DGX Spark 上，并以 OpenMDW 许可证发布。Inkling 是 Thinking Machines 的首个开源权重模型，约 1T 参数，支持 1M 上下文窗口，原生支持文本、图像和音频输入；Kimi K3 则是 2\.8T 参数的开源权重旗舰模型，上下文达 1M token。

rss · Interconnects \(Nathan Lambert\) · Aug 2, 13:01

**背景**: 帕累托前沿指的是在能力与成本或效率之间达到最佳平衡的模型集合；位于该前沿的开源模型既具竞争力又能实际部署。文章观察到，尽管训练成本不断上升，行业整合并未如预期发生——反而有更多公司投资于“token 机器”并公开发布模型。文章还提到中国实验室的持续发布节奏，以及 Thinking Machines 等美国新入局者的崛起。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/poolside/Laguna-S-2.1">poolside/Laguna-S-2.1 · Hugging Face</a></li>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our Open-Weights Model - Thinking Machines Lab</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K3 Tech Blog: Open Frontier Intelligence</a></li>

</ul>
</details>

**标签**: `#open-source AI`, `#large language models`, `#model releases`, `#Pareto frontier`, `#AI/ML`

---

<a id="item-15"></a>
## [解析 C 语言中的 sizeof 为何出人意料地困难](https://sebsite.pw/w/20260802-sizeof.html) ⭐️ 7.0/10

这篇文章深入探讨了在 C 语言中解析 sizeof 的困难，因为该操作符的操作数既可以是一元表达式，也可以是带括号的类型名，再加上复合字面量等因素，导致语法存在歧义。文中还指出，C2Y 新引入的 \_Countof 操作符也面临同样的问题。 对于编译器和解析器开发者而言，这揭示了 C 语言中一个微妙的语法歧义，在区分表达式和类型名时必须小心处理。随着 C2Y 引入 \_Countof，这种歧义的实际影响范围将进一步扩大。 朴素的解析思路是先检查开括号再尝试解析类型名，但 sizeof\(int\)\{0\} 这样的复合字面量会让该思路失效；复合字面量后还可能跟任意多个后缀运算符，例如 sizeof\(T\)\{\}\.x\[0\]\(\)。另外，sizeof\(int\)\+1 应理解为加法表达式，而不是对强制类型转换表达式求大小。

rss · Lobsters · Aug 2, 06:01

**背景**: 在 C 语言中，sizeof 的操作数要么是一个一元表达式，要么是一个用括号括起来的类型名，只有类型才需要加括号。复合字面量是 C99 引入的特性，允许在作用域内创建未命名对象，例如 \(int\)\{0\} 就是一个表达式，这造成了解析 sizeof 时的歧义。C2Y（即 C29）是 C 语言在 C23 之后的下一个修订版，预计于 2029 年底发布，其中新引入了 \_Countof 操作符，它也面临同样的解析问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.cppreference.com/c/language/compound_literal">Compound literals (since C 99) - cppreference.com</a></li>
<li><a href="https://thephd.dev/c2y-hitting-the-ground-running">C2y: Hitting the Ground Running | The Pasture - thephd.dev</a></li>

</ul>
</details>

**标签**: `#C`, `#parsing`, `#compilers`, `#sizeof`, `#grammar`

---

<a id="item-16"></a>
## [你的 JSON 在骗你：JavaScript 如何悄然破坏大整数](https://blog.gaborkoos.com/posts/2026-08-03-Your-JSON-Is-Lying-to-You/) ⭐️ 7.0/10

这篇博客文章演示了 JSON\.stringify 会静默地把 9007199254740993 这样的大整数改为 9007199254740992，因为 JavaScript Number 是 IEEE 754 双精度浮点数，精度有限。文章还探讨了其他序列化意外，例如 undefined 属性消失、Date 对象变成字符串、NaN 变成 null。 这篇文章指出了任何使用 JSON\.parse\(JSON\.stringify\(value\)\) 进行克隆、或通过 API 传递大 ID 的开发者都会遇到的数据完整性隐患。理解这些陷阱有助于在分布式系统、数据库以及前后端通信中避免难以察觉的 bug。 这种静默损坏之所以发生，是因为数字值在发生舍入之后，JSON\.stringify 已经无法检测到精度丢失。文章还介绍了通过返回 undefined 来删除属性的 replacer 函数、以数组作为属性白名单的形式，以及 toJSON\(\) 在序列化前改变值的机制。

rss · Lobsters · Aug 3, 01:40

**背景**: JavaScript 依据 IEEE 754 以 64 位浮点数表示所有数字，因此能够精确表示的最大整数是 Number\.MAX\_SAFE\_INTEGER，即 2^53 \- 1（9007199254740991）。JSON 本身没有规定数字精度的上限，所以不同的解析器和引擎对大整数的处理可能不一致。JSON 在 2000 年代初作为 XML 的轻量级替代方案被推广，后来在 RFC 4627 中正式定义，并在 RFC 8259 中更新。常见的 JSON 往返转换实际上是一种转换过程，只能保留 JSON 语法能够表示的数据类型和数值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.hackerone.com/blog/safely-handling-large-integers-json-best-practices-and-pitfalls">Safely Handling Large Integers in JSON : Best Practices... | HackerOne</a></li>
<li><a href="https://stackoverflow.com/questions/307179/what-is-javascripts-highest-integer-value-that-a-number-can-go-to-without-losin">math - What is JavaScript &#x27;s highest integer value that a number can...</a></li>
<li><a href="https://www.programiz.com/javascript/library/number/max_safe_integer">JavaScript Number . MAX _ SAFE _ INTEGER</a></li>

</ul>
</details>

**标签**: `#JSON`, `#JavaScript`, `#serialization`, `#data integrity`, `#floating-point`

---

<a id="item-17"></a>
## [写入时 EPIPE 可能意味着你用错了管道](https://rachelbythebay.com/w/2026/07/09/pipe/) ⭐️ 7.0/10

Rachel by the Bay 的这篇博文提出，write 调用返回 EPIPE 不仅仅是需要处理的错误，而是 Unix 管道设计或使用方式存在缺陷的征兆。文章认为正确做法是设计让写入端在读端关闭前就停止的管道，而不是依赖 EPIPE 处理之类的变通手段。 这很重要，因为大量 Unix 程序和脚本通过忽略 SIGPIPE、捕获 EPIPE 来应对管道破裂，导致令人困惑的错误和非标准行为。这篇文章挑战了一种常见做法，可能影响开发者编写命令行工具和设计对管道友好的程序的方式。 当管道的读端已关闭时，write\(\) 会返回 EPIPE，内核通常还会向写入进程发送 SIGPIPE，其默认行为是终止进程。作者认为，正确构建的管道根本不应该触发 EPIPE，应通过设计层面的修复而非信号处理补丁来解决。

rss · Lobsters · Aug 2, 08:35

**背景**: 在 Unix 中，管道通过内核管理的缓冲区把写入进程和读取进程连接起来。如果读取端提前退出（例如 \`yes \| head\`），写入端的 write\(\) 会返回 EPIPE，同时内核会发送 SIGPIPE 信号，默认终止进程。许多程序会安装 SIGPIPE 处理器或忽略该信号，以便通过 EPIPE 检测管道已关闭，但这篇博文认为 EPIPE 频繁出现恰恰说明管道本身被误用或设计不当。理解 SIGPIPE 等信号及其默认行为，是编写健壮的 Unix 命令行工具的基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/python/broken-pipe-error-in-python/">Broken Pipe Error in Python - GeeksforGeeks</a></li>
<li><a href="https://unix.stackexchange.com/questions/280723/fixing-signal-13-sigpipe-error-for-find-and-grep-pipeline">Fixing Signal 13 (SIGPIPE) error for find and grep pipeline</a></li>
<li><a href="https://stackoverflow.com/questions/108183/how-to-prevent-sigpipes-or-handle-them-properly">How to prevent SIGPIPEs (or handle them properly) Usage example</a></li>

</ul>
</details>

**标签**: `#unix`, `#pipes`, `#error-handling`, `#programming`

---

<a id="item-18"></a>
## [TP\-Link TL\-841N 的 Root 与固件分析发现重置后仍存在的硬编码凭据](https://blog.juni-mp4.com/posts/42/rooting-the-tplink-tl841n-pt1/) ⭐️ 7.0/10

这篇博文是对 TP\-Link TL\-841N 路由器进行 root 并分析其固件的技术过程。作者发现了硬编码且重置后仍有效的凭据（即使恢复出厂设置仍然有效），并将此文作为系列文章的第一部分发布。 硬编码且重置后仍有效的凭据，可能让知道这些凭据的人长期保有对受影响路由器的特权访问。这一发现凸显了低价消费级网络设备中的常见安全问题——未记录的凭据可能长期隐藏在固件中。 这篇文章标记为系列的第一部分，后续将继续分析。由于这些凭据在恢复出厂设置后仍然存在，单纯将路由器重置为出厂状态并不能清除它们，因此该问题更为严重。

rss · Lobsters · Aug 2, 18:32

**背景**: 路由器是在计算机网络之间转发数据的网络设备；消费级路由器运行控制其功能和安全的嵌入式固件。对路由器进行 root 是指获得该嵌入式系统的完全管理控制权，通常通过利用固件漏洞实现。固件分析是检查设备内部软件以发现弱点和漏洞的过程。硬编码凭据是直接嵌入在代码中而非安全存储的密码或密钥；重置后仍有效的凭据即使在恢复出厂设置后依然可用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aptive.co.uk/blog/what-are-hardcoded-credentials/">What are Hardcoded Credentials ? - Aptive</a></li>
<li><a href="https://learn.microsoft.com/en-us/azure/firmware-analysis/overview-firmware-analysis">Firmware analysis overview | Microsoft Learn</a></li>
<li><a href="https://networklessons.com/ip-routing/introduction-to-routers-and-routing">Introduction to Routers and Routing - NetworkLessons.com</a></li>

</ul>
</details>

**标签**: `#firmware analysis`, `#security`, `#embedded systems`, `#reverse engineering`, `#TP-Link`

---