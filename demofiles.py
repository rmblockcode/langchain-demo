import sys
from dotenv import load_dotenv

from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
load_dotenv() 

loader = TextLoader('datasources/files2.txt')
index = VectorstoreIndexCreator().from_loaders([loader])

query = sys.argv[1]
print(index.query(query))
