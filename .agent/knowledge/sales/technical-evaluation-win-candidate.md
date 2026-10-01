# Technical Evaluation / Tool Feedback - Win Candidate

## Status

- Evidence level: **Confirmed outcome + hypothesis for generalization**
- Standard rule: **No**
- Playbook status: **Candidate only**
- Validation target: 同種案件を追加で2〜4件応募し、返信率・受注率・実作業時間・実収益を比較する。

## Confirmed Win: CrowdWorks 13481213

2026-10-01、CrowdWorks案件「静的解析とLLMを融合したコードグラフ自動生成ツール（HCG）の利用評価実験」を受注。

Confirmed facts:

- 契約金額: 5,500円（税込）
- CrowdWorks画面上のワーカー受取見込: 4,290円
- 募集時の想定作業時間: 約2時間（環境設定込み）
- 募集人数: 10人
- 作業: HCGを導入し、Java / Python / JavaScriptコードを使って機能評価し、アンケート回答
- 要求スキル: Java / Python / JavaScriptの短いコード理解、Git、Python、Ollama、8GB以上のPC、CFG / AST / PDGの理解
- 作業完了期限: 2026-10-10
- 納品・検収前のため、actual revenueはまだ0円として扱う

Evidence:

- CrowdWorks公開案件: https://crowdworks.jp/public/jobs/13481213
- 2026-10-02にユーザーが契約詳細画面を提示

## Why This Lane May Fit

以下は今回1件の受注から得た**仮説**であり、まだ標準化しない。

- 実装そのものを納品するより、既存SEスキルを使って「理解・評価・フィードバック」するため仕様膨張リスクが小さい可能性がある。
- Java / Python / JavaScript、Git、ローカルLLM、静的解析など、一般モニターより技術条件が高いほど応募可能者が絞られ、SE経験が差別化になりやすい可能性がある。
- 1〜3時間程度・3,000〜10,000円程度・複数名募集・手順明確な評価実験は、第一段階の現金化と受注件数獲得に相性が良い可能性がある。
- コードレビュー、PoC評価、ベータテスト、技術アンケート、開発ツール評価、AI/LLM品質評価も隣接候補として探索価値がある。

## Priority Search Terms

- 利用評価実験
- 開発ツール 評価
- 技術評価 実験
- 研究実験 エンジニア
- エンジニア モニター
- 開発者 モニター
- 評価アンケート エンジニア
- AI ツール 評価
- LLM 評価
- 静的解析 評価
- コード分析 評価
- コードレビュー 技術評価
- PoC 評価
- ベータテスト エンジニア
- ユーザーテスト 開発ツール
- Git GitHub 評価
- Ollama ローカルLLM 評価
- Java Python JavaScript モニター

## Positive Signals

Gate 1で優先度を上げる候補:

- 想定1〜3時間程度
- 3,000〜10,000円以上
- 募集人数が複数
- 手順・完了条件・アンケート項目が明確
- Java / Python / JavaScript / Git / Linux / Docker / LLM等、既存SE経験と直接一致
- 実装納品より評価・検証が中心
- 発注者の評価・支払実績が確認できる

## Negative Signals

- 数十円〜数百円の一般アンケートのみ
- 「未経験者限定」など経験があることで条件外になる案件
- 外部サービスへの勧誘が主目的
- 作業時間・完了条件が不明
- 評価を名目に大規模な無料開発・修正を要求
- 長時間拘束、平日日中固定、継続前提で実質的に本業級
