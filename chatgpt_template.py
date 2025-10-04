from common import ChatOpenAI

from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

# ChatGPT 모델을 로드합니다.
chatgpt = ChatOpenAI(temperature=1)


template = """
너는 요리사야. 내가 가진 재료들을 갖고 만들 수 있는 요리를 추천하고, 그 요리의 레시피를 제시해줘.
내가 가진 재료는 아래와 같아.

<재료>
{재료}

"""

#ChatGPT에게 역할을 부여합니다.(위에서 정의한 Template 사용)
system_message_prompt = SystemMessagePromptTemplate.from_template(template)

#사용자가 입력할 매개변수 template을 선언합니다.
human_template = "{재료}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

#ChatPromptTemplate에 system message와 human message 템플릿을 삽입합니다.
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

#ChatGPT API에 ChatPromptTemplate을 입력할 때, human message의 매개변수인 '재료'를 할당하여 전달합니다.
#이와 같은 방식을 통해 ChatGPT는 ChatPromptTemplate의 구성요소인 system message와 human message를 전달받아, 대답 생성에 활용합니다.
answer = chatgpt(chat_prompt.format_prompt(재료="양파, 계란, 사과, 빵").to_messages())
print(answer.content)