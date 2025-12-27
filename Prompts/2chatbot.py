from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(
    model="models/gemini-flash-latest",
)

chat_history =[
  SystemMessage(content = 'you are a helpful assistant')
]

while True:
  user_input=input("You: ")
  chat_history.append(HumanMessage(content=user_input))
  if(user_input == 'exit'):
    break
  result=model.invoke(chat_history)
  chat_history.append(AIMessage(content=result.content))
  print("AI : ",result.content)

print(chat_history)

# Rem jb vi hmlog chatbot bnayenge  to SystemMessage,AIMessage,HumanMessage ka use krke hi bnayenge.