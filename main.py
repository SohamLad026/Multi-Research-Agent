from src.tools.tools import web_search

from src.agent.agent import search_agent


# r = web_search.invoke("Tell the Salary of an agentic ai engineer and a freelancer")
# print(r)

response = search_agent().invoke({
    'messages': [{'role': 'user', 'content': 'Search for LangChain agents'}]
})

# 3. Access the assistant's reply
print(response['messages'][-1].content)