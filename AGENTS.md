# FixCraft AI Organization - Root Operating Instructions

このリポジトリは、クラウドソーシング案件を「市場探索 → 競合調査 → 選別 → 提案設計 → 品質確認 → 応募 → 顧客対応 → 受注/失注 → 改善」まで一貫運用するAI組織の実行定義である。

## 起動時に必ず読む順序

1. この `AGENTS.md`
2. `.agent/AGENTS.md`
3. `.agent/skills/fixcraft-orchestrator/SKILL.md`
4. `.agent/knowledge/sales/market-sources.yaml`
5. `.agent/state/lead-state-machine.yaml`
6. 実行対象Skillが指定する Required Context

## 絶対ルール

- Human Gate 1/2/3 は人間だけが承認できる。AIは `recommend_approve` / `recommend_reject` まで。
- Gate 1 未承認の案件で試作・実装を開始しない。
- Gate 2 未承認の技術成果物を提案に採用しない。
- Gate 3 未承認の応募を送信しない。
- 競合、発注者、受注結果、実績を推測で埋めない。観測できない項目は `Unknown` とする。
- 「送信した」「応募した」「受注した」はEvidenceがある場合だけ記録する。
- 同一案件は `.agent/state/lead-state-machine.yaml` のdedupe規則で一意化し、毎回新規案件として扱わない。
- Knowledgeは事実・検証済み学習、Stateは進行中の事実、Playbookは再現可能な手順として分離する。
- `sources/` が存在する場合は同期済み参照資料としてread-onlyで扱う。

## 実行入口

原則として個別Skillを直接連鎖させず、`fixcraft-orchestrator` にmodeを渡して実行する。

- `morning-sales`: 市場探索、競合分析、案件評価、Gate 1候補作成
- `build-proposal`: Gate 1承認案件の解決設計、必要時試作、レビュー、Gate 2/3候補作成
- `apply-approved`: Gate 3承認済み案件の応募記録・提出支援
- `client-followup`: 返信、追加質問、条件交渉、受注/失注状態の整理
- `evening-pdca`: ファネル集計、失注/無返信分析、改善実験、Knowledge/Playbook候補作成

## 出力契約

全Skillは `.agent/schemas/skill-output-envelope-schema.yaml` の共通Envelopeを返し、Skill固有の結果を `result` に格納する。Leadの永続状態は `.agent/schemas/lead-workflow-schema.yaml` に従う。

## 変更品質

Skillを追加・変更したら `python .agent/scripts/validate-agent-organization.py` を実行する。Role、Mission、Inputs、Decision Rules、Output Contract、Handoff等の必須章が欠けるSkillは完成扱いにしない。
