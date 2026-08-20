# 音频放置说明

播放器会按 `data/cases.json` 里的相对路径去取文件。文件不存在时显示占位，不报错。

把音频拷进对应目录后提交即可，文件名必须一致。

## 热词 `01_hotword/`

每个 case 一个 `audio.mp3`：

```
audio/01_hotword/HW-FAIR-ZH-1/audio.mp3
audio/01_hotword/HW-FAIR-ZH-2/audio.mp3
audio/01_hotword/HW-FAIR-EN-1/audio.mp3
audio/01_hotword/HW-FAIR-EN-2/audio.mp3
audio/01_hotword/HW-FAIR-EN-3/audio.mp3
audio/01_hotword/HW-LIMIT-EN-1/audio.mp3
```

## 目标说话人 `02_target_speaker/`

每个 case 两个文件。请先听 enrollment，再听 mixture。

```
audio/02_target_speaker/TS-EN-1/enrollment.flac
audio/02_target_speaker/TS-EN-1/mixture.wav
audio/02_target_speaker/TS-EN-2/enrollment.flac
audio/02_target_speaker/TS-EN-2/mixture.wav
audio/02_target_speaker/TS-ZH-1/enrollment.wav
audio/02_target_speaker/TS-ZH-1/mixture.wav
audio/02_target_speaker/TS-ZH-2/enrollment.wav
audio/02_target_speaker/TS-ZH-2/mixture.wav
audio/02_target_speaker/TS-ZH-3/enrollment.wav
audio/02_target_speaker/TS-ZH-3/mixture.wav
audio/02_target_speaker/TS-ZH-4/enrollment.wav
audio/02_target_speaker/TS-ZH-4/mixture.wav
```

## 退化环境 `03_vitw/`

```
audio/03_vitw/VITW-ZH-1/audio.wav
audio/03_vitw/VITW-ZH-2/audio.wav
audio/03_vitw/VITW-ZH-3/audio.wav
audio/03_vitw/VITW-EN-1/audio.wav
audio/03_vitw/VITW-EN-2/audio.wav
audio/03_vitw/VITW-EN-3/audio.wav
```

## 耳语 `04_whisper/`

```
audio/04_whisper/WHSP-ZH-1/audio.wav
audio/04_whisper/WHSP-ZH-2/audio.wav
audio/04_whisper/WHSP-ZH-3/audio.wav
audio/04_whisper/WHSP-EN-1/audio.wav
audio/04_whisper/WHSP-EN-2/audio.wav
audio/04_whisper/WHSP-EN-3/audio.wav
```

仓库内已有 `.gitkeep`，拷贝音频后可以删掉它。GitHub 单文件建议小于 50 MB；这些 clip 都是数秒短音频。
