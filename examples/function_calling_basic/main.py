import os

from openai import OpenAI

client = OpenAI(
    base_url="https://api.platform.preferredai.jp/v1",
    api_key=os.environ["PLAMO_API_KEY"],
)

function = dict(
    name="get_current_weather",
    description="与えられた場所の現在の気温を返す",
    parameters=dict(
        type="object",
        properties=dict(
            location=dict(type="string", description="町の名前や地域の名前。例: 札幌市、北海道"),
            unit=dict(type="string", enum=["celsius", "fahrenheit"]),
        ),
        required=["location"],
    ),
)

tools = [dict(type="function", function=function)]

user_input = "今日の東京の気温は？"


result = client.chat.completions.create(
    model="plamo-2.0-prime",
    messages=[
        {"role": "user", "content": user_input},
    ],
    max_tokens=32,
    temperature=0.1,
    top_p=0.9,
    n=1,
    tools=tools,
    tool_choice={"type": "function", "function": {"name": "get_current_weather"}},
)

print(f"User input: {user_input}")
print(result.choices[0].message.tool_calls[0].function.arguments)
