from flask import Flask, request
from flask_cors import CORS
from lang_query import query_db, query_file

app = Flask(__name__)
CORS(app)

@app.route("/langchain-db", methods=['POST'])
def call_langchaindb():
    query = request.json.get('query')
    result = query_db(query)
    return {'result': result}

@app.route("/langchain-file", methods=['POST'])
def call_langchainfile():
    query = request.json.get('query')
    result = query_file(query)
    return {'result': result}