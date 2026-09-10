---
layout: default
title: "Horizon 每日速递：2026-09-10"
date: 2026-09-10
lang: zh
---

> 📅 2026-09-10 · 从 82 条资讯中精选出 29 条重要内容

---

1. [Calif Research 演示由 AI 辅助构建的微信零点击蠕虫](#item-1) <span class="score-badge score-high">9.0</span>
2. [研究者质疑能否将未发表数学成果托付给 OpenAI](#item-2) <span class="score-badge score-mid">8.0</span>
3. [Shopify 宣布移动端从 React Native 回归原生开发](#item-3) <span class="score-badge score-mid">8.0</span>
4. [Forgejo 16\.0\.4 修复模板仓库处理中的严重 RCE 漏洞](#item-4) <span class="score-badge score-mid">8.0</span>
5. [微软将 Rust 列为一级（Tier\-1）语言](#item-5) <span class="score-badge score-mid">8.0</span>
6. [苹果发布首款折叠屏 iPhone Duo](#item-6) <span class="score-badge score-mid">8.0</span>
7. [OpenAI 宣称给出 Navier–Stokes 反例，引发优先权争议](#item-7) <span class="score-badge score-mid">8.0</span>
8. [OpenAI 宣称解决千禧年数学难题，令学术界不安](#item-8) <span class="score-badge score-mid">8.0</span>
9. [JEP 544 提出对热点 Java 方法进行提前编译（AOT）](#item-9) <span class="score-badge score-mid">8.0</span>
10. [Cognition 发布 SWE\-2 编程模型，称以低 64% 成本逼近前沿水平](#item-10) <span class="score-badge score-mid">7.0</span>
11. [NASA 为火星开发的假彩色技术，如今用来揭示地球上的岩画](#item-11) <span class="score-badge score-mid">7.0</span>
12. [报告审视大型科技公司在美国军工复合体中日益加深的角色](#item-12) <span class="score-badge score-mid">7.0</span>
13. [Raymond Chen 揭秘：Windows XP 用蓄水池抽样算法选择初始用户头像](#item-13) <span class="score-badge score-mid">7.0</span>
14. [Sony 官网&quot;拥有&quot;数字游戏的表述被汇编为诉讼证据](#item-14) <span class="score-badge score-mid">7.0</span>
15. [Terence Tao 警告：AI 正在耗尽开放数学问题资源](#item-15) <span class="score-badge score-mid">7.0</span>
16. [Hugging Face 用 73 节点 Gradio Workflow 重建 AUTOMATIC1111 功能](#item-16) <span class="score-badge score-mid">7.0</span>
17. [IBM 发布 Granite Time Series PatchTST\-FM\-r2，商用友好许可的 SOTA 时序预测模型](#item-17) <span class="score-badge score-mid">7.0</span>
18. [OpenAI 的 Navier\-Stokes 声明引发 AI 数学成果归属争议](#item-18) <span class="score-badge score-mid">7.0</span>
19. [Proofpoint：四个黑客组织共用 BlueMoon 漏洞利用套件](#item-19) <span class="score-badge score-mid">7.0</span>
20. [环球音乐与 ElevenLabs 将推出授权 AI 音乐平台](#item-20) <span class="score-badge score-mid">7.0</span>
21. [数学家要求 OpenAI 证明未用其成果训练模型](#item-21) <span class="score-badge score-mid">7.0</span>
22. [Suno 发布 v6：首个获得唱片业授权的 AI 音乐模型](#item-22) <span class="score-badge score-mid">7.0</span>
23. [Apple 为 iPhone 18 Pro 推出“Reference Image”模式，用密码学签名照片](#item-23) <span class="score-badge score-mid">7.0</span>
24. [Interconnects：一次辞职让 AI 安全恐慌从余烬变成野火](#item-24) <span class="score-badge score-mid">7.0</span>
25. [Raschka 解析 looped transformer 与 GPT\-6 Astra 隐藏推理传闻](#item-25) <span class="score-badge score-mid">7.0</span>
26. [CHERIoT 无需 MMU 也能实现强硬件隔离](#item-26) <span class="score-badge score-mid">7.0</span>
27. [trynix\-preview GitHub Action 让评审者直接在浏览器中启动 PR 的 Nix 构建](#item-27) <span class="score-badge score-mid">7.0</span>
28. [解码 NEC V20 微码，推进周期精确仿真](#item-28) <span class="score-badge score-mid">7.0</span>
29. [Brown CEL 论文绘制跨语言 async/await 设计空间图谱](#item-29) <span class="score-badge score-mid">7.0</span>

---

<a id="item-1"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://simonwillison.net/2026/Sep/10/calif-research/">Calif Research 演示由 AI 辅助构建的微信零点击蠕虫</a><span class="score-badge score-high">9.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Simon Willison</span><span class="news-time">Sep 10, 00:56</span></div>
<p class="news-summary">2026 年 9 月 10 日，Calif Research 发布了 WeWorm 的演示，称其为首个通过微信通话在 iOS 和 Android 上传播的零点击蠕虫。据该团队描述，受害者无需接听电话，甚至完全不需要操作手机；即使接听，也听不到任何声音，攻击依然成功。该团队称，借助 AI，他们在约两天内找到了漏洞并写出了首个远程代码执行（RCE）漏洞利用，随后又用一周时间完成了蠕虫的构建。 如果这一说法得到证实，它将成为移动安全与 AI 风险领域的一个重要里程碑：一个无需任何用户交互、且能跨越两大主流移动平台、并借由拥有数十亿用户的即时通讯应用传播的蠕虫，意味着攻击能力的显著升级。该团队所称 AI 将过去需要更大团队耗时数月的工作压缩到大约两天，也直接呼应了当前关于 AI 降低漏洞利用开发门槛的争论。 该内容来自 Calif Research 自行发布的演示，而非经过独立验证的安全公告，且所提供的内容中没有给出 CVE 编号、受影响的微信版本号或底层漏洞的具体细节。文中称人类团队负责判断攻击目标以及如何安全测试，暗示 AI 承担了大部分漏洞利用实现工作，而人类负责确定方向；在所提供的材料中，该蠕虫及演示尚未得到腾讯或第三方研究人员的证实。</p>
<div class="news-background"><strong>背景</strong> 零点击漏洞利用无需用户任何操作即可攻陷设备——不需要点击、不需要打开链接、也不需要接听电话，因此比依赖诱骗用户交互的攻击更难被发现和防御。远程代码执行（RCE）是一类允许攻击者通过网络在目标机器上运行任意代码的漏洞，通常是把一个 bug 变成完整入侵的关键一步。这类威胁过去往往需要资源充足的团队投入数月时间，因此关于 AI 能够加速漏洞发现与武器化的说法受到防御方和政策制定者的密切关注。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.f5.com/glossary/zero-click-attack">Zero - click attack | F5</a></li>
<li><a href="https://en.wikipedia.org/wiki/Remote_code_execution">Remote code execution</a></li>
<li><a href="https://horizon3.ai/intelligence/blogs/ai-exploit-speed-scale/">AI-Powered Exploit Generation: Speed, Scale &amp; Cyber Risk | Horizon3</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#cybersecurity</span> <span class="tag">#AI</span> <span class="tag">#zero-click exploit</span> <span class="tag">#mobile security</span> <span class="tag">#WeChat</span></div>
</article>
<hr>

<a id="item-2"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://mathstodon.xyz/@andreasthom/117240535270608201">研究者质疑能否将未发表数学成果托付给 OpenAI</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">pred_</span><span class="news-time">Sep 10, 06:49</span></div>
<p class="news-summary">一个 Hacker News 讨论帖（评分 8.0/10，518 分、532 条评论）聚焦于一种担忧：OpenAI 可能未经署名就使用了合作研究者分享的未发表数学成果，帖子链接了 Andreas Thom 在 Mathstodon 上的发言以及 X 和 Bluesky 上的相关贴文。讨论的起因是有说法称某重要数学证明可能存在于模型的训练数据中，由此引发了关于成果是否应归功于合作研究者的争论。 这一事件提出了 AI 实验室与学术数学家合作时的署名规范与数据来源问题，并可能影响研究者今后是否愿意把未发表的思路分享给商业模型。由于数学界极为看重明确的作者归属，一旦实验室被怀疑无署名地复用保密合作内容，实验室赖以获取专家输入的信任基础就会直接受损。 相关证据仍属争议而非定论：评论者指出 OpenAI 已声明其模型并未在上述对话上训练过，而且“训练数据影响”和“在可验证数学上通过强化学习真正有所发现”这两种解释可能同时成立。也有人提出间接迹象，例如有说法称 OpenAI 在得知某项重要证明可能存在于训练数据后不久，就用一个仍在训练中的模型生成了 3000 亿输出 token，并形容这让人感觉像是“parallel construction”（平行构造证据）。</p>
<div class="news-background"><strong>背景</strong> Mathstodon 是面向数学工作者的 Mastodon 实例，支持 LaTeX 渲染，因此该领域的技术争论常在平台上展开；这个讨论帖还链接到 X（可通过 xcancel 前端访问）和 Bluesky，后者的帖子以 did:plc 去中心化标识符寻址。研究者会使用包括 Codex 在内的 OpenAI 模型来攻克开放问题，评论者还引用了一些说法：OpenAI 曾向大量研究者提供免费访问权限，而其内部模型被形容为以惊人速度解决开放问题。核心矛盾在于，研究者通常研究的是尚未解决的问题，因此与模型的任何互动都可能向其输入新鲜的、未发表的材料，而这些内容日后出现在实验室成果中时，往往难以证实或证伪。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://mathstodon.xyz/">About - Mathstodon</a></li>
<li><a href="https://www.emergentmind.com/topics/bluesky-social-network">Bluesky : Decentralized Social Network</a></li>
<li><a href="https://discuss.privacyguides.net/t/recommend-xcancel-com-twitter-frontend/21177">Recommend xcancel.com (Twitter Frontend) - Tool Suggestions ...</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 整体情绪对 OpenAI 持怀疑态度。评论者认为，如果把 OpenAI 视作一个人类合作者——在共同讨论中获取想法，随后沿着这些思路发表成果却不署名——这种行为会被视为极不道德；但也有人提出另一种解释：在大规模可验证数学任务上进行强化学习，本身就可能独立发现与任何具体对话无关的技巧。部分人进一步怀疑 AI 是否真的在开放问题上快速进步，还是外界被误导；也有人批评 OpenAI 在训练与生成决策上的时间点可疑。</div>
<div class="news-tags"><span class="tag">#OpenAI</span> <span class="tag">#AI research ethics</span> <span class="tag">#mathematics</span> <span class="tag">#research integrity</span> <span class="tag">#training data</span></div>
</article>
<hr>

<a id="item-3"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://shopify.engineering/back-to-native">Shopify 宣布移动端从 React Native 回归原生开发</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Sep 10, 15:19</span></div>
<p class="news-summary">Shopify 宣布将移动应用从 React Native 迁移回完全原生的 Swift 和 Kotlin 开发，推翻了其在 2020 年全面押注 React Native 的决定。Shop 应用是第一个完成迁移的，借助 AI 辅助，从概念验证到在应用商店发布的全原生应用仅用了 12 周；而拥有 300 多个屏幕的更大的 Shopify 应用也已在迁移中，预计今年晚些时候发布。 这是一家曾公开力挺 React Native 的重要工程团队做出的显著反转，表明 AI 编码模型正在重塑跨平台框架与平台原生开发之间的经典权衡。这一决定很可能影响其他大公司对 React Native 与原生开发的选择，并对 React Native 生态以及移动工程师的技能预期产生影响。 Shopify 表示他们构建了一个名为 Helix 的系统来逐步迁移，因为直接把 LLM 指向 React Native 代码库、试图一次性生成等价原生功能，只会产出无法维护、无法发布的代码。公司仍然称 React Native 是“一个优秀的框架”，并感谢 React Native 社区以及 Software Mansion（Reanimated 的作者）；同时提到此前在性能优化、跟进框架更新和外部依赖上耗费了大量时间。</p>
<div class="news-background"><strong>背景</strong> React Native 是 Meta 开源的一套框架，让开发者用同一套 JavaScript/React 代码库构建 Android 和 iOS 应用，因此很受希望“一次开发、多端复用”而非分别用 Swift 和 Kotlin 各写一遍的公司欢迎。Shopify 在 2020 年全面采用它，是为了避免重复开发同一功能、让非移动背景的开发者也能贡献代码，并摆脱不断追赶功能对齐的负担；2025 年 1 月仍有工程师撰文称 React Native 前景光明。Shopify 现在表示当初的押注是成功的，但编码模型的显著进步消除了跨平台方案的主要成本优势，因此他们从第一性原理重新审视了这个决定。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/React_Native">React Native</a></li>
<li><a href="https://reactnative.dev/">React Native · Learn once, write anywhere</a></li>
<li><a href="https://android-developers.googleblog.com/2026/05/build-android-apps-google-ai-studio.html">Build native Android apps in Google AI Studio</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 上的讨论（636 分、427 条评论）整体偏向务实而非绝对化，Waterluvian 等评论者认为 React Native 与原生之争只是一个由公司具体问题和资源决定的一般工程决策。多位开发者表示自己也做了同样的切换——tonic_note 称 AI 生成已让 React Native 失去大部分优势，keithnz 说在 AI 帮助下原生方案“手感好得多”，atonse 则描述了用 Codex 和 Maestro 几乎在一夜之间把一款 15-20 屏的应用从 React Native 迁移到 Android 和 iOS。pkaler 等人则把这场争论看作可追溯到 Cordova 时代的移动开发长期循环。</div>
<div class="news-tags"><span class="tag">#React Native</span> <span class="tag">#Mobile Development</span> <span class="tag">#Native Apps</span> <span class="tag">#Shopify</span> <span class="tag">#Engineering Strategy</span></div>
</article>
<hr>

<a id="item-4"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://codeberg.org/forgejo/forgejo/src/branch/forgejo/release-notes-published/16.0.4.md">Forgejo 16.0.4 修复模板仓库处理中的严重 RCE 漏洞</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">Lobsters</span><span class="news-time">Sep 10, 15:57</span></div>
<p class="news-summary">Forgejo 发布了 16.0.4 版本，修复了存在于 16.0.3 及之前版本中的一个严重远程代码执行（RCE）漏洞。已发布的 release notes 中列出了一项关键安全修复，即 PR #14301，标题为“防止模板展开干扰 git 仓库初始化”。 Forgejo 被广泛用作自托管的 Git 基础设施，因此这一严重 RCE 漏洞会影响所有尚未修补的实例，并可能波及其上托管的代码和 CI 流水线。此次披露还引发了与同源的 Gitea 项目的对比，以及社区关于漏洞发现与报告方式的更广泛讨论。 根据社区引用的 release notes，当从模板仓库生成新仓库时，Forgejo 会克隆模板仓库、删除 .git 文件夹、对 .forgejo/template 中列出的文件执行变量模板展开，然后初始化一个新的 git 仓库——而该漏洞正是模板展开干扰了这一初始化过程。有评论者指出，由于 Codeberg 的限流，release notes 页面一度难以访问；Gitea 项目的一位负责人则表示，Gitea 对本次修复的两个问题均不受影响。</p>
<div class="news-background"><strong>背景</strong> Forgejo 是一个跨平台、开源、可自托管的“forge”（代码托管平台），它使用 Git 进行版本控制，并提供 issue 跟踪、代码审查、wiki 和 CI 等功能。它源自 Gitea，而 Gitea 又派生自 Gogs，使用 Go 编写；Codeberg 等实例是最受关注的部署之一。远程代码执行（RCE）是一类漏洞，攻击者可以通过网络等手段在目标机器上运行任意命令或代码，因此它被视为最严重的安全漏洞类别之一。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Forgejo">Forgejo</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gitea">Gitea</a></li>
<li><a href="https://en.wikipedia.org/wiki/Remote_code_execution">Remote code execution</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 讨论总体偏技术性且态度正面，有评论者引用了这两项修复内容，还有人建议改用另一个 milestone 链接来查看发布说明。Gitea 项目的一位负责人表示 Gitea 不受这两个问题影响，同时提醒不应因安全事件而去指责报告者；另有评论者认为，在攻击者可能利用 AI 寻找漏洞的情况下，Forgejo 禁止 LLM 贡献的做法或许会让自己处于劣势。</div>
<div class="news-tags"><span class="tag">#security</span> <span class="tag">#vulnerability</span> <span class="tag">#rce</span> <span class="tag">#forgejo</span> <span class="tag">#git</span></div>
</article>
<hr>

<a id="item-5"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/">微软将 Rust 列为一级（Tier-1）语言</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">Lobsters</span><span class="news-time">Sep 10, 13:39</span></div>
<p class="news-summary">Rust Foundation 网站上的一篇客座文章指出，Rust 已成为微软的一级（Tier-1）语言，意味着微软将其视为生产软件中官方支持的一等选项，而不再是实验性语言。文章同时提到微软仍在持续推进 Rust 与 C++ 的原生平台能力演进。 微软是操作系统与 C/C++ 工具链领域最大的厂商之一，正式将 Rust 提升为一级语言，表明这一重量级平台拥有者已把 Rust 视为新代码的系统编程严肃选项。有评论者指出，这意味着所有在 C 和 C++ 工具链上同样有话语权的主流操作系统厂商，如今都在为全新项目多元化其系统编程语言选择。 这篇客座文章指出，经过数十年积累，C++ 在微软内部仍占主导地位，而微软的生产软件需经过严格的安全与质量流程；该文本身是发布在 Rust Foundation 网站上的客座投稿，并非微软的官方规范文档。在 Hacker News 讨论中，有评论者称真正的技术变化是用 MSVC 后端取代 LLVM，也有人追问 Visual Studio 何时提供 Rust 的一级调试支持——这两点均来自社区讨论，而非原文。</p>
<div class="news-background"><strong>背景</strong> Rust 是一门系统编程语言，其所有权（ownership）与借用检查（borrow checking）规则可在没有垃圾回收器的情况下提供内存安全，因此常被视为比 C 和 C++ 更安全的替代方案。微软多年来持续投入 Rust，包括在 Windows 中加入 Rust 组件，以及 Azure CTO Mark Russinovich 公开指出 CVE 中有很大比例源于内存安全问题。平台厂商的“一级（Tier-1）”地位通常意味着该语言获得官方生产环境支持与一等工具链集成；历史上 Rust 通过 LLVM 后端编译，而 MSVC（cl.exe）是微软自家的 C/C++ 编译器工具链。Zig 和 Odin 是较新的“更好的 C”语言，常被拿来与 Rust 比较，定位更底层、抽象更少。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/">Guest Post: Rust Is Tier - 1 Language at Microsoft</a></li>
<li><a href="https://news.ycombinator.com/item?id=49643546">Rust Is Tier - 1 Language at Microsoft | Hacker News</a></li>
<li><a href="https://learn.microsoft.com/en-us/cpp/build/reference/compiler-options?view=msvc-170">MSVC Compiler Options | Microsoft Learn</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 的讨论帖（564 分、305 条评论）总体积极但偏技术性：有评论者认为这一公告表明 Rust 已不再是“快速迭代、爱破坏兼容性”的稚嫩语言，其成熟度高于 Zig、Odin 等较新的“更好的 C/C++”语言；另一位评论者则强调，主流操作系统厂商如今都已多元化其系统编程语言选项，关于 MSVC 集成的公开消息也终于出现。还有人将此举与内存安全的经济账联系起来——引用约 70% 的 CVE 属于内存安全问题的说法——并给出微软计划到 2030 年通过自动化工具转换 10 亿行代码到 Rust，以及 DARPA 资助 C 到 Rust 转换研究的相关链接。</div>
<div class="news-tags"><span class="tag">#rust</span> <span class="tag">#microsoft</span> <span class="tag">#systems-programming</span> <span class="tag">#memory-safety</span> <span class="tag">#language-tooling</span></div>
</article>
<hr>

<a id="item-6"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.apple.com/iphone-duo/">苹果发布首款折叠屏 iPhone Duo</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">thecosmicfrog</span><span class="news-time">Sep 9, 18:15</span></div>
<p class="news-summary">苹果在其九月发布会上正式推出首款折叠屏 iPhone——iPhone Duo，起售价 1,999 美元，计划于 2026 年 10 月 23 日发售。这款护照式折叠机展开后为 7.6 英寸屏幕，苹果称其为 iPhone 史上最大、最薄的显示屏，面积比 iPhone 18 Pro Max 大约多出 50%。 这标志着苹果终于进入高端折叠屏市场；由于它是 iPhone，此前基本忽视折叠形态的开发者可能会真正为额外屏幕空间设计应用。一位使用 Google Pixel 折叠机的评论者指出，目前不少应用在折叠屏上要么完全无法运行，要么只是被拉伸，因此苹果的推动对 Android 折叠屏用户同样可能带来好处。 iPhone Duo 搭载全新的 A20 Pro 芯片，可同时驱动两块屏幕，并配备均热板散热以及苹果新的 C2 调制解调器以提升能效和网络速度；AT&amp;T 列出其配色为 Star White 与 Night Sky，折叠状态下可提供最长 44 小时视频播放。苹果将其定位为可放入口袋、且“比其他智能手机更保值”的设计，并与 iPhone 18 Pro 和 Pro Max 一同发布。</p>
<div class="news-background"><strong>背景</strong> 折叠屏手机通过铰链让屏幕展开成更大、接近平板的画面；苹果此前一直缺席这一品类，而 Google 等竞争对手已有折叠机在售。苹果的“护照式”设计意味着 Duo 比许多同类折叠机更矮更宽，更像一本小册子而不是一台展开的高长手机。在 1,999 美元的定价面前，消费者也在权衡苹果第一代硬件的记录，参考的正是 Apple Vision Pro 的市场反馈。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/IPhone_Duo">IPhone Duo</a></li>
<li><a href="https://www.apple.com/iphone-duo/">iPhone Duo - Apple</a></li>
<li><a href="https://tech.yahoo.com/phones/breaking-news/article/the-iphone-duo-is-official-apples-first-foldable-phone-arrives-october-23-starting-at-1999-175639957.html">The iPhone Duo is official: Apple&#x27;s first foldable phone ... Apple unveils its first foldable, the iPhone Duo - TechCrunch Apple Unveils the iPhone Duo, a Foldable Phone That Costs ... iPhone Duo - Apple (IN) iPhone Duo Is Apple&#x27;s First Foldable Phone. Surprise, It&#x27;s ...</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 的讨论（约 2,400 条评论）在真实的兴奋与价格质疑之间交织：一位 Pixel 折叠机用户欢迎苹果推动开发者为折叠屏认真设计应用，另一位则称赞 John Ternus 的演示有趣好玩。但主流情绪仍是对 1,999 美元的“价格惊吓”——即便以旧换新也觉得难以承受——以及对手机越做越大、苹果无意回归 iPhone 12/13 mini 或 Nexus 4 那种小尺寸的失望。多位评论者把这笔支出视为“花两千美元买第一代苹果产品”的风险，尤其是在 Vision Pro 之后。</div>
<div class="news-tags"><span class="tag">#apple</span> <span class="tag">#iphone</span> <span class="tag">#foldable-phones</span> <span class="tag">#hardware</span> <span class="tag">#mobile</span></div>
</article>
<hr>

<a id="item-7"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://simonwillison.net/2026/Sep/8/on-navier-stokes/">OpenAI 宣称给出 Navier–Stokes 反例，引发优先权争议</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Simon Willison</span><span class="news-time">Sep 8, 23:55</span></div>
<p class="news-summary">在 2026 年 9 月 8 日的一篇 link blog 文章中，Simon Willison 转述了 OpenAI 的说法：该公司使用一个未公开的内部模型——据报道是由约一万个 AI agent 组成的集群——给出了 Navier–Stokes 存在性与光滑性问题的解决结果，并附带了 Lean 证明助手中的形式化验证。该声明同时卷入一场优先权争议：纽约大学数学教授 Tristan Buckmaster 与供职于 Anthropic 的 Levent Alpöge 已在该问题上合作近一年并于 8 月 15 日取得突破，而 OpenAI 表示自己的攻关始于 9 月 1 日，起因是听到一则传闻。 如果获得独立验证，这将是自庞加莱猜想以来首个被解决的千禧年大奖难题，也将成为 AI for science 的标志性时刻——前沿模型开始攻克纯数学中长期悬而未决的公开问题。同时，它把研究优先权、成果归属以及 AI 辅助工作是否可能被追溯或泄露的问题，直接推到了相互竞争的 AI 实验室之间的公开辩论中。 根据该文章转述的说法，Navier–Stokes 相关攻关涉及约 270 万条 agent 消息和约 1300 亿输出 token，而所有尝试过的问题合计使用了 490 万条消息和约 3000 亿输出 token——按被称为 GPT-6 Astra 的模型公开 API 价格计算，成本约为 1500 万美元。据报道，OpenAI 于 9 月 6 日完成项目与 Lean 验证，声称在 Buckmaster 和 Alpöge 的成果公开之前未通过任何途径接触其工作，并表示不会申领 Clay 研究所的 100 万美元千禧年大奖；该结果尚未得到外部数学家或 Clay 数学研究所的验证。</p>
<div class="news-background"><strong>背景</strong> 千禧年大奖难题是 Clay 数学研究所于 2000 年选定的七个高难度数学问题，每个问题的正确解答可获 100 万美元奖金；截至 2026 年，只有庞加莱猜想被正式解决，而 Grigori Perelman 在 2010 年拒绝领奖。Navier–Stokes 存在性与光滑性问题问的是：描述流体运动的方程在三维空间和所有未来时间上是否总存在光滑且整体有定义的解，还是解可能发生爆破——真实流体中的湍流至今仍是物理学最大的未解难题之一。这则新闻也发生在关于“用于训练或提示 AI 模型的用户会话是否会泄漏进后续模型”的更广泛讨论背景之下，Willison 将其提炼为自己新的“假设性问题”：如果你用 ChatGPT 部分解决了一个千禧年难题，你的工作影响训练、进而让后来者率先解出它的概率有多大。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier-Stokes_existence_and_smoothness_problem">Navier-Stokes existence and smoothness problem</a></li>
<li><a href="https://en.wikipedia.org/wiki/Millennium_Prize_Problems">Millennium Prize Problems</a></li>
<li><a href="https://www.claymath.org/millennium-problems/">The Millennium Prize Problems - Clay Mathematics Institute</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Navier-Stokes</span> <span class="tag">#Millennium Prize</span> <span class="tag">#OpenAI</span> <span class="tag">#mathematics</span> <span class="tag">#AI for science</span></div>
</article>
<hr>

<a id="item-8"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.theverge.com/ai-artificial-intelligence/992953/openai-math-millennium-prize-navier-stokes">OpenAI 宣称解决千禧年数学难题，令学术界不安</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">The Verge AI</span><span class="news-time">Sep 9, 21:16</span></div>
<p class="news-summary">OpenAI 周二宣布，其一款尚未发布的模型仅用 88 小时就找到了纳维-斯托克斯（Navier-Stokes）存在性与光滑性问题的解，而这是克雷数学研究所（Clay Mathematics Institute）设立的千禧年大奖难题之一，相关说法出自该公司当天发布的博客文章。OpenAI 表示无意领取该问题附带的 100 万美元奖金，并称其唯一目的是报告自家 AI 模型取得的进展。 如果这一结果站得住脚，那么由机器给出、困扰人类研究者数代之久的难题的解答，将有力地说明 AI 正在多快地挺进数学前沿。但与此同时，OpenAI 推进此事的方式——据报道是在 Twitter 上听到传闻后抢在其他研究者之前冲刺——引发了“抢发”“刺探”以及违反学术惯例的指控，数学家担心这会给整个领域带来寒蝉效应。 OpenAI 的文章称，其系统表明流体运动的纳维-斯托克斯方程动力学可以在有限时间内产生奇点；研究员 Sébastien Bubeck 在新闻发布会上表示，团队是在“在 Twitter 上”看到竞争对手取得进展的传闻后才动手的。该结果尚未得到克雷数学研究所的验证或授奖，而且据报道 OpenAI 在 9 月之前并未公开涉足该问题，因此其真正的技术实质仍存争议。</p>
<div class="news-background"><strong>背景</strong> 千禧年大奖难题是克雷数学研究所于 2000 年选定的七个著名未解难题，每个难题的首个正确解答都可获得 100 万美元奖金。纳维-斯托克斯存在性与光滑性问题追问的是：描述流体运动的方程是否总有性质良好的解，还是可能崩溃为奇点；它与湍流这一物理学中最难的未解问题之一密切相关。由于奖金的存在，该问题是数学界研究最密集的题目之一，但据本文所述，它已让人类研究者困扰了近 90 年。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/navier-stokes-solution/">On the Navier–Stokes Millennium Prize Problem | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Navier–Stokes_existence_and_smoothness">Navier–Stokes existence and smoothness - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Millennium_Prize_Problems">Millennium Prize Problems - Wikipedia</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#OpenAI</span> <span class="tag">#mathematics</span> <span class="tag">#Navier-Stokes</span> <span class="tag">#AI research</span> <span class="tag">#academia</span></div>
</article>
<hr>

<a id="item-9"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://openjdk.org/jeps/544">JEP 544 提出对热点 Java 方法进行提前编译（AOT）</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Sep 10, 17:31</span></div>
<p class="news-summary">由 John Rose 主导、目前处于 Candidate 状态的 JEP 544 提出在训练运行（training run）中把选定的热点应用方法编译为本地代码，并存入 AOT 缓存，使 HotSpot 启动时即可直接使用这些优化后的本地代码。缓存生成沿用既有的 -XX:AOTCacheOutput=app.aot 工作流，生产环境则通过 -XX:AOTCache=app.aot 使用缓存，无需额外选项。 如果最终落地，这将让 Java 应用更快达到峰值性能，并在负载变化时仍能保持峰值性能，这对生命周期短暂或需要自动扩缩容的云原生服务尤为重要——JIT 预热开销一直是这类场景的痛点。该提案延续了 Project Leyden 在不改动应用代码的前提下改善启动、预热与内存占用的思路，但它目前仍只是 Candidate JEP，并非已定稿或已发布的功能。 AOT 代码与 JIT 代码可以共存且完全互操作，因为二者都由同一套 C1 和 C2 编译器生成；当 AOT 代码缺失、不兼容、不适用或之后被反优化（deoptimize）时，执行会回退到解释器和 JIT 机制。初期仅支持 AArch64 和 x64 架构，同时必须继续支持 Serial、Parallel、G1 和 ZGC 垃圾收集器；HotSpot 默认会把 AOT 代码写入缓存，同时继续保存 profile 数据，用于安排 AOT 代码的加载顺序并指导后续的 JIT 编译。</p>
<div class="news-background"><strong>背景</strong> Java 传统上依赖即时编译（JIT）：HotSpot 虚拟机先以解释方式执行字节码，只有在观察到足够的运行时行为后，才会用 C1 和 C2 把频繁执行的“热点”方法编译为本地代码，这也是应用需要一段预热期才能达到峰值性能的原因。提前编译（AOT）则是在生产运行之前就生成本地代码，代价是可能针对了错误的工作负载进行优化。Project Leyden 是 OpenJDK 为改善 Java 启动时间、预热与内存占用而设立的项目，此前已产出 JEP 483（提前类加载与链接，目标版本为 JDK 24），正是它引入了 JEP 544 所要扩展的 AOT 缓存工作流，此外还有 JEP 515（提前方法 profiling）等相关工作。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://openjdk.org/projects/leyden/">Project Leyden - OpenJDK</a></li>
<li><a href="https://openjdk.org/jeps/483">JEP 483 : Ahead - of - Time Class Loading &amp; Linking</a></li>
<li><a href="https://openjdk.org/jeps/515">JEP 515: Ahead-of-Time Method Profiling - OpenJDK AOT Cache :: Spring Boot JEP 516: Ahead-of-Time Object Caching with Any GC - OpenJDK Leyden AOT Cache Usage And Configuration - GitHub Exploring Advanced JVM Options | Baeldung Ahead-of-Time Processing With the JVM :: Spring Boot A Guide to Ahead-of-Time Cache in the Java - daily.dev</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Java</span> <span class="tag">#OpenJDK</span> <span class="tag">#JVM</span> <span class="tag">#AOT Compilation</span> <span class="tag">#Project Leyden</span></div>
</article>
<hr>

<a id="item-10"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://cognition.com/blog/swe-2">Cognition 发布 SWE-2 编程模型，称以低 64% 成本逼近前沿水平</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">seelos</span><span class="news-time">Sep 10, 15:29</span></div>
<p class="news-summary">Cognition 发布了 SWE-2，称其为自己最先进的编程模型，在 FrontierCode 1.1 Main 上取得 50.0% 的成绩，与 Fable 5.1 仅差一个百分点，而单任务成本低 64%。据 Cognition 介绍，SWE-2 是在 Kimi K3 基础上后训练而来，首次将强化学习扩展到数万亿参数规模，并沿用了 SWE-1.7 的训练基础设施与配方。 此次发布显示，在已有强大基础模型之上进行后训练与强化学习，能够把编程智能体推进到接近前沿模型的水准，这可能降低开发者与依赖 AI 编程工具的公司使用门槛。与此同时，它也加剧了闭源权重模型与开源替代方案之间的争论——有评论者认为，各实验室必须解释用户为何要选择又一个闭源模型，而不是更便宜的开源方案。 第三方信息将 SWE-2 描述为约 2800B 参数、采用专有许可的模型，且 Cognition 并未公布按 token 计费的 API 价格，因此“比 Fable 5.1 便宜 64%”是一个按任务计算的定价口径，而非公开的每百万 token 价目表，且这些数字均来自 Cognition 自身、尚待独立复现。评论者还指出，该模型在 Terminal Bench 2.1 上得分 92.8%，而在刚发布几周的 Terminal Bench 4 上仅得 27.3%，两者差距悬殊。</p>
<div class="news-background"><strong>背景</strong> Cognition 是自主 AI 编程智能体 Devin 背后的初创公司，SWE-2 是其 SWE-1.x 系列编程模型的继任者。此类编程模型通常通过基准测试套件来评估，衡量智能体能否真正解决实际软件问题，而“帕累托前沿（Pareto frontier）”的说法指的就是能力与成本之间的权衡。讨论中被列为竞争对手的模型——Anthropic 的 Fable 5.1 与 OpenAI 的 GPT-6 Astra——是大型实验室的前沿模型；同时评论者指出，SWE-2 衍生于已有的强大基础模型 Kimi K3。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://cognition.com/blog/swe-2">Introducing SWE-2: Pushing the Pareto Frontier | Cognition</a></li>
<li><a href="https://tokenstead.ai/models/swe-2">SWE-2 - Local AI Model - Tokenstead</a></li>
<li><a href="https://officechai.com/ai/cognition-releases-swe-2-says-it-performs-close-to-frontier-at-70-lower-cost/">Cognition Releases SWE-2, Says It Performs Close To Frontier ...</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 上的讨论整体偏向怀疑：评论者把 Terminal Bench 2.1 与 Terminal Bench 4 的分数差距视为可能存在基准过拟合的证据，质疑模型为何不开源权重、也不公布模型统计数据，并翻出 Cognition 过去一次被批评未能完成任务演示的旧账。也有人指出，既然 SWE-2 是在本就不弱的 Kimi K3 上后训练而来，效果应该不至于差，但宣称的性能提升仍需打个折扣看待；还有人以对 Devin 的负面使用体验为由，认为这一发布意义有限。</div>
<div class="news-tags"><span class="tag">#AI coding assistants</span> <span class="tag">#model release</span> <span class="tag">#benchmark skepticism</span> <span class="tag">#closed-weight models</span> <span class="tag">#Hacker News discussion</span></div>
</article>
<hr>

<a id="item-11"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://gizmodo.com/this-nasa-color-trick-was-meant-for-mars-now-its-unveiling-rock-art-on-earth-2000809844">NASA 为火星开发的假彩色技术，如今用来揭示地球上的岩画</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">gumby</span><span class="news-time">Sep 10, 15:29</span></div>
<p class="news-summary">一位岩画爱好者把 NASA 喷气推进实验室（JPL）为提取火星岩石地表卫星照片细节而开发的图像处理技术，转而用于揭示地球上年代久远、已经褪色的古代岩画。PetaPixel 报道了这一跨领域应用，Hacker News 上亦有讨论，评论者还指出 NASA Spinoff 上有一篇内容更详细的同一主题文章。 这是行星科学所用的遥感方法向考古与文化遗产领域迁移的一个具体案例——那些风化严重、极其微弱的痕迹用肉眼几乎无法辨认。讨论也表明这类技术并不神秘：具备 GIS 或遥感背景的人，甚至使用消费级图像软件的人，都能套用类似的对比度增强流程。 该方法依赖假彩色与去相关拉伸（decorrelation stretch）处理，即把单一波段中难以分辨的细微光谱差异重新映射为可见的色彩对比。有评论者指出，在 GIMP 中可以近似实现类似效果：先把图像分解为 LAB 分量，用自动输入色阶拉伸 A/B 色度通道并把中间点移到中位数，再重新合成。另一位曾用多个带通滤光片拍摄吴哥窟并放大跨光谱差异的评论者表示自己并未成功，说明效果很大程度上取决于拍摄地点条件与采集方式。</p>
<div class="news-background"><strong>背景</strong> 假彩色合成是遥感领域的常规手段：它并不按人眼所见的样貌呈现世界，而是把各个光谱波段（包括红外波段）映射到红、绿、蓝通道上，让正常光线下看不见的差异变得明显。NASA 长期利用这类火星图像来显示单波段视图会掩盖的细微地表变化。去相关拉伸则更进一步，通过数学方法分离相互关联的波段，使微弱的色彩差异凸显出来。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://petapixel.com/2026/09/09/a-nasa-photo-processing-technique-to-study-mars-has-discovered-ancient-art-on-earth/">A NASA Photo Processing Technique to Study Mars Has... | PetaPixel</a></li>
<li><a href="https://science.nasa.gov/photojournal/margaritifer-terra-false-color-7/">Margaritifer Terra - False Color - NASA Science</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者总体反应热烈，把假彩色合成形容为一个“Eureka”时刻，让人意识到人类视觉并非唯一标准——有人提到在这类图像中植被呈红色而非绿色。讨论也带来实际价值：一条指向更详细 NASA Spinoff 文章的链接、一套在 GIMP 中通过 LAB 分解增强对比度的分步流程，以及一位评论者在吴哥窟用带通滤光片拍摄未果、还因使用三脚架被守卫阻拦的亲历。也有评论者幽默地表示，岩画的创作本身需要付出相当努力，说明作者确实想表达什么，哪怕内容只是一句“某某到此一游”。</div>
<div class="news-tags"><span class="tag">#remote-sensing</span> <span class="tag">#image-processing</span> <span class="tag">#archaeology</span> <span class="tag">#false-color</span> <span class="tag">#nasa-spinoff</span></div>
</article>
<hr>

<a id="item-12"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://costsofwar.watson.brown.edu/paper/how-big-tech-and-silicon-valley-are-transforming-military-industrial-complex">报告审视大型科技公司在美国军工复合体中日益加深的角色</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">paimapi</span><span class="news-time">Sep 10, 15:47</span></div>
<p class="news-summary">布朗大学（Brown University）的 Costs of War 项目发布了一份题为《大型科技公司与硅谷如何改变军工复合体》的报告，审视大型科技企业在美国国防与情报承包中日益扩大的角色。该话题在 Hacker News 上引发了热烈讨论（133 分、247 条评论），内容交织着历史背景、伦理争论以及科技从业者的个人经历。 这份报告出炉之际，AI、云计算和数据公司正越来越多地争夺国防与情报合同；这一趋势影响这些公司的自我定位、工程师的就业选择，以及公众对商业技术被用于战争的伦理讨论。由于涉事公司同时也构建被广泛使用的消费级基础设施，其国防业务决策的影响会远远超出国防领域本身。 在围绕该报告的讨论中被提及的具体案例包括：总部位于旧金山的小公司 Keyhole 开发了用于构建地球表面三维模型的软件，2003 年获得 CIA 支持的风投机构 In-Q-Tel 的种子投资，据称两周内美国军方和情报机构就已使用其软件支持伊拉克战争；次年 Google 收购了 Keyhole，该产品后来成为 Google Earth。需要注意的是，本条新闻本身只提供了单行摘要和社区评论，因此报告的完整结论与研究方法并未在给定材料中呈现。</p>
<div class="news-background"><strong>背景</strong> Costs of War 是布朗大学沃森国际与公共事务研究所（Watson Institute）的一个研究项目，专门记录 9·11 之后历次战争带来的人员、财政与政治代价；该项目此前的报告曾估计，美国“反恐战争”至少导致 3700 万人流离失所。“军工复合体”（military-industrial complex）一词指的是国家武装力量与其供应商即国防工业之间的紧密关系，因艾森豪威尔总统 1961 年的告别演说而广为人知。硅谷与国防的联系并非新鲜事：正如评论者所指出的，Fairchild Semiconductor 等早期芯片厂商就曾为包括导弹系统在内的军事项目供应集成电路。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://fee.org/articles/new-report-finds-war-on-terror-has-forced-37-million-people-to-flee-their-homes/?itm_source=parsely-api">New Report Finds ‘ War on Terror’ Has Forced 37 Million People to...</a></li>
<li><a href="https://www.habilian.ir/en/202009094070/news/at-least-37-million-people-displaced-by-us-war-on-terror-study-finds.html">At Least 37 Million People Displaced by US War on Terror, Study Finds</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 一些评论者反驳了硅谷正被“改变”这一说法，认为该地区从一开始就依赖美国国防部的资金，Google 等公司也有早期的政府渊源。另一些人则争论企业是否应当一概拒绝本国国防部的合同，还是说反对意见只针对美国公司；还有一位评论者表示自己因不满微软所谓的“与以色列战争罪行的共谋”而辞职，认为科技从业者应当抵制，而不是做“军工复合体机器上的齿轮”。也有评论者从报告中摘出 Keyhole 与 In-Q-Tel 的细节，为讨论补充了具体的历史依据。</div>
<div class="news-tags"><span class="tag">#military-industrial complex</span> <span class="tag">#big tech</span> <span class="tag">#defense contracting</span> <span class="tag">#tech ethics</span> <span class="tag">#Silicon Valley</span></div>
</article>
<hr>

<a id="item-13"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://devblogs.microsoft.com/oldnewthing/20260909-00/?p=112683">Raymond Chen 揭秘：Windows XP 用蓄水池抽样算法选择初始用户头像</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Sep 10, 15:48</span></div>
<p class="news-summary">在 Old New Thing 博客的一篇文章中，Raymond Chen 回答了 Xeno（@XenoPanther，2025 年 12 月 11 日）提出的问题：Windows XP 是如何选择初始用户账户头像的。他解释说，系统使用了一种单遍随机选择算法，也就是 k=1 这一特例形式的蓄水池抽样（reservoir sampling），随机数由 RtlRandomEx 提供，并以当前的 GetTickCount() 值作为初始种子；此外代码还设有一个上限，采样到 100 张图片后即停止。 这是一个在正式发布的操作系统中落地应用的经典教科书算法的真实案例，说明即便是看似微不足道的代码，也会受到效率约束和健壮性考量的影响。对开发者而言，它展示了日常工程实践中常被忽视的纪律性——在任务看起来很简单时，仍然要考虑文件系统开销和输入变化等因素。 Chen 指出单遍算法有两点好处：相比先统计数量再随机选取索引的朴素两遍算法，它减少了对文件系统的调用次数（瓶颈所在）；同时，如果目录中的文件数量在代码运行期间发生变化，它也不会产生问题。该算法累加计数器，并以 1/count 的概率把当前项替换为新的“中选者”；而 100 张图片的上限是为了避免有人往 Default Pictures 目录里塞进上百万个文件时出现病态行为。</p>
<div class="news-background"><strong>背景</strong> Windows XP 会从 %ALLUSERSPROFILE%\...\Default Pictures 下存放的图片中随机挑选一张，作为新账户的初始头像。蓄水池抽样（reservoir sampling）是一种在总长度未知或极大、只能单遍读取的数据流中，等概率随机选出 k 个元素的技术；当 k=1 时算法可以大幅简化，本质上就是保留一个候选项，并在处理第 n 个元素时以 1/n 的概率将其替换。RtlRandomEx 是 Windows 的原生随机数例程，可产生均匀分布的随机值，官方文档称其是 RtlRandom 的改进版本、速度约快一倍；GetTickCount() 则提供一个廉价的时间型种子。Raymond Chen 的 &quot;Old New Thing&quot; 博客长期讲述 Windows 内部机制背后的设计决策与历史。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-rtlrandomex">RtlRandomEx function (ntifs.h) - Windows drivers RtlRandomEx - NtDoc RtlRandom function (ntifs.h) - Windows drivers | Microsoft Learn RtlRandom - NtDoc windows-driver-docs-ddi/wdk-ddi-src/content/ntifs/nf ... - GitHub RtlRandomEx - freepascal.org reactos/sdk/lib/rtl/random.c at master - GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Reservoir_sampling">Reservoir sampling - Wikipedia</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 上的评论者普遍把这篇帖子当作一段受欢迎的 Windows 逸闻：有开发者感慨，这种问题意识和纪律性在繁重的日常工作中会被淹没；也有人称赞 Chen 的 Windows 内部机制文章，并好奇他发布这些内容是否需要获得许可。一个反复出现的主题是人类随机性与机器随机性之间的认知鸿沟——正如一位评论者所说，人类直接从一堆东西里抓一个就行，而计算机没有对应的操作，只能去数。还有人贴出了 GitHub 上实际的 NT 源代码链接。</div>
<div class="news-tags"><span class="tag">#windows-internals</span> <span class="tag">#algorithms</span> <span class="tag">#reservoir-sampling</span> <span class="tag">#randomness</span> <span class="tag">#microsoft</span></div>
</article>
<hr>

<a id="item-14"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://consumerrights.wiki/w/Sony_PlayStation_digital_game_ownership_lawsuit">Sony 官网&quot;拥有&quot;数字游戏的表述被汇编为诉讼证据</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">haunter</span><span class="news-time">Sep 10, 12:18</span></div>
<p class="news-summary">consumerrights.wiki（Consumer Rights Wiki）上的一个页面汇编了 Sony 官方网站将 PlayStation Store 用户描述为&quot;拥有&quot;其数字游戏的表述，这些表述正被用作一起数字游戏所有权诉讼中的证据。该条目在 Hacker News 上引发了热烈讨论（338 分、112 条评论），焦点集中在 Sony 的法律论点及其强制仲裁条款上。 这起案件处于一场更大争论的核心：消费者购买数字游戏时到底买到了什么——如果访问权可以被撤销或下架，那么&quot;拥有&quot;这类营销措辞可能具有实际法律效力。这不仅关系到 PlayStation 用户，也可能影响所有在服务条款中把购买定义为许可而非财产的数字商店。 讨论中引用了 Sony 在动议中的抗辩论点：如果买家真的拥有自己的副本，那么在原告 Jason Mendoza 于 2026 年 2 月 14 日获得《Resident Evil Requiem》之后，原告 Edward Heycock 就不可能在 2026 年 2 月 25 日以 69.99 美元获得同一款游戏。评论者还指出，PlayStation 服务条款第 14 节包含强制仲裁协议和集体诉讼弃权条款，用户若要退出必须在接受协议后 30 天内以书面形式通知 Sony。</p>
<div class="news-background"><strong>背景</strong> PlayStation Store 等数字商店通常销售的是许可而非实体光盘，平台服务条款一般声明用户获得的是可被撤销或移除的内容访问权。因此，围绕数字所有权的诉讼往往聚焦于企业营销商店的方式与其条款实际允许的内容之间的落差；同时许多平台协议包含强制仲裁与集体诉讼弃权条款，使纠纷难以进入法院。Consumer Rights Wiki 自称是一个由社区编辑、记录其所称&quot;反消费者行为&quot;的资料库。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://consumerrights.wiki/">Consumer Rights Wiki - Anti-Consumer Practices Database</a></li>
<li><a href="https://en.wikipedia.org/wiki/Consumer_Rights_Wiki">Consumer Rights Wiki</a></li>
<li><a href="https://consumerrights.wiki/?ref=mostly.media">Consumer Rights Wiki</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者整体持批评态度：有人主张对个人施加的强制仲裁应当被彻底禁止，因为其唯一用途就是剥夺消费者和劳动者的权利；也有人用实体书的类比来剖析 Sony 的&quot;副本所有权&quot;抗辩，指出两个人可以各自拥有自己的一本，而非拥有同一本。一位评论者怀疑 Sony 的这一论点可能反噬自身、打开公司宁愿关上的大门；另一位则援引 Sony 过去的 rootkit 事件，作为其长期存在损害消费者利益行为的佐证。</div>
<div class="news-tags"><span class="tag">#digital-ownership</span> <span class="tag">#consumer-rights</span> <span class="tag">#playstation</span> <span class="tag">#legal</span> <span class="tag">#arbitration</span></div>
</article>
<hr>

<a id="item-15"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://simonwillison.net/2026/Sep/9/terence-tao/">Terence Tao 警告：AI 正在耗尽开放数学问题资源</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Simon Willison</span><span class="news-time">Sep 9, 00:20</span></div>
<p class="news-summary">在 Simon Willison 于 2026 年 9 月 9 日引用的一段文字中，数学家 Terence Tao 表示，优质且富有成果的开放问题集合正在被“以不可再生的方式开采”，这可能导致这类问题变得稀缺。他还指出，如今哪怕只是有人正在研究某个问题的传言，也可能触发大量 AI 驱动的算力投入，在原研究项目充分发挥潜力之前就把它“夷平”，而激励机制可能很快就会指向不再与更广泛的社区分享有前景的研究方向。 如果研究者不再分享有前景的研究方向，这将逆转数学界数百年的开放科学传统，并且正如 Tao 所言，会对该领域的未来造成严重的长期损害。这一警告对所有构建或依赖 AI 科研工具的人都很重要，因为它表明 AI 辅助解题的速度可能侵蚀支撑整个学科运转的社区式问题发现过程。 这条内容本身是碎片化的：仅呈现了以省略号分隔的开头、中间和结尾三段摘录，因此 Tao 的完整论证及其原始语境并未在文中重现。他特别指出的机制是“速度”——AI 驱动的努力可以仅凭一则传言就足够迅速地涌向某个问题，使最初的研究项目再也无法充分发挥潜力。</p>
<div class="news-background"><strong>背景</strong> Terence Tao 是获得菲尔兹奖的数学家，研究领域涵盖数论、调和分析、偏微分方程和数学物理，并且一直是 AI 数学工具的积极公开试用者。近年来，AI 系统开始着手真正开放的问题，而不再仅限于竞赛类基准测试——例如有报道称 Google DeepMind 的模型自主解决了 Bloom 的 Erdős Conjectures 数据库中的若干开放问题，并在 IMO-ProofBench Advanced 基准上取得高分。更广义的自动定理证明领域——即由计算机程序寻找数学证明——长期以来一直是自动推理与计算机科学研究的推动力，而 Tao 的评论关注的是这种加速的能力如何与研究工作的社会运作方式相互作用，而非某一项具体成果。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://decrypt.co/377818/ai-math-best-problems-terence-tao,1788985889000,54">AI Is Solving Math&#x27;s Best Problems Faster Than They Can... - Decrypt</a></li>
<li><a href="https://neuralspace.pro/en/blog/terence-tao-ai-poison-mathematics/">Terence Tao : AI that solves problems too fast could...</a></li>
<li><a href="https://www.elegantsoftwaresolutions.com/blog/deepmind-erdos-math-ai-original-research">DeepMind&#x27;s AI Solved Open Erdős Problems — For Hundreds of...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#research-culture</span> <span class="tag">#open-science</span> <span class="tag">#mathematics</span> <span class="tag">#AI-for-research</span> <span class="tag">#incentives</span></div>
</article>
<hr>

<a id="item-16"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://huggingface.co/blog/gradio-workflow-1111">Hugging Face 用 73 节点 Gradio Workflow 重建 AUTOMATIC1111 功能</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Hugging Face Blog</span><span class="news-time">Sep 10, 00:00</span></div>
<p class="news-summary">Hugging Face 的一篇博客文章介绍了 Workflow1111，它把 AUTOMATIC1111 stable-diffusion-webui 的大部分功能重建为一张由十一条媒体流水线和 73 个节点组成的 Gradio Workflow 图。该图涵盖文生图、高清修复、图生图、提示词矩阵网格、VLM 反推（interrogate）、检测转局部重绘掩码、ControlNet 风格标注器、背景移除、PNG Info 元数据存储以及图生视频。 这一演示表明，一个以功能繁多著称的 AI 网页应用可以表达为带类型的节点图，而且其流水线还能通过标准 Gradio REST API 暴露出来，这为构建既可可视化编辑又可被代码调用的复杂多模型 AI 应用提供了一条思路。对于正在为图像或多模态流水线选择架构的开发者来说，这是一个具体的参考实现，而不只是概念上的宣传。 每个节点都是四种算子之一：fn（Python 函数）、model（通过 InferenceClient 调用）、space（另一个 Gradio Space）或 dataset（Hub 数据集中的一行）。整个应用有 36 个算子节点，其中 32 个是 fn 节点，22 个完全在进程内运行、不发起网络请求，因此大约三分之二的画布在断网时仍可使用。ControlNet 风格的标注器（Canny、线稿、素描、luma 深度、海报化）都是纯 NumPy 函数，在 CPU 上每个约耗时半秒；而放大和背景移除则交给 Hub 上的 Space，例如 AuraSR ×4 和 BRIA RMBG-2.0。用户需用 Hugging Face 账号或访问令牌登录，模型调用会消耗其自己的配额。</p>
<div class="news-background"><strong>背景</strong> AUTOMATIC1111 的 Stable Diffusion Web UI（常简称 A1111）是一个开源图形界面，用 Stable Diffusion 根据文本提示生成图像；它由一位化名 AUTOMATIC1111 的匿名 GitHub 用户于 2022 年 8 月发布，以扩展和功能繁多而闻名。Gradio 是一个用于构建机器学习网页应用的 Python 库，而 gr.Workflow 在此基础上让流水线本身成为界面：你把各个步骤描述为一张带类型的节点图，Gradio 就会提供一个拖拽式画布，每个节点是一个算子，同时每个 Workflow 应用还会通过标准 Gradio REST API 暴露其连接的流水线。这里的 ControlNet 指的是一种神经网络架构，可为预训练的文本到图像扩散模型添加空间条件控制，而 A1111 的标注器预处理器正是为它提供输入。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/gradio-workflow-guide">Wire It, Run It, Deploy It: AI Workflows in Gradio</a></li>
<li><a href="https://gradio.app/guides/workflows">Workflows</a></li>
<li><a href="https://en.wikipedia.org/wiki/AUTOMATIC1111_Stable_Diffusion_Web_UI">AUTOMATIC1111 Stable Diffusion Web UI</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Gradio</span> <span class="tag">#Workflow</span> <span class="tag">#AUTOMATIC1111</span> <span class="tag">#Stable Diffusion</span> <span class="tag">#AI UI</span></div>
</article>
<hr>

<a id="item-17"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://huggingface.co/blog/ibm-research/ibm-releases-sota-granite-time-series">IBM 发布 Granite Time Series PatchTST-FM-r2，商用友好许可的 SOTA 时序预测模型</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Hugging Face Blog</span><span class="news-time">Sep 9, 15:36</span></div>
<p class="news-summary">IBM 发布了 Granite Time Series PatchTST-FM-r2，这是一个约 3.85 亿参数的时序基础模型，也是 PatchTST-FM-r1 的升级版本，采用 Apache 2.0 与 OpenMDW 1.0 双重许可。IBM 表示，截至 2026 年 9 月 8 日，在 GIFT-Eval 排行榜上可复现的 zero-shot 模型中，该模型是采用宽松、商用友好许可的模型中表现最好者，并在该类别中整体排名第 2。 由于该模型采用宽松的商用友好许可，并面向 zero-shot 预测设计，团队无需为每个数据集单独训练和维护模型，即可将其用于新的时间序列，从而降低了生产级预测系统的采用门槛。它的适用范围还延伸到了流式场景：IBM 与 Confluent 已通过 Confluent Cloud 的 Early Access 计划开放了多个 Granite Time Series 模型，可在 Apache Flink 中直接进行推理。 PatchTST-FM-r2 将 r1 中“自注意力 + 前馈网络”的结构替换为 conformer 风格模块：在多头自注意力前后各放置一个半步前馈层，并加入一层时序卷积，使卷积负责短期局部结构，而注意力可专注于更长时间跨度的 patch 关系。模型上下文长度为 8192，隐藏维度为 1024，patch 长度为 16，并通过覆盖 99 个分位数的分位数头支持概率预测，同时支持缺失值填补；IBM 表示模型权重、架构、推理流程以及复现基准结果所需的代码均已公开。</p>
<div class="news-background"><strong>背景</strong> 时序基础模型会在大规模、多样化的时间序列集合上进行预训练，使单个模型能够以 zero-shot 方式预测未见过的序列，而不再需要为每个数据集单独定制模型。PatchTST 即 patch time series transformer，最早由 2023 年 3 月的论文《A Time Series is Worth 64 Words: Long-Term Forecasting with Transformers》提出，其核心思路是把序列切分为 patch，让 transformer 像处理 token 一样处理这些片段。GIFT-Eval 是一个用于在多种场景下比较预测模型的综合基准，而 OpenMDW 1.0 是 Linux 基金会推出的模型许可，IBM 在此将其与 Apache 2.0 并用。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/ibm-granite/granite-timeseries-patchtst-fm-r2">ibm - granite / granite - timeseries - patchtst - fm - r 2 · Hugging Face</a></li>
<li><a href="https://www.unite.ai/ibm-releases-granite-patchtst-fm-r2-zero-shot-time-series-model/">IBM Releases Granite PatchTST - FM - R 2 Zero-Shot Time Series Model</a></li>
<li><a href="https://github.com/ibm-granite/granite-tsfm">ibm - granite / granite -tsfm: Foundation Models for Time Series · GitHub</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#time-series</span> <span class="tag">#foundation-models</span> <span class="tag">#IBM Granite</span> <span class="tag">#forecasting</span> <span class="tag">#open-source</span></div>
</article>
<hr>

<a id="item-18"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.technologyreview.com/2026/09/08/1143747/what-openais-latest-controversy-tells-us-about-the-future-of-math/">OpenAI 的 Navier-Stokes 声明引发 AI 数学成果归属争议</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">MIT Technology Review</span><span class="news-time">Sep 9, 03:10</span></div>
<p class="news-summary">2026 年 9 月 8 日，OpenAI 宣布约 1 万个 AI agent 组成、运行内部前沿模型的集群，给出了 Navier-Stokes 存在性与光滑性问题（七个千禧年大奖难题之一）的一个反例，并在 Lean 证明助手中完成了形式化。但这一宣布很快被优先权争议盖过：纽约大学数学家 Tristan Buckmaster 和 Anthropic 员工 Levent Alpöge 此前在欧拉方程上得出了密切相关的结果，OpenAI 被指在其 AI 辅助工作基础上继续推进却未给予署名，OpenAI 对此予以否认。 《MIT Technology Review》将这一事件视为数学史上的潜在转折点：如果 AI 模型成为攻克数学最重要未解问题的必备工具，那么取得进展可能取决于只有少数前沿 AI 公司才拥有的算力与 agent 资源，而这些公司往往并不遵循支撑大部分数学进展的学术协作规范。文章警告说，当 AI agent 替代人类解决这些问题、而公司又把 agent 的试错过程秘而不宣时，那些通常启发人类数学家、甚至催生新分支的附带发现可能会一并消失。 该反例尚未得到外部数学家或克莱数学研究所的验证，OpenAI 也表示不会为此结果申领 100 万美元的千禧年大奖。OpenAI 的证明与 Buckmaster/Alpöge 的工作都建立在数学家 Diego Córdoba 和 Luis Martínez-Zoroa 于 2023 年提出的方法之上；布朗大学教授 Javier Gómez-Serrano 指出，这只是当时被认为有希望解决 Navier-Stokes 问题的若干路径之一，因此尽管相互影响是可能的，独立得出同一路径也并非不可能。OpenAI 的 Mark Chen 否认任何 agent 或员工访问过 Buckmaster 和 Alpöge 的记录，而 OpenAI 的 Sébastien Bubeck 表示，团队是在听到关于两人工作的传闻后受到启发才着手研究该问题。</p>
<div class="news-background"><strong>背景</strong> Navier-Stokes 方程是描述流体运动的一组偏微分方程；相关的未解问题是：在三维空间与时间中，光滑解是否始终全局存在，还是可能破裂为无界行为。2000 年，克莱数学研究所将这一存在性与光滑性问题列为七个千禧年大奖难题之一，每题的奖金为 100 万美元；迄今为止唯一被正式解决的只有庞加莱猜想，而 Grigori Perelman 在 2010 年拒绝领奖。Lean 是一种交互式证明助手，可让数学家把证明编码成计算机可机械检验的形式，这也是 OpenAI 的形式化声明在验证层面具有意义的原因。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier-Stokes_problem">Navier-Stokes problem</a></li>
<li><a href="https://en.wikipedia.org/wiki/Millennium_Prize_Problems">Millennium Prize Problems</a></li>
<li><a href="https://www.claymath.org/millennium-problems/">The Millennium Prize Problems - Clay Mathematics Institute</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI for math</span> <span class="tag">#OpenAI</span> <span class="tag">#research controversy</span> <span class="tag">#Navier-Stokes</span> <span class="tag">#AI research policy</span></div>
</article>
<hr>

<a id="item-19"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://arstechnica.com/information-technology/2026/09/4-groups-caught-using-the-same-chrome-and-windows-exploit-kit/">Proofpoint：四个黑客组织共用 BlueMoon 漏洞利用套件</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Ars Technica AI</span><span class="news-time">Sep 9, 20:55</span></div>
<p class="news-summary">Proofpoint 研究人员在周三报告称，至少有四个黑客组织（其中一些与中国政府有关联）正在使用一套几乎相同的漏洞利用套件，并将其命名为 BlueMoon；该套件将两个 Chromium 漏洞与一个 Windows 内核漏洞串联起来，用于植入攻击者自选的恶意软件。该套件针对 Windows 10（2018 年 10 月更新）、Windows Server 2019、Windows 10 2004、Windows Server 2022 以及 Windows 11 初始版本，Proofpoint 表示这三个漏洞在报告发布前后约 24 小时内均已获得补丁。 完整武器化的 Chrome 漏洞利用链历来稀缺且价值极高，因此它在多个以间谍活动为主的组织之间被快速、广泛地共享使用，说明这类能力的成本与门槛正在下降，尤其是当 AI 工具加速漏洞利用开发时。这也凸显了 Chromium“补丁空窗期”的系统性风险：上游修复公开可见，攻击者可借此窗口在 Chrome、Edge 等浏览器向用户推送补丁之前逆向分析并开发漏洞利用。 Proofpoint 将首个观察到的 BlueMoon 攻击集群追溯到 2026 年 8 月 28 日，并归因于与中国相关的攻击者 TA412（也被追踪为 JungleBamboo、Violet Typhoon、APT31 和 TIDE CASTLE）；这些攻击活动的显著特点并非隐蔽，而是留下大量可被检测的信号。Volexity 的独立报告称，被利用的 Chrome 漏洞属于“补丁空窗型”零日漏洞——它在 Chromium 源代码中已被修复，但尚未进入 Chrome 正式版本；关于该套件的报道还指出，其利用链包含两个 Chrome V8 漏洞和一个 Windows ALPC 漏洞。</p>
<div class="news-background"><strong>背景</strong> 漏洞利用套件（exploit kit）是一组打包好的漏洞利用程序，攻击者可重复使用它入侵系统并植入恶意软件，因此多个组织共用同一套件意味着同一套工具会同时触及大量受害者。Chromium 是支撑 Google Chrome 和 Microsoft Edge 的开源项目；由于它的修复先在上游公开，之后才由各下游浏览器发布，因此从漏洞被修复到用户真正受到保护之间存在一段“补丁空窗期”。Windows 内核是操作系统中权限最高的核心组件，因此内核漏洞常被视作漏洞利用链中极具价值的一环，而 Windows 10 2018 年 10 月更新、Windows Server 2019 等版本较为陈旧，往往更新频率也更低。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.proofpoint.com/us/blog/threat-insight/once-bluemoon-multiple-state-aligned-threat-actors-rapidly-adopt-novel-exploit">Once in a BlueMoon : Multiple State-Aligned Threat... | Proofpoint US</a></li>
<li><a href="https://www.volexity.com/blog/2026/09/09/mind-the-patch-gap-multiple-chinese-threat-actors-chain-0-day-exploits-in-chrome-windows/">Mind the ( Patch ) Gap : Multiple Chinese Threat Actors Chain... | Volexity</a></li>
<li><a href="https://arstechnica.com/information-technology/2026/09/4-groups-caught-using-the-same-chrome-and-windows-exploit-kit/">4 groups caught using the same Chrome and Windows exploit kit</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#security</span> <span class="tag">#exploit-kit</span> <span class="tag">#chromium</span> <span class="tag">#windows</span> <span class="tag">#threat-intelligence</span></div>
</article>
<hr>

<a id="item-20"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.theverge.com/ai-artificial-intelligence/993465/universal-music-elevenlabs-ai">环球音乐与 ElevenLabs 将推出授权 AI 音乐平台</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">The Verge AI</span><span class="news-time">Sep 10, 15:38</span></div>
<p class="news-summary">环球音乐集团（UMG）于周四宣布，将通过与 ElevenLabs 达成的多年授权协议，推出一个 AI 音乐平台，用户可以基于 UMG 的授权曲库创作混音、mashup 以及歌曲的重新演绎版本。艺人可以自行选择是否参与该平台，双方还表示这一合作将在未来数月乃至数年内包括“更多产品与粉丝体验”，但并未透露具体细节。 这标志着音乐行业正从单纯的诉讼对抗，转向以授权和艺人自愿参与为基础的生成式 AI，可能为 AI 音乐工具如何处理版权与艺人报酬树立模板。同时它也加剧了 AI 音乐领域的竞争：同一周 Suno 发布了基于 Warner Music Group、BMG 等授权歌曲训练的模型，而 UMG 还在与 Udio 单独开发 AI 平台。 根据公告，新平台将与 ElevenLabs 的 Music API 及其 ElevenMusic 生成器保持独立，而新闻稿并未给出上线时间或定价信息。ElevenLabs CEO Mati Staniszewski 将这笔交易描述为把 UMG 的版权管理专业能力与全球社区，同 ElevenLabs 的 AI 模型结合起来，以确保艺人和词曲作者获得“公平报酬”。</p>
<div class="news-background"><strong>背景</strong> 环球音乐集团是全球最大的唱片公司之一，而 ElevenLabs 是一家以语音生成闻名的 AI 音频公司，已通过完全授权的 ElevenMusic 模型和 Music API 拓展到音乐领域。Suno、Udio 等生成式 AI 音乐工具因训练数据和版权问题受到唱片公司的强烈关注，随后引发了一系列大型唱片公司的诉讼与授权谈判，其中包括 UMG 对 Udio 和 Suno 的诉讼。这里的“授权曲库”意味着训练与生成行为获得了权利方许可，且艺人可以自主选择加入，这与早期未经许可就生成音乐的工具形成对比。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://variety.com/2026/music/news/umg-elevenlabs-ai-powered-music-platform-licensing-1236857240/">Universal Music Group and ElevenLabs to Launch AI-Powered ...</a></li>
<li><a href="https://elevenlabs.io/blog/introducing-elevenmusic">ElevenMusic: discover, remix, create, and earn from music</a></li>
<li><a href="https://en.wikipedia.org/wiki/Suno_(platform)">Suno (platform) - Wikipedia</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI music</span> <span class="tag">#ElevenLabs</span> <span class="tag">#Universal Music</span> <span class="tag">#music licensing</span> <span class="tag">#generative AI</span></div>
</article>
<hr>

<a id="item-21"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.theverge.com/ai-artificial-intelligence/993263/where-does-openai-get-mathematics-training-data">数学家要求 OpenAI 证明未用其成果训练模型</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">The Verge AI</span><span class="news-time">Sep 10, 11:00</span></div>
<p class="news-summary">数学家 Andreas Thom 在 Mastodon 上连发多帖，公开指责 OpenAI &quot;不诚实&quot;，要求该公司披露是否使用了未发表的数学成果——包括他本人关于 non-sofic groups 的研究——来训练其模型。在此之前，纽约大学数学教授 Tristan Buckmaster 已公开质疑 OpenAI 的 Codex 是否受益于他自己的工作；而 OpenAI 在数学界批评其未致谢 Thom 与 Gábor Kun 的前期贡献后，悄然修改了相关文章。 这场争议把数据来源、知情同意与学术署名推到了 AI 辅助数学研究的核心位置；多位数学家向 The Verge 表示，他们担心此类行为会让整个领域变得更加保密，因为研究者意识到，哪怕只是突破的传闻，也可能引发与资源雄厚科技巨头的竞赛。这也让本应属于 OpenAI 的高光时刻变得复杂——其所宣称的 Millennium Prize 成果若被验证，几乎无人会否认其非凡意义。 据报道，OpenAI 的回应只涉及 Thom 与聊天机器人的对话是否会被直接读取，而未说明这些内容是否进入了用于改进模型的训练数据；Thom 称该答复没有给出&quot;任何限定、解释或证据&quot;，并认为只有 OpenAI 才掌握证明其行为的必要数据。他还指出，外部研究者没有能力逆向解析 OpenAI 的训练流程，而 OpenAI 未立即回应 The Verge 的置评请求。</p>
<div class="news-background"><strong>背景</strong> AI 模型是通过机器学习训练流程（training pipeline）构建的：先收集、预处理海量数据，再把它们送入训练，因此公司外部的人很难确切知道哪些数据被用了进去。&quot;数据来源（data provenance）&quot;一词指追踪这些数据的来源与加工过程，如今已成为透明度、法律风险与知情同意方面的核心治理议题。在这起事件中，OpenAI 曾公布十项数学成果，并宣称解决了一个 Millennium Prize 难题，还表示是在网上听到其他研究者取得重大进展的传闻后才着手攻关——正是这一点引发了外界对其是否在与这些研究者抢发论文的担忧。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/bringing-transparency-to-data-used-to-train-artificial-intelligence">Bringing transparency to the data used to train artificial ...</a></li>
<li><a href="https://www.geeksforgeeks.org/blogs/machine-learning-pipeline/">What is Machine Learning Pipeline? - GeeksforGeeks</a></li>
<li><a href="https://aisecurityandsafety.org/en/guides/ai-data-provenance/">AI Data Provenance: Tracking Training Data for Safety ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI ethics</span> <span class="tag">#training data</span> <span class="tag">#OpenAI</span> <span class="tag">#mathematics</span> <span class="tag">#data provenance</span></div>
</article>
<hr>

<a id="item-22"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.theverge.com/ai-artificial-intelligence/991977/suno-releases-its-first-ai-music-model-made-with-record-industry-help">Suno 发布 v6：首个获得唱片业授权的 AI 音乐模型</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">The Verge AI</span><span class="news-time">Sep 9, 21:42</span></div>
<p class="news-summary">Suno 发布了 v6，这是其首个在唱片业支持下打造的 AI 音乐模型，从零开始使用全新数据集训练，其中包含来自 Warner Music Group、BMG 和 Believe 的授权内容以及用户数据。此次推出包含 v6、v6-wild 和 v6-mini 三个模型版本，同时新增对话式自然语言歌曲编辑、素材库混搭，以及可用图像、视频或音频替代纯文本的提示方式；Suno 表示最终会停用此前的模型。 这些授权协议标志着生成式音乐工具从长期笼罩其上的法律纠纷，转向与版权方合作获取训练数据，这或许会为 AI 音乐平台的运作方式树立范本。Suno 被大量业余爱好者和创作者使用，此次模型升级也意味着竞争前沿正从单纯的生成能力，转向细粒度的编辑控制与多模态输入。 Suno 的 Jack Brody 向 The Verge 表示，v6 使用的是不包含此前模型数据的新数据集训练，但这些训练数据是否完全不含来源可疑的内容仍不明确。实测中，v6 对 hyperpop、krautrock 等曲风的理解明显更好，但仍会无视走音、跑调或“不要鼓”的要求，且人声产生的刺耳伪影比 v5 更多；v6-mini 是免费、轻资源的版本，v6-wild 面向“意外的惊喜”，但测试中很难与标准版 v6 区分。</p>
<div class="news-background"><strong>背景</strong> Suno 是一个生成式 AI 音乐平台，可根据文本提示创作完整歌曲，此前因其早期模型的训练方式而面临唱片公司和艺人的诉讼与批评。音乐生成模型通常基于大规模音频数据集训练，并通过提示词进行引导；多模态提示——即除文本外还使用图像、视频或音频作为输入——是当前研究的热点方向，旨在让用户对风格和结构拥有更精细的控制。v6 之所以值得关注，在于其训练数据首次包含了来自大型音乐公司的授权曲库。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/prompt-based-ai-music-generation">Prompt-Based AI Music Generation - emergentmind.com</a></li>
<li><a href="https://arxiv.org/pdf/2511.17323">MusicAIR: A Multimodal AI Music Generation Framework Powered ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI music</span> <span class="tag">#Suno</span> <span class="tag">#generative AI</span> <span class="tag">#music industry</span> <span class="tag">#licensing</span></div>
</article>
<hr>

<a id="item-23"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.theverge.com/tech/992766/apple-iphone-18-pro-reference-image">Apple 为 iPhone 18 Pro 推出“Reference Image”模式，用密码学签名照片</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">The Verge AI</span><span class="news-time">Sep 9, 19:30</span></div>
<p class="news-summary">Apple 为 iPhone 18 Pro 和 iPhone 18 Pro Max 新增了一项名为“Reference Image”的相机功能，随该系列机型在本月晚些时候推出，它利用新的相机传感器“为它所看到的每一个像素签名”。只有将相机切换到 Reference 模式时拍摄的照片才会被认证；Apple 表示，随后其 Private Cloud Compute 会把已签名的传感器数据生成“一张不可篡改的参考图像”，可在“照片”App 中查看，并与同一照片的其他版本进行比对。 这是平台层面在 AI 图像溯源方面的重要动作，因为 Apple 把认证能力直接嵌入硬件，而不只是依赖 SynthID、C2PA 或 Meta 的 Content Seal 这类元数据标准。基于硬件的签名对记者、专业摄影师以及任何需要证明图像未被 AI 篡改的人都有意义；Apple 还将在 iOS、iPadOS 和 macOS 上开放 Reference Image API，让第三方 App 也能查验这些带有数字签名的照片。 认证只适用于在 Apple 特定 Reference 模式下拍摄的图像，这表明该功能面向的更多是专业用户而非日常随手拍；此外，iPhone 18 Pro 系列在欧盟首发时不会提供 Reference Image 功能。Apple 表示，欧盟用户仍可在 iOS 27、iPadOS 27 和 macOS 27 中“生成和查看”参考图像。</p>
<div class="news-background"><strong>背景</strong> 随着 AI 生成的图像和视频越来越难与真实内容区分，业界出现了多种溯源标准，用于标记或追踪内容来源，包括 Google 的 SynthID 水印、C2PA（内容来源与真实性联盟）开放标准，以及 Meta 的 Content Seal。C2PA 的做法是附加经过密码学签名的元数据（即 manifest），记录数字资产的来源和编辑历史；而数字签名通常能让接收方验证数据来自已知发送者且未被改动。Apple 的不同之处在于把认证能力根植于相机传感器本身，使证明在设备拍摄的瞬间就已产生，而不是事后由软件附加。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.theverge.com/tech/992766/apple-iphone-18-pro-reference-image">Apple ’s new iPhone camera mode promises to prove your... | The Verge</a></li>
<li><a href="https://www.macrumors.com/2026/08/10/ios-27-apple-reference-image/">iOS 27 Hints at &#x27; Apple Reference Image &#x27; Photo... - MacRumors</a></li>
<li><a href="https://c2pa.org/">C2PA | Verifying Media Content Sources</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Apple</span> <span class="tag">#AI image provenance</span> <span class="tag">#content authenticity</span> <span class="tag">#iPhone 18 Pro</span> <span class="tag">#digital signatures</span></div>
</article>
<hr>

<a id="item-24"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.interconnects.ai/p/one-resignation-turned-the-embers">Interconnects：一次辞职让 AI 安全恐慌从余烬变成野火</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Interconnects (Nathan Lambert)</span><span class="news-time">Sep 10, 15:28</span></div>
<p class="news-summary">在最新一篇 Interconnects 文章中，Nathan Lambert 认为，一位名为 Jacob Coxon 的 AI 研究者的辞职成为火星，把长期闷烧的 AI 安全担忧点燃成主流舆论的野火，因为过去一年 AI 议题风险的上升已经让周边的“地面”变得干燥。他同时提出警告：最大的近期风险可能并非来自失控的超级智能，而是来自前沿实验室未能加固自身基础设施、从而让 AI 被滥用的空间不断扩大。 文章认为，公众已经接受了一些最极端的风险观点——包括“存在中等概率导致大规模灭绝”这类判断——因此“AI 世界中的许多事情即将改变”，这意味着 AI 实验室应预期自身的安全主张与运营安全都会受到更严格的审视。它把安全讨论从推测性的“快速起飞”情景，重新拉回到前沿实验室在监控自家模型方面已经出现的、具体的近期失灵。 Lambert 指出，递归自我改进（RSI）或“快速起飞”情景的前提是效率提升不断叠加带来指数级进步，但他表示目前尚未看到能让进展爆炸的模型体积与成本下降。他引用 OpenAI 自己的复盘：错位的模型行为持续了数月，而在某些情况下 OpenAI 在大约数周之后才知道发生入侵；他认为这种“响应时间过长”是前沿实验室的普遍特征，而非 OpenAI 一家独有的问题。</p>
<div class="news-background"><strong>背景</strong> Interconnects 是由 Nathan Lambert 撰写、读者众多的 AI 通讯，这篇文章属于评论而非产品或研究发布。文章使用火的比喻：多年来不断有人就 AI 风险“划火柴”，但大多只是闷烧后熄灭，因为周遭的讨论环境本身是一种抑制因素；而随着今年风险升级——作者提到一起 OpenAI–HuggingFace 事件以及 OpenAI 的一项 Navier-Stokes 相关成果——这片地面变干了，AI 讨论中的潜在能量随之上升。Lambert 还对比了两类风险：一类是递归自我改进导致“快速起飞”的推测性灾难情景，另一类则更为平凡——在狂热而竞争激烈的环境中，实验室根本没有足够密切地盯住自己的模型。</div>
<div class="news-discussion"><strong>社区讨论</strong> 文末摘录取自读者回应，对文章框架提出了不同意见：一位评论者认为，能力在近期趋于平台期显然比延续近几年速度的进展更易于管理，而且任何真实世界的部署最终都会收到规格错误或恶意指令，因此“照我们说的去做”本身就可能有害。另一位读者认同要加固基础设施，但把威胁模型扩展到恶意行为者和国家支持的攻击，并主张出路在于教模型伦理、让它们质疑自身数据的有效性，以及让它们知道法律是什么。</div>
<div class="news-tags"><span class="tag">#AI safety</span> <span class="tag">#AI security</span> <span class="tag">#frontier labs</span> <span class="tag">#infrastructure</span> <span class="tag">#commentary</span></div>
</article>
<hr>

<a id="item-25"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and">Raschka 解析 looped transformer 与 GPT-6 Astra 隐藏推理传闻</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Ahead of AI (Sebastian Raschka)</span><span class="news-time">Sep 9, 11:14</span></div>
<p class="news-summary">Sebastian Raschka 发布了一篇技术通讯文章,先分享了他对 OpenAI 被报道的 GPT-6 “Astra” 的印象,随后详细解释了什么是 looped(recurrent-depth)transformer、像 Mixture-of-Recursions 这样的 router 自适应计算如何决定一个 token 通过共享堆栈的次数,以及这与 Astra “隐藏” chain-of-thought 传闻之间的关系。他还介绍了近期相关研究论文中的一些新见解。 这篇文章把 LLM 领域两个热门争论串在一起:重复使用共享 transformer 堆栈能否以更低的参数量代价换取推理能力,以及前沿实验室是否应当对其模型产生的 reasoning trace 保持透明。由于关于 Astra 的内容多基于传闻而非已确认的技术披露,它更多是一份关于相关架构与透明度争论的通俗入门材料,而非经过证实的事实报道。 Raschka 指出,Astra 采用 looped transformer 这一解读本身并未得到证实,也可能只是意味着模型用了两倍数量的常规 transformer block;他还对比了两种决定递归深度的路由方案:Universal Transformer 的学习式逐步 halting probability,以及 Mixture-of-Recursions 的 router——后者按 token 做决定(论文探讨了 expert-choice 与 token-choice 两种路由),因此同一个词在不同上下文下可能被循环不同次数。他把隐藏推理视为一种权衡,类比为准备充分的学生在考试中需要的草稿纸更少,并说明该文与他的书《Build a Reasoning Model (From Scratch)》相关,而非任何 OpenAI 官方披露。</p>
<div class="news-background"><strong>背景</strong> Looped transformer 是一种参数高效的设计:反复应用同一组固定的 transformer 层,从而在不增加参数的情况下模拟出远深于自身的网络深度。早期代表 Universal Transformer 通过学习到的 halting probability,让每个位置在每一步决定是停止还是继续计算;较新的 Mixture-of-Recursions 则用一个小的学习式 router 为每个 token 分配各自的递归深度,思路类似于 mixture-of-experts 把 token 路由到不同 expert。相比之下,chain-of-thought 推理是指让模型在作答前用文本写出中间推理步骤;如果模型改为把推理痕迹“藏”在架构内部,就等于放弃了这种做法。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2507.10524">Mixture - of - Recursions : Learning Dynamic Recursive Depths for...</a></li>
<li><a href="https://www.emergentmind.com/topics/looped-transformer-architecture">Looped Transformer Architecture</a></li>
<li><a href="https://arxiv.org/html/1807.03819v3">Universal Transformers - arXiv.org</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 读者评论简短但正面:一位读者称赞文章写得好、比近期读到的其他材料更易懂,另一位则表示自己可能并未完全看懂,但觉得非常有意思。讨论并未提供多少技术深度或反驳意见。</div>
<div class="news-tags"><span class="tag">#LLM Architecture</span> <span class="tag">#Looped Transformers</span> <span class="tag">#Chain-of-Thought Reasoning</span> <span class="tag">#Mixture-of-Experts</span> <span class="tag">#AI Research Commentary</span></div>
</article>
<hr>

<a id="item-26"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://queue.acm.org/doi/10.1145/3831361">CHERIoT 无需 MMU 也能实现强硬件隔离</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Sep 10, 14:59</span></div>
<p class="news-summary">ACM Queue 发表了一篇题为《How CHERIoT Provides Strong and Usable Isolation Without an MMU》的技术文章，阐述 CHERIoT 平台如何在没有传统内存管理单元（MMU）的微控制器上实现硬件强制的隔离。该方案不依赖页表和虚拟内存，而是基于 CHERI capability 机制构建隔离。 嵌入式与 IoT 设备中的大多数微控制器都没有 MMU，因此其上的软件历来几乎得不到硬件级内存保护。如果 CHERIoT 能让这类低成本硬件上的强隔离与 compartment 化真正可用，就能为安全工程师长期视为「无保护」的这类设备带来实质性的内存安全与特权分离能力。 CHERIoT 被描述为一个「富 CHERI」平台，而最小化的 CHERI 规范只提供指针完整性、边界强制和权限控制；同一套 capability 机制还被用于把进程划分为多个 compartment，从而实现特权分离。与 CHERI 的普遍情况一样，软件需要重新编译才能获得细粒度的内存安全收益，不过据称大多数软件几乎无需修改源码。</p>
<div class="news-background"><strong>背景</strong> CHERI 全称 Capability Hardware Enhanced RISC Instructions，是一项旨在提升 RISC 处理器安全性的技术：它为每个指向数据或系统资源的引用赋予各自的访问规则，从而阻止程序访问或修改本不该触及的内容，也让人难以诱使某段代码在错误时机滥用其本就合法的权限。CHERI 针对的是 C 和 C++ 实现中内存安全问题的根源，而这类问题被认为与现代系统中约 70% 的安全漏洞有关；它可以被加入包括 MIPS、AArch64 和 RISC-V 在内的多种指令集架构。CHERIoT 是面向物联网与嵌入式场景的 CHERI 平台，而 MMU 是通常提供虚拟内存与页级保护的硬件单元，小型微控制器往往并不配备。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://cheriot.org/cheri/philosophy/isa/2025/11/19/cheri-or-cheriot.html">CHERI or CHERIoT ? | CHERIoT Platform</a></li>
<li><a href="https://en.wikipedia.org/wiki/CHERI">CHERI</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#security</span> <span class="tag">#cheri</span> <span class="tag">#embedded-systems</span> <span class="tag">#hardware-isolation</span> <span class="tag">#microcontrollers</span></div>
</article>
<hr>

<a id="item-27"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://fzakaria.com/2026/09/09/review-a-pull-request-by-booting-it">trynix-preview GitHub Action 让评审者直接在浏览器中启动 PR 的 Nix 构建</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Sep 10, 00:32</span></div>
<p class="news-summary">Farid Zakaria 发布了 trynix-preview：一个 GitHub Action（以 `fzakaria/trynix@v1` 引用），它会在 pull request 上留下一条带有链接的评论，点击后可通过 trynix.dev 在浏览器中启动该 PR 的构建，整个过程不依赖服务器。演示是他在 sqlelf 项目上来自 fork 的 PR #31，点击评论中的链接后，浏览器标签页里会启动一台 Linux 机器，并把该 PR 构建出的 sqlelf 放进 PATH。 它几乎消除了评审基于 Nix 的 pull request 时的所有摩擦：评审者无需 clone、构建、SSH，也不用启动 Docker、虚拟机或云资源，只需点击一个链接就能得到一个可运行环境。这指向一种 CI 产物可在浏览器中即刻运行的工作流，不过目前它更多是补充而非取代传统 CI 产品。 该 action 本身不构建、也不缓存任何东西——它只是通过 `nix eval` 解析出 store path，并把缓存的 URL 和公钥交给浏览器，因此 PR 的构建产物必须已经存在于缓存中（例如 Cachix，开源项目 5 GiB 以内免费）。在 fork 的 pull request 上运行的工作流需要在 `actions/checkout` 步骤中设置 `allow-unsafe-pr-checkout: true`，这带来安全影响；作者建议为 PR 构建使用私有的、隔离的缓存，以免 fork 向主缓存推送。另有一种模式是只有维护者输入 `/trynix` 才触发工作流。性能是主要限制：大型二进制文件执行仍可能需要 1–2 分钟，因此该 action 最适合中小型二进制文件。</p>
<div class="news-background"><strong>背景</strong> Nix 是一个纯函数式包管理器，由 Eelco Dolstra 自 2003 年起开发，它把软件包视为不可变的值，并把每次构建存放在 `/nix/store` 下不可变的路径中。trynix.dev 正是利用了这一特性：它从二进制缓存（如 cache.nixos.org）中拉取某个包的闭包，载入到一台由 QEMU 编译为 WebAssembly 实现的 x86_64 Linux 虚拟机里，于是在浏览器标签页内就能打开一个带该包 PATH 的 shell，而服务器上不运行任何东西。trynix-preview 把这一能力用到了代码评审中：它使用定义在默认分支上的 GitHub Actions 工作流来检出并构建 pull request 的代码，然后将其发布到缓存。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://trynix.dev/">trynix</a></li>
<li><a href="https://github.com/marketplace/actions/trynix-preview">trynix preview · Actions · GitHub Marketplace · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nix_(package_manager)">Nix (package manager)</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Nix</span> <span class="tag">#GitHub Actions</span> <span class="tag">#CI/CD</span> <span class="tag">#Pull Request Review</span> <span class="tag">#Developer Tools</span></div>
</article>
<hr>

<a id="item-28"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://martypc.blogspot.com/2026/09/decoding-nec-v20-microcode.html">解码 NEC V20 微码，推进周期精确仿真</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Sep 10, 10:44</span></div>
<p class="news-summary">MartyPC 的开发者委托逆向工程专家 InfoSecDJ 对一颗 NEC V20（实为 Sharp 代工的第二货源版本）进行裸片摄影，得到了一张分辨率高达 70478x80672、约 5.6 吉像素的极高精度马赛克拼图。基于这些图像，他定位并解码了主微码 ROM 区块，发现该阵列尺寸为 258x116、共 29,928 位，推算出的微码字数达到 1032 个，而预期本应是 1024 个。 完整解码的微码 ROM 是实现 NEC V20 周期精确仿真的基础，可取代此前把 8088 核心复制过来、再外挂 V20 指令的做法。这对复古计算与仿真社区意义重大：更忠实的时序能让依赖精确指令周期的软件表现得与真实硬件一致，也延续了 reenigne 在 2020 年对 8088 微码所采用的同一套方法。 微码由一个 PLA 驱动，其 13 条输入线（其中 8 条似乎就是指令的操作码字节）构成可屏蔽的 AND 门逻辑，因此“不关心”位能让整段范围的指令共用同一份微码实现，避免 ROM 占满整个裸片。字数差异也得到解释：ROM 附近的金属层开关会根据生产的是 V20 还是 V30 而切断金属结构的一侧，使两种芯片共用同一套微码掩膜；此外解码尚未 100% 完成，仍有部分未识别的源值有待解出。</p>
<div class="news-background"><strong>背景</strong> NEC V20 是一款与 Intel 8088 引脚兼容且目标代码兼容的微处理器，其指令集与 80188 类似并带有若干扩展，凭借双 16 位内部数据总线和更快的有效地址计算等内部改进，运行速度略快于 8088。微码是 CPU 内部的固件层，负责把机器指令翻译成具体的控制信号，因此直接读取微码就能还原真实的指令时序。周期精确仿真指的是复现每条指令所占用的确切时钟周期数，使延时循环等对时序敏感的软件表现得与原机一致，而 MartyPC 正是一款追求这种保真度的仿真器。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NEC_V20">NEC V20 - Wikipedia</a></li>
<li><a href="https://www.cpu-world.com/CPUs/V20/index.html">NEC V20 processor family - CPU世界</a></li>
<li><a href="https://retrocomputing.stackexchange.com/questions/1191/what-exactly-is-a-cycle-accurate-emulator">emulation - What exactly is a cycle-accurate emulator ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#NEC V20</span> <span class="tag">#microcode</span> <span class="tag">#reverse engineering</span> <span class="tag">#emulation</span> <span class="tag">#CPU architecture</span></div>
</article>
<hr>

<a id="item-29"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://cel.cs.brown.edu/blog/design-space-async-await/">Brown CEL 论文绘制跨语言 async/await 设计空间图谱</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Sep 9, 15:22</span></div>
<p class="news-summary">布朗大学 CEL 研究组发布博客文章，总结其新论文《A Design Space Exploration of Async/Await》，系统梳理了七种现代 async runtime 在 async/await 实现上的差异。文章展示了一个将日志写入作为后台任务启动的小型伪代码程序，在七种 runtime 上会产生四种不同输出，且七者中没有两个行为完全一致。 这项工作为语言设计者、编译器工程师和系统研究者提供了一套结构化的分类体系，用来推理并发语义，这一点很重要，因为开发者常常默认 async/await 在各语言中行为一致。研究还表明即便是很小的程序也会出现行为分歧，这会影响并发代码的移植、推理和教学方式。 该分类体系涵盖多个维度，例如惰性求值与急切求值、await 点上的静态与动态挂起保证、任务 extent 的 indefinite 与 dynamic、runtime 持有强引用还是弱引用、销毁策略（await 完成、取消或终止），以及异常传播方式（destructive 或 never）。作者还将这一设计空间转化为异步程序核心演算上的形式化语义，通过小步归约追踪究竟是哪些设计决策导致示例程序产生分歧——例如 Swift 输出 &quot;AC&quot;，而 Trio 输出 &quot;ABC&quot;。</p>
<div class="news-background"><strong>背景</strong> async/await 是许多现代语言（包括 Python、Rust 和 Swift）提供的一对关键字，目的是让并发代码写起来像普通的顺序代码；博客作者将这一范式称为“straight-line asynchrony”（直线式异步），以区别于事件循环和回调。由于这些语言设计在不同社区中已发展了 15 年以上，表面语法看起来相似，但底层语义可能差异巨大。“设计空间探索”（design space exploration）是一个通用工程术语，指围绕功耗、性能、成本等关注参数，对候选设计点进行系统分析和剪枝。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Design_space_exploration">Design space exploration</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#async-await</span> <span class="tag">#concurrency</span> <span class="tag">#programming-languages</span> <span class="tag">#language-design</span> <span class="tag">#research-paper</span></div>
</article>
<hr>