from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
# from langchain_openai import ChatOpenAI
# model = ChatOpenAI()
from operator import itemgetter
prompt1 = ChatPromptTemplate.from_template(
    "generate a {attribute} color. Return the name of the color and nothing else:"
)
chain1 = prompt1 | StrOutputParser()
print(type(prompt1))
print(type(StrOutputParser()))

print(type(chain1))