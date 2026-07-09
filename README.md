# 🏀 NBA Star Player Injury Analytics
### Kawhi Leonard & High-Value Players | Load Management, Recovery & Prevention | 2018–2026

> ⚠️ **ACADEMIC RESEARCH DISCLAIMER:** Educational and portfolio purposes only. Data from Basketball Reference and published medical literature. Not medical advice.
>
> 🏀 **Personal Note:** Built around Kawhi Leonard — one of the greatest two-way players of his generation — whose career was repeatedly derailed by knee injuries while with the LA Clippers. Watching a generational talent lose years of his prime inspired this study.

---

## 📌 Overview

**Key finding:** Kawhi has a **25.6% career availability rate** (2018–2026) with **5 playoff runs denied**.

---

## 📊 Key Visualizations

### Chart 1 — Career Ceiling, Decline & Conditioning Protocols

![Ceiling and Conditioning](outputs/chart1_ceiling_conditioning.png)

- **Top:** Gold = projected 30 PPG ceiling. Red = actual — crashes to 0 in injured seasons
- **Middle:** Games missed across 12 star players — ✅ returned / ❌ did not
- **Bottom:** 5 conditioning protocols organizations must implement

---

### Chart 2 — Recovery Arcs, Return Probability & Recurrence Risk

![Recovery Arcs](outputs/chart2_recovery_arcs.png)

- **Top-left:** Kawhi vs Durant vs Curry pre/post injury — Durant & Curry returned, Kawhi has not
- **Top-right:** Kawhi 2026 return probability — 20% full peak / 35% partial / 45% limited
- **Bottom-left:** Recurrence risk pie by injury type
- **Bottom-center:** Monthly recovery progress arc
- **Bottom-right:** Conditioning effectiveness ranking

---

## 📈 Key Findings

| Season | Team | Played | Missed | PPG | Playoffs |
|--------|------|--------|--------|-----|---------|
| 2018-19 | Toronto | 60 | 22 | 26.6 | ✅ Won Championship |
| 2020-21 | Clippers | 52 | 30 | 24.8 | ✅ WCF |
| 2021-22 | Clippers | 0 | 82 | — | ❌ ACL tear |
| 2022-23 | Clippers | 0 | 82 | — | ❌ ACL rehab |
| 2023-24 | Clippers | 14 | 68 | 22.7 | ❌ Missed playoffs |
| 2024-25 | Clippers | 0 | 82 | — | ❌ Knee rehab |

**Kawhi 2026 Return Odds:** 20% full peak · 35% partial · 45% limited role

---

## 🏋️ Prevention Framework

1. **Strength & Conditioning** — Eccentric quad loading, single-leg stability
2. **Load Management** — GPS tracking, minutes caps, no back-to-backs
3. **Recovery** — Cryotherapy, 9+ hrs sleep, myofascial work
4. **Pre-Season Screening** — Full MRI, biomechanical scan
5. **Mental Health** — Sports psychologist, no pressure timelines

---

## 🚀 Setup

```bash
git clone https://github.com/Tommy-bit02/kawhi-injury-analytics.git
cd kawhi-injury-analytics
pip install -r requirements.txt
python src/01_pipeline.py
```

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C)
