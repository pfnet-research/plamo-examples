import os

from openai import OpenAI

client = OpenAI(
    base_url="https://api.platform.preferredai.jp/v1",
    api_key=os.environ["PLAMO_API_KEY"],
)

function_name = "introduce_charactors"
function = dict(
    name=function_name,
    description="与えられたキャラクターを紹介する",
    parameters=dict(
        type="object",
        properties=dict(
            name_list=dict(type="array", items=dict(type="string"), description="キャラクターの名前"),
        ),
        required=["name_list"],
    ),
)

user_input = (
    "桃から生まれた桃太郎は、おじいさんとおばあさんに大切に育てられ、立派に成長しました。"
    "桃太郎は、鬼ヶ島に行って鬼を退治することを決意し、犬、猿、きじを仲間にしました。"
    "そして、鬼たちをやっつけて、宝物を持って村に帰りました。桃太郎は英雄として称賛され、幸せに暮らしました。おしまい。"
)

result = client.chat.completions.create(
    model="plamo-2.0-prime",
    messages=[
        {"role": "user", "content": user_input},
    ],
    temperature=0.1,
    top_p=0.9,
    n=1,
    tools=[{"type": "function", "function": function}],
    tool_choice={"type": "function", "function": {"name": function_name}},
)

print(f"User input: {user_input}")
print(result.choices[0].message.tool_calls[0].function.arguments)
