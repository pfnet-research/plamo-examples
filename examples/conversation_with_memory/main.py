import datetime
import os

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
MODEL_NAME = "plamo-1.0-prime"
API_KEY = os.environ["PLAMO_API_KEY"]


class PlamoWithTokenizer(ChatOpenAI):

    def _plamo_tokenize(self, messages: list[BaseMessage]) -> list[int]:
        messages = [_convert_message_to_dict(message) for message in messages]
        response = requests.post(
            url=f"{BASE_URL}/tokenize",
            json={
                "model": MODEL_NAME,
                "messages": messages,
                "add_special_tokens": True,
                "add_generation_prompt": True,
            },
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
            },
        )
        response.raise_for_status()
        return response.json()["count"]

    def get_num_tokens_from_messages(self, messages: list[BaseMessage]) -> int:
        if len(messages) == 0:
            return 0
        num_tokens = self._plamo_tokenize(messages)
        return num_tokens


llm = PlamoWithTokenizer(
    base_url=BASE_URL,
    model=MODEL_NAME,
    streaming=False,
    verbose=True,
    temperature=0.7,
    api_key=API_KEY,
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
    max_token_limit=2**14,
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
