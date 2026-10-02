# 共通市場探索

## 適用範囲と方針

すべてのスケジュールと手動実行でこの手順を読む。実行時刻やmodeが変わっても探索原則は共通とする。月20,000円、現金化、完了件数、評価獲得の優先順位はoperating-constraints.yamlに従う。短時間の小粒案件を積極対象とし、技術実績にならないことだけで除外しない。

morning-salesは探索全体を行う。ほかのmodeで新規候補を探す場合も同じ探索全体を使い、元のmodeへ直接混ぜずGate 1で止める。build-proposalとapply-approvedでは対象案件の現在の募集状態を再確認する。client-followupは返信と結果をEvidenceで更新する。evening-pdcaは探索ログと結果を照合して媒体別KPIを集計する。受注済み案件の募集終了を失注と扱わない。

## 媒体とレーン

market-sources.yamlのenabled媒体を確認し、candidate媒体の探索経路も調べる。候補媒体は募集への応募、専門家への個別紹介、出品して待つ販売を区別する。出品サービスを募集中案件として数えない。登録、プロフィール送信、問い合わせ、応募は探索に含めず、既存のHuman Gateと権限に従う。

search-keywords.mdの全レーンを対象とする。開発・WordPress、AI/LLM評価、開発者向け技術評価・利用評価実験、Web/アプリ/ソフトのユーザーテスト、AIサービスのモニター・ヒアリング、エンジニア属性インタビュー、一般モニター・インタビュー、データ入力・調査・転記を独立して記録する。既存のSNS運用と業務自動化も継続する。

## 実行順序

1. 媒体内の新着・募集中一覧を掲載日時順に巡回する。確認できた一覧URL、並び順、ページ数または項目数を記録する。
2. カテゴリ一覧を巡回し、各レーンの確認範囲を記録する。
3. 媒体内のキーワード検索で補完する。検索エンジンとsite:検索は取りこぼし検出に限る。検索結果の断片やメール配信時点の情報だけで応募可能と判断しない。
4. 個別案件ページまたは認証済みの案件詳細で現在応募可能か確認する。日時、募集表示、締切、応募条件、応募数、募集人数、報酬、推定総時間、発注者実績、外部誘導をEvidenceで記録する。時間には環境設定、事前準備、面談、回答、納品を含める。
5. 終了・期限切れを採点とGate 1から除外し、rejection_reasonを残す。不明な案件はneeds_more_evidenceとして保留し、応募可能な候補に含めない。既存LeadはState Machineで許可されたexpired等への更新候補を出す。受注済み等の履歴は保持する。
6. State Machineのdedupe規則で既存Leadと照合する。重複は既存IDへ紐付け、初回発見日時を保持してlast_seen_atを更新する。別媒体の同一募集はcross_source_duplicate_ofを記録し、候補・集計の二重計上を防ぐ。
7. competitive-intelligenceが競合・発注者・受注者を分析する。観測できない情報はUnknownとし、終了案件の受注者調査は候補探索と分ける。
8. lead-qualifierがLead採点、bid-strategistがBid Strategyを作る。
9. sales-directorが営業情報を統合し、Human Gate 1へ判断材料を渡して停止する。

一覧機能のない紹介型媒体では、新着紹介と利用可能な募集一覧を確認する。カテゴリ機能がない場合も理由を記録する。アクセス不能や時間上限で残った範囲はblockedまたは未確認とし、検索エンジンで代替して巡回完了と報告しない。0件も記録する。

## 探索ログとState

各runのログはstate/discovery/<run_id>.yamlに保存する。discovery-template.yamlのentry_fieldsを各entries行の雛形として使い、一覧の巡回と個別案件確認を別の行で記録する。検索回数、確認件数、除外件数、重複件数、採用件数、探索時間を実測で残す。同じ案件の再観測を新規発見数に加えない。

Leadの追加項目はlead-workflow-schema.yamlとlead-template.yamlに従う。sourceはplatform、categoryはprimary_category、discovered_atはfirst_seen_atと同じ意味で扱う。既存ファイルでは旧項目を読み、追加項目の欠落はUnknown/nullとする。矛盾があればEvidenceを確認して修正候補を出す。posted_atを発見日時で代用しない。

applied/replied/won/lostはEvidenceで確認した最初のイベント日時とする。未確認はnullであり、未発生と断定しない。現在statusとは別に保持し、返信後失注や受注後の実作業を追えるようにする。actual_minutesは実作業時間、actual_revenueは実現した円収益、ratingは評価値・尺度・媒体・確認日時を記録する。契約金額や受取見込を実収益に加えない。

## 媒体別比較

metrics-template.yamlのsource_metric_fieldsを各source_metrics行の雛形として使う。同じ発見期間の重複排除済みLeadをコホートとして、集計日時も記録する。探索ログのsourceとLead/Application/Outcomeをlead_idで結び、媒体とカテゴリ別に母数、Unknown件数、未決着件数を併記する。

応募率は応募済みユニークLead数/応募可能なユニークLead数、返信率は返信済み/応募済み、受注率は受注済み/応募済みとする。探索効率は応募可能Lead数/探索時間、実収益/探索時間、契約金額/探索時間を分けて出す。分母0や時間未計測はnullとする。少数標本や未決着の多い媒体を早期に切らない。毎日から週次への変更は比較結果に基づく提案とし、外部スケジュールを自動変更しない。

## スケジュールの接続

リポジトリには時刻・cron定義がない。外部スケジュールは毎回最新のAGENTS.mdから起動し、modeを渡す。Skillを直接実行する場合も共通ルールを読む。古いプロンプトに検索エンジン起点や2媒体限定の記述があれば、この手順へ更新する。時刻と既存mode名、Human Gate 1/2/3は変更しない。
