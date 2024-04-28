# -*- coding: utf-8 -*-
from langchain_openai import ChatOpenAI
from langchain_core.tools import Tool
from langchain.agents import create_openai_tools_agent, AgentExecutor
from langchain import hub
from langchain.pydantic_v1 import BaseModel, Field
import requests


def multiply(first_int: int, second_int: int) -> int:
    """Multiply two integers together."""
    return first_int * second_int


class MultiplyInput(BaseModel):
    first_int: int = Field(description='第一个数字')
    second_int: int = Field(description='第二个数字')


def analysis():
    "获取中国移动实时流量信息"
    fake_data = {"operateUserId": 1000511, "beginDate": "", "endDate": "", "createDeptIds": ["1"],
                 "createDeptLevels": ["1"],
                 "taskName": ""}
    headers = {}
    resp = requests.post(url="http://192.168.0.156/platform-service/sms-dangerRecord/dangerRecordStatAnalysis",
                         json=fake_data, cookies={''})
    return resp.text


tools = [
    Tool(
        name="multiply",
        func=multiply,
        description="A tool that returns Multiply two integers together.",
        args_schema=MultiplyInput,
        # coroutine=aget_prime,
    ),
    Tool.from_function(
        func=analysis,
        name="analysis",
        description="当需要获取中国移动实时流量数据，可以使用此工具",
        # args_schema=CalculatorInput,
        # coroutine=llm_math_chain.arun,
    ),
]

model = ChatOpenAI(
    streaming=True,
    verbose=True,
    callbacks=[],
    openai_api_key="EMPTY",
    openai_api_base='http://127.0.0.1:20000/v1',
    model_name='Qwen1.5-7B-Chat',
    temperature=0.1,
    max_tokens=None,
    # openai_proxy=config.get("openai_proxy"),
)

# model.bind_tools([multiply],tool_choice="multiply")
prompt = hub.pull("hwchase17/openai-tools-agent")
agent = create_openai_tools_agent(llm=model, tools=tools, prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True,return_intermediate_steps=True)
# agent_executor.invoke(
#     {
#         "input": "Take 3 to the fifth power and multiply that by the sum of twelve and three, then square the whole result"
#     }
# )
while 1 :
    query = input('enter query:\n')
    agent_executor.invoke({
        "input": query
    })
