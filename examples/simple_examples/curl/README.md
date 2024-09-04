curl example
========================

curlで最低限APIをリクエストするためのサンプル

## セットアップ

### curlのインストール

事前にターミナル上で [curl](https://curl.se/) コマンドを利用できるようにしておく

### 環境変数の設定

環境変数 `API_KEY` に、[PLaMo β版 トライアル](https://plamo.preferredai.jp/)で申し込みを行ない、入手したAPIキーをセットしてください。

```sh
export API_KEY=<YOUR_API_KEY>
```

## 実行

```bash
curl -w "\n" -H "Authorization: Bearer ${API_KEY}" -H "Content-Type: application/json" \
    -d '{"messages":[{"role": "system", "content": "あなたは学校の先生です"},{"role": "user", "content": "二次方程式の解の公式を端的に教えてください"}], "model": "plamo-beta"}' \
    https://platform.preferredai.jp/api/completion/v1/chat/completions
```

## 実行結果例

```json
{"id":"chat-ab19098de4704cdc9556955c88047862","object":"chat.completion","created":1724991808,"model":"plamo-beta","choices":[{"index":0,"message":{"role":"assistant","content":" 二次方程式の解の公式は以下の通りです。\n\n\nax^2 + bx + c = 0 の場合、\n\n解 = (-b ± √(b^2 - 4ac)) / (2a)\n\n\nただし、√の中身がマイナスになる場合は、解は実数ではなく、虚数となります。\n\n\n例えば、x^2 - 5x + 6 = 0 の場合、\n\n解 = (5 ± √((-5)^2 - 4*1*6)) / (2*1)\n解 = (5 ± √(25 - 24)) / 2\n解 = (5 ± √1) / 2\n解 = (5 ± 1) / 2\n\n\nよって、解はx = 3、x = 2 となります。","tool_calls":[]},"logprobs":null,"finish_reason":"stop","stop_reason":null}],"usage":{"prompt_tokens":118,"total_tokens":344,"completion_tokens":226}}
```
