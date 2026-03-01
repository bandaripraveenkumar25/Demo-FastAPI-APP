from pydantic import BaseModel

class CreateContactInput(BaseModel):
    name: str
    email: str

class AgentRequest(BaseModel):
    message: str