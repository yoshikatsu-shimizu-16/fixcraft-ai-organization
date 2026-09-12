---
name: fixcraft-orchestrator
description: FixCraftの全AI組織を統括する。morning-sales、build-proposal、evening-pdcaでは必ず使う。
---
# FixCraft Orchestrator
`.agent/AGENTS.md`を読み、Knowledge/Stateを確認してから実行する。

morning-sales: `sales-scout` → `competitive-intelligence` → `lead-qualifier` → `sales-director` → `bid-strategist` → Gate 1。

build-proposal: Gate 1承認済みのみ、`solution-architect` → 必要時`prototype-engineer` → 種別レビュー → `technical-quality-lead` → Gate 2 → 必要時`refactor-engineer` → `proposal-writer` → `sales-director` → Gate 3。WordPressはセキュリティ、HP/LPはデザインレビュー必須。

evening-pdca: 結果収集 → `competitive-intelligence` → `improvement-lead` → KPI更新 → Playbook/標準ルール候補。

単価・案件種別・リスクで不要なSkillを呼ばない。勝ち筋がない案件は開発しない。
