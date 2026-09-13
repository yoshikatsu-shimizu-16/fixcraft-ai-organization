# Search Keywords

## Search Categories

案件探索では、以下を独立カテゴリとして扱う。`AI自動化`や`SNS運用`を`業務自動化`の一語にまとめて探索完了としてはいけない。

### 1. AI / LLM / AI Automation

AI / 生成AI / ChatGPT / OpenAI / OpenAI API / GPT / Gemini / Claude / LLM / AIエージェント / Agent / RAG / ベクトル検索 / Embedding / LangChain / LangGraph / MCP / チャットボット / FAQ Bot / AI検索 / AI要約 / AI文章生成 / AI画像生成 / プロンプト / Prompt / OCR / ドキュメント解析 / ナレッジ検索 / AI導入 / AI連携 / AI自動化 / 生成AI自動化

### 2. SNS Operations / SNS Automation

SNS運用 / SNS運用代行 / SNS管理 / SNS投稿 / 投稿代行 / 投稿作成 / 投稿自動化 / 予約投稿 / コンテンツ作成 / コンテンツ企画 / SNS分析 / SNSマーケティング / SNS集客 / Threads / X / Twitter / Instagram / TikTok / Facebook / LinkedIn / YouTube / Buffer / Hootsuite / Meta Business Suite / RSS連携 / SNS API / 自動投稿 / 投稿スケジュール / KPI分析 / エンゲージメント分析

### 3. Business Automation / Integration

GAS / Google Apps Script / 業務自動化 / 効率化 / API連携 / Webhook / n8n / Make / Zapier / Slack連携 / Notion連携 / Gmail連携 / Google Sheets連携 / スプレッドシート自動化 / CSV処理 / データ収集 / スクレイピング / バッチ処理 / 定期実行 / ワークフロー自動化

### 4. WordPress / Web Repair

WordPress / WP / プラグイン / テーマ / 保守 / セキュリティ / バグ修正 / 復旧 / 403 / 500 / PHP / JavaScript / サーバー移行 / SSL / WAF / DNS / Cloudflare / 表示崩れ / 不具合修正

### 5. Web / App Development

React / TypeScript / Node.js / Next.js / NestJS / Java / Spring Boot / AWS / Lambda / API開発 / 管理画面 / Webアプリ / SaaS / バックエンド / フロントエンド / Firebase / Supabase

## Problem Words

修正 / 改善 / 復旧 / エラー / 不具合 / 自動化 / 効率化 / 移行 / 連携 / 保守 / 調査 / 急募 / スポット / 継続 / 導入 / 構築 / 代行 / 運用 / 改修 / 最適化 / 分析

## High-Intent Query Examples

各市場では単語一覧を眺めて終わらず、カテゴリごとに複数の検索Queryを実行する。

- `ChatGPT 自動化`
- `OpenAI API 連携`
- `生成AI 導入`
- `AIエージェント 開発`
- `RAG 構築`
- `AI チャットボット`
- `SNS運用 自動化`
- `SNS 投稿 自動化`
- `Threads 運用`
- `X 投稿 自動化`
- `Instagram 運用代行`
- `SNS コンテンツ作成`
- `GAS 自動化`
- `n8n 自動化`
- `API連携 自動化`
- `WordPress 修正`
- `WordPress 復旧`
- `React 改修`

## Mandatory Coverage Rule

各Runでは、enabledな各市場について最低でも次のカテゴリを確認する。

1. AI / LLM / AI Automation
2. SNS Operations / SNS Automation
3. Business Automation / Integration
4. WordPress / Web Repair
5. Web / App Development

各カテゴリで原則2つ以上のQueryを試す。市場側の検索仕様で不可能な場合は、その理由をEvidenceとして記録する。

特に `AI / LLM / AI Automation` と `SNS Operations / SNS Automation` は必須カテゴリとし、0件でも検索を省略してはいけない。

## Query Construction

基本は `課題語 + 技術語` または `業務カテゴリ + 自動化/運用/代行` とする。必要に応じて納期語・継続語を加える。単一検索語だけで探索完了とせず、enabledな各市場で複数Queryを試す。各Runで使用した市場・カテゴリ・検索語・取得件数をEvidenceとして残す。

価格だけを売りにする案件、要求が広すぎる案件、納期と予算が破綻した案件は収集しても優先度を下げる。除外はScoutではなくQualifier/Directorの責任とし、Scoutは重大なhard blockerだけ明示する。
