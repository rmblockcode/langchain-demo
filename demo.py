from dotenv import load_dotenv
from langchain.llms import OpenAI

load_dotenv()
llm = OpenAI(temperature=0.9)

res = llm.predict("What would be a good company name for a company that makes colorful socks?")
print(res)
