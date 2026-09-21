---
layout: default
title: "Horizon 每日速递：2026-09-21"
date: 2026-09-21
lang: zh
---

> 📅 2026-09-21 · 从 84 条资讯中精选出 30 条重要内容

---

1. [小米发布 MiMo\-V2\.6 开源权重模型系列](#item-1) <span class="score-badge score-mid">8.0</span>
2. [Bryan Cantrill 谈 Sun Microsystems 究竟错在哪里](#item-2) <span class="score-badge score-mid">8.0</span>
3. [xAI 发布 Grok 4\.7，引发价格与基准测试之争](#item-3) <span class="score-badge score-mid">8.0</span>
4. [Cloudflare Python Workers 结束两年预览，正式 GA](#item-4) <span class="score-badge score-mid">8.0</span>
5. [Hugging Face 发布 tokenizers v1：大幅提升编码、解码与规模化性能](#item-5) <span class="score-badge score-mid">8.0</span>
6. [Meta 的 Muse AI 助手曝 0\-day 漏洞，可导致账户被完全接管](#item-6) <span class="score-badge score-mid">8.0</span>
7. [谷歌分析师卧底潜入 TeamPCP 供应链黑客团伙](#item-7) <span class="score-badge score-mid">8.0</span>
8. [Nathan Lambert 谈开放权重模型与美中竞争](#item-8) <span class="score-badge score-mid">8.0</span>
9. [OpenAI 的 \_\_obi cookie 将 ChatGPT 账号与第三方网站浏览行为关联起来](#item-9) <span class="score-badge score-mid">8.0</span>
10. [Project Zero 详解 Windows 悬空 COM 注册提权漏洞](#item-10) <span class="score-badge score-mid">8.0</span>
11. [NASA 火星采样返回任务实质上被取消](#item-11) <span class="score-badge score-mid">7.0</span>
12. [交互式可视化讲解器拆解 GPT\-2 Transformer 内部机制](#item-12) <span class="score-badge score-mid">7.0</span>
13. [随笔《注意力是你仅有的资源》：应用如何劫持注意力](#item-13) <span class="score-badge score-mid">7.0</span>
14. [AI 编程代理让 CI 成为瓶颈，Linear 重做其 CI 流水线](#item-14) <span class="score-badge score-mid">7.0</span>
15. [Kev：基于 Qwen3\.5 构建的微型“类 Jev”决策模型](#item-15) <span class="score-badge score-mid">7.0</span>
16. [光纤线路中断，FAA 暂停美国东海岸繁忙机场航班](#item-16) <span class="score-badge score-mid">7.0</span>
17. [Heretic 自动化移除开源权重语言模型的审查机制](#item-17) <span class="score-badge score-mid">7.0</span>
18. [TypeSafe AI 推出 Jev：Simon Willison 解析全新 “System One” 决策模型](#item-18) <span class="score-badge score-mid">7.0</span>
19. [Simon Willison 引用一则由 Claude Code 主导团队的一线描述](#item-19) <span class="score-badge score-mid">7.0</span>
20. [Simon Willison：MCP 对受管制的托管型 agent 仍有价值](#item-20) <span class="score-badge score-mid">7.0</span>
21. [Multiverse 将 LLM 块剪枝重构为 Ising 优化问题](#item-21) <span class="score-badge score-mid">7.0</span>
22. [调查：AI 边境监控塔未能阻止移民死亡](#item-22) <span class="score-badge score-mid">7.0</span>
23. [联合国科学小组：AI 保障措施不能等待科学确定性](#item-23) <span class="score-badge score-mid">7.0</span>
24. [亚马逊以「未授权访问」为由封禁 Meta 的 Muse AI 购物代理](#item-24) <span class="score-badge score-mid">7.0</span>
25. [Rift：面向 macOS 的全新多布局平铺窗口管理器](#item-25) <span class="score-badge score-mid">7.0</span>
26. [relation algebra 与 relational algebra：两个易混淆形式系统的辨析](#item-26) <span class="score-badge score-mid">7.0</span>
27. [Anish Athalye 发布 Optimal Trace 路线规划工具](#item-27) <span class="score-badge score-mid">7.0</span>
28. [开发者用同一套 C 代码同时打造 GBA、e\-Reader 与 PC 游戏](#item-28) <span class="score-badge score-mid">7.0</span>
29. [博主详解如何在 NixOS 上用 GoatCounter 搭建无机器人的自托管分析](#item-29) <span class="score-badge score-mid">7.0</span>
30. [Lambda MicroEgg 为 e\-graph 加入 alpha 感知的绑定器](#item-30) <span class="score-badge score-mid">7.0</span>

---

<a id="item-1"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://mimo.xiaomi.com/mimo-v2-6">小米发布 MiMo-V2.6 开源权重模型系列</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">volf_</span><span class="news-time">Sep 21, 20:12</span></div>
<p class="news-summary">小米正式发布并开源了 MiMo-V2.6 系列，包含 Flash（总参数 309B、激活参数 15B）和 Pro（总参数 1.02T、激活参数 42B）两个版本。此次发布还附带了异常详尽的技术报告，以及小米在训练期间公开分享的实时训练仪表盘。 这表明推出前沿级开源权重模型的不只是专业 AI 实验室，也包括大型消费硬件厂商，进一步强化了中国团队在开源权重发布上的领先格局。对从业者而言，可自由获取的权重加上官方强调的低成本定位，可能降低部署高性能模型的门槛。 两个版本均采用 Mixture-of-Experts（专家混合）架构，并使用混合注意力机制以提升计算效率，官方模型卡以「扩展强化学习以实现自我改进」为核心主题。在一位评论者的图像转 HTML 测试中，MiMo 2.6 Pro Ultraspeed 被评判为三者中整体效果最弱，但仍被形容为速度很快，耗时 36 分钟，而 Grok 4.7 为 25 分钟、Astra 为 19 分钟。</p>
<div class="news-background"><strong>背景</strong> 开源权重模型指的是将训练好的参数公开发布的 AI 模型，任何人都可以下载、运行、微调或部署，但具体的修改与再分发权限取决于许可证。它与完全开源的 AI 不同，后者还会公开源代码、训练数据、中间检查点和评测结果。DeepSeek、阿里云、Moonshot AI、Z.ai 等中国团队大多以开源权重方式、采用 Apache 或 MIT 等宽松许可证发布模型，而美国主要实验室则倾向于让较大模型保持闭源。Mixture-of-Experts 是一种每个 token 只激活部分参数的设计，因此模型可以拥有数千亿总参数，却在推理时只激活其中很小一部分。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://mimo.xiaomi.com/mimo-v2-6">MiMo - V 2 . 6 | Xiaomi</a></li>
<li><a href="https://mimo.mi.com/docs/en-US/news/latest/v2-6">Xiaomi MiMo Home</a></li>
<li><a href="https://openrouter.ai/xiaomi/mimo-v2.6-flash">MiMo - V 2 . 6 -Flash - API Pricing &amp; Providers | OpenRouter</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 上的讨论整体对透明度评价积极：一位评论者称公开的实时训练仪表盘是极佳的学习与教学工具，并称赞技术报告内容全面；另一位则表示相比美国模型，他对中国模型更感兴趣，理由是价格实惠。其他人则提供了具体对比——参数量、pelican 渲染测试，以及一项图像转 HTML 基准，其中 MiMo Pro 的评分低于 Grok 4.7 和 Astra——讨论还涉及何为「真正开放模型」的长期争论。</div>
<div class="news-tags"><span class="tag">#LLM</span> <span class="tag">#open-weights</span> <span class="tag">#Xiaomi</span> <span class="tag">#model-release</span> <span class="tag">#AI/ML</span></div>
</article>
<hr>

<a id="item-2"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://bcantrill.dtrace.org/2026/09/20/what-sun-got-wrong/">Bryan Cantrill 谈 Sun Microsystems 究竟错在哪里</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Sep 21, 07:14</span></div>
<p class="news-summary">Bryan Cantrill 在其 dtrace.org 博客上发表了一篇回顾性文章，认为 Sun 最根本的失败在于它“已经厌倦了经营企业的那套机制”。他用 2005 年的一个例子加以说明：一家基于 OpenSolaris 运行基础设施的高速成长创业公司想要采购 Sun 的硬件，却根本联系不上 Sun，而 Dell 的本地客户经理当晚就作出回应，并在不到两周内完成了服务器的租赁与交付。 这篇文章把 Sun 的历史变成给当今硬件与系统公司（包括 Cantrill 自己创办的 Oxide）的一堂警示课：再出色的战略或技术，也无法弥补在销售、服务与运营执行上的疏忽。它还在 Hacker News 上引发了大量讨论，工程师们分享了在 Sun、DEC 与 Dell 时代采购企业级硬件的亲身经历。 Cantrill 指出，他依然认同自己 2011 年在 Hacker News 评论中给出的分析，但 15 年后他会把结论进一步浓缩为“对经营企业失去兴趣”这一个核心问题。文章结尾的一个细节颇具意味：离开 Sun 后，他加入了那家 Sun 未能服务好的创业公司，而这家公司后来还雇用了 Dell 的“Steve”——也就是 Cantrill 最终与之共同创办 Oxide 的那位销售。</p>
<div class="news-background"><strong>背景</strong> Sun Microsystems 是工作站与服务器领域的先驱厂商，以 SPARC 处理器、Solaris 操作系统和 Java 闻名；它在 2000 年代中期将 Solaris 以 OpenSolaris 之名开源，并最终于 2010 年被 Oracle 收购。由 Cantrill 参与共同创办、总部位于加州 Emeryville 的 Oxide Computer Company 打造的是机架级、垂直整合的本地云（on-premises cloud）产品，并正在举办其一年一度的线下团队聚会 OxCon；根据 Intel Capital 的信息，Oxide 于 2026 年 2 月宣布完成 2 亿美元的 C 轮融资。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.intelcapital.com/oxide-closes-200m-series-c-to-scale-on-premises-cloud-computing/">Oxide Closes $200M Series C to Scale On-Premises Cloud Computing – Intel Capital</a></li>
<li><a href="https://www.linkedin.com/company/oxidecomputer">Oxide Computer Company | LinkedIn</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者大多认同这一诊断，并进一步补充细节：有人回忆说在 1990 年代末向 Sun 或 DEC 采购，意味着必须参加现场销售会议、反复修改报价，而一台 Alpha 服务器的导轨和电源线，价格甚至超过次日即可送达的整台 Dell 服务器。另有人列举了 Sun 的具体失误，包括 2002 年短暂取消 x86 版 Solaris，以及因坚持要求 Google 透露其服务器数量而错失 2002 年与 Google 的交易。还有人不同意这一框架，认为 Sun 从来就对经营企业毫无兴趣，它真正在意的始终是打造技术。</div>
<div class="news-tags"><span class="tag">#Sun Microsystems</span> <span class="tag">#industry-analysis</span> <span class="tag">#hardware</span> <span class="tag">#systems-history</span> <span class="tag">#Hacker News</span></div>
</article>
<hr>

<a id="item-3"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://x.ai/news/grok-4-7">xAI 发布 Grok 4.7，引发价格与基准测试之争</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">meetpateltech</span><span class="news-time">Sep 21, 15:50</span></div>
<p class="news-summary">xAI 发布了 Grok 4.7，这是在 Grok 4.6 基础上的版本更新，随即在 Hacker News 上引发大规模讨论（458 分、373 条评论）。所提供的材料中并未包含官方公告的具体内容，因此 xAI 对该模型的具体说法在此无法核实。 头部实验室每一次新前沿模型的发布，都会改变开发者对各家 API 的取舍，尤其是在价格、延迟与能力权衡发生变化时。这条消息之所以重要，是因为评论者将其视为对竞争压力的回应，也将其看作判断下一代竞品模型成色的参照。 据评论者称，Grok 4.7 的参数规模比 Grok 4.6 大约多 40%，但价格维持不变，即每百万输入 token 2 美元、每百万输出 token 6 美元，同时有用户表示实际使用时它更慢、更贵。评论者 simonw 分享了不同 reasoning 等级下的 token 用量测试，指出 low 和 medium 使用的 token 数相近，而 xhigh 反而比 high 更少，并表示希望在没有 OpenRouter 中转的情况下重新测试后再下结论。</p>
<div class="news-background"><strong>背景</strong> Grok 是 xAI 开发的大语言模型系列，4.6 与 4.7 这类发布属于版本迭代，而非全新的模型代际。前沿模型通常通过公开基准测试进行比较，但许多开发者已开始怀疑这些分数对真实使用表现的预测能力。这类模型的 API 定价一般按每百万 token 计费，并区分为输入 token（提示词）和输出 token（生成文本），而 OpenRouter 之类的服务让开发者可以通过统一接口把请求路由到众多模型。部分模型还提供可调节的 reasoning effort 设置，用来控制模型在作答前消耗多少 token 进行思考。</div>
<div class="news-discussion"><strong>社区讨论</strong> 整体情绪褒贬不一且偏怀疑：评论者质疑 xAI 的发布时机与商业逻辑，认为发布时间比原计划晚了近两周、参数规模增加 40% 却维持原价，说明 xAI 对 4.7 的结果并不完全满意，并有意抢在传闻中的 Opus 5.5 发布前一天推出。多位用户反映 Grok 4.7 在编码和智能体工作流中比预期更慢、更贵，也有人对基准测试本身表示怀疑，并期待今年晚些时候的 Grok 5 能带来更大跃升。</div>
<div class="news-tags"><span class="tag">#AI/ML</span> <span class="tag">#LLM</span> <span class="tag">#Grok</span> <span class="tag">#xAI</span> <span class="tag">#model release</span> <span class="tag">#benchmarks</span></div>
</article>
<hr>

<a id="item-4"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://blog.cloudflare.com/python-workers-ga/">Cloudflare Python Workers 结束两年预览，正式 GA</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">torutofu</span><span class="news-time">Sep 21, 13:38</span></div>
<p class="news-summary">Cloudflare 宣布其无服务器边缘平台上的 Python Workers 正式进入 general availability（GA），此前已预览约两年，并将 Python 称为「Cloudflare Developer Platform 上的一等公民、受完整支持的语言」。此次发布强调了改进的包支持、让主流 HTTP 客户端在 WebAssembly 环境中可直接通过 JavaScript fetch API 发起请求的上游贡献，以及围绕 Pyodide/Emscripten 与 PEP 783 的标准化工作。 让 Python 成为 Workers 上稳定受支持的语言，降低了庞大的 Python 开发者群体使用边缘无服务器基础设施的门槛，无需离开自己熟悉的语言。这也说明 Python-on-WebAssembly 工具链正在成熟——这项能力依赖 Pyodide、Emscripten、urllib3 等项目的上游改动，而非仅靠 Cloudflare 自己的补丁。 据公告所述，Cloudflare 向上游提交了贡献，使常见的 Python HTTP 客户端在 WebAssembly 环境中可直接通过 JavaScript fetch API 发起请求，同时 PyEmscripten 正通过 PEP 783 进行标准化。社区评论者询问 Workers 当前运行的 Pyodide 版本（有人提到上次查看时为 0.28.x），并质疑冷启动性能——这历来是基于 WebAssembly 的 Workers 的一项权衡。</p>
<div class="news-background"><strong>背景</strong> Cloudflare Workers 是一个无服务器平台，在 Cloudflare 边缘网络的 V8 运行时 workerd 中执行代码。由于该运行时执行的是 JavaScript 而非原生 Python 解释器，Cloudflare 选择运行编译为 WebAssembly 的 Python，借助社区项目 Pyodide——它通过 Emscripten 将 CPython 移植到 WebAssembly，并支持纯 Python 包以及许多带 C 扩展的包。WebAssembly 是一种可移植的二进制格式，2019 年成为 W3C 正式推荐标准，可让 Python 等语言被编译后运行在本非为其设计的运行环境中。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://pyodide.org/">Pyodide — Version 314.0.7</a></li>
<li><a href="https://github.com/pyodide/pyodide">GitHub - pyodide/pyodide: Pyodide is a Python distribution ... Pyodide — Version 314.1.0.dev0 Home - Pyodide About Us - Pyodide Pyodide - GitHub pyodide | Pyodide is a Python distribution for the browser ...</a></li>
<li><a href="https://webassembly.org/">WebAssembly</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 的讨论既有赞誉也有审视：一位 urllib3 维护者补充背景称，合并进 urllib3 的 Pyodide/Emscripten 支持以及后来的 JSPI 支持来自一笔大型外部贡献，资金给了实现该贡献的外部贡献者而非维护者；而竞品 Wasmer 的创始人则称这些进展很有意义，尤其是 PEP 783 标准化，但也指出仍存在架构层面的担忧。其他人提出了关于所用 Pyodide 版本和冷启动时间的具体问题，还有评论者开玩笑说把标题误读成了 Cloudflare 用 AI 取代了所有 Python 程序员并把他们「放出来」了。</div>
<div class="news-tags"><span class="tag">#Cloudflare Workers</span> <span class="tag">#Python</span> <span class="tag">#WebAssembly</span> <span class="tag">#Pyodide</span> <span class="tag">#Serverless</span></div>
</article>
<hr>

<a id="item-5"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://huggingface.co/blog/tokenizers-v1">Hugging Face 发布 tokenizers v1：大幅提升编码、解码与规模化性能</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Hugging Face Blog</span><span class="news-time">Sep 21, 00:00</span></div>
<p class="news-summary">Hugging Face 发布了 tokenizers v1，博文中称其为 release candidate，重点放在性能上，并称其相对 v0.23 “常常快上数十倍”。文章展示了 v1 release candidate 与其他常用 tokenizer 实现的基准测试结果，并详细介绍了重写的 BPE merge loop、prefix-sharing 缓存以及一套重构后的语言绑定。 tokenizers 是 Hugging Face Transformers 所使用的分词库，在 NLP 训练与推理流程中应用广泛，因此编码/解码速度的大幅提升会直接影响模型能拿到多少数据。作者把动机表述为避免分词成为 CPU 瓶颈、让 GPU 空转，这对在超大数据集上训练或需要同时服务大量并发请求的团队尤为重要。 新的 BPE merge loop 复用由调用方持有的 scratch buffer 而非每次调用都分配内存，把 symbol 存放在平坦数组中并用位置建立相邻链接，在单次模型调用中批量处理多个 pre-token，并把每个候选 pair 打包成一个 64 位值、把 merge rank 放在高位，从而使比较退化为整数比较且无需分支。1.0.0 的变更列表还包括：仅在需要时才计算 offsets 和 masks、在训练验证阶段复用同一套编码实现（以避免训练与推理产生不同的分词结果）、重写 normalizers、在 atomnorm 基础上支持 bitnorm、spm precompiled、简化 Python 绑定（减少锁、包装类型与手写分发代码，同时保留子类化、序列化、自定义 decoder、可变行为以及 free-threaded CPython 支持），以及面向 ExecuTorch 和 llama.cpp 的仅推理 C/C++ 绑定。博文指出，prefix-sharing 缓存只有在输入包含大量重复 pre-token 时才有收益，而提议中的 “tok-devices” GPU 编码组件属于 1.0.0 之后的探索，仍需进一步原型验证与测量。</p>
<div class="news-background"><strong>背景</strong> 分词是把原始文本转换为语言模型所消费的 token ID 的步骤，而 Byte-Pair Encoding（BPE）是最常见的子词算法之一，被 GPT、GPT-2、RoBERTa、BART 等模型采用；它按照排序后的 merge 规则反复合并出现频率最高的相邻符号对，这也正是 merge loop 成为热点路径的原因。Hugging Face 的 tokenizers 库提供了主流 tokenizer 的 Rust 实现，并提供 Python、Node.js 等绑定，同时也被 Transformers 内部使用。博文感谢了此前在快速 tokenizer 方面的开源工作，点名了 gigatoken、tiktoken、kitoken、tokie、fastokens、wordchipper 和 ai-tokenizer 等项目，并感谢 IBM、NVIDIA 与 ExecuTorch 团队贡献补丁并协助跨硬件测试。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/huggingface/tokenizers">GitHub - huggingface/tokenizers: Fast State-of-the-Art ... tokenizers/tokenizers at main · huggingface/tokenizers · GitHub @huggingface/tokenizers - npm huggingface/tokenizers | DeepWiki How to Use the Hugging Face Tokenizers Library to Preprocess ...</a></li>
<li><a href="https://huggingface.co/docs/tokenizers/index">Tokenizers - Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/Byte-pair_encoding">Byte-pair encoding - Wikipedia</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#tokenizers</span> <span class="tag">#NLP</span> <span class="tag">#performance</span> <span class="tag">#Hugging Face</span> <span class="tag">#library release</span></div>
</article>
<hr>

<a id="item-6"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://arstechnica.com/security/2026/09/muse-metas-extraordinarily-privileged-ai-assistant-has-a-serious-0-day/">Meta 的 Muse AI 助手曝 0-day 漏洞，可导致账户被完全接管</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Ars Technica AI</span><span class="news-time">Sep 21, 22:24</span></div>
<p class="news-summary">Ars Technica 安全记者 Dan Goodin 报道称，Meta 的 Muse AI 助手存在一个 0-day 漏洞，任何本地运行的应用或终端命令都能借此完全控制该 agent，包括获取用于认证用户 Muse 账户的 token。报道还提到，亚马逊已于周日开始在其网站上屏蔽 Muse。 Muse 是一款权限极高的助手——它被授权接入用户的 WhatsApp、邮箱、日历和社交账户，并获得 macOS 的磁盘写入、麦克风、摄像头、位置和日历权限，因此一个既能绕过这些操作系统防护、又会泄露其认证 token 的漏洞，会让每位用户已关联的账户都暴露在风险之中。这同时也削弱了 Meta 关于 Muse「从底层开始就为隐私和安全而构建」的宣传，并且出现在整个行业对 agent 安全性高度关注的时点。 据报道，Meta 的设计让任何本地安装的应用或执行的代码，无论其拥有哪些 macOS 权限，都能修改一长串未公开的设置；其中大部分无关紧要，例如深色模式，但有一项控制着转录发生的位置，该位置通常指向 Meta 运营的服务器地址。攻击者只要把该端点改指向自己的服务器，就能拿到可完全控制 Muse 账户的 token；此外 Muse 目前只有 macOS 版本，没有 Windows 版本。</p>
<div class="news-background"><strong>背景</strong> Muse 是 Meta 于 2026 年 9 月推出的个人 AI agent，宣传中它可以预约、填写表单、完成购物、生成文档并连接用户的应用与服务，甚至在任务需要时即时创建新工具。Meta 表示 Muse 运行在专用的「Muse Secure VM」上，而 WIRED 报道称该应用在上线第一周下载量超过 90 万次。由于这类 AI agent 必须以用户身份长期持有凭据和广泛的设备权限，一旦 token 与权限的隔离机制存在缺陷（这正是越来越多 agent 认证安全指南所关注的重点），便利功能就可能变成账户接管的入口。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/">Introducing Muse: The World’s First Personal AI Agent Built for Everyone</a></li>
<li><a href="https://www.wired.com/story/metas-muse-is-better-at-surveilling-than-helping-me/">Meta&#x27;s Muse Is Better at Surveilling Than Helping Me | WIRED</a></li>
<li><a href="https://nango.dev/blog/guide-to-secure-ai-agent-api-authentication/">A complete guide to securing API authentication for AI agents (2026) | Nango Blog</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#security</span> <span class="tag">#zero-day</span> <span class="tag">#AI assistant</span> <span class="tag">#Meta</span> <span class="tag">#vulnerability</span></div>
</article>
<hr>

<a id="item-7"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://arstechnica.com/security/2026/09/an-undercover-google-analyst-infiltrated-a-notorious-supply-chain-hacking-gang/">谷歌分析师卧底潜入 TeamPCP 供应链黑客团伙</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Ars Technica AI</span><span class="news-time">Sep 20, 11:07</span></div>
<p class="news-summary">在 SentinelOne 的 LABScon 研究会议上，谷歌威胁情报组（Google Threat Intelligence Group）研究员 Austin Larsen 披露，谷歌的一名卧底分析师曾在 TeamPCP 发动攻击期间潜入该知名供应链黑客团伙，使谷歌得以监控其内部聊天、预警受害目标并协助中断攻击。谷歌还追踪到上月在澳大利亚被逮捕并起诉的两名澳大利亚籍嫌疑人中一人据称犯下的操作安全（OpSec）失误，并将关键身份信息移交给执法部门，同时利用其可见性通知 AWS、微软等云服务商吊销被盗凭证。 这是一起罕见的、有据可查的科技公司对人类情报手段潜入网络犯罪团伙的案例，而非仅仅发布威胁报告，标志着谷歌通过新成立的 Cyber Disruption Unit 将“主动破坏”行动正式化。此事的另一重要意义在于，TeamPCP 污染了数百个开源程序、攻破了超过一千家企业，其行动还引发了关于生成式 AI 工具被用于构建零日漏洞利用的令人不安的疑问。 谷歌没有逐一联系受害者直接重置被盗凭证——Larsen 表示，考虑到被攻破企业的数量，这样做耗时过长——而是联系 Amazon Web Services、微软等提供商吊销这些凭证，并发送了数百封通知邮件。谷歌还获悉，该团伙核心圈内有人使用 AI 工具针对一款广泛使用的登录软件开发零日漏洞利用，以绕过双因素认证；谷歌拿到了该利用代码的副本，测试后发现略作调整即可生效，于是警告了软件开发者，后者修复了该安全漏洞。Larsen 强调，卧底分析师从未参与或鼓励任何非法黑客行为，形容其“只是一只停在墙上的苍蝇，只说刚好不被怀疑的话”。</p>
<div class="news-background"><strong>背景</strong> 软件供应链攻击针对的是软件生产流程中防护较弱的环节——如开源软件包、构建工具或厂商更新——使恶意代码通过受害者本就信任的软件触达大量下游目标。在 TeamPCP 的案例中，该团伙窃取开发者账号并用其向开源项目注入恶意软件，还发布了一个以《沙丘》为主题的自我传播蠕虫，将感染过程自动化。威胁情报公司通常通过监控基础设施和论坛来研究此类团伙，但以人类情报手段潜入犯罪组织是一种异常直接且在法律上颇为微妙的方式，因此谷歌特别强调了其行动所受到的约束与规范。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/security/2026/08/authorities-arrest-2-alleged-members-of-prolific-hacking-group-teampcp/">Authorities arrest 2 alleged members of prolific hacking group ...</a></li>
<li><a href="https://indianexpress.com/article/technology/tech-news-technology/who-is-teampcp-hacker-group-open-source-software-ai-10707205/">Who is TeamPCP , the rising hacker group ... - The Indian Express</a></li>
<li><a href="https://en.wikipedia.org/wiki/Supply_chain_attack">Supply chain attack - Wikipedia</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#cybersecurity</span> <span class="tag">#supply-chain attacks</span> <span class="tag">#open-source security</span> <span class="tag">#threat intelligence</span> <span class="tag">#AI misuse</span></div>
</article>
<hr>

<a id="item-8"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.interconnects.ai/p/the-current-balance-of-power-in-open">Nathan Lambert 谈开放权重模型与美中竞争</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Interconnects (Nathan Lambert)</span><span class="news-time">Sep 21, 11:56</span></div>
<p class="news-summary">Nathan Lambert 发布了他向国会议员及工作人员所做简报的准备稿，从美中竞争的角度阐述开放权重语言模型的现状。他指出，自大约 2025 年 4 月以来，中国 AI 公司已成为开放权重模型发布方面明显的领先者，并记录了众多美国知名公司与初创企业正在基于这些模型进行开发。 文章认为，开放权重模型如今是 AI 能力扩散的核心渠道，而中国实验室已占据开放模型使用的很大份额，这使得美国关于开放模型的政策决策对本国竞争力和国家安全都意义重大。它表明，美国企业正越来越多地依赖中国发布的模型来获得低成本、灵活的 AI 功能，这种态势具有战略与商业层面的影响。 Lambert 区分了开放权重模型（权重加上许可证和推理代码，如 Meta 的 Llama、阿里巴巴的 Qwen、Google 的 Gemma 以及 DeepSeek 的模型）与真正意义上的开源模型（后者还包含训练代码和数据）。他指出，对开放模型使用情况最准确的公开观察来自那些披露细分的平台——例如他提到开源编码 agent OpenCode 上中国模型的推理量约占 95% 或更高——而在 Together AI、Fireworks AI 等平台以及企业私有部署中的大量使用并未按模型细分统计。</p>
<div class="news-background"><strong>背景</strong> 开放权重模型会公开其训练所得的参数，使他人能够直接检查或运行；而 GPT-4、Claude Opus 4.5 等闭源模型只能通过 API 或 ChatGPT 这类产品访问。开放权重发布通常附带许可证和可在 Transformers、vLLM、SGLang 等库中使用的推理代码。由于这些模型可以被下载和复用，其能力传播可能比闭源 API 更快、更广，这正是模型的地理来源和许可条款成为政策关切的原因。一个相关的技术术语是蒸馏（distillation），指训练一个较小的模型去模仿较大的模型，二者之间最终性能差距的大小仍是研究中的话题。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.together.ai/">Together AI | The AI Native Cloud</a></li>
<li><a href="https://fireworks.ai/">Own Your Specialized Intelligence | Fireworks</a></li>
<li><a href="https://arxiv.org/abs/2210.12787">[2210.12787] Respecting Transfer Gap in Knowledge Distillation</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者称赞了这份综述，并集中讨论经济因素：有人指出定价模式正在演变，DeepSeek 是该类别的定义者，以约为专有模型十分之一的成本提供“几乎一样好”的性能，尽管这一差距正在从两端缩小。另一位评论者提问：中国实验室是否得到政府补贴以抢占全球市场，还是美国的制裁促使它们在优化功能的同时也注重效率；还有读者质疑 Lambert 的“一到两个月蒸馏差距”估计是如何得出的。</div>
<div class="news-tags"><span class="tag">#open-source AI</span> <span class="tag">#AI policy</span> <span class="tag">#US-China competition</span> <span class="tag">#open-weight models</span> <span class="tag">#LLMs</span></div>
</article>
<hr>

<a id="item-9"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector/">OpenAI 的 __obi cookie 将 ChatGPT 账号与第三方网站浏览行为关联起来</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Sep 20, 17:43</span></div>
<p class="news-summary">一项独立调查称，OpenAI 位于 bzr.openai.com 的广告采集器会设置名为 __obi 的 cookie，其作用域为 .openai.com 并与用户的 ChatGPT 账号绑定，随后该标识会从部署了 OpenAI 转化像素的普通第三方网站回传给 OpenAI。作者表示自己在手机上用两种独立抓包方法复现了该机制，并交叉核对了数月观测流量中覆盖 1,029 个主机名、936 个广告主像素的数据。 如果该发现属实，意味着 OpenAI 能够把你在参与广告计划的第三方网站上的行为回溯到你的 ChatGPT 账号——这与 Meta 和 Google 长期具备的能力在结构上相同，但被用在了 AI 聊天产品上，而用户往往会向这类产品透露他们不会发到社交网络上的信息。安装像素的广告主却看不到这种关联，因为 __obi 属于其脚本无法读取的域名。 文章称，电子邮箱、电话和姓名在传输前会做 SHA-256 哈希处理，而国家、地区、城市和邮政编码则以明文发送，其中邮政编码是被采集最多的表单字段（28 个站点共 100 次事件）；URL 被缩减为来源加路径，观测到的 23,929 个 URL 中没有一个携带查询字符串，但保留下来的路径中出现了某种疾病状况、债务解决方案营销漏斗和诉讼受理表单。文章还指出，在 881 个已知设置的像素中有 638 个启用了自动匹配（包括观测到的所有信贷和借贷广告主），大约每五个 ChatGPT 会话会产生一个同步令牌，移动端网页版投放广告时完全不进行同步，并且账号的服务端解析并未被直接观测到——返回 202 只能说明采集器接受了带有该 cookie 的事件。</p>
<div class="news-background"><strong>背景</strong> 转化像素是广告平台提供给广告主、用于嵌入其自有网站的一小段代码，以便把购买或注册行为归因到某条广告上；Meta 和 Google 多年来一直用“已登录账号 + 像素触发”的方式把站外行为关联到用户画像。&quot;Identity resolution&quot;（身份解析）是广告技术领域的通用说法，指把对同一个人的分散观测拼接成一份画像。据对该报告的报道，OpenAI 在自己的 cookie 政策中把 __obi 列为有效期为一年的分析类 cookie。文中描述的机制涉及 ChatGPT 签发的一个短时效 RS256 JWT（签发方 &quot;chatgpt-wadi&quot;、受众 &quot;bzr.openai.com&quot;、用途 &quot;obi_sync&quot;），其中携带账号标识与 obi 值。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://cyberpress.org/chatgpt-ad-collector-tracks-user-activity/">ChatGPT Ad Collector Tracks User Activity Across Third-Party ...</a></li>
<li><a href="https://www.notebookcheck.net/ChatGPT-s_obi-cookie-follows-you-to-other-websites.1404436.0.html">ChatGPT&#x27;s __ obi cookie follows you to other... - Notebookcheck News</a></li>
<li><a href="https://www.identity20.com/identity-resolution-and-cross-site-tracking-how-you-get-re-identified-online/">Identity Resolution and Cross - Site Tracking | Identity 2.0</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#privacy</span> <span class="tag">#tracking</span> <span class="tag">#OpenAI</span> <span class="tag">#ad-tech</span> <span class="tag">#web-security</span></div>
</article>
<hr>

<a id="item-10"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://projectzero.google/2026/09/windows-dangling-com.html">Project Zero 详解 Windows 悬空 COM 注册提权漏洞</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Sep 21, 18:21</span></div>
<p class="news-summary">Google Project Zero 发布了一篇简短博客，介绍微软近期修复的 Windows 提权漏洞 CVE-2026-66804，该漏洞由作者本人与另外 14 名研究者共同报告。它其实是 CVE-2026-50343（被 Calif 命名为 “Dark Elevator”）修复不彻底的产物，利用了 CrossDevice 组件的悬空 COM 对象注册。 该案例体现了 Windows 安全中反复出现的模式：修补某条触发路径并不等于消除根因，攻击者可以换用另一个高权限组件继续利用同一个悬空注册。对 Windows 管理员来说，需要确认终端已安装 CVE-2026-66804 的修复；对漏洞研究者而言，它提供了一套可复用的方法，用来寻找类似“路径可写、DLL 缺失”的 COM 注册。 这个悬空注册是系统级的 CrossDevice COM 对象，CLSID 为 {E9F83CF2-E0C0-4CA7-AF01-E90C70BEF496}，其进程内服务器 DLL 路径 %PROGRAMDATA%\CrossDevice\CrossDevice.Streaming.Source.dll 实际并不存在；由于 C:\ProgramData 对所有用户可写，攻击者可以创建该目录并放置任意 DLL。由于原始 Dark Elevator 漏洞所用的 InstallService 路径已被修复，作者改用了一个以 SYSTEM 运行且未启用自定义封送的 COM 服务——Shell Create Object Handler（CLSID 135fd325-45b7-4c30-89f8-4386961669f0），该对象无法被直接实例化；他还给出了基于 OleViewDotNet 与 NtObjectManager 模块的 PowerShell 检测脚本，用于枚举所有 LoadLibrary 无法解析其 DLL 的进程内 COM 类。</p>
<div class="news-background"><strong>背景</strong> COM（Component Object Model，组件对象模型）是 Windows 按固定标识而非文件路径来查找组件的机制；每个组件都有一个 CLSID，其注册信息通常写在 HKEY_CLASSES_ROOT 注册表项下，指向实现该组件的可执行文件或 DLL。因此一条注册通常包含两部分：类表项与服务器可执行文件；对“进程内”组件而言，服务器就是一个 DLL，会被加载进创建该对象的宿主进程——若宿主是以 SYSTEM 运行的服务，该 DLL 也随之以 SYSTEM 权限执行。所谓“悬空”注册，是指类表项存在、但它指向的 DLL 缺失；如果该路径又位于所有用户都可写的目录（例如 C:\ProgramData），低权限用户就能放置恶意 DLL，让高权限进程加载它，这正是本次提权的核心。博客还涉及 COM 的自定义封送（custom marshaling）策略，它决定对 COM 服务的调用如何处理，也是原始 Dark Elevator 漏洞所依赖的机制。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://cyfar.ca/posts/windows-exploitation-techniques-dangling-com-object-registrations">Windows Exploitation Techniques: Dangling COM Object ...</a></li>
<li><a href="https://www.pk-sharma.com/briefing/project-zero-dangling-com">Project Zero: a dangling COM registration is a SYSTEM ...</a></li>
<li><a href="https://www.unsafe.sh/go-443883.html">Windows Exploitation Techniques: Dangling COM Object ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Windows security</span> <span class="tag">#privilege escalation</span> <span class="tag">#COM objects</span> <span class="tag">#vulnerability research</span> <span class="tag">#CVE</span></div>
</article>
<hr>

<a id="item-11"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.science.org/content/article/nasa-s-mars-sample-return-mission-dead">NASA 火星采样返回任务实质上被取消</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">Muhammad523</span><span class="news-time">Sep 21, 19:14</span></div>
<p class="news-summary">据《Science》2026 年 1 月 6 日的一篇文章报道，NASA 的火星采样返回（MSR）计划——即 NASA 与 ESA 联合、旨在取回毅力号（Perseverance）火星车在火星上封存的岩芯与土壤样本的任务——已实质性地被取消。该计划于 2022 年正式获批，但始终未能摆脱成本与进度的不断膨胀。 此举取消了将火星物质带回地球的旗舰机器人计划，而这些样本本可在远超任何火星车车载仪器的实验室中被分析，以寻找古代生命迹象。它还可能让中国天问三号（计划于 2028 年 12 月至 2029 年 1 月的发射窗口实施）抢先完成首次火星采样返回，从而重塑行星探测领域的领先格局。 Hacker News 上的评论者指出，JPL 领导层使该项目成本膨胀到约 110 亿美元，且样本在 2040 年前都无法返回，并批评其架构围绕 Ariane 64 等传统运载火箭设计，而非采用 Starship 或 New Glenn 等更新、运力更强的火箭。还有评论者指出该文章日期为 2026 年 1 月 6 日，并质疑为何此时才被重新翻出。</p>
<div class="news-background"><strong>背景</strong> 火星采样返回原本是 NASA 与 ESA 的一项多任务联合计划：NASA 的毅力号火星车于 2021 年着陆耶泽罗撞击坑（Jezero Crater），负责钻取并在火星表面封存样本管；随后由着陆器与上升器把样本送入火星轨道，再由地球返回轨道器捕获并带回地球。采样返回被视为太阳系探测中优先级最高的目标之一，因为只有地球上的实验室才能完成包括生物特征搜寻在内的全套分析。火星采样返回已被研究和尝试数十年——苏联 1975 年的尝试因 N1 火箭连续失败而取消——截至 2026 年，中国的双次发射方案天问三号计划于 2028–2029 年窗口实施，俄罗斯航天局提出 2030 年代的 Mars-Grunt，日本 JAXA 的 MMX 则瞄准火星卫星火卫一的样本。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mars_sample-return_mission">Mars sample - return mission - Wikipedia</a></li>
<li><a href="https://science.nasa.gov/mission/mars-sample-return/">Mars Sample Return - NASA Science</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 的讨论（248 分、179 条评论）补充了文章之外的背景：一位评论者强调中国并行的天问三号计划将于 2028 年发射；另一位曾参与 ExoMars（即如今的罗莎琳德·富兰克林号火星车，发射时间从 2018 年一再推迟到 2028 年）的评论者则希望该任务仍能成行。其他人批评 JPL 将成本推高到 110 亿美元、时间表排到 2040 年，并且依赖 Ariane 64 等传统火箭而非 Starship 或 New Glenn（有评论对比阿波罗带回的 842 磅月岩与 MSR 仅约 1.1 磅的样本量）；还有评论者质疑，当初为何要让毅力号钻取并封存样本，交给一个尚未明确界定的未来任务去回收。</div>
<div class="news-tags"><span class="tag">#space exploration</span> <span class="tag">#NASA</span> <span class="tag">#Mars Sample Return</span> <span class="tag">#JPL</span> <span class="tag">#policy</span></div>
</article>
<hr>

<a id="item-12"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://poloclub.github.io/transformer-explainer/">交互式可视化讲解器拆解 GPT-2 Transformer 内部机制</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">aray07</span><span class="news-time">Sep 21, 19:43</span></div>
<p class="news-summary">Polo Club（poloclub.github.io）发布了一个交互式网页可视化讲解器，带领读者逐步了解 GPT-2 这类 Transformer 模型如何处理文本，涵盖分词、embedding、attention head 以及下一个 token 的采样过程。该项目在 Hacker News 上引发讨论，获得 132 分和 18 条评论。 Transformer 的内部机制几乎是所有现代大语言模型的基础，但仅凭论文很难理解，因此一个精心制作、可动手操作的可视化工具降低了学生、工程师以及好奇的非专业人士的理解门槛。这也说明交互式讲解器正逐渐成为教授机器学习概念的主流方式，而不再是小众的业余项目。 该讲解器专门聚焦 GPT-2，而 GPT-2 使用的是绝对位置编码（absolute positional encoding）——评论者指出这一设计在现代模型中已不再通用，因此读者不应把它当作通用蓝图。此外，它将 temperature 采样描述为平衡“安全性与创造力”也被认为用词不严谨，因为 temperature 实际控制的是 token 选择的随机性或可预测性。</p>
<div class="news-background"><strong>背景</strong> Transformer 是一种以自注意力（self-attention）为核心的神经网络架构，该机制让序列中的每个 token 衡量自己与所有其他 token 的关系；GPT-2 则是这一家族中较早期、规模相对较小的自回归语言模型。Attention head 会生成一个 attention 矩阵，并与 Value 向量相乘得到该 head 的输出，多个 head 并行运行以捕捉不同模式。Temperature 是作用于模型输出概率分布的采样参数：数值低时输出更确定、更重复，数值高时输出更随机、更多样。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://jalammar.github.io/illustrated-transformer/">The Illustrated Transformer – Jay Alammar – Visualizing machine...</a></li>
<li><a href="https://shivammehta25.github.io/posts/temperature-in-language-models-open-ai-whisper-probabilistic-machine-learning/">The need for sampling temperature and differences between whisper...</a></li>
<li><a href="https://medium.com/@shashankag14/understanding-sampling-techniques-in-large-language-models-llms-dfc28b93f518">Sampling Techniques in Large Language Models (LLMs) | Medium</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论整体偏正面：有人推荐 Jay Alammar 的《The Illustrated Transformer》作为配套资料，还有人提出了一个有价值的洞见——attention 矩阵与 Value 向量相乘，在数学上等同于把 Value 向量送入一个全连接层，而该层的权重由 attention head 在推理时根据 Key 和 Query 动态构造。也有人对细节提出异议：一位工程师表示，考虑到“transformer”在电子工程中的含义，这个词总是令人混淆；另一位评论者认为用“safety”来描述 temperature 所控制的东西并不恰当，并指出 temperature 为 0 的文本反而有一种不自然的“缺乏惊喜感”。还有评论者提醒，聚焦 GPT-2 可能误导非专业读者，因为绝对位置编码对模型能学到什么样的表示有着重大影响。</div>
<div class="news-tags"><span class="tag">#transformers</span> <span class="tag">#machine-learning</span> <span class="tag">#visualization</span> <span class="tag">#education</span> <span class="tag">#nlp</span></div>
</article>
<hr>

<a id="item-13"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://alicegg.tech/2026/09/21/attention">随笔《注意力是你仅有的资源》：应用如何劫持注意力</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Sep 21, 19:06</span></div>
<p class="news-summary">alicegg.tech 上的一篇个人随笔认为，注意力是一种有限且可被训练的资源，而 YouTube、Spotify、LinkedIn、Reddit 等以推荐算法驱动的现代产品正是为攫取这种资源而设计；相比之下，算法时代之前由书签和 RSS 订阅构成的旧式网络提供了一种更“有意图”的替代方案。这篇文章在 Hacker News 上引发热议，获得 528 分和 152 条评论。 这篇文章正处于关于注意力经济与数字健康的持续公共讨论之中，而此时用户越来越多地抱怨无尽的信息流、自动播放和 AI 生成的内容填充物，已经取代了他们曾经能够直接掌控的工具。Hacker News 上的讨论表明这种担忧并非抽象空谈，读者们分享了退出社交媒体、重建更慢节奏的订阅式阅读习惯的具体尝试。 这是一篇第一人称的论述性随笔，而非技术成果，其核心论证工具是“俄罗斯方块效应”（Tetris effect）——即长时间专注于某项活动会重塑人的思维、心理意象乃至梦境的现象。文章对“有意图的互联网”的怀旧式描述也受到质疑：有评论者指出，Lycos、Yahoo! 和 MSN 等门户网站早已是塞满广告的默认主页，而 Mosaic 浏览器在 1993 年就具备全文历史搜索功能，后来才被书签系统取代。</p>
<div class="news-background"><strong>背景</strong> 俄罗斯方块效应是一种广为人知的心理学现象：长时间投入某项活动的人，会在不相关的场景中开始识别出与之相关的模式——例如玩家会在云朵、楼房中看到下落的方块，甚至在入睡前眼前浮现方块。所谓“注意力经济”，是指平台通过推荐算法替用户挑选内容、从而争夺用户屏幕使用时长的商业模式。RSS（Really Simple Syndication）是一种标准化的网络订阅格式，用户可通过聚合器一次性订阅大量网站并集中阅读更新，而无需逐一访问；它在 2005 至 2006 年前后广泛流行，之后被主流浏览器逐渐弱化。本文标题也呼应了 2017 年 Google 那篇提出 transformer 架构的著名论文《Attention Is All You Need》。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tetris_effect">Tetris effect</a></li>
<li><a href="https://en.wikipedia.org/wiki/RSS">RSS</a></li>
<li><a href="https://en.wikipedia.org/wiki/Attention_Is_All_You_Need">Attention Is All You Need - Wikipedia</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者大体认同文章的判断，并分享了自己的实践：有人把戒掉社交媒体称为“我做过的最好的决定之一”，还有人表示自己常常在 Hacker News 和 YouTube 上耗费数小时却毫无收获，并提出开机前先写下待办清单的办法。也有反对的声音：一位评论者指出 Lycos、Yahoo! 和 MSN 等自定义主页早已充斥标题党图片链接和广告；另一条长评论则追溯了 Mosaic 全文历史搜索如何让位于书签、delicious，以及地址栏中出现的 Facebook“点赞”按钮而非 RSS。</div>
<div class="news-tags"><span class="tag">#attention economy</span> <span class="tag">#digital wellbeing</span> <span class="tag">#social media</span> <span class="tag">#productivity</span> <span class="tag">#web history</span></div>
</article>
<hr>

<a id="item-14"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://linear.app/now/ci-bottleneck-reworked">AI 编程代理让 CI 成为瓶颈，Linear 重做其 CI 流水线</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">julian_digital</span><span class="news-time">Sep 21, 19:23</span></div>
<p class="news-summary">Linear 发布了一篇工程博客，讲述 AI 编程代理如何让持续集成（CI）成为其开发流程中的瓶颈，以及他们如何相应地重做流水线。文中提到的主要改动是把工作负载从 GitHub Actions 迁移到配备更快 CPU、更高性能存储和更好缓存基础设施的第三方 runner 上，让同一条流水线跑在更快的机器上。 这展示了采用 AI 编程代理的一个具体副作用：当代理生成代码改动的速度远超人类时，瓶颈会从写代码转移到围绕代码的自动化验证基础设施上。正在引入编程代理的团队可能会发现，限制交付速度的不再是开发者，而是 CI 流水线。 这只是一家公司的经验报告，而非通用基准测试，而且所述的解决办法主要是让现有流水线跑在更快的硬件上，而不是重新设计流水线本身。评论者还指出，Linear 直到公司规模相当大之后才着手做这项优化，因此这套做法对小型团队的可迁移性有限。</p>
<div class="news-background"><strong>背景</strong> 持续集成（CI）是一种软件开发实践：开发者频繁地把代码改动合并到共享分支，由自动化系统对整合后的代码库进行构建和测试。CI 流水线通常运行在托管或自建的 runner（执行构建与测试任务的机器）上，其速度在很大程度上取决于 CPU、存储和缓存性能。GitHub Actions 是流行的 CI 服务，对已经托管在 GitHub 上的项目来说很方便，但其 runner 有时较慢，也常被抱怨可靠性问题。AI 编程代理利用大语言模型自主生成和修改代码，每天产生的改动量可能远超人类团队，从而加大这些流水线的负载。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Continuous_integration">Continuous integration - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/continuous-integration">What is continuous integration? - IBM</a></li>
<li><a href="https://www.linkedin.com/posts/youjjwal_devops-cicd-platformengineering-activity-7420684355896803329-mz_g">CI /CD Pipeline Bottlenecks : 3 Common Pitfalls | LinkedIn</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 上的讨论褒贬不一，且普遍对“以速度为中心”的叙事持怀疑态度。有评论者（torben-friis）认为，尽管大家都在提速，产品却没有明显改进；另一位（frangonf）指出 Linear 是在大约 1 亿美元 ARR 和数十亿美元估值时才做这项优化的；aliclark 则认为真正的瓶颈是人工与产品层面的验证，而不是 CI。也有人对迁离 GitHub Actions 并不意外，认为它虽然方便，但速度慢、可靠性也日益堪忧。</div>
<div class="news-tags"><span class="tag">#CI/CD</span> <span class="tag">#AI coding agents</span> <span class="tag">#developer productivity</span> <span class="tag">#engineering infrastructure</span> <span class="tag">#build systems</span></div>
</article>
<hr>

<a id="item-15"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://github.com/jaredpalmer/kev/tree/main">Kev：基于 Qwen3.5 构建的微型“类 Jev”决策模型</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">tosh</span><span class="news-time">Sep 21, 07:11</span></div>
<p class="news-summary">Jared Palmer 在 GitHub 上发布了 Kev，将其描述为一个基于 Qwen3.5 构建的微型“类 Jev（Jev-like）”决策模型家族。该项目在 Hacker News 上获得 389 分和 171 条评论，成为围绕开放权重模型生态中衍生作品讨论的焦点。 这个项目说明开放权重社区正以极快的速度，在 Qwen3.5 等现有基础模型之上衍生出专用变体，而不是从零训练全新范式。它同时让更广泛的技术受众第一次接触到正在兴起的“决策模型”类别——这类模型不生成自由文本，而是针对预设问题返回带校准概率的答案。 Kev 被定位为“类 Jev”而非对 Jev 的复刻；有评论者认为这一标签存疑，因为据说 Jev 使用 RLCD 训练，而 Qwen3.5 及其衍生模型采用的是 RLHF 类方法——这一分歧在现有材料中并未得到解答。由于该新闻条目的正文内容较少、项目自身的主张在此也无法独立验证，其具体模型规模、训练数据和许可协议仍不明确。</p>
<div class="news-background"><strong>背景</strong> Jev 被描述为 TypeSafe AI 所称 System One 家族的第一款模型：你提供一些内容（状态）以及一组预先定义好可能答案的问题，模型会为每个问题返回带有概率的答案，延迟仅数十到数百毫秒，成本只是主流大模型的一小部分。Qwen3.5 是阿里云 Qwen 系列中的开源多模态大语言模型家族，凭借宽松的许可和丰富的参数规模，常被用作微调和衍生产品的基座。因此“类 Kev”项目正处于这两种思路的交汇点：一个体积小、速度快、由开放权重 Qwen3.5 检查点微调而来的分类式决策模型。Kev 仓库被归为 Jared Palmer 所作，他以创建 React Query 与 TanStack 而闻名。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://jevaiguide.com/what-is-jev/">What Is Jev ? TypeSafe&#x27;s System One Model Explained</a></li>
<li><a href="https://grokipedia.com/page/Qwen35">Qwen3.5</a></li>
<li><a href="https://ai4coding.ru/solutions/jaredpalmer-kev">Kev — компактные модели принятия решений на базе Qwen 3 . 5</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者既有实用替代方案的讨论，也有质疑。用户 nico 认为，如果只需要分类并且能提供训练数据，用 embeddings 加逻辑回归分类器在邮件分类上只需 50–100 个样本就能达到约 95% 的准确率，在 CPU 上训练不到 5 分钟，模型小于 1MB，推理低于 100 毫秒。也有人从技术角度质疑“类 Jev”的定位（hbarka 指出 RLCD 与 RLHF 的训练方式不匹配），prodigycorp 则对被视为机会主义的“Jev 形状”项目表示疲倦，而声明无利益关联的 oscarfr 分享了一个列出众多 Jev 类模型的第三方基准页面。</div>
<div class="news-tags"><span class="tag">#llm</span> <span class="tag">#open-weight-models</span> <span class="tag">#qwen</span> <span class="tag">#classification</span> <span class="tag">#fine-tuning</span></div>
</article>
<hr>

<a id="item-16"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.reuters.com/world/us/faa-halts-some-us-east-coast-flights-due-communication-issues-2026-09-21/">光纤线路中断，FAA 暂停美国东海岸繁忙机场航班</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">allanbreyes</span><span class="news-time">Sep 21, 18:41</span></div>
<p class="news-summary">据路透社报道，一条光纤线路被切断导致通信中断，FAA 因此暂停了美国东海岸多个繁忙机场的航班。据一位评论者引用的事件描述，当系统尝试切换到备用光纤时，运维人员发现备用线路本身也已经断开。 这起事件表明，单一物理线缆故障可以级联放大为大规模的航空运输中断，影响成千上万旅客和航班时刻安排。它也引发了一个尖锐问题：关键航空通信基础设施的冗余设计，是否达到了科技行业视为基本要求的标准。 讨论指出了两个具体薄弱点：备用光纤似乎在没有触发任何告警的情况下失效，直到真正尝试切换时才发现其不可用；而在发生重叠切断时，仅有的两条路径设计无法提供保护。评论者还提到，FAA 的新一代空管系统 SMART 才刚刚开始部署，这并不能解决眼下物理层的冗余缺口。</p>
<div class="news-background"><strong>背景</strong> 光纤以光脉冲形式传输数据，是大多数现代通信的长距离骨干，因此一次挖掘机或施工事故就可能切断海量流量。关键系统通常通过配置两条或更多物理上彼此独立的路径，并持续监控每条路径来防范此类风险，因为互联网路由协议只有在确实存在替代路径时才能绕开故障进行重路由。然而，空中交通管制网络往往是专门构建的，管控比公共互联网更严格，这也可能意味着可选的独立运营商和路径更少。</div>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 的评论者大多批评其冗余设计：有人称一个关乎生命的系统直到尝试切换时才发现备用光纤不可用，实在“令人沮丧”；也有人认为，即便是中等重要性的业务，两条光纤路径都不够，因为重叠切断是会发生的。还有人对空管网络是否是与自愈型互联网不同的、冗余更少的独立网络提出疑问；也有人以玩笑口吻说，埋下一小段光纤，最能保证引来一台挖掘机把它挖断。</div>
<div class="news-tags"><span class="tag">#networking</span> <span class="tag">#infrastructure-resilience</span> <span class="tag">#aviation</span> <span class="tag">#fiber-optics</span> <span class="tag">#systems-reliability</span></div>
</article>
<hr>

<a id="item-17"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://heretic-project.org/">Heretic 自动化移除开源权重语言模型的审查机制</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">Bluestein</span><span class="news-time">Sep 21, 04:35</span></div>
<p class="news-summary">Heretic 是一个托管在 heretic-project.org 及 GitHub（p-e-w/heretic）上的开源项目，它把从基于 Transformer 的语言模型中移除拒答行为（即所谓“安全对齐”）的过程自动化，也就是“abliteration”，据称无需昂贵的后训练（post-training）。该项目在 Hacker News 上引发了 232 分、96 条评论的讨论，内容既有实际用例，也有技术上的提醒和政策层面的揣测。 Abliteration 降低了任何人从开源权重模型中去除拒答行为的门槛：这对那些想让模型完成被拒绝的正当任务的用户很重要，对把该技术视为对对齐机制攻击的 AI 安全研究者同样重要。由于开源权重可以被自由下载和修改，此类工具让“去审查”从专门的研究工作变成一种常规操作。 根据项目自身的介绍，Heretic 生成的未审查模型可与专家手工完成的 abliteration 相媲美，同时对模型能力的损害明显更小，其做法是使用基于 TPE 的优化来搜索消融参数。有评论者提醒说，底层训练数据本身可能就是围绕拒答而构建的，因此压制拒答方向并不能保证模型真的编码了正确的知识。</p>
<div class="news-background"><strong>背景</strong> 开源权重语言模型指的是训练好的参数张量被公开发布、任何人都可以下载、运行、微调或再分发的模型，这与只能通过受限 API 访问的模型形成对比。安全对齐会训练这类模型去拒绝有害或敏感的指令；而 abliteration 是一类技术，它定位并压制对拒答行为影响最大的那一个潜方向，相当于在权重层面而非通过提示词实现越狱。Heretic 的贡献在于把这一通常需要人工反复试错的过程自动化，使其无需昂贵的重新训练即可套用到模型上。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/p-e-w/heretic">GitHub - p-e-w/heretic: Fully automatic censorship removal ...</a></li>
<li><a href="https://www.emergentmind.com/topics/abliteration">Abliteration in LLMs: Removing Refusal Behavior</a></li>
<li><a href="https://promptengineering.org/llm-open-source-vs-open-weights-vs-restricted-weights/">Openness in Language Models : Open Source vs Open Weights vs...</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 整体情绪偏向实用而非恐慌：一位评论者表示，abliterated 模型对他逆向分析并重新掌控自己的中国产 IP 摄像头至关重要，因为主流模型会拒绝此类请求；而 Aurornis 则提醒，围绕拒答构建的训练数据可能意味着相关知识根本没有被编码，因此去掉拒答并不保证得到正确答案。其他人则表达了政策担忧（Tepix 预测 abliterated 与 “heretic” 开源权重模型“会最先被立法禁止”），还有人讲述了用 agent 把一台小米手机刷坏又救回、但引导加载程序仍锁着的亲身经历，以及一句改等 “Hexen” 的玩笑。</div>
<div class="news-tags"><span class="tag">#LLM</span> <span class="tag">#open-weight models</span> <span class="tag">#abliteration</span> <span class="tag">#AI safety</span> <span class="tag">#model fine-tuning</span></div>
</article>
<hr>

<a id="item-18"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://simonwillison.net/2026/Sep/21/jev/">TypeSafe AI 推出 Jev：Simon Willison 解析全新 “System One” 决策模型</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Simon Willison</span><span class="news-time">Sep 21, 23:09</span></div>
<p class="news-summary">TypeSafe AI 发布了 Jev，并将其称为全新类别 “System One models”（Simon Willison 更倾向于称之为 “decision models” 决策模型）的首个示例；Willison 于 2026 年 9 月 21 日发表了对它的分析。Jev 接受文本或半结构化的 “state” 输入，但只返回浮点数值，用于表示类别、是/否问题、评分以及相应的置信度，而不再生成文本。 Willison 将 Jev 视为 LLM 形态可能发生的一次范式转变：它不再生成需要软件解析的自然语言文本，而是直接向代码返回带类型的概率化决策，这可能让分类、排序与重排序任务更便宜、更可靠。但与此同时，他也警告这种设计让系统进一步退化为黑箱机器学习——只返回一个浮点数，无法解释决策为何做出，从而让偏见问题更加难以审计。 Jev 仅按输入 token 计费，价格为每百万 token 0.042 美元（输出免费），Willison 指出这比 OpenAI GPT-5 Nano 的每百万 0.05 美元还要便宜；多个问题会并行评估，因此发送许多问题的耗时大致与发送一个问题相同。该 API 提供三类问题，其中包括是/否类型的 “Noul” 问题，其 CEO 在 Hacker News 上确认该名称是 Bernoulli（伯努利）的缩写；Willison 也指出，由于只返回一个分数，当某内容被判定为垃圾信息时，你无法知道是哪些内容信号触发了这一判定。</p>
<div class="news-background"><strong>背景</strong> 传统 LLM 通常被视为读写文本的黑箱，其 API 计费一般分为输入与输出两部分，且输出价格更高。 “System One” 这一命名呼应了认知心理学中的双过程理论——把快速、直觉式的判断与较慢的审慎推理相对照；而“决策模型”这一说法则暗示它是一种狭窄而快速的组件，软件可以像调用函数一样调用它，而非通用聊天模型。Willison 的重排序实验使用了 BM25 —— 一种被 Elasticsearch、Lucene 和 Solr 等搜索系统采用的经典词法相关性打分函数——先用它低成本地召回候选文档，再由 Jev 对这些候选做相关性打分。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.langchain.com/blog/building-a-harness-with-jev">What Is Jev? A Guide to TypeSafe AI ’s System One Model</a></li>
<li><a href="https://jev-agent.com/">What is Jev? TypeSafe AI &#x27;s System One decision model explained</a></li>
<li><a href="https://dev.to/javiagu13/bm25-explained-the-algorithm-behind-modern-search-2jo3">BM 25 Explained: The Algorithm Behind Modern... - DEV Community</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 所提供的摘录显示，Hacker News 上的讨论在快速实验热情与质疑之间交织：TypeSafe AI 的 CEO 在那里回应了关于 Jev 命名的问题，有评论者调侃它是“Morty 对着死亡水晶说话的数字版本”；另一条讨论串则聚焦开源权重复刻项目，例如基于 Qwen 3.5 构建、产出 0.8B、4B 和 9B 模型的 Kev，其中有人链接到已经出现的 JevBench 基准，用于比较 “Jev-class decision models”。Willison 本人对这种黑箱特性表示不安，希望人们不要在忽视偏见问题的情况下使用 Jev，同时也称发布不到一周内涌现的活动量“极为惊人”。</div>
<div class="news-tags"><span class="tag">#LLM</span> <span class="tag">#AI models</span> <span class="tag">#decision models</span> <span class="tag">#model architecture</span> <span class="tag">#AI industry</span></div>
</article>
<hr>

<a id="item-19"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://simonwillison.net/2026/Sep/20/voxium/">Simon Willison 引用一则由 Claude Code 主导团队的一线描述</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Simon Willison</span><span class="news-time">Sep 20, 21:06</span></div>
<p class="news-summary">2026 年 9 月 20 日，Simon Willison 发布了一段署名 voxium 的简短自述，作者称自己入职一家大公司半个月，发现规格文档、代码、测试、PRD、工单、工单处理以及各类报告全部由 Claude Code 生成。据该自述，团队里没有人喜欢这种状况，员工被要求尽可能多地交付，每天工作 12 到 13 个小时，而用作者的话说，没有人真正去读任何东西。 这段自述虽然是未经核实的个案，却呈现了 AI 编程代理不仅影响个人效率、更可能重塑工程文化的图景，引发人们对代码评审、代码归属权，以及在代码生成变得廉价迅速时以产出量衡量绩效是否仍然合理的疑问。这也呼应了整个行业关于如何评估开发者绩效的更广泛讨论。 该自述称这种现象覆盖了从 L1 到 L7 的所有工程师，管理层多次表示提交代码不是瓶颈、质疑团队为何仍然缓慢；发帖人还称人们每天工作 12 到 13 个小时，只是“为了按回车键”。这段内容简短且匿名，因此这些说法属于个人描述而非经核实的报道，Willison 也只是将其作为引文呈现，并未展开调查或深度分析。</p>
<div class="news-background"><strong>背景</strong> Claude Code 是 Anthropic 推出的智能体式编程助手，运行在开发者的终端中，直接工作于本地开发环境，可协助构建功能、修复缺陷并自动化开发任务。在许多大型科技公司中，工程师按数字职级划分，从入门级的 L1 一直排到 L7，后者通常代表资深或杰出的一线工程师，因此自述中提到“从 L1 到 L7”意味着作者认为这一现象是全公司范围的，而非仅限于初级员工。Simon Willison 是知名开发者与博主，经常收集并点评与 AI 和软件开发相关的重要话题。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://code.claude.com/docs/en/overview">Overview - Claude Code Docs</a></li>
<li><a href="https://www.terminal.io/engineers/blog/defining-the-ladder-of-software-engineer-levels">Leveling Up: Defining the Ladder of Software Engineer ... - Terminal.io</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI-assisted development</span> <span class="tag">#software engineering culture</span> <span class="tag">#Claude Code</span> <span class="tag">#code review</span> <span class="tag">#AI in the workplace</span></div>
</article>
<hr>

<a id="item-20"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://simonwillison.net/2026/Sep/20/hn-49779718/">Simon Willison：MCP 对受管制的托管型 agent 仍有价值</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Simon Willison</span><span class="news-time">Sep 20, 20:24</span></div>
<p class="news-summary">2026 年 9 月 20 日，Simon Willison 发表了一篇简短的反驳文章，回应“MCP 一直都是个坏主意”的说法，认为这种批评“完全忽视了 MCP 如今带来的价值”。他承认，对于拥有不受限互联网访问权限的完整终端 agent 来说，MCP 基本没有必要；但他表示，在更受控的场景下，MCP 让四件事更容易实现：限制 agent 能访问哪些外部服务、在不暴露 API key 的前提下处理认证、为用户提供连接并认证更多服务的合理 UI，以及强有力的审计日志。 这篇文章出现在一场正在进行的争论之中：在 Claude Code、OpenClaw 这类终端编码 agent 可以凭借完整互联网访问直接调用 API 的今天，MCP 是否还有存在意义。Willison 的反驳把讨论从编码 agent 转向托管型或受管制的 agent 产品——在这类场景中，受限访问范围、凭证隔离、面向用户的连接流程和审计追踪等企业级需求才是决定性因素。 Willison 点名了他认为拥有“不受限互联网访问”的 agent——Claude Code、Codex、Meta Muse 和 OpenClaw——并把这种运行方式形容为相对 MCP 所支持模式的“YOLO”。值得注意的是，这些只是片段式评论而非完整的技术文章，因此他列出的四项好处（访问控制、不暴露密钥的认证、连接 UI、审计日志）是主张而非带有实现细节的论证。</p>
<div class="news-background"><strong>背景</strong> MCP（Model Context Protocol，模型上下文协议）是 Anthropic 于 2024 年 11 月推出的开放标准与开源框架，旨在标准化 LLM 等 AI 系统连接外部工具、数据源和系统的方式。Claude Code 这类基于终端的 agentic 编码工具，会通过自行规划步骤并调用读取文件、执行命令或编辑代码的工具来完成任务，且通常拥有较宽泛的网络访问权限。OpenClaw 则是一个免费的开源个人 AI agent，以 WhatsApp、Telegram 等消息平台作为主要交互界面，通过 LLM 执行任务。当前的争论正是：当 agent 能够自行访问任意 API 之后，是否还需要一个标准化的连接协议。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro">What is the Model Context Protocol (MCP)? - Model Context Protocol</a></li>
<li><a href="https://www.anthropic.com/news/model-context-protocol">Introducing the Model Context Protocol \ Anthropic</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#MCP</span> <span class="tag">#AI agents</span> <span class="tag">#protocols</span> <span class="tag">#developer tooling</span> <span class="tag">#Simon Willison</span></div>
</article>
<hr>

<a id="item-21"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://huggingface.co/blog/MultiverseComputingCAI/pruning-llms-like-a-physicist-block-removal-as-an">Multiverse 将 LLM 块剪枝重构为 Ising 优化问题</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Hugging Face Blog</span><span class="news-time">Sep 21, 13:44</span></div>
<p class="news-summary">Multiverse Computing 在 Hugging Face 发布博客，介绍其论文《LLM Compression by Block Removal with Constrained Binary Optimization》，将“删除哪些 transformer 块”这一问题重构为可直接映射到 Ising glass 的约束二元优化（CBO）问题。作者称在 Llama-3.3-70B-Instruct 上做 50% 压缩时，其方法在 MMLU 上比最好的同类块删除方法高出近 23 个百分点，代码已在 GitHub 开源。 块删除是压缩大语言模型越来越流行的手段，但现有方法要么独立评估每个块，要么只删除一段连续的块，导致大量存在耦合关系的搜索空间未被探索。把块选择建模为 Ising/QUBO 问题，使从业者可以复用成熟的经典、量子启发式乃至量子求解器；而在深度压缩区间报告的显著 MMLU 提升，说明这一重构可能实质性地改变激进剪枝的做法。 博客称，精确求解器处理 Llama-3.3-70B 的 80 个块（约 290 亿种配置）大约需要两天；之后问题被改写为 QUBO 形式，将约束吸收进惩罚项，从而可使用 quantum annealing、QAOA、tabu search 和专用分支定界求解器。值得注意的是，作者强调他们并不需要真正的基态，只需要一种快速生成若干优质低能态的方法；据称开源 tabu 求解器在已用暴力枚举验证的最难案例上能在数秒内达到最低能态，而最佳配置往往是一个激发态而非基态。</p>
<div class="news-background"><strong>背景</strong> 块删除通过整块删掉 transformer 块（层）而非单个权重来压缩大语言模型。博客把 magnitude、sensitivity 或“block influence”等现有评分启发式称为 mean-field 方法：就像物理学中的平均场理论那样，它们把每个块的贡献视为彼此独立。Ising 模型用相互作用的二元自旋系统表示物理对象，其能量取决于两两耦合；Ising glass（自旋玻璃）则是具有阻挫、全连接相互作用的无序版本；QUBO 是与之等价的二次二元优化形式，可交给退火机以及 tabu search、QAOA 等求解器处理。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ising_model">Ising model - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Spin_glass">Spin glass - Wikipedia</a></li>
<li><a href="https://link.springer.com/rwe/10.1007/978-1-4419-1153-7_1034">Tabu Search | Springer Nature Link</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#LLM compression</span> <span class="tag">#pruning</span> <span class="tag">#combinatorial optimization</span> <span class="tag">#Ising model</span> <span class="tag">#open-source</span></div>
</article>
<hr>

<a id="item-22"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.technologyreview.com/2026/09/21/1144166/border-towers-surveillance-investigation/">调查：AI 边境监控塔未能阻止移民死亡</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">MIT Technology Review</span><span class="news-time">Sep 21, 12:00</span></div>
<p class="news-summary">MIT Technology Review 与 Times of San Diego 合作开展为期一年的&quot;Dying on Camera&quot;调查，于 2026 年 9 月 21 日发布报道，指出由 Anduril 制造、美国海关与边境保护局（CBP）部署的 AI 边境监控塔，未能兑现其宣称的更快人道救援响应。报道聚焦何塞·莫拉莱斯·贝尔纳尔（José Morales Bernal）：他于 2024 年 4 月 8 日、32 岁生日前一天穿越进入新墨西哥州南部，尽管身处三座监控塔的探测范围内，最终仍然死亡。 这项调查检验了 AI 政府监控系统是否兑现其宣称的人道主义理由，而不仅是安全承诺，并触及围绕自动化侦测系统问责、以及数十亿美元边境技术开支的更广泛争论。其结论对 CBP 正在推进的监控塔扩建计划，以及包括 Anduril 在内、以&quot;拯救移民生命&quot;为宣传点的厂商都具有现实影响。 报道将技术承诺与实际结果相对照：CBP 在 2021 年关于新墨西哥州 Santa Teresa 站附近监控塔的新闻稿中称，该技术&quot;可以并将拯救移民生命&quot;；2024 年一份针对加州监控塔的许可申请更明确表示，若有人出现在监控塔视野内并显得处于困境，将派遣急救人员或第一响应者前往救助；Anduril 在 2021 年也宣称其软件能让探员走出通信运营中心、进入现场。报道还提到，截至 2023 年 8 月，CBP 在边境沿线安装了约 170 个救援信标，但退休边境巡逻主管 Mario Agundez 表示这些设备效果不佳，因为人们会避开它们，或者&quot;死在它们旁边&quot;。</p>
<div class="news-background"><strong>背景</strong> 美国南部边境长约 1951 英里，CBP 越来越依赖&quot;自主监控塔&quot;（Autonomous Surveillance Towers，AST）：这类杆载摄像与传感器设备利用 AI 自动侦测并跟踪人员，将实时视频传回控制室，并向探员配发的政府智能手机推送警报。Anduril 的 Lattice 软件是许多此类监控塔背后的平台，可将分散传感器的数据汇聚到统一的集成层。CBP 自 1998 年起还设有名为 BORSTAR 的搜救单位；2026 年，该机构在总额 18 亿美元的&quot;统一监控塔与监视&quot;（Consolidated Tower &amp; Surveillance）合同框架下，向 General Dynamics Information Technology 授予了一份价值最高达 1.15 亿美元的任务订单，用于部署下一代自主监控塔。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.technologyreview.com/2026/09/21/1144166/border-towers-surveillance-investigation/">The US spent billions on border surveillance. Why can’t it ...</a></li>
<li><a href="https://www.theguardian.com/us-news/2022/sep/16/anduril-towers-surveillance-us-mexico-border-migrants">‘Never sleeps, never even blinks’: the hi-tech Anduril towers spreading...</a></li>
<li><a href="https://www.defenseadvancement.com/news/next-gen-surveillance-towers-edge-ai-to-strengthen-us-border-security/">Next-Gen Surveillance Towers &amp; Edge AI to Strengthen US ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI surveillance</span> <span class="tag">#border security</span> <span class="tag">#AI ethics</span> <span class="tag">#government technology</span> <span class="tag">#investigative journalism</span></div>
</article>
<hr>

<a id="item-23"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.theverge.com/ai-artificial-intelligence/998090/un-ai-panel-hugging-face-hack-precautionary-principle">联合国科学小组：AI 保障措施不能等待科学确定性</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">The Verge AI</span><span class="news-time">Sep 21, 10:18</span></div>
<p class="news-summary">联合国人工智能独立国际科学小组发布了首份专题简报，主张各国政府不应等到完全弄清 AI 相关事件的确切成因与机制之后，才着手为先进 AI 建立更强有力的保障措施。该简报出炉前，OpenAI、Anthropic、Google、Meta 等公司均出现了已记录在案的事件，此外还有此前 Hugging Face 遭黑客入侵一事；简报同时呼吁在 AI 安全上投入更多资源、加强国际协调与问责。 这份简报在世界领导人齐聚纽约出席联合国大会、美中两国准备就 AI 举行会谈之际，进一步把 AI 推上全球外交议程的首要位置。它以联合国的正式身份强化了“安全措施不应被推迟”的立场，这一立场可能影响各国政府的监管设计，即便各国的法律路径仍各不相同。 该小组援引了最早写入 1992 年联合国《里约环境与发展宣言》的预防原则（precautionary principle），即科学上的不确定性不能成为推迟应对潜在严重或不可逆损害的理由；报告把“失控风险”正视为这类问题——即使其发生概率在科学上仍不确定，潜在危害也可能是灾难性或不可逆的。简报也承认各国采取的法律路径各不相同，但仍呼吁在安全与问责方面加强国际协调。</p>
<div class="news-background"><strong>背景</strong> 联合国人工智能独立国际科学小组于去年成立，是联合国首个全球性的人工智能科学机构。据报遭黑客入侵的 Hugging Face 是一家公司，同时也是一个开源社区，提供托管机器学习模型、数据集以及构建 AI 应用的工具。简报还提到“AI 智能体集群”（swarms of AI agents），即多个自主 AI 智能体相互协调、共同执行任务的群体，报告称这类集群曾接管在线留言板。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hugging_Face">Hugging Face - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/hugging-face">What is Hugging Face? | IBM</a></li>
<li><a href="https://www.thesys.dev/blogs/agent-swarms">Agent Swarms 101: Building Scalable Multi-Agent AI Systems</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI safety</span> <span class="tag">#AI governance</span> <span class="tag">#United Nations</span> <span class="tag">#AI regulation</span> <span class="tag">#cybersecurity</span></div>
</article>
<hr>

<a id="item-24"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.theverge.com/tech/998078/amazon-blocks-meta-muse-ai-agent-shopping">亚马逊以「未授权访问」为由封禁 Meta 的 Muse AI 购物代理</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">The Verge AI</span><span class="news-time">Sep 21, 09:21</span></div>
<p class="news-summary">亚马逊已阻止 Meta 的 Muse AI 代理在其电商平台上购物：从周日开始，Muse 用户会看到弹窗提示，称「未授权 AI 代理的持续访问违反了亚马逊的使用条件，而我们的客户已同意这些条件」。据 GeekWire 报道，Meta 并未事先通知亚马逊 Muse 将访问其商店；亚马逊还对 Muse 在浏览时不表明自身身份、并似乎会获取客户凭证等隐私与安全问题表示担忧。 这是自主 AI 购物代理与大型电商平台之间新兴冲突的最新升级：零售商正试图让交易继续发生在自己的渠道内，而非通过第三方代理完成。这也表明，平台使用条款的执行、代理身份标识以及数据访问权限，正在成为决定 agentic AI 电商能否开展的关键战场。 一位未具名的亚马逊发言人向 GeekWire 表示，代客户进行购买的第三方应用「应当公开运作，并尊重服务提供方是否参与的决定」。Meta 在发布 Muse 时表示，该代理无法看到安全登录信息或银行卡支付信息；The Verge 称在测试中成功用 Muse 从亚马逊购买了背心，但另有报道担忧 Muse 在没有获得必要访问权限的情况下仍能查看用户消息内容。</p>
<div class="news-background"><strong>背景</strong> Muse 是 Meta 推出的个人 AI 代理，旨在代替用户完成日常任务，包括在第三方网站上购物。亚马逊的《使用条件》规定了客户及第三方软件如何访问其商店；亚马逊一直在打压代用户购物的 agentic 服务——去年 11 月它曾就 Perplexity 的 Comet 购物体验提起诉讼，而今年 8 月法官在该案中支持了 Perplexity。此外，自 7 月以来，亚马逊的确认邮件明显变得信息稀疏，省略了具体商品名称和商品图片，以限制这些信息被外部 AI 服务抓取。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://ai.meta.com/muse/">Muse: Meta&#x27;s personal AI agent, features &amp; capabilities</a></li>
<li><a href="https://en.wikipedia.org/wiki/Perplexity_AI">Perplexity AI</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI agents</span> <span class="tag">#Amazon</span> <span class="tag">#Meta</span> <span class="tag">#platform policy</span> <span class="tag">#e-commerce</span></div>
</article>
<hr>

<a id="item-25"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://github.com/acsandmann/rift/">Rift：面向 macOS 的全新多布局平铺窗口管理器</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Sep 21, 18:02</span></div>
<p class="news-summary">Rift 是一款全新的开源 macOS 平铺窗口管理器，最初 fork 自 glide-wm 但此后已有显著差异，提供多种布局风格，包括类 i3/sway 的平铺、类 bspwm 的二叉空间分割（BSP）、浮动窗口框架、类 dwm 的 master-stack、类 niri 的滚动列以及手风琴式 stack 布局。它带有菜单栏图标用于切换工作区和布局，支持配置热重载、从菜单栏或 CLI 保存与恢复可复用布局，并提供基于 Mach port 的 IPC，便于 sketchybar 等第三方程序调用。 Rift 声称可在 macOS 开启“显示器具有单独的空间（Displays have separate Spaces）”的情况下正常工作，而作者表示其他主流 macOS 窗口管理器做不到这一点，同时它也无需关闭系统完整性保护（SIP）。这一组合直击 macOS 高级用户的长期痛点：他们希望在保留一块屏幕使用原生全屏、另一块屏幕继续工作的同时使用平铺式窗口管理。 Rift 依赖由 yabai 及其他项目逆向工程得到的私有、未公开 API——作者认为这是有意为之，因为 macOS 本身构建于这些 API 之上，因此更可靠、性能更好——并且它既不隶属于 glide-wm 也不隶属于 yabai。其他值得注意的功能包括鼠标焦点跟随并自动提升窗口、通过触控板手势切换工作区以及流畅的动画效果；不过该条目未提供基准测试、版本号或发布日期等具体信息。</p>
<div class="news-background"><strong>背景</strong> 平铺窗口管理器会自动把应用窗口排列成互不重叠的框架，通常依据数学公式计算布局，而不是像堆叠式窗口管理器那样让用户自由拖动窗口。macOS 本身并未内置平铺窗口管理器，因此长期以来由第三方工具填补这一空白，这在 macOS 高级用户中是一个规模不大但非常忠实的细分群体。Mach port 是 macOS 底层 Mach 内核（XNU）中基于句柄的进程间通信原语，被形容为轻量但文档匮乏，因此 Rift 的 IPC 机制对希望集成外部状态栏的开发者而言值得关注。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tiling_window_manager">Tiling window manager</a></li>
<li><a href="https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/Mach/Mach.html">Mach Overview - Apple Developer</a></li>
<li><a href="https://web.mit.edu/darwin/src/modules/xnu/osfmk/man/">Mach Kernel Interface Reference Manual - MIT</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#macOS</span> <span class="tag">#window manager</span> <span class="tag">#tiling</span> <span class="tag">#open source</span> <span class="tag">#desktop</span></div>
</article>
<hr>

<a id="item-26"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://remy.wang/blog/ra-ra.html">relation algebra 与 relational algebra：两个易混淆形式系统的辨析</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Sep 21, 17:01</span></div>
<p class="news-summary">在一篇博客文章中，Remy Wang 解释了人们长期混淆 relation algebra（Tarski 研究的数学/逻辑结构）与 relational algebra（Codd 提出的数据库查询理论）的现象，并指出 Wikipedia 以及数据库领域评论者 Jamie Brandon 都曾将两者混为一谈。他还提到，在他参与合著的一篇近期论文中提出的 Prela，似乎是自 Dirk Van Gucht 的 IUGQL 以来第一个基于 relation algebra 的查询语言。 这一区分之所以重要，是因为这两套系统具有不同的表达能力与不同的理论渊源，但名称却几乎相同，混淆它们可能同时误导数据库研究者和逻辑学家。这也说明 relation algebra 正悄然进入计算机科学领域，从 Alloy 分析器所称的 “relational logic” 一直到 Prela 这样的近期数据库查询语言。 Codd 定理指出，relational algebra 等价于 domain independent relational calculus，即一阶逻辑查询中性质良好的一部分；而 relation algebra 等价于 FOL^3，即限定一阶逻辑最多只能使用 3 个不同变量（但量词可以任意深度嵌套），并且可以通过增加 fork 算子扩展到与完整 FOL 相当的表达能力。文章还指出了另一处术语陷阱：Tarski 把 relation algebra 称为 “the calculus of relations”，而这又与数据库理论中的 relational calculus 不是一回事。</p>
<div class="news-background"><strong>背景</strong> Relational algebra 是 Edgar F. Codd 在 1970 年论文《A relational model of data for large shared data banks》中提出的理论，用代数结构来建模数据并定义查询，是关系型数据库和 SQL 的基础。Relation algebra 则是另一条传统，源自 19 世纪 De Morgan、Peirce、Schröder 的代数逻辑，并由 Alfred Tarski 及其学生从 1941 年关于关系演算的论文开始以公理化方式发展。两个名字只差两个字母，文章认为 Codd 在命名时甚至可能并不知道 relation algebra 的存在。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Relation_algebra">Relation algebra - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Relational_algebra">Relational algebra - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Alfred_Tarski">Alfred Tarski - Wikipedia</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#relation algebra</span> <span class="tag">#relational algebra</span> <span class="tag">#database theory</span> <span class="tag">#logic</span> <span class="tag">#terminology</span></div>
</article>
<hr>

<a id="item-27"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://anishathalye.com/optimal-trace/">Anish Athalye 发布 Optimal Trace 路线规划工具</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Sep 21, 15:13</span></div>
<p class="news-summary">Anish Athalye 发布了一款开源工具和纯客户端网页应用，可计算覆盖某一区域内全部步道的最优路线，并可针对总距离、爬升高度或预估行进时间等目标进行优化。他用该工具规划并完成了一次 Angel Island 的 trace 路线：该岛有 19.4 英里的独立道路与步道，规划路线总长 23.8 英里（其中 4.4 英里为重复走过的路段），实际完成距离为 24.6 英里，用时约五小时。 该项目将经典的 Chinese postman problem 应用于徒步和越野跑这一细分领域，把繁琐的手工规划任务转化为可求解的优化问题。最终成果是一个免费、基于浏览器的工具，可帮助徒步和跑步爱好者规划 trace 及类似的“走遍全部步道”路线，而无需专业软件。 该工具使用 OpenStreetMap 的步道数据，通过 USGS 3DEP API 获取精细高程数据，并使用 Tobler&#x27;s hiking function 结合移动平均来平滑高程剖面以估算行进时间；为避免严重高估爬升，需要设置 2 米的最小变化阈值。整个工具完全在客户端运行，使用无需认证的公共 API，可导出 GPX（包括将路线切成 4 英里一段的 split GPX 模式），源代码已在 GitHub 上公开，不过网页应用尚未针对移动端优化。</p>
<div class="news-background"><strong>背景</strong> Trace（历史上曾被称为 redlining）是一种徒步挑战，目标是走遍某一区域内的所有步道；这项玩法起源于新罕布什尔州的徒步社群，其中 White Mountains 的一次 trace 需要覆盖超过 1450 英里的独立步道。手工规划这样的路线十分困难，因为需要决定纳入哪些步道、如何把它们连接起来，同时尽量减少重复路段。距离和爬升这两类优化目标对应于 Chinese postman problem，这是一个著名的组合优化问题，即寻找一条经过图中每条边的最短回路。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://notchhostel.com/blog/im-not-racist-im-redlining/">I’m not Racist, I’m Redlining. - The Notch Hostel</a></li>
<li><a href="https://www.summitsinsolidarity.org/blog/im-not-racist-im-redlining">I’m Not Racist, I’m Redlining. - Summits In Solidarity Redlining Heritage Trail - Central District — Washington ... Redlining Guide to Hiking the White Mountains - SectionHiker Redlining Heritage Trail - Pioneer Square — Washington Trails ... What is &quot;Redlining&quot;? - New England &amp; New York Backcountry ... hiking patch red lining patches white mountains new hampshire ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#optimization</span> <span class="tag">#routing</span> <span class="tag">#algorithms</span> <span class="tag">#geospatial</span> <span class="tag">#side-project</span></div>
</article>
<hr>

<a id="item-28"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://mattgreer.dev/blog/making-a-game-for-gba-and-pc/">开发者用同一套 C 代码同时打造 GBA、e-Reader 与 PC 游戏</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Sep 21, 16:02</span></div>
<p class="news-summary">开发者 Matt Greer 发布博客文章，解释他为何以及如何用同一套共享 C 代码，为新游戏 Eridin 同时开发 Game Boy Advance / Nintendo e-Reader 版本和 PC 版本。GBA 一端使用 devkitPro 与 libtonc（与他此前的作品 Pixel Pup 相同的工具链），PC 一端使用 SDL2，并通过一个公共 API 层对接两端；这个 API 层受 e-Reader 自身内置游戏 API 的启发，具体实现分别放在 sprites.h 这类头文件对应的后端中。 这是一个具体而实用的跨平台游戏开发案例研究：目标平台差异极大，一端是 2001 年问世、分辨率与 60 fps 都受限的掌机，另一端是几乎没有限制的 PC。它展示了独立开发者如何对冲单一小众平台的发行风险。对于复古游戏与自制程序（homebrew）开发者而言，文中所描述的 API 分层做法是一种可复用的模式：既保持一份游戏逻辑代码，又让每个平台发挥自身优势。 Greer 表示两个版本差异最大的地方在于渲染：PC 版使用 subpixel（子像素）来让滚动更平滑，且不锁定 60 帧，能以更高分辨率渲染（例如 1200x800，缩放系数可调）；而 GBA 版的画面滚动方式明显更生硬，并且被限制在 60 fps。他还特意避免让 PC 版仅因为 e-Reader 版需要扫描卡片而照搬这一机制，否则会显得像噱头；他提到 REKKR 等受经典 Doom/Heretic 风格启发的作品作为参考，并说明文中展示的截图属于早期 mock-up，后续还会变化。</p>
<div class="news-background"><strong>背景</strong> Nintendo e-Reader 是 Game Boy Advance 的外设，2001 年 12 月在日本发售、2002 年 9 月在北美发售，它通过 LED 扫描器读取印在纸质 e-Reader 卡上、以点阵码（dot code）形式编码的数据，可用于解锁道具、关卡或小型游戏。由于这些点阵码必须能被稳定扫描，把卡片印制到可销售的质量异常困难——Greer 提到他此前的 e-Reader 作品 Pixel Pup 已经全部完成、甚至连卡都印好了，却因为合作印刷厂更换设备、无法再生产可扫描卡片而取消发行。devkitPro 为任天堂主机提供免费的自制程序工具链与库，与 libtonc 一起是常见的用 C 开发 GBA 软件的方式；SDL2 则是 PC 应用广泛使用的跨平台多媒体库。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nintendo_e-Reader">Nintendo e-Reader</a></li>
<li><a href="https://devkitpro.org/">devkitPro - Portal</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#game development</span> <span class="tag">#cross-platform</span> <span class="tag">#GBA</span> <span class="tag">#C</span> <span class="tag">#retro development</span></div>
</article>
<hr>

<a id="item-29"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://vincent.bernat.ch/en/blog/2026-goatcounter">博主详解如何在 NixOS 上用 GoatCounter 搭建无机器人的自托管分析</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Sep 20, 22:51</span></div>
<p class="news-summary">Vincent Bernat 发布了一篇约 21 分钟阅读量的技术指南，讲述他如何用开源、隐私友好的 GoatCounter 分析平台取代原先基于 GoAccess 的日志分析方案，并以声明式方式部署在 NixOS 上。他的方案包括一个更激进过滤机器人的自定义 JavaScript 客户端、为禁用 JavaScript 的读者准备的 CSS 回退方案，以及在该博客五台 Web 服务器上各自运行的本地代理，此外还用 Litestream 备份 SQLite 数据库并给出了恢复命令。 AI 爬虫曾把他的访问量虚增到每天约 2000 次，这也说明对于小型独立站点而言，传统的日志分析或基于 JavaScript 的分析已变得多么不可靠。这篇文章为那些希望在不使用 cookie、不存储 IP、也不依赖第三方分析厂商的前提下获得准确数据的开发者，提供了一套具体且可复现的实践模式。 GoatCounter 不存储 IP 地址、也不使用 cookie，而是根据 user agent 和 IP 地址生成一个有效期为 8 小时的会话标识符；它以单个二进制文件形式发布，后端使用 SQLite 或 PostgreSQL，给页面增加的体积仅约 3.5KB。Bernat 指出其功能集相对克制，但对博客而言已足够，并把 Umami、Plausible 和 Rybbit 列为复杂度递增的隐私友好替代品；他的 NixOS 配置通过 Colmena 的 deployment keys 管理密钥，并以只读方式 bind-mount 进容器。</p>
<div class="news-background"><strong>背景</strong> GoatCounter 是由 Martin Tournoij（arp242）创建的开源 Web 分析项目，定位为 Google Analytics 和 Matomo 的替代品，提供靠捐赠支持免费的托管服务，也可自托管；它可以通过 JavaScript 代码片段、后端中间件集成，或导入服务器日志文件来收集数据。NixOS 是基于 Nix 包管理器构建的 Linux 发行版，采用声明式的函数式配置，并支持原子升级与回滚。Bernat 此前使用的 GoAccess 是一款基于终端的实时 Web 日志分析器，可直接解析访问日志。促使他更换方案的大背景是 AI 爬虫的兴起——尽管他尝试过滤，这些流量仍让他此前的统计数据失去意义。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.goatcounter.com/">GoatCounter – open source web analytics</a></li>
<li><a href="https://github.com/arp242/goatcounter">GitHub - arp242/goatcounter: Easy web analytics. No tracking ... GoatCounter: Free, Open-Source Analytics Without Cookies Count Your Readers Without Spying on Them: Self-Hosted ... GoatCounter: Open Source alternative to Google Analytics Bot-free self-hosted analytics with GoatCounter on NixOS</a></li>
<li><a href="https://en.wikipedia.org/wiki/NixOS">NixOS - Wikipedia</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#self-hosted</span> <span class="tag">#analytics</span> <span class="tag">#nixos</span> <span class="tag">#goatcounter</span> <span class="tag">#privacy</span></div>
</article>
<hr>

<a id="item-30"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.philipzucker.com/lambda_miller_egg/">Lambda MicroEgg 为 e-graph 加入 alpha 感知的绑定器</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Sep 20, 16:04</span></div>
<p class="news-summary">Philip Zucker 发布了 Lambda MicroEgg，这是一个支持良作用域（well-scoped）、alpha 感知绑定器的 e-graph 工具，带有 s-expression 前端、公开代码仓库（philzook58/lambda-microegg）以及 WASM 演示。它大量基于 Max 的 microegg，但新增了内建绑定器、高阶 Miller 模式，以及重写右侧的避免捕获替换（capture-avoiding substitution）。 在把 e-graph 与等式饱和（equality saturation）用于编译器和程序变换时，如何处理绑定器与变量作用域一直是长期痛点，因此一个可用工具加演示为程序语言社区提供了处理 lambda 演算风格重写的具体起点。它是一项小众但内容扎实的贡献，而非影响广泛的行业级发布。 lifting 被存储为从 u32 Id 中借用的一个字节，因此作者希望开销很低；在一次 AC-10 饱和测试中，该工具比 egg 慢（类似任务约 0.6s），但“并非极其慢”，某次运行报告为 5 轮、17 次 union、9 个类、22 个 e-node，match/apply/rebuild 耗时约 15–22µs。一个有意的限制要求 Miller 元变量必须按其绑定的顺序应用，这在诸如 (foo (lam x (lam y (?a x y))) (lam x (lam y (?a y x)))) 这样的非线性模式下损失了一些能力，除非像 Max 提议的那样允许在模式中进行项构造。</p>
<div class="news-background"><strong>背景</strong> e-graph 是一种数据结构，可以紧凑地存储某种语言中项之间的等价关系，并支撑等式饱和（equality saturation）等技术：重写规则以非破坏性方式应用，同时保留大量等价表达式。lambda 演算作为函数与变量绑定的形式模型，对这类工具而言很棘手，因为绑定变量可以被重命名（alpha 等价），而替换必须避免意外捕获变量。Zucker 早前关于“lifting e-graphs”的工作提出通过 thinning 位向量把函数式 lifting 的概念内建进结构中，而 microegg 是一个小型 e-graph 实现，本项目在其上扩展了绑定器支持。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.philipzucker.com/lambda_miller_egg/">It’s an egraph that supports well - scoped alpha aware binders .</a></li>
<li><a href="https://en.wikipedia.org/wiki/E-graph">E-graph - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2606.22734">Lifting E - Graphs : A Function Isn’t a Constant</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#e-graphs</span> <span class="tag">#lambda-calculus</span> <span class="tag">#program-transformation</span> <span class="tag">#compilers</span> <span class="tag">#formal-methods</span></div>
</article>
<hr>