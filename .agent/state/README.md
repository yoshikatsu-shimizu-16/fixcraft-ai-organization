# State

Stateには現在進行中の観測事実だけを置く。KnowledgeやPlaybookを直接上書きしない。

Leadは `.agent/schemas/lead-workflow-schema.yaml` と `lead-state-machine.yaml` に従い、`lead_id`, `platform`, `dedupe_key`, `first_seen_at`, `last_seen_at`, `status`, `next_action`, `evidence` を持つ。Human Gateの承認は承認者・日時・対象artifactを記録し、AI推測で埋めない。

再実行時は新規Leadを乱造せずdedupe_keyで既存Stateを更新する。status遷移はstate machineに存在する経路だけを使う。
