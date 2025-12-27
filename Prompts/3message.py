from langchain_core.messages import SystemMessage,AIMessage,HumanMessage

from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()


model = ChatGoogleGenerativeAI(
    model="models/gemini-flash-latest",
)

message=[
  SystemMessage(content = 'you are a helpful assistant'),
  HumanMessage(content='Tell me about langChain')
]

result = model. invoke(message)
message.append(AIMessage(content=result.content))
print(message)