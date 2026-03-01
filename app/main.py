from fastapi import FastAPI
from app.schemas import AgentRequest
from app.agent import run_agent

app = FastAPI(title="Agent Demo App")

@app.post("/agent")
def agent_endpoint(request: AgentRequest):
    response = run_agent(request.message)
    return response