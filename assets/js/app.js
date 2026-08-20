const I18N = {
  zh: {
    "nav.overview": "概述",
    "nav.arch": "架构",
    "nav.results": "结果",
    "nav.listen": "试听室",
    "nav.cite": "引用",
    "hero.lede": "一个 1.7B SpeechLLM：在同一套参数里，用任务指令和可选参考输入，完成热词偏置、目标说话人抽取、退化环境与耳语识别。",
    "hero.listen": "进入试听室",
    "hero.github": "GitHub",
    "stat.entity": "GigaSpeechBench 实体误差（中 / 英，相对无热词）",
    "stat.recall": "CommonVoice 大词表 Recall@50",
    "stat.ts": "目标说话人 in-house WER",
    "stat.whsp": "耳语 wEar CER / WTIMIT WER",
    "ov.title": "四种识别条件，一个模型",
    "ov.p": "通用转写只是实际 ASR 的一部分。AmphionASR 把热词列表和注册音频当作任务条件，把退化与耳语当作非典型声学输入，输出始终是「被请求的那一路语音」的转写。",
    "fig1.cap": "图 1：AmphionASR 的四种识别能力。左上为热词偏置，右上为目标说话人，左下为退化稳健，右下为耳语识别。",
    "fig2.cap": "图 2：AmphionASR 架构。音频编码器把波形映到 LLM 嵌入空间；可选注册音频走同一编码器；检索支路在解码前插入 Top-K 热词。虚线为推理时可选路径。",
    "cap.hw.t": "热词偏置",
    "cap.hw.p": "细粒度双编码器从约 1 万候选中检索 Top-50，注入 prompt。相对无热词，中英实体误差分别下降 55% 与 37%；在线检索中位额外时延约 1–3 ms。",
    "cap.ts.t": "目标说话人",
    "cap.ts.p": "3–5 秒注册音频 + 混合语音。只转写被点名的说话人；目标不在场时应保持静默。In-house 正例 WER 13.02%，静音虚警 6.10%。",
    "cap.deg.t": "退化稳健",
    "cap.deg.p": "远场、噪声、混响、染色、丢包及其叠加。Voice-in-the-Wild 16 个子集中，有 8 个取得对照系统里的最低 WER。",
    "cap.wh.t": "耳语识别",
    "cap.wh.p": "低能量、非典型激励。中文 wEar CER 0.58%，英文 WTIMIT WER 6.11%，均为报告中的最低误差。",
    "arch.title": "编码器、检索器、语言模型",
    "arch.p": "音频编码器把 16 kHz 波形映到 LLM 嵌入空间；文本支路携带指令与可选条件；检索支路在解码前从大词表抽出 Top-K 热词。初始化自 Qwen3-ASR-1.7B，检索适配器 2.6M，从零训练。",
    "arch.note": "三阶段 LoRA SFT：Stage 1 联合更新编码器与 LLM（退化 + 耳语）；Stage 2–3 冻结编码器，加入热词、目标说话人，并回放通用转写以防遗忘。随后对 LLM 做 GRPO，再单独训练检索适配器。",
    "res.title": "报告中的关键数字",
    "res.p": "下面只摘录技术报告里最适合 Demo 讲清楚的对照。完整表格、协议边界与未覆盖的结论，以报告正文为准。",
    "res.entity": "实体识别 · GigaSpeechBench AVG",
    "res.entity.note": "对照系统均为通用 ASR（无热词 prompt）。AmphionASR w/ RAG 使用每领域词表、K=50。该对比衡量的是「完整检索偏置流水线」，而不是在相同输入下的检索单独贡献。",
    "res.other": "目标说话人 / 耳语",
    "th.sys": "系统",
    "res.ts.note": "TS-ASR 的 Qwen3-Omni 为零样本双音频指令；其余保留项目评测 prompt。耳语对照均贪婪解码，无 whisper 专用 prompt。",
    "listen.title": "24 条可讲清楚的样本",
    "listen.p": "中英各 12 条。每条都可以直接听输入音频；目标说话人请先听注册音频，再听混合音频。",
    "listen.loading": "正在载入样本…",
    "cite.title": "引用",
    "cite.p": "AmphionASR: Personalized Context-Aware Speech Recognition. Amphion Team, 2026.",
    "cite.copy": "复制 BibTeX",
    "cite.copied": "已复制",
    "foot.left": "Amphion Team · 试听室音频已随页面提供",
    "tab.all": "全部",
    "tab.hotword": "热词",
    "tab.target_speaker": "目标说话人",
    "tab.degradation": "退化环境",
    "tab.whisper": "耳语",
    "lang.all": "中英",
    "audio.pending": "音频稍后补入",
    "audio.ready": "播放",
    "ref": "参考转写",
    "ours": "AmphionASR",
    "more.hw": "展开完整 Top-50",
    "speakers.target": "目标",
    "speakers.enroll": "注册原文",
    "speakers.int": "干扰",
    "empty.hyp": "（空转写）",
    "aux": "辅助对照，非公平排名",
    "proto.hotword": "热词准确率 case 使用同一条音频和同一份独立检索 Top-50。Amphion 直接吃 prompt；百炼 Fun-ASR-Realtime 走官方 custom vocabulary，50 词统一权重 4。HW-LIMIT-EN-1 单独标为接口边界，不与前五条混作同协议结论。",
    "proto.target_speaker": "AmphionASR 与 Qwen3-Omni-30B-A3B 都接收 enrollment + mixture。FireRed-ASR2-LLM 只吃 mixture，是普通 ASR 对照，不用于公平的目标说话人排名。请先听注册，再听混合。",
    "proto.degradation": "真实录音子集，输入只有退化音频。对照为仓库内逐样本输出，不是论文汇总值的抄录。",
    "proto.whisper": "输入只有耳语音频，无 whisper 专用 prompt。九个对照与 AmphionASR 使用同一 WhisperEar sample ID。",
    "proto.all": "四类场景共用一个 1.7B 模型，只改指令和可选参考输入。",
    "zh": "中文",
    "en": "英文",
  },
  en: {
    "nav.overview": "Overview",
    "nav.arch": "Model",
    "nav.results": "Results",
    "nav.listen": "Listening room",
    "nav.cite": "Cite",
    "hero.lede": "A 1.7B SpeechLLM that handles hotword biasing, target-speaker extraction, degraded acoustics, and whispered speech in one parameter set, driven by task instructions and optional references.",
    "hero.listen": "Open the listening room",
    "hero.github": "GitHub",
    "stat.entity": "GigaSpeechBench entity error (ZH / EN vs. no hotword)",
    "stat.recall": "CommonVoice large-pool Recall@50",
    "stat.ts": "Target-speaker in-house WER",
    "stat.whsp": "Whispered wEar CER / WTIMIT WER",
    "ov.title": "Four recognition settings, one model",
    "ov.p": "Generic transcription is only part of practical ASR. AmphionASR takes hotword lists and enrollment audio as task conditions, and treats degradations and whisper as atypical acoustics. The desired output is always the transcript of the requested speech.",
    "fig1.cap": "Figure 1: Four recognition capabilities of AmphionASR. Top-left: hotword conditioning. Top-right: target-speaker ASR. Bottom-left: degradation-robust ASR. Bottom-right: whispered-speech ASR.",
    "fig2.cap": "Figure 2: AmphionASR architecture. The audio encoder maps the waveform into the LLM embedding space; optional enrollment uses the same encoder; a retrieval branch inserts top-K hotwords before decoding. Dashed paths are optional at inference.",
    "cap.hw.t": "Hotword biasing",
    "cap.hw.p": "A fine-grained dual encoder retrieves Top-50 from ~10k candidates and injects them into the prompt. Relative to no hotword context, entity error drops 55% (ZH) and 37% (EN). Online retrieval adds a few milliseconds.",
    "cap.ts.t": "Target speaker",
    "cap.ts.p": "A 3–5 s enrollment plus a mixture. Transcribe only the named speaker; stay silent if they are absent. In-house positive WER 13.02%, silence false-alarm 6.10%.",
    "cap.deg.t": "Degradation robustness",
    "cap.deg.p": "Far-field, noise, reverb, coloration, dropout, and compounds. Lowest WER on 8 of 16 Voice-in-the-Wild subsets among the compared systems.",
    "cap.wh.t": "Whispered speech",
    "cap.wh.p": "Low-energy, atypical phonation. 0.58% CER on Mandarin wEar and 6.11% WER on English WTIMIT, both the lowest in the report.",
    "arch.title": "Encoder, retriever, language model",
    "arch.p": "The audio encoder maps 16 kHz waveforms into the LLM embedding space. The text branch carries the instruction and optional conditions. The retrieval branch selects Top-K hotwords before decoding. Initialized from Qwen3-ASR-1.7B; 2.6M retrieval adapters trained from scratch.",
    "arch.note": "Three-stage LoRA SFT: Stage 1 updates encoder and LLM on degradation and whisper; Stages 2–3 freeze the encoder, add hotword and target-speaker data, and replay general transcription. GRPO then updates the LLM; retrieval adapters are trained last.",
    "res.title": "Headline numbers from the report",
    "res.p": "Only the contrasts that are easy to explain in a demo. Full tables, protocol caveats, and unsupported claims stay in the technical report.",
    "res.entity": "Entity recognition · GigaSpeechBench AVG",
    "res.entity.note": "Baselines are general ASR with no hotword prompt. AmphionASR w/ RAG uses per-domain pools, K=50. This measures the full retrieval-conditioned pipeline, not an isolated retrieval ablation under identical inputs.",
    "res.other": "Target speaker / whisper",
    "th.sys": "System",
    "res.ts.note": "Qwen3-Omni is zero-shot with a dual-audio instruction; other TS systems keep the project prompt. Whispered-speech baselines are greedy, with no whisper-specific prompt.",
    "listen.title": "24 cases that are easy to hear",
    "listen.p": "12 Mandarin and 12 English. Each case includes the input audio. For target-speaker cases, listen to enrollment first, then the mixture.",
    "listen.loading": "Loading cases…",
    "cite.title": "Cite",
    "cite.p": "AmphionASR: Personalized Context-Aware Speech Recognition. Amphion Team, 2026.",
    "cite.copy": "Copy BibTeX",
    "cite.copied": "Copied",
    "foot.left": "Amphion Team · listening-room audio is included",
    "tab.all": "All",
    "tab.hotword": "Hotword",
    "tab.target_speaker": "Target speaker",
    "tab.degradation": "Degradation",
    "tab.whisper": "Whisper",
    "lang.all": "ZH+EN",
    "audio.pending": "Audio coming later",
    "audio.ready": "Play",
    "ref": "Reference",
    "ours": "AmphionASR",
    "more.hw": "Show full Top-50",
    "speakers.target": "Target",
    "speakers.enroll": "Enrollment text",
    "speakers.int": "Interferer",
    "empty.hyp": "(empty transcript)",
    "aux": "auxiliary, not a fair ranking",
    "proto.hotword": "Accuracy cases share one audio clip and one independently retrieved Top-50. Amphion reads the prompt; Fun-ASR-Realtime uses official custom vocabulary with weight 4. HW-LIMIT-EN-1 is an API-boundary case, not mixed into the matched-protocol claim.",
    "proto.target_speaker": "AmphionASR and Qwen3-Omni-30B-A3B both receive enrollment + mixture. FireRed-ASR2-LLM is vanilla ASR on the mixture only, not a fair TS ranking. Listen to enrollment first.",
    "proto.degradation": "Real-recording subsets; input is the degraded clip only. Baselines are per-sample outputs from this project, not copied aggregate tables.",
    "proto.whisper": "Whispered audio only, no whisper-specific prompt. Nine baselines share WhisperEar sample IDs with AmphionASR.",
    "proto.all": "Four settings, one 1.7B model; only the instruction and optional references change.",
    "zh": "Chinese",
    "en": "English",
  },
};

const SCENES = ["all", "hotword", "target_speaker", "degradation", "whisper"];
const ENTITY_BARS = [
  { name: "AmphionASR w/ RAG", zh: 10.39, en: 9.35, ours: true },
  { name: "Fun-ASR-Realtime", zh: 10.91, en: 12.94 },
  { name: "Qwen3-ASR-1.7B", zh: 18.63, en: 13.81 },
  { name: "AmphionASR w/o RAG", zh: 23.18, en: 14.78, alt: true },
];

const state = {
  lang: localStorage.getItem("amphionasr-lang") || "zh",
  scene: "all",
  langFilter: "all",
  cases: [],
};

const t = (key) => I18N[state.lang][key] || I18N.en[key] || key;

function applyI18n() {
  document.documentElement.lang = state.lang === "zh" ? "zh-CN" : "en";
  document.querySelectorAll("[data-i18n]").forEach((el) => {
    el.textContent = t(el.dataset.i18n);
  });
  document.querySelectorAll(".lang-toggle button").forEach((btn) => {
    btn.classList.toggle("active", btn.dataset.lang === state.lang);
  });
}

function renderBars() {
  const max = Math.max(...ENTITY_BARS.flatMap((d) => [d.zh, d.en]));
  const host = document.getElementById("entity-bars");
  host.innerHTML =
    `<div class="bar-row"><div></div><div class="fine" style="margin:0">ZH B-CER · EN B-WER</div><div></div></div>` +
    ENTITY_BARS.map((d) => {
      const cls = d.ours ? "ours" : d.alt ? "alt" : "";
      return `<div class="bar-row">
      <div>${d.name}</div>
      <div>
        <div class="bar-track"><div class="bar-fill ${cls}" style="width:${(100 * d.zh) / max}%"></div></div>
        <div class="bar-track" style="margin-top:4px"><div class="bar-fill ${cls}" style="width:${(100 * d.en) / max}%;opacity:.7"></div></div>
      </div>
      <div class="num">${d.zh.toFixed(2)}<br>${d.en.toFixed(2)}</div>
    </div>`;
    }).join("");
}

function tokenize(text, lang) {
  if (!text) return [];
  if (lang === "zh") return [...text];
  return text.split(/(\s+|[.,!?;:"“”()])/).filter((x) => x !== "");
}

function lcsMask(a, b) {
  const n = a.length;
  const m = b.length;
  const dp = Array.from({ length: n + 1 }, () => new Uint16Array(m + 1));
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= m; j++) {
      dp[i][j] = a[i - 1] === b[j - 1] ? dp[i - 1][j - 1] + 1 : Math.max(dp[i - 1][j], dp[i][j - 1]);
    }
  }
  const keep = new Array(n).fill(false);
  let i = n;
  let j = m;
  while (i > 0 && j > 0) {
    if (a[i - 1] === b[j - 1]) {
      keep[i - 1] = true;
      i--;
      j--;
    } else if (dp[i - 1][j] >= dp[i][j - 1]) i--;
    else j--;
  }
  return keep;
}

function normTok(tok, lang) {
  if (lang === "zh") return tok;
  return tok.toLowerCase();
}

function markupDiff(hyp, ref, lang, highlights = []) {
  if (!hyp) return `<em class="empty-hyp">${t("empty.hyp")}</em>`;
  const a = tokenize(hyp, lang);
  const b = tokenize(ref, lang).map((x) => normTok(x, lang));
  const aNorm = a.map((x) => normTok(x, lang));
  const keep = lcsMask(aNorm, b);
  const hits = (highlights || []).map((h) => h.toLowerCase());
  return a
    .map((tok, i) => {
      const esc = escapeHtml(tok);
      const low = tok.toLowerCase();
      if (hits.some((h) => h && (low === h || tok === h))) return `<mark class="hit">${esc}</mark>`;
      if (/^\s+$/.test(tok) || /^[.,!?;:"“”()，。！？、；：]$/.test(tok)) return esc;
      if (!keep[i]) return `<mark class="err">${esc}</mark>`;
      return esc;
    })
    .join("");
}

function markupRef(ref, highlights = []) {
  if (!highlights.length) return escapeHtml(ref);
  const parts = highlights
    .slice()
    .sort((a, b) => b.length - a.length)
    .map(escapeReg);
  if (!parts.length) return escapeHtml(ref);
  const re = new RegExp(`(${parts.join("|")})`, "gi");
  return escapeHtml(ref).replace(re, '<mark class="hit">$1</mark>');
}

function escapeHtml(s) {
  return String(s)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function escapeReg(s) {
  return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function audioSlot(slot) {
  const label = slot.label[state.lang] || slot.label.en;
  const el = document.createElement("div");
  el.className = "audio-slot" + (slot.role === "enrollment" ? " enroll" : "");
  el.innerHTML = `<label>${escapeHtml(label)}</label>
    <audio controls preload="metadata" src="${escapeHtml(slot.src)}"></audio>
    <div class="ph" hidden>
      <strong>${t("audio.pending")}</strong>
      <code>${escapeHtml(slot.src)}</code>
    </div>`;
  const audio = el.querySelector("audio");
  audio.addEventListener("error", () => {
    el.classList.add("empty");
    audio.remove();
    el.querySelector(".ph")?.removeAttribute("hidden");
  });
  return el;
}

function renderToolbar() {
  const tabs = document.getElementById("scene-tabs");
  tabs.innerHTML = SCENES.map(
    (s) => `<button type="button" class="tab${state.scene === s ? " active" : ""}" data-scene="${s}">${t("tab." + s)}</button>`
  ).join("");
  tabs.onclick = (e) => {
    const btn = e.target.closest("[data-scene]");
    if (!btn) return;
    state.scene = btn.dataset.scene;
    renderToolbar();
    renderCases();
  };

  const chips = document.getElementById("lang-chips");
  const langs = [
    ["all", t("lang.all")],
    ["zh", t("zh")],
    ["en", t("en")],
  ];
  chips.innerHTML = langs
    .map(
      ([id, label]) =>
        `<button type="button" class="chip${state.langFilter === id ? " active" : ""}" data-lf="${id}">${label}</button>`
    )
    .join("");
  chips.onclick = (e) => {
    const btn = e.target.closest("[data-lf]");
    if (!btn) return;
    state.langFilter = btn.dataset.lf;
    renderToolbar();
    renderCases();
  };

  const protoKey =
    state.scene === "all" ? "proto.all" : `proto.${state.scene}`;
  document.getElementById("protocol").textContent = t(protoKey);
}

function renderCase(c) {
  const title = c.title[state.lang] || c.title.en;
  const highlights = c.hotwords?.targets?.map((x) => x.term) || c.highlights || [];
  const article = document.createElement("article");
  article.className = "case";
  article.id = c.id;

  const pills = [
    `<span class="pill ${c.lang}">${t(c.lang)}</span>`,
    `<span class="pill">${c.duration_sec.toFixed(1)}s</span>`,
    c.degradation ? `<span class="pill">${escapeHtml(c.degradation)}</span>` : "",
    c.protocol === "limit" ? `<span class="pill limit">API limit</span>` : "",
  ]
    .filter(Boolean)
    .join("");

  article.innerHTML = `
    <div class="case-top">
      <div>
        <h3>${escapeHtml(c.id)} · ${escapeHtml(title)}</h3>
        <div class="meta">${pills}</div>
      </div>
    </div>
    <div class="audio-grid"></div>
    <div class="speakers-host"></div>
    <div class="hotwords-host"></div>
    <div class="transcripts"></div>
    <p class="insight">${escapeHtml(c.insight[state.lang] || c.insight.en)}</p>
  `;

  const grid = article.querySelector(".audio-grid");
  c.audio_slots.forEach((slot) => grid.appendChild(audioSlot(slot)));

  if (c.speakers) {
    const host = article.querySelector(".speakers-host");
    host.className = "speakers";
    const rows = [];
    if (c.speakers.enroll_text) {
      rows.push(`<div><b>${t("speakers.enroll")}</b> ${escapeHtml(c.speakers.enroll_text)}</div>`);
    }
    rows.push(`<div><b>${t("speakers.target")}</b> ${escapeHtml(c.speakers.target)}</div>`);
    (c.speakers.interferers || []).forEach((s, i) => {
      rows.push(`<div><b>${t("speakers.int")} ${i + 1}</b> ${escapeHtml(s)}</div>`);
    });
    host.innerHTML = rows.join("");
  }

  if (c.hotwords) {
    const host = article.querySelector(".hotwords-host");
    host.className = "hotwords";
    const hits = new Set((c.hotwords.targets || []).map((x) => x.term));
    const chips = (c.hotwords.targets || [])
      .map((x) => `<span class="hw hit">${escapeHtml(x.term)}${x.rank ? ` · #${x.rank}` : ""}</span>`)
      .join("");
    const rest = (c.hotwords.retrieved || [])
      .filter((w) => !hits.has(w))
      .map((w) => `<span class="hw">${escapeHtml(w)}</span>`)
      .join("");
    host.innerHTML = `<div class="hw-list">${chips}</div>
      <details class="more"><summary>${t("more.hw")}</summary><div class="hw-list">${rest}</div></details>`;
  }

  const lines = article.querySelector(".transcripts");
  const tag = c.amphion_tag?.[state.lang] || "";
  lines.innerHTML = `
    <div class="line ref">
      <header><span>${t("ref")}</span></header>
      <div class="txt">${markupRef(c.ref, highlights)}</div>
    </div>
    <div class="line ours">
      <header><span>${t("ours")}</span><span>${escapeHtml(tag)}</span></header>
      <div class="txt">${markupDiff(c.amphion, c.ref, c.lang, highlights)}</div>
    </div>
    ${c.baselines
      .map((b) => {
        const note = b.note ? b.note[state.lang] || b.note.en || "" : "";
        const unfair = b.fair === false ? `<span class="unfair">${t("aux")}</span>` : "";
        return `<div class="line">
          <header><span>${escapeHtml(b.name)}${note ? " · " + escapeHtml(note) : ""}</span>${unfair}</header>
          <div class="txt">${markupDiff(b.text, c.ref, c.lang, highlights)}</div>
        </div>`;
      })
      .join("")}
  `;
  return article;
}

function renderCases() {
  const host = document.getElementById("cases");
  host.innerHTML = "";
  const filtered = state.cases.filter((c) => {
    if (state.scene !== "all" && c.scenario !== state.scene) return false;
    if (state.langFilter !== "all" && c.lang !== state.langFilter) return false;
    return true;
  });
  filtered.forEach((c) => host.appendChild(renderCase(c)));
}

function bindHeroCaps() {
  document.querySelectorAll(".cap[data-scene]").forEach((a) => {
    a.addEventListener("click", () => {
      state.scene = a.dataset.scene;
      renderToolbar();
      renderCases();
    });
  });
}

async function main() {
  document.querySelectorAll(".lang-toggle button").forEach((btn) => {
    btn.addEventListener("click", () => {
      state.lang = btn.dataset.lang;
      localStorage.setItem("amphionasr-lang", state.lang);
      applyI18n();
      renderToolbar();
      renderCases();
    });
  });
  document.getElementById("copy-bib").addEventListener("click", async () => {
    await navigator.clipboard.writeText(document.getElementById("bibtex").textContent);
    const btn = document.getElementById("copy-bib");
    btn.textContent = t("cite.copied");
    setTimeout(() => (btn.textContent = t("cite.copy")), 1200);
  });

  applyI18n();
  renderBars();
  bindHeroCaps();
  renderToolbar();

  const data = await fetch("data/cases.json").then((r) => r.json());
  state.cases = data.cases;
  renderCases();
}

main().catch((err) => {
  document.getElementById("cases").textContent = String(err);
});
