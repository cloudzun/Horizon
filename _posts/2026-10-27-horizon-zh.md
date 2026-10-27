---
layout: default
title: "Horizon 每日速递：2026-10-27"
date: 2026-10-27
lang: zh
---

> 📅 2026-10-27 · 从 72 条资讯中精选出 34 条重要内容

---

1. [TianoCore EDK II 高危 UEFI 漏洞波及全球大多数服务器](#item-1) <span class="score-badge score-high">9.0</span>
2. [DeepMind 发布 Genie 4 世界模型，原生支持音频](#item-2) <span class="score-badge score-mid">8.0</span>
3. [Ghostty 1\.4\.0 发布：完整实现 Kitty 图形协议并大幅提升性能](#item-3) <span class="score-badge score-mid">8.0</span>
4. [Tailscale 发布 Tailscale SSH 漏洞调查与修复更新](#item-4) <span class="score-badge score-mid">8.0</span>
5. [CPython 实验性 JIT 因 PEP 撤回而面临移除](#item-5) <span class="score-badge score-mid">8.0</span>
6. [Axiom Math 报告在 Lean 中形式化有限单群分类](#item-6) <span class="score-badge score-mid">8.0</span>
7. [维基百科的 WikiProject AI Cleanup 着手清理 AI 生成内容](#item-7) <span class="score-badge score-mid">8.0</span>
8. [斯坦福校报称 Anthropic 用盗版斯坦福教授著作训练 Claude](#item-8) <span class="score-badge score-mid">8.0</span>
9. [Project Zero 对比 BigSleep 与 Fuzzilli：LLM 在 V8 上发现更多漏洞](#item-9) <span class="score-badge score-mid">8.0</span>
10. [用纯 Java 实现 Haskell 风格的类型类实例解析](#item-10) <span class="score-badge score-mid">8.0</span>
11. [Go 发布首个 URGENT 安全版本，阻断被攻破的 eMudhra 证书](#item-11) <span class="score-badge score-mid">8.0</span>
12. [Survival LLM：可在个人电脑上离线运行的 AI 助手与应急资料库](#item-12) <span class="score-badge score-mid">7.0</span>
13. [Apple 发布搭载 M6 芯片的 14 英寸 MacBook Pro](#item-13) <span class="score-badge score-mid">7.0</span>
14. [Liquid AI 发布 LFM3：六个面向端侧的开源权重 2B 级多模态模型](#item-14) <span class="score-badge score-mid">7.0</span>
15. [美国政府被指隐瞒涉 Section 702 监控的秘密 FISA 法院裁决](#item-15) <span class="score-badge score-mid">7.0</span>
16. [Discord 将允许搜索引擎索引公开服务器消息](#item-16) <span class="score-badge score-mid">7.0</span>
17. [当 AI agent 写代码时，人类还需要懂什么](#item-17) <span class="score-badge score-mid">7.0</span>
18. [Liquid AI 发布 LFM3：六大 2B 级模型共享同一骨干](#item-18) <span class="score-badge score-mid">7.0</span>
19. [AI2 发布基准，检验 LLM 能否可靠评判研究想法的新颖性](#item-19) <span class="score-badge score-mid">7.0</span>
20. [Google 发布 Genie 4 世界模型，新增音频生成与实时提示编辑](#item-20) <span class="score-badge score-mid">7.0</span>
21. [数据中心反对浪潮成为美国中期选举的两党议题](#item-21) <span class="score-badge score-mid">7.0</span>
22. [OpenAI 宣称三项&quot;重大&quot;科学发现，并提出与学术界合作新范式](#item-22) <span class="score-badge score-mid">7.0</span>
23. [Anthropic IPO 文件暴露 AI 数据中心对天然气的依赖](#item-23) <span class="score-badge score-mid">7.0</span>
24. [Import AI 478：用数学做对齐、ProgramBench 与 Mirendil 的 RSI 实践](#item-24) <span class="score-badge score-mid">7.0</span>
25. [Astral 推出 tar\-codec：为 uv 打造更快更安全的 Rust tar 解析器](#item-25) <span class="score-badge score-mid">7.0</span>
26. [Syl 语言探索面向系统编程的编译期依赖类型](#item-26) <span class="score-badge score-mid">7.0</span>
27. [DJB 推出 Filian，将 Debian 软件包适配到内存安全的 Fil\-C 编译器](#item-27) <span class="score-badge score-mid">7.0</span>
28. [博主溯源：能在 Windows 11 上运行的最古老 GUI 程序](#item-28) <span class="score-badge score-mid">7.0</span>
29. [Tweedegolf 与 Microsoft 发布 Call Graph Analyzer，用于定位 Rust panic](#item-29) <span class="score-badge score-mid">7.0</span>
30. [针对常量除数的有符号 64 位向下取整除法新算法](#item-30) <span class="score-badge score-mid">7.0</span>
31. [Bill Cheswick 1992 年经典论文《An Evening with Berferd》再度引发关注](#item-31) <span class="score-badge score-mid">7.0</span>
32. [为什么大规模发送邮件的成本远超一次 TCP 连接](#item-32) <span class="score-badge score-mid">7.0</span>
33. [Stalwart v1\.0 发布：Rust 邮件服务器对标 Postfix 与 Dovecot](#item-33) <span class="score-badge score-mid">7.0</span>
34. [slughorn 以 C\+\+20 实现 Slug GPU 矢量图形渲染技术](#item-34) <span class="score-badge score-mid">7.0</span>

---

<a id="item-1"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://arstechnica.com/security/2026/10/code-execution-flaw-in-uefi-firmware-threatens-most-servers-on-planet-earth/">TianoCore EDK II 高危 UEFI 漏洞波及全球大多数服务器</a><span class="score-badge score-high">9.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Ars Technica AI</span><span class="news-time">Oct 27, 20:25</span></div>
<p class="news-summary">一个编号为 CVE-2026-97631、严重性评分 9.5/10 的内存破坏漏洞在 TianoCore EDK II 开源代码库中被披露，而大多数服务器厂商和数据中心都用该代码库构建 UEFI 启动固件。该漏洞由 Anthropic 的 Alex Matrosov 与 Google 的 Dan Holmes 发现，位于一个 ICMP 组件中，可让攻击者在操作系统以及 Secure Boot、TPM 等防御机制加载之前执行代码。 由于 EDK2 几乎是所有 UEFI 供应商（包括 AMI、Insyde 和 Phoenix）乃至微软加固版分支 Project Mu 所采用的事实参考实现，单个漏洞即可波及范围异常广泛的服务器与云基础设施。攻击者若能在如此早期的阶段执行代码，就能在 Secure Boot、TPM 度量与操作系统的可见范围之下植入其他恶意组件。 利用条件较为苛刻：系统必须启用 PXE 启动，攻击者必须在机器监听网卡 PXE 流量的数秒窗口内发起攻击，并且能够向其投递 ICMP 流量——而许多面向互联网的系统因前端服务或负载均衡器代为回应 ping 而不满足这一条件。以此方式投递的最终载荷不具备持久性、仅运行一次，但可为持久化植入打开通道；修复无需额外停机，因为固件补丁以 capsule 更新的形式在下次正常重启时生效。</p>
<div class="news-background"><strong>背景</strong> UEFI 是传统 BIOS 的现代替代方案，在机器上电后最先运行，负责初始化硬件并建立 Secure Boot 与可信平台模块（TPM）所依赖的信任链。TianoCore EDK II 是由 TianoCore 社区维护、采用 BSD 许可证的开源固件开发环境，是 UEFI 与 PI 规范的参考实现，因此硬件厂商和独立的 BIOS 供应商（IBV）都在其之上构建产品。PXE 启动是一项长期存在的机制，允许机器通过网络获取并启动操作系统镜像，在数据中心里广泛用于系统部署与安装。Capsule 更新是 UEFI 原生的固件镜像投递方式，由固件自身在重启过程中完成刷写。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/TianoCore_EDK_II">TianoCore EDK II</a></li>
<li><a href="https://blog.3mdeb.com/2024/2024-12-10-uefi-capsule-updates/">UEFI Update Capsules for Open Source firmware</a></li>
<li><a href="https://en.wikipedia.org/wiki/PXE_boot">PXE boot</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#security</span> <span class="tag">#UEFI</span> <span class="tag">#firmware</span> <span class="tag">#vulnerability</span> <span class="tag">#servers</span></div>
</article>
<hr>

<a id="item-2"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/">DeepMind 发布 Genie 4 世界模型，原生支持音频</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">acossta</span><span class="news-time">Oct 27, 16:06</span></div>
<p class="news-summary">Google DeepMind 发布了 Genie 4，这是其世界模拟模型的新一代版本，支持带原生音频的实时交互式模拟，并具备更先进的物理效果、自然的人体运动，以及由 Gemini 模型驱动的操控能力。根据 DeepMind 和 Google 博客的说法，Genie 4 建立在 Gemini 系列的能力之上，其中 Gemini Omni 负责将模拟锚定在真实世界外观上，该模型将很快向开发者和 Google AI Ultra 订阅用户推出。 像 Genie 4 这样的世界模型处在生成式视频与互动娱乐的交汇处，而 DeepMind 这次带音频和操控能力的重要发布，把“用提示词生成可玩环境”这一想法推进到更接近开发者可用的产品形态。该发布在社区引发大量审视（Hacker News 上 664 分、405 条评论），既说明关注度很高，也反映人们对这些演示的泛化能力存疑。 DeepMind 围绕实时交互、原生音频、先进物理和自然人體运动来介绍 Genie 4，但所给材料并未包含模型规模、延迟指标或授权条款等技术细节。社区测试者报告称，对于始终留在画面内的物体，一致性保持得很好，但当物体离开画面再返回时一致性就会失效；音频生成也可能与提示不符，例如在要求萨克斯时生成了单簧管的声音。</p>
<div class="news-background"><strong>背景</strong> “世界模型”是一种学习模拟环境及其动态的 AI 系统，用户可以描述或展示一个场景，然后与生成出来、持续演变的版本进行交互，而不是观看一段固定视频。DeepMind 的 Genie 系列是其中最知名的代表之一，Genie 4 接替了 Genie 3 等前代版本。这类模型通常会被拿来与 open-weights（开放权重，即训练后的参数公开发布）的替代方案比较，后者允许研究者和初创公司直接运行和修改模型——评论者正是以腾讯 HY-World 2.0 为例提出了这一对比。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/">Genie 4: A new generation of world simulation — Google DeepMind</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/google-deepmind/introducing-genie-4/">We’re announcing Genie 4, our new world model for real-time ...</a></li>
<li><a href="https://arstechnica.com/google/2026/10/deepminds-genie-4-world-model-adds-audio-and-more-realistic-people-to-simulations/">DeepMind unveils Genie 4 world model promising more realistic ...</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者对“世界模拟”的说法印象深刻但并不买账：有人指出当物体离开画面再返回时细节会发生变化——龙的那段演示里多出一座城堡、火车站台上走远的人群发生变化、香港骑摩托车的人先是没戴头盔后来又戴上了——认为这说明模型只是在画面内保持较强一致性，而非真正的世界模型。还有人指出音频不匹配（要萨克斯却给出单簧管），以及魔术棒把孔雀变成猫的示例在长提示反复强调写实的情况下仍显得像电子游戏；另有评论者认为腾讯开放权重的 HY-World 2.0 被低估，还有人贴出 Sam Altman 2024 年关于电影与电子游戏趋同的帖子。</div>
<div class="news-tags"><span class="tag">#world-models</span> <span class="tag">#generative-video</span> <span class="tag">#DeepMind</span> <span class="tag">#AI-research</span> <span class="tag">#model-releases</span></div>
</article>
<hr>

<a id="item-3"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://ghostty.org/docs/install/release-notes/1-4-0">Ghostty 1.4.0 发布：完整实现 Kitty 图形协议并大幅提升性能</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 27, 22:06</span></div>
<p class="news-summary">Ghostty 1.4.0 于 2026 年 10 月 27 日发布，历经七个月开发，包含来自 172 位贡献者的 2,889 次提交；该版本带来了大幅的性能与内存改进，并实现了项目所称的 100% 完整 Kitty 图形协议支持（包括动画与相对定位），成为首个达到该水平的非 Kitty 终端。此次发布还包括 SSH 集成改进、四项安全修复以及跨平台的大量其他改动。 完整符合 Kitty 图形协议意味着那些在终端中显示图像的应用现在可以把 Ghostty 当作 Kitty 的替代品，从而降低工具被绑定到单一模拟器上的动力。此次发布也凸显了 Ghostty 更宏观的策略：投入 libghostty 这一可嵌入的终端内核，维护者称其惠及整个终端生态，而不仅仅是一个 GUI 应用。 发布说明修复了四项安全公告，其中包括一个粘贴保护缺陷（GHSA-4hwh-wx3w-3fqg，未将回车视为行结束符），以及恶意 Kitty 图形命令（GHSA-mhff-mv4q-fp63）可能导致崩溃、挂起、强制大规模内存分配，甚至在有限情况下读取或删除允许临时目录之外的文件。资源限制也被加固：OSC 负载上限为 8 MiB，Kitty 图形负载上限为 65 MiB，每个单元格最多 64 个组合码点；项目还新增了对 Glyph Protocol（APC 25a1）的实验性解析（尚未渲染），并支持新的程序状态协议（OSC 7501），Ghostty 称这是其首创的首个终端规范。</p>
<div class="news-background"><strong>背景</strong> Ghostty 是由 Mitchell Hashimoto 创建的一款快速、功能丰富、跨平台的终端模拟器，采用平台原生 UI 与 GPU 加速，而非自绘界面。Kitty 图形协议是一种现代终端图形协议，通过 APC（Application Program Command）转义序列中的 base64 编码数据传输图像，使终端能够显示真实图片而不只是文本或 ASCII 艺术。libghostty 是该项目的可移植、零依赖核心库，以 C 和 Zig 编写，其他项目可用它构建终端模拟器或将终端功能嵌入自己的应用中。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://ghostty.org/">Ghostty</a></li>
<li><a href="https://github.com/ghostty-org/ghostty">GitHub - ghostty-org/ghostty: Ghostty is a fast, feature ...</a></li>
<li><a href="https://sw.kovidgoyal.net/kitty/graphics-protocol/">Terminal graphics protocol - kitty</a></li>
<li><a href="https://mitchellh.com/writing/libghostty-is-coming">Libghostty Is Coming – Mitchell Hashimoto</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 在 Hacker News 上，作者 Mitchell Hashimoto 借讨论串强调 libghostty 才是他真正的目标，认为一个免费、高质量、可复用的终端模拟内核比任何单一 GUI 应用对开发者更有价值。也有不少评论者提出异议或更多诉求：有人表示 Kitty 的 hints 模式是唯一阻止其切换到 Ghostty 的功能；有人指出 ⌘F/⌘V 查找框快捷键的缺陷仍未修复；还有人质疑为何要从 Konsole 或 iTerm2 迁移过来，称并未感受到明显的速度差异，并且更看重 tmux -CC 集成等具体功能。</div>
<div class="news-tags"><span class="tag">#terminal emulators</span> <span class="tag">#Ghostty</span> <span class="tag">#Kitty graphics protocol</span> <span class="tag">#open source releases</span> <span class="tag">#performance</span></div>
</article>
<hr>

<a id="item-4"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://tailscale.com/ssh-investigation-update">Tailscale 发布 Tailscale SSH 漏洞调查与修复更新</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">figmert</span><span class="news-time">Oct 27, 19:55</span></div>
<p class="news-summary">Tailscale 发布了一份针对 Tailscale SSH 漏洞的调查与修复更新，此前有研究员在补丁尚未广泛可用时公开披露了相关问题。据媒体报道，这次披露涉及 Tailscale 与 Headscale 的 11 个漏洞，而 Tailscale 正在准备一个客户端更新，用于修复 Tailscale SSH 中的权限提升弱点。 许多组织用 Tailscale SSH 在 tailnet 内管控谁能登录哪台机器，因此允许向 root 提升权限的漏洞会直接削弱那些依赖它、而非自管 SSH 密钥的团队的访问控制。该事件也助推了一个更广泛的讨论：网络层是否应该同时承担服务认证，因为这会把这些 VPN 与 SSH 访问集中到单一故障点上。 报道指出，最危险的攻击路径需要攻击者已拥有一台被授权的设备，具备相应权限，并启用了端口转发，而 Tailscale 据称并不建议所有人直接关闭 Tailscale SSH。在讨论中，一位前 Tailscale 员工将影响范围限定为：通过 Tailscale SSH（而非 OpenSSH）用 ACL 授权 SSH 进入某节点、且该用户没有通往 sudoers 或 root 的路径的场景；对没有 SSH 访问权限或无法连接到受影响节点的用户则不受影响。</p>
<div class="news-background"><strong>背景</strong> Tailscale 是基于 WireGuard 协议的 mesh VPN，它把组织内的设备与服务连接成一个名为 tailnet 的私有对等网络，并通过 ACL 定义访问规则。Tailscale SSH 是一项可选功能，让 Tailscale 负责该 tailnet 内 SSH 连接的身份认证与授权，从而省去分发和轮换 SSH 密钥、以及把 SSH 暴露在公网上的麻烦。Headscale 是另一个独立项目，是对兼容 Tailscale 的控制服务器的开源实现，此次披露中也提到了它。漏洞披露通常与厂商协调进行，以便在细节公开前完成修复；而非协调披露会压缩这一窗口，使防御方只能被动应对已公开的细节。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.securityweek.com/tailscale-rushes-patches-after-uncoordinated-disclosure-of-tailworm-flaws/">Tailscale Rushes Patches After Uncoordinated Disclosure of ...</a></li>
<li><a href="https://thehackernews.com/2026/10/unpatched-tailscale-ssh-flaws-could-let.html">Unpatched Tailscale SSH Flaws Could Let a Hacked Device Reach Root on ...</a></li>
<li><a href="https://tailscale.com/docs/features/tailscale-ssh">Tailscale SSH · Tailscale Docs</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 一位前 Tailscale 员工给出了最具体的范围界定，认为这些漏洞只有在 ACL 通过 Tailscale SSH 授予 SSH 访问、且用户没有通往 sudoers 或 root 的路径时才有意义；也有评论者表示，此事让他们更坚定地选择加固过的原生 OpenSSH 配合纯密钥认证，或在家庭实验室里改用纯 WireGuard。多位评论者反对让 Tailscale 同时承担 VPN 与 SSH 认证，认为这相当于单一故障点，风险与直接把 SSH 暴露在互联网上类似；还有人批评产品功能面不断扩大，并建议提供一种“锁定模式”来关闭 Taildrop、Taildrive、SSH、Funnel 等高风险功能。</div>
<div class="news-tags"><span class="tag">#security</span> <span class="tag">#tailscale</span> <span class="tag">#ssh</span> <span class="tag">#vulnerability-disclosure</span> <span class="tag">#networking</span></div>
</article>
<hr>

<a id="item-5"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://lwn.net/SubscriberLink/1102102/0c00e4d550f25f8c/">CPython 实验性 JIT 因 PEP 撤回而面临移除</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 27, 06:20</span></div>
<p class="news-summary">在历经数月讨论后，CPython 实验性即时编译（JIT）的维护者撤回了 PEP 836（&quot;JIT Go Brrr: The Path to a Supported JIT Compiler for CPython&quot;）；此前 Python 指导委员会在 6 月要求提交一份涵盖维护性、兼容性、成功指标与时间表的 PEP。Brett Cannon 确认相关工作将在主仓库停止，LWN 报道称该 JIT 很可能很快从 CPython 主分支中移除，以便在 Python 3.16 开发周期早期处理移除带来的问题。 该 JIT 是缩小 Python 性能差距最受关注的工作之一，其宣称的目标之一正是抵消 Python 3.13 引入的 free-threading 构建所带来的速度损失，因此移除它会降低外界对 CPython 自身性能路线图的近期预期。这同时为项目主分支能容忍多大程度的实验确立了先例，影响核心开发者以及那些押注 CPython 层面提速（而非第三方加速器）的人。 该 JIT 由 Brandt Bucher 于 2024 年初合入，用于 3.13 版本，事先并未经过标准跟踪 PEP 流程；指导委员会强调其审查重点并非决定 JIT 是否应成为受支持的特性，而是它是否应继续作为主分支中的实验，理由包括缺乏统一设计等。Cannon 表示在截止日期前提交替代 PEP 的可能性不大，因为所有积极推动该 JIT 的人都是被撤回 PEP 的作者或贡献者；LWN 还指出，目前仍不清楚最初的推动者是否打算在其他地方继续这项工作。</p>
<div class="news-background"><strong>背景</strong> CPython 是 Python 的参考实现，而即时编译器会在运行时把 Python 字节码翻译成机器码，希望让热点代码跑得比纯解释执行更快。Python 的演进通过 PEP（Python Enhancement Proposal）流程进行，这是一套书面设计文档机制，用于提出、评审和记录语言与流程变更，而指导委员会则是最终接受或否决这些提案的选举机构。free-threading 作为 Python 3.13 中的实验性构建引入，它禁用全局解释器锁（GIL），使线程可以在多核上并行运行，但会带来单线程性能损失。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://peps.python.org/pep-0001/">PEP 1 – PEP Purpose and Guidelines | peps . python .org</a></li>
<li><a href="https://docs.python.org/3/howto/free-threading-python.html">Python support for free threading — Python 3.15.2 documentation</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者总体持惋惜态度：一位长期关注该工作的网友表示，在指导委员会要求新 PEP 之前 JIT 进展非常快，并提到人们曾希望它能抵消 free-threading 的性能损失，但也承认那些越来越复杂的优化本身带来了疑问。有人追问为何 Ruby 和 JavaScript 都长期拥有 JIT 而 Python 的 JIT 尝试屡屡失败，猜测与基础解释器性能差异和资金投入有关；还有人建议采用基于装饰器的内联 Cython 作为务实替代方案。另一种观点则认为，虽然结果看起来像是官僚程序作祟，但严格遵循 PEP 流程恰恰是 Python 成为优秀语言的原因之一。</div>
<div class="news-tags"><span class="tag">#Python</span> <span class="tag">#CPython</span> <span class="tag">#JIT</span> <span class="tag">#performance</span> <span class="tag">#free-threading</span></div>
</article>
<hr>

<a id="item-6"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://cfsg.axiommath.ai/">Axiom Math 报告在 Lean 中形式化有限单群分类</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">pfdietz</span><span class="news-time">Oct 27, 16:29</span></div>
<p class="news-summary">Axiom Math 发布了一个项目页面，报告已在 Lean 中形式化有限单群分类（CFSG），这是数学中最庞大、最复杂的结果之一。现有证据仅包括页面标题和链接，因此无法在此独立核实该形式化的确切范围与完整性。 如果报告的范围属实，对 CFSG 进行机器校验将为这一原始证明分散在数万页文献、约百位作者手中的定理增加一层新的可信度。这也将成为检验 proof assistant 能否处理大型分类定理级别数学的重要案例。 现有证据无法说明 CFSG 的哪些部分已被形式化、是否覆盖全部 26 个 sporadic groups，或该工作是否依赖任何未证明的假设。原始分类证明主要发表于 1955 年至 2004 年间，散落在数百篇期刊文章中，因此完整的 Lean 形式化将是一项巨大的工程与数学工作。</p>
<div class="news-background"><strong>背景</strong> CFSG 指出，每个有限单群要么是循环群、交错群、Lie 型群，要么是 26 个 sporadic groups 之一。单群常被描述为有限群的“基本构件”，大致类似于整数中的素数。Lean 是一个基于依赖类型论的开源 proof assistant 和函数式编程语言，用于编写可由机器校验的数学证明。Autoformalization 则是将非形式化数学转换为 Lean 等形式系统中的形式化陈述与证明的相关任务。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Classification_of_finite_simple_groups">Classification of finite simple groups</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lean_theorem_prover">Lean theorem prover</a></li>
<li><a href="https://en.wikipedia.org/wiki/Autoformalization">Autoformalization</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者认为 auto-formalization 对 CFSG 很有价值，因为数学家过去曾以为分类已经完成，后来却发现遗漏的情形或 sporadic groups。有人遗憾形式化仍建立在集合论而非同伦论基础之上，也有人讨论前沿模型能否把所有数学教材转成 Lean。还有数学家称该分类令其不安，并附上了 Monster group 的链接。</div>
<div class="news-tags"><span class="tag">#Lean</span> <span class="tag">#formal verification</span> <span class="tag">#mathematics</span> <span class="tag">#group theory</span> <span class="tag">#autoformalization</span></div>
</article>
<hr>

<a id="item-7"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://spectrum.ieee.org/wikipedia-wikiproject-ai-writing-cleanup">维基百科的 WikiProject AI Cleanup 着手清理 AI 生成内容</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">rbanffy</span><span class="news-time">Oct 27, 11:08</span></div>
<p class="news-summary">IEEE Spectrum 发表了一篇关于维基百科 WikiProject AI Cleanup 的报道，这是一个由志愿者组成的协作项目，专门识别并清除维基百科中质量低劣的 AI 生成内容。该报道在 Hacker News 上获得约 429 分和 199 条评论，读者围绕 AI 文本难以辨识以及 AI 正被用于清理工作本身展开了讨论。 维基百科是网络上阅读量最大的参考资料之一，其社区如何处理机器生成文本，直接影响数百万读者所信赖的信息。这场讨论的影响也不限于维基百科：如何识别 AI 内容与如何用 AI 工具来做审核之间的矛盾，几乎适用于当下所有面对 LLM 生成内容的平台。 WikiProject AI Cleanup 是一个在维基百科站内组织的协作项目，设有参与者名单、待办事项清单以及指南与资源页面；清理工作通常先在 AI noticeboard（AINB）协调，同时也分散在整个维基上进行。项目指南强调这些内容只是建议，志愿者即便只凭常识、边做边向其他编辑学习也能顺利参与。</p>
<div class="news-background"><strong>背景</strong> 维基百科由志愿者撰写和维护，像 ClueBot NG 这样的老牌机器人早已自动处理回退明显破坏性编辑之类的任务。随着大语言模型普及，编辑们开始遇到带有明显 AI 特征的文章和编辑——编造的事实、错乱的格式、生硬的措辞——于是催生了专门的清理项目。可靠识别这类文本仍是一个开放的研究问题：检测方法从语言特征分析到水印技术都有，但没有一种是完全可靠的。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup">Wikipedia:WikiProject AI Cleanup - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup/Guide_and_resources">Wikipedia:WikiProject AI Cleanup/Guide and resources - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Wikipedia:Bots/Requests_for_approval/ClueBot_NG">Wikipedia : Bots /Requests for approval/ClueBot NG - Wikipedia</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者普遍对清理行动表示欢迎，有人还推荐了 Old School RuneScape 维基贡献者撰写的一篇类似文章。最引人注意的反面声音来自一位读者：他手动修正了明显低质量的 AI 编辑，却被维基百科自己的 AI 机器人立即回退，最终选择放弃；另有人则指出项目态度颇为微妙——AI 已不只是需要清理的问题，也成了清理工具的一部分。</div>
<div class="news-tags"><span class="tag">#wikipedia</span> <span class="tag">#ai-generated-content</span> <span class="tag">#content-moderation</span> <span class="tag">#llm</span> <span class="tag">#community</span></div>
</article>
<hr>

<a id="item-8"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://stanforddaily.com/2026/10/27/professors-books-pirated-to-train-claude/">斯坦福校报称 Anthropic 用盗版斯坦福教授著作训练 Claude</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">car</span><span class="news-time">Oct 27, 15:28</span></div>
<p class="news-summary">斯坦福校报（Stanford Daily）的一篇报道指称，Anthropic 使用了以非法途径获得的斯坦福大学教授著作副本来训练其 Claude 模型，这一指控被描述为涉及大型 AI 开发商的训练数据盗版争议。正如此前读者所讨论的，该文章的重点在于这些书籍的获取方式，而并未断言训练过程本身已被判定为违法。 这一指控正处在围绕“AI 公司能否用盗版书籍语料库训练模型”的日益扩大的争论之中，该争论已牵涉 Anthropic、Meta、OpenAI 和微软，并直接关系到作者与出版商的经济利益。对于一直以安全与伦理为定位的 Anthropic 而言，有关其训练数据来源的指控不仅涉及法律风险，也牵动其声誉。 Hacker News 上的评论者指出，该标题把两个不同问题混为一谈：一是据称非法的书籍获取与存储行为，二是用这些书籍进行训练是否合法，而据报道文章并未就此给出结论。讨论中还提到 Anthropic 此前就盗版书籍达成的 15 亿美元和解，评论者称此事被作为民事而非刑事问题处理。</p>
<div class="news-background"><strong>背景</strong> 像 Claude 这样的大语言模型是在海量文本语料上预训练的，这些语料历来包括 Books3 之类的书籍数据集——该数据集由约 19.6 万本书组成，取自盗版书库，并被多家 AI 开发商使用。这已引发作者团体对 Meta、OpenAI、微软和 Anthropic 等公司的诉讼与集体诉讼。根据搜索结果中引用的报道，一名联邦法官批准了 Anthropic 一项 15 亿美元的版权和解，将就盗版副本的使用向数千名作者支付每本书约 3000 美元。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.theatlantic.com/technology/archive/2023/09/books3-database-generative-ai-training-copyright-infringement/675363/">These 183,000 Books Are Fueling the Biggest Fight in ... AIAAIC - Books3 dataset Digital parasitism: The use of pirated books in AI training ... Judge approves a $1.5B Anthropic settlement over books used ... The Unbelievable Scale of AI’s Pirated-Books Problem</a></li>
<li><a href="https://authorsguild.org/news/meta-libgen-ai-training-book-heist-what-authors-need-to-know/">Meta&#x27;s Massive AI Training Book Heist: What Authors Need to ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude ( AI ) - Wikipedia</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 的评论者对 Anthropic 的行为以及双方的表述普遍持怀疑态度：有人将此案与因下载 JSTOR 文献而被起诉的 Aaron Swartz 相比较；有人虽然认为某位教授用“奴工”来形容过于夸张，但仍批评这种措辞；还有人认为标题应说明书籍是非法获取的，而非训练本身违法。多位评论者呼吁强制审计数据来源，并施加足以改变行业行为的重罚。</div>
<div class="news-tags"><span class="tag">#AI copyright</span> <span class="tag">#Anthropic</span> <span class="tag">#training data</span> <span class="tag">#book piracy</span> <span class="tag">#AI ethics</span></div>
</article>
<hr>

<a id="item-9"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://projectzero.google/2026/10/fuzzing-v-AI.html">Project Zero 对比 BigSleep 与 Fuzzilli：LLM 在 V8 上发现更多漏洞</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 27, 19:08</span></div>
<p class="news-summary">Google Project Zero 发布了 Fuzzilli（生成式 JavaScript 引擎模糊测试器）与 BigSleep（基于 LLM 的漏洞发现系统）在 Chrome V8 引擎上的对比结果。过去六个月中，BigSleep 报告了 45 个漏洞，Fuzzilli 报告了 37 个，两者在具体漏洞上的观测重叠率约为 25%。 这一结果是说明 LLM 智能体已能在 V8 这类经过大量模糊测试的目标上，以与专用模糊测试器相当甚至更高的速度发现安全漏洞的具体数据点。Project Zero 建议厂商同时运行模糊测试和智能体分析，这可能影响浏览器及软件安全团队的测试资源分配方式。 由于直接对比方法容易低估重叠率，Project Zero 针对 2023 年以来报告的漏洞进行了专门实验，估计理论重叠率约为 60%，这意味着许多漏洞仍然只能被其中一种方法发现。文章还分析了一个 V8 漏洞，涉及在 --ignition-elide-redundant-tdz-checks 标志下消除冗余的 temporal dead zone（TDZ）hole 检查；如果检查被错误移除，V8 内部的 the_hole 哨兵值可能泄漏。</p>
<div class="news-background"><strong>背景</strong> 模糊测试（fuzzing）是一种自动化测试技术，通过向软件输入大量生成或变异的输入来触发崩溃并发现漏洞；Fuzzilli 是一款面向 JavaScript 引擎的覆盖率引导模糊测试器，它使用名为 FuzzIL 的自定义中间语言变异程序，再将其翻译成 JavaScript。BigSleep 是 Google Project Zero 与 Google DeepMind 构建的智能体漏洞研究系统，利用大语言模型阅读和推理代码；它此前曾展示过发现真实 SQLite 漏洞的能力。V8 是 Chrome 的 JavaScript 引擎，其 temporal dead zone（TDZ）规则禁止在初始化前访问 let/const 变量，V8 使用特殊的 the_hole 哨兵值和运行时检查来执行这一规则。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/googleprojectzero/fuzzilli">GitHub - googleprojectzero/fuzzilli: A JavaScript Engine Fuzzer</a></li>
<li><a href="https://cloud.google.com/blog/products/identity-security/cloud-ciso-perspectives-our-big-sleep-agent-makes-big-leap">Cloud CISO Perspectives: Our Big Sleep agent ... - Google Cloud</a></li>
<li><a href="https://thehackernews.com/2024/11/googles-ai-tool-big-sleep-finds-zero.html">Google’s AI Tool Big Sleep Finds Zero-Day Vulnerability in ... Cloud CISO Perspectives: Our Big Sleep agent ... - Google Cloud From Naptime to Big Sleep: Using Large Language Models To ... Google’s AI Tool Big Sleep Uncovered Critical SQLite 0-Day ... Google uses large language model to discover real-world ... Google&#x27;s Big Sleep: From Concept to Vulnerability Discovery</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#fuzzing</span> <span class="tag">#LLM security</span> <span class="tag">#V8</span> <span class="tag">#vulnerability research</span> <span class="tag">#AI agents</span></div>
</article>
<hr>

<a id="item-10"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://garciat.com/posts/java-type-classes/">用纯 Java 实现 Haskell 风格的类型类实例解析</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 27, 10:11</span></div>
<p class="news-summary">garciat 的一篇技术博客（代码已以 GitHub 仓库 github.com/garciat/java-type-classes 发布）展示了如何完全用纯 Java 构建一个小型的 Haskell 风格类型类实例解析引擎，仅依赖反射、泛型类型元数据和一个小型一阶 unifier。该引擎可以自动解析类型类实例（包括 higher-kinded 实例），支持 overlapping 实例，并能针对任意嵌套的泛型类型（例如 Map&lt;String, List&lt;Optional&lt;Integer&gt;&gt;&gt;）推导出 witness。 它说明了 Java 在运行时究竟保留了多少类型层面的结构，以及在完全不改动语言的前提下能多接近类型级编程；这对从事类型系统、元编程和泛型库的 Java 实践者很有价值，也为 Haskell 程序员提供了一个有趣的对照。由于它只是实验而非正式发布，其价值主要在于展示了一种非平凡的技术方案，而不是直接用于生产环境。 作者明确说明该引擎并非为生产环境设计，实现依赖在静态方法上标注 @TypeClass 和 @TypeClass.Witness 来声明实例。重叠实例的处理方式是用基于 unification 的检查（例如 isSubstitutionInstance 比较实例返回类型）配合显式的 OVERLAPPING 声明来判定哪个更具体；而解析一个由 List 组成的 Map、其元素又是 Optional 时，需要递归实例化五个 witness 构造器，文中给出的调试日志展示了这一过程。</p>
<div class="news-background"><strong>背景</strong> Haskell 的类型类提供 ad-hoc 多态：函数可以针对 Show a 这样的约束编写，编译器再通过实例解析挑选具体实现，这一过程常被类比为逻辑编程中的 SLD 归结。Java 泛型的运作方式很不一样，尤其是大多数类型参数在运行时会被擦除，不过编译器会在 class 文件中记录泛型签名，反射可以读出来。Unification 是通过为变量寻找替换使两个项相等的算法；Robinson 提出的一阶版本有唯一的最一般解，是类型推断和逻辑编程的基础。而 higher-kinded 类型抽象的是类型构造器而非具体类型——Haskell 和 Scala 具备这一能力，Java 则没有直接支持，因此这个项目用编码技巧来近似实现。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Higher-kinded_type">Higher-kinded type</a></li>
<li><a href="https://en.wikipedia.org/wiki/Unification_(computer_science)">Unification (computer science) - Wikipedia</a></li>
<li><a href="https://www.baeldung.com/scala/higher-kinded-types">Higher-Kinded Types | Baeldung on Scala generics - What is a higher kinded type in Scala? - Stack ... Code sample Higher-kinded types - GitHub Pages Higher-Kinded Types in Depth - numberanalytics.com Higher-kinded types: the difference between giving up, and ... Mastering Higher-Kinded Types - numberanalytics.com</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Java</span> <span class="tag">#Haskell</span> <span class="tag">#type systems</span> <span class="tag">#metaprogramming</span> <span class="tag">#reflection</span></div>
</article>
<hr>

<a id="item-11"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://go.dev/blog/emudhra-incident">Go 发布首个 URGENT 安全版本，阻断被攻破的 eMudhra 证书</a><span class="score-badge score-mid">8.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 27, 00:31</span></div>
<p class="news-summary">10 月 19 日，Go 团队启动了紧急安全版本发布，在收到关于 eMudhra 签发证书遭遇严重公钥基础设施（PKI）失陷的通知后约七个半小时内就推出了针对性补丁。该补丁以 Go 史上首个 URGENT 轨道安全版本的形式发布，博客文章还说明了团队为何在运行时层面介入以及整个响应过程如何展开。 由于泄露的中间 CA 私钥可让攻击者在无需证明域名控制权的情况下，为任意域名签发可信 TLS 证书，因此任何进行 TLS 校验的 Go 应用都可能面临中间人攻击风险，且不受宿主操作系统信任存储的影响。这一事件还显示语言运行时正在承担“最后一道防线”的安全角色，并与更广泛的证书生态协同，这影响到每一位发布网络软件的 Go 开发者。 Mozilla 于 10 月 17 日将八个 eMudhra 中间证书（六个用于 TLS，两个用于代码签名）加入 OneCRL，从而在 Firefox 中实际屏蔽了它们；调查人员发现相关密钥强度极弱，私钥可在微秒级时间内被还原。Go 的博文公布了受影响中间证书的 SHA-256 指纹（例如 EM DV TLS CA - G3B 以及 G3C 系列 TLS 证书变体），而且响应并不限于 Go：Apple 的支持文档称自 2026 年 10 月 19 日起已屏蔽这些被攻破的证书，Python 3.14.10 也发布了紧急版本在其 ssl 模块中屏蔽这些密钥。</p>
<div class="news-background"><strong>背景</strong> TLS 的公网信任建立在层级结构之上：被操作系统、浏览器或语言运行时信任的根证书颁发机构（CA）为中间 CA 签名，中间 CA 再签发网站和代码使用的终端证书。因此中间 CA 的私钥极其敏感，因为持有者可以签发被客户端视为有效的证书；OneCRL 是 Mozilla 用于在 Firefox 范围内吊销此类中间证书的机制，无需等待常规的证书吊销检查。此次事件中，证书生成流程存在密码学缺陷，使密钥强度远低于应有水平，攻击者因而能够推导出私钥。正因如此，Go 团队选择在补丁版本中直接修补证书校验逻辑，而不是单纯依赖外部信任存储的更新。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://go.dev/blog/emudhra-incident">Our Response To The eMudhra... - The Go Programming Language</a></li>
<li><a href="https://blog.cloudflare.com/emudhra-certificate-compromise">8 eMudhra certificates are compromised. Here&#x27;s what you need ...</a></li>
<li><a href="https://unit42.paloaltonetworks.com/emudhra-certificate-compromise/">EMudhra Intermediate CA Certificates Compromised</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Go</span> <span class="tag">#security</span> <span class="tag">#PKI</span> <span class="tag">#incident-response</span> <span class="tag">#supply-chain-security</span></div>
</article>
<hr>

<a id="item-12"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.brangus.io/survival-llm">Survival LLM：可在个人电脑上离线运行的 AI 助手与应急资料库</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">Luc</span><span class="news-time">Oct 27, 19:55</span></div>
<p class="news-summary">一个名为 Survival LLM 的项目发布在 brangus.io 上，它将 AI 助手与一套应急参考资料库打包在一起，二者完全在一台普通消费级电脑上本地运行、无需联网，面向网络与基础设施中断的灾害场景。该项目在 Hacker News 上引发关注，获得 139 分和 88 条评论。 这个项目为本地 LLM 社区的一个更广泛问题提供了具体案例：当风险很高、又没有云端兜底时，运行在普通硬件上的小模型是否足够可靠。它引发的讨论把这一承诺与更简单、更轻量的替代方案放在一起权衡，对任何构建 offline-first 或边缘 AI 工具的人都有参考价值。 评论者引用了项目中的一张基准测试表：在内存 16–31 GB 的 Mac 或 PC 上运行 IBM Granite 8B 的配置，22 道题中答对了 14 道，批评者据此认为在普通消费级机器上它几乎一半情况会答错。讨论还提到了 Kiwix 式可搜索档案库以及 Project Nomad 等替代方案，核心的顾虑在于：纯档案库可能比基于 LLM 的界面更可靠、更轻量。</p>
<div class="news-background"><strong>背景</strong> 大语言模型可以用自然语言回答问题，但有时会产生“幻觉”，即输出流畅却在事实上缺乏依据的内容，这在要求准确性的领域是一个被广泛记录的可靠性问题。本地运行模型可以摆脱对云服务器和互联网的依赖，但消费级硬件限制了模型规模，而较小的模型通常准确度更低。这类应急准备项目通常会把本地模型与一个预存的参考资料语料库搭配使用，让助手有具体材料作为回答依据。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2510.06265v1">A Comprehensive Survey of Hallucination in Large Language ...</a></li>
<li><a href="https://www.emergentmind.com/topics/hallucination-in-large-language-models">LLM Hallucinations - emergentmind.com</a></li>
<li><a href="https://www.locize.com/blog/offline-first-apps">Offline-First Apps: Architecture, Frameworks &amp; Real Examples</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论情绪出现分化：一位经历过五级飓风的评论者表示，这样的工具本会是“一种恩赐”；另一些人则认为像 Kiwix 这样纯可搜索的档案库会更可靠、更轻量。一位支持者建议把 LLM 纯粹当作搜索技术使用——先字符串匹配，再语义检索，最后是搜索智能——而不是当作给出建议的顾问；还有人推荐 Project Nomad 作为可预配置、能搭配任意本地 LLM 或数据的替代方案。</div>
<div class="news-tags"><span class="tag">#local-llm</span> <span class="tag">#offline-first</span> <span class="tag">#disaster-preparedness</span> <span class="tag">#hallucination</span> <span class="tag">#edge-ai</span></div>
</article>
<hr>

<a id="item-13"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.apple.com/in/newsroom/2026/10/apple-introduces-the-new-14-inch-macbook-pro-with-m6/">Apple 发布搭载 M6 芯片的 14 英寸 MacBook Pro</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">beex</span><span class="news-time">Oct 27, 16:08</span></div>
<p class="news-summary">Apple 发布了搭载 M6 芯片的新款 14 英寸 MacBook Pro，并通过 Apple 的 N1 无线芯片增加 Wi-Fi 7 和 Bluetooth 6 支持，同时可驱动双路 4K 外接显示器，最高 165Hz。 对于考虑升级 MacBook Pro 的用户来说，这次发布很重要，因为它在新的芯片世代上更新了 Apple 的主流专业笔记本，同时也加剧了围绕芯片命名、升级价格和端侧 AI 宣传的长期讨论。 Apple 称 M6 是首款 2nm 芯片，配备 12 核 CPU、12 核 GPU 和双 16 核 Neural Engine；14 英寸机型的外接显示器支持从 144Hz 提升到双路 4K 165Hz，但所提供材料未包含价格和电池信息。</p>
<div class="news-background"><strong>背景</strong> Apple 的 M 系列芯片是基于 ARM 的 SoC，Apple 从 2020 年的 M1 开始将其用于 Mac，随后又为高端机型增加了 Pro、Max 和 Ultra 版本。M6 是新一代产品，Apple 将其宣传为 2nm 芯片，配备 12 核 CPU/GPU 和双 16 核 Neural Engine。Neural Engine 是 Apple 用于端侧机器学习的神经处理单元，而 Wi-Fi 7 和 Bluetooth 6 是更新的无线标准。评论区提到的 Asahi Linux 是一个为 Apple silicon Mac 提供 Linux 支持的项目。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/">Apple introduces M 6 and M5 Ultra for a big leap in... - Apple</a></li>
<li><a href="https://www.macrumors.com/2026/10/27/14-inch-macbook-pro-with-m6-chip/">Apple Announces New 14-Inch MacBook Pro With M 6 Chip</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apple_m1_chip">Apple m1 chip</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者强烈批评 Apple 的命名方式，认为在售的 M(n) Pro/Max 旁边同时提供基础版 M(n+1) 令人困惑；多人还关注升级成本，其中一位用户表示要尽量让 M1 Pro 撑到 M7 Pro/Max 上市。还有人提出用“AI Index”来验证离线 AI 设备宣传，有人称已把 M1 MacBook Air 换成 Asahi Linux 并更换电池以延长寿命，也有人希望 Mac 能更好地支持 AAA 游戏。</div>
<div class="news-tags"><span class="tag">#Apple</span> <span class="tag">#MacBook Pro</span> <span class="tag">#M6</span> <span class="tag">#hardware</span> <span class="tag">#Hacker News</span></div>
</article>
<hr>

<a id="item-14"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.liquid.ai/blog/lfm3">Liquid AI 发布 LFM3：六个面向端侧的开源权重 2B 级多模态模型</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">Philpax</span><span class="news-time">Oct 27, 17:04</span></div>
<p class="news-summary">Liquid AI 推出了新一代 Liquid Foundation Models——LFM3，这是一个基于同一共享骨干网络构建的开源权重模型家族，包含六个 2B 级模型，覆盖文本、视觉、音频、omni（全模态）以及决策任务。官方表示每个模型都可以在单张 GPU 上完成微调，并且设计目标是在设备端而非仅在云端快速运行。 此次发布把多模态能力压缩到体积小、可公开下载的形态，这对在笔记本电脑、AI PC 等边缘硬件上构建隐私敏感或低延迟应用的开发者意义重大。社区反应显示，已经在小规模本地数据标注与分诊场景中使用 Liquid 小模型的用户对此有切实兴趣。 根据 Liquid AI 的模型卡，在 32K 上下文下，LFM3-1.7B 在三类设备上的预填充速度至少快 2.5 倍、解码速度至少快 1.8 倍，且内存占用最低。讨论中的早期用户体验在工具链上褒贬不一：一位评论者在 Liquid playground 中发现视觉语言版本在纯文本提示上反而优于文本模型，但推测这是量化导致的；另一位则无法在 LM Studio 或 Rapid MLX 中加载 omni 与文本模型的 MLX 版本，报错为 safetensors 无法读取。</p>
<div class="news-background"><strong>背景</strong> Liquid AI 以构建 Liquid Foundation Models（LFM）为核心，这一系列模型面向端侧、边缘与云端部署，强调低延迟和硬件感知的执行方式。此前几代产品包括更小的视觉语言模型，例如提供约 450M 和 1.6B 两个规格、针对快速本地推理优化的 LFM2-VL。LFM3 延续了这一路线，把文本、视觉、音频、omni 和决策等变体统一到同一个 2B 级共享骨干上，开发者无需切换模型家族即可选择所需模态。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.liquid.ai/blog/lfm3">Introducing LFM3: Every Modality for Specialized Intelligence | Liquid AI</a></li>
<li><a href="https://www.marktechpost.com/2026/10/27/liquid-ai-lfm3-open-weight-2b-multimodal-models/">Liquid AI Releases LFM3: 6 Open-Weight 2B-Class Multimodal Models</a></li>
<li><a href="https://huggingface.co/LiquidAI/LFM3-1.7B">LiquidAI/ LFM 3 -1.7B · Hugging Face</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 上的整体情绪偏正面：一位评论者表示自己在 RTX A4500 上用 LFM 2.6 对邮件、消息和元数据进行标注，把它当作分诊层，把低置信度的条目升级给更大的模型处理，并期待换用 LFM3；另一位则称赞其一流的硬件支持和更便宜、更快的端侧处理。参与该版本发布的 samstevens 也在帖中表示愿意就本地模型与云端前沿模型的取舍回答问题。质疑主要集中在落地细节而非理念本身——包括在一个简单提示上给出的离奇答案（被归因于量化）以及在 LM Studio 和 Rapid MLX 中加载 MLX 版本失败。</div>
<div class="news-tags"><span class="tag">#local AI</span> <span class="tag">#multimodal models</span> <span class="tag">#on-device inference</span> <span class="tag">#Liquid AI</span> <span class="tag">#model release</span></div>
</article>
<hr>

<a id="item-15"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.wired.com/story/the-us-government-is-hiding-a-secret-court-ruling-about-how-it-spies-on-americans/">美国政府被指隐瞒涉 Section 702 监控的秘密 FISA 法院裁决</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">helterskelter2</span><span class="news-time">Oct 27, 14:06</span></div>
<p class="news-summary">Wired 报道称，两名美国参议员指认特朗普政府在推动国会续期 Section 702 监控项目的同时，隐瞒了一项与该项目相关的 FISA 法院裁决，并称此举违法。参议员 Ron Wyden 还警告存在一种对 Section 702 的机密解释，他表示多届政府都依赖该解释且拒绝将其解密。 这一争议直指美国人的通信在 Section 702 下如何被收集这一核心问题——该授权需由国会定期续期——以及立法者与公众能否在掌握完整信息的情况下对其加以评估。如果一项秘密法院解释实质上塑造了该项目的运作方式，那么隐瞒它就会限制续期辩论的范围，并加剧外界对监控基础设施监督不力的担忧，而这一基础设施正是加密与后门争论的根基。 报道的核心是政府尚未公布的一项 FISA 法院裁决；Wyden 曾表示，当相关的机密解释最终被解密时，美国人民会震惊于它竟拖了这么久，以及国会一直在信息不足的情况下辩论这项授权。文章将这项被隐瞒的裁决与政府推动国会续期 Section 702 的努力联系起来。</p>
<div class="news-background"><strong>背景</strong> Section 702 是《外国情报监视法》（FISA）的一部分，该 1978 年法律为在美国本土进行外国情报监视与收集设定了程序。2008 年的《FISA 修正案法》新增了 Section 702，允许收集美国境外人士的通信，并已成为重要的情报收集工具，但同时引发隐私担忧，因为美国人的通信可能被附带采集。对这些请求的监督由外国情报监视法院（FISC）负责，这是 FISA 设立的一个专门联邦法院，其程序基本保密，只公布有限的文件。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.wired.com/story/the-us-government-is-hiding-a-secret-court-ruling-about-how-it-spies-on-americans/">The US Government Is Hiding a Secret Court Ruling ... - WIRED</a></li>
<li><a href="https://en.wikipedia.org/wiki/United_States_Foreign_Intelligence_Surveillance_Court">United States Foreign Intelligence Surveillance Court - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Foreign_Intelligence_Surveillance_Act">Foreign Intelligence Surveillance Act - Wikipedia</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> Hacker News 的评论者总体持批评态度：有人引用 Wyden 的警告，并称监控美国公民是两党的共识点；也有人认为秘密法院与民主不相容，应当废除。若干评论者质疑美国自诩自由的形象与其国内监控规模之间的落差，还有人将此事与 Snowden、Lavabit 和国家安全信函（National Security Letters）等旧事联系起来，怀疑那些做法从未真正终止。</div>
<div class="news-tags"><span class="tag">#surveillance</span> <span class="tag">#privacy</span> <span class="tag">#section-702</span> <span class="tag">#civil-liberties</span> <span class="tag">#encryption</span></div>
</article>
<hr>

<a id="item-16"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://discord.com/blog/making-content-from-discoverable-servers-easier-to-discover">Discord 将允许搜索引擎索引公开服务器消息</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">DeepLogin</span><span class="news-time">Oct 27, 18:44</span></div>
<p class="news-summary">Discord 在一篇博客文章中宣布，「可发现服务器」（Discoverable Servers）公开频道中的消息将通过自动生成的公开 Server Web Page 被搜索引擎索引。多家媒体对该功能上线时间的报道集中在 2026 年底，具体日期从 11 月中旬到 12 月说法不一。 这一变化将大量社区讨论——问答帖、小众排障经验、模组与爱好者知识——从需要登录的平台释放到开放网络上，使其可被搜索和引用。它直接触及一个长期争论：Discord 取代传统论坛是否正在让可搜索的互联网变得碎片化。 索引范围仅限于可发现服务器，据媒体报道这类服务器需满足规模与活跃度门槛（据报道为至少 1,000 名成员）以及安全要求，同时管理员和用户都有选择退出的控制项。公告引发的一个关键未解问题是「追溯同意」：多年前由已不活跃成员发布的消息该如何处理。</p>
<div class="news-background"><strong>背景</strong> Discord 是一个以服务器（server）组织文本与语音频道的聊天平台，其内容历来大多位于登录墙之后，爬虫无法看到。它的 Server Discovery 功能会展示符合资格条件的公开社区，管理员需开启诸如「审核需双重验证」等设置才能继续留在列表中。要让这些内容可被索引，需要生成搜索引擎可抓取的页面；从技术上说，用 robots.txt 屏蔽爬虫与使用 noindex 指令并不等同——前者阻止抓取，但本身并不能把 URL 从搜索结果中移除。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/10/27/discord-is-making-its-public-communities-more-searchable-and-people-have-concerns/">Discord says it will let public-channel messages from servers ...</a></li>
<li><a href="https://www.dexerto.com/entertainment/discord-will-soon-let-anyone-find-public-server-messages-through-google-3422244/">Discord will soon let anyone find public server messages ...</a></li>
<li><a href="https://support.discord.com/hc/en-us/articles/360030843331-Enabling-Server-Discovery">Enabling Server Discovery – Discord</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者意见分歧但总体抱有期待：有人欢迎任何把内容拉出围墙花园的举措；一位服务器管理员表示会为新消息开启该功能，但担心如何告知那些过去发过言、如今已不活跃的成员。也有人批评规模与活跃度门槛，认为速通、ROM 改版等小众社区恰恰是受 Discord 登录要求影响最深的一群；还有人做出事实性纠正：文章从未提到 Google，网页搜索并不等于某一家公司。</div>
<div class="news-tags"><span class="tag">#discord</span> <span class="tag">#privacy</span> <span class="tag">#open-web</span> <span class="tag">#platform-policy</span> <span class="tag">#search-indexing</span></div>
</article>
<hr>

<a id="item-17"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://blog.adrq.dev/here-be-monsters-what-do-you-still-need-to-know-when-agents-do-the-work">当 AI agent 写代码时，人类还需要懂什么</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-hackernews">hackernews</span><span class="source-name">adrq</span><span class="news-time">Oct 27, 13:23</span></div>
<p class="news-summary">blog.adrq.dev 上的一篇题为《Here be monsters: What do you still need to know when agents do the work?》的博客文章，探讨了当 AI coding agent 接手实际编码工作后，人类仍然必须具备哪些技能和知识。该文在 Hacker News 上引发了规模可观的讨论（约 143 分、73 条评论），从业者结合自身经验进一步补充了关于系统级理解与 LLM 失效模式的看法。 随着基于 LLM 的 agent 承担越来越多多步骤的编码工作，工程师的角色正从逐行编写代码转向明确意图、审查产出并掌握整个系统的心智模型——这一变化会影响代码评审流程、新人上手方式以及团队如何划分责任归属。讨论还表明，这种转变并非全新事物：它与此前技术负责人在团队规模扩大到无法逐行阅读代码时所面对的情形如出一辙。 据称该博客在讨论期间一度无法访问（有评论者提到“Site is down”），因此可见的价值很大一部分来自评论区。评论者关注的是具体而非抽象的风险，包括有观点称 LLM 在数据库规范化决策上表现糟糕，以及有人认为开发者的不适感只是先行指标，真正的失败是产品故障、安全事故和宕机。</p>
<div class="news-background"><strong>背景</strong> AI coding agent 是由 LLM 驱动的工具，能够规划并执行多步骤的软件任务——读取文件、修改代码、运行测试——而不仅仅是补全一行代码。由于这类模型可能产出自信但错误的结果，从业者会关注已知的“失效模式”，例如虚构的文件路径、函数名或 API endpoint，以及工具误用。讨论中的核心概念“boxes and lines”式系统理解，指的是了解系统的各个组件及其交互方式，而不依赖任何单个实现细节。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/jaysonmulwa/reasoning-sentinels">jaysonmulwa/reasoning-sentinels: Reasoning audit skills for AI coding ...</a></li>
<li><a href="https://futureagi.com/glossary/failure-modes-in-ai/">What Are Failure Modes in AI ? FutureAGI Guide (2026)</a></li>
</ul>
</details>
<div class="news-discussion"><strong>社区讨论</strong> 评论者总体上认同文章前提，但提出了更锋利的补充：mrothroc 表示自己从一线工程师转为带团队后，学到的正是“理解系统”，即用 boxes-and-lines 和时序图来把握组件及其交互；trjordan 则对这一框架提出反驳，认为真正的失败是产品失败——用户愤怒、安全事故、宕机——而开发者的不适感只是先行指标。dgrcode 称赞了关于专家能融会贯通不同领域概念的表述，smallerfish 提醒 LLM 在规范化决策上表现糟糕，建议每隔几天暂停功能开发做代码与 schema 评审，LewisOrton 则质疑在模型能力持续扩张的情况下，“不可替代的人类价值”是否是一个稳定的定义目标。</div>
<div class="news-tags"><span class="tag">#AI agents</span> <span class="tag">#software engineering</span> <span class="tag">#LLM limitations</span> <span class="tag">#developer productivity</span> <span class="tag">#system design</span></div>
</article>
<hr>

<a id="item-18"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://huggingface.co/blog/LiquidAI/lfm3">Liquid AI 发布 LFM3：六大 2B 级模型共享同一骨干</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Hugging Face Blog</span><span class="news-time">Oct 27, 17:16</span></div>
<p class="news-summary">Liquid AI 发布了新一代 Liquid Foundation Models——LFM3，这是一个由六个开放权重、2B 级模型组成的家族（文本、视觉、音频、omni 与决策），全部从共享的 LFM3-1.7B-Base 检查点训练而来。此次发布包含公司首个 omni 模型、视觉模型的视频输入能力，以及一个视觉-语言-动作模型，所有模型权重均已在 Hugging Face 上公开。 通过让所有模态都保持在约 2B 参数规模并共用同一骨干，LFM3 降低了构建专用多模态系统的门槛：开发者可以在单张 GPU 上微调，并把模型部署到本地设备，而无需依赖大型云端模型。这也让 Liquid AI 的小模型路线在与其它面向边缘与 Agent 场景的紧凑型多模态模型竞争中更具辨识度。 Liquid AI 表示，新的 tri-hybrid 架构与训练配方使 LFM3-1.7B 在参数少 35% 的情况下超过了 LFM2.5-2.6B；文本模型在 4-bit 精度下约占用 1 GB，并支持 256K 上下文窗口。决策模型 LFM3-VL-2B 在 15 种本体（embodiment）上联合训练，报告称在四个 LIBERO 测试集上平均成功率为 96.2%，在 RoboCasa-GR1 桌面任务上为 45.7%，并在 Jetson AGX Orin 上以 TensorRT FP16 运行时可在 50 毫秒以内生成动作块。</p>
<div class="news-background"><strong>背景</strong> Liquid AI 源自 MIT CSAIL，其 Liquid Foundation Models 采用短卷积与注意力混合的架构，而非纯 Transformer 堆栈，目标是让模型在手机、笔记本等边缘硬件上快速推理。LFM2 已经确立了这种混合设计，而 LFM3 通过覆盖多种设备目标的硬件在环（hardware-in-the-loop）架构搜索对其重新设计。所谓 omni 模型，是指在单一统一架构中处理文本、图像、音频、视频等多种模态的模型；VLA（视觉-语言-动作）模型则把这一思路延伸到机器人控制，输出的不只是文本，还有动作。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.liquid.ai/blog/lfm3">Introducing LFM 3 : Every Modality for Specialized Intelligence | Liquid AI</a></li>
<li><a href="https://huggingface.co/LiquidAI">LiquidAI ( Liquid AI )</a></li>
<li><a href="https://www.marktechpost.com/2026/10/27/liquid-ai-lfm3-open-weight-2b-multimodal-models/">Liquid AI Releases LFM 3 : 6 Open-Weight 2B-Class... - MarkTechPost</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#multimodal</span> <span class="tag">#foundation-models</span> <span class="tag">#LFM3</span> <span class="tag">#Liquid AI</span> <span class="tag">#model-release</span></div>
</article>
<hr>

<a id="item-19"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://huggingface.co/blog/allenai/novelty-bench">AI2 发布基准，检验 LLM 能否可靠评判研究想法的新颖性</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Hugging Face Blog</span><span class="news-time">Oct 27, 16:12</span></div>
<p class="news-summary">Ai2 发布了《Old Ideas, Novel Problems》研究，并同时公开了配套的基准、数据和代码，用实证方法检验大语言模型评判科研想法新颖性的可靠程度。团队用 pointwise（绝对评分）和 pairwise（比较两个想法谁更新颖）两种形式评测了六个 LLM 评审——GPT-5.1、GPT-5.2、GPT-5.4、Claude Sonnet 4.5、Claude Opus 4.5 和 Claude Opus 4.6，并发布了可用于构建新评测集的自动化流水线。 像 Ai2 的 AutoDiscovery 和 Theorizer 这样的自动化想法生成系统，必须能区分真正新颖的方向与只是重新包装已有工作的想法，因此不可靠的新颖性评审可能动摇整个 AI 辅助科学发现的流程。评审结论会因提示词、推理预算或文献获取方式的细微变化而翻转，这对所有用 LLM 评审给研究想法打分、评审论文或筛选生成假设的人来说都是一个警示。 新颖性标签是从 ICLR 评审意见中自动挖掘的，只保留评审者明确就原创性达成一致的投稿（包括评审者认可其原创性的前 10% 论文），并与来自普通 LLM 生成器的低新颖性想法配对。作为额外校验，一位专家审阅了 30 组“人类 vs 生成”配对，样本偏向最强评审判错的案例，结果专家在全部 30 组中都更偏好人类想法，并认为没有一个生成想法具有新颖性；作者还把两组想法改写成统一结构，以检验评审是否只是在对写作风格做出反应，并指出许多核心结论并不依赖标签本身，而是依赖不同合理评测设置之间的相互矛盾。</p>
<div class="news-background"><strong>背景</strong> 随着 LLM 越来越多地被用作自动评估器——即所谓的“LLM-as-a-judge”模式——研究者开始把判断研究想法相对于已有文献是否新颖的任务交给它们。构建这样的“新颖性评审”并没有标准做法：团队要选择模型、提示词、评测形式（绝对评分还是比较配对）、推理预算，有时还要接入文献检索系统，而每一个选择都可能改变最终结论。同行评审由人类评审者判断原创性，通常被当作参照标准，这也是该基准从 ICLR 会议评审意见中挖掘标签的原因。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/allenai/novelty-bench">Can we trust LLMs to judge whether a research idea is novel?</a></li>
<li><a href="https://arxiv.org/pdf/2610.02022v1">Old Ideas, Novel Problems: The Instability of LLM-Based ...</a></li>
<li><a href="https://noy-sternlicht.github.io/Novelty-Evaluation-Web/">Old Ideas, Novel Problems: The Instability of LLM-Based ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#LLM evaluation</span> <span class="tag">#novelty assessment</span> <span class="tag">#benchmark</span> <span class="tag">#AI for science</span> <span class="tag">#research ideas</span></div>
</article>
<hr>

<a id="item-20"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.theverge.com/tech/1019076/google-genie-4-ai-model">Google 发布 Genie 4 世界模型，新增音频生成与实时提示编辑</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">The Verge AI</span><span class="news-time">Oct 27, 16:00</span></div>
<p class="news-summary">Google 宣布推出新一代世界模型 Genie 4，用于生成可交互的 AI 体验，共有四项主要更新：更逼真的世界、可通过自然语言提示实时修改体验、支持音频生成，以及底层使用 Gemini 3.8 Flash 辅助模拟。生成的体验时长也从上一代 Genie 3 的一分钟提升到约两分钟。 Google 将 Genie 4 定位为可用于影视预可视化、游戏创意原型以及机器人训练场景的工具，说明世界模型正从研究演示走向实际的内容制作与机器人工作流。该模型还将通过 Project Genie 面向 Google AI Ultra 订阅用户开放，表明 Google 希望让付费消费者而不只是研究人员接触到世界模型。 Google 提醒称，随着模拟时长增加，细节和物体恒存性（object permanence）可能随时间发生漂移；Genie 4 首先以仅面向“受信任测试者”的研究预览形式推出，The Verge 也表示自己未能亲自试用该模型。Google 称 Genie 4 “即将”向 Google AI Ultra 订阅用户开放，并已开启通过 Project Genie 体验的候补名单。</p>
<div class="news-background"><strong>背景</strong> 世界模型是一类机器学习系统，它会在内部构建环境的表征，并预测环境在动作作用下如何变化，可模拟物理、物体交互与因果等动态，而不只是做分类或生成输出。Google DeepMind 的 Genie 3 驱动着 Project Genie 这一早期研究原型，用户可以用图像、文本甚至 Google 街景作为提示来创建并探索可交互世界。被指为 Genie 4 底层引擎的 Gemini 3.8 Flash 属于 Gemini 的 Flash 系列模型，该系列主打速度与成本效率。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/world-models/">What Is a World Model? | NVIDIA Glossary</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie/">Project Genie: AI world model now available for Ultra users ...</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash">Gemini 3 . 8 Flash | Gemini API | Google AI for Developers</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Google Genie 4</span> <span class="tag">#world models</span> <span class="tag">#generative AI</span> <span class="tag">#interactive experiences</span> <span class="tag">#Gemini 3</span></div>
</article>
<hr>

<a id="item-21"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.theverge.com/policy/1019152/data-centers-midterm-elections">数据中心反对浪潮成为美国中期选举的两党议题</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">The Verge AI</span><span class="news-time">Oct 27, 10:00</span></div>
<p class="news-summary">在 2026 年美国中期选举中，宾夕法尼亚、俄亥俄、亚利桑那和艾奥瓦等州的候选人正纷纷与数据中心建设保持距离，提出成本回收规则、取消税收优惠、限制保密协议（NDA），部分人甚至主张全面暂停建设。与此同时，与 AI 相关的超级政治行动委员会在这些选战中投入巨资：由 Marc Andreessen 和 OpenAI 总裁 Greg Brockman 支持的 Leading the Future 一年内已花费 4500 万美元，Anthropic 支持的 Public First Action 称已募资 8000 万美元，新成立的 Tomorrow Together 则在摇摆选区众议院竞选中投放了 400 万美元广告，内容涉及数据中心开发与 AI 安全。 地方对数据中心的抵触正演变为能够左右选情的议题，这意味着围绕 AI 基础设施的政治环境——审批、税收减免、用水与用电要求——可能在单个城镇之外全面收紧。由于反对情绪跨越党派界线，并同时出现在国会选区和州长选战中，开发商以及依赖其算力供给的 AI 公司所面临的不只是地方 zoning 风险，而是上升的政治风险。 文章引用了昆尼皮亚克大学（Quinnipiac University）10 月初对宾夕法尼亚州可能投票选民的一项民调：64% 的受访者认为该州的 AI 数据中心弊大于利（误差范围为上下 3.9 个百分点），而在民主党受访者中这一比例高达 80%。候选人立场差异很大——有人支持不超过三年的暂停建设，有人主张取消税收优惠并要求数据中心自行承担成本，也有人明确反对暂停令；一份泄露的 NRSC（全国共和党参议院委员会）备忘录把数据中心形容为俄亥俄州参议院选战中“挂在 Husted 脖子上的锚”。</p>
<div class="news-background"><strong>背景</strong> 数据中心是容纳云服务与 AI 模型背后服务器的大型高耗能设施，当前的 AI 热潮推动了新一轮快速建设。社区居民往往反对，是因为这类设施消耗大量电力和水资源，可能推高当地公用事业成本，而且通常以在保密协议（NDA）下谈成的税收减免作为招商条件，条款并不公开。超级政治行动委员会（super PAC）是可以无限额募资和支出、用于支持或反对候选人的独立政治委员会，这也是为何有 AI 行业背景的团体在这些选战中成为显眼力量。</div>
<div class="news-tags"><span class="tag">#data centers</span> <span class="tag">#AI infrastructure</span> <span class="tag">#technology policy</span> <span class="tag">#elections</span> <span class="tag">#community opposition</span></div>
</article>
<hr>

<a id="item-22"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.theverge.com/ai-artificial-intelligence/1019143/openai-eth-kaseya-science-math-physics">OpenAI 宣称三项&quot;重大&quot;科学发现，并提出与学术界合作新范式</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">The Verge AI</span><span class="news-time">Oct 26, 23:34</span></div>
<p class="news-summary">在声称解决多个长期数学难题的数百篇手稿大规模发布后不到一个月，OpenAI 又宣布了三项自称&quot;重大&quot;的发现：每个维度下 local smoothing 猜想的证明（据称同时解决了 Kakeya 猜想与 Stein 限制性猜想）、通过一个在次指数时间内精确计数固定宽度 CNF 公式满足赋值的确定性算法来否定指数时间假设（ETH），以及四维中包含规范场与费米子的某些相互作用量子场论的严格存在性证明（含 QCD）。相关成果已发布到 GitHub，其中计算机科学证明由 Russell Impagliazzo、Ramamohan Paturi 和 Ryan Williams 负责审查，物理学部分则由 David Gross 领衔，成员包括 Michael Douglas、Arthur Jaffe、Igor Klebanov 和 Nikita Nekrasov。 这次公告的意义与其说在成果本身，不如说在流程：OpenAI 把自报的 AI 生成突破与具名外部&quot;引导者&quot;、Lean 形式化证明、问题筛选方式的披露以及对复核研究者的资助捆绑在一起，这可能为如何对待 AI 生成的研究主张树立规范。此事恰好紧随 OpenAI 自家 AGMAI 数学顾问组的建议——该小组建议 AI 公司不要给予特定人士优先获取此类成果的特权——因此真正具有影响力的部分是这套合作模式。 物理学成果尚未完整公开，仅被描述为四维中含规范场与费米子的理论的&quot;存在性证明&quot;；数学成果则以模型原始输出的形式直接发布，因为顾问建议让研究者自行给出解释，而不是先交给指定专家。OpenAI 还发布了一封公开信，就早期访问、对检查与解释成果者如何给予认可、以及如何支持学生等问题向社区征询意见；其 AGMAI 小组则把不平等获取、借用他人声誉和有偏选择列为反对&quot;优先访问指定&quot;做法的理由。</p>
<div class="news-background"><strong>背景</strong> Kakeya 猜想由挂谷宗一于 1917 年提出，问的是欧氏空间中一个在每一方向都含有单位线段的集合最小能有多小；据维基百科，该猜想在大于三维的情形仍未解决，而据本文报道，三维情形的证明前不久刚让纽约大学的王虹获得菲尔兹奖。Stein 限制性猜想是调和分析中的核心未解问题，研究函数傅里叶变换限制到曲面上的有界性；指数时间假设（ETH）则是被广泛使用的假定，认为 3-SAT 无法在次指数时间内求解。Lean 是一个证明助手，把定理编码后按公理级别进行机器检查，这正是&quot;Lean 形式化证明&quot;被提议作为让 AI 输出可独立验证的手段的原因。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kakeya_conjecture">Kakeya conjecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/Restriction_conjecture">Restriction conjecture - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant) - Wikipedia</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI for science</span> <span class="tag">#OpenAI</span> <span class="tag">#mathematics</span> <span class="tag">#research collaboration</span> <span class="tag">#formal verification</span></div>
</article>
<hr>

<a id="item-23"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.theverge.com/ai-artificial-intelligence/1018994/anthropic-ipo-ai-data-center-energy-climate-risk">Anthropic IPO 文件暴露 AI 数据中心对天然气的依赖</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">The Verge AI</span><span class="news-time">Oct 26, 21:45</span></div>
<p class="news-summary">在提交给美国证券交易委员会（SEC）的 S-1 文件中，Anthropic 承认其数据中心正越来越依赖天然气，部分规划中的站点将由现场燃气轮机供电。文件还把气候变化本身列为财务风险，警告气温上升将推高其服务器冷却所需的电力和水成本。 这一披露让 AI 行业日益增长的电力需求受到具体关注，而此时美国正计划进行十年来规模最大的化石燃料发电产能建设。它表明，AI 热潮的能源与气候代价已经大到足以被一家筹备上市的公司列为风险因素。 Anthropic 从超大规模云服务商处租用算力，但去年宣布了一项 500 亿美元的计划，在得克萨斯州和纽约州扩建数据中心；文件指出，燃气轮机短缺正迫使开发商在等待并网期间改用效率更低、污染更大的现场燃气发电设备。文件还警告，如果数据中心的用电需求被认为影响了其他电力用户，监管机构可能施加附加条件或备用容量费；而若无法确保电力供应，公司可能不得不推迟甚至放弃相关项目。</p>
<div class="news-background"><strong>背景</strong> S-1 是公司在首次公开募股（IPO）前向 SEC 提交的注册文件，必须披露对业务构成重大影响的风险。AI 数据中心需要消耗大量电力来训练和运行模型，为这些设施降温也需要大量水资源。在美国，公用事业公司和开发商正竞相增加发电产能，而燃烧天然气发电的燃气轮机供应紧张，这正是部分运营方转而采用现场发电、而非等待并网的原因。</div>
<div class="news-tags"><span class="tag">#AI infrastructure</span> <span class="tag">#data centers</span> <span class="tag">#energy</span> <span class="tag">#climate risk</span> <span class="tag">#Anthropic</span></div>
</article>
<hr>

<a id="item-24"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://jack-clark.net/2026/10/26/import-ai-478-math-for-alignment-programbench-and-mirendil-shows-what-rsi-means/">Import AI 478：用数学做对齐、ProgramBench 与 Mirendil 的 RSI 实践</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Import AI (Jack Clark)</span><span class="news-time">Oct 26, 12:31</span></div>
<p class="news-summary">Jack Clark 的 Import AI 第 478 期综述了三条线索：AI 安全初创公司 Resolution（前身为 Sequent）用“计划 + 编排 agent”的工作流（其中包含撰写 Lean 代码）自动形式化了与统计学习理论相关的数学内容，包括奇点消解（resolution of singularities）；用于评估编程 agent 的基准 ProgramBench；以及 Mirendil——据通讯所述，在该公司里单个人就能从零预训练出一个还不错的模型，展示了优化 AI 研发流程所能达到的效果。 这一期指向一种转变：AI 系统从“辅助研究”走向“执行多步骤研究计划”，这对安全研究（对学习理论背后的数学做形式化验证）和治理都很重要，因为递归自我改进正是实验室与政策制定者最为警惕的能力之一。 Resolution 的流程是：研究者先与 agent 一起制定两份计划——一份高层、人类可读的版本，以及一份 112 页、拆解为原子步骤的详细计划——随后由编排 agent 启动子 agent 分别做纸笔数学推导、撰写 Lean 代码以及检查进度，执行阶段除了计划和一些从既往内部形式化工作中蒸馏出的 agent 技能外几乎不需要额外脚手架。由于摘录并不完整，若干内容（例如文中出现的 &quot;$135k&quot; 成本数字，以及 OpenAI 关于前沿模型训练环境安全的文章）无法在此完整描述。</p>
<div class="news-background"><strong>背景</strong> Import AI 是 Jack Clark 长期撰写的周更通讯，面向技术读者总结 AI 论文、实验室动态与政策进展。自动形式化（autoformalization）指把非形式化的数学翻译成机器可检验的形式，通常使用 Lean 证明助手，使证明可以由软件验证而非人工审阅。递归自我改进（RSI）指 AI 系统能显著加速研发更好 AI 系统所需的研究，实验室既将其视为能力里程碑，也视为安全隐患。根据基准追踪网站的描述，ProgramBench 要求软件工程 agent 依据编译后的二进制文件和文档重建完整程序，并用隐藏的行为测试评分。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://benchmarklist.com/benchmarks/programbench/">ProgramBench Benchmark Scores &amp; AI Model... | BenchmarkList</a></li>
<li><a href="https://finance.biggo.com/news/03447e80-597e-4957-929e-456807f6e8cb">Ex-Anthropic Researchers Launch Mirendil, Raise $200M Seed ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#AI alignment</span> <span class="tag">#AI research</span> <span class="tag">#benchmarks</span> <span class="tag">#recursive self-improvement</span> <span class="tag">#newsletter</span></div>
</article>
<hr>

<a id="item-25"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://astral.sh/blog/tar-codec">Astral 推出 tar-codec：为 uv 打造更快更安全的 Rust tar 解析器</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 27, 16:59</span></div>
<p class="news-summary">从 0.131 版本开始，uv 改用 tar-codec 解析 Python 源码分发包（sdist），取代此前使用的 astral-tokio-tar。Astral 表示 tar-codec 的速度约为旧实现的两倍，同时降低了 uv 受到 parser differential 及其他安全风险的影响，并发布了一篇详细博客解释其设计。 uv 安装的每个 sdist 都要经过一个处理不可信字节的 tar 解析器，因此让这条路径既更快又更严格，能直接提升安装性能并缩小这一广泛使用的 Python 打包工具的攻击面。博客中关于 parser differential 的讨论，对其他需要解析不可信来源归档格式的 Rust 项目同样有参考价值。 tar-codec 以一个“分类”阶段开头，根据第一个 block 的 magic 和版本号，把后续解析锁定在单一格式家族（UStar/pax 或 GNU）上，目的正是降低 differential 风险。它默认拒绝 SCHILY.xattr.* 这类 pax vendor record（也提供跳过选项），提取环节则依赖 cap-std——在缺少 openat2 RESOLVE_BENEATH 语义的系统上，其系统调用次数会随路径深度线性增长。</p>
<div class="news-background"><strong>背景</strong> tar 归档是头部与文件内容依次排列的序列，其格式存在许多方言——V7、UStar、pax 和 GNU 扩展——它们在一些边界情形上的解释并不一致，甚至可以层层叠加。Python 的源码分发包（sdist）本质上就是 tar 归档，而 wheel 本质上则是 ZIP 归档，因此 Astral 用 Rust 编写的 Python 包管理器 uv 必须安全地解包 sdist。所谓 parser differential，是指两个组件对同一段字节做出不同解释，可能让恶意归档中的条目绕过校验器；公开漏洞记录中就描述了 astral-tokio-tar 的此类问题（CVE-2026-32766，0.5.6 及更早版本会静默跳过畸形的 PAX 扩展）以及 tar-rs crate 的 CVE-2026-33055。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.sentinelone.com/vulnerability-database/cve-2026-32766/">CVE-2026-32766: astral - tokio - tar Parser Vulnerability</a></li>
<li><a href="https://iterasec.com/blog/understanding-parser-differential-vulnerabilities/">Parser Differential Vulnerabilities Explained | Iterasec</a></li>
<li><a href="https://github.com/sunfishcode/cap-std">GitHub - sunfishcode/cap-std: Capability-oriented version of ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Rust</span> <span class="tag">#tar</span> <span class="tag">#parsing</span> <span class="tag">#security</span> <span class="tag">#uv</span></div>
</article>
<hr>

<a id="item-26"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://thenumb.at/Syl-Intro/">Syl 语言探索面向系统编程的编译期依赖类型</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 27, 14:40</span></div>
<p class="news-summary">一篇新的技术文章以作者正在开发的 Syl 语言为载体，阐述了如何把编译期依赖类型引入系统编程。Syl 用模态类型系统来编码编译期计算，每个值都带有一个沿两条轴定义的 mode——静态性（static / dynamic）与擦除性（erased / unerased），其主要灵感来自 András Kovács 的两层类型论（two-level type theory）以及对 OxCaml 的规划。 主流系统语言其实已经提供编译期计算能力——C++ 的 templates 与 constexpr、Rust 的 const generics、Zig 的 comptime，甚至 C 的 _Generic——但文章认为这些特性往往限制重重、缺乏真正的类型系统，或两者兼有。如果这种模态化的表述方式可行，就能让系统程序员在不牺牲可预测运行时行为的前提下获得类型级保证，这对编译器开发者、语言设计者以及关注底层性能的工程师都具有意义。 Syl 的 mode 之间存在子模态（sub-moding）关系：static 值可以弱化为 dynamic，unerased 值可以弱化为 erased，但标注不能反过来“加强”mode，因此 `let x = 0 @ static unerased;;` 合法，而忘记静态性是单向的。文章用一个带类型的解释器作为示例，其表达式类型本身就是一个以 sort 为参数的递归函数，并通过 `match erased` 在编译期解析被匹配项；作者同时指出 Syl 目前还没有等式类型（equality types），并计划用 mode polymorphism 取代 staticity 的模态公理 K 所依赖的隐式应用规则。</p>
<div class="news-background"><strong>背景</strong> 依赖类型允许类型引用普通的值——最经典的例子是由长度索引的向量类型，长度检查因此发生在编译期。这一思想的推广形式已出现在主流函数式语言中，即 GADT（广义代数数据类型），它让数据类型的每个构造子细化类型索引，而常见的演示正是 Syl 文章所使用的那种带类型解释器。擦除（erasure）则是与之互补的技巧：把索引值标记为仅存在于编译期，使其不产生运行时表示，这正是让依赖类型可用于性能敏感代码的关键。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Generalized_algebraic_data_type">Generalized algebraic data type - Wikipedia</a></li>
<li><a href="https://jadon.io/blog/erasable-dependent-types/">Erasable Dependent Types</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#dependent types</span> <span class="tag">#programming languages</span> <span class="tag">#compile-time</span> <span class="tag">#systems programming</span> <span class="tag">#Syl</span></div>
</article>
<hr>

<a id="item-27"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://cr.yp.to/2025/fil-c.html">DJB 推出 Filian，将 Debian 软件包适配到内存安全的 Fil-C 编译器</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 27, 16:42</span></div>
<p class="news-summary">Daniel J. Bernstein（djb）在 cr.yp.to 上发布笔记，记录了用内存安全 C/C++ 编译器 Fil-C 编译并运行 Debian 库和应用程序的经验，并介绍了 Filian 项目——它自动把 Debian 软件包适配到 Fil-C。在 Debian 13 系统上，Filian 会下载、编译并安装 Fil-C，然后获取选定的 Debian 源码包，用 Fil-C 编译并安装。 如果一位知名系统程序员能在源码基本不改动的前提下，用内存安全编译器重建主流发行版的相当一部分软件，就说明内存安全可以渐进式引入，而不必重写代码。这对发行版、软件包维护者以及所有在权衡加固 C/C++ 基础设施以防范内存安全漏洞的实际成本的人都有意义。 Bernstein 表示，在 Zen 4 单核上运行的近 9000 个密码学微基准测试中，Fil-C 编译的代码通常比 clang 编译的代码多花 1 到 4 倍的周期。Filian 沿用 Debian 的多架构模型，提出 amd64fil0 ABI，使 Fil-C 构建可与常规 amd64 构建共存；Bernstein 也提到一些粗糙之处，例如与 binNMU（+b）软件包的版本不匹配，以及 readline 需要手动创建 include 路径符号链接，而 Filian 计划消除这些麻烦。</p>
<div class="news-background"><strong>背景</strong> Fil-C 是 C 和 C++ 的一种内存安全实现，目标是高度兼容现有代码，把内存安全错误作为 panic 捕获，而不需要重写程序。Debian 软件包通过标准化的元数据和构建规则从源码构建，这正是能够用另一种编译器自动重建的前提。以 qmail、djbdns 和 NaCl 闻名的 Bernstein 表示，这项工作的私心是把管理的机器切换到 Fil-C 编译的代码以保护它们；他还提到 Mikael Brockman 的 Filnix，一个把 Nix 软件包适配到 Fil-C 的相关项目。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://cr.yp.to/2025/fil-c.html">Notes by djb on using Fil-C (2025)</a></li>
<li><a href="https://fil-c.org/">Fil-C</a></li>
<li><a href="https://github.com/pizlonator/fil-c">GitHub - pizlonator/fil-c: Fil-C: completely compatible ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#memory-safety</span> <span class="tag">#Fil-C</span> <span class="tag">#Debian</span> <span class="tag">#C/C++</span> <span class="tag">#compilers</span></div>
</article>
<hr>

<a id="item-28"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://blog.enlyth.com/posts/oldest-windows-gui-app-win-11/">博主溯源：能在 Windows 11 上运行的最古老 GUI 程序</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 26, 19:49</span></div>
<p class="news-summary">在 enlyth.com 的一篇博文中，作者寻找能在 Windows 11 上不经修改、不靠模拟即可运行的最古老 GUI 程序：先展示了来自早期 Win32s 版本、日期为 1993 年 2 月 22 日的 FREECELL.EXE，随后又挖出更早的 CDPLAYER.EXE（来自 NT 3.1 Build 347，链接时间为 1992 年 11 月 16 日）。作为作者自称的“作弊”手段，他还借助 otvdm（WineVDM）16 位兼容层，跑起了取自 Windows 1.01、日期为 1985 年 11 月 15 日的 REVERSI.EXE，并且可以完整游玩。 这篇博文用实测检验了 Windows 向后兼容性到底能延伸多远，证明上世纪 90 年代初的二进制程序在今天的 Windows 11 上仍能执行。它的价值主要体现在“软件考古”层面：文中记录了可执行文件格式与调用约定变更等具体坑点，解释了为何某些早期 NT 时代程序能幸存而另一些不能，同时凸显了 otvdm 这类社区工具如何填补微软放弃 16 位支持后留下的空白。 由于 64 位 Windows 已不再包含 NTVDM，16 位 Windows 程序无法原生运行，这就把搜寻范围推向了早期 NT 时代。作者发现 1991 年前后的 NT 预发布版使用了与现代 Windows 不兼容的 PE 草案格式，而直到 1992 年中的构建仍假设使用 cdecl 调用约定而非 stdcall，导致 API 参数被从栈上清理两次而崩溃；CDPLAYER.EXE 之所以能存活，是因为它链接系统的 crtdll.dll，而 Windows 11 的 SysWOW64 中仍提供该 DLL，此外还需要一个小型 cdemu.dll 来伪造 CD-ROM 驱动器才能播放音频。</p>
<div class="news-background"><strong>背景</strong> Windows 一向以能运行非常古老的软件著称，但这种兼容性有边界：64 位版本的 Windows 取消了 NTVDM（NT 虚拟 DOS 机），也就是让系统执行 16 位 Windows 与 DOS 程序的组件。Win32s 是 1990 年代初期的一个附加组件，使 32 位应用可以运行在 16 位 Windows 3.x 之上，随它分发的程序正是早期 32 位二进制文件的来源之一。另外两个概念也很关键：一是 x86 调用约定，如 cdecl 与 stdcall，二者的区别在于由调用方还是被调用方从栈上清除参数；二是 otvdm（又称 WineVDM），这是一个源自 Wine 的社区兼容层，可让 64 位 Windows 运行 16 位应用。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Wine_(software)">Wine (software) - Wikipedia</a></li>
<li><a href="https://learn.microsoft.com/en-us/cpp/cpp/cdecl?view=msvc-170">__cdecl | Microsoft Learn 1.17 - Calling Conventions (Windows) - offsecdiaries.com x86 Disassembly/Calling Conventions - Wikibooks Calling conventions (System V, cdecl) | Computer Internals Unmanaged calling conventions - .NET | Microsoft Learn GitHub - HBelusca/NTPEConv: Converts executable images from ...</a></li>
<li><a href="https://archive.org/details/windows-1.01-1985">Microsoft Windows 1.01 (1985) : Microsoft : Free Download ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Windows compatibility</span> <span class="tag">#software archaeology</span> <span class="tag">#legacy software</span> <span class="tag">#GUI</span> <span class="tag">#reverse engineering</span></div>
</article>
<hr>

<a id="item-29"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://tweedegolf.nl/en/blog/242/finding-panics-with-call-graph-analyzer/">Tweedegolf 与 Microsoft 发布 Call Graph Analyzer，用于定位 Rust panic</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 27, 16:45</span></div>
<p class="news-summary">在 Open Device Partnership 框架下并与 Microsoft 合作，Tweedegolf 发布了 Call Graph Analyzer（CGA），该工具从单态化后的 MIR 中提取调用图，并据此追踪编译产物中哪些函数可能 panic。运行 `cargo cga check` 会直接报告有问题的调用，例如指出对 `core::num::&lt;impl u64&gt;::strict_sub` 的调用可能 panic。 该工具瞄准了 Rust 开发者常问的问题——如何消除 panic，并声称即使代码不使用 `unwrap` 也能找出 panic 路径，这对嵌入式、安全关键以及要求“零 panic”的代码库意义重大。它还展示了一条可行的 Rust 静态分析路线：通过编译器外部的 rustc-driver 访问编译器状态。 CGA 只对带入口点的 crate 有效——即含 `fn main` 的二进制 crate，以及包含 `no_mangle` 或 `export_name` 导出符号的库 crate（包括嵌入式 Rust 的中断处理函数）——并且依赖 build-std。使用 CGA 编译大约比 `cargo check` 慢 2x–3x，作者建议使用 `opt-level=2`，因为在该级别下一般不会漏掉可达的 panic，从而减少误报且不产生漏报；部分项目会因其 `build.rs` 预期使用原生 rustc 而非 rustc-driver 而无法运行。</p>
<div class="news-background"><strong>背景</strong> MIR（Mid-level IR）是 rustc 位于源码与 LLVM IR 之间的中层中间表示，借用检查与许多优化都在这一层进行。单态化（monomorphization）是把泛型代码针对具体类型展开的过程，只有展开之后，完整的函数间调用关系才会显现出来。调用图把这些调用关系表示为图，因此工具可以从程序入口点出发，判断哪些函数可达、其中哪些可能 panic。CGA 以 rustc-driver 形式运行，这与 Clippy 等工具从编译器外部访问编译器状态的机制相同；该工作深受 Ferrocene（面向安全关键系统、通过 TÜV SÜD 认证的 Rust 工具链）的启发。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/OpenDevicePartnership/cga">Call Graph Analyzer (CGA) - GitHub</a></li>
<li><a href="https://rustc-dev-guide.rust-lang.org/mir/index.html">The MIR (Mid-level IR) - Rust Compiler Development Guide</a></li>
<li><a href="https://ferrocene.dev/">Ferrocene | Safety-Qualified Rust Toolchain for Critical Systems</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#Rust</span> <span class="tag">#static analysis</span> <span class="tag">#call graph</span> <span class="tag">#panics</span> <span class="tag">#developer tooling</span></div>
</article>
<hr>

<a id="item-30"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.benjoffe.com/fast-floordiv">针对常量除数的有符号 64 位向下取整除法新算法</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 26, 18:44</span></div>
<p class="news-summary">Ben Joffe 发布了一篇博客文章（日期为 2026 年 10 月 27 日），提出了一种在除数于编译期已知时计算有符号整数向下取整除法的新方法，涵盖负除数、各种位宽以及 ARM64 专属的代码生成细节。文章给出了以 86400 等除数为示例的具体常量推导，并在 Apple M4 Pro、Snapdragon X1-26-100、AMD Ryzen 9 9950X3D 和 Intel Core i7 上，用吞吐量与延迟基准对比了该方法与语言内置除法运算的表现。 整数除法是 CPU 上最慢的基础操作之一，因此用乘法加移位序列替代运行时除法一直是编译器与库的经典优化方向；把这一优化扩展到对有符号 64 位值正确的向下取整语义，对编译器、数学库和底层系统代码都有实际意义。作者指出该技术还能用于更快的正模运算和更快的“欧几里得”除法，这扩大了它在实现这些运算的库中的潜在用途。 文章展示了如何用魔数常量做 128 位乘法、再加上偏置以及对负乘数的“add back”修正来处理 86400 这类除数，并指出在 x86 上该修正开销很低（adc），而在 ARM64 上由于高低两半需要分别相乘，会多出一次 smulh/umulh 乘法。文章还说明该方法适用于所有位宽、收益最大的是 64 位场景，并且 ARM64 需要为高、低 64 位半结果分别执行一次乘法。</p>
<div class="news-background"><strong>背景</strong> 对编译期已知常量做整数除法时，编译器通常会将其改写为乘以预先计算好的“魔数”常量再移位，这一方法记录在 Henry S. Warren Jr. 的《Hacker&#x27;s Delight》一书中。C 等大多数语言中的有符号除法是向零截断，而向下取整除法是向负无穷取整，两者在操作数为负时结果不同；作者引用了《Hacker&#x27;s Delight》中“向下取整往往才是你想要的结果”的说法。要为负除数与负被除数正确处理向下取整变体，需要额外的修正步骤，而新公式正是试图在这些步骤上节省开销。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.benjoffe.com/fast-floordiv">The missing chapter of Hacker &#x27; s Delight</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hacker&#x27;s_Delight">Hacker &#x27; s Delight - Wikipedia</a></li>
<li><a href="https://www.scs.stanford.edu/~zyedidia/arm64/umulh.html">UMULH -- A64 - Stanford University</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#integer division</span> <span class="tag">#compiler optimization</span> <span class="tag">#ARM64</span> <span class="tag">#bit manipulation</span> <span class="tag">#systems programming</span></div>
</article>
<hr>

<a id="item-31"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://www.cheswick.com/ches/papers/berferd.pdf">Bill Cheswick 1992 年经典论文《An Evening with Berferd》再度引发关注</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 27, 18:48</span></div>
<p class="news-summary">Lobsters 上的一则投稿让 Bill Cheswick 1992 年的论文《An Evening with Berferd: In Which a Cracker is Lured, Endured, and Studied》重新进入公众视野。该文记述了 Cheswick 与 AT&amp;T Bell Labs 的同事如何用诱饵和陷阱，与代号“Berferd”的入侵者周旋数月，追踪其位置并研究其手法。论文还记录了他们在受控环境中搭建 chroot“Jail”以观察攻击者活动的过程。 这篇论文被普遍视为最早一批关于后来被称为 honeypot 式攻击者观察的一手记录，因此至今仍是 intrusion detection 与威胁情报领域的基础性参考文献。它重新引发讨论，也说明现代基于欺骗的安全思路有相当一部分可以追溯到 1990 年代初的实战应急响应实验。 Cheswick 的记述强调了这场较量的刻意性与交互性：防守方并未简单封堵入侵者，而是向其提供虚假线索并设法拖住对方，以便观察其手法并追踪来源。观察工作在一个基于 chroot 的“jail”中进行，目的是在监控的同时限制攻击者的活动范围，这一做法预示了后来的沙箱与 honeypot 隔离实践。</p>
<div class="news-background"><strong>背景</strong> 在计算机安全领域，honeypot 是一种伪装成合法且有价值目标的诱饵系统或数据集，用来吸引攻击者，从而使防守方能够检测、转移或研究他们。Honeypot 通常按所针对的威胁类型划分，例如电子邮件或垃圾邮件陷阱以及服务器端陷阱，并且存在一个关键局限：它只能反映针对该 honeypot 本身的活动，而非整体威胁态势。Cheswick 的论文早于 honeypot 这一术语的广泛使用，记录的是同一思路的早期人工操作版本。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="http://www.cheswick.com/ches/papers/berferd.pdf">An Evening with Berferd In Which a Cracker is ... - Cheswick</a></li>
<li><a href="https://en.wikipedia.org/wiki/Honeypot_(computing)">Honeypot (computing) - Wikipedia</a></li>
<li><a href="https://web.eecs.umich.edu/~aprakash/security/handouts/berferd.pdf">An Evening with Berferd In Which a Cracker is Lured, Endured ...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#security</span> <span class="tag">#honeypots</span> <span class="tag">#intrusion-detection</span> <span class="tag">#networking</span> <span class="tag">#computer-history</span></div>
</article>
<hr>

<a id="item-32"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://evancz.dev/why-is-it-so-expensive-to-send-an-email">为什么大规模发送邮件的成本远超一次 TCP 连接</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 26, 13:25</span></div>
<p class="news-summary">Elm 的创建者、曾在 Google 参与 Gmail“分类收件箱（tabbed inbox）”团队工作的 Evan Czaplicki 发表了一篇详细文章，解释了为什么事务性邮件的价格并不便宜——他引用了常见的“每 1000 封约 15 美元”这一数字——尽管通过 SMTP 真正把邮件发出去在技术上并不复杂。在实验中，他用 Haskell 和 C 配合 OpenSSL 自己写了一个发送器，配置了私钥和 DNS 记录，并成功把邮件投递到了 Gmail，但他发现 Outlook 用户根本收不到这些邮件，连垃圾箱里都没有。 这篇文章重新定义了一个常被低估的系统问题：邮件的难点不在协议本身，而在于送达率、域名与 IP 信誉以及运维信任，而这些恰恰是第三方服务商真正在售卖的东西。对那些想用几百行代码替掉事务性邮件服务商的开发者——无论是做副业项目还是早期产品——这是一次很实用的现实提醒。 文章指出 SMTP 是一种明文、对话式的协议（使用 HELO、MAIL FROM 等关键字和 220 之类的数字状态码），而实际障碍在于 ISP 对 25 端口的封锁以及各邮箱服务商的垃圾邮件过滤；大型服务商在很大程度上依赖 IP 地址段的信誉，这就迫使严肃的发送方自持 IP 段并维持较高的日均发信量。作者也明确承认自己认知有限，表示从未与反垃圾邮件团队共事，并欢迎“走廊那头的反垃圾同事”指正。</p>
<div class="news-background"><strong>背景</strong> 传统上邮件通过 25 端口上的 SMTP 发送，而许多住宅宽带 ISP 会封锁该端口以抑制垃圾邮件、保护自身网络信誉，因此发送方通常需要经由邮件服务商中转。现代邮箱服务商还要求域名认证——在 DNS 中发布 SPF、DKIM 和 DMARC 记录——以验证发送方有权代表该域名发信、且邮件内容未被篡改，同时会评估发件方信誉来决定是投递、过滤还是静默丢弃。正是“认证 + 信誉”这套组合，使得“打开一个 TCP 连接”无法等同于大规模可靠送达，也正是专业事务性邮件服务存在的原因。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://www.smtp.com/blog/technical/why-is-port-25-often-blocked-by-isps/">Why is port 25 often blocked by ISPs ? - SMTP .com</a></li>
<li><a href="https://linuxize.com/post/email-authentication-spf-dkim-dmarc/">Email Authentication Explained: SPF, DKIM, and DMARC</a></li>
<li><a href="https://mailtrap.io/blog/email-infrastructure-platforms/">6 Best Email Infrastructure Platforms Compared [2026] - Mailtrap</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#email infrastructure</span> <span class="tag">#deliverability</span> <span class="tag">#SMTP</span> <span class="tag">#transactional email</span> <span class="tag">#systems engineering</span></div>
</article>
<hr>

<a id="item-33"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://stalw.art/blog/stalwart-1-0/">Stalwart v1.0 发布：Rust 邮件服务器对标 Postfix 与 Dovecot</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 26, 16:28</span></div>
<p class="news-summary">开源 Rust 邮件与协作服务器 Stalwart 经过五年开发，发布了首个稳定版本 v1.0。此次发布重点包括性能优化、最终确定数据库 schema 以简化升级，以及新增对 PDF 和办公文档的全文搜索。 稳定版 1.0 和最终确定的 schema 降低了升级风险，使 Stalwart 在生产邮件部署中更具可信度。它与 Postfix 3.11 和 Dovecot 2.4 的对比 benchmark 为基础设施运维人员提供了具体参照，不过这些数据由厂商发布。 文章称 v1.0 包含近 200 个 commit、涉及 1,300 多个文件，其中大部分是性能工作；benchmark 在相同的 Azure 服务器上进行，配置为 8 个 AMD EPYC Zen 5 vCPU、32 GiB 内存、本地 NVMe，并加载 1,000 个邮箱以及三个最多含 250,000 封邮件的大邮箱。Stalwart 在 SMTP 上对比 Postfix 3.11、在 IMAP 上对比 Dovecot 2.4，并采用相同的加密、密码哈希和全文搜索设置。</p>
<div class="news-background"><strong>背景</strong> Stalwart 是一个用 Rust 编写的开源邮件与协作服务器，支持 JMAP、IMAP、POP3、SMTP、CalDAV、CardDAV 和 WebDAV。JMAP 是一种基于 HTTP 和 JSON 的现代邮件协议，被开发为 IMAP 及专有邮件 API 的替代方案。Postfix 和 Dovecot 分别是部署最广泛的开源 SMTP 和 IMAP 组件之一，因此常被用作对比对象。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/stalwartlabs/stalwart">GitHub - stalwartlabs/stalwart: All-in-one Mail ...</a></li>
<li><a href="https://stalw.art/">Stalwart Mail &amp; Collaboration Server</a></li>
<li><a href="https://en.wikipedia.org/wiki/JSON_Meta_Application_Protocol">JSON Meta Application Protocol - Wikipedia</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#email</span> <span class="tag">#rust</span> <span class="tag">#open-source</span> <span class="tag">#mail-server</span> <span class="tag">#benchmarks</span></div>
</article>
<hr>

<a id="item-34"></a>
<article class="news-item">
<h2 class="news-title"><a href="https://slughorn.io/">slughorn 以 C++20 实现 Slug GPU 矢量图形渲染技术</a><span class="score-badge score-mid">7.0</span></h2>
<div class="news-meta"><span class="source-chip chip-rss">rss</span><span class="source-name">Lobsters</span><span class="news-time">Oct 27, 13:11</span></div>
<p class="news-summary">slughorn 是一个采用 MIT 许可证的新 C++20 库，实现了 Slug GPU 矢量图形渲染技术，可从 SVG、FreeType、Blend2D、Cairo 和 Skia 接收几何数据，也可直接使用其原生的 Canvas API 绘制图形。它将生成的曲线和 band 数据烘焙进 GPU 纹理图集（RGBA32F 的 curve texture 与 RGBA16UI 的 band texture），并上传至 OpenGL、Vulkan、WebGPU 和 DirectX，同时提供 Python 绑定文档。 Slug 风格的渲染方式可直接在 GPU 上绘制填充和描边的矢量几何，并具备分辨率无关性；将该技术封装在熟悉的 canvas API 与多个现代后端之后，可以降低图形工程师的使用门槛——否则他们需要自行实现这一算法。同时支持桌面图形 API 与 WebGPU，使其对原生应用和基于浏览器的工具都具有相关性。 该库以 Atlas 对象（例如 2048 尺寸的图集）为核心，作为 GPU 纹理的后备存储，其上叠加 Canvas 用于创作形状、渐变和复合路径，并可用相反绕向在图形中挖出镂空。需要注意的是，它仍是一个细分领域的早期项目，而非被广泛采用的标准；现有材料并未确立其性能数据、API 稳定性或生产可用性。</p>
<div class="news-background"><strong>背景</strong> Slug 是由 Eric Lengyel 提出的 GPU 渲染技术，最初为文字渲染设计，如今也能处理通用矢量图形：它不在每帧把轮廓三角化，也不预计算有向距离场（SDF/MSDF）图集，而是将字形和图形以二次贝塞尔曲线与线段列表的形式存放在小型 GPU 缓冲区中，并在着色器中求值。Slughorn 是 AlphaPixel 实现该方法的库。作为受支持的输入来源，Blend2D 和 Cairo 都是成熟的 C++ 2D 矢量图形库，其中 Blend2D 被定位为 Cairo 的高性能替代方案。</div>
<details class="news-refs"><summary>参考链接</summary>
<ul>
<li><a href="https://sluglibrary.com/">Slug Font Rendering Library</a></li>
<li><a href="https://alphapixeldev.com/sdf-vs-msdf-vs-slug-vs-rive-gpu-text-rendering/">SDF vs MSDF vs Slug: GPU Text Rendering | AlphaPixel</a></li>
<li><a href="https://pypi.org/project/slughorn/">GPU vector graphics : quadratic-Bezier curve rendering via signed...</a></li>
</ul>
</details>
<div class="news-tags"><span class="tag">#GPU vector graphics</span> <span class="tag">#C++20</span> <span class="tag">#Slug algorithm</span> <span class="tag">#rendering backends</span> <span class="tag">#graphics libraries</span></div>
</article>
<hr>