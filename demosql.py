import sys
from dotenv import load_dotenv
from langchain import OpenAI, SQLDatabase, SQLDatabaseChain

load_dotenv() 

db = SQLDatabase.from_uri("sqlite:///datasources/chinook.db")
llm = OpenAI(temperature=0, verbose=True)
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

query = sys.argv[1]
db_chain.run(query)
