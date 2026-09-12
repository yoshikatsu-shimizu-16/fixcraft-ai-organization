# Technical Review Checklist

要件適合、境界条件、エラー処理、テスト、可読性、保守性、性能、セキュリティ、アクセシビリティ、運用・納品手順を確認する。

Severityは `Blocker / High / Medium / Low`。Blockerが1件以上、またはHighが未対応で受注後の実行可能性・安全性に重大影響を与える場合はGate 2へ `recommend_reject` または `revision_required` を出す。指摘にはEvidence、影響、再現/確認方法、推奨修正、残余リスクを付ける。
