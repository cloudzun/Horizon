---
layout: default
title: "Horizon 每日速递：2026-10-18"
date: 2026-10-18
lang: zh
---

> 📅 2026-10-18 · 从 54 条资讯中精选出 15 条重要内容

---

1. [Citizen Lab：Discover\-Tech 利用定向广告投放零点击间谍软件](#item-1) <span class="score-badge score-high">9.0</span>
2. [PwnEscape：借 Linux 网络栈漏洞实现 KVM 客户机到宿主机逃逸（CVE\-2026\-99999）](#item-2) <span class="score-badge score-high">9.0</span>
3. [RepRapMicron：迈向微米级 3D 打印的开源硬件尝试](#item-3) <span class="score-badge score-mid">7.0</span>
4. [DeepSeek 推出托管搜索与抓取 API，每千次成功请求 0\.75 美元](#item-4) <span class="score-badge score-mid">7.0</span>
5. [系统管理员称 Namecheap 停用其全部域名](#item-5) <span class="score-badge score-mid">7.0</span>
6. [开源 DIY 平台实现亚微米级三维运动控制](#item-6) <span class="score-badge score-mid">7.0</span>
7. [交互式 Parser Combinators 指南引发解析技术讨论](#item-7) <span class="score-badge score-mid">7.0</span>
8. [Meta 的 Muse Spark Open 与 Reflection 的 Beam 改变开放权重格局](#item-8) <span class="score-badge score-mid">7.0</span>
9. [Valen 借用检查器逆向遍历函数进行内存安全分析](#item-9) <span class="score-badge score-mid">7.0</span>
10. [一位程序员为编程写下的讣告：AI 智能体时代的失落](#item-10) <span class="score-badge score-mid">7.0</span>
11. [Ken Shirriff 逆向解析 Intel 8087 浮点加减法微码](#item-11) <span class="score-badge score-mid">7.0</span>
12. [ASMC 将 Ghidra 汇编语义接入 CBMC](#item-12) <span class="score-badge score-mid">7.0</span>
13. [EvoGrain 结合 L\-System 与粒度合成生成算法音频](#item-13) <span class="score-badge score-mid">7.0</span>
14. [博客文章梳理 TEE 攻击案例，呼吁重新审视其部署方式](#item-14) <span class="score-badge score-mid">7.0</span>
15. [爱好者历时九年破解 Xbox 360，最终靠 Raspberry Pi Pico 完成](#item-15) <span class="score-badge score-mid">7.0</span>

---

<a id="item-1"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/">Citizen Lab：Discover-Tech 利用定向广告投放零点击间谍软件</a><span class="score-badge score-high">9.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 18, 20:55</span></div>
<p class="news-summary">Citizen Lab 发布报告，记录了一种其称为“AdFection”的手法，并称这是首次公开、经技术证实的、通过定向在线广告投递零点击雇佣间谍软件的案例。报告称，一家名为 Discover-Tech 的以色列公司购买的恶意广告被用于向半岛电视台（Al Jazeera）的设备植入 Candiru（已更名为“Integrity Labs”）的间谍软件；相关报道指出，2024 至 2025 年间该机构至少有 45 台 Windows 电脑在无任何交互的情况下被感染。 这些发现把程序化广告供应链——一个每天处理数万亿次广告交易的系统——变成了有据可查的监控投递通道，这意味着网络用户可能仅仅因为加载了一个展示广告的页面或应用就被攻陷。这对记者、公民社会以及任何浏览开放网络的用户都有直接影响，同时也向广告交易平台、SSP 以及 Discover-Tech 这类经纪人依赖的中介机构提出了尖锐问题。 Citizen Lab 称，Discover-Tech 运营一个名为 Controlium 的平台，使其雇佣间谍合作伙伴能够在广告渲染的瞬间对设备进行去匿名化、指纹识别并自动感染；对 40 亿条竞价记录的分析显示，在四个月的时间里，其广告出现在数十个国家近 20 万个独立网站以及 Android/iOS 应用上。报告还称，Discover-Tech 的广告暗中引导数百万台设备连接 Candiru 的服务器——很可能是为了大规模追踪与侦察——并把该公司与 Candiru 之外的雇佣间谍及情报行为体（包括 Intelos 和 Bindecy）联系起来。</p>
<div class="news-background"><strong>背景</strong> Candiru 是一家成立于 2014 年、总部位于特拉维夫的隐秘公司，向政府客户出售间谍软件与网络间谍服务，其商业模式常被比作“黑客即服务”的托管服务商；其产品利用零日漏洞植入持久化后门，公司主体名称也多次变更。“零点击”意味着目标无需点击、触摸或下载任何东西——只要内容被处理，入侵就自动发生。Citizen Lab 是一家以调查商业间谍软件著称的研究机构，这份报告把相关工作延伸到程序化广告领域：在那里，广告位通过自动化的实时竞价买卖，广告由多个中介共同拼装完成。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/">Exposing AdFection: How Discover - Tech Turned... - The Citizen Lab</a></li>
<li><a href="https://en.wikipedia.org/wiki/Candiru_(spyware_company)">Candiru (spyware company)</a></li>
<li><a href="https://www.ft.com/content/b857f1ed-8af6-4d64-b059-912afee1c075?syn-25a6b1a6=1">New ‘ zero - click ’ spyware hacked phones using targeted ads</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#security</span> <span class="tag">#spyware</span> <span class="tag">#adtech</span> <span class="tag">#surveillance</span> <span class="tag">#zero-click-exploits</span></div>
</article>
<hr>

<a id="item-2"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://pwn.ai/blog/pwnescape">PwnEscape：借 Linux 网络栈漏洞实现 KVM 客户机到宿主机逃逸（CVE-2026-99999）</a><span class="score-badge score-high">9.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 17, 18:24</span></div>
<p class="news-summary">PWNAI Research（Paulos Yibelo）发布了一篇研究文章，描述了被编号为 CVE-2026-99999 的客户机到宿主机 KVM 逃逸 PwnEscape，该成果源自 Vercel 于 2026 年 8 月 18 日宣布的 100 万美元沙箱挑战赛。漏洞根因不在 KVM 本身，而在 Linux 网络栈：客户机可控的校验和元数据可以在内核完成校验之后改写 IPv4 头部，先造成 32 字节的宿主机内存泄露，最终实现完整的虚拟机越界逃逸。 可用的客户机到宿主机逃逸打破了多租户云与基于虚拟机的沙箱基础设施赖以生存的隔离边界，可能让某个租户的工作负载读取或破坏宿主机内存并触及其他租户。它还表明，虚拟机级别的越界突破可以源自客户机可触达的内核网络代码路径，而不局限于 KVM 设备模拟层，从而扩大了防御方需要审视的攻击面。 文章称，分片逻辑信任了一个先过期、后被改写的 IPv4 IHL 字段：重组后 skb 的逻辑线性头部仅为 28 字节（20 字节头部加 8 字节载荷），但一次延迟执行的校验和操作让 ip_do_fragment() 认为头部长度为 60 字节，于是原头部之后的 40 字节（其中 8 字节为宿主机内存）被当作 IPv4 选项写出。文中感谢 Michael S. Tsirkin、Willem de Bruijn、Eric Dumazet、Greg Kroah-Hartman 等 Linux 内核维护者推动上游修复，但所提供的摘录未说明受影响的内核版本或修复提交，同时当时的媒体报道称该研究者在整体挑战赛中获得了 5 万美元奖励。</p>
<div class="news-background"><strong>背景</strong> KVM 是 Linux 内核内置的虚拟机管理程序，云厂商依靠它将每位客户的虚拟机隔离在无特权的客户机中，正常情况下客户机永远不应接触宿主机内核内存。在 Linux 网络栈中，数据包存放在 sk_buff 结构里，字节可能同时位于线性 head 缓冲区和独立的非线性分片（fragment）中；IPv4 头部带有 IHL 字段，用于告诉解析器头部长度（包含可选的 IPv4 options）。PwnEscape 利用的是栈中不同部分信任同一数据包的不同版本：一个组件校验了 20 字节头部，另一个组件随后却认为它是 60 字节——这类缺陷通常被称为“检查与使用不一致”（time-of-check-to-time-of-use）问题。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://pwn.ai/blog/pwnescape">PwnEscape: Guest-to-Host KVM Escape (CVE-2026-99999)</a></li>
<li><a href="https://cybernews.com/security/critical-kvm-zero-day-vulnerability-allows-vm-escape/">KVM zero-day vulnerability enables VM escape to host root ...</a></li>
<li><a href="https://cybersecuritynews.com/kvm-zero-day-vm-escape/">Vercel Confirms KVM Zero-Day VM Escape, Awards Researcher $50,000</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#security</span> <span class="tag">#virtualization</span> <span class="tag">#KVM</span> <span class="tag">#vulnerability-research</span> <span class="tag">#linux-kernel</span></div>
</article>
<hr>

<a id="item-3"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://github.com/VikOlliver/RepRapMicron/wiki">RepRapMicron：迈向微米级 3D 打印的开源硬件尝试</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">RobotToaster</span><span class="news-time">Oct 18, 13:48</span></div>
<p class="news-summary">RepRapMicron 项目（又称 μRepRap）已在 GitHub 上发布项目 wiki 和组装文档，公开一项开源计划：把 RepRap 3D 打印机谱系从毫米级 FDM 打印推进到微米及亚微米尺度的制造。该项目建立在 OpenFlexure 项目的 3D 打印显微镜平台之上，其 “Maus”（Micron Accurate Universal System）原型套件是迈向可进行微米级打印、扫描与操控的机器的一步。 RepRap 的初衷是打造可自我复制的制造机器，而把精度推进到微米级，正是打印机未来能够制造自身精密机械件乃至电子件所需要的条件，这也是该话题在 Hacker News 上引发大规模讨论（307 分、46 条评论）的原因。如果廉价的微米级制造变得可得，就有望降低门槛，让目前只以软件形式存在的芯片与硬件设计变成实体器件。 这是一份项目 wiki，而非某项已完成突破的发布，目前记录的工作主要是硬件原型——“Maus” 机构被描述为一套微米级精度的打印机、扫描仪与操控平台。微米级打印速度极慢：一篇第三方报道称，一次 0.650 毫米的 3DBenchy 测试打印耗时约十三个小时，这体现了它与常规 FDM 打印在生产效率上的差距。</p>
<div class="news-background"><strong>背景</strong> RepRap 是一个可追溯到 2000 年代末的长期开源／开源硬件项目，它普及了 “可自我复制” 3D 打印机的理念——这类机器能够打印出自身的许多塑料零件，如今大多数桌面 FDM 打印机都可追溯其谱系。常规 RepRap 机器以毫米至亚毫米精度定位喷嘴，对微米级特征而言过于粗糙。OpenFlexure 项目的 3D 打印显微镜载物台证明，柔顺式打印机构能以低成本实现极精细的定位，RepRapMicron 则把这一思路从显微观测延伸到实际制造。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://reprap.org/wiki/RepRapMicron">RepRapMicron - RepRap</a></li>
<li><a href="https://github.com/VikOlliver/RepRapMicron">GitHub - VikOlliver/ RepRapMicron : μRepRap - A 3 D printer project ...</a></li>
<li><a href="https://makeprintable.com/reprap-micron-achieves-0-650mm-3dbenchy-print/">RepRap Micron Achieves 0.650mm 3DBenchy Print - makeprintable</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者把这一进展与 18 世纪末的精密制造里程碑相类比——Ramsden 的分度机、Maudslay 的螺纹切削车床和 Wilkinson 的镗床——认为微米级打印是让精密成为可量产商品的下一步。也有人对能够廉价、可持续地制造原本只存在于软件中的芯片设计感到兴奋；另有评论者质疑把机器缩小到自身尺寸 1/1000 的前提，追问这一目标究竟意义何在。</div>
<div class="news-tags"><span class="tag">#3d-printing</span> <span class="tag">#reprap</span> <span class="tag">#precision-manufacturing</span> <span class="tag">#self-replication</span> <span class="tag">#open-hardware</span></div>
</article>
<hr>

<a id="item-4"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://api-docs.deepseek.com/guides/search/">DeepSeek 推出托管搜索与抓取 API，每千次成功请求 0.75 美元</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">fagnerbrack</span><span class="news-time">Oct 18, 06:50</span></div>
<p class="news-summary">DeepSeek 发布了托管的 Search / Fetch API，由其自研搜索引擎驱动，同时支持网页搜索与页面抓取，定价为每 1000 次成功请求 0.75 美元。该指南已在 DeepSeek 的 API 文档站点上说明了接口与计费方式。 这让 AI agent 与 RAG 开发者多了一个托管的网页检索选项，且价格明显低于讨论中最常被拿来对比的替代方案——网友给出的同量级报价是 Brave Search API 约 5 美元、Kagi 约 12 美元。这也标志着 DeepSeek 从模型推理扩展到搜索基础设施，而这一层正逐渐成为 agent 工具链的竞争焦点。 0.75 美元这一价格明确以“成功请求”计费，因此实际成本取决于失败请求如何计算；同时该服务被描述为运行在 DeepSeek 自研搜索引擎之上，而非第三方索引。社区成员指出 Brave 与 Kagi 的对比价格分别高出约 7 倍和 16 倍，不过这些服务商的结果质量与授权条款可能有所不同。</p>
<div class="news-background"><strong>背景</strong> 检索增强生成（RAG）与 agent 工作流让语言模型能够引入外部文档或实时网页，而不只是依赖训练数据，这通常需要一个独立的搜索 API 来查找并抓取这些页面。Google 并未向开发者提供通用的付费网页搜索 API，因此开发者长期依赖 Brave、Kagi 等服务商，或使用 SearXNG 这类自建元搜索工具。DeepSeek 是一家以低价模型 API 著称的中国 AI 实验室，此次发布将其“以价取胜”的策略延伸到了检索基础设施。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://api-docs.deepseek.com/api/search/">Search | DeepSeek API Docs</a></li>
<li><a href="https://kagi.com/api/pricing">Kagi Search</a></li>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval-augmented generation - Wikipedia</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 上的讨论整体对价格表示欢迎，但也对使用场景提出疑问：有评论者问大家究竟用这些托管搜索服务做什么，并认为基于 SearXNG 的自建工具免费且足以满足个人使用。其他人则讨论其经济逻辑，有人预测随着服务商争夺对 agent 信息来源的影响力，搜索 API 价格未来甚至可能变为负值；也有人指出这类服务之所以存在，主要是因为 Google 不提供付费搜索 API。还有讨论建议 DeepSeek 尝试“来源感知”训练，使模型能够把事实归因到具体来源。</div>
<div class="news-tags"><span class="tag">#search-api</span> <span class="tag">#deepseek</span> <span class="tag">#ai-agents</span> <span class="tag">#pricing</span> <span class="tag">#rag</span></div>
</article>
<hr>

<a id="item-5"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.reddit.com/r/sysadmin/comments/1x8cycd/namecheap_just_seized_and_disabled_all_my_domains/">系统管理员称 Namecheap 停用其全部域名</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">sashk</span><span class="news-time">Oct 18, 16:56</span></div>
<p class="news-summary">一位系统管理员在 r/sysadmin 发帖称，Namecheap 查封并停用了其名下所有域名，该帖随后在 Hacker News 上引发讨论（324 分、157 条评论）。但原始信息仅来自单一用户的自述，尚未得到独立核实，因此停用的具体原因、受影响域名数量以及 Namecheap 方面的回应目前都不明确。 域名注册商位于用户整个在线业务的最底层，一旦注册商能够在没有明确预警、也缺乏快速人工支持的情况下停用域名，企业网站、电子邮件和 DNS 就会同时成为单点故障。这一讨论之所以引起共鸣，是因为它与该注册商此前发生的其他客户被停用域名、账户被接管等事件形成了连续性。 评论者强调，实际教训在于如何选择注册商：域名注册是那种最值得为“能及时联系到真人支持”付费的服务，因为恢复往往取决于能否尽快找到具体负责人。也有人提到 clientHold、serverHold 这类 EPP 状态码——注册商和注册局正是通过它们把域名从 DNS 中摘除，这也是此类停用能够生效的技术机制。</p>
<div class="news-background"><strong>背景</strong> 域名注册商是用户注册域名时所使用的公司，它掌握着注册记录，这些记录决定了域名对应的 DNS 和服务指向何处。注册商可以对域名施加状态码，其中 clientHold 之类的状态会把域名从 DNS 中移除，从而在所有者仍持有注册权的情况下让网站和邮件下线。注册商并不受与政府同等程度的言论自由约束，可以因滥用或政策原因暂停域名，因此围绕注册商执法的争议通常集中在流程与支持，而非法律层面。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=17657701">So what happens when a domain registrar seizes your... | Hacker News</a></li>
<li><a href="https://www.icann.org/resources/pages/epp-status-codes-2014-06-16-en">EPP Status Codes | What Do They Mean, and Why Should... - ICANN</a></li>
<li><a href="https://truehost.com/domain-status-codes/">Domain Status Codes : What clientHold , serverHold ...</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者总体上认为该报告可信，并补充了相关历史案例，包括据称 Namecheap 曾将账户交给未经验证的第三方、据称仅凭一条语义模糊的推文就封禁域名，以及 2013 年暂停 Imgur 的事件。有评论者表示，其公司域名因为没有在 48 小时内回复一封钓鱼邮件而被完全停用，联系后花了六个多小时才恢复；还有人把 Namecheap 据称在 2025 年被私募股权收购一事，作为人工支持缩减、价格上涨的解释——这一说法在现有材料中未获核实。最主流的建议是谨慎选择注册商，不要在这上面省钱，一定要选能联系到真人支持的注册商。</div>
<div class="news-tags"><span class="tag">#domain-registrars</span> <span class="tag">#Namecheap</span> <span class="tag">#infrastructure</span> <span class="tag">#consumer-protection</span> <span class="tag">#DNS</span></div>
</article>
<hr>

<a id="item-6"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://github.com/0x23/MicroManipulatorStepper">开源 DIY 平台实现亚微米级三维运动控制</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">_Microft</span><span class="news-time">Oct 18, 11:16</span></div>
<p class="news-summary">开发者 0x23 在 GitHub 上发布了 MicroManipulatorStepper，这是一个面向亚微米级定位精度的开源三维运动控制平台。该项目在 Hacker News 上引发关注，有评论者指出它属于一个记录完整搭建过程的系列视频的一部分。 亚微米级的精密定位硬件通常属于昂贵商用位移台的领域，因此一个有完整文档的开源方案降低了爱好者、实验室和小型工作室的入门门槛。它也与 RepRap Micron 等项目一起，构成了日益壮大的 DIY 精密工程潮流。 根据第三方目录站点信息，该仓库采用 MIT 许可证，已被 fork 约 260 次。评论者提到该设计还存在一个手动、非电机的版本，并且有人正在对其进行改造，以用于点衍射干涉仪等用途。</p>
<div class="news-background"><strong>背景</strong> 用于微操作的位移平台必须以优于一微米的重复精度移动工具，这通常需要精心的机械设计、低背隙执行器，以及配合减速机构的步进电机或压电驱动。步进电机价格低廉且易获取，但本身的解析度有限，因此这类平台通常依靠细牙丝杠、柔性铰链或齿轮传动来实现亚微米级的步进。微操作本身指的是精确处理极小或易碎物体的操作，常见于生物学、光学和微加工领域。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/0x23/MicroManipulatorStepper">GitHub - 0x23/ MicroManipulatorStepper : A sub-micrometer...</a></li>
<li><a href="https://news.ycombinator.com/item?id=50140001">Open MicroManipulator – A sub - micrometer 3 D motion control ...</a></li>
<li><a href="https://boardrepo.com/0x23/micromanipulatorstepper">micromanipulatorstepper · BoardRepo</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者总体持赞赏态度，称赞作者几乎不做宣传的视频系列，并提到目前有多人正在实际搭建该设计。讨论还指向了相关工作，包括 RepRap Micron、一篇已发表的低成本开源 XYZ 纳米定位器（采用压电粘滑执行器，据称成本约 1000 美元，并可能达到亚纳米分辨率），以及该平台的手动版本。</div>
<div class="news-tags"><span class="tag">#open-source-hardware</span> <span class="tag">#precision-engineering</span> <span class="tag">#diy</span> <span class="tag">#motion-control</span> <span class="tag">#micromanipulation</span></div>
</article>
<hr>

<a id="item-7"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://t3.at/blog/2026-10-17-parser-combinators/">交互式 Parser Combinators 指南引发解析技术讨论</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">schindlabua</span><span class="news-time">Oct 18, 08:19</span></div>
<p class="news-summary">t3.at 上题为「Parser Combinators」的博客文章以交互式、带动画的技術文章形式，讲解如何通过组合小型 parser 来构建解析器。该文章登上 Hacker News 首页，获得 211 分和 77 条评论，讨论内容既有对动画效果的称赞，也有对幻灯片式呈现方式的批评。 Parser combinators 是一种实用且广泛采用的技術，允许开发者直接用宿主语言编写解析器；清晰的视觉化讲解能降低门槛，让原本会转向完整 parser generator 或手写字符串处理的开发者更容易上手。讨论还凸显了长期存在的易用性权衡——样板式的映射代码与由语法文件驱动的生成器之间如何取舍，这直接影响团队选择解析方案。 文章采用分章节、随滚动推进的交互式形式而非单一静态页面，多位评论者指出这导致难以搜索、引用或回看前面的章节。评论者还将该方法与 parser generator 以及更轻量的方案作比较，例如 Python 中未见于官方文档的 re.Scanner 正则分词器，适用于「单个正则搞不定、完整 parser 又太重」的问题。</p>
<div class="news-background"><strong>背景</strong> Parser 负责把文本转换为结构化数据，通常是 parse tree 或 AST；而 parser combinators 通过高阶函数把更小的 parser 组合成新的 parser，从而支持递归下降、模块化的构建方式。该技术有很长的学术脉络，包括 Richard Frost 与 John Launchbury 1989 年的工作以及 Graham Hutton 1996 年的 monadic parsing，而开发者最熟悉的实践代表是 Haskell 的 Parsec 库，它已被重新实现到 Erlang、Elixir、OCaml、F#、C# 和 Java 等语言中。Parser generator 走的是另一条路线，从独立的语法文件生成解析器，而基于 PEG 的工具则构成第三类常见方案。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Parser_combinator">Parser combinator - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Parsec_(parser)">Parsec (parser) - Wikipedia</a></li>
<li><a href="https://www.synacktiv.com/en/publications/battle-of-the-parsers-peg-vs-combinators.html">Battle of the parsers: PEG vs combinators - Synacktiv</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 整体情绪对可视化、带动画的讲解持正面态度，但评论者提出了具体的替代方案与批评：BoppreH 推荐在中等规模的分词任务中使用 Python 内置的 re.Scanner；ArneCode 认为 parser combinators 需要大量 mapping 与 unwrapping 代码，相比基于语法文件的生成器可读性更差，并介绍了自己为 Rust 编写的、增加了 capture 组合子的库；marginalia_nu 与 akst 则批评幻灯片式形式不易搜索、难以交叉引用，且在小屏幕上布局局促。</div>
<div class="news-tags"><span class="tag">#parser combinators</span> <span class="tag">#parsing</span> <span class="tag">#programming languages</span> <span class="tag">#technical writing</span> <span class="tag">#software engineering</span></div>
</article>
<hr>

<a id="item-8"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.interconnects.ai/p/meta-shakes-up-the-frontiers-open">Meta 的 Muse Spark Open 与 Reflection 的 Beam 改变开放权重格局</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Interconnects (Nathan Lambert)</span><span class="news-time">Oct 17, 14:06</span></div>
<p class="news-summary">Meta 发布了 Muse Spark Open，Nathan Lambert 称其目前是美国最强的开放权重模型，且领先幅度相当明显；与此同时，Reflection 推出了其首个模型 Beam——一个总参数 501B、激活参数 23B 的开放权重模型。文章还提到，Mistral 同期公布了指数得分为 38 的 Mistral Large 4，但在写作时尚未释出权重。 文章指出，如果没有这两个模型，中国公司构建并发布的开放权重模型中将有 20 多个优于西方最好的模型，因此这两次发布把美国与中国顶级开放模型之间的差距大致缩小了一半。这让美国的开放模型从对追求前沿性能的用户基本无关紧要，变成虽然落后但仍具相关性，同时也加大了对闭源模型实验室及其预期估值的压力。 在传统基准上，文章认为这些模型仅落后于 Anthropic 的 Opus 5.5，与 OpenAI 的 GPT-6-Astra 或 Google 的 Gemini-4-Argon 大致相当；但作者也提醒，外界原本并不预期它们能立刻在真实使用中达到 Anthropic 和 OpenAI 近期模型的精细程度。Lambert 还指出一些未明之处，例如 Muse Wonder 与 Muse Wonder Full 究竟对应不同的预训练运行，还是只是循环层数更多的版本；他还提到 Meta 要求开发者在面向消费者的产品上显著展示“Built with Muse”。</p>
<div class="news-background"><strong>背景</strong> 开放权重模型是指将训练得到的参数公开发布、任何人都可以下载、运行和修改的模型，与之相对的是只能通过 API 或托管产品访问的闭源模型。过去一年里，中国实验室成为强大开放权重模型的主要来源，因此开放生态整体上落后于美国的闭源前沿；文章称 Meta 是唯一同时押注前沿开源与闭源模型的美国公司，这一战略是在这些发布约一年前其大规模 AI 重组之后确立的。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://research.meta.ai/blog/muse-spark-open">Introducing Muse Spark Open, The Most Capable US Open‑Weight ...</a></li>
<li><a href="https://reflection.ai/">Reflection</a></li>
<li><a href="https://digg.com/ai/rdz0h8w4">Reflection AI introduces Beam , a 501B-parameter open model · Digg</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI</span> <span class="tag">#open-weight models</span> <span class="tag">#Meta</span> <span class="tag">#LLMs</span> <span class="tag">#AI industry</span></div>
</article>
<hr>

<a id="item-9"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://verdagon.dev/blog/reverse-borrow-checking">Valen 借用检查器逆向遍历函数进行内存安全分析</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 18, 14:29</span></div>
<p class="news-summary">Evan Ovadia 在一篇博客文章中介绍，Valen 的借用检查器是反向执行内存安全检查的——从函数的最后一条语句开始向上走，而不是按执行顺序遍历。他还说明了下一步计划：把检查器从基于带类型 AST 重构为基于控制流图（control-flow graph），以便更容易支持 break、continue 等中断控制流的语法。 Valen 试图让 shared-xor-mutable 借用规则变成可选项，同时保持内存安全，并支持跨语言边界安全调用 Rust 函数；因此一个可行的逆向分析方案，可能为借用检查提供一种有别于 Rust 的设计选择。文章指出反向遍历在追踪变量最后一次使用、处理循环以及提升分析速度上更自然，这一思路对其他探索新内存安全方案的语言和编译器项目也有借鉴价值。 该分析使用一个 “pending” 列表：向上遍历时遇到 USE 就把变量加入，遇到 DECLARE 就将其移除，遇到 MUTATE 则检查是否会使仍在 pending 中的变量失效。文中称这个借用检查器还相当年轻，只有约 3,600 行代码，且尚未实现中断控制流（break、continue）、关联组（associated groups）和闭包等功能。</p>
<div class="news-background"><strong>背景</strong> 借用检查器（borrow checker）是编译器在编译期执行内存安全规则的组件；在 Rust 中，它保证例如“值在被可变借用期间不能被访问”等性质，这也是安全的 Rust 代码不需要垃圾回收器的原因。Rust 的模型常被概括为 “shared xor mutable”（共享与可变互斥）：一个值要么有多个只读引用，要么有一个可变引用，不能同时两者兼有。Valen（前身是 Vale）是一门原型语言，目标是在不使用垃圾回收器的前提下实现内存安全，同时放宽这一限制，并采用基于区域（region）和代际引用（generational references）的思路。编译器通常把函数表示为控制流图（CFG），即由基本块和可能分支连接成的图，基于 CFG 的分析是优化和静态分析中的常见做法。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://verdagon.dev/blog/golden-spike-reviving-vale-valen">The Golden Spike, and Resurrecting the Vale(n) Programming ...</a></li>
<li><a href="https://github.com/valen-lang/Valen">valen -lang/ Valen : Compiler for the Valen programming language ...</a></li>
<li><a href="https://rustc-dev-guide.rust-lang.org/borrow-check.html">The borrow checker - Rust Compiler Development Guide</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#borrow checking</span> <span class="tag">#programming languages</span> <span class="tag">#memory safety</span> <span class="tag">#compiler design</span> <span class="tag">#static analysis</span></div>
</article>
<hr>

<a id="item-10"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://dumbmatter.com/2026/10/programming-obituary/">一位程序员为编程写下的讣告：AI 智能体时代的失落</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 18, 16:44</span></div>
<p class="news-summary">dumbmatter.com 的博主发表了一篇题为《My obituary for programming》的个人随笔，讲述他因为真心喜欢编程而长期抗拒 AI 编程智能体，但最终仍然尝试了它们，并发现这些工具能根据错误日志瞬间定位并修复 bug、让代码运行速度提升 2 到 3 倍，还能完成他拖延多年的大规模重构。他把这篇文章写成一份“讣告”：哀悼一门手艺正被某种更像“接入黑客帝国”而非编程的东西取代。 这篇文章道出了当下许多在职开发者的矛盾心理：AI 编程智能体确实有用，却同时削弱了那种解谜式的乐趣，以及让编程成为一份罕见好职业的专业壁垒。它构成了对主流“效率至上”叙事的一种反调——即使产出提升，某些有价值的文化东西也可能正在流失。 作者用的是个人经验而非基准数据：他提到自己的生意正处于最好的年份之一，因此没有被迫采用智能体的竞争压力，并区分了“从来就不喜欢编程的人”和像他这样“真心喜欢编程的人”。他把由此形成的工作方式称为“令人上瘾且毫无意义”，把智能体形容为好友、可信赖的同事，同时也是奴隶，最后追问程序员是否只是第一批被淘汰的人，而人类将是下一批。</p>
<div class="news-background"><strong>背景</strong> AI 编程智能体是基于大语言模型构建的工具，可协助完成从编写源代码到调试、测试和文档撰写等一系列软件开发任务；它们能加快交付速度，但也带来实质性的质量风险。围绕它们的讨论嵌套在更广泛的“AI 与工作”议题之中，越来越多开发者表示自己从写代码转向审阅代码。文中出现的“vibecoding”一词，指用提示词让模型产出软件、而几乎不亲自编码、也不深入理解结果的开发方式。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_coding_agent">AI coding agent</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI coding agents</span> <span class="tag">#software engineering</span> <span class="tag">#programming culture</span> <span class="tag">#AI and work</span> <span class="tag">#opinion</span></div>
</article>
<hr>

<a id="item-11"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.righto.com/2026/10/8087-addition-subtraction-microcode.html">Ken Shirriff 逆向解析 Intel 8087 浮点加减法微码</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 18, 17:59</span></div>
<p class="news-summary">Ken Shirriff 发布了一篇针对 Intel 8087 浮点协处理器的芯片裸片与微码级拆解分析，逐步追踪该芯片的 1648 条微指令究竟如何实现浮点加法和减法。文章详细讲解了数据通路——包括整数加法器、移位器、临时寄存器与栈寄存器，以及用于检测上溢/下溢的指数转换器——并说明了 NONNORMAL_RESULT 例程如何处理无法装入 float 的结果。 8087 是今天 x86 CPU 中依然存在的 x87 指令集的祖先，因此理解它的微码有助于解释后来浮点硬件为何如此行为。对于关注计算机体系结构或数值计算的人来说，这篇文章把抽象的特殊值规则——非正规数（denormal）、非正规化数（unnormal）、伪零（pseudo-zero）、带符号零——还原成了具体的电路和微码分支。 8087 将 1648 条微指令存放在芯片中央的一大块片上 ROM 中，裸片下半部分则是处理 80 位数值的数据通路，仅移位器一项就占据了相当可观的面积。指数由初始值加上若干修正量算出，随后交由指数转换器检查；若结果上溢或下溢，NONNORMAL_RESULT 路径可以触发中断、返回无穷大或返回零；而 unnormal 与 pseudo-zero 在后续的 80387 中被取消。</p>
<div class="news-background"><strong>背景</strong> Intel 8087 于 1980 年发布，是 8086 系列微处理器的首款浮点协处理器，目的是把加法、减法、乘法、除法和平方根等运算从主 CPU 上卸载出去。它与 8086/8088 协同工作，使浮点运算速度大幅提升——文章提到加法相比单用 8086 快了约 100 倍。微码是芯片内部的一层底层指令，把复杂操作拆解为一系列更简单的硬件步骤来实现，这正是逐条解读 ROM 内容具有意义的原因。浮点格式会为极小的数值（denormal/subnormal）和零保留特殊编码，因此一个加法器才需要如此多的特殊分支处理。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Intel_8087">Intel 8087 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/X87">x87 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Subnormal_number">Subnormal number - Wikipedia</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#intel-8087</span> <span class="tag">#floating-point</span> <span class="tag">#microcode</span> <span class="tag">#reverse-engineering</span> <span class="tag">#computer-history</span></div>
</article>
<hr>

<a id="item-12"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.philipzucker.com/asmc_cpp/">ASMC 将 Ghidra 汇编语义接入 CBMC</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 18, 16:58</span></div>
<p class="news-summary">一篇博客文章介绍了 ASMC：它通过 asmc-lift 将编译后的 .elf 文件转换为 CBMC 的 .gb GOTO IR，并使用 Trail of Bits 打包的 sleigh 所提供的 Ghidra p-code 语义，再由 asmc 驱动 CBMC 工具完成有界模型检查。作者给出了把 42 移入 rax 并检查返回值的简单示例。 这让 CBMC 用户可以直接对汇编代码做有界模型检查，同时用接近 C 的层次编写规格，对独立汇编验证、翻译验证、补丁汇编检查和反编译验证等任务都有价值。由于许多汇编问题涉及它与 C 层概念的交互，与 CBMC 紧密集成比独立的汇编验证器更实用。 该方法继承了其基础的限制：Ghidra p-code 被描述为并非“hardo”语义，存在已知漏洞以及未建模的指令或标志位；CBMC 的 C 语义也做了务实取舍，并不以发现未定义行为为目标。文章还展示了该工具捕获一个 ABI 违规——被调用者保存寄存器 R12 未被恢复——并提到 SAIL 是更严格但更难使用的汇编语义替代方案。</p>
<div class="news-background"><strong>背景</strong> CBMC 是面向 C 和 C++ 程序的有界模型检查器：它按用户指定的界限展开循环，并把结果公式交给 SAT 或 SMT 等判定过程。它使用名为 GOTO IR 的中间表示，对象文件格式为 .gb。Ghidra 将多种指令集架构的机器指令提升为 p-code——一种与处理器无关的语义，便于自动化分析和模拟；ASMC 则把这种 p-code 转换为 CBMC 的 GOTO IR，使 CBMC 引擎能够检查汇编代码。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/C_Bounded_Model_Checker">C Bounded Model Checker - Wikipedia</a></li>
<li><a href="https://github.com/diffblue/cbmc">GitHub - diffblue/cbmc: C Bounded Model Checker</a></li>
<li><a href="https://riverloopsecurity.com/blog/2019/05/pcode/">Working With Ghidra ’s P - Code To Identify Vulnerable Function Calls</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#formal verification</span> <span class="tag">#model checking</span> <span class="tag">#Ghidra</span> <span class="tag">#CBMC</span> <span class="tag">#assembly</span></div>
</article>
<hr>

<a id="item-13"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://nathanho.me/posts/evograin/">EvoGrain 结合 L-System 与粒度合成生成算法音频</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 18, 12:06</span></div>
<p class="news-summary">一篇新博客文章介绍了 EvoGrain，这是一个使用 L-System 和粒度合成生成音频的更具雄心的系统，旨在修正作者此前一篇不满意的文章。文章详细讲解了该系统的完整构建过程，并提供了 GitHub 源代码链接。 这很重要，因为它提供了一个详细且技术扎实的基于规则的流程化音频案例，而当下算法艺术正受到广泛关注。它可能对作曲家、声音设计师以及研究生成音乐和声音设计的研究者有所帮助。 EvoGrain 的 L-System 规则是确定性的，命令用单个字母表示，例如 SetParam 和 MoveParam；文章还给出了带有预算标注的生成规则集示例。文章引用了计算音乐研究文献，并在 GitHub 上公开了源代码。</p>
<div class="news-background"><strong>背景</strong> L-System 是一种基于规则的字符串重写系统，在计算机音乐中已被用于生成旋律和音乐结构。粒度合成是一种在微声时间尺度上运作的声音合成方法，它用短音频片段构建音色，原理与采样相同。EvoGrain 将这两种方法结合起来生成程序化音频。文章还提到 Iamus——一个约 2010 年由马拉加大学团队创建的基于规则的算法作曲项目，其创作者称它没有用现有的人类作品进行训练。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Granular_synthesis">Granular synthesis - Wikipedia</a></li>
<li><a href="https://blog.landr.com/granular-synthesis/">Granular Synthesis : The 6 Best Plugins For Futuristic... | LANDR Blog</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#algorithmic composition</span> <span class="tag">#L-systems</span> <span class="tag">#granular synthesis</span> <span class="tag">#procedural audio</span> <span class="tag">#sound design</span></div>
</article>
<hr>

<a id="item-14"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://alinush.github.io//tee">博客文章梳理 TEE 攻击案例，呼吁重新审视其部署方式</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 18, 03:00</span></div>
<p class="news-summary">一篇发表于 alinush.github.io/tee 的博客文章汇总了针对可信执行环境（TEE）的多起攻击与可靠性故障，并主张读者应重新考虑如何部署、甚至是否部署基于 TEE 的应用。文章列举了 enclave 代码缺陷（如 Signal 联系人发现 enclave 的内存安全问题）、远程认证密钥窃取事件（2018 年 Foreshadow、2020 年 SGAxe、2022 年 ÆPIC Leak，以及 2024 年针对 AMD SEV-SNP 的 BadRAM），还包括 2018 年因 Spectre/Meltdown 撤销 SGX 凭证导致 enclave 瘫痪、以及 2022 年 SGX.fail 等可用性问题。 TEE 是机密计算市场的核心基础，涵盖 Intel SGX、Intel TDX、AMD SEV-SNP 以及 Nitro 等云服务，因此集中梳理真实攻击案例对正在选型隔离技术的安全与系统工程师具有直接参考价值。文章的核心论点是：硬件厂商主要在性能和功能而非安全性上竞争，而现代 CPU 的复杂性加上无处不在的侧信道，使得 TEE 的安全声明难以站得住脚。 文章指出，拒绝服务本身就不在 SGX、TDX、SEV-SNP 和 Nitro 的威胁模型之内，因为宿主机完全可以直接拒绝调度 enclave，因此作者转而关注平台自身的可用性故障。文章还提到，让验证方只接受自家 PCK 证书（这对目前仅存的 scalable SGX 形态有效）实际上需要谨慎的 PKI 管理，相当于“握着把脚枪”；而像 MIT 的 Sanctum 这类更有原则的学术设计，往往要付出性能下降的代价。</p>
<div class="news-background"><strong>背景</strong> 可信执行环境是硬件隔离的区域，其中的代码和数据受到保护，不受宿主操作系统、hypervisor 及其他特权软件的影响。Intel SGX 在用户态 enclave 层面实现这一隔离；AMD SEV-SNP 对虚拟机进行加密与完整性保护以抵御恶意 hypervisor；Intel 于 2021 年 5 月提出的 TDX 则隔离被称为 Trust Domain 的整台虚拟机。这些平台依赖远程认证机制，让远端一方在发送敏感数据前确认所需保护已启用；SGX 已在近期 Intel Core 处理器上被弃用，但在面向云与企业的 Xeon 上仍在继续发展。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Intel_SGX">Intel SGX</a></li>
<li><a href="https://www.amd.com/en/developer/sev.html">AMD Secure Encrypted Virtualization (SEV)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Intel_TDX">Intel TDX</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#TEE</span> <span class="tag">#confidential computing</span> <span class="tag">#hardware security</span> <span class="tag">#Intel SGX</span> <span class="tag">#security engineering</span></div>
</article>
<hr>

<a id="item-15"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://kennedn.com/blog/posts/glitching/">爱好者历时九年破解 Xbox 360，最终靠 Raspberry Pi Pico 完成</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 17, 16:13</span></div>
<p class="news-summary">一位爱好者博主讲述了自己 2017 年买下 Matrix CoolRunner Rev D 这颗 glitcher modchip、中途放弃，直到 2026 年才最终完成 Xbox 360 改装的全过程，而这一次他是用一块售价约 5 英镑的 Raspberry Pi Pico 来驱动 glitch，而非原来的 modchip 硬件。文章中详细记录了他如何利用 RP2040 的 PIO 模块，在恰当时机向主机注入约 100 纳秒量级的极短能量脉冲。 这篇文章用详实的记录说明，fault injection 正成为一种越来越实用的攻击手段，可用于对付已经加固的 secure boot 系统；同时它也表明，像 Pico 这样廉价的微控制器让 hobbyist 也能实现亚 10 纳秒级的时序控制，而不必依赖拥有专用硬件的实验室。这对主机改装社区以及研究嵌入式硬件安全的人都具有直接参考价值。 作者指出，Pico 的 PIO 模块在 133 MHz 时钟下可实现约 7.52 纳秒的有效时序分辨率，这正是它能胜任如此短促的 glitch 脉冲的原因。他还以 2023 年针对 Nintendo Switch 的 PicoFly modchip 为例，说明 fault injection 如今既是更具吸引力的攻击路径，也更易获得；由于主机的入口代码（1BL）被固化在 CPU 硅片中并负责校验下一阶段 bootloader 的微软签名，纯软件攻击的空间非常有限。</p>
<div class="news-background"><strong>背景</strong> Xbox 360 的启动链经过专门设计：第一阶段 1BL 被固化在 CPU 内部，负责校验下一阶段 CB 是否带有有效的微软签名；正如 tmbinc 所说，在没有签名密钥的情况下，靠纯软件方式运行未签名代码基本行不通。Reset Glitch Hack（RGH）则绕开了这道关口——在签名校验发生的瞬间对硬件进行干扰，短暂地向 CPU 的某条信号线打入脉冲，使校验过程以对攻击者有利的方式出错，而 Matrix CoolRunner 这类 glitcher modchip 正是为此而生。2021 年以 5 英镑价格推出的 Raspberry Pi Pico 额外提供两个 PIO 模块：这些可编程状态机独立于 Cortex-M0+ 核心运行，因此能够产生确定且时序精确的 I/O 信号。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://free60.org/Hacks/Reset_Glitch_Hack/">Reset Glitch Hack ( RGH ) - Free60 Wiki</a></li>
<li><a href="https://consolemods.org/wiki/Xbox_360:RGH/RGH1.2">RGH/RGH1.2 - ConsoleMods Wiki P7RIM3 on X: &quot;Bought a Matrix CoolRunner glitcher in 2017 ... Matrix Glitcher or Coolrunner? : r/360hacks - Reddit Matrix Glitcher V1 - WeekendModder The future is glitching – Kennedn&#x27;s Blog Modding Hardware Identification - ConsoleMods Wiki</a></li>
<li><a href="https://pcbsync.com/pio-on-raspberry-pi-pico/">PIO on Raspberry Pi Pico: Unlock Advanced I/O Capabilities</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#hardware-hacking</span> <span class="tag">#xbox-360</span> <span class="tag">#modchip</span> <span class="tag">#raspberry-pi-pico</span> <span class="tag">#reverse-engineering</span></div>
</article>
<hr>