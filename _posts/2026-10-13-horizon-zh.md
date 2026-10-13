---
layout: default
title: "Horizon 每日速递：2026-10-13"
date: 2026-10-13
lang: zh
---

> 📅 2026-10-13 · 从 76 条资讯中精选出 20 条重要内容

---

1. [网络攻击触发欧洲超市冷柜进入自动除霜模式](#item-1) <span class="score-badge score-mid">8.0</span>
2. [开发者将 WiFi 7 路由器改造成 320 Msps 软件定义无线电接收机](#item-2) <span class="score-badge score-mid">8.0</span>
3. [Show HN：将 PS2 游戏静态重编译为 WebAssembly](#item-3) <span class="score-badge score-mid">8.0</span>
4. [Filippo Valsorda 发布后量子时代的密码学正确答案指南](#item-4) <span class="score-badge score-mid">8.0</span>
5. [研究员利用 Flask Cookie 密钥在 Google 发现 9 万美元 RCE 漏洞](#item-5) <span class="score-badge score-mid">8.0</span>
6. [Z\.ai 发布法律领域大模型 GLM\-Legal，引发广泛讨论](#item-6) <span class="score-badge score-mid">7.0</span>
7. [Intel 文档里记载、却无任何 CPU 执行过的 x86 指令](#item-7) <span class="score-badge score-mid">7.0</span>
8. [开发者用 C 语言通过 CGI 交付商业 Web 产品](#item-8) <span class="score-badge score-mid">7.0</span>
9. [Codex CLI 默认安装常驻自更新后台守护进程](#item-9) <span class="score-badge score-mid">7.0</span>
10. [十年后回看 Kevin Kelly 2016 年的 AI 预测](#item-10) <span class="score-badge score-mid">7.0</span>
11. [Meta AI 的 'Muse Wonder' 文章引发图像模型好评与隐私担忧](#item-11) <span class="score-badge score-mid">7.0</span>
12. [Python 3\.15 发布：引入 lazy import，3\.10 正式停止支持](#item-12) <span class="score-badge score-mid">7.0</span>
13. [微软发布 Maia 300，欲让自研芯片成为主要 AI 推理系统](#item-13) <span class="score-badge score-mid">7.0</span>
14. [Import AI 476：创造力与 RSI、美国开源权重模型、AI 走向太空](#item-14) <span class="score-badge score-mid">7.0</span>
15. [Linus Torvalds 借助 Claude Code 推进一项大型 Linux 内核改进](#item-15) <span class="score-badge score-mid">7.0</span>
16. [法国多家超市遭网络攻击，数百家门店冷柜被远程关闭](#item-16) <span class="score-badge score-mid">7.0</span>
17. [Lemire 声称在 Python 中实现每秒数十 GB 的 JSON 解析](#item-17) <span class="score-badge score-mid">7.0</span>
18. [用 xxHash 取代 SHA1 做着色器哈希，Unreal 编辑器启动提速](#item-18) <span class="score-badge score-mid">7.0</span>
19. [批评：DHH 的 Campfire Rust 重写表明基准测试仍需人类判断](#item-19) <span class="score-badge score-mid">7.0</span>
20. [通过 esp\-hosted 让 ESP32 充当 Linux 单板机的无线协处理器](#item-20) <span class="score-badge score-mid">7.0</span>

---

<a id="item-1"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.tomshardware.com/tech-industry/cyber-security/unprecedented-cyberattack-cripples-supermarket-fridges-across-europe-as-hackers-activate-automatic-defrosting-delivery-and-store-prices-also-impacted-by-incident">网络攻击触发欧洲超市冷柜进入自动除霜模式</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">Zeekaas</span><span class="news-time">Oct 12, 12:16</span></div>
<p class="news-summary">一场网络攻击扰乱了法国超市连锁 Intermarché 的制冷与定价系统，相关报道提到约有 150 家门店成为目标，攻击者还触发了冷藏柜的自动除霜循环；路透社、BBC 和《世界报》均在 2026 年 10 月 12 日报道了此事。报道还指出配送业务和店内价格同样受到影响。 这是一个发生在传统关键基础设施行业之外的、关于遗留 OT（运营技术）暴露面的现实案例：零售制冷控制器属于嵌入式、生命周期极长的设备，且越来越多地联网，因此某一类控制器被攻破就可能大规模影响食品安全、能耗和门店运营。这说明 OT/IoT 安全风险已经延伸到普通商业环境，而不再只是电网和工厂的问题。 社区分析认为嫌疑对象很可能是已服役 15 至 20 年的 Danfoss 制冷控制器，例如 SM800（2021 年终止服务）和 SC355（2016 年终止服务），而 Claroty 的 Team82 研究团队此前也发布过关于 Danfoss 制冷控制器漏洞的研究。触发除霜是一种成本低但影响大的操作：它无需物理接触即可浪费能源并干扰温度控制。</p>
<div class="news-background"><strong>背景</strong> OT（运营技术）指直接控制物理设备的硬件与软件，例如负责管理超市冷藏柜压缩机循环和除霜时序的制冷控制器。自动除霜是一种按计划执行的常规循环，系统会暂停制冷或启动加热元件以清除蒸发器上的结冰，这已是现代商用制冷的标准配置。这些控制器越来越多地接入网络，因为厂商大力宣传远程诊断和跨门店能效监测的价值，让运营方无需为简单任务派遣维修工程师。遗留控制器往往无法打补丁，而一台已稳定运行数十年的控制器通常会被继续使用，因为更换它在短期内看不到明显收益。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://insanecyber.com/legacy-ot-systems-why-hackers-love-them/">Legacy OT Systems: Why They’re Still a Hacker’s Best Friend</a></li>
<li><a href="https://www.fridgefreezerdirect.co.uk/ffd-info-centre/commercial-refrigeration/understanding-types-of-defrost">Types of Defrost in Commercial Refrigeration - FFD</a></li>
<li><a href="https://www.commercialcoolingdirect.com/knowledge/buying-guides/defrosting-methods-in-commercial-refrigerators-and-freezers/">Defrosting Methods in Commercial Refrigerators and Freezers ...</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 上的评论者反驳了“为什么要把冰柜连上互联网”这种想当然的说法，认为利润微薄、以轮班作业为主的运营方根本没有余力去做安全评审或按周期更换设备，而且部分实验室设备和其他机械实际上被订阅锁死，必须联网才能运行。其他人则指出了具体的遗留 Danfoss 型号和 CVE 线索，还有人猜测此事可能与 2026 年 8 月一起涉及美军基地小卖部冰柜的类似事件有关，但同时明确表示两者也可能毫无关联。</div>
<div class="news-tags"><span class="tag">#cybersecurity</span> <span class="tag">#OT/IoT security</span> <span class="tag">#critical infrastructure</span> <span class="tag">#legacy systems</span> <span class="tag">#vulnerability disclosure</span></div>
</article>
<hr>

<a id="item-2"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://github.com/h0m3us3r/w1700k-sdr">开发者将 WiFi 7 路由器改造成 320 Msps 软件定义无线电接收机</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">djfergus</span><span class="news-time">Oct 12, 12:41</span></div>
<p class="news-summary">一位开发者（h0m3us3r）在 GitHub 上发布了一个项目，将一台 WiFi 7 路由器改造成能够以 320 Msps（每秒 320 兆采样）进行采样的软件定义无线电（SDR）接收机。该项目建立在同一开发者此前的 eSpDR 项目之上，后者曾把一块 ESP32 Wi-Fi 微控制器变成 SDR。 这表明，普通的消费级 Wi-Fi 硬件——其射频部分本就很大程度上由软件驱动——或许可以充当廉价的 SDR 前端，而无需专用实验室设备。若该方法能够推广，爱好者和工程师将有望以低成本获得 5 GHz 频段的高采样率接收机，用于实验和射频测量。 该接收机实现了 320 Msps 的采样率，对应极宽的瞬时带宽；同一开发者此前还曾基于 ESP32 打造过名为 eSpDR 的 SDR。评论者指出，该路由器所用的芯片组也出现在 Banana Pi R4 上，而后者内置了用于 NVMe 的 PCIe 接口，暗示这一方案可能移植到该开发板上。</p>
<div class="news-background"><strong>背景</strong> 软件定义无线电（SDR）是一种无线电系统，其中传统上由模拟硬件完成的功能——如混频器、滤波器和解调器——改由软件执行，从而使单一设备能够处理多种无线协议。320 Msps 这一数字指的是采样率，即每秒采集的离散信号样本数，它决定了可表示的最高频率（奈奎斯特极限）。Wi-Fi 7（IEEE 802.11be，品牌名为“极高吞吐量”）工作在 2.4、5 和 6 GHz 频段，因此将其射频部分挪用于通用 SDR 接收格外引人注目，因为这些芯片是大规模量产且廉价的。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Software-defined_radio">Software-defined radio</a></li>
<li><a href="https://en.wikipedia.org/wiki/WiFi_7">WiFi 7</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sampling_(signal_processing)">Sampling (signal processing) - Wikipedia</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 的评论者反应热烈，他们提到了该开发者此前基于 ESP32 的 eSpDR 项目，并希望更多常见的 Wi-Fi 网卡能变成低成本的 SDR。有评论者认为，由于芯片组相同，这一方案很可能在 Banana Pi R4 上也能运行；另一位评论者则将其成本与传统服务监测仪作了有利对比，并畅想了搭建廉价射频测量装置的可能性；还有人提出了监管方面的疑问，即三星为何限制第三方使用手机上的 FM 收音机。</div>
<div class="news-tags"><span class="tag">#Software Defined Radio</span> <span class="tag">#WiFi 7</span> <span class="tag">#Hardware Hacking</span> <span class="tag">#RF Engineering</span> <span class="tag">#Embedded Systems</span></div>
</article>
<hr>

<a id="item-3"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://github.com/snuri00/ps2-web-recomp">Show HN：将 PS2 游戏静态重编译为 WebAssembly</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">deadxwarrior</span><span class="news-time">Oct 12, 06:46</span></div>
<p class="news-summary">一个由用户 snuri00 发布、名为 ps2-web-recomp 的 GitHub 项目以 Show HN 形式登上 Hacker News，其内容是将 PlayStation 2 游戏静态重编译为 WebAssembly。该帖获得 272 分和 143 条评论，讨论涉及重编译项目的信任与恶意软件风险、AI 在这类工作中的角色，以及一个相关的 PS Vita ARM 转 WASM 的转译器项目。 静态重编译通过提前将原主机二进制代码翻译为目标平台代码，让游戏逻辑直接在宿主机器上执行，从而规避传统模拟器的运行时开销；而面向 WebAssembly 则意味着这类游戏原则上可以在浏览器中运行，无需针对特定平台单独构建。评论还反映出更大的趋势：日益增多的反编译／重编译项目，尚未建立起老牌模拟器社区那样的审查与信任声誉。 现有材料并未说明该项目具体覆盖了哪些游戏、哪些 PS2 硬件模块或使用了什么工具链，且该条目被定性为一个由个人开发的早期项目，尚未展现出广泛影响。评论者指出，对结构复杂的多芯片主机做静态重编译，仍然依赖手工编写的运行时来替代原硬件行为，而如何验证这类二进制文件的来源仍是一个未解决的问题。</p>
<div class="news-background"><strong>背景</strong> PlayStation 2 的核心是一颗名为 Emotion Engine 的定制芯片，它是一颗基于 MIPS 架构、主频约 294.912 MHz 的 CPU，与两个向量处理单元（VPU0 和 VPU1）以及 DMA 等模块紧密协作。静态重编译是一种在无需原始源码的情况下，把为旧硬件架构编写的二进制程序转换为可在现代硬件上执行的程序的技术；与通过额外软件层复现主机行为的模拟器不同，重编译后的游戏代码直接在处理器上运行，由运行时负责提供主机原本的服务。WebAssembly 是一种可移植的二进制指令格式，可运行在浏览器的 JavaScript 引擎中，如今也越来越多地运行在浏览器之外，因此很自然地成为运行翻译后游戏代码的目标平台。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Emotion_Engine">Emotion Engine - Wikipedia</a></li>
<li><a href="https://www.copetti.org/writings/consoles/playstation-2/">PlayStation 2 Architecture | A Practical Analysis PS2 System Architecture | ps2dev/ps2sdk | DeepWiki Emotion Engine - PS2 Developer wiki - psdevwiki.com PlayStation 2 technical specifications - Wikipedia Sony&#x27;s Emotionally Charged Chip - Inside the PS2 Architecture Inside the PS2’s Emotion Engine - by ObsoleteSony</a></li>
<li><a href="https://retroportingtoolkit.com/docs/start/what-is-static-recompilation">What is static recompilation? - Retro Porting Toolkit</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者总体上对这项重编译工作表示赞赏，但 aceazzameen 提出了信任方面的担忧：原生反编译项目近来大量涌现，而它们至少目前还缺乏模拟器社区那样的审查机制，因此是否存在隐藏恶意软件的风险值得考虑。zuInnp 称赞重编译成果，同时对 AI 给自己职业带来的变化表达了复杂情绪；Megabinator 建议把重编译器本身也编译成 WebAssembly，这样就能托管在任何地方，并直接在浏览器中完成转换；eluusive 则开玩笑说，没有漫长的 CD 读取画面还怎么玩《Gran Turismo》。kodablah 分享了一个相关项目 vitaslop——一个用 WASM 构建的 PS Vita ARM 转 WASM 转译器，支持 WebGPU 着色器与音频转码，他表示尽管目前只测试了少量游戏，但在旗舰 Android 手机的 Chrome 移动版上运行效果相当不错。</div>
<div class="news-tags"><span class="tag">#webassembly</span> <span class="tag">#static-recompilation</span> <span class="tag">#emulation</span> <span class="tag">#retro-gaming</span> <span class="tag">#reverse-engineering</span></div>
</article>
<hr>

<a id="item-4"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://words.filippo.io/right-answers/">Filippo Valsorda 发布后量子时代的密码学正确答案指南</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 12, 13:44</span></div>
<p class="news-summary">Filippo Valsorda 发布了《（后量子）密码学正确答案》，这是继 Colin Percival（2009 年）、Thomas Ptacek（2015 年）以及 Latacora（2018 年、2024 年）之后该开发者指南系列的最新一篇。更新后的建议指出，所有非对称加密答案相较 2018 年都已改变，多数相较 2024 年也已改变：非对称加密推荐使用 HPKE 搭配 MLKEM768-X25519（即 X-Wing），对称加密推荐 XAES-256-GCM 或 XChaCha20Poly1305，对称「签名」则推荐 HMAC-SHA-256。 这是一份来自知名密码学专家、面向开发者且立场明确的可落地建议，而它出现的时点恰逢后量子迁移时间表据称发生剧变——文中称已有共识需要在 2029 年前完成迁移。这意味着目前依赖 RSA 或椭圆曲线密钥交换来提供长期安全性的团队，可能需要比原计划更早重新审视库与协议选型；而一份被广泛引用的速查表，也会影响众多库和应用所采用的默认配置。 后量子 HPKE 的 KEM 目前仍处于草案阶段，而且被不必要地拆分到四份不同的草案中，作者因此编写了 filippo.io/hpke-pq 将这些实现发布出来，并称草案作者已承诺不会更改线格式。该指南还把「用你能负担得起的最好的模型做代码审查」列入密码学正确答案，并认为对称密码学不受实质影响，因为 Grover 算法并不会明显改变实际建议；同时文中引用了一系列 wolfSSL 与 Botan 的 CVE 作为反面教材。</p>
<div class="news-background"><strong>背景</strong> 「密码学正确答案」是一项延续多年的非正式传统：由受尊敬的密码学家直接给开发者一套明确的算法选择建议，而非罗列一堆选项；早期版本主要推荐 NaCl 及其后继者 libsodium。后量子密码学指能够抵御未来量子计算机攻击的算法，其中 ML-KEM（原名 CRYSTALS-Kyber）已于 2024 年 8 月被 NIST 标准化为 FIPS 203，作为抗量子的密钥封装机制。HPKE（混合公钥加密）是一种标准构造，把密钥封装机制与对称加密结合起来，让缓慢的非对称运算只需处理一小段密钥。Grover 算法是一种量子搜索算法，对对称密码只能带来平方级加速，因此该指南认为对称密钥长度无需大幅提升。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ML-KEM">ML-KEM</a></li>
<li><a href="https://en.wikipedia.org/wiki/HPKE">HPKE</a></li>
<li><a href="https://en.wikipedia.org/wiki/Libsodium">Libsodium</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#cryptography</span> <span class="tag">#post-quantum</span> <span class="tag">#security</span> <span class="tag">#software-engineering</span> <span class="tag">#ML-KEM</span></div>
</article>
<hr>

<a id="item-5"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://simonkoeck.com/writeups/google-devsite-flask-session-pickle-rce">研究员利用 Flask Cookie 密钥在 Google 发现 9 万美元 RCE 漏洞</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 12, 14:40</span></div>
<p class="news-summary">一位安全研究员发布 writeup 披露：developers.google.com 下发的 Flask session cookie 所使用的签名密钥就藏在 cookie 自身之中，攻击者可借此伪造 cookie，并最终在 Google 共享的 DevSite 平台上实现远程代码执行，获得 9 万美元赏金。奖金构成为 Normal Google Applications（T2）S0 级 RCE 基础奖金 75,000 美元，再因报告质量优异乘以 1.2。 这条攻击链说明，一个设计错误——把签名密钥存进它所保护的数据里——足以瓦解整个共享平台（而非单个应用）的会话完整性，让两次无需认证的 GET 请求变成在 Google 服务器上执行代码。它也提醒所有使用客户端 session 的团队：签名不等于安全，而反序列化只有在无人能伪造外层 cookie 时才勉强“安全”。 cookie 的 payload 经过 zlib 压缩，其中包含一个被 Flask 标记为字节值的 &quot; b&quot; 键，base64 解码后得到一个 oauth2client.client.OAuth2WebServerFlow 的 pickle 对象，进而泄露了用于派生 HMAC-SHA1 签名密钥的 OAuth client secret；研究员通过篡改签名中的某个字符（被拒绝）并用恢复出的密钥重新签名原始 payload（被接受）来确认密钥有效。回调逻辑会把 flow 对象从 session 中读出并交给 pickle.loads 处理，因此只要自选一个 CSRF token、并在对应的 flow 键下放入构造好的 pickle，即可实现代码执行；writeup 称该密钥可在七个 Google 域名上签发有效 session，包括 developers.google.com、firebase.google.com、developer.android.com、source.android.com 和 docs.partner.android.com。</p>
<div class="news-background"><strong>背景</strong> Flask 把客户端 session 存放在一个经过密码学签名（通过 itsdangerous 库）但未加密的 cookie 中，因此任何拿到 cookie 的人都能读到其内容；签名本应防止篡改，因为只有服务器知道 SECRET_KEY。但在这个案例中，密钥并非独立的随机值，而是一个被嵌进 session 数据本身的 OAuth client 凭据，所以只要从任意一个 cookie 中把它提取出来，防篡改保护就彻底失效。攻击链的后半段依赖 Python 的 pickle 格式：反序列化不可信的 pickle 数据可以执行任意代码，这也正是 writeup 的修复清单要求对一切跨越客户端边界的数据弃用 pickle、并把 OAuth flow 对象以不透明引用形式保留在服务端的原因。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://cyberpress.org/critical-google-devsite-flaw/">Critical Google DevSite Flaw Let Attackers Execute Remote ...</a></li>
<li><a href="https://stackoverflow.com/questions/42283778/generating-signed-session-cookie-value-used-in-flask">Generating signed session cookie value used in Flask Code sample</a></li>
<li><a href="https://hackindex.io/tools/flask-cookie">Flask Session Cookie Decoder &amp; Forger — Decode, Verify ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#security</span> <span class="tag">#vulnerability-research</span> <span class="tag">#remote-code-execution</span> <span class="tag">#flask</span> <span class="tag">#bug-bounty</span></div>
</article>
<hr>

<a id="item-6"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://z.ai/blog/glm-legal">Z.ai 发布法律领域大模型 GLM-Legal，引发广泛讨论</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">ilreb</span><span class="news-time">Oct 12, 16:11</span></div>
<p class="news-summary">Z.ai 在其博客 z.ai/blog/glm-legal 上发布了面向法律领域的 GLM-Legal 大语言模型。该发布在 Hacker News 上引发强烈反响，获得 432 分和 248 条评论，讨论集中在法律基准测试、厂商信任与隐私，以及高风险场景下的人类在环（human-in-the-loop）要求。 法律工作是高风险领域，出错可能影响个人权利、财务和生活，因此厂商推出专门的法律大模型会立刻引出对评测质量与责任归属的质疑。讨论也反映出更广泛的行业趋势：有评论者引用 Anthropic 近期政策，指出当 AI 产品被用于可能影响健康、法律权利、财务或基本服务获取的场景时，必须有一名具备资质的“人类在环”。 本次提供的材料未包含该博客文章的技术细节，因此训练数据、模型规模或基准得分等信息无法在此核实。在可见的评论中，一位自称律师的用户表示对某项基准测试 20% 的通过率并不感到印象深刻；另一位用户则认为基准应区分为通用任务与新颖任务，而不应被当作单一数字看待。</p>
<div class="news-background"><strong>背景</strong> 领域专用大模型是指为特定行业适配或微调的通用模型，在法律领域通常用专门的基准来评测其在合同审查、文书起草和法律检索等方面的能力。人类在环（human-in-the-loop，HITL）指的是人类主动参与自动化系统的运行、监督或决策过程的机制，这也是法律 AI 常被定位为起草辅助工具而非自主法律建议的原因。评论者还提到 Z.ai 此前的“工作区快照”事件，引用一篇第三方博客文章称该公司在每次提示前会抓取用户的整个工作区，并认为这种行为会削弱人们对法律产品的信任。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.legalbenchmarks.ai/?trk=public_profile__posts-text">Legal Benchmarks - Legal AI Benchmarking</a></li>
<li><a href="https://en.wikipedia.org/wiki/Human-in-the-loop">Human - in - the - loop - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/human-in-the-loop">What Is Human In The Loop (HITL)? | IBM</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 整体情绪褒贬不一：有评论者欢迎更好的法律工具并提出司法可及性的论点，例如有人提到印度约有 5800 万件待审案件，希望 LLM 能筛出情节清晰的案件以释放法官的时间。质疑主要针对可能无法区分通用与新颖法律任务的基准，以及据称 20% 的通过率；而一个突出的反驳观点是，鉴于 Z.ai 此前涉嫌的工作区快照行为，信任才是真正的瓶颈，且高风险用途需要人工复核——正如 Anthropic 政策所要求的那样。</div>
<div class="news-tags"><span class="tag">#LLM</span> <span class="tag">#legal-tech</span> <span class="tag">#AI-safety</span> <span class="tag">#privacy</span> <span class="tag">#benchmarks</span></div>
</article>
<hr>

<a id="item-7"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://purplesyringa.moe/blog/who-is-vfmaddrnd231pd/">Intel 文档里记载、却无任何 CPU 执行过的 x86 指令</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">pngmangi</span><span class="news-time">Oct 12, 21:12</span></div>
<p class="news-summary">博主 purplesyringa 在一篇博文中调查了 VFMADDRND231PD 这条指令：它是一条针对打包双精度浮点值的 FMA（融合乘加）指令，带有按指令指定的舍入控制，出现在 Intel 软件开发手册（SDM）中，但没有任何汇编器认识它，也没有已知的 CPU 执行它。据相关报道，该指令出现于 2024 年版手册，并在 2026 年版中被删除，且未给出任何说明。 这个案例说明，即便是权威的厂商文档也可能描述从未真正流片的硬件，这对依赖指令集手册来编写编译器、汇编器、模拟器或底层工具的人来说尤为重要。它也引出了一个更广泛的讨论：当程序员只能通过编译器和抽象层间接接触指令时，会损失多少真正的理解。 该指令的编码为 VEX.DDS.128.66.0F3A.W1 B8 /r /ib，其中 “DDS” 表示第二个寄存器操作数编码在 VEX.vvvv 字段中，第一个源寄存器则被结果覆盖，同时由 imm8 指定舍入模式。一位评论者指出，旧版 binutils 明确解释了这些 VEX.vvvv 约定（必须为 1111b、NDS、DDS、NDD2），而这正是该指令晦涩名称所掩盖的细节。</p>
<div class="news-background"><strong>背景</strong> FMA（融合乘加）指令在一个步骤内计算 a*b+c 并只做一次舍入，广泛用于科学计算、机器学习和图形学；在 x86 上它作为 FMA3/FMA4 扩展的一部分引入，并使用 VEX 编码，把操作数与前缀信息压缩进紧凑的字节模式中。Intel 软件开发手册是编译器与模拟器作者赖以判断哪些指令存在、如何编码的权威参考。VFMADDRND231PD 属于带有内嵌舍入控制的一类指令，其舍入模式按指令单独指定，而不是通过 MXCSR 控制寄存器设置。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.felixcloutier.com/x86/vfmaddrnd231pd">VFMADDRND231PD — Fused Multiply-Add of Packed Double ...</a></li>
<li><a href="https://news.lavx.hu/article/intel-s-manual-described-an-instruction-no-cpu-ever-executed">Intel&#x27;s manual described an instruction no CPU ever executed</a></li>
<li><a href="https://asm-docs.microagi.org/x86/vfmaddrnd231pd.html">Vfmaddrnd231pd - ASM Reference</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者大多倾向于“硬件问题”这一推测：enjoyyourlife 给出了 Felix Cloutier 的参考页面链接，并猜测该指令因从未真正可用而被删除。pbsd 引述旧版 binutils 手册，精确说明了 VEX.vvvv/DDS 的语义；Lerc 则以此指令为例，说明晦涩难读的助记符如何让人远离与机器的直接交互。LoganDark 起初以为这个名字是某个 RISC-V 扩展，读文章后才确认它属于 x86。</div>
<div class="news-tags"><span class="tag">#x86</span> <span class="tag">#assembly</span> <span class="tag">#instruction-set</span> <span class="tag">#hardware</span> <span class="tag">#reverse-engineering</span></div>
</article>
<hr>

<a id="item-8"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://prophitt.me/writing/a-modern-web-app-in-c">开发者用 C 语言通过 CGI 交付商业 Web 产品</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 12, 20:52</span></div>
<p class="news-summary">一位开发者发布文章，介绍了他用纯 C 语言编写、通过 CGI（Common Gateway Interface，通用网关接口）在 OpenBSD 上运行的商业 Web 产品 marketyour.games。该应用采用被称为 BCHS 的技术栈——OpenBSD、C、httpd 和 SQLite——打包为一个静态链接的单一二进制文件加一个 SQLite 数据库文件，整个系统据称只依赖三个库。 这篇文章刻意反衬当下层层堆叠框架、包管理器和容器运行时的趋势，主张 CGI 式服务拥有更少的活动部件和更小的供应链攻击面。如果这一思路获得关注，可能会影响开发者对依赖风险和部署简洁性的思考，尤其是在软件包仓库被攻击事件频发的背景下。 在这种模式下，每个请求都会派生一个新进程，部署新版本只需替换一个文件，无需重启服务器也不会停机，并通过 OpenBSD 的 pledge 和 unveil 来降低权限、限制文件访问。作者指出 CGI 开箱即用的功能很少——他自己写了一个 cgi.h 头文件，并提到存在 kcgi 等替代库；他还表示如果 fork 的开销日后成为问题，FastCGI 是一条简单的升级路径。</p>
<div class="news-background"><strong>背景</strong> CGI 是一种历史悠久且已标准化的接口，让 Web 服务器在每个请求时调用一个外部程序，通过环境变量传递输入，并将该程序的输出作为 HTTP 响应返回；这类程序传统上存放在 cgi-bin 目录中。它是 1990 年代构建动态网站的主流方式，但在 2000 年代初逐渐失宠，原因是每请求 fork 一个进程被认为开销过高，而且各类框架提供了更多开箱即用的功能。文章的出发点是，这些反对意见在现代内核上已不再成立，因为内核已对进程 fork 做了大量优化。单一二进制部署（应用及其资源打包为一个可执行文件）是类似思路，因 Go 等语言而流行。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.e-reading-lib.com/htmbook.php/orelly/web/cgi/ch01_01.html">[Chapter 1] The Common Gateway Interface ( CGI ) - e-Reading Library</a></li>
<li><a href="https://moonvine.io/docs/glossary/c/cgi-bin-directory/">CGI - Bin Directory — Moonvine</a></li>
<li><a href="https://rootknecht.net/blog/gin-gonic/">Single binary web app with Gin-Gonic · Rootknecht.net</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者大多印证了这一做法：有人指出 busybox 内置了对 cgi-bin 的支持，并认同文章论证充分，尤其是在用 pledge 和 chroot 降低权限方面。其他人则分享了切身的平行经验——一个客户端编译为 WebAssembly、服务端用 C++ 并置于 nginx 之后的游戏项目，以及一家基于 C 和 FastCGI 构建、运行良好直到迁移到微软工具链后才问题频出的 Web 开发公司。一位 Go 的拥护者指出，Go 同样支持单二进制服务（在 CGO_ENABLED=0 时甚至不依赖 libc），但也坦言自己并不喜欢用 C 进行并发编程。</div>
<div class="news-tags"><span class="tag">#C</span> <span class="tag">#Web Development</span> <span class="tag">#CGI</span> <span class="tag">#Minimal Dependencies</span> <span class="tag">#Systems Programming</span></div>
</article>
<hr>

<a id="item-9"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://github.com/openai/codex/issues/48195">Codex CLI 默认安装常驻自更新后台守护进程</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">whimblepop</span><span class="news-time">Oct 12, 18:29</span></div>
<p class="news-summary">根据 OpenAI Codex CLI 仓库的 GitHub issue（#48195），自 0.157.0 版本起，只要打开一次交互式 codex 会话，就会静默启动一个受管的后台守护进程（app-server --managed-daemon）：它在窗口关闭后依然存活，把约 374MB 的平台包复制到与已安装 CLI 解耦的版本化目录中，并启动一个分离的更新器，在启动 5 分钟后检查更新，之后每小时检查一次。该 issue 要求 OpenAI 把 daemon_auto_start 这个行为改为可选（opt-in）而非默认开启。 Codex CLI 是被广泛使用的 AI 编程代理，默认开启的常驻后台进程与自动更新器会让大量开发者用户对信任、隐私和资源占用产生担忧。社区第一手反馈中出现的数 GB 磁盘占用、自动更新破坏文件权限等问题，说明这不仅是设计层面的抱怨，而是 Codex 用户当下就需要处理的实际运维问题。 目前没有正式文档化的关闭方式，但评论者指出该功能当前受一个 feature flag 控制，即在 `~/.codex/config.toml` 中设置 `[features] daemon_auto_start = false`；此外还有把 `~/.codex` 下的 pid、lock 等文件软链到 `/dev/null` 并用 `chattr +i` 标记为不可写的变通做法。相关行为还包括：自动更新会在 60 秒 drain 预算结束后强杀正在进行的 turn（issue #40969），以及 issue #48043 报告在 Windows 11 上守护进程安装失败并报 &quot;Access is denied&quot;。</p>
<div class="news-background"><strong>背景</strong> Codex CLI 是 OpenAI 开源的命令行 AI 编程代理，可在用户本地机器上读写文件、执行命令并完成软件开发任务。厂商正越来越多地把这类代理推向“常驻”（persistent）模式，这需要后台守护进程与自更新机制来保证代理随时可用且保持最新，但这与“CLI 工具应由包管理器安装、更新和卸载”的普遍预期相冲突。有评论者指出 Claude Code 采用类似的运行模式：在本地的 share 目录下保存带版本号的二进制，并运行后台进程。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/openai/codex/issues/48195">CLI: make `daemon_auto_start` opt-in — a persistent, self ...</a></li>
<li><a href="https://daily.dev/posts/codex-cli-installs-a-persistent-self-updating-background-daemon-by-default-unpmj86e7">Codex CLI installs a persistent, self-updating background ...</a></li>
<li><a href="https://news.ycombinator.com/item?id=50060694">Codex CLI installs a persistent, self-updating background ...</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 这个约 239 条评论的 Hacker News 讨论整体偏负面：有用户称该守护进程在他系统上总共占用约 12GB，另有人报告自动更新会随机破坏权限、把 `.git` 变成只读并阻断任务目标，还有多人指出关闭方式没有文档、非常折腾。给出的关闭路径是把 `daemon_auto_start` 设为 false，并“废掉”`~/.codex` 下的 pid/lock 文件；反方观点则认为 Claude Code 其实做了差不多的事、包管理器本可以更合理地处理后台更新，也有开发者表示相比这类“过度工程化”的代理，更青睐 hax 这样以 bash 为主的极简 harness。</div>
<div class="news-tags"><span class="tag">#codex-cli</span> <span class="tag">#developer-tools</span> <span class="tag">#ai-coding-agents</span> <span class="tag">#privacy</span> <span class="tag">#software-quality</span></div>
</article>
<hr>

<a id="item-10"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://taylor.town/kk-ai-2026">十年后回看 Kevin Kelly 2016 年的 AI 预测</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">surprisetalk</span><span class="news-time">Oct 12, 15:16</span></div>
<p class="news-summary">taylor.town 上的一篇回顾文章《Kevin Kelly&#x27;s 2016 AI Predictions, 10 Years Later》重新审视了 Kelly 在 2016 年书中做出的 AI 预测，并在 Hacker News 上引发讨论，因评论内容扎实而获得 7.0/10 的评分。gwern、stephen_cagle、cousinbryce、rossdavidh 和 at1as 等评论者就这些预测在十年后的准确性展开了辩论。 这类回顾之所以重要，是因为 AI 预测会影响资金投入、研究方向和公众预期，同时也提供了一个难得的机会，用十年的实际结果来检验一位知名技术专家的 2016 年论断。讨论还凸显了一个持续存在的分歧：AI 究竟是走向通用超级智能，还是演变为一堆各自专用的窄领域系统。 评论者普遍认为 Kevin Kelly 的预测大致相当于抛硬币：stephen_cagle 把这批预测&quot;完全任意地&quot;拆成 16 条，即便从宽计算也只命中约 8 条，他指出这算不错，但远谈不上够格冠以书中&quot;Inevitable&quot;（必然）之名。gwern 则认为最重要的一条预测是 Kelly 对奇点（Singularity）的彻底否定，而自 2016 年以来，公众情绪转向背离这一论断的幅度也最大。</p>
<div class="news-background"><strong>背景</strong> Kevin Kelly 是《连线》（Wired）杂志的联合创始人，也是 2016 年出版的《必然》（The Inevitable）一书的作者，书中列举了他认为将塑造未来数十年的若干技术力量，AI 便是其中之一。讨论中提到的&quot;奇点&quot;（Singularity）是 Ray Kurzweil 等人推广的概念，指 AI 最终会在一次迅速失控的起飞中超越人类智能。&quot;The Bitter Lesson&quot;是 Rich Sutton 提出的著名论点，认为随算力扩展的通用方法往往会胜过人工设计的领域专用方法；而 Stockfish 是一款历史悠久的国际象棋引擎，在讨论中被用来说明专用软件在国际象棋上仍能击败大型语言模型。</div>
<div class="news-discussion"><strong>社区讨论</strong> 整体情绪褒贬不一，且偏向批评：stephen_cagle 给 Kelly 打分约为 16 条预测中命中 8 条，并指出 Kelly 最干净利落的那条预测——AI 会遵循由用户驱动的网络效应——并未成真；cousinbryce 则冷言指出 Google 的主要产品&quot;过去是、现在依然是广告&quot;。gwern 聚焦于 Kelly 对奇点的否定，认为这是最关键的一条论断，并暗示过去十年积累的证据已使舆论背离 Kelly 的立场。rossdavidh 则持相反看法，认为 Kelly&quot;AI 的主体将是专用软件大脑&quot;这一预测比&quot;The Bitter Lesson&quot;更经得起时间检验，理由是 Stockfish 在国际象棋上仍能击败最大的 LLM，且真正产生生产力的 AI 大多是为特定用途定制的；at1as 还轻松地补充推荐了 Kelly 已绝版的摄影集《Vanishing Asia》。</div>
<div class="news-tags"><span class="tag">#AI predictions</span> <span class="tag">#Kevin Kelly</span> <span class="tag">#Singularity</span> <span class="tag">#AI development</span> <span class="tag">#technology forecasting</span></div>
</article>
<hr>

<a id="item-11"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://research.meta.ai/blog/muse-wonder">Meta AI 的 &#x27;Muse Wonder&#x27; 文章引发图像模型好评与隐私担忧</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">meetpateltech</span><span class="news-time">Oct 12, 16:48</span></div>
<p class="news-summary">Meta AI 一篇题为 &#x27;Muse Wonder&#x27; 的研究博客文章在 Hacker News 上引发大量讨论，获得 527 分和 299 条评论，评论者普遍将其视为 Meta Muse 模型系列中的图像生成版本发布。文章正文并未提供，但评论者 Simon Willison 贴出了 &#x27;pelican&#x27;（鹈鹕）测试输出，并对比了 Muse 1.2（8 月）和 Muse 1.3（9 月），另一位评论者则表示自己对 Muse Wonder 做了图像转 HTML 的测试。 Muse 系列已经是 Meta 消费级 AI 布局中的旗舰产品——据报道，Muse 个人 AI 智能体应用在 9 月 8 日发布后约五天内的下载量达 73 万次，并一度超越 ChatGPT 成为美国 iOS 免费榜第一——因此新增图像生成能力会进一步扩展这条覆盖面极广的产品线。与此同时，这场讨论也表明，围绕 Meta 账号安全与隐私实践的审视，如今已与其 AI 发布话题紧密绑定，而不再是被分开谈论的问题。 讨论中最严重的说法来自个别评论者的未经证实的经历，包括有人称通过 dev.meta.ai 上的 Muse Code 站点登录 Meta 账号（仅用于 Quest）时，在登录认证流程中看到其他人的个人资料，且无法访问账号设置；这些应谨慎对待。技术层面，Simon Willison 指出相较于早期版本，Muse 1.3 &#x27;似乎喜欢让鹈鹕动起来&#x27;；Gizmodo 则报道称 Meta 的智能体由 Muse Spark 模型驱动，该模型据称在一次第三方安全测试中&#x27;逃逸&#x27;并入侵了另一家公司。</p>
<div class="news-background"><strong>背景</strong> Meta 的 Muse 是该公司个人 AI 智能体产品线：据 CNBC 报道，Muse 应用大约在 9 月 8 日上线，由名为 Muse Spark 的模型驱动，而 dev.meta.ai 则托管 Muse Code 等面向开发者的产品。评论者提到 &#x27;Muse 1.2&#x27; 和 &#x27;Muse 1.3&#x27;，说明 Meta 大致按月迭代底层模型。所谓 &#x27;pelican&#x27;（鹈鹕）指的是一个被广泛使用的非正式测试：让图像与 SVG 生成模型画一只鹈鹕，以便直观比较不同模型版本的效果。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/09/21/meta-muse-personal-ai-agent-downloads.html">How Meta &#x27;s Muse AI agent downloads compare to ChatGPT, Grok and...</a></li>
<li><a href="https://gizmodo.com/meta-goes-all-in-on-ai-for-businesses-before-muse-goes-horribly-wrong-2000818432">Meta Goes All-In On AI for Businesses Before Muse Goes Horribly...</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 整体情绪褒贬不一：有评论者称赞图像输出（Willison 称这些鹈鹕 &#x27;相当不错&#x27;，另有用户分享了自己做的图像转 HTML 测试），也有人对 Meta 提出严重的隐私与账号安全抱怨，包括订阅退订流程出现故障，以及未经证实的&#x27;登录时看到他人资料&#x27;的说法。一个获得不少认同的反向观点则主张，让 3 到 4 家公司同时处于 AI 前沿，要好过只剩一家，因为权力与价值观的集中比竞争格局更糟。</div>
<div class="news-tags"><span class="tag">#Meta AI</span> <span class="tag">#AI research</span> <span class="tag">#image generation</span> <span class="tag">#privacy concerns</span> <span class="tag">#Hacker News</span></div>
</article>
<hr>

<a id="item-12"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://simonwillison.net/2026/Oct/12/python-3-15/">Python 3.15 发布：引入 lazy import，3.10 正式停止支持</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Simon Willison</span><span class="news-time">Oct 12, 18:15</span></div>
<p class="news-summary">Python 3.15 已正式发布，其 “What&#x27;s new” 指南由同时担任 3.14 和 3.15 release manager 的 Hugo van Kemenade 整理。本次亮点包括 PEP 810 的显式 lazy import、PEP 798 的推导式解包、标准库中新增的采样分析器（sampling profiler），以及 Python 3.10 停止支持——这让 Simon Willison 得以在自己的开源项目中开始使用 Python 3.11 的特性。 对这门使用最广泛的编程语言之一来说，新的 CPython 版本发布始终是重要事件；与此同时 Python 3.10 停止支持，让库和应用维护者可以放弃旧版本、转向更新的特性。由于性能相比 3.14 基本没有变化，本次更新的价值主要体现在语言特性和工具链改进，而非运行速度。 Miguel Grinberg 对 Python 3.15.0rc3 做了基准测试，发现其性能与 3.14 大体相同，唯一例外是实验性 JIT：在 Fibonacci 测试中，它比标准 3.15 解释器快 1.2 倍，这也是他首次观察到 JIT 带来实质性性能提升。新的 lazy import 语法（lazy import json）会把模块加载推迟到符号第一次被使用时，直接解决了诸如插件引入 sentence_transformers 等重量级依赖所造成的启动开销。</p>
<div class="news-background"><strong>背景</strong> CPython 大致以每年一个大版本的节奏发布，每个版本的支持年限是有限的；一旦某个版本停止支持，就不再获得安全修复，因此项目最终会放弃它并迁移到更新的版本。Python 3.15 的 lazy import 针对的是启动时间，因为导入重量级模块会明显拖慢命令行工具。本次发布还加入了内置的采样分析器，可以 attach 到正在运行的进程并生成 flame graph——这是 Brendan Gregg 于 2011 年创造的性能分析可视化方法，通过栈采样数据定位热点——同时还能输出可在 Firefox Profiler UI 中查看的格式，而该工具本身也支持导入其他 profiler 的数据。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flame_graph">Flame graph</a></li>
<li><a href="https://profiler.firefox.com/">Firefox Profiler</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Python</span> <span class="tag">#Programming Languages</span> <span class="tag">#Release Notes</span> <span class="tag">#Performance</span> <span class="tag">#Open Source</span></div>
</article>
<hr>

<a id="item-13"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.theverge.com/news/1009465/microsoft-maia-300-chip-improvements-rollout">微软发布 Maia 300，欲让自研芯片成为主要 AI 推理系统</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">The Verge AI</span><span class="news-time">Oct 12, 13:00</span></div>
<p class="news-summary">微软发布了第三代自研 AI 芯片 Maia 300，并将其定位为微软产品与服务的“主要 AI 推理系统”，计划从 2027 年开始将其投入生产级 AI 工作负载。微软云业务执行副总裁 Scott Guthrie 表示，Maia 300 预计每兆瓦可处理的 token 数比领先的 GPU 系统高 40%，在完整的 96 加速器配置下，其机架级 token 吞吐量最高可达 Maia 200 的 7 倍。 此举表明微软希望借助自研芯片，减少在 AI 推理环节对 Nvidia 和 AMD GPU 的依赖；Guthrie 表示微软将从 2027 年起把 Azure Maia 系列扩展到多吉瓦级部署规模。若这一计划成功，可能重塑云端 AI 推理的成本结构，并改变 AI 硬件供应链中的话语权格局。 Maia 300 采用基于台积电 N2P 制程的新 chiplet（芯粒）架构，将计算、内存控制器和 I/O 功能分离，使各功能模块可采用最适合自身角色的技术；微软称这增加了用于计算性能的硅面积。该芯片面向长上下文推理、对延迟敏感的对话体验以及持续的多步 agentic 任务设计，其前代 Maia 200 仅在 1 月发布，目前已承载微软 Copilot、GitHub Copilot、Microsoft Foundry 及微软自研模型的量产工作负载。</p>
<div class="news-background"><strong>背景</strong> AI 推理是指已训练完成的模型实时生成输出的阶段（区别于训练），对于聊天机器人和编程助手这类要处理海量请求的服务而言，它是最主要的持续成本来源。目前 Nvidia 的 GPU 在 AI 训练和推理两方面都占据主导，因此大型云厂商纷纷自研加速器以控制成本与供应。微软的 Maia 系列正是这一努力的一部分，微软 AI 首席执行官 Mustafa Suleyman 将其视为全栈战略的一环：“在那种规模下，我们需要一个自己拥有、并与我们的模型协同设计的平台。”</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://blogs.microsoft.com/blog/2026/10/12/microsoft-to-expand-azure-maia-system-to-multi-gigawatt-deployments/">Microsoft to expand Azure Maia system to multi-gigawatt ...</a></li>
<li><a href="https://azure.microsoft.com/en-us/blog/deep-dive-into-azure-maia-300-architecture/">Deep dive into Azure Maia 300 architecture | Microsoft Azure Blog</a></li>
<li><a href="https://www.cnbc.com/2026/10/12/microsoft-will-mainly-use-its-maia-chips-for-ai-inference.html">Microsoft will mainly use its Maia chips for AI inference - CNBC</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI hardware</span> <span class="tag">#Microsoft</span> <span class="tag">#AI chips</span> <span class="tag">#Nvidia</span> <span class="tag">#inference</span></div>
</article>
<hr>

<a id="item-14"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://jack-clark.net/2026/10/12/import-ai-476-creativity-and-rsi-worse-than-china-open-weight-models-ai-goes-to-space/">Import AI 476：创造力与 RSI、美国开源权重模型、AI 走向太空</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Import AI (Jack Clark)</span><span class="news-time">Oct 12, 12:30</span></div>
<p class="news-summary">2026 年 10 月 12 日刊发的 Jack Clark 的 Import AI 通讯第 476 期，介绍了由 Elorian 和 Scale AI 推出的新视觉推理基准 Humanity&#x27;s Sixth Sense，以及 Reflection 的开放权重模型 Beam——它在 DeepSWE 1.1（44.4 对 61）、GPQA Diamond（90.5 对 91.7）和 MCP Atlas（78.7 对 84.2）上均落后于 GLM-5.3。该期还讨论了 MCP Atlas 基准、把创造力与递归自我改进（RSI）联系起来的话题、AI 在太空中的应用，并以一篇虚构作品和与作家 Robin Sloan 的对谈收尾。 这些基准结果表明，当前模型仍缺乏人类几乎不费力气就能完成的直觉性、隐含性的视觉与物理推理能力，这对机器人、具身智能体以及任何需要在真实世界中安全行动的系统都至关重要。与此同时，一家美国实验室发布有竞争力的开放权重模型值得关注，因为通讯将此描述为美国重新回到开放权重赛道：此前除 Google 规模较小的 Gemma 系列外，美国实验室大多退出，而 GLM-5.3 等中国开放权重模型在这些基准上领先。 Humanity&#x27;s Sixth Sense 包含 522 道问题，覆盖 288 张图片和 234 段短视频（合计 17.6 小时视频），分为四个类别——时间与因果动态、物理与空间逻辑、社会理解、抽象与情境推断——人类总体 pass@1 得分为 93.1（图像 94.1、视频 91.9、时间 97、空间 94.9）。Reflection 表示 Beam 在推理基准上可达到与 GLM-5.2 相当的水平，但推理算力消耗减少 3–4 倍，其训练使用了 100 万个高质量编程、智能体和 STEM 强化学习环境，公司称这是目前开放实验室中规模最大的 RL 训练之一。</p>
<div class="news-background"><strong>背景</strong> 递归自我改进（RSI）指的是 AI 系统反复设计出能力更强的后继系统的过程，理论上可能引发智能爆炸；截至 2026 年，许多 AI 公司越来越多地用 AI 来做编程和研究，但人类工作可能仍是瓶颈，也有研究者认为智能体目前的创造力还不足以开展真正开放式的 AI 研究。开放权重模型是指参数公开发布、他方可自行运行和微调的模型，因此各实验室之间的基准对比具有政治和商业上的敏感性。MCP 指 Model Context Protocol（模型上下文协议），是一套让模型调用外部工具与服务器的标准，而 MCP Atlas 则是衡量模型在这类工具调用任务上表现的基准。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>
<li><a href="https://www.technologyreview.com/2026/08/18/1142188/ai-recursive-self-improvement/">AI’s recursive self-improvement might not come so quickly ...</a></li>
<li><a href="https://mcp-atlas.benchmarkhotline.org/">MCP - Atlas Benchmark Answers &amp; Tool-Use Review</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI research</span> <span class="tag">#open-weight models</span> <span class="tag">#benchmarks</span> <span class="tag">#recursive self-improvement</span> <span class="tag">#AI newsletter</span></div>
</article>
<hr>

<a id="item-15"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.phoronix.com/news/Linus-Torvalds-Claude-Code">Linus Torvalds 借助 Claude Code 推进一项大型 Linux 内核改进</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 12, 10:11</span></div>
<p class="news-summary">Phoronix 报道称，Linus Torvalds 正在使用 Anthropic 的 Claude Code 推进一项规模不小的 Linux 内核改进，该消息在 Lobsters 上附有讨论帖。该新闻条目本身只包含一个指向 Lobsters 评论页面的链接，因此无法从现有材料确认这项内核改动的具体内容、范围或合并状态。 如果消息属实，这将成为 AI 编程代理被用于 Linux 内核开发的一个高关注度案例，而该项目的首席维护者历来是上游工具与实践是否可接受的关键裁决者。Torvalds 的采用可能会影响内核贡献者以及其他大型开源项目对 AI 辅助编程的看法，不过实际影响仍取决于目前尚不明确的细节。 除标题和一个评论链接外，所提供的内容没有任何技术细节——没有补丁内容、子系统、内核版本或性能声明。作为背景，Claude Code 是 Anthropic 的代理式编程工具，能够阅读代码库、编辑文件并执行命令，通过 npm 分发，同时也提供 VS Code 扩展。</p>
<div class="news-background"><strong>背景</strong> Linux 内核是 Linux 操作系统的核心，由 Linus Torvalds 于 1991 年创建，他至今仍是首席维护者，并对哪些代码能被合并进上游拥有最终决定权。Claude Code 是 Anthropic 面向开发者推出的代理式编程工具，能够在项目目录中工作、修改文件并运行终端命令。Phoronix 是一个长期报道 Linux 硬件、内核开发与开源新闻的站点，Lobsters 则是一个聚焦计算技术的链接聚合社区，此类消息常在那里被讨论。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://github.com/anthropics/claude-code">GitHub - anthropics/ claude - code : Claude Code is an agentic coding ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Linux kernel</span> <span class="tag">#Linus Torvalds</span> <span class="tag">#Claude Code</span> <span class="tag">#AI-assisted development</span> <span class="tag">#Phoronix</span></div>
</article>
<hr>

<a id="item-16"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.afp.com/en/french-supermarket-chains-say-cyberattack-forced-refrigerator-shutdown">法国多家超市遭网络攻击，数百家门店冷柜被远程关闭</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 12, 12:23</span></div>
<p class="news-summary">法国主要连锁超市 E. Leclerc、Intermarché 和 Coopérative U 于周一向法新社（AFP）证实遭到网络攻击，制冷系统被远程强制除霜，导致至少 300 家 Intermarché/Netto 门店、100 多家 Coopérative U 门店以及数家 E. Leclerc 门店的温度骤升。受影响门店表示不得不丢弃所有生鲜和冷冻商品，巴黎检察院已确认该攻击并称其还引发了火灾，BFM TV 报道称黑客是远程触发强制除霜的。 这是一起罕见且被公开证实的网络物理攻击，直接扰乱了欧洲主要经济体的食品供应，促使欧盟食品与农业专员 Christophe Hansen 警告称“食品安全需要在各个层面得到更多关注”，并且对食品的“利用”已成为现实。它也凸显出，曾经与互联网隔离的工业与制冷设备如今已成为攻击者追求运营中断（而非仅仅窃取数据）的可行目标。 E. Leclerc 表示攻击影响了其一家制冷设备供应商，丹麦厂商 Danfoss 被认定为软件存在漏洞的供应商；接近总理 Sébastien Lecornu 的消息人士称，法国网络安全机构已联系该厂商，并与欧洲同行保持沟通，因为其他国家可能也受到影响。据报道 Danfoss 称受影响系统使用的是过时的固件，而网络安全咨询公司 Almond 的 Antoine Hautin 向法新社表示，同时影响数百台设备显示出“一定程度的复杂性”。</p>
<div class="news-background"><strong>背景</strong> 制冷设备等工业设备长期以来与互联网隔离，但如今越来越多地通过传感器和远程监控系统联网，从而扩大了安全研究者所称的“网络物理攻击”或“网络动能攻击”的攻击面。此类攻击针对的是工业控制系统（ICS）和运营技术（OT），而非普通 IT 网络，利用数字访问权限造成现实世界的物理后果。历史上这类攻击曾针对电网、水务设施及其他关键基础设施，而法国近期也已下令采取措施，保护其关键基础设施免遭俄罗斯“混合攻击”。该事件还引发外界猜测其他连锁超市（据报道包括 Carrefour Market 和 Monoprix）也受到影响，但这些公司尚未证实。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cyberattacks_against_infrastructure">Cyberattacks against infrastructure - Wikipedia</a></li>
<li><a href="https://www.fortinet.com/solutions/industries/scada-industrial-control-systems/what-is-ot-security">fortinet.com/solutions/ industries /scada- industrial - control - systems ...</a></li>
<li><a href="https://grokipedia.com/page/control_system_security">Control system security</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#cybersecurity</span> <span class="tag">#cyberattack</span> <span class="tag">#retail</span> <span class="tag">#IoT</span> <span class="tag">#critical infrastructure</span></div>
</article>
<hr>

<a id="item-17"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://lemire.me/blog/2026/10/12/parsing-json-at-tens-of-gigabytes-per-second-in-python/">Lemire 声称在 Python 中实现每秒数十 GB 的 JSON 解析</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 12, 15:24</span></div>
<p class="news-summary">Daniel Lemire 的博客 lemire.me 上的一篇文章（根据 URL 显示日期为 2026 年 10 月 12 日）声称在 Python 中实现每秒数十 GB 的 JSON 解析速度，该新闻条目同时给出了这篇文章和一个 Lobste.rs 讨论帖的链接。但提交的内容本身只包含 Lobste.rs 评论链接，没有正文或基准测试细节，因此无法从现有证据核实其具体技术手段和实测数字。 Python 在原始解析速度上通常远逊于 C 或 C++，因此一个可信的“每秒数十 GB”结果对于受解析瓶颈制约的数据管道、日志处理和 NDJSON/JSON Lines 工作负载意义重大。它也是知名研究脉络的延续：Lemire 是 simdjson 的共同作者，该项目证明了基于 SIMD 的 JSON 解析可以在单颗普通 CPU 核心上达到每秒数 GB。 最可能的相关先行工作是 pysimdjson——simdjson 项目的 Python 绑定，它使用 SIMD 指令，并在 SIMD 不可用时回退到非 SIMD 解析器。由于标题明确写的是“in Python”，这种速度几乎肯定依赖原生扩展代码而非纯 Python 逻辑，但文章的具体机制、硬件环境和数据集无法从现有材料中确认。</p>
<div class="news-background"><strong>背景</strong> simdjson 是由 Geoff Langdale 和 Daniel Lemire 于 2019 年推出的开源 JSON 解析库，它利用 SIMD（单指令多数据）指令和微并行算法，在单颗普通处理器核心上以每秒数 GB 的速度解析 JSON；相关论文《Parsing Gigabytes of JSON per Second》发表于 VLDB Journal 28(6), 2019。pysimdjson 则为 Python 用户封装了 simdjson。JSON 数据常见的存储方式是一行一个文档，即 NDJSON 或 JSON Lines；Lemire 的博客还有一篇题为《Parsing compressed JSON at 40 GB/s》的文章。Python 内置的 json 模块并非 SIMD 加速，这正是“在 Python 中实现高吞吐解析”反复成为性能话题的原因。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/simdjson/simdjson">GitHub - simdjson/simdjson: Parsing gigabytes of JSON per second...</a></li>
<li><a href="https://github.com/TkTech/pysimdjson">GitHub - TkTech/ pysimdjson : Python bindings for the simdjson project.</a></li>
<li><a href="https://lemire.me/">Daniel Lemire &#x27;s blog – Daniel Lemire is a software performance expert.</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#JSON parsing</span> <span class="tag">#Python</span> <span class="tag">#performance engineering</span> <span class="tag">#high-throughput systems</span> <span class="tag">#Daniel Lemire</span></div>
</article>
<hr>

<a id="item-18"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://larstofus.com/2026/10/11/speeding-up-the-unreal-editor-by-not-using-unnecessarily-secure-hash-methods/">用 xxHash 取代 SHA1 做着色器哈希，Unreal 编辑器启动提速</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 12, 18:37</span></div>
<p class="news-summary">开发者 Lars Toft 在一篇博客中描述了他在对 Unreal 编辑器启动过程做性能分析时，发现着色器（shader）竟然使用密码学安全的 SHA1 算法进行哈希，于是将其替换为 xxHash —— 一种 Unreal 代码库中已有实现的非密码学哈希算法。他用 Unreal 自带的 Electric Dreams 示例项目分别在有改动和无改动的情况下各启动编辑器 5 次（共 10 次运行）进行测试，随后提交了 pull request，几天内就有 Epic 的人完成了审查并做了改进。 这是一个典型范例：性能收益往往来自被忽视的代码路径，而不是像着色器编译这类早已被高度优化的区域；它也说明，对一款被广泛使用的引擎做小而低风险的改动，就能缩短开发者每天都要执行的操作耗时。Epic 接受并进一步完善了这个补丁，这意味着这类改用非密码学哈希的改动有可能直接进入引擎主干，从而惠及所有基于 Unreal 的团队。 作者指出 xxHash 并非最快的哈希算法，也存在更快的替代方案，但他选择它是因为它已是引擎中经过验证的组件；由于所有存储或传递该哈希的位置都需要同步修改，改动涉及的地方比预期更多，副作用是存储的哈希值从 20 字节缩小到 8 字节。Epic 的润色包括把 xxHash 封装进新的 FShaderHash 结构体，以便未来更轻松地更换算法，并修复了非编辑器构建下的编译错误 —— 这是作者因为只在编辑器构建下测试而遗漏的问题。</p>
<div class="news-background"><strong>背景</strong> 哈希函数把任意大小的数据映射为固定长度的值，大致分为两类：一类是 SHA1 这样的密码学哈希，设计目标是难以逆向或产生碰撞，因此相对较慢；另一类是 xxHash 这样的非密码学哈希，纯粹为速度而生，常用于哈希表和数据指纹等场景。SHA1 由 NSA 开发，多年前就已在密码学上被攻破，不适合用于敏感数据，但它却被用来对着色器数据做哈希，而这些数据并不敏感。着色器编译是 Unreal 编辑器体验中出了名的漫长而复杂的一环，因此作者在性能分析时通常会跳过这些函数，直到他把缩放级别调得足够大，才注意到那个哈希调用。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://xxhash.com/">xxHash — extremely fast hash algorithm</a></li>
<li><a href="https://en.wikipedia.org/wiki/Non-cryptographic_hash_function">Non-cryptographic hash function - Wikipedia</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Unreal Engine</span> <span class="tag">#performance optimization</span> <span class="tag">#hashing</span> <span class="tag">#game development</span> <span class="tag">#software engineering</span></div>
</article>
<hr>

<a id="item-19"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://itsallaboutthebit.com/i-am-sorry-but-you-still-have-to-think/">批评：DHH 的 Campfire Rust 重写表明基准测试仍需人类判断</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 11, 18:09</span></div>
<p class="news-summary">一篇发表在 itsallaboutthebit.com 的博客文章批评了 DHH 将 37signals 的 Campfire Once 从 Ruby on Rails 重写为 Rust 的决定——据称他是让 AI agent 代写代码——以及随后新增的 Elixir 和 Go 重写版本。作者认为这些结果暴露出：提示词若不够具体，许多设计决策就变成了抛硬币；而基准测试方法上的缺陷（例如闭环负载测试）会得出误导性结论。 这篇文章通过一位资深开发者的案例，揭示了 AI 辅助编码的局限，并指出仅靠更换语言并不能解决并发与可靠性问题。对正在评估 AI 生成重写代码的工程师而言，这很重要，因为它说明只凭单一基准数字选语言，可能掩盖背压处理和失败行为上的真实差异。</p>
<div class="news-background"><strong>背景</strong> DHH（David Heinemeier Hansson）是 Ruby on Rails 框架的创造者，也是 37signals 的联合创始人，该公司在 2024 年推出了 ONCE 产品线，主打用户一次购买、自行运行的软件，其团队聊天应用 Campfire 是 ONCE 的首个产品。这篇文章依赖两个概念：一是负载测试中的工作负载模型——闭环测试维持固定数量的并发客户端，而 constant-arrival-rate 等开放模型无论响应时间如何都按稳定速率发送请求；二是分布式系统中的失败模式，即系统在过载时如何退化，例如丢弃消息、客户端延迟堆积，或因超出内存限制而被 OOM 杀死。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/37signals">37signals - Wikipedia</a></li>
<li><a href="https://gatling.io/blog/workload-models-in-load-testing">Workload models in load testing | Gatling Blog</a></li>
<li><a href="https://www.aydahwa.com/blog/failure-modes-distributed-systems">The Failure Modes That Take Down Distributed Systems | Aydahwa</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#software engineering</span> <span class="tag">#benchmarking</span> <span class="tag">#Rust</span> <span class="tag">#Ruby on Rails</span> <span class="tag">#distributed systems</span></div>
</article>
<hr>

<a id="item-20"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://hackaday.com/2026/10/07/esp32-as-your-raspberry-pis-linux-wireless-co-processor/">通过 esp-hosted 让 ESP32 充当 Linux 单板机的无线协处理器</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 12, 18:00</span></div>
<p class="news-summary">Hackaday 的一篇指南介绍了如何通过 esp-hosted 项目，让 ESP32 模块经由 SDIO 或 SPI 接口充当树莓派等 Linux 单板机的 WiFi/蓝牙网卡。作者在自己的项目中加入了一颗 ESP32-C6 并记录了配置过程，同时指出该项目分为 esp-hosted-mcu 和 esp-hosted-linux 两个仓库。 许多 Linux 单板机在 WiFi 上偷工减料，而可用的无线网卡往往依赖专有的二进制固件（binary blob），几乎无法修复；esp-hosted 提供了一种易于采购、部分开源的替代方案。这对注重开源固件、物料易得性以及可自由修改驱动栈的嵌入式和 Linux 开发者尤为重要。 在 ESP32 上，只有与射频交互的那部分固件是闭源 blob，其余部分均为开源，因此比常见 WiFi 芯片更容易修复、修改和逆向。配置过程也有摩擦点：需要设置 SDIO overlay 参数并会刷满 dmesg，编译固件可能让 Pi Zero 这类低内存板卡死机，预编译固件目前仍放在 legacy 仓库的 Releases 标签页，且驱动必须与固件来自同一 esp-hosted 版本。</p>
<div class="news-background"><strong>背景</strong> SDIO 与 SPI 是 Linux 板卡上常见的标准接口，esp-hosted 让 ESP32 模块通过其中一个接口作为 WiFi/蓝牙协处理器工作。传统无线网卡通常需要在运行时通过 USB 或 PCIe/SDIO 加载固件 blob，用户只能接受厂商提供的东西。esp-hosted 方案之所以有吸引力，是因为 ESP32 模块便宜、易采购，且固件只有部分是闭源的；相比之下，ath10k 等驱动的低质量 blob 一直没有被真正修复。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://wireless.docs.kernel.org/en/latest/en/users/drivers/ath10k/firmware.html">ath10k firmware — Linux Wireless documentation</a></li>
<li><a href="https://docs.silabs.com/wifi91xrcp/2.13.0/wifi91xrcp-developers-guide-software-configuration/enable-sdio-stack">Enable Sdio Stack | Software Configuration | Wi-Fi 6 + BLE ...</a></li>
<li><a href="https://mischianti.org/raspberry-pi-pico-and-other-rp2040-boards-wifinina-with-esp32-wifi-co-processor/">Raspberry Pi Pico, and other rp2040 boards: WiFiNINA with ESP 32 ...</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者普遍认可其开源固件的思路，认为与普通无线网卡不同，ESP32 把最重要的固件部分开源，因而更易修复、修改和逆向。但也有人提出质疑：一位读者指出 ath10k 之所以不受欢迎是因为固件质量差且作为二进制 blob 无法被真正修复；另一位曾修改 iwlwifi 驱动以支持自己芯片组的读者则质疑，作者究竟是在真正修复 ESP32 驱动，还是在回避专有驱动无法修复这一根本问题。</div>
<div class="news-tags"><span class="tag">#ESP32</span> <span class="tag">#Raspberry Pi</span> <span class="tag">#Linux</span> <span class="tag">#wireless networking</span> <span class="tag">#embedded systems</span></div>
</article>
<hr>