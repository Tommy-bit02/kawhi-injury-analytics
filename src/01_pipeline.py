"""
=============================================================================
NBA Star Player Injury Analytics — Load Management, Recovery & Prevention
Kawhi Leonard & High-Value Players | 2018–2026
=============================================================================

STUDY METHODOLOGY & SPIRIT

This project was born from watching one of basketball's greatest players —
Kawhi Leonard — lose years of his prime to injury and the Clippers lose
multiple playoff runs as a result. It asks the hardest question in modern
NBA management: how do you protect your most valuable asset when the asset
is a human being?

Kawhi's story is not just about bad luck. It is about the collision of
elite competitive drive, organizational load management philosophy, and
the brutal physical demands of NBA basketball. His ACL tear in 2021 —
a franchise-altering moment — became the centerpiece of a league-wide
conversation about player safety, rest protocols, and what it truly
costs when a star misses games.

This study uses Kawhi as the cornerstone case study, then expands to
other stars whose injuries directly denied their teams playoff
opportunities — Durant's Achilles, Zion's foot, Simmons' back —
to build a framework for what organizations can do differently.

"The best ability is availability." — Unknown

METHODOLOGY:
  Step 1 — Injury Severity Scoring: Composite metric weighting games
            missed, recovery duration, and return-to-peak status
  Step 2 — Playoff Impact Analysis: Quantifying wins lost when stars miss
  Step 3 — Kawhi Career Timeline: Season-by-season availability study
  Step 4 — Rehab Protocol Analysis: Recovery rates by injury type
  Step 5 — Organizational Prevention Framework: Evidence-based strategies
  Step 6 — Future Odds Modeling: Probability of return to peak performance

CITATIONS:
  [1] NBA Injury Tracker — Basketball Reference (2018–2026)
  [2] Journal of Orthopaedic & Sports Physical Therapy — ACL Return-to-Sport
  [3] UCSF Sports Medicine — NBA Load Management Research (2024)
  [4] ESPN Analytics — Injury Impact on Playoff Probability (2025)
  [5] Second Spectrum — Player Tracking & Workload Data (2026)

⚠️  DISCLAIMER: Player injury and performance data is compiled from
    publicly available sources. Recovery projections are based on
    published medical research and population-level outcomes — NOT
    individual medical assessments. This is academic research only.
    Do not use for medical decisions. All player names used under
    fair use for analytical and educational purposes.
=============================================================================
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, GradientBoostingRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score, r2_score
import warnings
warnings.filterwarnings("ignore")

print("=" * 70)
print("  NBA STAR PLAYER INJURY ANALYTICS")
print("  Kawhi Leonard & High-Value Players | Load Management & Prevention")
print()
print("  'The best ability is availability.'")
print()
print("  ⚠️  Academic research only — not medical advice")
print("=" * 70)

injuries = pd.read_csv("data/star_player_injuries.csv")
rehab    = pd.read_csv("data/rehab_protocols.csv")
kawhi    = pd.read_csv("data/kawhi_timeline.csv")

print(f"\n✅ {len(injuries)} player-injury records | {injuries['player'].nunique()} players\n")

# =============================================================================
# MODULE 1 — KAWHI CAREER AVAILABILITY ANALYSIS
# =============================================================================
print("-" * 70)
print("  MODULE 1: KAWHI LEONARD — CAREER AVAILABILITY DEEP DIVE")
print("  The cost of losing a franchise player season after season")
print("-" * 70)

kawhi_active = kawhi[kawhi['games_played'] > 0]
kawhi_all    = kawhi.copy()
total_games  = kawhi_all['games_played'].sum()
total_missed = kawhi_all['games_missed'].sum()
playoff_runs_lost = kawhi_all[~kawhi_all['team_made_playoffs']]['season'].nunique()

print(f"\n  Kawhi Leonard Career Summary (2018–2026):")
print(f"  Total games played:      {total_games}")
print(f"  Total games missed:      {total_missed}")
print(f"  Availability rate:       {total_games/(total_games+total_missed)*100:.1f}%")
print(f"  Playoff runs denied:     {playoff_runs_lost} seasons")
print(f"  Peak scoring seasons:    {len(kawhi_active[kawhi_active['pts_avg']>24])}")

print(f"\n  Season-by-Season:")
print(f"  {'Season':<10} {'Team':<16} {'Games':>6} {'Missed':>7} {'PPG':>6}  Playoffs")
print("  " + "-" * 56)
for _, row in kawhi_all.iterrows():
    status = "✅ YES" if row['team_made_playoffs'] else "❌ NO"
    ppg    = f"{row['pts_avg']:.1f}" if row['pts_avg'] > 0 else "—"
    print(f"  {row['season']:<10} {row['team']:<16} {row['games_played']:>6} "
          f"{row['games_missed']:>7} {ppg:>6}  {status}")

kawhi.to_csv("outputs/kawhi_career_analysis.csv", index=False)

# =============================================================================
# MODULE 2 — INJURY SEVERITY SCORING
# =============================================================================
print("\n" + "-" * 70)
print("  MODULE 2: INJURY SEVERITY SCORES — ALL STAR PLAYERS")
print("  Composite: games missed (50%) + recovery (30%) + peak return (20%)")
print("-" * 70)

injuries_s = injuries.sort_values('severity_score', ascending=False)
print(f"\n  {'Player':<22} {'Injury':<28} {'G Miss':>7} {'Rcv Mo':>7} "
      f"{'To Peak':>8} {'Severity':>9}")
print("  " + "-" * 82)
for _, row in injuries_s.iterrows():
    peak = "✅" if row['returned_to_peak'] else "❌"
    print(f"  {row['player']:<22} {row['injury_type']:<28} "
          f"{row['games_missed']:>7} {row['recovery_months']:>7} "
          f"{peak:>8} {row['severity_score']:>9.3f}")

injuries.to_csv("outputs/injury_severity_scores.csv", index=False)

# =============================================================================
# MODULE 3 — PLAYOFF IMPACT ANALYSIS
# =============================================================================
print("\n" + "-" * 70)
print("  MODULE 3: PLAYOFF COST ANALYSIS")
print("  When stars go down — what do their teams lose?")
print("-" * 70)

playoff_cost = injuries[injuries['playoff_team_missed'] & (injuries['games_missed'] > 30)]
print(f"\n  {len(playoff_cost)} cases where star injury directly impacted playoff teams:\n")
for _, row in playoff_cost.iterrows():
    pct = row['games_pct_missed']
    print(f"  🏀 {row['player']} ({row['team']}, {row['season']})")
    print(f"     Missed {row['games_missed']} games ({pct:.0f}% of season) — "
          f"{row['injury_type']}")
    print(f"     Recovery: {row['recovery_months']} months | "
          f"Returned to peak: {'Yes' if row['returned_to_peak'] else 'No'}")
    print()

# =============================================================================
# MODULE 4 — REHAB PROTOCOL & PREVENTION FRAMEWORK
# =============================================================================
print("-" * 70)
print("  MODULE 4: REHABILITATION PROTOCOLS BY INJURY TYPE")
print("  What the science says about recovery and organizational prevention")
print("-" * 70)

print(f"\n  {'Injury Type':<22} {'Avg Recovery':>13} {'Return %':>9} "
      f"{'Recurrence%':>12} {'NBA Cases':>10}")
print("  " + "-" * 70)
for _, row in rehab.sort_values('avg_recovery_months', ascending=False).iterrows():
    print(f"  {row['injury_type']:<22} {row['avg_recovery_months']:>10} mo "
          f"{row['return_to_peak_pct']:>8}% "
          f"{row['recurrence_risk_pct']:>11}% "
          f"{row['nba_cases_2018_2026']:>10}")

print("\n  KEY ORGANIZATIONAL PREVENTION STRATEGIES:")
prevention = {
    'Load Management Protocol':   'GPS tracking, minutes caps, back-to-back restrictions',
    'Pre-Season Screening':       'Full-body MRI, movement analysis, biomechanical testing',
    'In-Season Workload Tracking':'Real-time exertion monitoring via wearables (Catapult)',
    'Court Surface Standards':    'Hardwood shock absorption, venue-specific protocols',
    'Mental Health Integration':  'Psychological load as injury risk factor (Ben Simmons)',
    'Nutrition & Recovery Staff': 'Sleep tracking, cryotherapy, individualized nutrition',
}
for strategy, detail in prevention.items():
    print(f"\n  ✅ {strategy}")
    print(f"     {detail}")

rehab.to_csv("outputs/rehab_protocols_analysis.csv", index=False)

# =============================================================================
# MODULE 5 — RETURN-TO-PEAK PREDICTION MODEL
# =============================================================================
print("\n" + "-" * 70)
print("  MODULE 5: ML MODEL — PREDICT RETURN TO PEAK PERFORMANCE")
print("-" * 70)

le = LabelEncoder()
injuries['injury_enc'] = le.fit_transform(injuries['injury_type'])
injuries['pos_enc']    = LabelEncoder().fit_transform(injuries['position'])

FEATS = ['games_missed','recovery_months','age_at_injury',
         'injury_enc','pos_enc','games_pct_missed']
X = injuries[FEATS]
y = injuries['returned_to_peak'].astype(int)

if len(X) > 8:
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=42)
    sc  = StandardScaler()
    lr  = LogisticRegression(random_state=42, max_iter=500)
    lr.fit(sc.fit_transform(X_tr), y_tr)
    acc = lr.score(sc.transform(X_te), y_te)
    print(f"\n  Logistic Regression — Return-to-Peak Predictor")
    print(f"  Accuracy: {acc:.3f} (small sample — directional only)")
else:
    print("\n  Sample too small for split — showing full-dataset coefficients")
    sc  = StandardScaler()
    lr  = LogisticRegression(random_state=42, max_iter=500)
    lr.fit(sc.fit_transform(X), y)

coefs = pd.Series(lr.coef_[0], index=FEATS).sort_values()
print("\n  Feature coefficients (negative = reduces return-to-peak odds):")
for feat, coef in coefs.items():
    direction = "↓ Risk" if coef < 0 else "↑ Helps"
    print(f"    {feat:<25} {coef:>8.4f}  {direction}")

# Kawhi 2026 prediction
kawhi_features = np.array([[82, 18, 33, 0, 2, 100.0]])
prob = lr.predict_proba(sc.transform(kawhi_features))[0][1]
print(f"\n  🏀 KAWHI LEONARD 2025-26 RETURN-TO-PEAK PROBABILITY:")
print(f"     Model estimate: {prob*100:.1f}%")
print(f"     Context: 3 knee-related injuries, age 33-34, 3+ years of heavy load")
print(f"     Medical consensus (ACL at age 30+): 55-65% return to pre-injury level")

pd.DataFrame({'feature': FEATS, 'coefficient': lr.coef_[0]}).to_csv(
    "outputs/return_to_peak_model.csv", index=False)

print("\n✅ Pipeline complete. Run 02_visualizations.py to generate charts.\n")
