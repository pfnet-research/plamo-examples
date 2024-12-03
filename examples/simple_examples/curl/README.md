curl example
========================

curlで最低限APIをリクエストするためのサンプル

## セットアップ

### curlのインストール

事前にターミナル上で [curl](https://curl.se/) コマンドを利用できるようにしておく

### 環境変数の設定

環境変数 `PLAMO_API_KEY` に、[PLaMo Prime](https://plamo.preferredai.jp/)で申し込みを行ない、入手したAPIキーをセットしてください。

```sh
export PLAMO_API_KEY=<YOUR_API_KEY>
```

## 実行

```bash
curl -w "\n" -H "Authorization: Bearer ${PLAMO_API_KEY}" -H "Content-Type: application/json" \
    -d '{"messages":[{"role": "system", "content": "あなたは学校の先生です"}, {"role": "user", "content": "二次方程式の解の公式を端的に教えてください"}], "model": "plamo-1.0-prime"}' \
    https://platform.preferredai.jp/api/completion/v1/chat/completions
```

## 実行結果例

```json
{"id":"chat-eb6da3a371c546c8a8c4629794328c5b","object":"chat.completion","created":1733220118,"model":"plamo-1.0-prime","choices":[{"index":0,"message":{"role":"assistant","content":"二次方程式の解の公式は以下の通りです。\n\n二次方程式の解の公式\n\n二次方程式の解の公式は、二次方程式の解を求めるための公式で、次のように表されます。\n\nx = (-b ± √(b² - 4ac)) / 2a\n\nここで、a、b、cは二次方程式の係数であり、xは解となります。\n\nこの公式を用いることで、二次方程式の解を簡単に求めることができます。\n\nなお、二次方程式とは、一般的にはax² + bx + c = 0の形式で表される方程式のことを指します。\n\n以上が、二次方程式の解の公式についての回答です。ご理解いただけましたでしょうか？他にも何か質問がありましたら、お気軽にお尋ねください。","tool_calls":[]},"logprobs":null,"finish_reason":"stop","stop_reason":null}],"usage":{"prompt_tokens":169,"total_tokens":394,"completion_tokens":225},"prompt_logprobs":null}
```
