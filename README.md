# 🚀 FastAPI Agent Demo App (Python).

A minimal AI Agent application built with:

- FastAPI
- Pydantic
- Modular project structure
- Simple Planner → Executor pattern

This project demonstrates how to structure a basic agent service using Python.

---

# 📁 Project Structure

```
agent_app/
│
├── app/
│   ├── __init__.py
│   ├── main.py        # FastAPI entrypoint
│   ├── agent.py       # Planner + Executor logic
│   ├── tools.py       # Tool implementations (Mock CRM)
│   └── schemas.py     # Pydantic models
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Requirements

- Python 3.9+
- pip
- virtual environment (recommended)

---

# 📄 requirements.txt

Create a file named `requirements.txt`:

```
fastapi
uvicorn
pydantic
```

---

# 🧭 Setup Instructions

## 1️⃣ Clone the Repository

```
git clone https://github.com/bandaripraveenkumar25/Demo-FastAPI-APP.git
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

Run from the project root directory:

```
uvicorn app.main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

# 🧪 API Testing

Open Swagger UI in your browser:

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

1. The user sends a message to the `/agent` endpoint.
2. The planner detects the intent.
3. The executor calls the appropriate tool.
4. The response is returned as structured JSON.

---

# 📜 License

MIT License

