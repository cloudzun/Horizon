---
layout: default
title: "Horizon 每日速递：2026-03-08"
date: 2026-03-08
lang: zh
---

> 📅 2026-03-08 · 从 72 条资讯中精选出 14 条重要内容

---

1. [Andrej Karpathy 启动面向单 GPU 训练的自主 AI 研究项目](#item-1) ⭐️ 8.0/10
2. [社区使用 Unsloth 基准测试 Qwen 3.5 本地部署](#item-2) ⭐️ 8.0/10
3. [SWE-CI 基准通过 CI 评估 AI 代理的代码库维护能力](#item-3) ⭐️ 8.0/10
4. [基于 Rust 的 WebAssembly 开发工程笔记](#item-4) ⭐️ 7.0/10
5. [社区整理列表识别常见 LLM 写作套路](#item-5) ⭐️ 7.0/10
6. [LibreOffice 敦促欧盟委员会遵守开放标准指南](#item-6) ⭐️ 7.0/10
7. [Simon Willison 强调 Joseph Weizenbaum 1976 年关于 AI 心理影响的警告](#item-7) ⭐️ 7.0/10
8. [OpenAI 向开源维护者提供免费 ChatGPT Pro 和 Codex 访问权限](#item-8) ⭐️ 7.0/10
9. [Grammarly 因 AI 功能未授权使用身份面临反对](#item-9) ⭐️ 7.0/10
10. [新协议断言内容作者身份与人类身份](#item-10) ⭐️ 7.0/10
11. [推送与拉取：三种响应式算法](#item-11) ⭐️ 7.0/10
12. [Antirez 探讨 GNU 生态内的 AI 重新实现](#item-12) ⭐️ 7.0/10
13. [文章称 Nix 理论承诺有缺陷但实用价值依然有效](#item-13) ⭐️ 7.0/10
14. [Ki Editor 发布为多光标结构代码编辑器](#item-14) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Andrej Karpathy 启动面向单 GPU 训练的自主 AI 研究项目](https://github.com/karpathy/autoresearch) ⭐️ 8.0/10

Andrej Karpathy 已启动 autoresearch 仓库的开发，专注于在单 GPU nanochat 训练设置上自动运行研究的 AI 代理。此次更新标志着利用最少硬件资源自动化科学研究流程的开源工作的开始。 该项目通过在负担得起的单 GPU 硬件上实现自主实验，而不是需要大规模集群，显著降低了 AI 研究的门槛。它结合了自主 AI 代理与高效 LLM 训练的趋势，有望让模型开发更加普及。 该系统利用了 nanochat 项目，这是一个专为在单 GPU 节点上训练 LLM 而设计的最小化且易于修改的代码库。autoresearch 项目旨在将 AI 代理链接在一起，处理从文献综述到实验执行和报告撰写的任务。

github · karpathy · Mar 8, 16:36

**背景**: nanochat 是 Karpathy 创建的一个实验性框架，涵盖所有主要 LLM 阶段，包括在最小硬件上的 tokenization 和 pretraining。自主 AI 代理是可以感知环境并采取行动以实现特定目标而无需人工干预的软件程序。结合这些可以实现不依赖昂贵云基础设施的自动化机器学习工作流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/karpathy/nanochat">NanoChat – The best ChatGPT that $100 can buy - GitHub</a></li>
<li><a href="https://github.com/karpathy/autoresearch/blob/master/README.md">autoresearch /README.md at master · karpathy/ autoresearch · GitHub</a></li>
<li><a href="https://www.webpronews.com/andrej-karpathys-autoresearch-wants-to-turn-ai-into-a-fully-automated-scientist/">Andrej Karpathy's AutoResearch Wants to Turn AI Into a Fully...</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#LLM Training`, `#AutoML`, `#Efficient AI`, `#Open Source`

---

<a id="item-2"></a>
## [社区使用 Unsloth 基准测试 Qwen 3.5 本地部署](https://unsloth.ai/docs/models/qwen3.5) ⭐️ 8.0/10

用户正在使用 Unsloth 优化的量化格式在消费级硬件上成功部署 Qwen 3.5 模型，实现了每秒约 100 个 token 的速度。讨论突出了不同 GPU 配置和 Q4_K_M 及 Q8_0 等量化级别的具体性能指标。 这表明高性能大型语言模型正变得适用于本地推理，而无需依赖云 API，显著降低了开发者的延迟和隐私担忧。它验证了 Unsloth 优化工具作为在可用硬件上运行最先进模型的关键基础设施的地位。 基准测试显示，带有思考模式的 Qwen 3.5 35B 达到了 DeepSeek API 性能的 92.5%，而无思考设置提供了更快的实际速度。用户注意到尽管有 Unsloth Dynamic 2.0 文档，但对 IQ4_XS 与 Q4_K_S 等各种可用量化选项感到困惑。

hackernews · Curiositry · Mar 7, 23:32

**背景**: Unsloth 是一个以通过重写特定模型模块来优化 LLM 微调和推理速度而闻名的库。量化是一种压缩技术，通过降低模型精度使更大的模型适应有限的 VRAM。理解参数数量和量化级别之间的权衡对于平衡模型质量与硬件限制至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/unslothai/unsloth">GitHub - unslothai/ unsloth : Fine-tuning & Reinforcement Learning for...</a></li>
<li><a href="https://symbl.ai/developers/blog/a-guide-to-quantization-in-llms/">A Guide to Quantization in LLMs | Symbl.ai</a></li>

</ul>
</details>

**社区讨论**: 用户报告称在消费级 GPU 上性能稳定，尽管有些人对不同量化变体缺乏清晰解释表示困惑。比较表明，在某些情况下，与较新的 3.5 版本相比，旧版 Qwen 3 模型可能提供更好的 token 生成速度。

**标签**: `#LLM`, `#Local Inference`, `#Quantization`, `#Unsloth`, `#AI Engineering`

---

<a id="item-3"></a>
## [SWE-CI 基准通过 CI 评估 AI 代理的代码库维护能力](https://arxiv.org/abs/2603.03823) ⭐️ 8.0/10

这篇 arXiv 论文介绍了 SWE-CI，这是一个包含 100 个任务的新基准，源自真实世界仓库的演进历史，用于评估 AI 代理在持续集成流水线上的表现。该研究衡量了模型维护代码库的性能，其中 Claude Opus 4.6 达到了 0.71 的最高解决率。 该基准将重点从单一问题解决转移到持续的代码库维护，解决了评估 AI 软件工程代理方面的关键空白。它提供了一种标准化方法来比较模型在涉及持续集成的真实世界开发工作流程中的能力。 每个任务对应平均跨越 233 天和 71 次连续提交的演进历史，为代理能力提供了真实的测试环境。然而，社区讨论强调了局限性，即 CI 通过/失败指标可能无法捕捉语义不变量或防止削弱断言之类的回归风险。

hackernews · mpweiher · Mar 8, 08:11

**背景**: 之前的基准测试如 SWE-Bench 侧重于解决单个 GitHub 问题，而不是通过持续集成流水线进行长期维护。持续集成 (CI) 是一种开发实践，代码更改会自动测试和集成以尽早发现错误。理解这些区别是掌握为何 SWE-CI 代表 AI 评估指标进步的关键。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2603.03823">[2603.03823] SWE-CI: Evaluating Agent Capabilities in Maintaining Codebases via Continuous Integration</a></li>
<li><a href="https://github.com/SWE-bench/SWE-bench">GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub</a></li>

</ul>
</details>

**社区讨论**: 评论者认为 CI 通过/失败指标无法捕捉语义不变量，并建议将代理与具有固定时间预算的人类基准进行比较。一些用户指出只有 Claude Opus 目前显示出有用的性能水平，而其他人则批评排除了更新的 GPT 模型和专有 harness。

**标签**: `#AI Agents`, `#Software Engineering`, `#Benchmarking`, `#Continuous Integration`, `#LLM Evaluation`

---

<a id="item-4"></a>
## [基于 Rust 的 WebAssembly 开发工程笔记](https://notes.brooklynzelenka.com/Blog/Notes-on-Writing-Wasm) ⭐️ 7.0/10

一篇详细的工程博客文章发布，分享了在基于 Rust 的 WebAssembly 开发过程中遇到的实际经验和陷阱。该文章引发了关于并发模式和接口设计策略的重大讨论。 这很重要，因为它解决了系统编程中的关键挑战，如并发性和接口设计，这些挑战影响 Web 应用程序的性能和安全性。它为工程师 navigating Rust 与 WebAssembly 集成的复杂性提供了指导。 关键讨论点包括 Rust 中异步互斥锁的陷阱、wasm-bindgen 的局限性以及 WebAssembly 组件模型的新兴提案。社区成员还强调了像 tsify 这样的工具用于维护跨边界的类型安全。

hackernews · vinhnx · Mar 8, 09:24

**背景**: WebAssembly 是一种二进制指令格式，设计为编程语言的便携式编译目标，支持在 Web 上进行高性能部署。Rust 是一种以内存安全和并发著称的系统编程语言，通常与 Wasm 配对用于客户端和服务器应用程序。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a></li>
<li><a href="https://webassembly.org/">WebAssembly</a></li>
<li><a href="https://dzone.com/articles/rust-and-webassembly-for-web-apps">Rust and WebAssembly: Unlocking High-Performance Web Apps - DZone</a></li>

</ul>
</details>

**社区讨论**: 社区成员讨论了当前 C 风格接口的局限性，警告不要滥用异步互斥锁，并建议使用 tsify 等工具来确保类型安全。一些人将绑定复杂性与 Emscripten 的 embind 进行了比较，同时指出了 Firefox 在改进 Web API 暴露方面的努力。

**标签**: `#Rust`, `#WebAssembly`, `#Systems Programming`, `#Concurrency`, `#Web Development`

---

<a id="item-5"></a>
## [社区整理列表识别常见 LLM 写作套路](https://tropes.fyi/tropes-md) ⭐️ 7.0/10

一个托管在 tropes.fyi 的新 markdown 文件整理了大型语言模型生成文本中常见的特定风格模式和过度使用的词汇。该资源在 Hacker News 上获得了显著关注，促使研究人员验证了诸如 GPT-4o 过度使用"tapestry"和"camaraderie"等词汇的发现。 该资源很重要，因为它帮助开发者和用户通过更好的 prompt engineering 识别并减轻经常困扰 AI 生成内容的同质化风格。通过识别这些套路，从业者可以优化输入以产生更自然且不易被检测的输出，从而提高 AI 助手的整体质量。 用户指出，简单地将列表添加到 system prompt 可能会创建递归指令层，表明它对人类读者理解 AI 局限性更有用。特定模型表现出独特的口头禅，例如 Gemini 倾向于在历史语境中使用不恰当的技术隐喻，或者 Claude 偏好使用"genuine"和"honest"等词汇。

hackernews · walterbell · Mar 7, 21:08

**背景**: Large Language Models (LLM) 是在海量文本数据集上训练的 AI 系统，用于生成类人语言，通常依赖 prompt engineering 来指导其输出。Prompt engineering 涉及构建自然语言输入以产生指定结果，随着组织将 generative AI 集成到工作流中，这项技能变得至关重要。尽管取得了进步，这些模型通常从其训练数据中继承偏见和风格怪癖，导致其写作中出现可识别的模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_engineering">Prompt engineering</a></li>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model</a></li>

</ul>
</details>

**社区讨论**: 社区讨论包括研究人员的验证，他们确认了 GPT-4o 中"tapestry"等特定过度使用的词汇，以及关于如何有效利用该列表的实际批评。用户分享了关于不同模型的轶事，例如 Gemini 持续使用技术隐喻以及 Claude 频繁使用"genuine"等真诚标记。大家一致认为，虽然该列表是有价值的参考，但直接用其指令 LLM 需要仔细的 prompt design 以避免混淆。

**标签**: `#LLM`, `#Prompt Engineering`, `#AI Writing`, `#Natural Language Processing`, `#Community Resources`

---

<a id="item-6"></a>
## [LibreOffice 敦促欧盟委员会遵守开放标准指南](https://blog.documentfoundation.org/blog/2026/03/05/cra-guidances/) ⭐️ 7.0/10

The Document Foundation 已正式请求欧盟委员会遵守其关于文档格式的开放标准指南。此举突显了一个具体案例，即欧盟流程似乎要求使用专有软件许可证才能充分参与。 这种情况强调了欧盟治理政策中开放标准与专有软件主导地位之间持续的紧张关系。它引发了人们对结构性偏见的担忧，这种偏见可能强制政策制定者使用 Microsoft 许可证，从而影响互操作性和开源采用。 社区讨论揭示了关于此问题是源于结构性偏见还是简单的程序疏忽和无能的辩论。一些用户指出委员会已经接受了请求，而其他人则回顾了过去的 OOXML 腐败等丑闻。

hackernews · maxloh · Mar 8, 14:09

**背景**: 欧盟委员会经常制定互操作性和开放标准指南，以确保公平竞争和数据可访问性。LibreOffice 是一个流行的开源办公套件，使用 ODT 和 ODS 等开放格式，与 Microsoft Office 等专有解决方案竞争。过去的争议涉及 OOXML 等标准，其中有指控称企业捕获影响了政策决策。

**社区讨论**: 评论者之间存在分歧，一方认为这是需要 Microsoft 许可证的结构性偏见，另一方则认为这只是由无能引起的程序疏忽。虽然有些人对过去的 OOXML 丑闻表示沮丧，但另一些人指出委员会已经接受了请求，或者现代软件对开放格式的处理很好。

**标签**: `#Open Source`, `#EU Policy`, `#Interoperability`, `#LibreOffice`, `#Software Standards`

---

<a id="item-7"></a>
## [Simon Willison 强调 Joseph Weizenbaum 1976 年关于 AI 心理影响的警告](https://simonwillison.net/2026/Mar/8/joseph-weizenbaum/#atom-everything) ⭐️ 7.0/10

Simon Willison 分享了一段 Joseph Weizenbaum 1976 年的引言，涉及简单计算机程序对用户心理的影响。这一分享突出了 Weizenbaum 的观察，即即使是短暂的互动也能在正常人身上诱发妄想思维。 这一历史见解与现代 LLM 开发至关重要，因为它警告了人类将简单算法拟人化的倾向。它强调了关于用户如何与聊天机器人形成情感依恋的 AI safety 和伦理担忧。 该引言源自 Weizenbaum 1976 年对其创作 ELIZA 的反思，该程序旨在模仿 Rogerian 心理治疗师。Willison 通过 Internet Archive 和 Professor Casey 的 TikTok 视频引用了该引言。

rss · Simon Willison · Mar 8, 14:59

**背景**: Joseph Weizenbaum 于 1966 年在 MIT 创建了 ELIZA，这是一个早期的自然语言处理程序。它使用 pattern matching 和 substitution methodology 来模拟对话，而实际上并不理解所处理的单词。该程序通常被视为通过自然语言进行人机交互的第一步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/artificial-intelligence/eliza-the-first-step-in-human-computer-interaction-through-natural-language-processing/">ELIZA: The First Step in Human-Computer Interaction Through ...</a></li>
<li><a href="https://liacademy.co.uk/the-story-of-eliza-the-ai-that-fooled-the-world/">The Story Of ELIZA: The AI That Fooled The World</a></li>

</ul>
</details>

**标签**: `#AI Ethics`, `#Computer History`, `#ELIZA`, `#AI Safety`, `#Tech Philosophy`

---

<a id="item-8"></a>
## [OpenAI 向开源维护者提供免费 ChatGPT Pro 和 Codex 访问权限](https://simonwillison.net/2026/Mar/7/codex-for-open-source/#atom-everything) ⭐️ 7.0/10

OpenAI 启动了一项计划，向热门开源项目的核心维护者提供六个月免费的 ChatGPT Pro 访问权限，其中包括 Codex 和条件性 Codex Security 功能。此举紧随 Anthropic 上月末宣布向符合条件的维护者提供免费 Claude Max 访问权限之后。 该计划显著降低了关键生态系统贡献者的成本，同时可能通过高级 AI 工具提高代码安全性和维护效率。这突出了 AI 提供商之间日益激烈的趋势，即争夺关键开源软件社区的影响力和好感度。 虽然 Anthropic 指定了如 5,000+ GitHub stars 等指标，但 OpenAI 的申请表除了月度下载量等定量指标外，还要求提供项目重要性等定性数据。该套餐包括价值每月 200 美元的 ChatGPT Pro，以及用于维护者自动化和发布工作流的 API credits。

rss · Simon Willison · Mar 7, 18:13

**背景**: OpenAI Codex 是一套旨在自动化软件工程任务的 AI 驱动编码代理套件，最近在 2026 年初更新了 GPT-5.3-Codex 模型。Codex Security 是 2026 年 3 月发布的新代理，可在隔离环境中扫描存储库漏洞并提出修复建议。Anthropic 的 Claude Max 是一个每月定价 200 美元的高级计划，针对需要复杂问题解决能力的开发者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/form/codex-for-oss/">Codex for Open Source | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex">OpenAI Codex</a></li>
<li><a href="https://grokipedia.com/page/Codex_Security_OpenAI">Codex Security (OpenAI)</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Open Source`, `#AI Tools`, `#Software Engineering`, `#Industry News`

---

<a id="item-9"></a>
## [Grammarly 因 AI 功能未授权使用身份面临反对](https://www.theverge.com/ai-artificial-intelligence/890921/grammarly-ai-expert-reviews) ⭐️ 7.0/10

Grammarly 推出了一项专家评审功能，该功能在不征得同意的情况下生成受真实人物启发的写作建议。用户发现他们自己或同事的身份被用于模拟 AI 反馈而未获许可。 这种情况突显了生成式 AI 产品中未经授权身份使用的重大伦理和法律风险。它影响了对 AI 工具的信任，并提出了关于大语言模型时代同意权和隐私权的问题。 该功能允许用户选择特定的专家来启发反馈，但一些列出的个人惊讶地发现自己未经事先同意就被列入其中。AI 生成的反馈模仿了这些个人的风格或权威，可能会歪曲他们的观点。

rss · The Verge AI · Mar 6, 20:58

**背景**: 生成式 AI 模型通常需要大型数据集来学习风格和模式，其中有时包括未经明确许可从网络上抓取的个人数据。随着 AI 模仿人类行为的能力越来越强，数字肖像或身份权的概念正成为一个关键的法律战场。对于致力于 AI 技术负责任部署的用户和开发者来说，了解这些风险至关重要。

**标签**: `#AI Ethics`, `#Privacy`, `#Generative AI`, `#Legal Compliance`, `#Responsible AI`

---

<a id="item-10"></a>
## [新协议断言内容作者身份与人类身份](https://codeberg.org/robida/human.json) ⭐️ 7.0/10

一个名为 human.json 的新轻量级协议已被提出，允许创作者声明作者身份并为他人的人类身份担保。该提议目前正在 Lobste.rs 技术社区中进行讨论。 这一举措解决了数字生态系统中关于 AI 生成内容和机器人验证的关键新兴问题。建立一种证明人类身份的标准方法有助于恢复在线互动和内容所有权的信任。 该协议托管在 Codeberg 上，旨在成为一种无需重型基础设施的身份断言轻量级解决方案。可用摘要中的具体技术实施细节有限，主要集中在担保的概念框架上。

rss · Lobsters · Mar 8, 16:31

**背景**: 人工智能的崛起带来了关于 AI 生成内容和机器人验证的关键新兴问题。用户越来越需要在数字生态系统中区分人类互动和自动化系统的方法。轻量级技术协议为这些验证挑战提供了潜在的解决方案，而无需重型基础设施。

**标签**: `#protocol`, `#identity`, `#authorship`, `#security`, `#web`

---

<a id="item-11"></a>
## [推送与拉取：三种响应式算法](https://jonathan-frere.com/posts/reactivity-algorithms/) ⭐️ 7.0/10

这篇文章对用于在软件系统中实现响应式的三种不同算法进行了技术比较。它具体分析了这些架构模式中推送和拉取数据变更的机制。 响应式系统是现代前端框架和状态管理库的基础。理解这些底层算法有助于工程师构建更高效且可维护的应用程序。 讨论集中在细粒度响应式系统中常见的基于推送（push-based）和基于拉取（pull-based）模型之间的权衡。技术深度旨在解决框架作者面临的性能影响和实现复杂性问题。

rss · Lobsters · Mar 7, 16:52

**背景**: 软件中的响应式（Reactivity）是指当数据更新时，变更通过系统自动传播。常见模型包括变更立即通知的基于推送（push-based）系统，以及按需检查依赖的基于拉取（pull-based）系统。这些模式在 Angular、Vue 和 Svelte 等框架中至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dev.to/luciano0322/push-based-vs-pull-based-reactivity-the-two-driving-models-behind-fine-grained-systems-56jc">Push-based vs. Pull-based Reactivity: The Two Driving Models ...</a></li>
<li><a href="https://plutojl.org/en/docs/reactivity/">Reactivity – how Pluto notebooks update automatically</a></li>
<li><a href="https://medium.com/coreteq/reactive-algorithms-how-angular-took-the-right-path-c90e9f0183c2">Mastering Reactive Algorithms in Angular: Signals vs RxJS...</a></li>

</ul>
</details>

**标签**: `#Reactivity`, `#Software Architecture`, `#Algorithms`, `#Frontend Engineering`

---

<a id="item-12"></a>
## [Antirez 探讨 GNU 生态内的 AI 重新实现](https://antirez.com/news/162) ⭐️ 7.0/10

Salvatore Sanfilippo 发表了一篇关于 GNU 项目内 AI 驱动重新实现的分析。他研究了人工智能工具如何被用于重建现有的自由软件基础设施。 这一讨论意义重大，因为它解决了 AI 生成代码对自由软件许可证构成的法律和伦理挑战。它影响了开源社区如何看待 AI 辅助开发的完整性和许可证合规性。 文章侧重于自由软件基础设施与新兴 AI 技术的交汇点。它突出了 GNU 生态系统中创新与保护原始作者权利之间的张力。

rss · Lobsters · Mar 8, 16:39

**背景**: GNU 是一个庞大的自由软件工具集，构成了许多操作系统的骨干，受严格的 copyleft 许可证管辖。AI 重新实现是指使用机器学习模型重写现有代码，这引发了关于衍生作品的问题。这些概念对于理解文章中讨论的潜在冲突至关重要。

**标签**: `#GNU`, `#AI`, `#Open Source`, `#Systems Programming`

---

<a id="item-13"></a>
## [文章称 Nix 理论承诺有缺陷但实用价值依然有效](https://fzakaria.com/2026/03/07/nix-is-a-lie-and-that-s-ok) ⭐️ 7.0/10

一位公认的 Nix 专家发表文章指出 Nix 的核心抽象在理论上并不完全成立。尽管如此，作者仍认为该工具对开发者的实用价值依然有效。 这挑战了函数式包管理的基础宣传，同时向用户保证了其在现实世界中的应用。它鼓励更务实地采用 Nix，而不必依赖绝对的理论保证。 文章具体区分了理想化的可复现模型与在生产环境中观察到的实际行为。它指出理解这些局限性对于使用 Nix 构建可靠系统至关重要。

rss · Lobsters · Mar 7, 22:15

**背景**: Nix 是一个创建于 2003 年的跨平台包管理器，它将软件包视为不可变的值。它将函数式编程概念应用于包管理，旨在实现可复现和声明式的系统配置。最近的研究继续评估这种函数式模型在多大程度上能实现大规模的二进制级可复现构建。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nix_(package_manager)">Nix (package manager)</a></li>
<li><a href="https://nixos.org/">Nix & NixOS | Declarative builds and deployments</a></li>
<li><a href="https://arxiv.org/pdf/2501.15919v1">Does Functional Package Management Enable Reproducible Builds ...</a></li>

</ul>
</details>

**标签**: `#Nix`, `#DevOps`, `#Software Engineering`, `#Package Management`, `#Technical Commentary`

---

<a id="item-14"></a>
## [Ki Editor 发布为多光标结构代码编辑器](https://ki-editor.org/) ⭐️ 7.0/10

Ki Editor 已宣布为一款新的代码编辑器，结合了基于抽象语法树的多光标功能与结构编辑能力。该工具允许开发者通过代码的层次语法结构进行操作，而不是将其视为纯文本。 这种集成填补了编程语言工具中的一个重要空白，有望在保持编辑灵活性的同时减少语法错误。它代表了一种新颖的方法，可能会影响未来的集成开发环境和软件工程工作流。 与传统编辑器不同，Ki Editor 通过称为抽象语法树的层次语法结构来操作代码。该项目托管在 GitHub 上，并包含安装和构建说明的文档。

rss · Lobsters · Mar 7, 16:03

**背景**: 结构编辑指的是编辑知晓底层结构的文档，例如由上下文无关语法定义的计算机程序。大多数源代码编辑器是带有语法高亮等功能的文本编辑器，而结构编辑器将代码解析为树状表示。这种方法旨在通过强制结构约束使编写具有无效语法的程序变得更加困难。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Structural_editing">Structural editing</a></li>
<li><a href="https://sesamedisk.com/ki-editor-ast-code-editing/">Ki Editor: Revolutionizing Code Editing with AST-Based ...</a></li>

</ul>
</details>

**标签**: `#Developer Tools`, `#Structural Editing`, `#IDE`, `#Programming Languages`, `#Software Engineering`

---