import os

from openai import OpenAI

client = OpenAI(
    base_url=f'https://platform.preferredai.jp/api/completion/v1',
    # other params...,
)

completion = client.chat.completions.create(
  model="plamo-beta",
  messages=[
    {"role": "system", "content": "あなたは学校の先生です"},
    {"role": "user", "content": "二次方程式の解の公式を端的に教えてください"},
  ]
)

print(completion.choices[0].message)