from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain import OpenAI, SQLDatabase, SQLDatabaseChain

load_dotenv()
db = SQLDatabase.from_uri("sqlite:///datasources/chinook.db")

def query_db(query: str) -> str:
    llm = OpenAI(temperature=0, verbose=True)
    db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
    return db_chain.run(query)

def query_file(query: str) -> str:
    loader = TextLoader('datasources/file1.txt')
    index = VectorstoreIndexCreator().from_loaders([loader])
    return index.query(query)