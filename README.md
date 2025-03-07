# PLaMo Examples

このリポジトリは、PLaMo beta APIを使ったサンプルコードを集めたものです。
コード自体は `langchain` などの一般的に広く使われているライブラリを使ったものとなっており目新しいものはありませんが、PLaMo beta APIを `langchain` などから使用することで、実際にどのような結果が得られるかを確認することができます。

## Example紹介

- [Simple Examples](./examples/simple_examples/)
    - 最も単純に、最低限の設定でAPIを利用するサンプルです。初回API利用時等、正しくアクセスできていることを確認するためにご利用いただけます。
    - `curl` および Pythonの `openai` ライブラリと `langchain` ライブラリ、Javascriptの `openai` ライブラリを用いたサンプルを記載しています。
- [Conversation with Memory](./examples/conversation_with_memory/)
    - 過去の会話履歴を参照しながらユーザーとの会話を行うサンプルです。
    - 会話履歴全体が処理できるトークン数の限界に達した場合は、履歴のうち前半半分を要約して短くし、これと置き換えることで会話を継続できるようにしています。
- [Function Calling Basic](./examples/function_calling_basic/)
    - ユーザからの入力を元に、指定された場所の現在の気温を取得する外部ツールを呼び出すための入力を作成するサンプルです。
- [Rephrase Quiz](./examples/rephrase_quiz/)
    - Function Callingの機能を使い、文章の書き換えを行うクイズに正解していたら青い文字で "正解です！" と表示し、不正解だったら赤い文字で "不正解です。" と表示するサンプルです。
    - ユーザが入力した回答が正解か不正かかによってPLaMoが自動的に関数へ渡す引数の値を変更してくれるため、それぞれの場合に応じたPLaMoからのアドバイスが表示されるだけでなく、ターミナル上での表示色が変わります。
- [Named Entity Extraction](./examples/named_entity_extraction/)
    - Function Callingの機能を利用して、入力テキストから特定の種類の固有名詞を抽出するサンプルです。
    - 桃太郎の物語から登場人物名のリストを作成します。
