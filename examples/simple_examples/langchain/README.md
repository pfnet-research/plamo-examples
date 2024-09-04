langchain example
========================

Pythonの `langchain` ライブラリを用いて、最低限APIをリクエストするためのサンプル

## セットアップ

### パッケージのインストール

```
pip install -r requirements.txt 
```

### 環境変数の設定

環境変数 `OPEAI_API_KEY` に、[PLaMo β版 トライアル](https://plamo.preferredai.jp/)で申し込みを行ない、入手したAPIキーをセットしてください。

```sh
export OPENAI_API_KEY=<YOUR_API_KEY>
```

## 実行

下記コマンドで `sample.py` を実行してください。

```
python sample.py
```

### 実行結果例

```
 二次方程式の解の公式は以下のとおりです。

二次方程式 ax^2 + bx + c = 0 の解は

x = [-b ± sqrt(b^2 - 4ac)] / (2a)

となります。

ここで、

・a, b, c は方程式の係数
・sqrt は平方根
・± はプラスマイナスの記号で、二通りの解を表します。

この公式は、二次方程式を解く際に広く利用されています。
```
