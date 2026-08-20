# AmphionASR Demo Page

GitHub Pages 站点：[https://asd5152306.github.io/amphion-asr-demo/](https://asd5152306.github.io/amphion-asr-demo/)

配套静态页，对应技术报告 *AmphionASR: Personalized Context-Aware Speech Recognition*（Amphion Team, 2026.07）。页面展示统一 1.7B SpeechLLM 的四种条件识别，以及 24 条已对齐转写的试听 case。

## 现在有什么

- 中 / 英双语
- 架构示意、GigaSpeechBench / TS-ASR / 耳语关键数字
- 24 条 case：热词 6、目标说话人 6、退化环境 6、耳语 6
- 转写对照、热词 Top-50、协议说明
- 24 条 case 的输入音频（目标说话人含注册音频 + 混合音频）

音频目录约定见 [audio/README.md](audio/README.md)。

## 本地预览

GitHub Pages 和本地都需要 HTTP（不要直接打开 `index.html`）：

```bash
python3 -m http.server 8080
```

然后访问 `http://localhost:8080`。

## 开启 GitHub Pages

仓库 Settings → Pages → Build and deployment：

- Source: **Deploy from a branch**
- Branch: `main` / `/ (root)`

公开地址为 `https://<user>.github.io/amphion-asr-demo/`。

## 数据来源

`data/cases.json` 由 `scripts/build_cases.py` 从 AmphionASR 试听短名单生成。改 case 文案后重新运行该脚本即可。
