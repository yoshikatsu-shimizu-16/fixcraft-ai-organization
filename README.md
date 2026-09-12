# FixCraft AI Organization

クラウドソーシング営業を、案件探しだけで終わらせず「市場・競合調査 → 応募判断 → 差別化 → 必要最小限の試作 → 提案 → 応募 → 顧客対応 → 受注/失注 → 改善」まで回すAI組織です。

## 起動

Agentは `AGENTS.md` を最初に読み、そこから `.agent/AGENTS.md` と `fixcraft-orchestrator` に従います。

```text
このリポジトリの AGENTS.md を読み、FixCraft Orchestratorを起動してください。
mode: morning-sales
Human Gateで必ず停止し、Evidenceのない事実を作らないでください。
```

## 実行モード

- `morning-sales`: CrowdWorks/Lancers等の有効市場から候補収集、競合調査、採点、Gate 1候補
- `build-proposal`: Gate 1承認済み案件を設計・試作・レビューし、Gate 2/3候補へ
- `apply-approved`: Gate 3承認済み応募の提出支援と応募記録
- `client-followup`: 発注者返信、追加質問、交渉、クロージング
- `evening-pdca`: KPI、勝敗要因、競合変化、改善実験を更新

## 組織フロー

```text
Sales Scout
  -> Competitive Intelligence
  -> Lead Qualifier
  -> Sales Director
  -> Bid Strategist
  -> Human Gate 1
  -> Solution Architect
  -> Prototype Engineer (必要時のみ)
  -> Domain Reviewer (WordPress / Web Design 等)
  -> Technical Quality Lead
  -> Human Gate 2
  -> Refactor Engineer (必要時)
  -> Proposal Writer
  -> Sales Director
  -> Human Gate 3
  -> Application Manager
  -> Client Closing Manager
  -> Outcome Recorder
  -> Improvement Lead
  -> Knowledge / Playbook / Scoring 改善
```

## 重要ファイル

- `.agent/knowledge/sales/market-sources.yaml`: 探索対象市場と優先順位
- `.agent/knowledge/sales/lead-scoring.yaml`: 再現可能な採点基準
- `.agent/state/lead-state-machine.yaml`: 案件状態遷移とHuman Gate
- `.agent/schemas/skill-output-envelope-schema.yaml`: 全Skill共通出力
- `.agent/skill-contract-standard.md`: Skillの必須契約
- `.agent/scripts/validate-agent-organization.py`: Skill構造検証

## 検証

```bash
python .agent/scripts/validate-agent-organization.py
```

Skillの役割や責任境界が欠けた変更はCIで失敗します。
