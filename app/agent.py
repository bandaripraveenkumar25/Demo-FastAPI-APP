from app.schemas import CreateContactInput
from app.tools import create_contact
import json
import re

def simple_planner(message: str):
    """
    Very basic planner:
    Detects intent to create contact.
    """
    if "create contact" in message.lower():
        return "create_contact"
    return "unknown"

def extract_contact_info(message: str):
    """
    Simple extraction (replace with LLM in real system)
    """
    email_match = re.search(r'[\w\.-]+@[\w\.-]+', message)
    name_match = re.search(r'name is (\w+)', message.lower())

    name = name_match.group(1).capitalize() if name_match else "Unknown"
    email = email_match.group(0) if email_match else "unknown@email.com"

    return CreateContactInput(name=name, email=email)

def run_agent(message: str):
    intent = simple_planner(message)

    if intent == "create_contact":
        data = extract_contact_info(message)
        result = create_contact(data.name, data.email)
        return {
            "action": "create_contact",
            "result": result
        }

    return {
        "action": "none",
        "result": "No valid action detected."
    }