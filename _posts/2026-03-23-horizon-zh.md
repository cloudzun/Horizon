---
layout: default
title: "Horizon 每日速递：2026-03-23"
date: 2026-03-23
lang: zh
---

> 📅 2026-03-23 · 从 82 条资讯中精选出 16 条重要内容

---

1. [Bram Cohen 提出基于 CRDT 的版本控制未来愿景](#item-1) ⭐️ 8.0/10
2. [Sebastian Raschka 发布现代 LLM 注意力机制变体的可视化指南](#item-2) ⭐️ 8.0/10
3. [iPhone 17 Pro 演示本地运行 400B 参数 LLM](#item-3) ⭐️ 7.0/10
4. [Trivy 漏洞扫描工具遭遇第二次 GitHub Actions 供应链攻击](#item-4) ⭐️ 7.0/10
5. [从美国服务迁移个人及企业技术基础设施至欧盟的实用指南](#item-5) ⭐️ 7.0/10
6. [深入剖析《过山车大亨》的汇编级优化技巧](#item-6) ⭐️ 7.0/10
7. [GitHub appears to be struggling with measly three nines availability](#item-7) ⭐️ 7.0/10
8. [Reports of code's death are greatly exaggerated](#item-8) ⭐️ 7.0/10
9. [Simon Willison 为 Bram Cohen 基于 CRDT 的版本控制系统构建交互式可视化工具](#item-9) ⭐️ 7.0/10
10. [Musk 宣布在德克萨斯州奥斯汀建设 Terafab 芯片制造工厂](#item-10) ⭐️ 7.0/10
11. [Lossy self-improvement](#item-11) ⭐️ 7.0/10
12. [Nelson Elhage 探讨错误处理与 Structured Concurrency 之间的关联](#item-12) ⭐️ 7.0/10
13. [Whistler 将实时 eBPF 编程引入 Common Lisp REPL](#item-13) ⭐️ 7.0/10
14. [Nolan Lawson 反思软件编程艺术的衰退](#item-14) ⭐️ 7.0/10
15. [Domenic Denicola 批评 Windows 原生应用开发的碎片化现状](#item-15) ⭐️ 7.0/10
16. [Qt 6.11 发布，带来重大图形、异步 C++ 及性能改进](#item-16) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Bram Cohen 提出基于 CRDT 的版本控制未来愿景](https://bramcohen.com/p/manyana) ⭐️ 8.0/10

BitTorrent 创始人 Bram Cohen 发表了名为「Manyana」的文章及约 470 行 Python 演示代码，提出了一种以 CRDT（无冲突复制数据类型）和改进合并冲突处理为核心的版本控制新方案。该文章引发了社区热烈讨论，获得超过 640 个赞和 360 条评论。 版本控制是所有软件开发的基础设施，合并冲突处理的任何实质性改进都可能影响数百万开发者的日常工作。这位备受尊敬的系统设计者提出的方案重新引发了关于无冲突合并是否真正可取的根本性辩论——它是否会掩盖开发者需要手动解决的重要语义冲突。 Manyana 明确定位为演示而非完整的版本控制系统，由约 470 行 Python 代码实现，针对单个文件进行操作。该方案专注于使用 CRDT 实现无冲突合并，但批评者认为，当两位开发者做出根本不兼容的修改时，这种方法可能产生语法上合并成功但语义上有问题的代码。

hackernews · Lobsters · Mar 22, 15:16

**背景**: CRDT（无冲突复制数据类型）是一种为分布式系统设计的数据结构，允许多个副本独立、并发地更新，并通过数学保证所有副本最终收敛到相同的一致状态，无需协调。它们广泛应用于协同编辑工具和分布式数据库。当前的版本控制系统（如 Git）通过检测文本冲突并要求开发者手动解决来处理并发编辑，这虽然令人困扰，但也作为一种安全机制来捕获语义上不兼容的修改。Bram Cohen 最为人知的身份是 BitTorrent 协议的创建者，他在版本控制实践方面有长期的思考和写作历史。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type">Conflict-free replicated data type - Wikipedia</a></li>
<li><a href="https://bramcohen.com/p/manyana">Manyana - by Bram Cohen - Bram’s Thoughts</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bram_Cohen">Bram Cohen - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区对核心前提持深度怀疑态度。多位资深开发者认为合并冲突是一个特性而非缺陷——它迫使开发者面对语义上的不兼容性，而 CRDT 会悄无声息地掩盖这些问题，可能产生可编译但逻辑错误的代码。一些评论者指出，更好的合并工具（如四窗格合并工具）已经解决了用户体验问题，无需更换底层版本控制系统；另一些人则倡导基于 rebase 的工作流来完全避免合并提交。还有人认为 AI 辅助合并是更有前景的未来方向。

**标签**: `#version-control`, `#CRDTs`, `#git`, `#developer-tools`, `#distributed-systems`

---

<a id="item-2"></a>
## [Sebastian Raschka 发布现代 LLM 注意力机制变体的可视化指南](https://magazine.sebastianraschka.com/p/visual-attention-variants) ⭐️ 8.0/10

Sebastian Raschka 发布了一份全面的可视化指南，涵盖现代大语言模型中使用的主要注意力机制变体，从 Multi-Head Attention (MHA)、Grouped Query Attention (GQA) 到 Multi-Head Latent Attention (MLA)、稀疏注意力以及混合架构。 随着 LLM 架构的快速演进，一份结构清晰的可视化参考资料对于理解内存效率、推理速度和模型质量之间权衡的从业者和研究人员来说极具价值。鉴于 DeepSeek-V3 等新模型正在采用日益复杂的注意力机制，这份指南是一份非常及时的教育资源。 该指南涵盖了从标准 Multi-Head Attention 到更高效变体的演进，包括 GQA（通过在多个查询头之间共享 key 和 value 头来减少 KV cache 内存）、MLA（使用低秩压缩处理 query、key 和 value 投影，首次在 DeepSeek-V2 中提出），以及通过仅计算部分 token 对交互来降低二次复杂度的稀疏注意力机制。指南还涉及了结合不同注意力策略的混合架构。

rss · Ahead of AI (Sebastian Raschka) · Mar 22, 11:55

**背景**: 注意力机制是 Transformer 模型的核心计算组件，而 Transformer 架构是几乎所有现代 LLM 的基础。标准的 Multi-Head Attention (MHA) 在 "Attention Is All You Need" 论文中提出，计算序列中所有 token 之间的成对相似度分数，其计算复杂度随序列长度呈二次增长。为解决这一计算瓶颈，研究人员开发了多种变体，例如 Grouped Query Attention (GQA) 通过在多组查询头之间共享 key-value 头来减少内存占用，而 DeepSeek 首创的 Multi-Head Latent Attention (MLA) 则将 key-value 表示压缩到低维潜在空间中。稀疏注意力机制采用不同的策略，仅选择性地计算特定 token 对之间的注意力，从而显著降低长序列的计算量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/deep-learning/grouped-query-attention-gqa/">Grouped Query Attention (GQA) - GeeksforGeeks</a></li>
<li><a href="https://medium.com/data-science/deepseek-v3-explained-1-multi-head-latent-attention-ed6bee2a67c4">DeepSeek-V3 Explained 1: Multi-head Latent Attention - Medium</a></li>
<li><a href="https://medium.com/@thekzgroupllc/sparse-attention-mechanisms-5d85991955e1">Sparse Attention Mechanisms . Scaling Generative AI... | Medium</a></li>

</ul>
</details>

**标签**: `#LLM`, `#attention-mechanisms`, `#deep-learning`, `#transformer-architecture`, `#educational`

---

<a id="item-3"></a>
## [iPhone 17 Pro 演示本地运行 400B 参数 LLM](https://twitter.com/anemll/status/2035901335984611412) ⭐️ 7.0/10

anemll 团队演示了 iPhone 17 Pro 本地运行一个 400B 参数的 Mixture of Experts (MoE) 大语言模型，通过 SSD 到 GPU 的流式传输技术处理庞大的模型权重，无需将所有参数同时加载到设备内存中。 这一演示展示了端侧 AI 推理的快速进展，表明即便是旗舰智能手机也可能很快能够在本地运行超大规模语言模型，从而实现无需依赖云服务器的隐私保护和离线 AI 助手功能。 该模型采用 MoE 架构，虽然总参数量为 400B，但在每次推理过程中实际激活的参数仅为很小一部分（可能低至数十亿级别），大幅降低了实际计算需求。SSD 到 GPU 的流式传输方案按需从设备闪存中加载模型权重，而非将所有权重常驻内存，这一技术与 Apple 2023 年发表的「LLM in a Flash」研究论文密切相关。

hackernews · anemll · Mar 23, 14:30

**背景**: Mixture of Experts (MoE) 是一种神经网络架构，模型中包含多个「专家」子网络，但路由机制在每次输入时仅激活其中一小部分，即使总参数量非常庞大，计算成本也能保持可控。这意味着一个 400B 的 MoE 模型在推理时的计算开销可能与一个小得多的稠密模型相当。Apple 2023 年发表的「LLM in a Flash」论文提出了在 DRAM 有限的设备上高效运行 LLM 的技术方案，通过从闪存（SSD）流式传输模型权重，并使用窗口化和行列捆绑策略来最小化数据传输量。这些方法对于内存稀缺但拥有高速 NVMe 存储的移动设备尤为重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@csburakkilic/understanding-moe-architectures-the-difference-between-total-and-active-parameters-ad1d161fccaa">Understanding MoE Architectures: The Difference Between Total ...</a></li>
<li><a href="https://apxml.com/courses/mixture-of-experts-advanced-implementation/chapter-4-efficient-moe-inference/moe-inference-challenges">MoE Inference Challenges: Memory & Latency - apxml.com</a></li>
<li><a href="https://arxiv.org/html/2410.14740v2">Harnessing Your DRAM and SSD for Sustainable and Accessible LLM Inference with Mixed-Precision and Multi-level Caching</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一——多位评论者指出「400B」的标题具有误导性，因为 MoE 模型在推理时仅激活一小部分参数（可能低至 2B），实际有效模型远小于总参数量所暗示的规模。也有人提出散热节流等实际问题，一位 iPad M2 用户反映设备「几秒内就变得极其烫手」。部分评论者将 SSD 流式传输方案与 Apple 2023 年的「LLM in a Flash」论文联系起来，还有人提到了 anemll 在 iPhone 上运行 OpenClaw 等更广泛的工作。

**标签**: `#on-device-AI`, `#LLM-inference`, `#iPhone`, `#edge-computing`, `#MoE`

---

<a id="item-4"></a>
## [Trivy 漏洞扫描工具遭遇第二次 GitHub Actions 供应链攻击](https://socket.dev/blog/trivy-under-attack-again-github-actions-compromise) ⭐️ 7.0/10

在 2026 年 3 月 19 日首次供应链攻击发生仅三天后，攻击者于 3 月 22 日再次攻击 Trivy，利用未完全轮换的凭据在 DockerHub 上发布了恶意镜像（v0.69.5 和 v0.69.6）。第二次攻击利用大范围的 GitHub Actions 标签篡改，在受影响的 CI/CD 流水线中转储运行器进程内存、窃取 SSH 密钥并外泄机密信息。 Trivy 是容器和云原生生态系统中使用最广泛的开源漏洞扫描工具之一，其被攻陷具有连锁影响——依赖 Trivy 进行安全扫描的组织可能已经泄露了自身 CI/CD 机密信息。此事件凸显了 GitHub Actions 安全模型中的系统性缺陷，可变标签使攻击者能够大规模篡改受信任的 Actions。 恶意载荷专门在 GitHub Actions 运行器中执行，目标包括进程内存转储、SSH 密钥和环境机密信息。安全公司 Socket 和 Wiz 将根本原因追溯到首次攻击后不完整的凭据轮换——Trivy 维护者承认轮换过程「不是原子性的」，攻击者可能在此过程中捕获了刷新后的令牌。

hackernews · jicea · Mar 22, 09:45

**背景**: Trivy 是由 Aqua Security 开发的开源安全扫描工具，可检测容器、Kubernetes 集群、代码仓库和云环境中的漏洞、错误配置和机密信息。GitHub Actions 是一个 CI/CD 平台，允许开发者自动化工作流；Actions 通过标签（类似版本号）引用指向特定代码提交。「标签篡改」（tag poisoning）攻击指攻击者覆盖现有标签使其指向恶意代码，导致所有引用该标签的工作流在不知情的情况下执行攻击者的载荷。GitHub 官方安全指南建议将 Actions 固定到完整的 commit SHA 而非标签，因为 SHA 是不可变的，无法被重定向。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://socket.dev/blog/trivy-under-attack-again-github-actions-compromise">Trivy Under Attack Again: Widespread GitHub Actions Tag Comp...</a></li>
<li><a href="https://www.csoonline.com/article/4148317/trivy-vulnerability-scanner-backdoored-with-credential-stealer-in-supply-chain-attack.html">Trivy vulnerability scanner backdoored with credential stealer in supply chain attack | CSO Online</a></li>
<li><a href="https://www.upwind.io/feed/trivy-supply-chain-incident-github-actions-compromise-breakdown">Trivy Supply Chain Attack: GitHub Actions Compromise - Upwind</a></li>

</ul>
</details>

**社区讨论**: 社区成员质疑为什么 GitHub 不对 Actions 强制实施不可变版本控制，以从根本上杜绝此类攻击，认为已发布的 Actions 不应允许使用可变标签。关于不完整的凭据轮换存在大量技术讨论——评论者对 Trivy 所称的轮换过程「不是原子性的」感到困惑，质疑攻击者究竟如何截获了刷新后的令牌。社区也注意到漏洞扫描工具本身变成漏洞的讽刺意味，并有人指出攻击者似乎在至少两次独立的凭据轮换尝试中维持了持久访问。

**标签**: `#supply-chain-security`, `#github-actions`, `#trivy`, `#devops-security`, `#vulnerability`

---

<a id="item-5"></a>
## [从美国服务迁移个人及企业技术基础设施至欧盟的实用指南](https://rz01.org/eu-migration/) ⭐️ 7.0/10

一份关于将数字基础设施从美国服务迁移至欧盟替代方案的综合指南在技术社区引发广泛关注，在 Hacker News 上获得了 764 分和 605 条评论，包含大量实用建议和真实迁移经验。 这反映了个人和企业因数据主权、地缘政治风险和隐私问题而减少对美国技术基础设施依赖的重要趋势，这一趋势可能重塑全球云计算和 SaaS 提供商的竞争格局。 社区频繁推荐的欧盟替代方案包括：Hetzner 用于服务器托管，Bunny.net 替代 Cloudflare 和 S3，mailbox.org 提供支持自定义域名的邮件服务，Fernand 作为 CRM 工具，以及 AISLER 用于 PCB 制造。部分公司反馈其迁移进度已达约 90%，仅剩少量对美国服务的依赖尚未解决。

hackernews · exitnode · Mar 23, 10:17

**背景**: 欧盟数据主权是指在欧盟境内产生的数据应在欧盟法律（特别是 GDPR）框架下进行存储、处理和管理的原则。根据 GDPR，任何向第三国传输个人数据的行为都不得削弱欧盟内部保障的保护水平。日益加剧的地缘政治紧张局势以及对美国政府通过 CLOUD Act 等法律获取美国公司所持数据的担忧，加速了将数字基础设施完全保留在欧盟管辖范围内的需求。这一趋势并不仅限于欧洲用户——讨论显示，加拿大及其他非美国用户也在寻求替代方案，以减少对美国科技公司的依赖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kingston.com/en/blog/data-security/understanding-eu-data-sovereignty">Understanding EU Data Sovereignty ... - Kingston Technology</a></li>
<li><a href="https://piwik.pro/blog/eu-hosting-vs-data-sovereignty/">EU Hosting vs. EU Sovereignty | Piwik PRO blog</a></li>

</ul>
</details>

**社区讨论**: 社区讨论高度务实且以解决方案为导向，用户分享了具体的欧盟服务推荐和真实迁移经验。Hetzner 服务器的性价比、Bunny.net 作为 Cloudflare/S3 替代品以及 mailbox.org 的邮件托管服务获得了显著关注。这一趋势不仅限于欧盟居民，一位加拿大用户描述了其有意停止向美国公司提供资金和数据的努力，同时承认完全脱钩几乎不可能实现。

**标签**: `#data-sovereignty`, `#EU-infrastructure`, `#cloud-migration`, `#privacy`, `#geopolitics`

---

<a id="item-6"></a>
## [深入剖析《过山车大亨》的汇编级优化技巧](https://larstofus.com/2026/03/22/the-gold-standard-of-optimization-a-look-under-the-hood-of-rollercoaster-tycoon/) ⭐️ 7.0/10

一篇详细的技术文章深入分析了《过山车大亨》中使用的底层优化技巧，包括用位移操作替代乘除法、2 的幂次对齐数据结构，以及其他使游戏在 1990 年代硬件上表现卓越的汇编技术。 《过山车大亨》至今仍是游戏史上最著名的手工优化软件范例之一，理解其技术为注重性能的编程提供了宝贵经验，即使在硬件已大幅进步的今天，这些经验依然具有参考价值。 文章重点介绍了位移操作（例如用 `>> 3` 代替 `/ 8`）以及围绕 2 的幂次设计数据结构以实现快速地址计算等技术，但社区成员指出了一个重大错误：文章声称现代编译器不会将除以 2 的幂次优化为位移操作，这是不正确的，因为这是一种广为人知的编译器优化。文章还讨论了游戏设计师如何被要求在游戏公式中使用对 CPU 友好的数字。

hackernews · mariuz · Mar 22, 19:02

**背景**: 《过山车大亨》于 1999 年发布，几乎完全由一位程序员 Chris Sawyer 独立开发，他用 x86 汇编语言编写了游戏约 99%的代码，而非使用 C++ 等高级语言。汇编语言使程序员能够直接控制 CPU 指令，实现极其精细的优化，但代价是开发难度和代码复杂度大幅增加。该游戏在 486 或早期 Pentium 处理器等性能有限的硬件上模拟了包含游客、游乐设施、财务和地形的完整主题公园。OpenRCT2 是该游戏的开源重制版本，通过逆向工程将原始汇编代码转译为 C 语言，保留了许多原始的优化模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RollerCoaster_Tycoon">RollerCoaster Tycoon - Wikipedia</a></li>
<li><a href="https://www.gamedev.net/forums/topic/630027-roller-coaster-tycoon-written-in-assembly/">Roller Coaster Tycoon written in Assembly . - GameDev.net | Forum</a></li>

</ul>
</details>

**社区讨论**: 社区讨论非常活跃，多位评论者质疑了文章中关于编译器不会将除以 2 的幂次优化为位移操作的说法——这是一种广为人知的编译器优化，该错误显著削弱了文章在此方面的可信度。其他评论者分享了有趣的类比案例，指出《魔兽争霸》1/2 和《星际争霸》在 386/486 硬件上出于同样的性能考虑使用了相同的 2 的幂次地图尺寸技术。此外还有关于游戏设计师是否仍需在公式中考虑数值特性的深入讨论，一些人认为即使在 2026 年这仍然具有现实意义。

**标签**: `#game-development`, `#optimization`, `#assembly-language`, `#retrocomputing`, `#software-engineering`

---

<a id="item-7"></a>
## [GitHub appears to be struggling with measly three nines availability](https://www.theregister.com/2026/02/10/github_outages/) ⭐️ 7.0/10

GitHub is struggling to maintain even 99.9% availability, with community criticism pointing to prioritization of AI features and the Azure migration as contributing factors alongside ongoing security concerns.

hackernews · richtr · Mar 23, 10:39

**标签**: `#github`, `#infrastructure`, `#availability`, `#devops`, `#cloud-reliability`

---

<a id="item-8"></a>
## [Reports of code's death are greatly exaggerated](https://stevekrouse.com/precision) ⭐️ 7.0/10

Steve Krouse argues that code and human programmers remain essential despite AI advances, emphasizing that precision and conventional software work won't be easily replaced.

hackernews · stevekrouse · Mar 22, 11:09

**标签**: `#AI-coding`, `#software-engineering`, `#future-of-work`, `#LLMs`, `#developer-productivity`

---

<a id="item-9"></a>
## [Simon Willison 为 Bram Cohen 基于 CRDT 的版本控制系统构建交互式可视化工具](https://simonwillison.net/2026/Mar/22/manyana/#atom-everything) ⭐️ 7.0/10

2026 年 3 月 22 日，Simon Willison 为 Bram Cohen 新发布的基于 CRDT 的版本控制演示项目「Mañana」创建了一个基于浏览器的交互式可视化工具。Willison 使用 Claude 解读了 Cohen 的 470 行 Python 实现，并让 Claude 利用 Pyodide 构建了一个交互式 UI，使算法可以直接在浏览器中运行。 这项工作让 BitTorrent 创始人提出的版本控制新愿景变得人人可以通过浏览器访问和探索。基于 CRDT 的版本控制可能从根本上改变分布式开发中合并冲突的处理方式，而这类交互式可视化工具有助于开发者社区理解和评估这种新颖方案。 Mañana 明确定位为演示项目而非完整的版本控制系统——它仅对单个文件进行操作，尚未实现 cherry-pick 和本地撤销功能，但 README 中描述了这些功能的实现方案。该可视化工具通过 Pyodide（将 CPython 编译为 WebAssembly）直接在浏览器中运行 Python 代码，无需任何服务端基础设施。

rss · Simon Willison · Mar 22, 18:57

**背景**: CRDT（Conflict-free Replicated Data Type，无冲突复制数据类型）是一种专为分布式系统设计的数据结构，允许多个副本独立、并发地更新而无需协调，并保证所有副本最终收敛到相同状态。传统版本控制系统如 Git 通过显式的合并操作处理并发编辑，可能产生需要手动解决的冲突。Bram Cohen 以发明 BitTorrent 闻名，他提出使用 CRDT 作为版本控制新方案的基础，以更优雅地处理合并问题。Pyodide 是一个将 CPython 移植到 WebAssembly 的项目，使完整的 Python 代码可以直接在浏览器中运行而无需服务器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bramcohen.com/p/manyana">Manyana - by Bram Cohen - Bram ’s Thoughts</a></li>
<li><a href="https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type">Conflict-free replicated data type - Wikipedia</a></li>
<li><a href="https://conzit.com/post/envisioning-the-future-of-version-control-with-manyana">Envisioning the Future of Version Control with Manyana</a></li>

</ul>
</details>

**标签**: `#version-control`, `#crdt`, `#pyodide`, `#ai-assisted-development`, `#visualization`

---

<a id="item-10"></a>
## [Musk 宣布在德克萨斯州奥斯汀建设 Terafab 芯片制造工厂](https://www.theverge.com/ai-artificial-intelligence/898722/musk-terafab-chip-plant) ⭐️ 7.0/10

Elon Musk 于 2025 年 6 月 21 日宣布计划在德克萨斯州奥斯汀建设一座名为"Terafab"的半导体制造工厂，由 Tesla、xAI 和 SpaceX 联合开发。该工厂旨在大规模生产芯片，服务于 Musk 旗下各公司在人工智能、机器人和太空数据中心领域的需求。 这一宣布标志着全球最具影响力的科技人物之一正大力推动芯片制造的垂直整合，可能会冲击目前由台积电和三星等代工厂主导的半导体供应链。如果 Terafab 成功落地，将有望降低 Musk 旗下公司对外部芯片供应商的依赖，并重塑 AI 算力基础设施格局。 据报道，该项目将先在奥斯汀建设一座较小规模的先进技术晶圆厂，然后逐步扩展至完整的 Terafab 愿景。目前关于制程节点、投资金额、建设时间线和产能等具体细节仍然匮乏，项目的实际可行性仍存在较大不确定性。

rss · The Verge AI · Mar 22, 14:06

**背景**: 半导体制造工厂（晶圆厂）是全球资本密集度最高的设施之一，通常耗资数百亿美元且需要数年时间建设。目前先进芯片制造主要集中在少数几家公司，包括台湾的台积电（TSMC）、韩国的三星以及美国的 Intel。太空数据中心是一个新兴概念，提议将 AI 计算基础设施部署到轨道上，利用充足的太阳能来解决地面数据中心日益严峻的能源瓶颈问题。Musk 和其他科技高管曾对半导体行业能否跟上 AI 工作负载激增带来的需求表示担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Terafab">Terafab - Wikipedia</a></li>
<li><a href="https://www.cbsnews.com/news/terafab-elon-musk-chips-semiconductors-what-to-know/">What is Elon Musk's Terafab chip project? Here are his "most epic ...</a></li>
<li><a href="https://www.houstonchronicle.com/news/houston-texas/space/article/elon-musk-terafab-chip-22091406.php">Elon Musk's Terafab project begins in Austin for space data centers</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#AI-infrastructure`, `#Elon Musk`, `#chip-manufacturing`, `#Tesla`

---

<a id="item-11"></a>
## [Lossy self-improvement](https://www.interconnects.ai/p/lossy-self-improvement) ⭐️ 7.0/10

Nathan Lambert argues that while AI self-improvement is real, it is inherently 'lossy' and therefore unlikely to lead to rapid recursive intelligence explosion or fast takeoff scenarios.

rss · Interconnects (Nathan Lambert) · Mar 22, 19:39

**标签**: `#AI-safety`, `#self-improvement`, `#AI-alignment`, `#fast-takeoff`, `#AI-capabilities`

---

<a id="item-12"></a>
## [Nelson Elhage 探讨错误处理与 Structured Concurrency 之间的关联](https://blog.nelhage.com/post/concurrent-error-handling/) ⭐️ 7.0/10

知名系统工程师 Nelson Elhage 发表了一篇博客文章，探讨错误处理模式如何自然地引出并与 Structured Concurrency 概念相关联，将编程语言设计中的两个基础领域连接在一起。 Structured Concurrency 正在各大主流编程语言（如 Java 21、Swift、Kotlin）中获得广泛采用，理解它与错误处理这一长期设计难题之间的关系，能帮助开发者更深入地掌握如何编写正确的并发程序。 文章从常见的错误处理模式出发，揭示了 Structured Concurrency 背后的设计动机，指出在并发场景中正确地传播错误本质上需要 Structured Concurrency 所提供的作用域和生命周期保证。

rss · Lobsters · Mar 23, 16:59

**背景**: Structured Concurrency 是一种编程范式，它将并发执行的线程封装在明确定义的作用域内，类似于结构化编程用代码块和函数取代了任意的 "goto" 语句。它确保派生的任务具有清晰的所有权、生命周期和取消语义，从而使并发代码更易于理解。并发程序中的错误处理历来十分困难，因为一个任务中的错误必须在其他任务仍在运行时被可靠地传播和处理。Nelson Elhage（nelhage）是一位备受尊敬的系统程序员，以深入的软件工程技术写作而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Structured_concurrency">Structured concurrency - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 该文章被分享到 Lobsters 并引发了社区讨论，但提供的内容中未包含具体的评论详情。

**标签**: `#structured-concurrency`, `#error-handling`, `#programming-languages`, `#systems-programming`, `#concurrency`

---

<a id="item-13"></a>
## [Whistler 将实时 eBPF 编程引入 Common Lisp REPL](https://atgreen.github.io/repl-yell/posts/whistler/) ⭐️ 7.0/10

Whistler 是一个新项目，使开发者能够从 Common Lisp REPL 中交互式地编写和部署 eBPF 程序，将 Lisp 的实时编程能力与 Linux 内核的可编程性结合起来。 该项目代表了两项强大但鲜有交集的技术的新颖结合，有望为 eBPF 开发提供更快的反馈循环——在这一领域，迭代速度通常受限于针对内核的编译-加载-测试周期。 该项目利用 Common Lisp 的 REPL（Read-Eval-Print Loop）实现 eBPF 程序的实时交互式开发，开发者无需重启工作流即可修改和重新加载内核级的追踪或网络逻辑。目前可获取的技术实现细节有限，但该方案面向同时对 Lisp 和 Linux 内核探测感兴趣的系统程序员。

rss · Lobsters · Mar 23, 01:39

**背景**: eBPF（extended Berkeley Packet Filter）是嵌入 Linux 内核的一项革命性技术，允许用户自定义程序安全地在内核空间运行，无需修改内核源代码或加载内核模块，广泛应用于网络、可观测性、追踪和安全领域。Common Lisp 是一门成熟的编程语言，以其强大的 REPL 驱动交互式开发工作流著称，开发者可以在实时环境中增量地编写、测试和修改代码。将这两项技术结合，使开发者能够利用 Lisp 的快速原型设计优势来处理传统上需要更严格开发周期的内核级编程任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ebpf.io/">eBPF - Introduction, Tutorials & Community Resources</a></li>
<li><a href="https://mastodon.social/@lobsters/116277274990051975">Lobsters: " Whistler : Live eBPF Programming from the Common L…"</a></li>

</ul>
</details>

**社区讨论**: 该项目在 Lobsters 上被分享并引发了一些讨论，但详细的社区评论内容暂不可获取。

**标签**: `#eBPF`, `#Common Lisp`, `#systems-programming`, `#REPL`, `#Linux`

---

<a id="item-14"></a>
## [Nolan Lawson 反思软件编程艺术的衰退](https://nolanlawson.com/2026/03/22/the-diminished-art-of-coding/) ⭐️ 7.0/10

知名软件工程师和 Web 性能专家 Nolan Lawson 于 2026 年 3 月 22 日发表了一篇题为《The Diminished Art of Coding》的反思性文章，探讨在 AI 辅助开发时代，软件编程的工艺和艺术性正在如何衰退。 随着 AI 编程助手迅速改变软件编写方式，这篇文章触及了软件工程社区中一个日益加剧的文化和职业矛盾——编程的深层技艺是否正在被侵蚀。在越来越多开发者依赖 AI 工具生成代码的背景下，这一讨论尤为重要，因为它可能重新定义"技术精湛的程序员"的含义。 这篇文章在技术社区 Lobsters 上被分享和讨论，表明资深开发者对这一话题有浓厚兴趣。虽然文章的具体论点和结论在现有内容中未完全呈现，但从标题和背景来看，文章探讨的是 AI 工具如何将编程从一种创造性技艺转变为更加机械化的过程。

rss · Lobsters · Mar 22, 21:55

**背景**: Nolan Lawson 是一位备受尊敬的软件工程师，目前在 Microsoft Edge 担任 Web 性能项目经理。他在开源社区中因 PouchDB（一个离线优先的 JavaScript 数据库）项目以及在 Web 性能和 Web Components 方面的贡献而广为人知。他在华盛顿大学学习语言学和计算语言学，曾从事机器学习和自然语言处理工作，后来转向 Web 前端开发。凭借在软件工程多个领域的丰富经验，他的观点在开发者社区中具有相当的影响力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/nolanlawson/">nolanlawson (Nolan Lawson) · GitHub PodRocket - Nolan Lawson Nolan Lawson: The changing Open Source landscape, one ... What web components are good at with Nolan Lawson Between the Wires: An interview with Microsoft Edge ...</a></li>
<li><a href="https://opensource.org/maintainers/nolanlawson">Nolan Lawson: The changing Open Source landscape, one ...</a></li>

</ul>
</details>

**社区讨论**: 这篇文章被发布到 Lobsters 社区进行讨论，说明它在开发者群体中引起了共鸣，但具体的评论内容在现有资料中不可获取。

**标签**: `#software-engineering`, `#AI-coding`, `#craft-of-programming`, `#developer-culture`, `#essay`

---

<a id="item-15"></a>
## [Domenic Denicola 批评 Windows 原生应用开发的碎片化现状](https://domenic.me/windows-native-dev/) ⭐️ 7.0/10

知名 Web 标准贡献者 Domenic Denicola 在其博客上发表了一篇详细分析文章，剖析了 Windows 原生应用开发碎片化且令人困惑的现状，重点指出了开发者面临的多种竞争框架和工具链难题。 这一批评揭示了 Windows 开发者长期面临的痛点：他们必须在 Win32、WinForms、WPF、UWP、WinUI 3 和 .NET MAUI 等众多重叠的 UI 框架中艰难抉择，且没有清晰统一的发展路径，这可能促使更多开发者转向跨平台方案或基于 Web 的解决方案。 文章分析了 Microsoft 如何反复推出新的 UI 框架，却未能完全弃用或替代旧框架，导致开发者无法确定应投入哪项技术。Avalonia UI 等第三方替代方案应运而生，尤其在 Microsoft 自身框架难以有效覆盖的跨平台场景中填补了空白。

rss · Lobsters · Mar 22, 13:30

**背景**: 过去二十多年间，Microsoft 为 Windows 桌面开发引入了多种 UI 框架。Win32 和 WinForms 可以追溯到 Windows 最早期，而 WPF（Windows Presentation Foundation）在 2006 年引入了基于 XAML 的 UI。UWP（通用 Windows 平台）于 2015 年随 Windows 10 推出，采用沙箱化的现代应用模型，但此后基本被放弃，转而推出作为 Windows App SDK 一部分的 WinUI 3，为传统桌面应用提供现代 Fluent Design 能力。与此同时，.NET MAUI（多平台应用 UI）于 2022 年作为 Xamarin.Forms 的继任者推出，支持在 Windows、Android、iOS 和 macOS 上进行跨平台开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://avaloniaui.net/blog/winui-vs-wpf-vs-uwp">WinUI vs WPF vs UWP - Avalonia UI</a></li>
<li><a href="https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/">Build desktop Windows apps with the Windows App SDK - Windows ...</a></li>
<li><a href="https://appisto.app/blog/state-of-dotnet-maui">The State of .NET MAUI in 2025: Still Worth It? - appisto.app</a></li>

</ul>
</details>

**社区讨论**: 该文章在 Lobsters 上引发了讨论，开发者们普遍对 Windows 开发生态系统的碎片化表示不满，并就哪个框架（如果有的话）值得作为新项目的长期技术投入展开了辩论。

**标签**: `#windows`, `#native-development`, `#desktop-apps`, `#developer-experience`, `#microsoft`

---

<a id="item-16"></a>
## [Qt 6.11 发布，带来重大图形、异步 C++ 及性能改进](https://www.qt.io/blog/qt-6.11-released) ⭐️ 7.0/10

Qt 6.11 已正式发布，带来了性能提升、增强的图形和 3D 能力、新的连接和语言支持，以及全新的异步 C++ 编程方式。 作为使用最广泛的跨平台应用开发框架之一，Qt 的功能丰富的新版本影响着庞大的桌面、移动和嵌入式开发者生态；而游戏引擎级别的 3D 能力和全新的异步 C++ 模型可能会显著拓展 Qt 的应用范围。 Qt 6.11 引入了 Qt Canvas Painter，这是一个受 HTML5 canvas 2D context 启发的新 2D 渲染组件，据称比现有基于 OpenGL 后端的 QPainter 快得多。该版本还宣称其 3D 能力已达到游戏引擎同等水平。

rss · Lobsters · Mar 23, 19:23

**背景**: Qt 是一个成熟的开源跨平台框架，主要使用 C++ 编写，用于构建桌面、移动和嵌入式系统的图形用户界面和应用程序。它由 The Qt Company 维护，拥有庞大的开发者社区，并提供 Python（PyQt、PySide）等语言的绑定。QPainter 是 Qt 长期使用的 2D 绘图 API，而新的 Canvas Painter 旨在对 2D 渲染工作负载进行现代化改造并提升性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.qt.io/blog/qt-6.11-released">Qt 6 . 11 Released!</a></li>
<li><a href="https://www.phoronix.com/news/Qt-6.11-Toolkit">Qt 6 . 11 Toolkit Released With "The Same 3D Capabilities..." - Phoronix</a></li>

</ul>
</details>

**标签**: `#qt`, `#release`, `#cross-platform`, `#gui-framework`, `#cpp`

---