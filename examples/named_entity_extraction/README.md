Function Calling
================

Function Callingの機能を利用して、入力テキストから特定の種類の固有名詞を抽出するサンプルです。

ユーザが入力した桃太郎の物語を元に、登場人物の一覧を作成します。

## 使い方

まず、環境変数 `PLAMO_API_KEY` に、[PLaMo Prime](https://plamo.preferredai.jp/)で申し込みを行なっていただき入手したAPIキーをセットしてください。

```sh
export PLAMO_API_KEY=<YOUR_API_KEY>
```

次に、必要なパッケージをインストールして、サンプルを実行します。

```sh
pip install -r requirements.txt

python main.py
```

### 実行例

```
User input: 桃から生まれた桃太郎は、おじいさんとおばあさんに大切に育てられ、立派に成長しました。桃太郎は、鬼ヶ島に行って鬼を退治することを決意し、犬、猿、きじを仲間にしました。そして、鬼たちをやっつけて、宝物を持って村に帰りました。桃太郎は英雄として称賛され、幸せに暮らしました。おしまい。
{"name_list": ["桃太郎", "おじいさん", "おばあさん", "犬", "猿", "きじ", "鬼"]}
```
