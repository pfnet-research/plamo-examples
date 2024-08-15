import datetime

import requests
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryBufferMemory
from langchain_core.messages import BaseMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain_openai.chat_models.base import _convert_message_to_dict
from loguru import logger
from openai import BadRequestError

JST = datetime.timezone(datetime.timedelta(hours=9))
current_time_jst = datetime.datetime.now(JST)

BASE_URL = "https://platform.preferredai.jp/api/completion/v1"
MODEL_NAME = "plamo-beta"


class Plamo(ChatOpenAI):

    def get_num_tokens_from_messages(self, messages: list[BaseMessage]) -> int:
        num_tokens = 0
        messages_dict = [_convert_message_to_dict(m) for m in messages]
        for message in messages_dict:
            for key, value in message.items():
                if isinstance(value, list):
                    for val in value:
                        if isinstance(val, str) or val["type"] == "text":
                            text = val["text"] if isinstance(val, dict) else val
                            ret = requests.post(
                                url=BASE_URL,
                                json={
                                    "model": MODEL_NAME,
                                    "prompt": text,
                                },
                            )
                            num_tokens += ret.json()["count"]
                        else:
                            raise ValueError(f"Unrecognized content block type\n\n{val}")
                elif not value:
                    continue
                else:
                    num_tokens += len(value)
        return num_tokens


llm = Plamo(
    base_url=BASE_URL,
    model=MODEL_NAME,
    streaming=False,
    verbose=True,
    max_tokens=1000,
    temperature=0.7,
)

prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(
            f"今日は{current_time_jst.strftime('%Y年%m月%d日')}です。"
            "あなたはとてもカジュアルな言葉遣いで話す、ユーザの友人です。"
            "どんな言葉にも親身になりつつ、少し冗談を交えて、親しげに返事をしてください。"
            "返答は、できるだけ短い文章にしてください。"
            "過去の会話も覚えているので、会話の流れを忘れないようにしてください。\n"
            "Do not hallucinate."
        ),
        MessagesPlaceholder(variable_name="history"),
        HumanMessagePromptTemplate.from_template("{input}"),
    ]
)


memory = ConversationSummaryBufferMemory(
    llm=llm,
    return_messages=True,
    max_token_limit=3000,
)
conversation = ConversationChain(
    llm=llm,
    prompt=prompt,
    verbose=False,
    memory=memory,
)

while True:
    user_input = input("User: ")
    if user_input == "exit":
        break

    if user_input == "/reset":
        conversation.memory.chat_memory.clear()
        conversation.memory.moving_summary_buffer = ""
        response = {
            "response": ("今まで覚えた全てを、忘れるね。" "（´・ω・`）.;:…（´・ω...:.;::..（´・;::: .:.;: ｻﾗｻﾗ..")
        }
    else:
        while True:
            try:
                response = conversation.invoke(user_input)
                break
            except BadRequestError as e:
                logger.error(e)
                n_messages = len(conversation.memory.chat_memory.messages)
                pruned_memory = conversation.memory.chat_memory.messages[: n_messages // 2]
                conversation.memory.moving_summary_buffer = conversation.memory.predict_new_summary(
                    pruned_memory, conversation.memory.moving_summary_buffer
                )
                logger.info(f"summary_buffer: {conversation.memory.moving_summary_buffer}")
                latest_half_history = conversation.memory.chat_memory.messages[-n_messages // 2 :]
                conversation.memory.chat_memory.clear()
                conversation.memory.chat_memory.add_messages(latest_half_history)
                logger.info(f"Pruned memory to {len(conversation.memory.chat_memory.messages)} messages")
    print("PLaMo:", response["response"])
