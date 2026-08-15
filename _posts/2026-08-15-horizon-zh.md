---
layout: default
title: "Horizon 每日速递：2026-08-15"
date: 2026-08-15
lang: zh
---

> 📅 2026-08-15 · 从 74 条资讯中精选出 26 条重要内容

---

1. [免费午餐的终结：软件从根本上转向并发](#item-1) <span class="score-badge score-high">9.0</span>
2. [自动化的讽刺：Bainbridge 1983 年开创性论文](#item-2) <span class="score-badge score-high">9.0</span>
3. [借助 Codex 实现 232 倍内核加速的 AI 辅助优化](#item-3) <span class="score-badge score-mid">8.0</span>
4. [另一个肖恩·伯恩不存在：身份验证之败](#item-4) <span class="score-badge score-mid">8.0</span>
5. [Qwen 3\.8 27B 发布，成为强大的本地推理模型](#item-5) <span class="score-badge score-mid">8.0</span>
6. [macOS 屏幕共享漏洞遭积极利用，可完全控制设备](#item-6) <span class="score-badge score-mid">8.0</span>
7. [GLM\-5\.3 证明中国实验室靠创新而非蒸馏追赶前沿](#item-7) <span class="score-badge score-mid">8.0</span>
8. [Sebastian Raschka 从零构建 AI 文本检测器](#item-8) <span class="score-badge score-mid">8.0</span>
9. [AI 让软件过度安全，执法机构恐将迎来新一轮“go dark”](#item-9) <span class="score-badge score-mid">8.0</span>
10. [压缩即预测——但仅在固定编码条件下成立](#item-10) <span class="score-badge score-mid">8.0</span>
11. [在 Linux 内核、Musl Libc 和 BGP 中实现 IPv8 互联网草案](#item-11) <span class="score-badge score-mid">8.0</span>
12. [使用 TLA\+模型检查提升系统安全性](#item-12) <span class="score-badge score-mid">8.0</span>
13. [2004 年 RuneScape 如何打造适应 56k 拨号的多人在线协议](#item-13) <span class="score-badge score-mid">8.0</span>
14. [AI 并非在思维上超越数学家，而是在记忆上超越他们](#item-14) <span class="score-badge score-mid">7.0</span>
15. [RISC\-V 的可选特性导致碎片化与兼容性问题](#item-15) <span class="score-badge score-mid">7.0</span>
16. [Unicode 的幽灵字符：CJK 编码之谜](#item-16) <span class="score-badge score-mid">7.0</span>
17. [圆桌讨论：审视影响美国政策的'审查\-工业复合体'观念](#item-17) <span class="score-badge score-mid">7.0</span>
18. [OpenAI 和 Anthropic 降价应对中国 AI 对手崛起](#item-18) <span class="score-badge score-mid">7.0</span>
19. [苹果携手阿里为中国定制训练 AI 模型](#item-19) <span class="score-badge score-mid">7.0</span>
20. [Firefox 成为最后一个支持 uBlock Origin 的主流浏览器](#item-20) <span class="score-badge score-mid">7.0</span>
21. [Serokell 在第五部分中重点介绍 GHC 依赖类型进展](#item-21) <span class="score-badge score-mid">7.0</span>
22. [ActivityPub 因“无聊”而胜出](#item-22) <span class="score-badge score-mid">7.0</span>
23. [RVA23 对比 ARMv9：指令数与代码密度小实验](#item-23) <span class="score-badge score-mid">7.0</span>
24. [软件工程无银弹，40 年后依然如此](#item-24) <span class="score-badge score-mid">7.0</span>
25. [curl 项目推出实时性能页面以追踪性能回退](#item-25) <span class="score-badge score-mid">7.0</span>
26. [潜在推理模型比预期更可解释](#item-26) <span class="score-badge score-mid">7.0</span>

---

<a id="item-1"></a>
<article class="news-item">
<h2 class="news-title"><a href="http://www.gotw.ca/publications/concurrency-ddj.htm">免费午餐的终结：软件从根本上转向并发</a><span class="score-badge score-high">9.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 15, 10:31</span></div>
<p class="news-summary">Herb Sutter 于 2005 年 3 月在《Dr. Dobb&#x27;s Journal》发表的文章指出，通过提高时钟频率等传统方式来提升 CPU 性能已接近极限。他认为软件开发人员必须转向并发，才能充分利用业界向超线程（hyperthreading）和众核（multicore）架构的转变。 这篇文章被广泛认为是向软件行业发出‘免费’性能提升时代结束的警示，过去软件无需修改就能在新硬件上跑得更快。它从根本上改变了软件工程实践，使并发成为所有开发者而非少数专家的核心关注点。 这篇文章最早于 2004 年 12 月发布在 Sutter 的博客上，并于 2005 年 3 月发表在《Dr. Dobb&#x27;s Journal》上；配套的 CPU 趋势图于 2009 年 8 月更新，以确认该趋势仍在继续。Sutter 指出，大多数应用程序并非天然可并行化，而隐式并行化编译器也无法与显式线程化和并行化代码的效果相媲美。</p>
<div class="news-background"><strong>背景</strong> 并发（concurrency）指的是多个计算或任务同时执行，通常通过线程或进程实现。众核处理器（multicore processor）在单个芯片上包含多个独立的处理单元，即核心（core）。几十年来，随着时钟频率的提高，软件无需修改即可自动获得性能提升；但在触及物理极限后，制造商转向众核设计，迫使软件必须显式编写为并行运行才能有效利用更多核心。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Concurrency_(computer_science)">Concurrency (computer science) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multi-core_processor">Multi - core processor - Wikipedia</a></li>
<li><a href="https://www.techtarget.com/searchdatacenter/definition/multi-core-processor">What is a multicore processor and how does it work?</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#concurrency</span> <span class="tag">#multicore</span> <span class="tag">#parallel computing</span> <span class="tag">#software engineering</span> <span class="tag">#Herb Sutter</span></div>
</article>
<hr>

<a id="item-2"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://ckrybus.com/static/papers/Bainbridge_1983_Automatica.pdf">自动化的讽刺：Bainbridge 1983 年开创性论文</a><span class="score-badge score-high">9.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 15, 17:13</span></div>
<p class="news-summary">Lisanne Bainbridge 在 1983 年发表的论文《自动化的讽刺》指出，自动化往往会加剧而非消除人类操作员面临的问题，尤其是在异常情况下。文章强调了这样一个悖论：随着自动化程度提高，人类操作员的角色反而变得更加关键，并主张设计人机协作。 这篇论文被认为是具有开创性的奠基之作，从根本上改变了有关人因、自动化和安全关键系统的研究。其见解在现代人工智能、安全性和系统工程研究中仍具有高度相关性，并被频繁引用。 该论文发表于《Automatica》期刊，认为操作员在常规自动化操作期间不会锻炼技能，却需要在无法自动化的罕见关键干预中发挥作用。Bainbridge 指出监控任务令人疲惫，并认为在自动化条件下，操作员可能需要更多而非更少的培训。</p>
<div class="news-background"><strong>背景</strong> 在工业自动化中，人类操作员传统上被视为错误的主要来源，而自动化被期望通过移除人来减少这些错误。Bainbridge 的论文通过指出 &#x27;讽刺&#x27; 之处挑战了这一假设：留给人类的恰恰是最难自动化的任务——异常和不可预见的情况——而常规自动化会削弱处理这些情况所需的关键技能。到 2016 年 11 月，该论文已被引用超过 1800 次，成为人因工程领域的奠基性参考文献。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ironies_of_Automation">Ironies of Automation</a></li>
<li><a href="https://humanfactors101.com/2020/05/24/the-ironies-of-automation/">The Ironies of Automation – Human Factors 101</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#human factors</span> <span class="tag">#automation</span> <span class="tag">#human-computer interaction</span> <span class="tag">#safety-critical systems</span> <span class="tag">#control theory</span></div>
</article>
<hr>

<a id="item-3"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://sankalp.bearblog.dev/autoresearch/">借助 Codex 实现 232 倍内核加速的 AI 辅助优化</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">tosh</span><span class="news-time">Aug 15, 11:00</span></div>
<p class="news-summary">一位开发者利用 OpenAI 的 Codex 自动研究、剖析并优化计算内核，实现了 232 倍的加速。这项工作展示了一个由 AI 驱动的“基准测试→剖析→验证→研究→改进”的内核优化循环。 这一结果凸显了 AI 在传统上需要深厚 GPU 编程专业知识才能完成的底层性能工程中日益增长的能力。它可能降低内核优化的门槛，但也引发了关于过拟合特定输入以及 AI 生成优化可靠性的担忧。 所提供内容中未给出具体内核和硬件细节，但该工作遵循了使用 Codex 的基准测试-剖析-验证-研究-改进流程。社区评论指出，许多以此方式优化的竞赛解决方案在分布外输入上失效，表明结果可能无法泛化。</p>
<div class="news-background"><strong>背景</strong> 计算内核是为 GPU 等高吞吐量加速器编译的例程，优化其对性能至关重要。OpenAI Codex 是 2025 年 4 月发布的 AI 编程代理，可以编写代码和修复错误，这里被用于自动化优化循环。这种方法反映了 LLM 协助性能工程任务的日益增长趋势，尤其是在训练数据丰富的 GPU 和 SIMD 内核领域。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)">OpenAI Codex (AI agent) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Compute_kernel">Compute kernel - Wikipedia</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 社区评论既表达了热情，也表达了谨慎。一位用户指出，某竞赛中前 10 个解决方案中有 8 个（均为 AI 优化）在竞赛以外的任何输入上都会失效，而专家调整过的解决方案则保持稳健。其他人则欣赏这篇人类撰写的长文，并推测训练数据对 GPU 内核特别丰富，是否因为这类内核在 AI 研究人员自己工作中也很重要。</div>
<div class="news-tags"><span class="tag">#AI-assisted development</span> <span class="tag">#Kernel optimization</span> <span class="tag">#Codex</span> <span class="tag">#GPU programming</span> <span class="tag">#Benchmarking</span></div>
</article>
<hr>

<a id="item-4"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://conic.al/writing/the-other-sean-byrne-doesnt-exist/">另一个肖恩·伯恩不存在：身份验证之败</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">rdl</span><span class="news-time">Aug 15, 04:18</span></div>
<p class="news-summary">在这篇个人随笔中，肖恩·伯恩描述了身份验证和数据匹配系统如何反复将他与另一个同名的人混淆——而那个“另一个肖恩·伯恩”其实并不存在。故事展现了这种错误匹配如何导致严重的官僚和法律后果。 这个故事暴露了基于姓名的身份系统有多么脆弱，误报可能导致服务被拒、被捕甚至财务受损，却几乎无人为此负责。对于设计并依赖自动化身份检查的软件工程师、数据管理者和政策制定者来说，这是一个警示。 背后的技术问题涉及概率记录关联和模糊匹配，这类方法会根据姓名、出生日期等字段的相似度打分来关联记录；如果阈值设得过于宽松，不同的人就可能被合并为同一身份。文章中的经历表明，这类误报可能造成改变人生的后果，而举证责任往往落在受害者身上。</p>
<div class="news-background"><strong>背景</strong> 身份验证（identity proofing）是确认某人确实为其所声明身份的过程，通常通过检查证件或将数据与可信来源比对。记录关联（record linkage）又称数据匹配或实体解析，是在没有公共标识符时跨数据库关联记录的技术，分为确定性方法和概率性方法，后者依赖多字段证据的平衡。模糊匹配算法使用距离度量来查找相似但不完全相同的记录，有助于处理拼写错误和姓名变体，但也可能产生误报。一些英语国家缺乏全民身份证号，使得基于姓名的匹配更加普遍、也更容易出错。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Probabilistic_record_linkage">Probabilistic record linkage</a></li>
<li><a href="https://moj-analytical-services.github.io/splink/topic_guides/theory/probabilistic_vs_deterministic.html">Probabilistic vs Deterministic linkage - Splink</a></li>
<li><a href="https://www.okta.com/blog/industry-insights/what-is-identity-proofing/">What Is Identity Proofing ? | Okta</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者分享了各自被有缺陷的身份系统误伤的经历，其中一人估计这类错误让他损失超过两万美元。还有人提到电影《巴西》中经典的 Tuttle/Buttle 姓名混淆，并认为英语国家没有国民身份证号是根本原因之一。整体情绪是恐惧和批评，许多人指出自动化系统被赋予过高信任，而误报造成伤害后却无人担责。</div>
<div class="news-tags"><span class="tag">#identity systems</span> <span class="tag">#data quality</span> <span class="tag">#privacy</span> <span class="tag">#software failures</span> <span class="tag">#bureaucracy</span></div>
</article>
<hr>

<a id="item-5"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://huggingface.co/Qwen/Qwen3.8-27B-FP8">Qwen 3.8 27B 发布，成为强大的本地推理模型</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">erdaltoprak</span><span class="news-time">Aug 14, 15:00</span></div>
<p class="news-summary">Qwen 3.8 27B 是新发布的本地大语言模型，在 Hugging Face 上提供 FP8 精度版本。据 Hacker News 社区测试，它展现出强大的推理能力，成为继 Gemma 4 之后第二个通过某用户私人基准测试的本地模型。 这一发布表明本地大语言模型正在缩小与更大模型之间的推理差距，使得更复杂的任务能够在个人硬件上运行。它也凸显了开源权重 Qwen 模型和量化格式生态的成长，让先进 AI 更易获得。 该模型以 FP8 精度运行，以少量数值细节换取更低内存占用和更快处理速度。社区测试注意到，在启用多 token 预测（MTP）时，它大约消耗五倍的 token，耗时 12 分 30 秒，而且其 VRAM 使用效率低于 Gemma 4 或 Glimmer。</p>
<div class="news-background"><strong>背景</strong> Qwen 是阿里云 DAMO 研究院开发的开源大语言模型系列，于 2023 年 8 月首次发布，采用 Apache 2.0 许可证。FP8（8 位浮点）是一种量化格式，可降低内存需求并加速推理，使模型更易于本地运行。本地大语言模型直接运行在用户自己的电脑或工作站上，而不是依赖云端 API，这需要足够的 RAM 或 VRAM。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Qwen_language_model">Qwen (language model)</a></li>
<li><a href="https://exploreai.tools/ai-models/mistral-nemo-12b-instruct-fp8-2407">Mistral Nemo 12B Instruct FP 8 (v24.07) - Open-Source Quantized AI...</a></li>
<li><a href="https://iternal.ai/how-to-run-llm-locally">How to Run an LLM Locally : Step-by-Step Guide (2026)</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 社区整体评价积极。CMay 称赞 Qwen 3.8 27B 是继 Gemma 4 之后第二个通过其私人基准测试的本地模型；simonw 称赞它能画出解剖结构正确的自行车上的鹈鹕。dexterlagan 认为其基础软件工程能力可用，dofm 则观察到与 Qwen 3.6 相比，其思考轨迹呈现出独特的笔记式风格。</div>
<div class="news-tags"><span class="tag">#Qwen</span> <span class="tag">#Local LLM</span> <span class="tag">#Reasoning</span> <span class="tag">#FP8</span> <span class="tag">#Hacker News</span></div>
</article>
<hr>

<a id="item-6"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://arstechnica.com/security/2026/08/vulnerability-giving-attackers-full-control-of-macs-is-under-active-exploitation/">macOS 屏幕共享漏洞遭积极利用，可完全控制设备</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Ars Technica AI</span><span class="news-time">Aug 14, 18:32</span></div>
<p class="news-summary">荷兰网络安全官员警告称，高危 macOS 屏幕共享漏洞 CVE-2026-65400 正遭到积极利用。Apple 已为 macOS Tahoe、Sequoia 和 Sonoma 发布补丁。 该漏洞允许未经身份验证的攻击者以 root 权限执行代码，从而可能完全控制受影响的 Mac。由于该漏洞已在野外被利用并植入 Monero 矿工程序，启用了屏幕共享的 Mac 用户应立即打补丁。 该漏洞源于 macOS 屏幕共享功能中的状态管理缺陷，CVSS 严重性评分为 7.1/10。在端口 5900 暴露于互联网的系统上观察到了利用行为，攻击者获取了 root 权限；相关细节已在 Black Hat 安全大会上公开。</p>
<div class="news-background"><strong>背景</strong> CVE-2026-65400 是 Common Vulnerabilities and Exposures（CVE）标识符，这是公开已知安全漏洞的标准化命名体系。受影响的 macOS 屏幕共享功能基于 VNC（Virtual Network Computing），这是一种远程桌面协议，允许用户通过网络查看和控制另一台电脑的屏幕，通常使用端口 5900。Apple 在披露漏洞时常使用&quot;可能允许&quot;等留有余地的措辞，这是软件开发商的常见做法。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures">Common Vulnerabilities and Exposures - Wikipedia</a></li>
<li><a href="https://www.redhat.com/en/topics/security/what-is-cve">What is a CVE?</a></li>
<li><a href="https://en.wikipedia.org/wiki/VNC">VNC - Wikipedia</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#security</span> <span class="tag">#macOS</span> <span class="tag">#vulnerability</span> <span class="tag">#CVE</span> <span class="tag">#exploit</span></div>
</article>
<hr>

<a id="item-7"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.interconnects.ai/p/glm-53-how-chinese-labs-keep-stride">GLM-5.3 证明中国实验室靠创新而非蒸馏追赶前沿</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Interconnects (Nathan Lambert)</span><span class="news-time">Aug 14, 21:23</span></div>
<p class="news-summary">Z.ai 发布了 GLM-5.3，这是一个约 750B 参数的模型，基于与 GLM-5.2 相同的基座模型并大幅扩展了后训练。它在许多基准测试上超越了 Moonshot AI 的 Kimi K3，并在部分测试上超过 Claude Fable 5 或 GPT-5.6-Sol，开放权重将在两周后上线 Hugging Face。 此次发布表明，中国实验室可以通过独立创新和后训练实力而非蒸馏来达到前沿水平，挑战了关于其竞争方式的常见假设。它加剧了前沿竞赛的动态，并可能重塑以基准驱动的发展模式和模型发布周期。 GLM-5.3 约有 750B 参数，约为 Kimi K3 参数量的三分之一，最初仅在 coding 计划中提供。Z.ai 表示“我们做的只是扩展后训练”，这意味着该模型使用与 GLM-5.2 相同的基座，但后训练大幅增强。</p>
<div class="news-background"><strong>背景</strong> GLM（通用语言模型）是中国公司 Z.ai（前身为智谱 AI）开发的一系列开放权重大型语言模型。知识蒸馏是一种将知识从大型教师模型转移到较小学生模型的技术，曾有传言称这解释了中国实验室的快速进步。后训练指在初始预训练之后应用的微调和强化学习等技术，可以在不改变基座模型的情况下显著提升基准性能。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GLM_(AI)">GLM (AI) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Z.ai">Z.ai - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 一位评论者称赞了这篇文章，并询问 Z.ai 原生的 AI 安全能力，指出 Z.ai 和阿里巴巴似乎拥有最好的团队，但所有中国实验室都缺乏算力，因此质疑有多少算力被用于复杂 agentic 部署的安全测试。该评论者认为 Z.ai 正在采取类似 Anthropic 的发布前测试方法，但尚无政府的“自愿”授权。</div>
<div class="news-tags"><span class="tag">#GLM</span> <span class="tag">#AI frontier</span> <span class="tag">#Chinese AI labs</span> <span class="tag">#model release</span> <span class="tag">#benchmarks</span></div>
</article>
<hr>

<a id="item-8"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://magazine.sebastianraschka.com/p/ai-detector-from-scratch">Sebastian Raschka 从零构建 AI 文本检测器</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Ahead of AI (Sebastian Raschka)</span><span class="news-time">Aug 15, 11:54</span></div>
<p class="news-summary">Sebastian Raschka 发布了一篇从零构建 AI 文本检测器的分步教程，涵盖数据集构建、微调 DistilBERT 分类器、通过 API 和 UI 进行本地部署，以及将该检测器作为验证器来训练小型语言模型以规避检测。该项目受 Substack 新推出的 AI 检测功能启发，采用了与 Pangram 模型类似的方法。 本教程提供了一个关于 AI 检测器如何工作的实用端到端示例，并强调了其固有限制，包括与新 LLM 的猫鼠动态以及误报风险。对于构建内容审核工具的开发者、希望在使用语法检查器时保持人类写作风格的作者，以及那些对超越数学和代码的、基于验证器的 LLM 训练感兴趣的人来说，这都很有价值。 该检测器返回 0–100 的分数，表示分类器基于微调 DistilBERT 对文本为 AI 生成的估计概率。教程指出，该分数不应被解释为 AI 作者身份的一般概率，并明确承认 AI 检测器是一场猫鼠游戏，随着新 LLM 学会规避检测，检测器需要不断更新。</p>
<div class="news-background"><strong>背景</strong> AI 文本检测可以通过多种方式实现，包括监督分类器、基于扰动的概率测试、困惑度测量和水印技术。DistilBERT 是 BERT 的蒸馏小型版本，在保持大部分性能的同时更快、更轻量，适合在分类任务上进行微调。RLVR（带可验证奖励的强化学习，Reinforcement Learning with Verifiable Rewards）是一种训练范式，最早于 2024 年在 Tülu 3 中引入，它使用验证器根据客观标准提供奖励；在本项目中，它被用来训练小型语言模型生成能够规避检测的文本。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/docs/transformers/model_doc/distilbert">DistilBERT · Hugging Face</a></li>
<li><a href="https://medium.com/@adnanmasood/rlvr-explained-reinforcement-learning-with-verifiable-rewards-examples-risks-and-faqs-89815659bd76">Reinforcement Learning with Verifiable Rewards ... | Medium</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI detection</span> <span class="tag">#Machine Learning</span> <span class="tag">#NLP</span> <span class="tag">#DistilBERT</span> <span class="tag">#Tutorial</span></div>
</article>
<hr>

<a id="item-9"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://blog.cryptographyengineering.com/2026/08/14/everything-is-about-to-go-dark/">AI 让软件过度安全，执法机构恐将迎来新一轮“go dark”</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 15, 12:50</span></div>
<p class="news-summary">在 Cryptography Engineering 博客 2026 年 8 月的一篇文章中，作者认为 AI 很快会让软件变得过于安全，并预测主要软件在未来两年内很可能耗尽可远程利用的漏洞。他说，这将导致美国情报与执法机构突然失去很大一部分监控能力。 如果执法和情报机构无法再远程利用漏洞，围绕加密与通信访问权的“going dark”争论将更加激烈。其结果会影响公共安全、监控政策，以及所有技术用户对隐私与安全之间平衡的取舍。 文章指出，虽然 AI 可以加速漏洞发现，但可用漏洞的数量是有限的，并且很可能很快就会触顶。文章还提到，“例外访问”（exceptional access）之争从未真正消失，在英国等地甚至更加恶化，而且强制植入的后门可能被执法机构原本要防范的对手所滥用。</p>
<div class="news-background"><strong>背景</strong> “Going dark”是美国联邦调查局（FBI）等执法机构使用的术语，指它们难以访问依法有权获取的加密通信和数据。过去，监控往往依赖于对电话等通信进行窃听，《火线》（The Wire）等剧集对此有所体现。文章认为，AI 驱动的软件安全改进可能会缩小可利用漏洞的规模，从根本上改变执法机构自 2010 年前后以来一直依赖的攻击性安全格局。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cryptographyengineering.com/2026/08/14/everything-is-about-to-go-dark/">Everything is about to “ go dark ” – A Few Thoughts on Cryptographic...</a></li>
<li><a href="https://archives.fbi.gov/archives/news/speeches/going-dark-are-technology-privacy-and-public-safety-on-a-collision-course">FBI — Going Dark : Are Technology, Privacy, and Public Safety on...</a></li>
<li><a href="https://www.everycrsreport.com/reports/R44481.html">Encryption and the “ Going Dark ” Debate - EveryCRSReport.com</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者大多对同情间谍机构持怀疑态度，有人讽刺地表示“可怜的间谍/警察”应该去干活，而不是大规模收集所有人的通信和元数据。其他人则认为情报机构会适应局面并创造性地利用 AI，立法通常太慢而难以奏效，而且后门最终主要会伤害强制推行后门的国家，尤其是在非美国政府正减少对美国软件依赖的背景下。</div>
<div class="news-tags"><span class="tag">#encryption</span> <span class="tag">#law-enforcement</span> <span class="tag">#AI</span> <span class="tag">#surveillance</span> <span class="tag">#geopolitics</span></div>
</article>
<hr>

<a id="item-10"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://lukefleed.xyz/posts/compression/">压缩即预测——但仅在固定编码条件下成立</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 15, 13:01</span></div>
<p class="news-summary">一篇技术博客文章严谨地审视了‘压缩即预测’这一说法，并从信息论角度证明了这一等价关系的两个方向。文章表明，顺序概率模型可以转化为无损压缩器，其理想载荷长度等于模型的累计对数损失，而任何唯一可解码的编码都会诱导出一个预测分布。 这篇文章为 Hacker News 和近期大语言模型讨论中流行的说法提供了重要的限定条件，澄清了等价关系真正成立的条件。对于机器学习和系统领域的读者而言，它强调了在比较压缩与预测之前，必须考虑模型传输和解码器已知的信息。 证明涵盖了两个方向：顺序模型可转换为基于算术编码的压缩器，而唯一可解码的编码可以分解为下一符号的条件概率。一个关键限定是，对数损失不包含传输模型本身的成本，因此一旦计入参数，对数损失更低的模型仍然可能产生更大的完整文件。</p>
<div class="news-background"><strong>背景</strong> ‘压缩即预测’这一思想可追溯至 1940 年代克劳德·香农的信息论，该理论将熵与数据源的可预测性联系起来。在自适应压缩中，模型为下一个符号分配概率，熵编码器将这些概率转换为比特；交叉熵和对数损失则衡量预测分布与观测数据的匹配程度。近期包括 3Blue1Brown 视频和 ngrok 文章在内的讨论，都通过语言建模重新梳理了这一数学关系，而 Hutter 奖和最小描述长度（MDL）的相关文献也早已将学习与压缩联系起来。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://fatsil.org/culture-traditional-skills/compression-is-prediction/">Compression Is Prediction - FATSIL</a></li>
<li><a href="https://dev.to/trismegistus/compression-is-prediction-and-it-explains-why-llms-actually-work-209e">Compression Is Prediction — and It Explains Why... - DEV Community</a></li>
<li><a href="https://machinelearningmastery.com/cross-entropy-for-machine-learning/">A Gentle Introduction to Cross - Entropy for Machine Learning</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#compression</span> <span class="tag">#prediction</span> <span class="tag">#information theory</span> <span class="tag">#entropy</span> <span class="tag">#machine learning</span></div>
</article>
<hr>

<a id="item-11"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://goonhost.rocks/blog/implementing-ipv8-internet-draft">在 Linux 内核、Musl Libc 和 BGP 中实现 IPv8 互联网草案</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 14, 19:05</span></div>
<p class="news-summary">goonhost.rocks 研究团队依据 draft-thain-ipv8-02 互联网草案，在 Linux Kernel 6.6、Musl Libc 和 BGP 中完整实现了 IPv8 协议栈，并部署到分布式多 AS 测试网络。该协议在实验室中运行顺畅，但在真实网络环境下因路径 MTU 发现失败和路由不对称等问题而失效。 这项工作将一个未经检验的激进提案转化为实证数据，精确揭示了 IPv8 在真实网络条件下失败的原因和环节。它为未来互联网草案的压力测试提供了可复现的方法，并指出了任何 64 位寻址方案在部署前都必须解决的 PMTUD 黑洞和路由表膨胀等问题。 该实现为 Linux 内核 6.6 增加了原生 AF_INET8 地址族（family 46），支持 TCP8、UDP8 和 RAW8 套接字，并提供 28 字节 IPv8 头部解析和 64 位路由表查找。然而，更大的头部会使 1500 字节 MTU 链路失效，除非全局强制将 TCP MSS 钳制到 1452 字节；同时该地址方案可能使 Default-Free Zone 的 BGP 路由表从约 115 万条膨胀至 300 万至 500 万条。</p>
<div class="news-background"><strong>背景</strong> IPv8 是一个投机性的互联网草案（draft-thain-ipv8-02），提议用 64 位分层地址结构（ASN.Host）取代 IPv4/IPv6，为每个 32 位 ASN 持有者提供 43 亿个主机地址。它声称完全向后兼容 IPv4，并将 DHCP、DNS、NTP、WHOIS 等服务整合为单一的“Zone Server”。任何人都可以无障碍地撰写和发布互联网草案，因此这类提案的真实可行性需要实际实现和压力测试来验证。goonhost.rocks 团队从 Linux 内核 ring-0 代码到用户态 libc 和 BGP 路由构建了完整协议栈，以实证方式评估这些主张。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://goonhost.rocks/blog/implementing-ipv8-internet-draft">We implemented the IPv 8 Internet - Draft in the Linux Kernel, Musl Libc...</a></li>
<li><a href="https://news.ycombinator.com/item?id=49298039">Hey HN, A few weeks ago, the &quot; Internet Protocol...&quot; | Hacker News</a></li>
<li><a href="https://www.linkedin.com/posts/franckmartin_re-ipv8-anyone-can-write-and-publish-an-activity-7450657926991597568-qtCD">IPv 8 Internet Drafts : No Barrier to Entry, but Value is... | LinkedIn</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#IPv8</span> <span class="tag">#Internet-Draft</span> <span class="tag">#Linux Kernel</span> <span class="tag">#BGP</span> <span class="tag">#Networking</span></div>
</article>
<hr>

<a id="item-12"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://depot.dev/blog/tla-verification">使用 TLA+模型检查提升系统安全性</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 15, 05:12</span></div>
<p class="news-summary">Depot 重建了 Depot Registry 的垃圾回收器，并使用 TLA+模型检查器 TLC 对其进行验证。模型检查器发现了一个真实的并发 bug，涉及不对称的引用计数器，而测试和代码审查都未能发现。 这展示了形式化验证在分布式系统中的实用价值，因为稀有交错在大规模下会变成现实。它强调了模型检查如何通过穷举所有可达状态来补充测试的不足，而不仅仅是工程师想象出的执行顺序。 关键不变量 ManifestCountNeverUndercounts 表述为 blobActive =&gt; blobManifestCount &gt;= TrueGlobalManifestCount，体现了多计数可容忍而少计数则违规。模型还包含错误的计数器以使不变量有意义，并且团队使用 S3 bucket versioning，因为启用版本控制而非不可变内容才能保证删除的安全性。</p>
<div class="news-background"><strong>背景</strong> TLA+是由 Leslie Lamport 开发的一种形式化规范语言，用于设计和验证并发及分布式系统。TLC 是一个模型检查器，它探索每个可达状态和每个可能的交错，以检查不变量是否成立。与只运行开发者预期交错的测试不同，模型检查穷举所有可能性，因此在发现罕见并发 bug 方面很有价值。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/TLA+">TLA+ - Wikipedia</a></li>
<li><a href="https://lamport.azurewebsites.net/tla/formal-methods-amazon.pdf">Use of Formal Methods at Amazon Web Services</a></li>
<li><a href="https://web.mit.edu/6.005/www/fa14/classes/17-concurrency/">Reading 17: Concurrency</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#TLA+</span> <span class="tag">#formal verification</span> <span class="tag">#distributed systems</span> <span class="tag">#model checking</span> <span class="tag">#system safety</span></div>
</article>
<hr>

<a id="item-13"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://jkm.dev/posts/how-2004-runescape-fit-a-multiplayer-rpg-into-56k-dialup/">2004 年 RuneScape 如何打造适应 56k 拨号的多人在线协议</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 15, 04:45</span></div>
<p class="news-summary">一篇详细的技术博客对 2004 年 RuneScape 2 客户端进行了逆向工程，揭示游戏如何利用增量压缩和位填充协议设计，在 56k 拨号网络上运行多人在线 3D RPG。文章拆解了诸如 8 位玩家计数和每个玩家 1 个“无变化”位等具体机制，将每个游戏 tick 的带宽压缩到仅几个字节。 这是一次针对极端带宽限制下网络协议设计的高价值历史性深入剖析，为游戏开发者和软件工程师提供了实用经验。这种紧密协同设计、逐位优化的方法仍出现在现代竞技游戏、回滚网络代码和行情数据源中——这些场景里每个字节都至关重要。 该分析基于 2004 年 RuneScape 2 客户端的反编译代码，代码片段经过翻译和整理以增强可读性，但保留了原始逻辑。核心原则是“无变化”仅用一个 0 位表示，带宽只分配给真正移动的玩家，而协议模式由客户端和服务器共享并编译到两端。</p>
<div class="news-background"><strong>背景</strong> 增量编码（即增量压缩）以连续状态之间的差异而非完整文件来传输数据，从而显著降低带宽占用。位填充是一种互补技术，仅为每个数据字段分配所需的最小位数。2004 年时，56k 调制解调器下行速率约为 5 KB/s，上行更低，因此 RuneScape 的客户端和服务器依赖一种严格协同设计的协议，每个字节都要精打细算。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Delta_encoding">Delta encoding - Wikipedia</a></li>
<li><a href="https://python.plainenglish.io/bit-packing-for-efficient-storage-achieving-50-efficiency-in-memory-cfa643ae79fc">Bit Packing for Efficient Storage: Achieving 50% Efficiency in Memory</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#networking</span> <span class="tag">#game development</span> <span class="tag">#protocol design</span> <span class="tag">#RuneScape</span> <span class="tag">#history of tech</span></div>
</article>
<hr>

<a id="item-14"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://davidepiffer.com/p/ai-isnt-outthinking-mathematicians">AI 并非在思维上超越数学家，而是在记忆上超越他们</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">rzk</span><span class="news-time">Aug 15, 18:13</span></div>
<p class="news-summary">一篇文章认为，AI 在数学上的成就源于更强的记忆与检索能力，而非更深的推理，这重新定义了应如何解读 AI 的成功。 若此观点成立，它将挑战人们对机器推理的普遍假设，并影响数学家与 AI 研究者评估大模型输出的方式。它同时提升了 AI 生成的负面结果的价值，而人类数学家很少发表这些结果。 评论者补充说，AI 还能通过永不疲倦来硬算（out-brute-force）胜过人类，并且可以存储和复用失败记录；与之相比，人类数学家因发表激励很少发表负面结果。</p>
<div class="news-background"><strong>背景</strong> 求解数学题的大型语言模型（LLM）在很大程度上依赖从海量训练语料中进行模式匹配与检索，有时还会借助外部记忆或检索增强生成（RAG）技术。在数学中，‘负面结果’（即证明某种方法行不通）对指导后续研究很有价值，但由于期刊和学术聘任更青睐正面成果，这类结果很少被发表。这篇文章由此切入一场旷日持久的争论：基于记忆的行为是否算作真正的推理。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval - augmented generation - Wikipedia</a></li>
<li><a href="https://www.emergentmind.com/topics/memory-augmented-neural-networks">Memory - Augmented Neural Networks</a></li>
<li><a href="https://openai.com/index/ten-advances-in-mathematics/">Ten advances in mathematics and theoretical computer... | OpenAI</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论区大体认同人类的聪明常常源于比他人记得更多，但也补充说 AI 的优势还来自不知疲倦的硬算。有评论者强调 AI 发表负面结果的潜在价值，也有人表示文章有道理但不同意标题。</div>
<div class="news-tags"><span class="tag">#AI</span> <span class="tag">#mathematics</span> <span class="tag">#reasoning</span> <span class="tag">#machine learning</span> <span class="tag">#cognitive science</span></div>
</article>
<hr>

<a id="item-15"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://dmitry.gr/?r=06.%20Thoughts&amp;proj=12.%20RV">RISC-V 的可选特性导致碎片化与兼容性问题</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 14, 19:12</span></div>
<p class="news-summary">Dmitry Grinberg 发表了一篇长篇批评文章，指出 RISC-V 的可扩展性与可选特性会导致不同实现之间的碎片化和兼容性问题。他认为该 ISA 无法同时兼顾高端超算与小型微控制器场景，并预测 RISC-V 最终只会主导低成本微控制器领域。 这篇批评挑战了“RISC-V 凭借开放与灵活将席卷从数据中心到嵌入式所有市场”的说法。兼容性与碎片化问题直接决定 RISC-V 能否成为高性能计算领域 ARM 和 x86 的可信替代品，因此影响深远。 文中详述了具体的 ISA 缺陷，包括可选的 supervisor 模式以及 misa、stvec、mtvec 等 machine 模式 CSR，导致无法可靠检测当前特权级别。文章还援引 Popek &amp; Goldberg 虚拟化要求，认为 RISC-V 的“一切皆可选”设计违背了操作系统和虚拟机监控程序所需的基本假设。</p>
<div class="news-background"><strong>背景</strong> RISC-V 是一种开放指令集架构（ISA），它定义了基础整数指令以及大量可选扩展和特权级别（machine、supervisor、user）。sepc、misa 等控制与状态寄存器（CSR）保存异常程序计数器和 CPU 特性信息，是异常、中断及特权模式检测的基础。由于 RISC-V 将许多特性设为可选，不同实现可能支持不同的 ISA 子集，从而给软件的兼容性和可移植性带来挑战。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RISC-V">RISC - V - Wikipedia</a></li>
<li><a href="https://docs.riscv.org/reference/isa/_attachments/riscv-privileged.pdf">The RISC - V Instruction Set Manual, Volume II: Privileged Architecture</a></li>
<li><a href="https://lupyuen.github.io/articles/privilege">Star64 JH7110 + NuttX RTOS: RISC - V Privilege Levels and UART...</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 评论者大多对这篇批评积极讨论：有人同意 RISC-V 存在缺陷，但称其为“够用”的业余爱好和嵌入式选择；也有人指出 Meta、AMD 和 NVIDIA 的实际成功案例。一个反复出现的反驳观点是，RISC-V 最好被理解为“ISA 生成框架”而非单一固定 ISA，因此一定程度的碎片化是预期且可控的。</div>
<div class="news-tags"><span class="tag">#RISC-V</span> <span class="tag">#ISA</span> <span class="tag">#CPU Architecture</span> <span class="tag">#Open Hardware</span> <span class="tag">#Design</span></div>
</article>
<hr>

<a id="item-16"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.dampfkraft.com/ghost-characters.html">Unicode 的幽灵字符：CJK 编码之谜</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">sensanaty</span><span class="news-time">Aug 15, 14:34</span></div>
<p class="news-summary">文章深入探讨了「彁」这个被编入 JIS 与 Unicode、却始终无法查明出处的日本汉字之谜。它记录了这个『幽灵字符』如何进入标准，以及人们对其真正来源的持续追寻。 这个故事揭示了 CJK 字符编码中隐藏的脆弱性——数字化错误与原始资料丢失可能让错误永久固化在全球标准中。对于依赖 Unicode 进行准确文本处理的语言学家、历史学家和开发者而言，这一问题非常重要。 「彁」这个字符收录于 JIS X 0208 和 Unicode，但没有任何已知出处，是所谓的『幽灵文字』（幽霊文字）之一。评论者指出有证据表明它可能源于某张报纸的劣质扫描，也有人提到类似幽灵字符在 CJK 字符集中大量存在。</p>
<div class="news-background"><strong>背景</strong> 中文、日文和韩文共享一套语素文字，统称为 CJK 字符；Unicode 通过 Han unification（汉字统一）将它们映射为统一字符集。日本 JIS 字符集收录了数千个汉字，其中一些后来被查明无法找到可靠来源，被称为『幽灵文字』。由于 Unicode 继承了这些字符集，这些幽灵字符如今被永久分配了码位。截至 Unicode 17.0，该标准共编码了 101,996 个 CJK 统一表意文字。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CJK_Unified_Ideographs">CJK Unified Ideographs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Han_unification">Han unification</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者对文章及其作者 Paul McCann（polm）表示赞赏，他是日本 NLP 开发者，以 fugashi 分词器封装和一本日文 NLP 著作闻名。还有人提出字符起源的理论，包括报纸劣质扫描，并指出类似幽灵字符在《康熙字典》等来源中大量存在；也有评论开玩笑说可以用幽灵字符表示『无法命名的完全未知概念』。</div>
<div class="news-tags"><span class="tag">#unicode</span> <span class="tag">#cjk</span> <span class="tag">#encoding</span> <span class="tag">#ghost-characters</span> <span class="tag">#technical-deep-dive</span></div>
</article>
<hr>

<a id="item-17"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.technologyreview.com/2026/08/13/1141399/roundtables-inside-the-censorship-industrial-complex-idea-shaping-us-policy/">圆桌讨论：审视影响美国政策的&#x27;审查-工业复合体&#x27;观念</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">MIT Technology Review</span><span class="news-time">Aug 13, 21:00</span></div>
<p class="news-summary">《麻省理工科技评论》于 2026 年 8 月 13 日举办了一场仅面向订阅者的圆桌讨论，探讨&#x27;审查-工业复合体&#x27;这一观念——即政府、科技和研究机构合作压制保守派言论——如何从右翼信息圈进入美国主流政策讨论。 这一讨论之所以重要，是因为&#x27;审查-工业复合体&#x27;的说法正日益影响美国的立法和科技政策，甚至波及立法者与监管机构。它对于言论自由和平台治理的影响，关系到所有互联网用户，而不仅仅是保守派。 这场圆桌讨论录制于 2026 年 8 月 13 日，仅对麻省理工校友和订阅者开放，可收听音频或观看视频。主讲人包括《麻省理工科技评论》运营执行编辑 Amy Nordrum 和特稿与调查高级记者 Eileen Guo。</p>
<div class="news-background"><strong>背景</strong> &#x27;审查-工业复合体&#x27;是一个术语，指一个据称由意识形态一致的政府、非营利组织、媒体、科技、金融和学术机构组成的网络，协作开展审查活动。该说法刻意呼应了美国总统德怀特·艾森豪威尔 1961 年对&#x27;军事-工业复合体&#x27;的警告。多年来，这一观念主要在右翼媒体中流传，但在 2024 年的关键事件以及关于网络言论审核的持续争论之后，它开始进入政策视野。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Censorshipindustrial_complex">Censorship–industrial complex</a></li>
<li><a href="https://overcentral.com/en/censorship-industrial-complex-internet-policy/">Censorship - Industrial Complex Changes Internet and US Policy</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#censorship</span> <span class="tag">#US policy</span> <span class="tag">#internet freedom</span> <span class="tag">#tech policy</span> <span class="tag">#democracy</span></div>
</article>
<hr>

<a id="item-18"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://arstechnica.com/ai/2026/08/openai-and-anthropic-in-price-war-as-chinese-ai-rivals-gain-ground/">OpenAI 和 Anthropic 降价应对中国 AI 对手崛起</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Ars Technica AI</span><span class="news-time">Aug 14, 14:27</span></div>
<p class="news-summary">OpenAI 将其最快且最实惠的模型 GPT-5.6 Luna 的价格下调了 80%，而 Anthropic 推出的 Claude Opus 5 定价仅为该公司最强模型 Fable 5 的一半。根据 Silicon Data 的 token 价格指数，自 7 月中旬以来，客户为美国领先实验室模型支付的价格已下降近四分之一。 这场价格战表明，来自 DeepSeek 和 Moonshot 等实验室的更便宜且能力日益增强的开源权重中国模型，正迫使美国领先 AI 公司在成本而非仅仅是性能上展开竞争。这种压力对关注 AI 账单上升的企业客户，以及对寻求万亿美元 IPO 估值的 OpenAI 和 Anthropic 都很重要。 Silicon Data 的 token 价格指数追踪客户为美国领先实验室模型支付的价格，该指数自 7 月中旬以来已下跌近四分之一。DoorDash 和 Airbnb 等公司已开始使用中国制造的模型来控制成本，同时 OpenAI 和 Anthropic 正将部分企业客户从固定订阅转向按用量计费。</p>
<div class="news-background"><strong>背景</strong> Token 是语言模型处理的数据单位，常用于计算许多客户的账单。DeepSeek 等中国实验室成立于 2023 年，发布开源权重的大型语言模型，开发者可以自由下载和修改，其训练成本据报道仅为美国领先模型的一小部分；Moonshot AI 是一家总部位于北京的人工智能公司，也是中国“AI 六虎”之一。这些开源模型缩小了与美国专有闭源模型的性能差距，同时价格低得多，加剧了 OpenAI 和 Anthropic 面临的竞争压力。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek</a></li>
<li><a href="https://en.wikipedia.org/wiki/Moonshot_AI">Moonshot AI</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI</span> <span class="tag">#OpenAI</span> <span class="tag">#Anthropic</span> <span class="tag">#Chinese AI</span> <span class="tag">#pricing</span></div>
</article>
<hr>

<a id="item-19"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.theverge.com/ai-artificial-intelligence/980160/apple-intelligence-china-custom-ai-model-alibaba">苹果携手阿里为中国定制训练 AI 模型</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">The Verge AI</span><span class="news-time">Aug 14, 09:21</span></div>
<p class="news-summary">据报道，苹果在阿里巴巴的支持下训练了一个面向中国的定制大语言模型，这一消息来自路透社。此举标志着苹果改变了此前在中国使用本土模型提供生成式 AI 功能的策略。 这将使苹果成为首家获准在中国提供自有专有 AI 模型的美国公司，在全球最大的智能手机市场占据重要竞争优势。这也表明美国科技公司必须在美中关系紧张之际应对北京严格的 AI 监管。 上个月，苹果已向中国网信部门正式注册其端侧生成式 AI 服务，扫清了一项重大监管障碍。据报道，面向中国的定制模型让苹果对产品拥有更大控制权，消息人士称 Apple Intelligence 将在 iOS 系统更新后的数月内于中国上线。</p>
<div class="news-background"><strong>背景</strong> Apple Intelligence 是苹果的个人智能系统，由 Apple Foundation Models 驱动，可在 iPhone、iPad、Mac 等设备上实现个人上下文理解与屏幕感知。在中国，OpenAI 的 ChatGPT 等外国 AI 模型不可用，且 AI 模型在公开发布前必须向政府注册并通过审核，因此苹果此前依赖中国本土模型。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.apple.com/apple-intelligence/">Apple Intelligence and Siri - Apple</a></li>
<li><a href="https://developer.apple.com/apple-intelligence/">Apple Intelligence - Apple Developer</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Apple</span> <span class="tag">#AI</span> <span class="tag">#Alibaba</span> <span class="tag">#China</span> <span class="tag">#partnership</span></div>
</article>
<hr>

<a id="item-20"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.pcworld.com/article/3212428/firefox-is-now-the-last-major-browser-that-still-supports-ublock-origin.html">Firefox 成为最后一个支持 uBlock Origin 的主流浏览器</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 15, 05:08</span></div>
<p class="news-summary">Firefox 重申了对 uBlock Origin 的支持，并通过 Bluesky 发文表示这种支持不会消失。与此同时，Microsoft Edge 正准备淘汰 Manifest V2 扩展，这将导致 uBlock Origin 等广告拦截扩展被禁用。 随着 Edge 和其他 Chromium 浏览器转向 Manifest V3，Firefox 成为唯一一个能运行 uBlock Origin 等功能完整广告拦截扩展的主流浏览器。这对注重隐私的用户以及保持浏览器生态的竞争性和多样性具有重要意义。 Firefox 并非基于 Chromium，而 Edge、Opera、Brave、Vivaldi 和 Samsung Browser 等其他大多数浏览器都是。Safari 和 DuckDuckGo 也不支持 uBlock Origin，因此对于希望无妥协使用这款广告拦截扩展的用户来说，Firefox 实际上是唯一选择。</p>
<div class="news-background"><strong>背景</strong> uBlock Origin 是一款免费、开源、以低 CPU 和内存占用著称的广告拦截及内容拦截扩展。Chromium 系浏览器转向 Manifest V3 这一新的扩展规范，旨在提升隐私、安全和性能，但限制了广告拦截扩展的功能。Firefox 在支持 Manifest V3 的同时，仍继续支持较旧的 Manifest V2 扩展，因此 uBlock Origin 能够继续运行。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UBlock_Origin">uBlock Origin - Wikipedia</a></li>
<li><a href="https://ublockorigin.com/">uBlock Origin - Free, open-source ad blocker extension</a></li>
<li><a href="https://developer.chrome.com/docs/extensions/develop/migrate/what-is-mv3">Extensions / Manifest V 3 | Chrome for Developers</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Firefox</span> <span class="tag">#uBlock Origin</span> <span class="tag">#Manifest V3</span> <span class="tag">#ad-blocking</span> <span class="tag">#browsers</span></div>
</article>
<hr>

<a id="item-21"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://serokell.io/blog/serokell-s-work-on-ghc-dependent-types-part-5">Serokell 在第五部分中重点介绍 GHC 依赖类型进展</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 15, 10:42</span></div>
<p class="news-summary">Serokell 的 GHC 团队发布了其关于在 Haskell 中实现依赖类型的系列报告的第五部分，重点介绍了三项主要贡献：GADT 中的可见 forall、命名空间指定的导入，以及种类检查中的类型实例。报告还描述了较小的改进，包括 HsType 和 HsExpr 的统一、新的类型族，以及四个名称解析错误的修复。 这些编译器改动使 Dependent Haskell 更接近实用化，为 Haskell 生态系统中更具表现力的类型级编程提供了支持。种类检查中类型实例排序的长期修复解决了一类影响依赖种类类型族的声明顺序错误。 该报告引用了 GHC Proposal #378「Design for Dependent Types」及其量词表，包括依赖积 foreach a -&gt; ty。报告还列出了五个类型族（Tuple、Constraints、Tuple#、Sum#），以及四个与 Template Haskell 和内建语法处理相关的已修复错误（#25174、#25179、#25180、#25182）。</p>
<div class="news-background"><strong>背景</strong> 依赖类型允许类型依赖于值，从而提供更强的编译时保证。Haskell 的 GHC 编译器正在逐步实现 Dependent Haskell 的设计，这涉及通过新的量词扩展类型系统并统一表达式和类型语法。GHC 提案流程指导这些更改，社区通过错误报告和设计讨论跟踪进展。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://serokell.io/blog/why-dependent-haskell">Why Dependent Haskell is the Future of Software Development</a></li>
<li><a href="https://github.com/ghc-proposals/ghc-proposals/discussions/663">Merging HsExpr , HsType , and Pat · ghc -proposals ghc -proposals...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Haskell</span> <span class="tag">#GHC</span> <span class="tag">#Dependent Types</span> <span class="tag">#Type Systems</span> <span class="tag">#Compiler</span></div>
</article>
<hr>

<a id="item-22"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://o.ee/blog/activitypub-won-by-being-boring/">ActivityPub 因“无聊”而胜出</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 14, 18:44</span></div>
<p class="news-summary">在一篇配合 Evan Prodromou 在 FediForum 2026 的演讲《如何在一场关于 ActivityPub 的对话中胡说八道》的文章中，作者认为 ActivityPub 之所以胜出，是因为它有意保持平淡无奇——把联邦化当作普通的 Web 管道设施，而不是追求精巧的架构。这篇文章称赞该协议“仅就交换活动数据达成最小共识”的设计，是 Fediverse 得以成长的关键。 这很重要，因为它解释了为什么 ActivityPub 能成为去中心化社交网络的事实标准，而其他协议却举步维艰。它把该协议看似“平庸”的特质描述为一种优势：最小化共识促成了开放性、defederation 和渐进式演进，这对任何构建或选择去中心化系统的人都有借鉴意义。 文章指出，ActivityPub 是基于 ActivityStreams 2.0 的 W3C 推荐标准，由包括 Prodromou 在内的五人编写，并且刻意不规定审核方式、界面、排序或产品类别。它把“联合屏蔽”（defederation）视为该协议应对滥用的主要防御手段，并勾勒了未来的工作方向——签名、隐私、可迁移性、商业规模——最终走向一个像 HTTP 那样向后兼容的 ActivityPub 2.0。</p>
<div class="news-background"><strong>背景</strong> ActivityPub 是 W3C 标准化的开放、去中心化社交网络协议，首个版本于 2018 年发布。Fediverse（联邦宇宙）是一个由相互连接的服务器（如 Mastodon）组成的全球网络，通过这些平台使用 ActivityPub 进行跨平台通信。该协议通过 ActivityStreams 2.0 格式标准化了活动数据（如 Create、Like、Follow）的交换，而把审核、政策和用户体验留给各个实例自行决定。这种“最小可行共识”正是文章所说的“无聊”，但它被证明足以支撑一个不断壮大的生态系统。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://o.ee/blog/activitypub-won-by-being-boring/">ActivityPub Won by Being Boring - Owl Owl OÜ</a></li>
<li><a href="https://allthingsopen.org/articles/activitypub-explained-the-protocol-connecting-the-fediverse">ActivityPub explained: The protocol connecting the Fediverse</a></li>
<li><a href="https://www.theverge.com/24063290/fediverse-explained-activitypub-social-media-open-protocol">The fediverse , explained : Mastodon, Threads, and the... | The Verge</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#ActivityPub</span> <span class="tag">#Fediverse</span> <span class="tag">#Decentralization</span> <span class="tag">#Protocol Design</span> <span class="tag">#Social Web</span></div>
</article>
<hr>

<a id="item-23"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://gist.github.com/camel-cdr/3a7aed17e017e8cab675ad696c7d14af">RVA23 对比 ARMv9：指令数与代码密度小实验</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 15, 00:42</span></div>
<p class="news-summary">作者使用 chibicc C 编译器设计了一个实验，通过 QEMU 和 GEM5 对比 RISC-V RVA23 与 ARMv9 的动态指令数和代码密度。结果显示 ARM 需要解码的指令更少，而 RISC-V 需要取指的字节更少；在禁用向量扩展时，RVA23 相比 RVA22 几乎没有优势。 这项实验为两大主流 ISA 之间的实际差异提供了具体、可量化的数据，帮助开发者理解代码密度、指令数与微操作拆分之间的权衡。同时它也表明，RVA23 的主要差异化特性 RVV 在标量负载中尚未被充分利用。 RISC-V 静态二进制体积比 ARM 小约 18%，但 ARM 平均少 6.5% 的动态指令。作者修改了 QEMU 的 tcg/plugins/insn.c 插件来统计取指字节数，因为原生 QEMU 不具备此功能。实验排除了 SIMD 代码，并使用来自 musl-libc 的未优化标量 mem*/str* 实现。</p>
<div class="news-background"><strong>背景</strong> RVA23 是最新的 RISC-V 应用配置文件，强制加入向量扩展（RVV）等特性，旨在为高性能 64 位芯片奠定坚实基础。ARMv9 是 ARM 当前的架构世代，具备 SVE2 及安全/性能相关特性。chibicc 是一个小型 C11 编译器，常被用作教学工具。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://riscv.org/blog/risc-v-rva23-a-major-milestone/">RISC - V RVA 23 —A Major Milestone - RISC - V International</a></li>
<li><a href="https://github.com/rui314/chibicc">GitHub - rui314/ chibicc : A small C compiler · GitHub</a></li>
<li><a href="https://llvm.org/docs/RISCV/RISCVVectorExtension.html">RISC - V Vector Extension - LLVM</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#RISC-V</span> <span class="tag">#ARM</span> <span class="tag">#ISA</span> <span class="tag">#compiler</span> <span class="tag">#QEMU</span></div>
</article>
<hr>

<a id="item-24"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://cekrem.github.io/posts/there-is-still-no-silver-bullet/">软件工程无银弹，40 年后依然如此</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 14, 15:18</span></div>
<p class="news-summary">这篇发表在 cekrem.github.io 上的文章认为，弗雷德·布鲁克斯 1986 年的“没有银弹”预言至今依然正确，即使 AI 编码工具获得了巨额投资。文章指出，AI 主要压缩的是偶然复杂度，而本质复杂度仍然是真正的瓶颈。 这一论点很重要，因为它挑战了“编码即将完全自动化”的主流 AI 炒作，而这种炒作推动了数千亿美元的投资。它将 AI 重新定位为处理软件开发中的“偶然”部分而非“本质”部分，因此需求分析、设计和工程判断仍然至关重要。 作者明确反对“代码从来不是难点”的说法，认为这曲解了布鲁克斯并侮辱了程序员，并指出行业二十年来一直在寻找“10 倍忍者摇滚明星”程序员，且积累了丰富的技艺文献。文章还提到 METR 2026 年 2 月的后续研究，其中迹象转向加速但统计上不具结论性，部分原因是 30–50% 的开发者承认会保留那些他们认为 AI 能赢的任务。</p>
<div class="news-background"><strong>背景</strong> 弗雷德·布鲁克斯 1986 年的论文《没有银弹：软件工程中的本质与偶然》区分了本质复杂度（概念构造：需求、设计、规格说明）和偶然复杂度（将其实现为代码的劳动）。布鲁克斯预测，没有任何单一技术或管理方法能在十年内使生产力、可靠性或简单性提高一个数量级。本文将该区分应用于 AI 辅助开发：AI 可以自动化语法和常规编码，但无法消除决定构建什么的硬性概念工作。这篇论文已成为关于现代 AI 工具能否真正解决软件工程问题的辩论中的一块试金石。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/No_Silver_Bullet">No Silver Bullet - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/The_Mythical_Man-Month">The Mythical Man-Month - Wikipedia</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#software engineering</span> <span class="tag">#AI</span> <span class="tag">#Fred Brooks</span> <span class="tag">#essay</span> <span class="tag">#complexity</span></div>
</article>
<hr>

<a id="item-25"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://daniel.haxx.se/blog/2026/08/14/curl-performance-2/">curl 项目推出实时性能页面以追踪性能回退</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 14, 11:33</span></div>
<p class="news-summary">curl 维护者 Daniel Stenberg 在 curl.se/perf 推出了实时性能页面，并引入了 curl 的性能测试套件。该页面跟踪基准测试结果，并通过手动设置的“stakes”阈值来帮助发现性能回退。 性能回退在 curl 这样广泛使用的 HTTP 客户端中历来难以检测，而这一举措为项目提供了一种持续、可见的方式来捕捉细微的性能下降。它也让开发者和下游用户能够了解 curl 性能随时间和不同环境的演变情况。 测试结果高度依赖具体的机器、第三方库版本和测试服务器，因此这些数值最适合用于短期回归检测。Stenberg 指出，“stakes”是按测试手动设置的阈值，可在条件变化时进行调整，目前大多数测试由 Stefan Eissing 编写。</p>
<div class="news-background"><strong>背景</strong> curl 是一个用于通过 URL 传输数据的命令行工具和库，支持 HTTP、HTTPS、FTP 等协议。对这类项目进行性能测试很困难，因为结果会因硬件、库和环境而异，团队曾多次考虑构建性能测试套件，但都因挑战太大而搁置。Stenberg 选择了一种务实的方式，一步步构建该系统，而非采用 Grafana 这类他认为过于复杂的完整监控方案。</div>
<div class="news-discussion"><strong>社区讨论</strong> 在评论中，@Moritz 询问了历史性能数据，Stenberg 回复说旧的第三方库通常无法与旧版 curl 兼容，投入大而收益小。@Nick 建议对过去的提交反向运行测试以发现被遗漏的回退；Stenberg 表示代码是开放的，鼓励任何人尝试，但这并非他目前的重点。</div>
<div class="news-tags"><span class="tag">#curl</span> <span class="tag">#performance</span> <span class="tag">#benchmarking</span> <span class="tag">#regression testing</span></div>
</article>
<hr>

<a id="item-26"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://arxiv.org/abs/2604.04902">潜在推理模型比预期更可解释</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Aug 15, 16:17</span></div>
<p class="news-summary">一篇新的 arXiv 预印本（v2，2026 年 8 月 10 日修订）研究了两个最先进的潜在推理模型，发现在逻辑推理数据集上，潜在推理 token 通常对预测并非必要。当 token 必要时，对于正确预测的实例，有 65%–93%的情况可以解码出金标准推理轨迹。 这挑战了关于潜在推理模型本质上不透明且难以监控的普遍假设。证明可解释性可以预示预测正确性，可能提升黑盒推理系统的安全性与调试能力。 作者表明，LRM 通常可以在不使用潜在推理 token 的情况下产生相同的最终答案，这使先前工作中这些 token 的作用受到质疑。他们还提出一种方法，无需预先知道金标准推理轨迹即可解码出经过验证的自然语言推理链，该方法在多数正确预测上成功，但在少数错误预测上也能成功。</p>
<div class="news-background"><strong>背景</strong> 潜在推理模型（LRM）在模型的连续隐藏状态中执行多步推理，而不是生成自然语言推理步骤，这降低了推理成本但使监控变得更加困难。相比之下，显式推理模型会生成透明的、逐步的思维链。本文以逻辑推理数据集为测试平台，研究 LRM 虽不以自然语言推理，是否仍具有可解释性。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2507.06203">A Survey on Latent Reasoning</a></li>
<li><a href="https://grokipedia.com/page/Scaling_Latent_Reasoning_via_Looped_Language_Models">Scaling Latent Reasoning via Looped Language Models</a></li>
<li><a href="https://ajithp.com/2025/02/14/latent-reasoning-the-next-evolution-in-ai-for-scalable-adaptive-and-efficient-problem-solving/">Latent Reasoning in AI: The Future of Scalable Problem-Solving</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#interpretability</span> <span class="tag">#machine learning</span> <span class="tag">#reasoning models</span> <span class="tag">#AI safety</span></div>
</article>
<hr>