from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

template = PromptTemplate(
    input_variables=["question"],
    template="What is {question}?"
)

prompt = template.format(question="React JS")

response = llm.invoke(prompt)

print(response.content)