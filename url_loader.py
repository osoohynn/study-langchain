# WebBaseLoader의 임포트 경로를 최신 권장 경로로 수정합니다.
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://comgo.dev/articles/20")

data = loader.load()
print(data[0].page_content)
