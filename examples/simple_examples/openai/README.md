openai example
========================

Pythonの `openai` ライブラリを用いて、最低限APIをリクエストするためのサンプル

## セットアップ

### パッケージのインストール

```
pip install -r requirements.txt 
```

### 環境変数の設定

環境変数 `OPENAI_API_KEY` に、[PLaMo β版 トライアル](https://plamo.preferredai.jp/)で申し込みを行ない、入手したAPIキーをセットしてください。

```sh
export OPENAI_API_KEY=<YOUR_API_KEY>
```

## 実行

下記コマンドで `sample.py` を実行してください。

```
python sample.py
```

## 実行結果例

```
ChatCompletionMessage(content=' 二次方程式の解の公式は以下の通りです。\n\n\nax^2＋bx＋c=0の解は\n\nx=(-b±√(b^2-4ac))/(2a)\n\n\n二次方程式の解の公式の導き方を知りたい場合は、お気軽にお尋ねください。', refusal=None, role='assistant', function_call=None, tool_calls=[])
```
