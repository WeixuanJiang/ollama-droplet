from flask import Flask, request, jsonify, Response
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain_core.output_parsers import StrOutputParser
import os
import logging
logging.basicConfig(level=logging.DEBUG)


app = Flask(__name__)

# Initialize LangChain components
parser = StrOutputParser()
template = """Question: {question}

Answer: Let's think step by step."""
prompt = ChatPromptTemplate.from_template(template)
model = OllamaLLM(model="nemotron-mini",base_url=os.getenv("OLLAMA_BASE_URL"))
chain = prompt | model | parser

def generate_stream_response(question):
    # Stream chunks from the chain in real-time
    for chunk in chain.stream({"question": question}):
        yield chunk + " "  # Add a newline after each chunk for better readability

@app.route('/ask', methods=['GET'])
def ask():
    app.logger.debug("Debug information")
    question = request.args.get('question')
    if not question:
        return jsonify({"error": "Question parameter is required"}), 400
    
    # Return the generator as a streaming response
    return Response(generate_stream_response(question), content_type='text/plain')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
