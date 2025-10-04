# 이 파일은 공통으로 사용되는 모듈 임포트와 환경 변수 로딩을 담당합니다.

from dotenv import load_dotenv

# .env 파일이 있다면 환경 변수를 불러옵니다.
load_dotenv()

# 자주 사용되는 클래스들을 여기서 임포트하여 다른 파일에서 쉽게 가져다 쓸 수 있도록 합니다.
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain.prompts import PromptTemplate, ChatPromptTemplate