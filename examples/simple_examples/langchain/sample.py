import os

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url=f"https://platform.preferredai.jp/api/completion/v1",
    model="plamo-2.0-prime",
    api_key=os.environ["PLAMO_API_KEY"],
    # other params...,
)

messages = [
    {"role": "system", "content": "あなたは学校の先生です"},
    {"role": "user", "content": "二次方程式の解の公式を端的に教えてください"},
]

print(llm.invoke(messages).content)
