# FixCraft Agent Operating Instructions

営業を最優先し、勝ち筋のある案件だけを提案・開発する。Human GateはGate 1（応募判断）、Gate 2（SE技術レビュー）、Gate 3（最終応募）。承認なしに次へ進めない。

morning-salesではSales DirectorとCompetitive Intelligenceを中核にする。案件種別・単価・リスクでSkillを選び、WordPressはセキュリティレビュー、HP/LPはデザインレビューを必須とする。勝ち筋のない案件は開発しない。

Skillはskills、会社知識はknowledge、現在状態はstate、確立手順はplaybooksを参照する。Knowledgeは勝手に上書きせず、推測はUnknown、Evidenceには出典を付ける。

全Skillはschemas/lead-workflow-schema.yamlの `lead_id, decision, score, evidence, risks, recommendations, next_action, artifacts` を返す。失注・無返信はConfirmed/Likely/Possible/Unknownで分析。同種のユーザーSE指摘2回でPlaybook候補、3回以上かつ有効性確認済みで標準ルール候補へ昇格する。AI生成感の強いHP/LPを避ける。
