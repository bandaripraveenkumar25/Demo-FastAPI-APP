# Demo-FastAPI Agent Demo App (Python).


# 🚀 FastAPI Agent Demo App (Production-Structured)

A minimal but production-structured AI Agent application built with:

- FastAPI
- Pydantic
- Modular architecture
- Planner → Executor pattern
- Typed tool schemas

This project demonstrates how to structure an agent system for real-world deployment instead of a simple chatbot loop.

---

# 📦 Features

- ✅ Clean modular architecture
- ✅ Planner → Executor pattern
- ✅ Typed tool schemas (Pydantic)
- ✅ Mock CRM tool
- ✅ FastAPI REST API
- ✅ Production-friendly folder layout

---

# 📁 Project Structure

```
agent_app/
│
├── app/
│   ├── __init__.py
│   ├── main.py        # FastAPI entrypoint
│   ├── agent.py       # Planner + Executor logic
│   ├── tools.py       # Tool implementations (CRM mock)
│   └── schemas.py     # Pydantic models
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Requirements

- Python 3.9+
- pip
- virtualenv (recommended)

---

# 📄 requirements.txt

Create a file named `requirements.txt`:

```
fastapi
uvicorn
pydantic
```

(Optional if adding LLM support later)
```
openai
langchain
langgraph
```

---

# 🧭 Setup Instructions

## 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/agent_app.git
cd agent_app
```

---

## 2️⃣ Create Virtual Environment

### Windows

```
python -m venv venv
venv\Scripts\activate
```

### Mac / Linux

```
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 4️⃣ Run the Application

Run from project root:

```
uvicorn app.main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

# 🧪 API Testing

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

Example request:

```json
{
  "message": "Create contact, name is John, email john@test.com"
}
```

Example response:

```json
{
  "action": "create_contact",
  "result": {
    "status": "success",
    "contact_id": "C12345",
    "name": "John",
    "email": "john@test.com"
  }
}
```

---

# 🧠 How It Works

### 1️⃣ Planner
Detects user intent (create contact)

### 2️⃣ Extractor
Parses structured data from message

### 3️⃣ Tool Executor
Calls mock CRM tool

### 4️⃣ FastAPI Layer
Exposes agent via REST endpoint

---

# 🏗 Architecture Pattern

```
Client
   ↓
FastAPI
   ↓
Agent (Planner → Executor)
   ↓
Tool Layer
   ↓
External Systems (CRM / ERP / APIs)
```

---

# 🔐 Production Upgrade Ideas

- Replace rule-based planner with LLM function-calling
- Add LangGraph orchestration
- Add policy engine (RBAC)
- Add audit logging
- Add retry + timeout handling
- Add evaluation test harness
- Dockerize for deployment
- Add CI/CD pipeline

---

# 🧑‍💻 Development Notes

Run server in development mode:

```
uvicorn app.main:app --reload
```

Production mode:

```
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

# 📌 Why This Structure?

This structure avoids:

❌ Monolithic single-file agents  
❌ Hardcoded logic in API layer  
❌ Unstructured tool execution  

Instead it follows:

✔ Separation of concerns  
✔ Typed tool contracts  
✔ Extensible orchestration layer  

---

# 📜 License

MIT License

---

# 🙌 Next Steps

You can evolve this into:

- Multi-agent orchestration
- Enterprise CRM integration
- Finance approval agent
- Governance + policy layer
- Production-grade AgentOps platform
