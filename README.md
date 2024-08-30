# PLaMo Examples

このリポジトリは、PLaMo beta APIを使ったサンプルコードを集めたものです。
コード自体は `langchain` などの一般的に広く使われているライブラリを使ったものとなっており目新しいものはありませんが、PLaMo beta APIを `langchain` などから使用することで、実際にどのような結果が得られるかを確認することができます。

## Example紹介

- [Simple Examples](./examples/simaple_examples/)
    - 最も単純に、最低限の設定でAPIを利用するサンプルです。初回API利用時等、正しくアクセスできていることを確認するためにご利用いただけます。
    - `curl` および Pythonの `openai` ライブラリ、`langchain` ライブラリを用いたサンプルを記載しています。
- [Conversation with Memory](./examples/conversation_with_memory/)
    - 過去の会話履歴を参照しながらユーザーとの会話を行うサンプルです。
    - 会話履歴全体が処理できるトークン数の限界に達した場合は、履歴のうち前半半分を要約して短くし、これと置き換えることで会話を継続できるようにしています。
