import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")
response = llm.invoke("Xin chào, bạn có thể trả lời bằng tiếng Việt không?")
print("✅ API hoạt động! Response:")
print(response.content)
