from typing import List
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

split_prompt = ChatPromptTemplate.from_template("""
You are an assistant that breaks down complex analytical questions into atomic sub-questions.

Input: "{query}"

Output: A Python list of sub-questions. Be precise and do not merge concepts. 
Use this exact format:
[
  "First sub-question.",
  "Second sub-question."
]
""")

def split_into_subqueries(user_input: str) -> List[str]:
    chain = split_prompt | llm | StrOutputParser()
    raw = chain.invoke({"query": user_input})
    try:
        return eval(raw.strip())
    except Exception:
        return [user_input]