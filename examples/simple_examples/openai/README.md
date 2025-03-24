openai example
========================

Pythonの `openai` ライブラリを用いて、最低限APIをリクエストするためのサンプル

## セットアップ

### パッケージのインストール

```
pip install -r requirements.txt 
```

### 環境変数の設定

環境変数 `PLAMO_API_KEY` に、[PLaMo Webサイト](https://plamo.preferredai.jp/)で申し込みを行ない、入手したAPIキーをセットしてください。

```sh
export PLAMO_API_KEY=<YOUR_API_KEY>
```

## 実行

下記コマンドで `sample.py` を実行してください。

```
python sample.py
```

## 実行結果例

```
ChatCompletionMessage(content='二次方程式の解の公式は、以下の通りです。\n\nx = (-b ± √(b^2 - 4ac)) / 2a\n\nこの公式は、二次方程式 ax^2 + bx + c = 0 の解を求めるために使用されます。a、b、c はそれぞれ定数であり、a が 0 でないことが前提です。\n\n解の公式の使い方は、まず a、b、c の値を特定し、それらを公式に代入します。そして、計算順序に従って、√(b^2 - 4ac) を求め、その結果を元の式に代入して、x の値を求めます。\n\nなお、√(b^2 - 4ac) の値が負の場合、解は存在しません。また、√(b^2 - 4ac) の値がゼロの場合、解は一つだけになります。\n\n以上が二次方程式の解の公式の概要です。詳細な説明や具体例については、必要に応じてお伝えいたします。', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=[])
```
