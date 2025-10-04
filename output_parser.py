from common import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List

# 1. Pydantic 모델을 사용하여 출력될 JSON의 구조를 정의합니다.
# 예를 들어, "recommendations"라는 키에 문자열 리스트가 담긴 형태입니다.
class Recommendations(BaseModel):
    recommendations: List[str] = Field(description="추천 목록")

# 2. JsonOutputParser를 생성하고, 위에서 정의한 Pydantic 모델을 알려줍니다.
parser = JsonOutputParser(pydantic_object=Recommendations)

# 3. 프롬프트를 수정하여 JSON 형식의 출력을 명확히 지시합니다.
#    parser.get_format_instructions()는 LLM에게 JSON 형식을 설명해주는 가이드입니다.
prompt = PromptTemplate(
    template="""{query}에 대한 답변을 다음 JSON 형식에 맞춰서 작성해줘.\n{format_instructions}
""",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# 최신 ChatOpenAI 모델을 사용합니다.
model = ChatOpenAI(temperature=0)

# 4. LCEL을 사용하여 프롬프트, 모델, 파서를 `|` 연산자로 연결합니다.
chain = prompt | model | parser

# 5. 체인을 실행하면, LLM의 답변이 자동으로 JSON으로 파싱됩니다.
response = chain.invoke({"query": "한국 영화 5개를 추천해줘"})

# 최종 결과는 파이썬 딕셔너리(dict) 형태입니다.
print("--- 출력 결과 ---")
print(response)
print("\n--- 결과 타입 ---")
print(type(response))
