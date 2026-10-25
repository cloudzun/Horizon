---
layout: default
title: "Horizon 每日速递：2026-10-25"
date: 2026-10-25
lang: zh
---

> 📅 2026-10-25 · 从 61 条资讯中精选出 20 条重要内容

---

1. [Moderna 与 Merck：mRNA 癌症疫苗使黑色素瘤死亡与复发风险降低 42%](#item-1) <span class="score-badge score-high">9.0</span>
2. [Goose：无需堆、GC 与生命周期标注的内存安全系统语言](#item-2) <span class="score-badge score-mid">8.0</span>
3. [Sebastian Raschka 发布 11 小时视频课程：从零构建推理模型](#item-3) <span class="score-badge score-mid">8.0</span>
4. [C\+\+26 ISO 投票未获通过，成员国反对票达 41%](#item-4) <span class="score-badge score-mid">8.0</span>
5. [手写 SIMD FAST 检测器让 2 美元 ESP32\-S3 的特征检测速度翻倍](#item-5) <span class="score-badge score-mid">8.0</span>
6. [据报印度政府网站仍在提供已吊销的 eMudhra 证书](#item-6) <span class="score-badge score-mid">8.0</span>
7. [node2shell Brotli 漏洞 CVE\-2026\-111497 亦影响 Python 及其他解码器](#item-7) <span class="score-badge score-mid">8.0</span>
8. [rqlite 作者回顾分布式 SQLite 十二年演进历程](#item-8) <span class="score-badge score-mid">8.0</span>
9. [十年前的 Inception v3 CNN 在皮肤癌诊断上胜过前沿 LLM](#item-9) <span class="score-badge score-mid">7.0</span>
10. [俄勒冈警方为一名警员的记录开出 250 万美元、44,816 小时的报价](#item-10) <span class="score-badge score-mid">7.0</span>
11. [Dan Luu 呼吁软件开发者树立更高目标](#item-11) <span class="score-badge score-mid">7.0</span>
12. [伯克利数学教授博切尔兹称 AI 时代批改作业“没有意义”](#item-12) <span class="score-badge score-mid">7.0</span>
13. [Cerebras 详解如何在自家芯片上部署万亿参数前沿模型](#item-13) <span class="score-badge score-mid">7.0</span>
14. [三星电视 root shell 引发对端侧 TensorFlow Lite 追踪的争论](#item-14) <span class="score-badge score-mid">7.0</span>
15. [Google AI Overviews 正在掏空出版商的流量](#item-15) <span class="score-badge score-mid">7.0</span>
16. [POSIX wordexp\(3\) 对不可信输入不安全，即使启用 WRDE\_NOCMD 亦然](#item-16) <span class="score-badge score-mid">7.0</span>
17. [Zig 实现部分运算符优先级，十年提案落地](#item-17) <span class="score-badge score-mid">7.0</span>
18. [一次 glibc pthread 改动意外破坏了 Chromium 音频](#item-18) <span class="score-badge score-mid">7.0</span>
19. [Astral 推出 uv 与 ty 实验性集成预览](#item-19) <span class="score-badge score-mid">7.0</span>
20. [SimCity 如何在 16 MHz 的 386SX 上跑完整城市模拟](#item-20) <span class="score-badge score-mid">7.0</span>

---

<a id="item-1"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://arstechnica.com/health/2026/10/personalized-mrna-cancer-vaccine-cut-melanoma-death-recurrence-by-42/">Moderna 与 Merck：mRNA 癌症疫苗使黑色素瘤死亡与复发风险降低 42%</a><span class="score-badge score-high">9.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">_Microft</span><span class="news-time">Oct 25, 19:29</span></div>
<p class="news-summary">Moderna 与 Merck 报告称，其个性化 mRNA 癌症疫苗与 Keytruda 联合使用，在一项试验中使黑色素瘤患者的死亡与复发风险降低了 42%。这一结果被广泛视为 mRNA 肿瘤疗法的重要临床里程碑，不过所提供的材料中并未包含完整的试验细节。 如果这一结果能够站得住脚，它将成为个性化 mRNA 疫苗能在现有免疫疗法基础上带来实质性获益的最清晰例证之一，从而强化 mRNA 平台在传染病之外的价值。这对黑色素瘤患者和肿瘤科医生都很重要，也关系到两家公司的商业前景——它们的 mRNA 业务此前与新冠疫苗需求紧密绑定。 标题中的 42%是相对风险下降而非绝对风险下降；有评论者指出，单用 Keytruda 时复发或死亡的绝对风险约为 30%，而 Keytruda 联合 intismeran（讨论中提到的该疫苗名称）后为 18%。由于每一剂疫苗都围绕患者自身的肿瘤定制，其生产与物流模式与常规现货疫苗差别很大；同时，所提供材料并未包含试验分期、受试者人数或随访时长等信息。</p>
<div class="news-background"><strong>背景</strong> 个性化 mRNA 癌症疫苗的做法是：对患者肿瘤进行测序以识别新抗原（即该癌症特有的突变蛋白），再将这些靶点编码进人工合成的 mRNA 分子中，使免疫系统学会攻击肿瘤。截至 2024 年，已有多款此类疗法在黑色素瘤、胰腺癌和头颈癌中开展临床试验。Keytruda（pembrolizumab）是一种人源化单克隆抗体，通过抑制 PD-1、阻断 PD-L1/PD-L2 相互作用，帮助恢复 T 细胞介导的肿瘤杀伤。相对风险下降与绝对风险下降的区别在此至关重要：相对风险的较大降幅，在基线风险不同的情况下，可能只对应一个不大的绝对变化。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Personalized_mRNA_cancer_vaccine_therapy">Personalized mRNA cancer vaccine therapy</a></li>
<li><a href="https://en.wikipedia.org/wiki/Pembrolizumab">Pembrolizumab - Wikipedia</a></li>
<li><a href="https://casrai.org/guides/absolute-risk-reduction-relative-risk-and-nnt">Absolute Risk Reduction, RRR &amp; NNT — CASRAI</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者普遍印象深刻，但对数字保持谨慎，其中一位指出复发或死亡的绝对风险从约 30%降至 18%，并认为如果真实世界结果能够维持，这一差异会相当明显。其他人讨论了 Moderna 按需定制的生产模式——更像即时的定制服务而非传统疫苗实验室，也提到了 BioNTech 的竞争性个性化疫苗管线，并观察到数据泄露后 Moderna 股价反而下跌，原因是市场预期已被抬到“治愈癌症”的高度。还有一些评论带有个人色彩，希望该疗法能尽快惠及患者。</div>
<div class="news-tags"><span class="tag">#mRNA vaccines</span> <span class="tag">#cancer research</span> <span class="tag">#oncology</span> <span class="tag">#biotech</span> <span class="tag">#clinical trials</span></div>
</article>
<hr>

<a id="item-2"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://aardappel.github.io/goose/">Goose：无需堆、GC 与生命周期标注的内存安全系统语言</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 25, 20:10</span></div>
<p class="news-summary">Goose 是一门新发布的系统编程语言，由 Lobster 语言的作者推出，具备内存安全性，但不使用堆分配器、垃圾回收、引用计数、析构函数，也没有生命周期标注或 `unsafe` 代码。在该仓库自带的 16 项基准测试中，Goose 据称分别达到惯用 C++ 的 3.3 倍、手工优化 C++ 的 1.16 倍、最佳安全 Rust 的 1.12 倍速度，同时内存占用分别少 1.9 倍、1.3 倍和 1.2 倍。 Goose 切入的是系统编程领域长期存在的矛盾：Rust 式的内存安全一直需要显式的生命周期标注和严格的别名规则，而带垃圾回收的语言又会带来运行时开销。如果这些性能与安全声明在作者自测之外也能成立，Goose 就提供了第三条路径——由编译器静态分配固定的数据栈，这可能会吸引那些既想要安全、又不愿承担 Rust 标注负担或 GC 运行时开销的系统开发者。 每个动态值都内联存放在由编译器分配的数据栈上：增长时只需推进指针，作用域结束时内存即被释放，而指向可增长数组内部的引用在数组存活期间始终有效，因此不需要 `reserve` 调用或下标变通方案。线程作为彼此独立的程序运行，没有共享的可变内存，只能通过按类型区分的队列交换值，且传递的值必须是任意深度上都不含引用的扁平数据；编译器本身用 C++ 编写并输出 C 代码，发布说明中还称该项目是一次「用 AI 实现新语言、而非复刻已有语言」的实验。</p>
<div class="news-background"><strong>背景</strong> 大多数语言管理动态内存的方式不外乎两种：一种是使用带垃圾回收器的堆，自动回收不可达对象；另一种是像 C 和 C++ 那样手动分配与释放。Rust 走了第三条路，借助编译期的所有权与借用检查实现确定性释放，但复杂代码往往需要显式写出生命周期标注，告诉编译器某个引用能有效多久。Goose 则提出由编译器静态分配少量可增长的数据栈，并推断每个引用根的归属，从而在去掉垃圾回收器和标注语法的同时，仍保持内存安全。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://aardappel.github.io/goose/">The Goose Programming Language · Goose</a></li>
<li><a href="https://github.com/aardappel/goose">GitHub - aardappel/ goose : The Goose Programming Language</a></li>
<li><a href="https://doc.rust-lang.org/book/ch10-03-lifetime-syntax.html">Validating References with Lifetimes - The Rust Programming ...</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 上的讨论整体充满好奇且大体具有建设性，作者本人也在帖中主持了 AMA；评论者对具体细节提出了质疑，例如 jcmoyer 认为教程的第一个示例在事实上就是错的，因为其中的 C++ 对照字符串符合小字符串优化（SSO）条件、并不会逐个分配堆内存，而 malisper 则追问：在栈数量固定的前提下，如何表示任意数量、大小动态变化的值，比如一个存放字符串的哈希表。也有人对该模型表示认可：anigbrowl 觉得把内存更像栈来管理在直觉上很有吸引力，pradn 则认为一门语言只覆盖受限的一类程序是可以接受的，前提是你能静态指明可增长内存区域的数量。</div>
<div class="news-tags"><span class="tag">#programming-languages</span> <span class="tag">#systems-programming</span> <span class="tag">#memory-management</span> <span class="tag">#rust</span> <span class="tag">#performance</span></div>
</article>
<hr>

<a id="item-3"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://magazine.sebastianraschka.com/p/building-reasoning-models">Sebastian Raschka 发布 11 小时视频课程：从零构建推理模型</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Ahead of AI (Sebastian Raschka)</span><span class="news-time">Oct 24, 11:14</span></div>
<p class="news-summary">Sebastian Raschka 为他的《Build a Reasoning Model (From Scratch)》内容发布了 8 讲配套编程视频，总时长约 11 小时，用 Python 和 PyTorch 完整讲解实现、评估与强化学习流程。该系列从一个预训练 LLM 出发，逐步搭建评估与改进方法，既是他早前《Coding LLMs from the Ground Up》课程的续篇，也可以独立观看。 如今几乎所有当代 LLM 都是推理模型或提供推理模式，但多数讲解仍停留在概念层面，因此这门课程对希望拿到可运行代码而非幻灯片的工程师和研究者具有实际价值。课程覆盖 KV cache、torch.compile 与验证器构建等工程细节，为从业者提供了一条可复现的路径，去掌握平时只在论文中描述的技术。 课程从文本分词、下载 Qwen3 权重、检查张量形状与 logits 开始，随后讲解贪心解码与流式生成、end-of-sequence 处理、加入 KV cache，并与 torch.compile 结合比较不同硬件的性能。课程还逐步构建了一个数学答案验证器，用于在 MATH-500 上评估模型，并在后续作为可验证奖励强化学习（RLVR）的奖励信号，最后几讲涉及蒸馏与检查点对比；Raschka 提到完整的文字讲解、图表和练习可在 Manning 与 Amazon 上的书中获得。</p>
<div class="news-background"><strong>背景</strong> 推理模型是指在给出答案前会生成较长中间推理过程的 LLM，其能力既可以在推理阶段通过 inference scaling 提升，也可以在训练阶段通过强化学习以及从更强模型蒸馏来改进。KV cache 是一种常见的推理优化手段，它缓存已经计算过的 key-value 状态，避免模型在每一步生成时重复计算历史 token；而贪心解码则是在每一步直接选择概率最高的下一个 token。可验证奖励强化学习（RLVR）利用可自动校验的答案来训练模型，这正是数学验证器既能做评估又能作为奖励来源的原因。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training">The State of Reinforcement Learning for LLM Reasoning</a></li>
<li><a href="https://developer.nvidia.com/blog/optimizing-inference-for-long-context-and-large-batch-sizes-with-nvfp4-kv-cache/">Optimizing Inference for Long Context and Large Batch Sizes ...</a></li>
<li><a href="https://heidloff.net/article/greedy-beam-sampling/">Decoding Methods for Generative AI | Niklas Heidloff</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 可见评论简短且以正面为主，读者表示这些内容让他们在假期有了期待。有评论者提问：小模型能否在普通笔记本上展现出真正的推理提升？但摘录中未见对该问题的回复，也没有出现实质性的技术争论。</div>
<div class="news-tags"><span class="tag">#reasoning models</span> <span class="tag">#LLMs</span> <span class="tag">#video course</span> <span class="tag">#reinforcement learning</span> <span class="tag">#machine learning education</span></div>
</article>
<hr>

<a id="item-4"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.linkedin.com/posts/robertseacord_balloting-has-completed-for-c26-unfortunately-activity-7519795140887035918-5PWL">C++26 ISO 投票未获通过，成员国反对票达 41%</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 24, 18:00</span></div>
<p class="news-summary">C++26 标准草案的投票已经结束，结果未获通过：在 20 个参与投票的 P-Member 中仅 12 个（60%）投赞成票，低于至少 66.66% 的要求；而在 22 个成员国机构中有 9 个（41%）投反对票，超过了 25% 的上限。公布这一结果的 Robert Seacord 称这是“C++ 社区有点悲伤的一天”，并希望委员会能够“弥合分歧、以建设性的方式继续前行”。 对于一个被广泛用于系统、游戏、嵌入式和金融软件的语言而言，ISO 投票未通过是一项重大的程序性挫折，也说明各国国家机构愿意否决它们认为存在争议的草案，而不是照单全收。由于编译器厂商已经在实现 C++26 的特性，这一结果引发了对草案中哪些部分能够保留、以及 WG21 内部共识机制是否需要重新审视的疑问。 按照所述规则，弃权的 P-Member 不计入 P-Member 投票，而评论者指出有 12 个国家弃权——其中有几个国家是因为无法形成统一的国内立场——这本身被认为是草案存在争议的信号。也有评论者质疑数字对不上：20 个投票者中 12 票赞成意味着 8 票反对，而成员国机构的统计却是 22 票中 9 票反对；不过无论怎么算，结果都明显偏离门槛。</p>
<div class="news-background"><strong>背景</strong> C++ 通过 ISO/IEC JTC1/SC22 第 21 工作组（WG21）进行标准化，这是一个负责制定语言标准的国际专家委员会；C++23 及计划中的 C++26 等大型修订都以 ISO 标准形式发布。在 ISO 中，各国家标准化机构按“一国一票”的原则对草案投票：P-Member 是参与成员国家机构，有义务对提交委员会表决的问题投票，而其他类别的成员投票权有限甚至没有。草案必须同时满足 P-Member 赞成比例门槛和成员国机构反对票上限，才能进入发布阶段，这也是本次结果中两个百分比分别报告的原因。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://open-std.org/jtc1/sc22/wg21/">ISO/IEC JTC1/SC22/ WG 21 - The C++ Standards Committee - ISOCPP</a></li>
<li><a href="https://www.iso.org/sites/ConsumersStandards/voting_iso.html">Voting and membership in ISO</a></li>
<li><a href="https://helpdesk-docs.iso.org/article/328-rules-to-manage-participation">Rules to manage participation - ISO Helpdesk Knowledge Base</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论情绪明显分为两派：一些人对此感到惋惜，追问在“同样的社会问题反复出现几十年”之后应当吸取什么教训，还有人表示多年来参与 contracts 提案工作的人所受到的对待“令人羞耻”。另一些人则认为否决是健康的信号，称 contracts 提案“争议极大且缺陷严重”，国家机构做对了，并认为这或许清楚地表明 WG21“会议室里的专家”式投票方式需要重新审视。</div>
<div class="news-tags"><span class="tag">#C++</span> <span class="tag">#ISO standards</span> <span class="tag">#WG21</span> <span class="tag">#programming languages</span> <span class="tag">#standards process</span></div>
</article>
<hr>

<a id="item-5"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://shraiwi.com/blog/simd-fast-esp32s3/">手写 SIMD FAST 检测器让 2 美元 ESP32-S3 的特征检测速度翻倍</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 25, 14:57</span></div>
<p class="news-summary">开发者 Shranav Palakurthi 编写了一个利用 ESP32-S3 的 128 位 SIMD 指令的 FAST 角点检测器，在他的测试中把吞吐量从参考实现的 5.1 MP/s 提升到 11.2 MP/s，约提升 220%。该 SIMD 版本处理一帧 QVGA（320x240）图像仅需约 6 毫秒，源码已随博客文章一并公开。 它说明在售价约 2 美元的微控制器上也能实现实时、VGA 级别的计算机视觉，这对嵌入式与边缘 AI 场景意义重大——在这些场景中，增加专用加速器或改用 Linux 级板卡在成本、功耗或延迟上都不可取。该文还记录了过去几乎没有公开示例代码、鲜为人知的 ESP32-S3 SIMD 指令。 该工作需要绕过两个 ISA 限制：芯片不支持直接的未对齐读取，因此东、西两侧像素块是通过从两个拼接的寄存器中提取切片获得的；芯片仅实现有符号 8 位比较，作者通过将无符号字节与 0x80 异或，把它们平移到有符号区间（因为 x - 128 == x ^ 0x80）。他还编写了一个名为 basm 的基础寄存器分配器，并提到也实现了 SIMD 加速的评分函数，但未在文中展开。</p>
<div class="news-background"><strong>背景</strong> FAST（Features from Accelerated Segment Test）是一种经典的角点检测算法，常作为特征匹配、视觉里程计和 SLAM 的基础模块；它围绕候选中心取 16 个像素组成的环，判断是否有足够多连续像素与中心像素的差异超过阈值。SIMD（单指令多数据）让一条指令并行处理一整组数值——此处即是由 128 位寄存器承载的 16 个 8 位像素值。ESP32-S3 基于双核 Cadence Xtensa LX7，主频最高 240 MHz，集成 Wi-Fi 与蓝牙 LE；相比于 ARM NEON 等主流平台，其 SIMD 支持的相关资料相对匮乏。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://hackaday.com/2024/07/01/simd-accelerated-computer-vision-on-the-esp32-s3/">SIMD-Accelerated Computer Vision On The ESP32-S3 - Hackaday</a></li>
<li><a href="https://www.hackster.io/news/shranav-palakurthi-taps-into-the-espressif-esp32-s3-s-simd-powers-doubles-tinyml-cv-performance-fd4fc92e8402">Shranav Palakurthi Taps into the Espressif ESP 32 - S 3 &#x27;s SIMD Powers...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#embedded-systems</span> <span class="tag">#computer-vision</span> <span class="tag">#SIMD</span> <span class="tag">#ESP32-S3</span> <span class="tag">#performance-optimization</span></div>
</article>
<hr>

<a id="item-6"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://captnemo.in/blog/2026/10/23/emsign-revoked-gov-in/">据报印度政府网站仍在提供已吊销的 eMudhra 证书</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 24, 04:06</span></div>
<p class="news-summary">2026 年 10 月 17 日，八个链接到 emSign ECC Root CA - G3 的 eMudhra 中间 CA 被发现私钥可被轻易恢复；次日这些中间 CA 被吊销，Mozilla 与 Chrome 也开始不再信任整个 G3 根证书。10 月 23 日发布的一篇博客文章称，数天之后仍有大量印度政府网站在提供已吊销的 eMudhra 证书，并对 MeitY 于 10 月 21 日所称此次事件对印度网站影响“非常有限”、持续时间“非常短”的说法提出质疑。 这起事件表明，吊销证书或不再信任某个根证书，并不会自动让它在仍在运行的政府服务器上消失，因此在事件被宣布已受控之后，民众可能仍会长期访问到证书失效或不受信任的 HTTPS 页面。由于浏览器不信任的是整个 G3 根证书、而不只是八个被攻破的中间 CA，eMudhra 估计约有 30,000 张证书需要迁移；博客称这些证书大多属于通过 InCommon 使用 eMudhra 的美国高校，而非印度网站。 博客指出，有问题的密钥生成于 2025 年 4 月，也就是说在问题被报告之前，任何人大约有 18 个月的时间可以恢复这些私钥；此外，eMudhra 于 10 月 19 日在其未受影响的 RSA 层级（emSign Root CA - G1）上以“Superseded”为由吊销了 9,356 张证书，这批证书恰好对应所有缺少 emSign 自身 CP/CPS 所要求的 certificate-type policy OID 且尚未过期的证书（记录为 Bug 2082782）。文中跟踪表格列出受影响主机及其状态，如“Revoked”“Fixed”和“No response”，既涵盖 .gov.in 域名，也涵盖肯尼亚的 .go.ke 域名，数据来自 crt.sh、SSL Labs 和 CRL 查询。</p>
<div class="news-background"><strong>背景</strong> 公钥基础设施依赖证书颁发机构（CA）签发数字证书，把公钥与某个域名绑定，浏览器正是借此验证 HTTPS 网站的身份。CA 通常将根证书离线保管，并通过中间 CA 签发终端实体证书，因此某个中间 CA 被攻破时可以只吊销它而不必废弃根证书。吊销信息通过证书吊销列表（CRL）等机制发布，而 crt.sh 这类 Certificate Transparency 日志则让研究人员可以枚举某个域名签发过哪些证书。浏览器以及 Mozilla 等根证书计划还可以彻底取消对某个根证书的信任，从而使链接到该根的所有证书失效。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.thehindu.com/sci-tech/technology/what-is-emudhra-web-security-key-leak/article71610041.ece">What is eMudhra , and what we know about the web... - The Hindu</a></li>
<li><a href="https://en.wikipedia.org/wiki/Intermediate_certificate_(cryptography)">Intermediate certificate (cryptography)</a></li>
<li><a href="https://www.ssldragon.com/blog/root-intermediate-certificate/">Root and Intermediate Certificates: Key Differences Explained</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#TLS</span> <span class="tag">#PKI</span> <span class="tag">#security incident</span> <span class="tag">#certificate revocation</span> <span class="tag">#India government</span></div>
</article>
<hr>

<a id="item-7"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.aikido.dev/blog/python-packages-vulnerable-node2shell-brotli-cve-2026-111497">node2shell Brotli 漏洞 CVE-2026-111497 亦影响 Python 及其他解码器</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 24, 11:01</span></div>
<p class="news-summary">Node.js 于 2026 年 10 月 21 日披露了被命名为“node2shell”的 CVE-2026-111497，次日 Python 方面也确认其 Brotli 与 brotlicffi 包受同一解码器缺陷影响。随后 libbrotli、Brotli 1.2.1、brotlicffi 1.2.1.0、C++、Node.js 22.23.4/24.22.1/26.12.1、bun 和 Envoy 相继发布了补丁，更多补丁仍在陆续推出。 由于缺陷位于共享的 Brotli 解码器而非 Node.js 本身，任何捆绑了同一份代码的语言运行时、库或 HTTP 服务都会受影响。其广泛影响在于：urllib3、requests、httpx 和 aiohttp 等常见 Python HTTP 客户端只要检测到该包已安装就会自动解码 Brotli，因此即使开发者从未显式 import Brotli，也可能触达存在漏洞的代码路径。 根本原因是 c/dec/decode.c 中块类型切换处理存在越界写，影响 Brotli 1.0.3 至 1.2.0 版本，在解压不受信任的压缩数据时可能泄露内存、造成拒绝服务，甚至可能实现代码执行。只有解码路径受影响：Apache 的 mod_brotli 和默认 Nginx 配置只做响应压缩，另外 PyPI 公告 PYSEC-2026-4322 与 PYSEC-2026-4323 现已可让 pip-audit、OSV 和 Dependabot 标记存在风险的安装。</p>
<div class="news-background"><strong>背景</strong> Brotli 是 Google 开发的一种无损压缩算法与数据格式，常被用作 HTTP 内容编码（“Content-Encoding: br”）以压缩传输中的网页内容，其解码器被内置在浏览器、服务器、CDN 以及众多语言运行时和软件包中。该漏洞属于内存破坏类问题：解码器会写出已分配缓冲区的边界，而这类破坏往往可被利用以在受影响进程内实现任意代码执行。由于 Brotli 是以依赖形式嵌入而非独立服务，同一个 CVE 会传导到解码器的每一个使用方，这也是公告建议团队盘点传递依赖、并在缺少补丁时关闭 Brotli 解码的原因。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://nvd.nist.gov/vuln/detail/cve-2026-111497">NVD-CVE-2026-111497</a></li>
<li><a href="https://vercel.com/kb/bulletin/node-js-security-advisory">Node.js security advisory: Brotli decoder RCE (CVE-2026 ...</a></li>
<li><a href="https://thehackernews.com/2026/10/nodejs-brotli-decoder-bug-could-allow.html">Node.js Brotli Decoder Bug Could Allow Remote Code Execution ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#security</span> <span class="tag">#vulnerability</span> <span class="tag">#brotli</span> <span class="tag">#compression</span> <span class="tag">#nodejs</span></div>
</article>
<hr>

<a id="item-8"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://philipotoole.com/twelve-years-of-distributed-sqlite/">rqlite 作者回顾分布式 SQLite 十二年演进历程</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 24, 06:41</span></div>
<p class="news-summary">rqlite 的作者 Philip O&#x27;Toole 发表了一篇第一人称回顾文章，时间距他在 2014 年 9 月发布 rqlite 公告已过去十二年。他梳理了“分布式 SQLite”如何从周末上传到 GitHub 的项目，发展成如今他估计约有十几个项目的类别，其中少数获得风险投资、两个已被收购。他还指出，目前关于这一类别的大部分文章都把故事起点放在 2021 年前后，因此他写下了从 2014 年开始的版本。 这篇文章是该设计领域的一手历史记录，而这一领域如今已相当拥挤；它梳理了几条主要技术路线之间的取舍：rqlite 基于 leader 的 CP 复制、LiteFS 的文件系统级复制、cr-sqlite 基于 CRDT 的多写收敛，以及对 SQLite 本身的分支 libSQL。对于需要判断自己究竟需要何种持久性与可用性保证的工程师来说，这一框架很有参考价值。 O&#x27;Toole 强调，rqlite 自始至终未变的核心设计是它是一个 CP 系统：写操作必须经过 leader，必须获得多数节点确认，处于分区的少数派会拒绝写入。最早的版本使用 goraft 库（当时 InfluxDB 和 etcd 也在用），2016 年初换成了 Hashicorp 的 Raft 实现并沿用至今；而 rqlite 在 v8.0 中处理 SQLite WAL 的方式，反过来又受到了 Litestream 的启发。</p>
<div class="news-background"><strong>背景</strong> SQLite 是一个嵌入式关系数据库，整个数据库存放在单个文件中，本身没有跨机器复制的机制。Raft 是一种共识算法，让一组节点就同一串状态变更序列达成一致，从而在部分节点失效时系统仍能继续工作。rqlite 的核心思路是在 SQLite 前面加一层 Raft 日志，把每次写入复制到整个集群，这样丢失一个节点不意味着丢失数据；相比之下，Litestream 把单节点上的 write-ahead log 页面持续流式复制到 S3 之类的副本，用备份与恢复来应对机器故障，而不是实时共识。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/rqlite/rqlite">rqlite / rqlite : The lightweight, fault-tolerant database built on SQLite .</a></li>
<li><a href="https://en.wikipedia.org/wiki/Raft_consensus_algorithm">Raft consensus algorithm</a></li>
<li><a href="https://litestream.io/how-it-works/">Litestream replicates SQLite databases in real-time to S3.</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论区整体非常正面，读者感谢 O&#x27;Toole 的贡献，并称赞他是维护者的榜样。一位工程师补充了自己的实战经验：其前公司同样用 Go 和 Hashicorp 的 Raft 在 SQLite 之上构建分布式层，最初把事务中的每条语句都作为日志上的独立命令，后来改为最多两条命令——先做一次分布式 begin，随后由发起节点在本地执行整个事务并累积所有语句，最后回滚并发送一条携带整批语句的 commit 命令。</div>
<div class="news-tags"><span class="tag">#SQLite</span> <span class="tag">#distributed systems</span> <span class="tag">#Raft</span> <span class="tag">#replication</span> <span class="tag">#databases</span></div>
</article>
<hr>

<a id="item-9"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://lynchlab.net/llm-skin-cancer">十年前的 Inception v3 CNN 在皮肤癌诊断上胜过前沿 LLM</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">sungam</span><span class="news-time">Oct 25, 17:15</span></div>
<p class="news-summary">一位博主报告称，一个十年前的 Inception v3 卷积网络在单张 H100 GPU 上用 ISIC Archive 的 68,011 张皮肤镜与临床图像微调后，在皮肤癌诊断上胜过了两个前沿 LLM。该对比使用了 200 个留出的测试病灶，同一病灶或同一患者的其他所有照片都已从训练集和验证集中移除，也未用于模型选择或阈值设定。 这一结果是一个具体案例，说明小型、专用的模型在什么情况下能胜过大型通用模型，也为“应用应当调用通用 LLM 还是部署专用分类器”的争论提供了素材。由于 LLM 如今可以低成本地帮助构建这类专用模型，这一事件暗示着构建窄领域高精度系统的经济性可能正在改变。 该网络是 ImageNet 预训练的 Inception v3 并对全部层做了微调，即从日常照片迁移学习到皮肤镜图像，而非从零训练。评论者指出该设置只是 200 个病灶的留出基准，且结果来自针对特定基准调优的任务专用模型，因此应带着这些局限来理解这一对比结论。</p>
<div class="news-background"><strong>背景</strong> Inception v3 是 Google 于 2016 年发布的卷积神经网络架构，以分解卷积、标签平滑和辅助分类器著称，常被用作迁移学习的骨干网络。在标注数据往往稀缺的医学影像领域，用领域图像微调预训练 CNN 是标准做法。ISIC Archive 是由 International Skin Imaging Collaboration 策划的大型皮肤镜与临床图像集合，贡献方包括 Memorial Sloan Kettering Cancer Center 和 Hospital Clínic de Barcelona，常被用于皮肤病灶分类基准。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Inception_(deep_learning_architecture)">Inception (deep learning architecture) - Wikipedia</a></li>
<li><a href="https://challenge.isic-archive.com/data/">ISIC Challenge</a></li>
<li><a href="https://huggingface.co/docs/timm/main/models/inception-v3">Inception v3 - Hugging Face</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 的评论者大多并不惊讶专用模型能在窄任务上获胜，他们用 3000 万参数的 KataGo 网络下围棋强于参数量大得多的 LLM、以及计算器在算术上胜过 LLM 作类比。最尖锐的批评认为这种对比本质上是“benchmaxxing”——针对特定基准调优的模型在该基准上自然会胜过通用模型。也有人认为这种框架忽略了 LLM 在诊断中的真正潜力，例如纳入病历记录、让模型主动追问患者、以及处理纹身等分布外图像。</div>
<div class="news-tags"><span class="tag">#machine-learning</span> <span class="tag">#medical-ai</span> <span class="tag">#llms</span> <span class="tag">#benchmarks</span> <span class="tag">#computer-vision</span></div>
</article>
<hr>

<a id="item-10"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://theintercept.com/2026/10/01/oregon-police-misconduct-public-records-cost-fee/">俄勒冈警方为一名警员的记录开出 250 万美元、44,816 小时的报价</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">tdeck</span><span class="news-time">Oct 25, 18:04</span></div>
<p class="news-summary">The Intercept 报道称，俄勒冈州一个警察局告知当地一家新闻媒体，仅针对一名警员的公共记录申请，检索和处理就至少需要 44,816 小时的员工工时，费用约为 2,484,599.04 美元。该消息在 Hacker News 上获得 302 分、76 条评论，其中一位引用原文的评论者称涉事机构是尤金警察局（Eugene Police Department）。 数百万美元的报价加上数万工时的估算，实际上可能等同于拒绝：很少有地方新闻机构付得起这笔钱，也等不起隐含的漫长周期。此类案例直接影响公众能了解多少警方行为，因为针对地方警察局的问责报道大多依赖州级公共记录法，而非联邦 FOIA。 所报的 44,816 小时相当于按每周 40 小时计算的约 21.5 年全职工作，这也是评论者认为最荒谬的一点。需要注意的是：本次条目并未附上 The Intercept 原文，因此具体数字和涉事机构名称来自条目摘要以及评论者的引用，而非原文本身。</p>
<div class="news-background"><strong>背景</strong> 俄勒冈州的公共记录法编于 ORS 第 192 章，规定除豁免披露的记录外，任何人都有权查阅公共机构的公共记录，同时允许机构收取制作记录的费用。美国联邦《信息自由法》（FOIA）只适用于联邦机构；向市警察局提出的申请适用各州法规，而收费标准、费用减免和答复期限在各州差异很大。记者通常可以要求提供分项估价或申请费用减免，而 2026 年的报道已经记录了费用、逾期不答复和执法不力如何让记者疲惫到放弃申请。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://oregon.public.law/statutes/ors_chapter_192">ORS Chapter 192 – Records; Public Reports and Meetings</a></li>
<li><a href="https://oregon.public.law/rules/oar_250-001-0020">OAR 250-001-0020 – Fees for Public Records - OregonLaws</a></li>
<li><a href="https://www.poynter.org/commentary/2026/public-records-delays-journalists-foia/">Public records delays are wearing journalists down. I’m one ...</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者普遍认为这个数字本身就是一种阻挠，有人还指出机构也会用“拖延战术”——其 2026 年 3 月向学区提交的申请至今只收到八次按月分批的部分回复，且看不到终点。也有人把视野放宽：一位评论者提到德国围绕其 FOIA 等效法律的持续争议，包括 Jens Spahn 在内的政界人士正提议允许此类高得令人却步的收费，并收窄申请主体范围；另一位则以英国 FOIA 30 天内答复的做法作对比。还有评论者指出这并非俄勒冈的孤例，并援引另一桩媒体索取武力使用记录的报道，涉及一名同时是警察的波特兰市议员候选人。</div>
<div class="news-tags"><span class="tag">#public records</span> <span class="tag">#government transparency</span> <span class="tag">#FOIA</span> <span class="tag">#journalism</span> <span class="tag">#police accountability</span></div>
</article>
<hr>

<a id="item-11"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://danluu.com/ambitious/">Dan Luu 呼吁软件开发者树立更高目标</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">ltratt</span><span class="news-time">Oct 24, 21:47</span></div>
<p class="news-summary">Dan Luu 发表了题为《We should be more ambitious with the software we build》的文章，认为整个行业在软件创造上的野心过低、安于现状。该文被发布到 Hacker News，获得 726 分并引发约 670 条评论。 这篇文章之所以引发共鸣，是因为当下的软件行业越来越偏向渐进式优化——比如让 ripgrep 或 Postgres 快一点——而不是创造质变性的新能力。在 LLM 辅助编程让小项目变得唾手可得的背景下，关于什么才算真正有雄心的工程，这场讨论直接关系到开发者如何分配时间、团队如何评判质量。 Luu 的论点是一种文化层面的批评，而非技术主张；讨论随后分化为几条不同线索：LLM 生成的代码是否过拟合且难以维护、“让 X 更快”是否算得上雄心，以及开发者圈子之外软件质量究竟有多差。评论者给出了具体反例，包括一个用于在 Kobo 电子阅读器上构建带沙箱 e-ink 应用的 SDK，以及对某款 Hitachi 热泵存在未记录功能和硬编码配置行为的批评。</p>
<div class="news-background"><strong>背景</strong> Dan Luu 是一位知名软件工程师和博主，他关于工程文化、性能和行业实践的文章常在 Hacker News 上广泛传播。讨论中提到的“更快的马”出自一则据传是 Henry Ford 的名言：顾客只会要求一匹更快的马，而不会想到汽车——这里被用来质疑优化现有工具是否真的算有雄心。Hacker News 的分数和评论数大致可以反映一篇文章在该站技术受众中的共鸣程度。</div>
<div class="news-discussion"><strong>社区讨论</strong> 整体讨论热度很高，但具体观点分歧明显：一位评论者称 LLM 通过加入杂乱、过拟合的代码“硬化”了公司里数百个内部应用；另一位则认为 AI 终于让自己得以推进长期缺乏时间的副项目，例如一个 Kobo 电子墨水应用 SDK。多位评论者反驳了文章框架，指出“更快的 Postgres/正则”本身就是“更快的马”的隐喻，真正需要的是更有雄心的思考而非仅仅更有雄心的软件；还有人提醒，在开发者圈子之外，日常软件的质量依然很差。</div>
<div class="news-tags"><span class="tag">#software-engineering</span> <span class="tag">#engineering-culture</span> <span class="tag">#software-quality</span> <span class="tag">#hacker-news</span> <span class="tag">#opinion</span></div>
</article>
<hr>

<a id="item-12"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.dailycal.org/news/campus/academics/ai-use-leads-uc-berkeley-math-professor-to-see-no-point-in-grading-homework/article_bdf1eae2-c08b-491f-b9f1-81a7cea177de.html">伯克利数学教授博切尔兹称 AI 时代批改作业“没有意义”</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">romanhn</span><span class="news-time">Oct 25, 16:28</span></div>
<p class="news-summary">据《Daily Californian》报道，加州大学伯克利分校数学家、菲尔兹奖得主 Richard Borcherds 表示，在学生可以使用 AI 工具完成作业的情况下，批改作业“没有意义”。这一说法在 Hacker News 上引发广泛关注，评论者围绕“当语言模型可以给出答案时，作业的目的究竟是什么”展开讨论。 这一表态来自顶尖研究型大学的一位知名数学家，为“课后作业是否还能可靠衡量学生学习效果”的 broader 争论增添了有分量的声音。如果教师越来越多地放弃计分作业，转而依赖考试、课堂作业或其他受监督的评估方式，可能会改变本科课程（尤其是技术类课程）的组织方式以及学生的评价方式。 这一消息是学生报纸报道的教授言论，而非有据可查的课程政策变动，所提供材料中也没有描述任何具体的新评分规则。评论者还指出，研究型大学的终身教授通常把作业批改交给助教，因此这一表态可能本身就反映出教授并不直接参与日常批改工作。</p>
<div class="news-background"><strong>背景</strong> 正如评论者所指出的，Richard Borcherds 是加州大学伯克利分校的数学家、菲尔兹奖得主，最著名的成就是在“Monstrous Moonshine”猜想方面的工作——该猜想把模函数与 Monster 群 的表示联系起来。大学数学课程中的作业传统上有两个作用：一是让学生通过低风险的练习获得循序渐进的反馈，二是让教师了解哪些学生跟得上进度。能够解出常规习题集的生成式 AI 工具同时削弱了这两种功能，这也是争论从“如何检测作弊”转向“作业究竟为了什么”的原因。</div>
<div class="news-discussion"><strong>社区讨论</strong> 评论者总体上对这一说法持怀疑态度：有人指出其中的讽刺意味——终身教授本来就不太会亲自批改习题集，这项工作通常由助教承担，因此真正的问题在于作业的目的究竟是什么。也有人担心，失去计分式的渐进练习会削弱促使学生在考试前接触材料的外在压力；少数人则质疑，既然考试才是衡量掌握程度的手段，给大学生批改作业本身是否重要。还有评论者更进一步，认为高等教育应回归学术本身，而不是职业 skills 培训。</div>
<div class="news-tags"><span class="tag">#AI-in-education</span> <span class="tag">#academic-integrity</span> <span class="tag">#LLMs</span> <span class="tag">#grading</span> <span class="tag">#community-discussion</span></div>
</article>
<hr>

<a id="item-13"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.cerebras.ai/blog/how-we-deploy-trillion-parameter-frontier-models-on-cerebras">Cerebras 详解如何在自家芯片上部署万亿参数前沿模型</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">gmays</span><span class="news-time">Oct 25, 01:33</span></div>
<p class="news-summary">Cerebras 发布了一篇博客，介绍其如何在自家硬件上部署万亿参数级别的前沿 AI 模型，该文在社区引发热烈讨论（344 分、125 条评论）。但本次提供的正文内容为空，因此文中具体涉及的模型、吞吐数据与部署技术细节无法在此核实。 万亿参数模型通常需要借助张量并行与流水线并行，把模型拆分到大量互联的 GPU 上才能提供推理服务，因此任何能在单块晶圆级芯片上运行此类模型的方法，都可能改变前沿模型推理在延迟与成本上的权衡。由于 Cerebras 的体量远小于超大规模云厂商，它能否真正交付这种服务能力，将决定它能否成为可行的替代推理供应商。 博客中的具体数据——实际提供哪些模型、每秒 token 数、定价，以及权重如何在晶圆上分布——无法与所提供的文本核对；社区评论者则对 Cerebras 所提供模型的新旧程度和质量都提出了质疑。评论者还提出一个硬件层面的问题：处理单元（PE）构成的二维网格及其仅与四邻通信的模式，是否真能像示意图那样顺畅地映射到逐层流式计算的流程上。</p>
<div class="news-background"><strong>背景</strong> Cerebras 做的是晶圆级芯片：它不把硅晶圆切割成一颗颗独立裸片，而是将整片晶圆保留为一块单片处理器，其 CS-2 与 CS-3 系统在 462 平方厘米的晶圆上集成多达约 85 万个处理单元，并通过片上网状互连相连。其核心卖点在于，把一个模型放在单块晶圆上，可以省去通常在 GPU 集群上做大模型推理时受限于设备间网络通信的开销。万亿参数语言模型——即拥有约一万亿个可学习权重的模型，例如 2023 年训练的 1.085 万亿参数的 PanGu-Σ——正处在这一扩展性难题的极端位置，因此能否服务这类模型是对该架构的一次重要检验。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Wafer-scale_integration">Wafer - scale integration - Wikipedia</a></li>
<li><a href="https://www.emergentmind.com/topics/cerebras-wafer-scale-engine">Cerebras Wafer - Scale Engine Overview</a></li>
<li><a href="https://developer.nvidia.com/blog/demystifying-ai-inference-deployments-for-trillion-parameter-large-language-models/">Demystifying AI Inference Deployments for Trillion Parameter ...</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 主流态度偏向怀疑：一位评论者认为 Cerebras 缺乏资金与制造产能来跟上需求，因此只能用低价入门套餐让用户体验一下，而无法持续提供顶级模型。其他人表示，实际可用的模型（例如 GPT-OSS 120B 和某个 Qwen 模型）虽然速度很快，但质量不足以满足自己的工作需求；还有不少人预计 Cerebras 只能以落后前沿 6 到 9 个月的节奏提供模型。一位曾与该公司有过专业合作的评论者称赞其技术，但批评其团队执行力不足。</div>
<div class="news-tags"><span class="tag">#Cerebras</span> <span class="tag">#AI infrastructure</span> <span class="tag">#large language models</span> <span class="tag">#model serving</span> <span class="tag">#hardware</span></div>
</article>
<hr>

<a id="item-14"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://twitter.com/log4j/status/2113014142600953868?s=46">三星电视 root shell 引发对端侧 TensorFlow Lite 追踪的争论</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">testing22321</span><span class="news-time">Oct 24, 05:49</span></div>
<p class="news-summary">一个 Hacker News 讨论帖合并了两条在社交媒体上流传的说法：一是有 root 权限的三星电视会在 960x540 的截取图像上运行 TensorFlow Lite 模型来追踪观看者；二是三星电视会扫描附近的蓝牙麦克风以推断家中的事件。该帖获得 727 分和 555 条评论，但这两条说法目前除帖中引用的社交媒体原帖外，尚无其他来源证实。 智能电视摆在家庭中最私密的空间里，因此若有可信证据表明设备在端侧做图像分析或蓝牙扫描，将构成影响数百万家庭的重大隐私事件，并可能招致监管或法律层面的审视。这一讨论也说明，逆向工程的发现往往在被与公开产品文档核对之前就已迅速病毒式传播。 评论者指出，狗叫和婴儿哭声检测是该三星产品线用于 SmartThings 集成的已宣传功能，被当作“发现”的许多内容其实记录在公开手册、FCC 备案文件和专利申请中。该领域此前已有公开成果，尤其是 Synacktiv 在 GreHack 2021 上展示的三星 Q60T Tizen 漏洞利用，实现了 root shell 和固件解密。</p>
<div class="news-background"><strong>背景</strong> TensorFlow Lite 是 Google 用于在低功耗和嵌入式设备上运行轻量级机器学习模型的框架，因此它出现在电视、手机和微控制器上，而不只存在于数据中心。在电视上取得 root shell 意味着获得其操作系统的最高权限，通常借助固件或引导加载程序漏洞实现，从而让研究者能够检查运行中的进程和网络流量。蓝牙低功耗（BLE）扫描可以枚举附近主动广播的设备，这既是消费级设备查找类应用的基础，也是隐私追踪担忧的由来。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/synacktiv/samsung-q60t-exploit">GitHub - synacktiv/samsung-q60t-exploit</a></li>
<li><a href="https://www.synacktiv.com/sites/default/files/2021-11/GreHack2021_Rooting_Samsung_Q60T_Smart_TV.pdf">Rooting Samsung Q60T Smart TV - Synacktiv</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 整体情绪偏向怀疑：一位评论者指出此事已流传过十几次，而逆向工程的第一步就是阅读公开文档和 FCC 备案，这些材料本就能解释设备的出厂行为。其他人关注法律责任，引用 Clements-Jeffrey 诉 Absolute Software 案作为侵犯隐私责任的先例；还有一些人讨论如何剥离电视的“智能”功能，或向遥测数据注入故意误导的信息。</div>
<div class="news-tags"><span class="tag">#privacy</span> <span class="tag">#reverse-engineering</span> <span class="tag">#smart-tv</span> <span class="tag">#security</span> <span class="tag">#surveillance</span></div>
</article>
<hr>

<a id="item-15"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.theverge.com/column/1017983/google-ai-search-online-publishing">Google AI Overviews 正在掏空出版商的流量</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">The Verge AI</span><span class="news-time">Oct 25, 12:00</span></div>
<p class="news-summary">The Verge 的 &quot;Stepback&quot; 专栏（作者 Emma Roth）详细阐述了 Google 的 AI 搜索功能——尤其是 AI Overviews——如何大幅削减出版商从搜索中获得的点击量。文中引用 Similarweb 的数据称，《纽约时报》来自搜索的流量占比在三年间从 44% 降至 35.5%；拥有《每日邮报》和 Metro 的 DMG Media 则向英国竞争与市场管理局（CMA）表示，受 AI Overviews 影响，其 2025 年 6 月至 7 月的点击率下降幅度最高达 89%。 文章认为，Google 与出版商之间长期互惠的&quot;内容换流量&quot;关系已经破裂，这威胁到依赖搜索引流的新闻机构的广告商业模式。这些数据也与 Google 公开宣称 AI 搜索有利于网络生态的说法相矛盾，并且正值英国 CMA 等监管机构审视 AI Overviews 的市场影响之际。 这些数字与 Google 搜索负责人 Liz Reid 去年的说法形成对比——她称点击量&quot;相对稳定&quot;，并称 AI 搜索会把更多点击导向论坛、视频和播客类网站。其他佐证包括 Digiday 报道的调查：19 家 Digital Content Next 成员在 2025 年 5 月至 6 月间 Google 流量下滑 1% 至 25%；皮尤研究中心发现用户在看到 AI Overview 时更不可能点击链接。据报道，Google 还在测试一项计划，为 AI Overviews 和 AI Mode 中使用的内容向出版商付费。</p>
<div class="news-background"><strong>背景</strong> AI Overviews 是 Google 的生成式 AI 功能，会在搜索结果最顶部放置一段由 AI 撰写的摘要，底层使用 Google 的 Gemini 模型；它于 2024 年 5 月在美国上线，到 2024 年 10 月扩展至全球。这加速了所谓&quot;零点击&quot;（zero-click）搜索的趋势——用户的查询直接在结果页被解答，无需访问任何外部网站。出版商过去大量投入 SEO（搜索引擎优化），以便在 Google 经典的蓝色链接列表中排名靠前，这一模式的前提是用户会点击进入他们的网站。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Google_AI_Overviews">Google AI Overviews</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zero-click_result">Zero-click result - Wikipedia</a></li>
<li><a href="https://searchengineland.com/guide/zero-click-searches">Zero-Click Searches: What They Are &amp; How SEOs Can Adapt</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI search</span> <span class="tag">#Google AI Overviews</span> <span class="tag">#online publishing</span> <span class="tag">#SEO</span> <span class="tag">#web traffic</span></div>
</article>
<hr>

<a id="item-16"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://yossarian.net/til/post/posix-wordexp-3-is-dangerous/">POSIX wordexp(3) 对不可信输入不安全，即使启用 WRDE_NOCMD 亦然</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 25, 15:09</span></div>
<p class="news-summary">yossarian.net 上的一篇技术文章警告称，POSIX 的 wordexp(3) API 默认开启全部展开特性（包括命令替换）来执行 shell 风格展开，因此对攻击者可控的字符串传入 flags=0 可能导致 shell 命令被执行。作者指出，即便使用 WRDE_NOCMD 标志也只是部分缓解：musl 会把工作委托给系统 shell，仅做敷衍的扫描，会漏掉某些命令替换模式；macOS 的 libc 则委托给 /usr/lib/system/wordexp-helper，据称直到 2023 年仍存在同样的绕过问题。 wordexp(3) 常被推荐为在 C 中实现 tilde 展开（如 ~/foo 展开为 /home/me/foo）的简便方法，开发者可能因此未意识到它会把输入交给类似 shell 的解析流程，从而在系统级甚至 setuid 相关代码中形成隐蔽的注入隐患。这也提醒人们：libc 封装层中与安全相关的过滤在不同平台和不同 libc 实现之间可能并不一致，在某个系统上看似成立的检查，换一个系统就可能失效。 flags 参数决定行为，默认值 0 会启用命令展开，因此除非传入 WRDE_NOCMD，该 API 可能触发命令执行；但文章认为该标志只是“权宜之计”，因为委托给 shell 的实现可能被这样的模式欺骗：底层 shell 视其为合法命令替换，而前置扫描却识别不出来。作者还表示，由于 macOS 默认 shell 已从 bash 换成 zsh，他不确定该绕过是否仍然有效，并提到 macOS 过去是把工作委托给 Perl。</p>
<div class="news-background"><strong>背景</strong> wordexp(3) 是 POSIX 定义的 C 库函数，对字符串执行类似 shell 的展开，包括 tilde 展开、变量替换和分词，结果放在 wordexp_t 结构中，包含 we_wordc、we_wordv 等字段。由于它模仿 shell 语义，当输入不可信时就会继承 shell 行为带来的风险。musl 与 macOS 的 libc 都是通过调用外部 helper 或 shell 来实现，而非完全在进程内解析，这正是安全检查与实际 shell 行为之间产生差异的根源。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://yossarian.net/til/post/posix-wordexp-3-is-dangerous/">TIL: POSIX wordexp (3) is dangerous - yossarian.net</a></li>
<li><a href="https://www.man7.org/linux/man-pages/man3/wordexp.3.html">wordexp (3) - Linux manual page - man7.org</a></li>
<li><a href="https://github.com/esmil/musl/blob/master/src/misc/wordexp.c">musl/src/misc/wordexp.c at master · esmil/musl · GitHub</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#security</span> <span class="tag">#POSIX</span> <span class="tag">#C</span> <span class="tag">#shell-injection</span> <span class="tag">#systems-programming</span></div>
</article>
<hr>

<a id="item-17"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://ziglang.org/devlog/2026/#2026-10-24">Zig 实现部分运算符优先级，十年提案落地</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 25, 14:18</span></div>
<p class="news-summary">在日期为 2026-10-24 的 Zig devlog 中，核心贡献者 Ryan Liptak 介绍了 issue #114 终于在 master 分支上由贡献者 CMDRZero 实现——该提案于 2016 年 2 月 8 日提交，是 Zig 语言第二古老的未关闭提案。按照这一改动，某些运算符组合不再具有既定优先级，编译器会直接报错 &quot;ambiguous operator precedence ... use parentheses to disambiguate&quot;，而不是默默选择一种求值顺序。 这一改动强制程序员在真正存在歧义时显式写出求值顺序，从而消除了 Zig 代码中一类隐蔽的误读问题，对阅读或审查 Zig 源码的人尤其重要。它也表明 Zig 维护者愿意为可学习性而打破 C 风格的优先级传统，这对 Zig 社区之外的语言设计者同样具有参考价值。 像 `x + y * z` 这样的常见表达式仍然无需括号即可解析，编译器诊断信息还会提示该表达式在 Zig 0.17.x 中的原有求值方式（例如 `(... orelse ...) == ...`），以便迁移。Liptak 表示所有语义变更都会写入 0.17.0 的发布说明并给出迁移建议；该篇 devlog 还涉及其他工作，例如通过 `@bitCast` 转换成 `@Vector(n, u1)` 把整数拆成单个比特，以及 LLVM 后端的性能改善。</p>
<div class="news-background"><strong>背景</strong> 运算符优先级是一套决定表达式中哪个运算符结合更紧的规则，因此 `x + y * z` 表示 `x + (y * z)` 而不是 `(x + y) * z`。Zig 过去沿用类似 C 的固定优先级表，当多种运算符混在一个表达式里时就很难记住。所谓 &quot;部分&quot; 优先级，是指某些运算符对之间的顺序被刻意留空，编译器只对这些真正有歧义的组合要求加括号，而不强加一个全序排名；其他语言设计也曾探索过这种偏序优先级，例如 Carbon 的运算符优先级提案。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ziglang/zig/issues/114">require parentheses sometimes to disambiguate confusing ...</a></li>
<li><a href="https://ziglang.org/devlog/2026/">Devlog ⚡ Zig Programming Language</a></li>
<li><a href="https://docs.carbon-lang.dev/proposals/p000555-operator-precedence.html">#000555: Operator precedence | Carbon Language documentation</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#zig</span> <span class="tag">#programming languages</span> <span class="tag">#language design</span> <span class="tag">#operator precedence</span> <span class="tag">#compilers</span></div>
</article>
<hr>

<a id="item-18"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://refi64.dev/posts/chromium-audio-break.html">一次 glibc pthread 改动意外破坏了 Chromium 音频</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 25, 15:34</span></div>
<p class="news-summary">一篇技术复盘文章记录了一次常规的 glibc 更新如何导致 Chromium 音频播放（尤其是 YouTube）失效，并抛出运行时错误“The futex facility returned an unexpected error code.”。作者通过对比多个 glibc 版本的调用栈，把回归定位到 Adhemerval Zanella 提交的“nptl: Remove futex_wait_cancelable”补丁——该补丁在 __pthread_cond_wait_common 中用 __futex_abstimed_wait_cancelable64 取代了 futex_wait_cancelable。 这个案例说明，C 库线程代码中一个经过代码评审、看似微小的内部重构，也可能向外扩散，以常规测试难以发现的方式破坏 Chromium 这类庞大而复杂的应用。它也为发行版维护者在推送运行时库升级前扩大测试范围提供了具体论据，同时说明在排查离奇崩溃时理解底层同步语义的重要性。 调查的关键在于显示线程阻塞在 pthread 条件变量等待中的调用栈；作者还指出第二个助推因素：Chromium 构建硬编码了一份极为激进的 field trial 测试配置，而文档明确说明非开发者构建（例如 Linux 发行版提供的 Chromium）应当通过 GN 参数 disable_fieldtrial_testing_config=true 将其关闭。作者总结的教训是：再小的改动都值得测试，而最离奇的 bug 故事往往有最朴素的修复方式。</p>
<div class="news-background"><strong>背景</strong> futex（“fast userspace mutex”，快速用户态互斥量）是 Linux 内核提供的加锁基础构件：线程在用户态自旋和竞争，只有确实需要睡眠或唤醒时才进入内核系统调用。glibc 的 NPTL 实现正是在 mutex、条件变量等 POSIX 原语之下使用 futex，因此 pthread_cond_wait 内部包含精细编写的 futex 等待逻辑，还要处理取消和超时。由于这些代码路径位于所有多线程应用的最底层，glibc 各版本之间细微的语义差异，就可能在遥远的用户态软件（例如浏览器的音频处理链路）中表现为莫名其妙的故障。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Futex">Futex - Wikipedia</a></li>
<li><a href="https://deepwiki.com/kraj/glibc/4.2-mutexes-condition-variables-and-futexes">Mutexes, Condition Variables and Futexes | kraj/glibc | DeepWiki</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#glibc</span> <span class="tag">#Chromium</span> <span class="tag">#Linux</span> <span class="tag">#debugging</span> <span class="tag">#pthreads</span></div>
</article>
<hr>

<a id="item-19"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://astral.sh/blog/uv-ty-integration">Astral 推出 uv 与 ty 实验性集成预览</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 24, 15:27</span></div>
<p class="news-summary">Astral 宣布其 Python 包管理器 uv 与类型检查器兼语言服务器 ty 之间达成实验性集成预览。此次集成在命令行和编辑器中为 PEP 723 Python 脚本提供一等支持，并新增统一的 `uv check` 命令，可一步完成环境准备、依赖安装与 ty 类型检查。 这是 Astral 迈向其“集成式工具链”愿景的首个具体步骤：uv 对项目环境与依赖的理解，加上 ty 对代码的理解，可解锁任一工具单独无法实现的能力。已经在使用 uv、Ruff 或 ty 的 Python 开发者，有望获得更简单一致的项目检查与独立脚本检查工作流。 使用 PEP 723 脚本支持与 `uv check` 需要 uv 0.12.3 及以上版本和 ty 0.0.76 及以上版本；在 VS Code 中脚本支持需通过 `ty.experimental.useUv` 设置或执行 `TY_UV=scripts ty check` 手动开启，而运行 `uv check` 会自动启用集成。Astral 表示 `uv check` 后续将支持 Ruff，以统一 lint 与类型检查，并正在开发诸如检测未使用依赖这类结合两项工具信息的检查；同时 ty 本身仍处于 beta 阶段、尚未发布 1.0。</p>
<div class="news-background"><strong>背景</strong> Astral 打造了三款基于 Rust 的 Python 工具：uv 是高速包管理器与项目管理器，可通过 uvx 运行工具并识别 PEP 723 内联脚本元数据；Ruff 是定位为 Flake8、Black 等工具更快替代品的 linter 与格式化工具；ty 则是用 Rust 编写的极快类型检查器与语言服务器，目标是对标 mypy、Pyright 和 Pylance。PEP 723 是一项 Python 标准，允许单个脚本以内联元数据声明依赖与 Python 版本要求，工具无需额外项目文件即可构建正确环境。过去这些工具各自负责 Python 开发的不同环节，而本次集成是围绕“对项目的共同理解”将它们连接起来的首次尝试。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/astral-sh/uv">GitHub - astral-sh/ uv : An extremely fast Python package and project...</a></li>
<li><a href="https://github.com/astral-sh/ty">GitHub - astral-sh/ty: An extremely fast Python type checker ...</a></li>
<li><a href="https://github.com/astral-sh/ruff">GitHub - astral-sh/ruff: An extremely fast Python linter and ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Python</span> <span class="tag">#uv</span> <span class="tag">#ty</span> <span class="tag">#developer tooling</span> <span class="tag">#type checking</span></div>
</article>
<hr>

<a id="item-20"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://larstofus.com/2025/11/16/how-to-run-a-city-builder-on-12-5-mhz/">SimCity 如何在 16 MHz 的 386SX 上跑完整城市模拟</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 24, 14:18</span></div>
<p class="news-summary">一篇于 2025 年 11 月 16 日发表在 larstofus.com 的博客文章，深入分析了初代 SimCity 如何在一颗发布时钟频率为 16 MHz 的 Intel 386SX 上运行完整的城市模拟。其核心机制是 s_sim.c 中的 Simulate() 函数：它接收的不是 deltaTime，而是一个从 0 循环到 15 的计数器（即 &quot;mod16&quot; 参数），并据此决定这一帧实际执行模拟的哪一部分——交通、火灾、电力、犯罪、税收——因此绝大多数系统在任意一帧中都被跳过。作者还附上了更正说明：文章早前版本误写为 12.5 MHz，而那是基础版 386 的时钟频率，并非 SX 版本。 这篇文章是&quot;把工作分摊到多帧&quot;的一个具体案例，说明只要愿意让不同子系统以不同频率更新，一个 CPU 密集的模拟类游戏也能塞进极小的时间预算里。作者把这一经验延伸到现代实践，认为同样的道理可以解释 Unreal 的 Lumen 为何不必每帧重算全部光照——也解释了它的反射为何偶尔会显得过时或异常。对于习惯在每个 tick 中无条件运行所有 gameplay 代码的游戏程序员和性能工程师来说，这篇文章很值得一读。 文章展示的代码并非原始代码的精确复制，而是为了让讲解更清晰做了删减的近似版本。作者对比了两种思路：固定大小的分块（把长任务切成固定大小的小块分摊到多帧）与运行时决定的调度（每块的大小取决于屏幕尺寸或距上次更新的时间等因素），并以某个 .ini 文件中的 FACES_PER_FRAME 变量作为可调固定分块的例子。他还认为，就 SimCity 而言，这些被跳过的更新在玩法上几乎察觉不到。</p>
<div class="news-background"><strong>背景</strong> 由 Maxis 于 1989 年推出的 SimCity 是城市建造（city builder）品类的开山之作之一：它不跟随某个角色或卷轴式动作场景，而是持续模拟一个相互关联的经济系统，涵盖用地规划、人口、税收、交通、电网、犯罪与火灾风险。这类&quot;系统之系统&quot;的模拟传统上非常吃 CPU，因为每个 tick 都有大量小计算触及地图的许多部分。该游戏当年公布的系统需求中列出的 CPU 是 Intel 386SX——386 的简化版本——其发布频率为 16 MHz，这个算力放在今天任何一颗数 GHz 的多核处理器面前都微不足道。文章借助 SimCity 的源码文件（如 s_sim.c）来解释游戏每帧的工作量是如何被削减到能塞进这个预算里的。</div>
<div class="news-tags"><span class="tag">#game-development</span> <span class="tag">#retro-computing</span> <span class="tag">#performance-optimization</span> <span class="tag">#simulation</span> <span class="tag">#software-engineering</span></div>
</article>
<hr>