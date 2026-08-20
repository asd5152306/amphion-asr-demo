#!/usr/bin/env python3
"""Compile AmphionASR demo cases into data/cases.json."""
from __future__ import annotations

import json
from pathlib import Path

BUNDLE = Path("/chenmingjie/lx/AmphionASR/demo_cases/listening_bundle")
OUT = Path("/chenmingjie/lx/amphion-asr-demo/data/cases.json")


def load_prompt(case_id: str) -> dict:
    path = BUNDLE / "01_hotword" / case_id / "prompt.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def hw_audio(case_id: str, ext: str = "mp3") -> str:
    return f"audio/01_hotword/{case_id}/audio.{ext}"


def ts_enroll(case_id: str, ext: str) -> str:
    return f"audio/02_target_speaker/{case_id}/enrollment.{ext}"


def ts_mix(case_id: str, ext: str = "wav") -> str:
    return f"audio/02_target_speaker/{case_id}/mixture.{ext}"


def vitw_audio(case_id: str) -> str:
    return f"audio/03_vitw/{case_id}/audio.wav"


def whsp_audio(case_id: str) -> str:
    return f"audio/04_whisper/{case_id}/audio.wav"


def ranks(prompt: dict, terms: list[str]) -> list[dict]:
    retrieved = prompt.get("hotwords_retrieved") or prompt.get("hotwords_all") or []
    out = []
    for term in terms:
        rank = None
        if term in retrieved:
            rank = retrieved.index(term) + 1
        out.append({"term": term, "rank": rank})
    return out


def hotword_block(case_id: str, terms: list[str]) -> dict:
    prompt = load_prompt(case_id)
    retrieved = prompt.get("hotwords_retrieved") or prompt.get("hotwords_all") or []
    return {
        "k": 50,
        "targets": ranks(prompt, terms),
        "retrieved": retrieved,
    }


CASES = [
    # —— Hotword ——
    {
        "id": "HW-FAIR-ZH-1",
        "scenario": "hotword",
        "lang": "zh",
        "featured": True,
        "protocol": "fair",
        "title": {
            "zh": "四个奥地利地名，目标最低排第 50",
            "en": "Four Austrian place names, last target at rank 50",
        },
        "duration_sec": 8.208,
        "source_id": "common_voice_zh-CN_18987820",
        "audio_slots": [
            {"role": "audio", "src": hw_audio("HW-FAIR-ZH-1"), "label": {"zh": "输入音频", "en": "Input audio"}}
        ],
        "hotwords": None,  # filled below
        "ref": "豪斯鲁克地区埃舍瑙是奥地利上奥地利州格里斯基尔兴县的一个市镇。",
        "amphion": "豪斯鲁克地区埃舍瑙是奥地利上奥地利州格里斯基尔兴县的一个市镇。",
        "amphion_tag": {"zh": "检索 Top-50", "en": "with retrieval Top-50"},
        "baselines": [
            {
                "name": "AmphionASR (no hotword)",
                "fair": True,
                "text": "豪斯鲁克地区埃舍瑙是奥地利上奥地利州格里斯蒂尔新县的一个市镇。",
            },
            {
                "name": "Fun-ASR-Realtime",
                "fair": True,
                "note": {"zh": "同一 Top-50 自定义词表，权重 4", "en": "same Top-50 custom vocabulary, weight 4"},
                "text": "豪斯鲁克地区埃舍瑙是奥地利上奥地利州格里茨基尔兴县的一个市镇。",
            },
        ],
        "insight": {
            "zh": "同协议对照：Amphion 恢复全部四个地名；百炼已收到正确候选，仍把「格里斯」写成「格里茨」。",
            "en": "Matched protocol: Amphion recovers all four names; Fun-ASR already has the correct candidate but writes 格里斯 as 格里茨.",
        },
    },
    {
        "id": "HW-FAIR-EN-1",
        "scenario": "hotword",
        "lang": "en",
        "featured": True,
        "protocol": "fair",
        "title": {
            "zh": "五个英国城堡地名",
            "en": "Five English castle towns",
        },
        "duration_sec": 8.064,
        "source_id": "common_voice_en_21869937",
        "audio_slots": [
            {"role": "audio", "src": hw_audio("HW-FAIR-EN-1"), "label": {"zh": "输入音频", "en": "Input audio"}}
        ],
        "ref": "Norman castles existed at Rockingham, Barnwell, Lilbourne, Northampton and Wellingborough.",
        "amphion": "Norman castles existed at Rockingham, Barnwell, Lilbourne, Northampton and Wellingborough.",
        "amphion_tag": {"zh": "检索 Top-50", "en": "with retrieval Top-50"},
        "baselines": [
            {
                "name": "AmphionASR (no hotword)",
                "fair": True,
                "text": "Norman castles existed at rockingham, banwell, lindbyborn, northampton and waringborough.",
            },
            {
                "name": "Fun-ASR-Realtime",
                "fair": True,
                "note": {"zh": "五个目标词全部写入自定义词表", "en": "all five targets accepted into custom vocabulary"},
                "text": "Norman castles existed at Rockingham, Banbury. not that.",
            },
        ],
        "insight": {
            "zh": "Amphion 五个地名全对；百炼只保住 Rockingham，随后替换并截断。",
            "en": "Amphion gets all five names; Fun-ASR keeps only Rockingham, then substitutes and truncates.",
        },
    },
    {
        "id": "HW-FAIR-EN-2",
        "scenario": "hotword",
        "lang": "en",
        "featured": True,
        "protocol": "fair",
        "title": {
            "zh": "音乐人名与意大利语曲名",
            "en": "Composer name and Italian song title",
        },
        "duration_sec": 9.252,
        "source_id": "common_voice_en_41681495",
        "audio_slots": [
            {"role": "audio", "src": hw_audio("HW-FAIR-EN-2"), "label": {"zh": "输入音频", "en": "Input audio"}}
        ],
        "ref": "Azzaiolo's \"Chi passa per 'sta strada\" was adapted by English composer William Byrd.",
        "amphion": "Azzaiolo's \"Chi passa per 'sta strada\" was adapted by English composer William Byrd.",
        "amphion_tag": {"zh": "检索 Top-50", "en": "with retrieval Top-50"},
        "baselines": [
            {
                "name": "AmphionASR (no hotword)",
                "fair": True,
                "text": "Asai yolas \"chippa sa persta strada\" was adapted by english composer william word.",
            },
            {
                "name": "Fun-ASR-Realtime",
                "fair": True,
                "text": "As I yolas, \"Chippasa perstastrada\" was adapted by English composer William Byrd.",
            },
        ],
        "insight": {
            "zh": "目标词最低排到第 25；Amphion 三个全对，百炼只修正了 William Byrd。",
            "en": "Lowest target at rank 25; Amphion recovers all three, Fun-ASR only fixes William Byrd.",
        },
    },
    {
        "id": "HW-FAIR-ZH-2",
        "scenario": "hotword",
        "lang": "zh",
        "featured": True,
        "protocol": "fair",
        "title": {
            "zh": "钟善辅 / 中山虎同音字",
            "en": "Homophone pair: 钟善辅 vs 中山虎",
        },
        "duration_sec": 8.664,
        "source_id": "common_voice_zh-CN_18774760",
        "audio_slots": [
            {"role": "audio", "src": hw_audio("HW-FAIR-ZH-2"), "label": {"zh": "输入音频", "en": "Input audio"}}
        ],
        "ref": "钟善辅，四川涪陵人，又名钟世民，笔名中山虎、山虎，中国共产党早期领导人。",
        "amphion": "钟善辅，四川涪陵人，又名钟世民，笔名中山虎、山虎，中国共产党早期领导人。",
        "amphion_tag": {"zh": "检索 Top-50", "en": "with retrieval Top-50"},
        "baselines": [
            {
                "name": "AmphionASR (no hotword)",
                "fair": True,
                "text": "钟山虎，四川涪陵人，又名钟世民，笔名钟山虎、山虎。中国共产党早期领导人。",
            },
            {
                "name": "Fun-ASR-Realtime",
                "fair": True,
                "text": "钟善辅，四川涪陵人，又名钟世民，笔名钟山虎、山虎，中国共产党早期领导人。",
            },
        ],
        "insight": {
            "zh": "Amphion 同时恢复姓名与笔名；百炼恢复了「钟善辅」，仍把笔名「中山虎」写成同音的「钟山虎」。",
            "en": "Amphion recovers both the name and the pen name; Fun-ASR gets 钟善辅 but writes 中山虎 as the homophone 钟山虎.",
        },
    },
    {
        "id": "HW-FAIR-EN-3",
        "scenario": "hotword",
        "lang": "en",
        "featured": True,
        "protocol": "fair",
        "title": {
            "zh": "Wizkids / Demogoblin / HeroClix",
            "en": "Wizkids / Demogoblin / HeroClix",
        },
        "duration_sec": 7.416,
        "source_id": "common_voice_en_19982029",
        "audio_slots": [
            {"role": "audio", "src": hw_audio("HW-FAIR-EN-3"), "label": {"zh": "输入音频", "en": "Input audio"}}
        ],
        "ref": "Wizkids released a Demogoblin figure as part of their Amazing Spider-Man \"HeroClix\" set.",
        "amphion": "Wizkids released a Demogoblin figure as part of their Amazing Spider-Man \"HeroClix\" set.",
        "amphion_tag": {"zh": "检索 Top-50", "en": "with retrieval Top-50"},
        "baselines": [
            {
                "name": "AmphionASR (no hotword)",
                "fair": True,
                "text": "Whiz kids released a \"demo goblin\" figure as part of their \"amazing spiderman hero clicks\" set.",
            },
            {
                "name": "Fun-ASR-Realtime",
                "fair": True,
                "text": "Wizkids released a Demogoblin figure as part of their Amazing Spider-Man Heroics set.",
            },
        ],
        "insight": {
            "zh": "四个品牌/角色词都已写入百炼词表；Amphion 全对，百炼把词表第 3 的 HeroClix 改成常见词 Heroics。",
            "en": "All four brand/character terms were in Fun-ASR's vocabulary; Amphion is exact, Fun-ASR replaces rank-3 HeroClix with Heroics.",
        },
    },
    {
        "id": "HW-LIMIT-EN-1",
        "scenario": "hotword",
        "lang": "en",
        "featured": False,
        "protocol": "limit",
        "title": {
            "zh": "Adelaide–Wolseley：接口长度边界",
            "en": "Adelaide–Wolseley: vocabulary length limit",
        },
        "duration_sec": 8.100,
        "source_id": "common_voice_en_38192591",
        "audio_slots": [
            {"role": "audio", "src": hw_audio("HW-LIMIT-EN-1"), "label": {"zh": "输入音频", "en": "Input audio"}}
        ],
        "ref": "It runs roughly parallel to both the Dukes Highway and the Adelaide–Wolseley railway line.",
        "amphion": "It runs roughly parallel to both the Dukes Highway and the Adelaide–Wolseley railway line.",
        "amphion_tag": {"zh": "检索 Top-50", "en": "with retrieval Top-50"},
        "baselines": [
            {
                "name": "AmphionASR (no hotword)",
                "fair": True,
                "text": "It runs roughly parallel to both the dukes highway and the adelaide wallisley railway line.",
            },
            {
                "name": "Fun-ASR-Realtime",
                "fair": False,
                "note": {
                    "zh": "49/50：Adelaide–Wolseley 含非 ASCII 且超 15 字符，被官方词表规则拒绝",
                    "en": "49/50 accepted; Adelaide–Wolseley rejected by official vocabulary rules (non-ASCII and length > 15)",
                },
                "text": "It runs roughly parallel to both the Dukes Highway and the Adelaide-Wollongong railway line.",
            },
        ],
        "insight": {
            "zh": "这不是同协议准确率对比，而是产品边界：Amphion 可直接使用完整检索 prompt；百炼无法接收目标长词，并识别成另一个地名。",
            "en": "Not a matched-accuracy comparison: Amphion takes the full retrieved prompt, while the Fun-ASR API rejects the long target and maps it to another place name.",
        },
    },
    # —— Target speaker ——
    {
        "id": "TS-EN-1",
        "scenario": "target_speaker",
        "lang": "en",
        "featured": True,
        "protocol": "fair",
        "title": {
            "zh": "对照模型完整转写了干扰说话人",
            "en": "Baseline transcribes the interferer verbatim",
        },
        "duration_sec": 3.945,
        "source_id": "tsasr_libri2mix_test_672-122797-0019_2830-3980-0001_s2_sup",
        "audio_slots": [
            {"role": "enrollment", "src": ts_enroll("TS-EN-1", "wav"), "label": {"zh": "注册音频 5.0s", "en": "Enrollment 5.0s"}},
            {"role": "mixture", "src": ts_mix("TS-EN-1"), "label": {"zh": "混合音频 3.9s", "en": "Mixture 3.9s"}},
        ],
        "speakers": {
            "enroll_text": None,
            "target": "THEY SAID TO THE GALATIANS YOU HAVE NO RIGHT TO THINK HIGHLY OF PAUL",
            "interferers": ["REJOICE IN THY OWN FRESH YOUTH"],
        },
        "ref": "They said to the Galatians you have no right to think highly of Paul.",
        "amphion": "They said to the glaziers, you have no right to think highly of Paul.",
        "amphion_tag": {"zh": "双音频", "en": "dual audio"},
        "baselines": [
            {
                "name": "Qwen3-Omni-30B-A3B",
                "fair": True,
                "note": {"zh": "同样接收 enrollment + mixture", "en": "same enrollment + mixture prompt"},
                "text": "Rejoice in thy own fresh youth.",
            },
            {
                "name": "FireRed-ASR2-LLM",
                "fair": False,
                "note": {"zh": "无 enrollment / 普通 ASR，不作公平排名", "en": "no enrollment / vanilla ASR, not a fair ranking"},
                "text": "it's tragic isn't it but i don't like to see you fall",
            },
        ],
        "insight": {
            "zh": "Qwen 输出与干扰说话人原文逐字一致；Amphion 跟随目标人，并把 Galatians 听成 glaziers——保留自然小错误。",
            "en": "Qwen matches the interferer verbatim; Amphion follows the enrolled speaker, with a natural slip (Galatians → glaziers).",
        },
    },
    {
        "id": "TS-EN-2",
        "scenario": "target_speaker",
        "lang": "en",
        "featured": True,
        "protocol": "fair",
        "title": {
            "zh": "对照选干扰人，普通 ASR 串两路",
            "en": "Baseline picks the interferer; vanilla ASR concatenates both",
        },
        "duration_sec": 3.260,
        "source_id": "tsasr_libri2mix_test_672-122797-0005_260-123440-0018_s2_sup",
        "audio_slots": [
            {"role": "enrollment", "src": ts_enroll("TS-EN-2", "wav"), "label": {"zh": "注册音频 7.4s", "en": "Enrollment 7.4s"}},
            {"role": "mixture", "src": ts_mix("TS-EN-2"), "label": {"zh": "混合音频 3.3s", "en": "Mixture 3.3s"}},
        ],
        "speakers": {
            "enroll_text": None,
            "target": "I AM VERY TIRED OF SWIMMING ABOUT HERE O MOUSE",
            "interferers": ["OH THAT MADE HIM SO ANGRY"],
        },
        "ref": "I am very tired of swimming about here O mouse.",
        "amphion": "I am very tired of swimming about here. Oh, mouse.",
        "amphion_tag": {"zh": "双音频", "en": "dual audio"},
        "baselines": [
            {
                "name": "Qwen3-Omni-30B-A3B",
                "fair": True,
                "text": "Oh, that made him so angry.",
            },
            {
                "name": "FireRed-ASR2-LLM",
                "fair": False,
                "note": {"zh": "无 enrollment / 普通 ASR", "en": "no enrollment / vanilla ASR"},
                "text": "i am very tired of swimming about so angry",
            },
        ],
        "insight": {
            "zh": "三种行为边界清楚：Qwen 选说话人 1，Amphion 跟随 enrollment 选说话人 2，FireRed 把两路末尾拼在一起。",
            "en": "Three distinct behaviors: Qwen selects speaker 1, Amphion follows enrollment to speaker 2, FireRed concatenates both tails.",
        },
    },
    {
        "id": "TS-ZH-1",
        "scenario": "target_speaker",
        "lang": "zh",
        "featured": True,
        "protocol": "fair",
        "title": {
            "zh": "对照转写了注册音频本身",
            "en": "Baseline transcribes the enrollment clip itself",
        },
        "duration_sec": 3.925,
        "source_id": "tsasr_magicdata_test_38_5867_000017_sup",
        "audio_slots": [
            {"role": "enrollment", "src": ts_enroll("TS-ZH-1", "wav"), "label": {"zh": "注册音频 4.4s", "en": "Enrollment 4.4s"}},
            {"role": "mixture", "src": ts_mix("TS-ZH-1"), "label": {"zh": "混合音频 3.9s", "en": "Mixture 3.9s"}},
        ],
        "speakers": {
            "enroll_text": "跳转到河北卫视",
            "target": "下班给我电话",
            "interferers": ["这张专辑得到了大部分得好评"],
        },
        "ref": "下班给我电话",
        "amphion": "下班给我电话。",
        "amphion_tag": {"zh": "双音频", "en": "dual audio"},
        "baselines": [
            {
                "name": "Qwen3-Omni-30B-A3B",
                "fair": True,
                "text": "跳转到河北卫视。",
            },
            {
                "name": "FireRed-ASR2-LLM",
                "fair": False,
                "note": {"zh": "无 enrollment / 普通 ASR", "en": "no enrollment / vanilla ASR"},
                "text": "得到了大部分支持",
            },
        ],
        "insight": {
            "zh": "不声称 Qwen「选错说话人」：它逐字输出的是 enrollment，而不是 mixture 中的目标句。FireRed 跟随干扰人；只有 Amphion 用注册声纹抽出目标语句。",
            "en": "Qwen is not described as picking the wrong speaker: it copies the enrollment text. FireRed follows the interferer; only Amphion extracts the target from the mixture.",
        },
    },
    {
        "id": "TS-ZH-2",
        "scenario": "target_speaker",
        "lang": "zh",
        "featured": True,
        "protocol": "fair",
        "title": {
            "zh": "三路干扰下仍跟随目标",
            "en": "Follows the target under three interferers",
        },
        "duration_sec": 5.659,
        "source_id": "tsasr_kespeech_test_1001986_000001_sup",
        "audio_slots": [
            {"role": "enrollment", "src": ts_enroll("TS-ZH-2", "wav"), "label": {"zh": "注册音频 4.9s", "en": "Enrollment 4.9s"}},
            {"role": "mixture", "src": ts_mix("TS-ZH-2"), "label": {"zh": "混合音频 5.7s", "en": "Mixture 5.7s"}},
        ],
        "speakers": {
            "enroll_text": "为了自己和他人的生命安全着想",
            "target": "为其提供更加完善的基础设施保障。",
            "interferers": [
                "这难道不是边开车边通话的标准吗变种吗",
                "东北部突出而西南部平缓",
                "酂城镇是中国河南省永城市下辖的一个镇",
            ],
        },
        "ref": "为其提供更加完善的基础设施保障。",
        "amphion": "以及提供更加完善的基础设施保障。",
        "amphion_tag": {"zh": "双音频", "en": "dual audio"},
        "baselines": [
            {
                "name": "Qwen3-Omni-30B-A3B",
                "fair": True,
                "text": "这难道不是边开车边通话，还敢小看我们，真是吃饱了撑的。",
            },
            {
                "name": "FireRed-ASR2-LLM",
                "fair": False,
                "note": {"zh": "无 enrollment / 普通 ASR", "en": "no enrollment / vanilla ASR"},
                "text": "这难道不是边开车边通话通话需要证吗驾照吗",
            },
        ],
        "insight": {
            "zh": "Qwen 与 FireRed 都主要跟随干扰说话人 1；Amphion 跟随目标人，只把句首「为其」听成「以及」。",
            "en": "Qwen and FireRed follow interferer 1; Amphion follows the enrolled speaker, slipping only 为其 → 以及.",
        },
    },
    {
        "id": "TS-ZH-3",
        "scenario": "target_speaker",
        "lang": "zh",
        "featured": False,
        "protocol": "fair",
        "title": {
            "zh": "对照跟随第二个干扰人",
            "en": "Baseline follows the second interferer",
        },
        "duration_sec": 3.788,
        "source_id": "tsasr_aishell_test_S0906_000021_sup",
        "audio_slots": [
            {"role": "enrollment", "src": ts_enroll("TS-ZH-3", "wav"), "label": {"zh": "注册音频 3.1s", "en": "Enrollment 3.1s"}},
            {"role": "mixture", "src": ts_mix("TS-ZH-3"), "label": {"zh": "混合音频 3.8s", "en": "Mixture 3.8s"}},
        ],
        "speakers": {
            "enroll_text": "上海作为一线城市代表",
            "target": "用支付宝扫一下就能付款。",
            "interferers": ["戈涛人清朝诗人文学家官员", "你既然提到了"],
        },
        "ref": "用支付宝扫一下就能付款。",
        "amphion": "用支付宝扫一下就能付款。",
        "amphion_tag": {"zh": "双音频", "en": "dual audio"},
        "baselines": [
            {
                "name": "Qwen3-Omni-30B-A3B",
                "fair": True,
                "text": "既然提到了",
            },
            {
                "name": "FireRed-ASR2-LLM",
                "fair": False,
                "note": {"zh": "无 enrollment / 普通 ASR", "en": "no enrollment / vanilla ASR"},
                "text": "用支付宝扫一下就能付款",
            },
        ],
        "insight": {
            "zh": "Qwen 输出与干扰人 2 只差句首「你」；Amphion 明确跟随 enrollment 对应的目标人。FireRed 也转到目标，仅作无注册对照。",
            "en": "Qwen matches interferer 2 minus the leading 你; Amphion follows the enrolled target. FireRed also hits the target as a no-enrollment reference.",
        },
    },
    {
        "id": "TS-ZH-4",
        "scenario": "target_speaker",
        "lang": "zh",
        "featured": False,
        "protocol": "fair",
        "title": {
            "zh": "对照逐字复述注册音频",
            "en": "Baseline recites the enrollment verbatim",
        },
        "duration_sec": 3.379,
        "source_id": "tsasr_aishell_test_S0765_000010_sup",
        "audio_slots": [
            {"role": "enrollment", "src": ts_enroll("TS-ZH-4", "wav"), "label": {"zh": "注册音频 3.8s", "en": "Enrollment 3.8s"}},
            {"role": "mixture", "src": ts_mix("TS-ZH-4"), "label": {"zh": "混合音频 3.4s", "en": "Mixture 3.4s"}},
        ],
        "speakers": {
            "enroll_text": "其作案后身上有大量血迹",
            "target": "一些没有直接收益的项目。",
            "interferers": ["犬齿后方的牙齿宽广", "是一部原住民温馨喜剧"],
        },
        "ref": "一些没有直接收益的项目。",
        "amphion": "一些没有直接收益的项目。",
        "amphion_tag": {"zh": "双音频", "en": "dual audio"},
        "baselines": [
            {
                "name": "Qwen3-Omni-30B-A3B",
                "fair": True,
                "text": "其作案后身上有大量血迹。",
            },
            {
                "name": "FireRed-ASR2-LLM",
                "fair": False,
                "note": {"zh": "无 enrollment / 普通 ASR", "en": "no enrollment / vanilla ASR"},
                "text": "第四没有直接收益的项目",
            },
        ],
        "insight": {
            "zh": "Qwen 与 enrollment 官方原文逐字一致，却没有转写 mixture；Amphion 输出目标人的完整内容。",
            "en": "Qwen copies the enrollment transcript and ignores the mixture; Amphion outputs the target speaker in the mix.",
        },
    },
    # —— VITW ——
    {
        "id": "VITW-ZH-1",
        "scenario": "degradation",
        "lang": "zh",
        "featured": True,
        "protocol": "fair",
        "degradation": "transmission dropout",
        "title": {
            "zh": "传输丢包：商场周末",
            "en": "Transmission dropout: weekend mall",
        },
        "duration_sec": 7.600,
        "source_id": "vitw_03858_real_zh_dropout",
        "audio_slots": [
            {"role": "audio", "src": vitw_audio("VITW-ZH-1"), "label": {"zh": "退化音频", "en": "Degraded audio"}}
        ],
        "ref": "那个新开的商场品牌挺多的，下次周末可以去逛逛，说不定能买到喜欢的东西。",
        "amphion": "那个新开的商场品牌挺多的，下次周末可以去逛逛，说不定能买到喜欢的东西。",
        "amphion_tag": {"zh": "无额外 prompt", "en": "no extra prompt"},
        "baselines": [
            {"name": "Qwen3-ASR-1.7B", "fair": True, "text": "那个云台的商品牌挺多的，下次周末可以去逛，定能买到喜欢的东西。"},
            {"name": "Seed 2.0 Lite", "fair": True, "text": "那边开的商品牌挺多的，下次周末可以去逛逛，指不定能买到喜欢的东西。"},
            {"name": "Fun-ASR-Realtime", "fair": True, "text": "那个云台的商品牌挺多的，下次周末可以去逛逛，说不定能买到喜欢的东西。"},
        ],
        "insight": {
            "zh": "三个对照都在 dropout 位置丢失或替换语义，AmphionASR 完整恢复。",
            "en": "All three baselines lose or rewrite meaning at the dropout; Amphion recovers the full sentence.",
        },
    },
    {
        "id": "VITW-ZH-2",
        "scenario": "degradation",
        "lang": "zh",
        "featured": True,
        "protocol": "fair",
        "degradation": "echo",
        "title": {
            "zh": "回声：地铁上画画",
            "en": "Echo: sketching on the subway",
        },
        "duration_sec": 5.760,
        "source_id": "vitw_04061_real_zh_echo",
        "audio_slots": [
            {"role": "audio", "src": vitw_audio("VITW-ZH-2"), "label": {"zh": "退化音频", "en": "Degraded audio"}}
        ],
        "ref": "我刚才在地铁上看到有人在画画，画得还挺像的。",
        "amphion": "我刚才在地铁上看到有人在画画，画得还挺像的。",
        "amphion_tag": {"zh": "无额外 prompt", "en": "no extra prompt"},
        "baselines": [
            {"name": "Qwen3-ASR-1.7B", "fair": True, "text": "我刚才在地铁上的时候，在画画，画的还挺像。"},
            {"name": "Seed 2.0 Lite", "fair": True, "text": "我刚才在地铁上闻到有人在画画，画得还挺香。"},
        ],
        "insight": {
            "zh": "Seed 把「看到/像」变成「闻到/香」，语义错误非常直观；Qwen3-ASR 同时漏掉主语信息。",
            "en": "Seed turns 看到/像 into 闻到/香; Qwen3-ASR also drops the subject.",
        },
    },
    {
        "id": "VITW-EN-1",
        "scenario": "degradation",
        "lang": "en",
        "featured": True,
        "protocol": "fair",
        "degradation": "echo",
        "title": {
            "zh": "回声：狗咬坏了旧玩具",
            "en": "Echo: the dog chewed the old toys",
        },
        "duration_sec": 4.680,
        "source_id": "vitw_04569_real_en_echo",
        "audio_slots": [
            {"role": "audio", "src": vitw_audio("VITW-EN-1"), "label": {"zh": "退化音频", "en": "Degraded audio"}}
        ],
        "ref": "The dog needs a new toy because he has chewed up all of his old ones.",
        "amphion": "The dog needs a new toy because he has chewed up all of his old ones.",
        "amphion_tag": {"zh": "无额外 prompt", "en": "no extra prompt"},
        "baselines": [
            {"name": "Qwen3-ASR-1.7B", "fair": True, "text": "The dog needs a new toy because it chewed up all of its bones."},
            {"name": "Seed 2.0 Lite", "fair": True, "text": "The dog needs a new toy because it's chewed up all of its old ones."},
        ],
        "insight": {
            "zh": "Amphion 保留 he / his / old ones；两个对照都发生代词或名词替换。",
            "en": "Amphion keeps he / his / old ones; both baselines swap pronouns or nouns.",
        },
    },
    {
        "id": "VITW-EN-2",
        "scenario": "degradation",
        "lang": "en",
        "featured": True,
        "protocol": "fair",
        "degradation": "echo",
        "title": {
            "zh": "回声：红绿灯坏了",
            "en": "Echo: the traffic light was broken",
        },
        "duration_sec": 5.400,
        "source_id": "vitw_04526_real_en_echo",
        "audio_slots": [
            {"role": "audio", "src": vitw_audio("VITW-EN-2"), "label": {"zh": "退化音频", "en": "Degraded audio"}}
        ],
        "ref": "The traffic light was broken so everyone was confused about who had the right of way.",
        "amphion": "The traffic light was broken so everyone was confused about who had the right of way.",
        "amphion_tag": {"zh": "无额外 prompt", "en": "no extra prompt"},
        "baselines": [
            {"name": "Qwen3-ASR-1.7B", "fair": True, "text": "The traffic was wrong, so everyone was confused about who had the right and where."},
            {"name": "Seed 2.0 Lite", "fair": True, "text": "The traffic was slow so everyone was confused about who had the right of way."},
        ],
        "insight": {
            "zh": "两个对照都把关键事件 traffic light was broken 改写成新语义；Qwen 还把 right of way 听成 right and where。",
            "en": "Both baselines rewrite the event (broken light → wrong/slow traffic); Qwen also splits right of way.",
        },
    },
    {
        "id": "VITW-ZH-3",
        "scenario": "degradation",
        "lang": "zh",
        "featured": True,
        "protocol": "fair",
        "degradation": "recording coloration",
        "title": {
            "zh": "录音染色：推销保险电话",
            "en": "Recording coloration: insurance sales call",
        },
        "duration_sec": 7.440,
        "source_id": "vitw_04182_real_zh_recording",
        "audio_slots": [
            {"role": "audio", "src": vitw_audio("VITW-ZH-3"), "label": {"zh": "退化音频", "en": "Degraded audio"}}
        ],
        "ref": "刚才那个推销电话说是推销保险的，我说不需要。",
        "amphion": "刚才那个推销电话说是推销保险的，我说不需要。",
        "amphion_tag": {"zh": "无额外 prompt", "en": "no extra prompt"},
        "baselines": [
            {"name": "Qwen3-ASR-1.7B", "fair": True, "text": "刚才那个电话，说是推销保险，我说不需要。"},
            {"name": "Seed 2.0 Lite", "fair": True, "text": "刚才那个，这通电话，说是推销保险，我说不需要。"},
            {"name": "Fun-ASR-Realtime", "fair": True, "text": "和变化。不需要。"},
        ],
        "insight": {
            "zh": "Qwen 和 Seed 漏掉或替换了「推销电话」；百炼几乎丢失整句，Amphion 完整恢复。",
            "en": "Qwen and Seed drop or rewrite 推销电话; Fun-ASR nearly collapses; Amphion is complete.",
        },
    },
    {
        "id": "VITW-EN-3",
        "scenario": "degradation",
        "lang": "en",
        "featured": True,
        "protocol": "fair",
        "degradation": "recording coloration",
        "title": {
            "zh": "录音染色：航班延误",
            "en": "Recording coloration: delayed flight",
        },
        "duration_sec": 6.880,
        "source_id": "vitw_04851_real_en_recording",
        "audio_slots": [
            {"role": "audio", "src": vitw_audio("VITW-EN-3"), "label": {"zh": "退化音频", "en": "Degraded audio"}}
        ],
        "ref": "The flight was delayed by two hours, so we had to wait at the airport for a long time.",
        "amphion": "The flight was delayed by two hours, so we had to wait at the airport for a long time.",
        "amphion_tag": {"zh": "无额外 prompt", "en": "no extra prompt"},
        "baselines": [
            {"name": "Qwen3-ASR-1.7B", "fair": True, "text": ""},
            {"name": "Seed 2.0 Lite", "fair": True, "text": "Our flight was delayed by two hours, so we had to wait at the airport for a long time."},
        ],
        "insight": {
            "zh": "同一段录音染色上，Qwen 没有产生转写；Amphion 完整恢复。Seed 仅把 The 改为 Our，作为健康对照。",
            "en": "Qwen emits an empty transcript on the same clip; Amphion is complete. Seed only swaps The → Our, as a healthy control.",
        },
    },
    # —— Whisper ——
    {
        "id": "WHSP-ZH-1",
        "scenario": "whisper",
        "lang": "zh",
        "featured": True,
        "protocol": "fair",
        "title": {
            "zh": "采菊东篱下",
            "en": "Picking chrysanthemums by the eastern fence",
        },
        "duration_sec": 4.440,
        "source_id": "whisperear_lgu_whsp_00210",
        "audio_slots": [
            {"role": "audio", "src": whsp_audio("WHSP-ZH-1"), "label": {"zh": "耳语音频", "en": "Whispered audio"}}
        ],
        "ref": "采菊东篱下，悠然见南山。",
        "amphion": "采菊东篱下，悠然见南山。",
        "amphion_tag": {"zh": "无 whisper-specific prompt", "en": "no whisper-specific prompt"},
        "baselines": [
            {"name": "Qwen3-ASR-1.7B", "fair": True, "text": "采菊东篱下，悠然见南山。"},
            {"name": "FireRed-ASR2-LLM", "fair": True, "text": "在去动力下悠然见南山"},
            {"name": "Fun-ASR-Nano-2512", "fair": True, "text": "在驱动力下，悠然见南山。"},
            {"name": "GLM-ASR-Nano-2512", "fair": True, "text": "在驱动力下，悠然见南山"},
            {"name": "Kimi-Audio-7B-Instruct", "fair": True, "text": "在曲动力下悠然见南山"},
            {"name": "MiniCPM-o 2.6", "fair": True, "text": "在驱动力下，悠然见南山。"},
            {"name": "MOSS-Audio-4B-Instruct", "fair": True, "text": "在曲动里下游染剑南山"},
            {"name": "Step-Audio 2 mini", "fair": True, "text": "在曲中，你下悠然见南山。"},
            {"name": "Whisper-large-v3", "fair": True, "text": "在驱动力下悠然见南山"},
        ],
        "insight": {
            "zh": "除 Qwen3-ASR 外，八个对照都把名句前半听成「在…动力下」一类高频组合。",
            "en": "Except Qwen3-ASR, eight baselines map the first half to a high-frequency 在…动力下 pattern.",
        },
    },
    {
        "id": "WHSP-ZH-2",
        "scenario": "whisper",
        "lang": "zh",
        "featured": True,
        "protocol": "fair",
        "title": {
            "zh": "力拔山兮气盖世",
            "en": "Strength to uproot mountains",
        },
        "duration_sec": 6.120,
        "source_id": "whisperear_lgu_whsp_00269",
        "audio_slots": [
            {"role": "audio", "src": whsp_audio("WHSP-ZH-2"), "label": {"zh": "耳语音频", "en": "Whispered audio"}}
        ],
        "ref": "力拔山兮气盖世，时不利兮骓不逝。",
        "amphion": "力拔山兮气盖世，时不利兮骓不逝。",
        "amphion_tag": {"zh": "无 whisper-specific prompt", "en": "no whisper-specific prompt"},
        "baselines": [
            {"name": "Fun-ASR-Nano-2512", "fair": True, "text": "力拔山兮气盖世，时不利兮骓不逝。"},
            {"name": "Qwen3-ASR-1.7B", "fair": True, "text": "力拔山兮气盖世，时不利兮骓不逝。"},
            {"name": "FireRed-ASR2-LLM", "fair": True, "text": "力拔山兮气盖世时不利兮骓不至"},
            {"name": "GLM-ASR-Nano-2512", "fair": True, "text": "李拔身兮其盖世，世不离兮追不至。"},
            {"name": "Kimi-Audio-7B-Instruct", "fair": True, "text": "力拔山兮气盖世时不力兮骓不逝"},
            {"name": "MiniCPM-o 2.6", "fair": True, "text": "篱笆山西起，盖石石不离西，追不止。"},
            {"name": "MOSS-Audio-4B-Instruct", "fair": True, "text": "利马神兮既开时，时不利兮骓不逝。"},
            {"name": "Step-Audio 2 mini", "fair": True, "text": "立马山西乞丐时，誓不离席，追不止。"},
            {"name": "Whisper-large-v3", "fair": True, "text": "离把身习即开始,誓不离习,追不知。"},
        ],
        "insight": {
            "zh": "耳语条件下的文言同音字；多数对照表面流畅，语义已偏。",
            "en": "Classical homophones under whisper; most baselines stay fluent but drift in meaning.",
        },
    },
    {
        "id": "WHSP-EN-1",
        "scenario": "whisper",
        "lang": "en",
        "featured": True,
        "protocol": "fair",
        "title": {
            "zh": "Hindu ideology",
            "en": "Hindu ideology",
        },
        "duration_sec": 4.365,
        "source_id": "whisperear_wtimit_whsp_00138",
        "audio_slots": [
            {"role": "audio", "src": whsp_audio("WHSP-EN-1"), "label": {"zh": "耳语音频", "en": "Whispered audio"}}
        ],
        "ref": "Does Hindu ideology honor cows?",
        "amphion": "Does Hindu ideology honor cows?",
        "amphion_tag": {"zh": "无 whisper-specific prompt", "en": "no whisper-specific prompt"},
        "baselines": [
            {"name": "FireRed-ASR2-LLM", "fair": True, "text": "dashing through the snow"},
            {"name": "Fun-ASR-Nano-2512", "fair": True, "text": "Does Hindu ideology on account."},
            {"name": "GLM-ASR-Nano-2512", "fair": True, "text": "Doesn't do ideology on the count."},
            {"name": "Kimi-Audio-7B-Instruct", "fair": True, "text": "Doesnt do ideology on the counts."},
            {"name": "MiniCPM-o 2.6", "fair": True, "text": "Doesn't do ideology on account"},
            {"name": "MOSS-Audio-4B-Instruct", "fair": True, "text": "Dust into ideology on accounts."},
            {"name": "Qwen3-ASR-1.7B", "fair": True, "text": "Does into ideology, on accounts."},
            {"name": "Step-Audio 2 mini", "fair": True, "text": "Doesn't do ideology on accounts."},
            {"name": "Whisper-large-v3", "fair": True, "text": "Cuts into ideology on accounts."},
            {"name": "Fun-ASR-Realtime", "fair": True, "text": "Doesn't do ideology on the couch."},
        ],
        "insight": {
            "zh": "加入百炼后十个对照全部错误，且错误集中在相似发音组合；Amphion 唯一完整正确。",
            "en": "Ten baselines all fail, clustering on similar phonetic patterns; Amphion is the only complete match.",
        },
    },
    {
        "id": "WHSP-EN-2",
        "scenario": "whisper",
        "lang": "en",
        "featured": True,
        "protocol": "fair",
        "title": {
            "zh": "Connoisseur / shellfish",
            "en": "Connoisseur / shellfish",
        },
        "duration_sec": 4.616,
        "source_id": "whisperear_wtimit_whsp_00413",
        "audio_slots": [
            {"role": "audio", "src": whsp_audio("WHSP-EN-2"), "label": {"zh": "耳语音频", "en": "Whispered audio"}}
        ],
        "ref": "A connoisseur will enjoy this shellfish dish.",
        "amphion": "A connoisseur will enjoy this shellfish dish.",
        "amphion_tag": {"zh": "无 whisper-specific prompt", "en": "no whisper-specific prompt"},
        "baselines": [
            {"name": "FireRed-ASR2-LLM", "fair": True, "text": "a connoisseur would have tried this shellfish dish"},
            {"name": "Fun-ASR-Nano-2512", "fair": True, "text": "Accordingly, the survey judged this selfish decision."},
            {"name": "GLM-ASR-Nano-2512", "fair": True, "text": "A colleague of mine tried this shark fish dish."},
            {"name": "Kimi-Audio-7B-Instruct", "fair": True, "text": "A colleague served a giant dish of shellfish dish."},
            {"name": "MiniCPM-o 2.6", "fair": True, "text": "According to Sophia, I tried this shellfish dish."},
            {"name": "MOSS-Audio-4B-Instruct", "fair": True, "text": "I call myself a childish selfish dish."},
            {"name": "Qwen3-ASR-1.7B", "fair": True, "text": "At Connie's house, I tried this shellfish dish."},
            {"name": "Step-Audio 2 mini", "fair": True, "text": "A coney sofa adorned this shellfish dish."},
            {"name": "Whisper-large-v3", "fair": True, "text": "I got myself a giant shellfish dish."},
        ],
        "insight": {
            "zh": "长难词和整句结构同时正确；九个对照均至少有一处实质错误。",
            "en": "Both the rare word and the full syntax are correct; every baseline has at least one material error.",
        },
    },
    {
        "id": "WHSP-ZH-3",
        "scenario": "whisper",
        "lang": "zh",
        "featured": True,
        "protocol": "fair",
        "title": {
            "zh": "天上七颗星，地上七块饼",
            "en": "Seven stars above, seven cakes below",
        },
        "duration_sec": 4.920,
        "source_id": "whisperear_lgu_whsp_00116",
        "audio_slots": [
            {"role": "audio", "src": whsp_audio("WHSP-ZH-3"), "label": {"zh": "耳语音频", "en": "Whispered audio"}}
        ],
        "ref": "天上七颗星，地上七块饼。",
        "amphion": "天上七颗星，地上七块饼。",
        "amphion_tag": {"zh": "无 whisper-specific prompt", "en": "no whisper-specific prompt"},
        "baselines": [
            {"name": "FireRed-ASR2-LLM", "fair": True, "text": "天上七颗星地上七块屏"},
            {"name": "Fun-ASR-Nano-2512", "fair": True, "text": "天上几颗星地上几块冰"},
            {"name": "GLM-ASR-Nano-2512", "fair": True, "text": "天上七颗星，地上七块冰"},
            {"name": "Kimi-Audio-7B-Instruct", "fair": True, "text": "天上几颗星，地上几块冰。"},
            {"name": "MiniCPM-o 2.6", "fair": True, "text": "天上几颗星，地上几块饼。"},
            {"name": "MOSS-Audio-4B-Instruct", "fair": True, "text": "天上七颗星地上七块冰"},
            {"name": "Qwen3-ASR-1.7B", "fair": True, "text": "天上几颗星，地上几块冰。"},
            {"name": "Step-Audio 2 mini", "fair": True, "text": "天上几颗星，地上几块冰。"},
            {"name": "Whisper-large-v3", "fair": True, "text": "天上起顆星地上起怪病"},
        ],
        "insight": {
            "zh": "九个对照全部至少错一个关键词，错误集中在「七/几」与「饼/冰/屏/病」。",
            "en": "All nine baselines miss at least one keyword, clustering on 七/几 and 饼/冰/屏/病.",
        },
    },
    {
        "id": "WHSP-EN-3",
        "scenario": "whisper",
        "lang": "en",
        "featured": True,
        "protocol": "fair",
        "title": {
            "zh": "Curiosity / mediocrity",
            "en": "Curiosity / mediocrity",
        },
        "duration_sec": 3.822,
        "source_id": "whisperear_wtimit_whsp_00371",
        "audio_slots": [
            {"role": "audio", "src": whsp_audio("WHSP-EN-3"), "label": {"zh": "耳语音频", "en": "Whispered audio"}}
        ],
        "ref": "Curiosity and mediocrity seldom coexist.",
        "amphion": "Curiosity and mediocrity seldom coexist.",
        "amphion_tag": {"zh": "无 whisper-specific prompt", "en": "no whisper-specific prompt"},
        "baselines": [
            {"name": "FireRed-ASR2-LLM", "fair": True, "text": "curabitur metus arcu dictum sodales elit"},
            {"name": "Fun-ASR-Nano-2512", "fair": True, "text": "Curiosity made your car the same complex."},
            {"name": "GLM-ASR-Nano-2512", "fair": True, "text": "Kira stamina to create the sound of existence."},
            {"name": "Kimi-Audio-7B-Instruct", "fair": True, "text": "Curiosity and mediocrity seem to coexist."},
            {"name": "MiniCPM-o 2.6", "fair": True, "text": "Curiosity got the better of me"},
            {"name": "MOSS-Audio-4B-Instruct", "fair": True, "text": "Curas de amigurumi, zentum coexist."},
            {"name": "Qwen3-ASR-1.7B", "fair": True, "text": "Kurasteam video card the Samsung Coexes."},
            {"name": "Step-Audio 2 mini", "fair": True, "text": "Curas stam midu gare ti sadam koxis."},
            {"name": "Whisper-large-v3", "fair": True, "text": "Kyra's team will be recording the sound of coexist."},
        ],
        "insight": {
            "zh": "九个对照全错；多数把两个低频抽象词改写成表面流畅的近音短语。Amphion 是唯一完整保留五词结构的模型。",
            "en": "All nine baselines fail; most rewrite two rare abstract words into fluent near-homophones. Amphion is the only five-word match.",
        },
    },
]

HW_TERMS = {
    "HW-FAIR-ZH-1": ["格里斯基尔兴县", "上奥地利州", "奥地利", "豪斯鲁克地区埃舍瑙"],
    "HW-FAIR-EN-1": ["Northampton", "Rockingham", "Wellingborough", "Lilbourne", "Barnwell"],
    "HW-FAIR-EN-2": ["Chi passa per 'sta strada", "Azzaiolo", "William Byrd"],
    "HW-FAIR-ZH-2": ["山虎", "钟世民", "中国共产党", "中山虎", "四川涪陵", "钟善辅"],
    "HW-FAIR-EN-3": ["Wizkids", "HeroClix", "Amazing Spider-Man", "Demogoblin"],
    "HW-LIMIT-EN-1": ["Dukes Highway", "Adelaide–Wolseley"],
}


def main() -> None:
    for case in CASES:
        if case["id"] in HW_TERMS:
            case["hotwords"] = hotword_block(case["id"], HW_TERMS[case["id"]])
            case["highlights"] = HW_TERMS[case["id"]]
        elif case["scenario"] == "target_speaker":
            case["highlights"] = []
        else:
            case["highlights"] = []

    payload = {
        "meta": {
            "model": "AmphionASR",
            "scale": "1.7B",
            "title": "Personalized Context-Aware Speech Recognition",
            "team": "Amphion Team",
            "date": "2026-07-28",
            "audio_status": "placeholder",
            "audio_note": {
                "zh": "音频文件稍后放入对应目录即可自动显示播放器，无需改页面代码。",
                "en": "Drop audio files into the matching folders later; players appear automatically.",
            },
            "case_count": len(CASES),
        },
        "cases": CASES,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {OUT} ({len(CASES)} cases)")


if __name__ == "__main__":
    main()
