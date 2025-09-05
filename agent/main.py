from fastapi import FastAPI
from pydantic import BaseModel
from langgraph.graph import StateGraph, END
from langchain.llms.ollama import Ollama
from langchain.tools import tool
import requests

# --- Define Tools ---
@tool
def get_inventory(rule_name: str):
    """Get devices supporting a given rule."""
    resp = requests.get(f"http://backend:8000/api/devices/filter/?rule={rule_name}")
    return resp.json()

@tool
def filter_devices(name: str = None, location: str = None, ip: str = None):
    """Filter devices by name, location, or IP."""
    params = {}
    if name: params["name"] = name
    if location: params["location"] = location
    if ip: params["ip"] = ip
    resp = requests.get("http://backend:8000/api/devices/filter/", params=params)
    return resp.json()

@tool
def execute_rule(device_id: int, rule_name: str):
    """Execute a rule on a device."""
    resp = requests.post(f"http://backend:8000/api/devices/{device_id}/execute/", data={"rule": rule_name})
    return resp.json()

# --- User interaction simulation ---
def ask_user_for_filter(state):
    # Simulate asking user for filter criteria
    if not state.get("filter_criteria"):
        state["next_action"] = "Please provide filter criteria (name, location, ip):"
        return state, "wait_for_user_filter"
    else:
        return state, "filter_devices"

def wait_for_user_filter(state):
    # Wait for user input; in real app, integrate with frontend/chat
    if state.get("filter_criteria"):
        return state, "filter_devices"
    else:
        state["next_action"] = "Awaiting filter criteria..."
        return state, "wait_for_user_filter"

def ask_user_to_select(state):
    devices = state.get("filtered_devices", [])
    if len(devices) == 1:
        state["selected_device"] = devices[0]
        return state, "execute_rule"
    elif len(devices) > 1 and not state.get("selected_device"):
        # Ask user to select from device list
        state["next_action"] = f"Please select device by ID from: {devices}"
        return state, "wait_for_user_selection"
    elif state.get("selected_device"):
        return state, "execute_rule"
    else:
        state["next_action"] = "No devices found. Please try different filter criteria."
        return state, END

def wait_for_user_selection(state):
    if state.get("selected_device"):
        return state, "execute_rule"
    else:
        state["next_action"] = "Awaiting device selection..."
        return state, "wait_for_user_selection"

def report_results(state):
    result = state.get("result")
    state["next_action"] = f"Execution result: {result}"
    return state, END

# --- Graph Nodes ---
def parse_command(state):
    rule_name = state.get("rule_name")
    if not rule_name:
        state["next_action"] = "Please specify a rule to run (e.g., R1):"
        return state, "wait_for_rule"
    return state, "get_inventory"

def wait_for_rule(state):
    if state.get("rule_name"):
        return state, "get_inventory"
    else:
        state["next_action"] = "Awaiting rule name..."
        return state, "wait_for_rule"

def inventory_step(state):
    devices = get_inventory(state["rule_name"])
    state["devices"] = devices
    return state, "ask_user_for_filter"

def filter_step(state):
    criteria = state.get("filter_criteria", {})
    filtered = filter_devices(**criteria)
    state["filtered_devices"] = filtered
    return state, "ask_user_to_select"

def execute_step(state):
    selected = state["selected_device"]
    result = execute_rule(selected["id"], state["rule_name"])
    state["result"] = result
    return state, "report_results"

# --- Build Graph ---
graph = StateGraph()
graph.add_node("parse_command", parse_command)
graph.add_node("wait_for_rule", wait_for_rule)
graph.add_node("get_inventory", inventory_step)
graph.add_node("ask_user_for_filter", ask_user_for_filter)
graph.add_node("wait_for_user_filter", wait_for_user_filter)
graph.add_node("filter_devices", filter_step)
graph.add_node("ask_user_to_select", ask_user_to_select)
graph.add_node("wait_for_user_selection", wait_for_user_selection)
graph.add_node("execute_rule", execute_step)
graph.add_node("report_results", report_results)

graph.add_edge("parse_command", "wait_for_rule")
graph.add_edge("wait_for_rule", "get_inventory")
graph.add_edge("get_inventory", "ask_user_for_filter")
graph.add_edge("ask_user_for_filter", "wait_for_user_filter")
graph.add_edge("wait_for_user_filter", "filter_devices")
graph.add_edge("filter_devices", "ask_user_to_select")
graph.add_edge("ask_user_to_select", "wait_for_user_selection")
graph.add_edge("wait_for_user_selection", "execute_rule")
graph.add_edge("execute_rule", "report_results")

graph.set_entry_point("parse_command")
graph.set_end("report_results")

app = graph.compile()

# --- FastAPI Integration ---
api = FastAPI()

class ChatRequest(BaseModel):
    rule_name: str = None
    filter_criteria: dict = None
    selected_device: dict = None

@api.post("/chat")
def chat(req: ChatRequest):
    # Pass full state; in real app, manage session and user context
    state = req.dict()
    result = app(state)
    return result