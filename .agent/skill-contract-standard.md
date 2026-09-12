# FixCraft Skill Contract Standard

すべての `.agent/skills/*/SKILL.md` は、役職名だけでなく「何を受け取り、何を判断し、どこまで責任を持ち、誰へ渡すか」を再現可能に定義する。

## 必須章

- `# Role`: 組織上の役割と権限
- `# Mission`: 成功条件
- `# Inputs`: 必要入力と入力不足時の扱い
- `# Required Context`: 必ず読むKnowledge/State/Playbook
- `# Responsibilities`: 自分が責任を持つ事項
- `# Non-responsibilities`: 他役割へ越権しない境界
- `# Procedure`: 順序付きの実行手順
- `# Decision Rules`: 再現可能な判定基準
- `# Output Contract`: 共通Envelopeの`result`内容
- `# Handoff`: 誰へ何を渡すか
- `# Stop Conditions`: 停止・エスカレーション条件

## 設計原則

RoleとMissionは別物とする。Roleは「誰か」、Missionは「何を達成するか」。Procedureだけで判断を曖昧にせず、Decision Rulesに数値・閾値・条件を可能な限り置く。SkillはHuman Gateを承認しない。Evidenceなしの事実を出力しない。複数案件を扱うSkillに単一Lead形式を強制しない。
