openai javascript example
========================

JavaScriptの [`openai` ライブラリ](https://github.com/openai/openai-node)を用いて、最低限APIをリクエストするためのサンプル

## セットアップ

### パッケージのインストール

```
npm install openai
```

### 環境変数の設定

環境変数 `PLAMO_API_KEY` に、[PLaMo Webサイト](https://plamo.preferredai.jp/)で申し込みを行ない、入手したAPIキーをセットしてください。

```sh
export PLAMO_API_KEY=<YOUR_API_KEY>
```

## 実行

下記コマンドで `sample.js` を実行してください。

```
node sample.js
```

## 実行結果例

```javascript
{
  role: 'assistant',
  content: '二次方程式の解の公式は次の通りです。\n' +
    '\n' +
    'x = (-b ± √(b^2 - 4ac)) / 2a\n' +
    '\n' +
    '二次方程式が ax^2 + bx + c = 0 の形式であるとき、この公式を使って解を求めることができます。\n' +
    '\n' +
    'a、b、cはそれぞれ二次方程式の係数であり、＋√(b^2 - 4ac)の部分は、判別式と呼ばれます。判別式の値によって、二次方程式の解の数が決まります。\n' +
    '\n' +
    '・判別式が0の場合、解は1つです。\n' +
    '・判別式が正の場合、解は2つです。\n' +
    '・判別式が負の場合、解はありません。(二次方程式に実数解がないということです。)\n' +
    '\n' +
    '以上のように、この公式は二次方程式を解くために非常に重要な公式となります。',
  tool_calls: []
}
```
