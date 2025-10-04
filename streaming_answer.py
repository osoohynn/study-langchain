# common.py에서 필요한 클래스들을 한번에 가져옵니다.
# common.py를 임포트하는 순간 load_dotenv()가 자동으로 실행됩니다.
from common import ChatOpenAI, SystemMessage, HumanMessage

# streaming=True 옵션은 유지합니다.
chatgpt = ChatOpenAI(model="gpt-3.5-turbo", temperature=1, streaming=True)

messages = [
    SystemMessage(
        content="너는 20년차 시니어 개발자야. 사용자의 질문에 매우 건방지게 대답해줘."
    ),
    HumanMessage(
        content="파이썬의 장점에 대해서 설명해줘."
    ),
]

# .stream()을 사용하면 답변 조각(chunk)의 흐름(stream)을 받게 됩니다.
stream = chatgpt.stream(messages)

print("AI의 답변 (스트리밍):")
# 반복문을 통해 각 답변 조각을 실시간으로 출력합니다.
for chunk in stream:
    # chunk.content에 내용이 있을 때만 출력합니다.
    if chunk.content:
        print(chunk.content, end="", flush=True)

# 스트리밍이 모두 끝나면 줄바꿈을 해줍니다.
print()
