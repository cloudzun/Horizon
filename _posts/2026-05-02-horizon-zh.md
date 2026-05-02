---
layout: default
title: "Horizon 每日速递：2026-05-02"
date: 2026-05-02
lang: zh
---

> 📅 2026-05-02 · 从 72 条资讯中精选出 16 条重要内容

---

1. [Uber 提议将司机网络转化为自动驾驶传感器网格](#item-1) ⭐️ 8.0/10
2. [DeepSeek V4 预览版模型挑战前沿 AI 能力](#item-2) ⭐️ 8.0/10
3. [英国 AI 安全研究所评估 GPT-5.5 网络能力](#item-3) ⭐️ 8.0/10
4. [马斯克出庭作证，承认 xAI 蒸馏 OpenAI 模型](#item-4) ⭐️ 8.0/10
5. [Ubuntu 基础设施中断阻碍关键漏洞响应](#item-5) ⭐️ 8.0/10
6. [优化 ML-KEM-768 封装密钥以节省 24 个八位字节](#item-6) ⭐️ 8.0/10
7. [VideoLAN 发布开源 AV2 解码器 dav2d](#item-7) ⭐️ 7.0/10
8. [NetHack 5.0.0 发布并引入基于 Lua 的关卡编译](#item-8) ⭐️ 7.0/10
9. [加州开始对自动驾驶汽车交通违章开具罚单](#item-9) ⭐️ 7.0/10
10. [企业 AI 运营兼顾规模化与数据主权](#item-10) ⭐️ 7.0/10
11. [特朗普政府解雇 NSF 全体监督委员会成员](#item-11) ⭐️ 7.0/10
12. [五角大楼与七家科技公司签署机密 AI 合同，Anthropic 落选](#item-12) ⭐️ 7.0/10
13. [用去中心化 Web of Trust 对抗 LLM 垃圾内容](#item-13) ⭐️ 7.0/10
14. [约 200 行 C++实现游戏开发用无栈协程](#item-14) ⭐️ 7.0/10
15. [Dijkstra 1982 年公开信批评 APL 对编程思维的负面影响](#item-15) ⭐️ 7.0/10
16. [SentinelOne 发现 fast16：早于 Stuxnet 的高精度破坏恶意软件](#item-16) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Uber 提议将司机网络转化为自动驾驶传感器网格](https://techcrunch.com/2026/05/01/uber-wants-to-turn-its-millions-of-drivers-into-a-sensor-grid-for-self-driving-companies/) ⭐️ 8.0/10

Uber 正推出一项计划，旨在为其数百万司机配备传感器，构建分布式数据采集网络，从而为自动驾驶汽车公司提供关键的训练场景数据。该计划旨在利用 Uber 现有的车队解决行业当前的数据瓶颈问题，而非仅依赖专用测试车辆。 该战略可通过提供专用车队难以匹敌的、可扩展且地理分布广泛的训练数据，显著加速自动驾驶汽车的开发进程。这也标志着 Uber 的战略转型，使其在更广泛的 AI 与机器人生态系统中扮演关键基础设施合作伙伴的角色。 该计划面临硬件成本、司机同意权以及监管合规等重大障碍，尤其是在需要 LIDAR 等高端传感器的情况下。行业观察人士指出，Uber 的即时真正价值可能在于 shadow mode 模拟，即自动驾驶公司无需部署物理传感器即可利用数百万次真实的 Uber 行程来测试其模型。

hackernews · nickvec · May 2, 15:38

**背景**: 自动驾驶汽车的开发高度依赖机器学习模型，而这些模型需要海量真实驾驶数据进行训练，以识别复杂的交通场景。传统上，公司通常使用配备昂贵传感器的专用测试车队来收集数据，但这限制了地理覆盖范围和可扩展性。众包数据采集利用日常车辆收集道路和交通信息，为更新高精地图和提升 AI 感知系统提供了一种更具成本效益的替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.esri.com/about/newsroom/publications/wherenext/crowdsourced-location-intelligence-autonomous-vehicles">Disrupting the Autonomous-Vehicle Industry with Crowdsourced Maps</a></li>

</ul>
</details>

**社区讨论**: 社区讨论对私人车辆安装传感器的可行性与成本表示怀疑，许多人质疑通用数据相较于专有数据集的实际价值。评论者还强调，Uber 在自动驾驶公司的战略股权投资以及 shadow mode 数据模拟的潜力，比物理传感器网格本身具有更直接的影响力。

**标签**: `#Autonomous Vehicles`, `#Data Infrastructure`, `#AI/ML Training`, `#Tech Strategy`, `#Hacker News Discussion`

---

<a id="item-2"></a>
## [DeepSeek V4 预览版模型挑战前沿 AI 能力](https://simonwillison.net/2026/Apr/24/deepseek-v4/) ⭐️ 8.0/10

DeepSeek 发布了 V4 系列预览版模型，包括拥有 1.6 万亿参数的 V4-Pro 和 2840 亿参数的 V4-Flash，两者均支持百万级上下文窗口，并展现出前沿级别的推理能力。 这些模型为闭源前沿 AI 提供了极具成本效益的替代方案，有望重塑开发者工作流并影响整个行业的 API 定价策略。 这些模型采用 MoE 架构，并结合了 DeepSeek 稀疏注意力机制与逐词压缩技术，但用户指出复杂推理任务可能会消耗比预期更多的 Token。

hackernews · indigodaddy · May 1, 16:52

**背景**: 大型语言模型通常通过标准化基准测试来评估其在编程、数学和推理方面的性能。MoE 架构在每次推理时仅激活总参数的一小部分，从而在保持高能力的同时降低计算成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek-ai/DeepSeek-V4-Pro · Hugging Face</a></li>
<li><a href="https://api-docs.deepseek.com/news/news260424">DeepSeek V4 Preview Release | DeepSeek API Docs</a></li>
<li><a href="https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro">CAISI Evaluation of DeepSeek V4 Pro | NIST</a></li>

</ul>
</details>

**社区讨论**: 开发者称赞 DeepSeek V4 能够直接遵循指令且不像竞品那样频繁触发安全拒绝，同时也指出其在复杂任务中更高的 Token 消耗会部分抵消较低的 API 定价优势。

**标签**: `#Artificial Intelligence`, `#Large Language Models`, `#Software Engineering`, `#Developer Tools`, `#Model Benchmarking`

---

<a id="item-3"></a>
## [英国 AI 安全研究所评估 GPT-5.5 网络能力](https://simonwillison.net/2026/Apr/30/gpt-55-cyber-capabilities/#atom-everything) ⭐️ 8.0/10

英国 AI 安全研究所发布评估报告，指出 OpenAI 的 GPT-5.5 具备与 Anthropic 受限模型 Claude Mythos 相当的网络能力。与 Claude Mythos 不同，GPT-5.5 目前已向公众开放。 这一对比凸显了商用 AI 模型在发现和利用软件漏洞方面的快速进步，引发了关于 AI 安全与防御准备的紧迫问题。安全专家和政策制定者必须立即应对广泛可用的高能力 AI 系统所带来的现实风险。 该评估专门测试了模型发现安全漏洞和开发漏洞利用程序的能力，指出 GPT-5.5 的性能与受限访问的 Claude Mythos 相当。此前 Claude Mythos 因能够针对主流操作系统生成已修补和未修补漏洞的利用程序而受到关注。

rss · Simon Willison · Apr 30, 23:03

**背景**: 大型语言模型正越来越多地被测试用于自动化网络安全任务，包括漏洞发现和漏洞利用程序生成。英国 AI 安全研究所系统性地评估前沿 AI 模型，以了解其在广泛部署前的攻防能力。Claude Mythos 是 Anthropic 开发的先进且受限访问的模型，而 GPT-5.5 则代表 OpenAI 最新广泛发布的版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos">Claude Mythos</a></li>
<li><a href="https://grokipedia.com/page/Claude_Mythos">Claude Mythos</a></li>
<li><a href="https://red.anthropic.com/2026/mythos-preview/">Claude Mythos Preview \ red.anthropic.com</a></li>

</ul>
</details>

**标签**: `#AI Security`, `#LLM Evaluation`, `#Cybersecurity`, `#AI Governance`, `#OpenAI`

---

<a id="item-4"></a>
## [马斯克出庭作证，承认 xAI 蒸馏 OpenAI 模型](https://www.technologyreview.com/2026/05/01/1136800/musk-v-altman-week-1-musk-says-he-was-duped-warns-ai-could-kill-us-all-and-admits-that-xai-distills-openais-models/) ⭐️ 8.0/10

在马斯克与 OpenAI landmark trial 的第一周庭审中，马斯克作证称 Sam Altman 和 Greg Brockman 欺骗了他以获取资金，同时承认其公司 xAI 对 OpenAI 的模型使用了知识蒸馏技术。 这一承认将模型蒸馏技术推向了主流法律审查的焦点，可能重塑整个生成式 AI 行业的知识产权标准和竞争格局。 庭审揭示知识蒸馏是一种广泛接受的机器学习技术，用于将大型模型压缩为更小、更高效的版本，但其在此案中的应用引发了关于专有数据使用的复杂问题。

rss · MIT Technology Review · May 1, 22:08

**背景**: 模型蒸馏（Model Distillation）是一种成熟的机器学习研究方法，通过让较小的学生模型学习较大教师模型的行为来提升效率并降低部署成本。在此次诉讼的背景下，该技术处于关于使用专有输出进行训练是否构成知识产权侵权或公平竞争实践的核心争议之中。马斯克与 OpenAI 的庭审正在审查该公司最初的非营利使命与其当前商业化路线之间的差异，而蒸馏等技术实践已成为整个行业数据溯源争议的关键证据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/codetodeploy/distillation-data-and-double-standards-in-the-ai-race-d6d5fc788ece">AI Model Distillation Explained : Anthropic, Data Extraction, and the...</a></li>
<li><a href="https://labelbox.com/blog/a-pragmatic-introduction-to-model-distillation-for-ai-developers/">A pragmatic introduction to model distillation for AI developers</a></li>
<li><a href="https://www.linkedin.com/pulse/model-distillation-key-scalable-efficient-ai-arpit-gupta-ghy6c">Model Distillation : The Key to Scalable & Efficient AI</a></li>

</ul>
</details>

**标签**: `#AI Industry`, `#Legal Proceedings`, `#Model Distillation`, `#AI Safety`, `#OpenAI vs xAI`

---

<a id="item-5"></a>
## [Ubuntu 基础设施中断阻碍关键漏洞响应](https://arstechnica.com/security/2026/05/ubuntu-infrastructure-has-been-down-for-more-than-a-day/) ⭐️ 8.0/10

Ubuntu 的核心基础设施已中断超过一天，严重阻碍了针对新发现的关键 root 级别漏洞的沟通与协调工作。 此次长时间中断直接影响依赖 Ubuntu 服务获取及时安全补丁的系统管理员与开发者，可能导致系统面临被主动利用的风险。 此次中断特别影响了用于发布安全公告的官方渠道，意味着针对该 root 级别漏洞的缓解措施无法高效分发给受影响的用户。

rss · Ars Technica AI · May 1, 19:12

**背景**: Ubuntu 基础设施包含官方服务器和通信平台，负责向全球数百万 Linux 系统分发软件更新和安全公告。当这些服务出现长时间中断时，整个生态系统将失去在活跃安全威胁期间交付紧急补丁和协调事件响应的主要机制。

**标签**: `#Linux`, `#System Administration`, `#Cybersecurity`, `#Infrastructure`, `#Ubuntu`

---

<a id="item-6"></a>
## [优化 ML-KEM-768 封装密钥以节省 24 个八位字节](https://runxiyu.org/comp/mlkem768pack/) ⭐️ 8.0/10

一项最新的技术分析展示了一种优化的编码技术，成功将 ML-KEM-768 后量子密码算法的封装密钥大小精确减少了 24 个八位字节。该优化针对 NIST FIPS 203 标准中定义的特定序列化格式，且未改变底层的密码学安全性。 这一缩减对于带宽受限的网络和高吞吐量系统极具价值，因为在这些场景中每一个字节都会影响性能和存储成本。随着后量子密码学成为现代基础设施的强制要求，此类微观优化将直接惠及 IoT 设备、移动网络和大规模 TLS 部署。 该优化专注于改进公钥参数的位打包和序列化例程，在严格保持符合 FIPS 203 规范的同时仔细移除了冗余的填充字节。实现者必须确保同时更新编码和解码例程，以防止与符合标准的库出现互操作性故障。

rss · Lobsters · May 2, 04:49

**背景**: ML-KEM-768（前身为 Kyber）是一种由 NIST 标准化的后量子密钥封装机制，旨在抵御未来量子计算机的攻击。密钥封装机制允许发送方使用接收方的公钥安全地生成并传输共享密钥，从而构成 TLS 等现代安全通信的基础。由于基于格密码的算法天生比传统的 RSA 或 ECC 产生更大的密钥尺寸，优化其序列化体积是其在实际应用中落地的一项关键工程挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ML-KEM">ML-KEM - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Key_encapsulation_mechanism">Key encapsulation mechanism</a></li>

</ul>
</details>

**标签**: `#Cryptography`, `#Post-Quantum Cryptography`, `#ML-KEM`, `#Systems Optimization`, `#Security Engineering`

---

<a id="item-7"></a>
## [VideoLAN 发布开源 AV2 解码器 dav2d](https://code.videolan.org/videolan/dav2d) ⭐️ 7.0/10

VideoLAN 发布了 dav2d，这是一款专为 AOMedia 开发的下一代 AV2 视频编码标准设计的高速、可移植的开源解码器。 该早期解码器为多媒体工程师提供了关键的参考实现，以便在官方 AV2 编码器和最终规范成熟前测试播放工作流。它顺应了行业向开放、免版税编解码器转型的趋势，这些编解码器旨在以更低码率提供更高压缩效率，服务于流媒体和广播应用。 该解码器专为小巧、高度可移植和全平台速度优化而设计，但开发者需注意高质量编码器的开发通常滞后于解码器发布。AV2 在 AV1 架构基础上构建，旨在实现显著提升的压缩效率，并增强对 AR、VR 和分屏使用场景的支持。

hackernews · dabinat · May 2, 17:32

**背景**: 像 AV1 及其继任者 AV2 这样的视频编解码器是用于压缩原始视频数据以便高效存储和网络传输的标准化算法。开放媒体联盟（AOMedia）正在开发这些开放且免版税的格式，以满足流媒体、广播和视频通话不断发展的需求。解码器是将压缩视频流重建为可观看帧的关键软件组件，提前提供开源解码器可使开发者在官方编解码器最终定稿前做好播放软件的准备。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AV2_(codec)">AV2 - Wikipedia</a></li>
<li><a href="https://av2.aomedia.org/">AV2 Specification</a></li>

</ul>
</details>

**社区讨论**: 社区对 AV2 相比 AV1 的压缩潜力表现出浓厚兴趣，同时指出高质量编码器的成熟仍需较长时间。部分用户则转向了关于网站用户体验和托管该项目 GitLab 实例性能的题外讨论。

**标签**: `#Video Codecs`, `#AV2`, `#Multimedia Engineering`, `#Open Source`, `#Systems Programming`

---

<a id="item-8"></a>
## [NetHack 5.0.0 发布并引入基于 Lua 的关卡编译](https://nethack.org/v500/release.html) ⭐️ 7.0/10

NetHack 开发团队正式发布了 5.0.0 版本，将传统的 yacc 和 lex 构建时编译器替换为在游戏运行时处理关卡和任务数据的 Lua 系统。此次里程碑式更新还包含了自上一主要版本以来的 3100 多项修复与改动。 这一架构转变使拥有数十年历史的代码库实现了现代化，让关卡设计更加灵活，且贡献者无需掌握复杂的构建时工具链即可参与开发。它展示了老牌开源项目如何通过成功集成现代脚本语言来维持长期开发与社区活力。 由于数据处理和文件结构的根本性改变，旧版存档和遗骨文件无法在 5.0.0 版本中继续使用。Lua 脚本现已直接嵌入游戏包中并在运行时执行，彻底移除了对独立构建时地牢编译器的依赖。

hackernews · rsaarelm · May 2, 18:03

**背景**: NetHack 是一款极具影响力的开源 Roguelike 游戏，最初发布于 1987 年，以其深度的程序化生成、ASCII 图形和复杂机制而闻名。历史上，其关卡和地牢生成依赖于 yacc 和 lex 工具在编译阶段处理文本文件，随着开发工具的演进，这一工作流变得越来越难以维护。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nethack.org/v500/release.html">NetHack 5.0.0: Release Notes</a></li>
<li><a href="https://github.com/NetHack/NetHack">GitHub - NetHack/NetHack: Official NetHack Git Repository · GitHub</a></li>
<li><a href="https://deepwiki.com/NetHack/NetHack/3.2-level-generation">Level Generation | NetHack/NetHack | DeepWiki</a></li>

</ul>
</details>

**社区讨论**: 社区成员表达了强烈的怀旧之情与兴奋，但许多人遗憾地指出此次更新破坏了与数十年老存档的兼容性。开发者和玩家普遍称赞从 yacc 和 lex 向 Lua 的迁移是必要的现代化举措，同时部分用户推荐了 3D 客户端等社区项目，并呼吁开发团队参与未来的 Roguelike 会议。

**标签**: `#Open Source`, `#Game Development`, `#Legacy Systems`, `#Lua`, `#Software Releases`

---

<a id="item-9"></a>
## [加州开始对自动驾驶汽车交通违章开具罚单](https://www.bbc.com/news/articles/clypjx3rg2go) ⭐️ 7.0/10

加州现已开始对违反交通法规的自动驾驶汽车开具罚单，为公共道路上的无人驾驶汽车建立了正式的执法机制。 这一监管转变确立了自动驾驶交通的明确责任框架，确保汽车制造商无法逃避交通违规的责任。 新政策凸显了尚未解决的实际操作挑战，例如执法部门如何在没有人类驾驶员签字或接收罚单的情况下，物理拦截无人驾驶汽车并处理违规记录。

hackernews · geox · May 2, 17:59

**背景**: 自动驾驶汽车依靠先进的软件和传感器系统在公共道路上导航，而非依赖人类驾驶员，这在传统的交通执法模式中留下了空白。历史上，交通罚单主要针对人类驾驶员的行为，这为实施违规的自动化系统带来了监管不确定性。加州现在正通过将自动驾驶技术视为可问责实体，明确现有交通法如何适用于这些无人驾驶技术。

**社区讨论**: 评论者正在积极讨论实际的执法后勤问题，例如警察如何在拦截过程中与无人驾驶汽车互动，同时也提出了关于企业责任阈值以及市政可能因交通罚款而损失收入的担忧。

**标签**: `#Autonomous Vehicles`, `#AI Regulation`, `#Public Policy`, `#Traffic Systems`

---

<a id="item-10"></a>
## [企业 AI 运营兼顾规模化与数据主权](https://www.technologyreview.com/2026/05/01/1136772/operationalizing-ai-for-scale-and-sovereignty/) ⭐️ 7.0/10

麻省理工科技评论在 EmTech AI 会议上的专题讨论探讨了企业如何通过实施严格的治理框架和专用 AI 工厂，在保障数据所有权的同时实现安全、可扩展的 AI 部署。 这一战略转变回应了日益增长的合规与安全需求，使全球组织能够在保持本地数据控制权的同时，充分利用大规模 AI 模型所需的计算基础设施。 AI 工厂作为隔离的专用环境确保了运营独立性与安全的数据流转，而治理框架则需应对复杂的跨境数据存储法律与隐私合规要求。

rss · MIT Technology Review · May 1, 15:31

**背景**: 数据主权规定信息受其生成地法律与监管框架的管辖，随着全球云计算的普及，这一原则变得日益复杂。为满足合规要求并扩展 AI 工作负载，企业正部署 AI 工厂，即专门设计用于主动生成和处理智能数据而非仅存储文件的数据中心。这些设施结合了先进的硬件验证、优化的电力管理和严格的安全协议，以支持企业级 AI 运营。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aws.amazon.com/about-aws/whats-new/2025/12/aws-ai-factories/">Introducing AWS AI Factories</a></li>
<li><a href="https://blogs.sw.siemens.com/tecnomatix/the-rise-of-ai-factories-accelerating-the-design-and-operations-of-next-gen-data-centers/">The rise of AI Factories: accelerating the design and ...</a></li>
<li><a href="https://www.ibm.com/think/topics/data-sovereignty">What is data sovereignty? - IBM</a></li>

</ul>
</details>

**标签**: `#AI Operations`, `#Data Sovereignty`, `#MLOps`, `#Enterprise AI`, `#AI Governance`

---

<a id="item-11"></a>
## [特朗普政府解雇 NSF 全体监督委员会成员](https://www.technologyreview.com/2026/05/01/1136722/mass-firing-trump-fresh-blow-american-science-nsf-nsb/) ⭐️ 7.0/10

特朗普政府近期解雇了美国 NSF 监督委员会的全部 22 名成员，直接撤除了负责指导该机构 90 亿美元研究项目的决策机构。 这一前所未有的举措可能破坏美国数千个学术与科研项目的资金渠道，进而延缓技术创新并削弱国家的科研基础设施。 NSF 依赖其 NSB 制定战略优先级并批准重大资助项目，因此该委员会的突然空缺可能导致关键资金审批和政策执行陷入停滞。

rss · MIT Technology Review · May 1, 09:00

**背景**: NSF 是美国主要的联邦机构之一，负责为非医学领域的各类基础研究与教育提供资金支持。其管理机构 NSB 由总统任命的成员组成，成员任期交错且为期六年，旨在保障政策连续性与专业监督。根据法律规定，该委员会负责向总统和国会提供科学政策建议，并监督基金会的日常运营与预算分配。

**标签**: `#Science Policy`, `#Research Funding`, `#Academic Research`, `#NSF`, `#Government Impact`

---

<a id="item-12"></a>
## [五角大楼与七家科技公司签署机密 AI 合同，Anthropic 落选](https://www.theverge.com/ai-artificial-intelligence/922113/pentagon-ai-classified-openai-google-nvidia) ⭐️ 7.0/10

2026 年 5 月 1 日，美国国防部批准了与 OpenAI、Google、Microsoft、Amazon、Nvidia、xAI 以及初创公司 Reflection AI 的协议，允许其在机密军事网络上部署模型。Anthropic 因拒绝签署允许无限制用于军事行动的技术合同而落选。 此次采购转变加速了商业前沿 AI 在安全国防工作流中的整合，标志着军方在情报和作战能力上对私营部门创新的战略依赖。同时，这也凸显了行业在 AI 伦理部署上的分歧，各企业正努力平衡政府需求与自身安全政策。 获批供应商将在作战、情报和企业运营中支持机密工作流，但具体的战术应用场景尚未公开。获得 Nvidia 支持的初创公司 Reflection AI 与科技巨头一同入选，反映出国防部在传统国防承包商之外多元化 AI 供应链的努力。

rss · The Verge AI · May 1, 14:09

**背景**: 政府机密网络是用于处理敏感国家安全数据的隔离计算环境，任何第三方软件部署前都必须通过严格的安全认证。五角大楼近期的 AI 采购战略旨在快速将商业模型整合到这些安全系统中，以保持与全球对手的技术平衡。Anthropic 公开坚持严格的使用政策，限制其模型被用于武器开发或无限制的致命性应用，这与国防部提出的广泛作战条款直接冲突。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.abhs.in/blog/pentagon-ai-classified-networks-openai-google-nvidia-reflection-anthropic-excluded-2026">Pentagon Deploys AI on Classified Networks: 7 Companies, Not ...</a></li>
<li><a href="https://federalnewsnetwork.com/defense-news/2026/05/dod-strikes-deals-with-major-tech-firms-to-deploy-ai-on-classified-networks/">DoD strikes deals with major tech firms to deploy AI on ...</a></li>
<li><a href="https://techcrunch.com/2025/10/09/reflection-raises-2b-to-be-americas-open-frontier-ai-lab-challenging-deepseek/">Reflection AI raises $2B to be America's open frontier AI lab ...</a></li>

</ul>
</details>

**标签**: `#AI Policy`, `#Government AI`, `#Tech Industry`, `#AI Procurement`, `#Defense Technology`

---

<a id="item-13"></a>
## [用去中心化 Web of Trust 对抗 LLM 垃圾内容](https://blog.tangled.org/vouching/) ⭐️ 7.0/10

本文提出借鉴密码学中的 Web of Trust 模型来验证人类作者身份，以应对日益增长的 LLM 生成垃圾内容问题。 这种去中心化验证方法为集中式 AI 审核提供了可扩展的替代方案，有望在保护用户隐私的同时维护平台生态免受自动化内容泛滥的冲击。 该系统依赖点对点担保来建立可信链条，但必须解决 Sybil 攻击和新用户冷启动等潜在实施挑战。

rss · Lobsters · May 1, 17:17

**背景**: Web of Trust 是一种去中心化密码学框架，最初用于 PGP 和 OpenPGP 系统中验证公钥所有权，无需依赖中心化的证书颁发机构。现代应用将这一概念扩展至去中心化身份验证领域，利用密码学证明和同行背书替代传统的平台控制型身份数据库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Web_of_trust">Web of trust - Wikipedia</a></li>
<li><a href="https://www.geeksforgeeks.org/what-is-web-of-trust/">What is Web of Trust? - GeeksforGeeks</a></li>
<li><a href="https://curity.io/resources/learn/decentralized-identifiers/">Decentralized Identifiers (DIDs) Explained | Curity Identity Server</a></li>

</ul>
</details>

**标签**: `#AI Safety`, `#Content Moderation`, `#Web of Trust`, `#LLM Spam`, `#Decentralized Systems`

---

<a id="item-14"></a>
## [约 200 行 C++实现游戏开发用无栈协程](https://vittorioromeo.com/index/blog/sfex_coroutine.html) ⭐️ 7.0/10

一位开发者发布了一个约 200 行代码的 C++无栈协程教育性实现。该方案展示了专为高性能游戏开发设计的底层控制流管理方法。 该实现为游戏开发者提供了一种透明且无依赖的轻量级替代方案，有助于替代较重的标准库协程功能，从而实现精确的内存与性能控制。掌握这些底层机制有助于工程师优化关键游戏循环并避免隐藏的内存分配开销。 与保存完整调用栈的有栈协程不同，这种无栈方法仅在挂起之间保存协程状态，要求将局部变量存储为类成员或专用状态结构体。该实现通过手动管理控制流避免了堆内存分配，非常适合对延迟要求严格的实时系统。

rss · Lobsters · May 2, 06:33

**背景**: 协程是可以暂停执行并在稍后恢复的函数，允许进行协作式多任务处理而无需传统线程的开销。无栈协程与有栈协程的不同之处在于它不保存完整的调用栈，而是仅保存恢复执行所需的状态，这降低了内存占用，但需要显式的状态管理。C++20 引入了使用 co_await 和 co_yield 关键字的原生无栈协程，但理解手动实现有助于深入掌握编译器转换过程和内存布局。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Coroutine">Coroutine - Wikipedia</a></li>
<li><a href="https://stackoverflow.com/questions/28977302/how-do-stackless-coroutines-differ-from-stackful-coroutines">c++ - How do stackless coroutines differ from... - Stack Overflow</a></li>
<li><a href="https://stackoverflow.com/questions/57163510/are-stackless-c20-coroutines-a-problem">c++ - Are stackless C++20 coroutines a problem? - Stack Overflow</a></li>

</ul>
</details>

**标签**: `#C++`, `#Game Development`, `#Coroutines`, `#Systems Programming`, `#Low-Level Optimization`

---

<a id="item-15"></a>
## [Dijkstra 1982 年公开信批评 APL 对编程思维的负面影响](https://www.jsoftware.com/papers/Dijkstra_Letter.htm) ⭐️ 7.0/10

Edsger W. Dijkstra 于 1982 年发表了一封致 APL 编程语言的公开信，批评其密集的符号语法和面向数组的范式会阻碍清晰思考并助长不良的软件开发实践。 这篇历史文献对现代编程语言设计和软件工程哲学仍具有重要参考价值，揭示了代码可读性与简洁性之间的长期争论。它持续影响着开发者如何评估语言语法及其对程序员认知的影响。 Dijkstra 特别警告称，APL 的极端简洁性和对特殊图形符号的依赖会导致代码过于密集，难以维护和推理。该信件强调，语言设计选择会直接塑造程序员解决问题的方式及整体软件质量。

rss · Lobsters · May 2, 12:34

**背景**: APL 由 Kenneth E. Iverson 于 20 世纪 60 年代开发，以其面向数组的编程范式和大量独特的数学符号而闻名。这种符号化表示法能够实现高度简洁的代码，但要求程序员掌握一套专门的操作符词汇。该语言对后来的函数式编程、电子表格以及数值计算软件包的发展产生了深远影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/APL_(programming_language)">APL (programming language) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/APL_syntax_and_symbols">APL syntax and symbols - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Programming Languages`, `#Computer Science History`, `#Software Engineering`, `#Language Design`, `#Edsger Dijkstra`

---

<a id="item-16"></a>
## [SentinelOne 发现 fast16：早于 Stuxnet 的高精度破坏恶意软件](https://www.sentinelone.com/labs/fast16-mystery-shadowbrokers-reference-reveals-high-precision-software-sabotage-5-years-before-stuxnet/) ⭐️ 7.0/10

SentinelOne Labs 发现并分析了一个可追溯至 2005 年的此前未记录的破坏性恶意软件框架 fast16，其时间比 Stuxnet 早五年。该恶意软件专门针对高精度计算软件，以隐蔽方式篡改计算结果。 这一发现证明了在 Stuxnet 公开之前就已存在精密的网络破坏工具，从而改写了网络战的发展时间线。它揭示了国家级网络能力的早期演变，为现代威胁情报和防御策略提供了重要的历史背景。 fast16.sys 组件通过专门针对工程软件并直接在内存中修补代码，注入几乎无法察觉的数学错误。研究人员将该恶意软件的起源与神秘的 ShadowBrokers 引用联系起来，表明早在二十年前就已使用了高级逆向工程和内存操纵技术。

rss · Lobsters · May 2, 10:23

**背景**: Stuxnet 于 2010 年被发现，被公认为首个旨在物理破坏工业系统（特别是伊朗核离心机）的精密网络武器。在此之前，网络攻击通常局限于数据窃取或系统瘫痪，而非对科学或工程计算进行精确且难以察觉的篡改。了解 fast16 表明，威胁行为者早在网络安全行业意识到此类威胁之前，就已经在开发高度专业化且隐蔽的破坏框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sentinelone.com/labs/fast16-mystery-shadowbrokers-reference-reveals-high-precision-software-sabotage-5-years-before-stuxnet/">fast16 | Mystery ShadowBrokers Reference Reveals High-Precision Software Sabotage 5 Years Before Stuxnet | SentinelOne</a></li>
<li><a href="https://thehackernews.com/2026/04/researchers-uncover-pre-stuxnet-fast16.html">Researchers Uncover Pre-Stuxnet ‘fast16’ Malware Targeting Engineering Software</a></li>
<li><a href="https://www.wired.com/story/fast16-malware-stuxnet-precursor-iran-nuclear-attack/">Newly Deciphered Sabotage Malware May Have Targeted Iran’s ...</a></li>

</ul>
</details>

**社区讨论**: 链接的 Lobsters 帖子引发了安全研究人员之间活跃的技术讨论，大家普遍认可该恶意软件的历史意义，并就其潜在归属和运行机制展开辩论。参与者还分享了关于内存修补技术的见解，并将 fast16 的隐蔽手段与现代高级持续性威胁进行了对比。

**标签**: `#Cybersecurity`, `#Malware Analysis`, `#Threat Intelligence`, `#Cyber Warfare`, `#Reverse Engineering`

---