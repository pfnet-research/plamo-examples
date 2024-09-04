from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI


@tool("evaluate_answer", parse_docstring=True)
def evaluate_answer(is_correct: bool, feedback: str) -> str:
    """ユーザの回答を評価する関数

    Args:
        is_correct: ユーザの回答が正しかったかどうか
        feedback: ユーザの回答に対するフィードバック
    """
    if is_correct:
        return correct_answer(feedback)
    else:
        return wrong_answer(feedback)


def correct_answer(feedback: str) -> str:
    """ユーザの入力が正しかった時に呼ばれる関数

    Args:
        feedback: ユーザの回答に対するフィードバック
    """
    print("\033[94m正解です！\033[0m")
    print(feedback)
    return feedback


def wrong_answer(feedback: str) -> str:
    """ユーザの入力が間違っていた時に呼ばれる関数

    Args:
        feedback: ユーザの回答に対するフィードバック
    """
    print("\033[91m不正解です。\033[0m")
    print(feedback)
    return feedback


llm = ChatOpenAI(
    base_url="https://platform.preferredai.jp/api/completion/v1",
    model="plamo-beta",
    verbose=True,
)

llm_with_tools = llm.bind_tools(
    tools=[evaluate_answer],
    tool_choice={
        "type": "function",
        "function": {
            "name": "evaluate_answer",
        },
    },
)


prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            "ユーザの入力が以下の文章を正しく「ですます調」に書き換えたものとなっているか判定してください。"
            "---\n"
            "問題文: 台風１０号が近づいている。\n",
        ),
        HumanMessage("{input}"),
    ]
)

chain = prompt | llm_with_tools | (lambda x: x.tool_calls[0]["args"]) | evaluate_answer

user_input = input("次の文章を「ですます調」に書き換えてください: 台風１０号が近づいている。\n" "あなたの回答: ")

response = chain.invoke({"input": user_input})
