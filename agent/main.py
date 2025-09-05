from fastapi import FastAPI
from pydantic import BaseModel
from langchain.llms import Ollama
from langchain.agents import initialize_agent, Tool
import requests

app = FastAPI()

def inventory_tool(rule_name: str):
    resp = requests.get(f"http://backend:8000/api/devices/filter/?rule={rule_name}")
    return resp.json()

def device_filter_tool(query: str):
    params = {}
    if "name:" in query:
        params["name"] = query.split("name:")[1].split()[0]
    if "location:" in query:
        params["location"] = query.split("location:")[1].split()[0]
    if "ip:" in query:
        params["ip"] = query.split("ip:")[1].split()[0]
    resp = requests.get("http://backend:8000/api/devices/filter/", params=params)
    return resp.json()

tools = [
    Tool(
        name="GetInventory",
        func=inventory_tool,
        description="Get inventory devices that support a given rule. Input is rule name."
    ),
    Tool(
        name="DeviceFilter",
        func=device_filter_tool,
        description="Filter devices by name, location, or IP. Input is a query like 'name:printer location:Mumbai ip:10.10'"
    ),
]

llm = Ollama(base_url="http://ollama:11434", model="llama3")
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):
    response = agent.run(req.message)
    return {"response": response}