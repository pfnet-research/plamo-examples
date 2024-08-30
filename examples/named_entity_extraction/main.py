from openai import OpenAI
client = OpenAI(
    base_url="https://platform.preferredai.jp/api/completion/v1"
)

function = dict(
    name="introduce_charactors",
    description="与えられたキャラクターを紹介する",
    parameters=dict(
        type="object",
        properties=dict(
            name_list=dict(type="array", items=dict(type="string"), description="キャラクターの名前"),
        ),
        required=["name_list"],
    ),
)

tools = [
    dict(type="function", function=function)
]

user_input = (
    "桃から生まれた桃太郎は、おじいさんとおばあさんに大切に育てられ、立派に成長しました。"
    "桃太郎は、鬼ヶ島に行って鬼を退治することを決意し、犬、猿、きじを仲間にしました。"
    "そして、鬼たちをやっつけて、宝物を持って村に帰りました。桃太郎は英雄として称賛され、幸せに暮らしました。おしまい。"
)

result = client.chat.completions.create(
    model="plamo-beta",
    messages=[
        {"role": "system", "content": "introduce_charactors(name_list)は与えられたキャラクターを紹介する関数です。これを使って以下の物語の登場人物を紹介してください。"},
        {"role": "user", "content": user_input},
    ],
    temperature=0.1,
    top_p=0.9,
    n=1,
    tools=tools,
    tool_choice={
        "type": "function",
        "function": {
            "name": "introduce_charactors"
        }
    },
)

print(f"User input: {user_input}")
print(result.choices[0].message.tool_calls[0].function.arguments)
