from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="models/gemini-flash-latest",  # ✅ exists in your account
    temperature=0.2
)

result = model.invoke("What is the capital of India?")
print(result.content)


# genai.configure(api_key=None)

# for m in genai.list_models():
#     print(m.name) check available models in my account