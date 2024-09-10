Function Calling
================

指定したJSON Schemaに適合するようにJSONを出力させるサンプルです。

「今日の東京の天気は？」というユーザの入力を元に、与えられた場所の今日の気温を返す

```
get_current_feather(location: string, unit: string)
```

のような関数を呼び出すための入力データを作成します。

## 使い方

まず、環境変数 `OPENAI_API_KEY` に、[PLaMo β版 トライアル](https://plamo.preferredai.jp/)で申し込みを行なって入手したAPIキーをセットしてください。

```sh
export OPENAI_API_KEY=<YOUR_API_KEY>
```

次に、必要なパッケージをインストールして、サンプルを実行します。

```sh
pip install -r requirements.txt

python main.py
```

### 実行例

```
User input: 今日の東京の天気は？
{ "location": "東京", "unit": "celsius" }
```
