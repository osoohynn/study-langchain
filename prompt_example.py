from common import ChatOpenAI, HumanMessage
from langchain.prompts import PromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate

examples = [
  {
    "question": "아이유로 삼행시 만들어줘",
    "answer":
"""
아: 아이유는
이: 이런 강의를 들을 이
유: 유가 없다.
"""
  },

  {
    "question": "김민수로 삼행시 만들어줘",
    "answer":
"""
김: 김치는 맛있다
민: 민달팽이도 좋아하는 김치!
수: 수억을 줘도 김치는 내꺼!
"""
  }
]

example_prompt = PromptTemplate(input_variables=["question", "answer"], template="Question: {question}\n{answer}")

prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question: {input}",
    input_variables=["input"]
)

chatgpt = ChatOpenAI(temperature=1)

# LCEL (LangChain Expression Language)을 사용하여 프롬프트와 모델을 `|` 연산자로 연결합니다.
# 이것이 LangChain의 가장 최신이자 표준 방식입니다.
chain = prompt | chatgpt

# .invoke()를 사용하여 체인을 실행하고, 딕셔너리 형태로 input을 전달합니다.
response = chain.invoke({"input": "호날두로 삼행시 만들어줘"})

print(response.content)
