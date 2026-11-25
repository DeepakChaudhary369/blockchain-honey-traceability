# 🍯 Blockchain Honey Traceability Assurance Agent

An intelligent honey-product traceability and assurance system that follows product records across the supply chain, checks traceability compliance, analyzes supply-chain information, and coordinates multiple agents through a workflow orchestrator.

The system is designed to demonstrate **Traceability, Compliance, and Supply-Chain Analysis agents**, persistent product-state management, RAG-based traceability rules, workflow chaining, failure handling and recovery, telemetry, authorization, and secure deployment.

---

## 📌 Project Overview

Honey products pass through multiple stages such as harvesting, collection, processing, packaging, distribution, and delivery.

Maintaining reliable information about these stages is important for understanding:

- Where the product originated
- Which actors handled the product
- Where each supply-chain event occurred
- When each event occurred
- Whether required traceability information is available
- The current state of the product

This project provides an API-based assurance system that combines multiple specialized agents into a single workflow.

---

## 🎯 Objectives

The system aims to:

1. Track honey products throughout the supply chain.
2. Maintain persistent product-state information.
3. Retrieve and check traceability rules.
4. Perform compliance checking.
5. Analyze supply-chain events.
6. Chain multiple agents into one workflow.
7. Handle tool failures safely and provide recovery information.
8. Record workflow telemetry.
9. Apply role-based authorization and API-key protection.
10. Deploy the backend as a live web service.

---

## 🏗️ System Architecture

```text
                    USER / CLIENT
                         |
                         v
                  FASTAPI BACKEND
                         |
                         v
                WORKFLOW ORCHESTRATOR
                         |
          +--------------+--------------+
          |              |              |
          v              v              v
   TRACEABILITY      COMPLIANCE     SUPPLY-CHAIN
      AGENT             AGENT          ANALYSIS
          |              |              |
          v              v              v
   PRODUCT STORE     RAG RULES      PRODUCT DATA
          |              |
          +--------------+--------------+
                         |
                         v
                 PRODUCT STATE
                         |
                         v
                FINAL ASSURANCE
                     RESULT

        WORKFLOW
           |
           +----> TELEMETRY
           |
           +----> FAILURE / RECOVERY
```

---

## 🤖 Agents

### 1. Traceability Agent

The Traceability Agent retrieves the complete traceability information for a honey product.

It provides:

- Product ID
- Product name
- Origin
- Current supply-chain stage
- Supply-chain events
- Event locations
- Event actors
- Event timestamps
- Event notes

Endpoint:

```text
GET /traceability/{product_id}
```

---

### 2. Compliance Agent

The Compliance Agent checks whether a product satisfies the available traceability rules.

The agent retrieves relevant rules through the RAG rule-retrieval component and checks the product against those requirements.

Example checks include:

- Product identification
- Product origin
- Supply-chain events
- Event location
- Event actor
- Event timestamp

Endpoint:

```text
GET /compliance/{product_id}
```

Example successful response:

```json
{
  "success": true,
  "product_id": "HNY-003",
  "compliant": true,
  "violations": []
}
```

---

### 3. Supply-Chain Analysis Agent

The Supply-Chain Analysis Agent analyzes the recorded supply-chain events and current product state.

It provides information such as:

- Current stage
- Number of events
- Recorded stages
- Locations
- Actors
- Supply-chain analysis

Endpoint:

```text
GET /supply-chain/{product_id}
```

---

## 🔎 RAG-Based Traceability Rules

The project includes a rule retrieval component for traceability requirements.

Current rules include:

| Rule ID | Rule |
|---|---|
| TR-001 | Product Identification |
| TR-002 | Product Origin |
| TR-003 | Supply Chain Events |
| TR-004 | Event Location |
| TR-005 | Event Actor |
| TR-006 | Event Timestamp |

The current implementation uses **keyword-based rule retrieval** to identify relevant traceability rules.

This provides the RAG-style retrieval layer required by the project without claiming a vector database or embedding-based semantic retrieval.

---

## 💾 Database and Product State

The system uses **SQLite** for persistent product storage.

Product records contain:

```text
Product ID
Product Name
Origin
Current Stage
Supply-Chain Events
    ├── Stage
    ├── Location
    ├── Actor
    ├── Timestamp
    └── Notes
```

Supported product stages include:

```text
harvested
collected
processed
packaged
distributed
delivered
```

The product state is persisted in the database so that records remain available across application restarts.

---

## 🔗 Workflow Orchestration

The Workflow Orchestrator coordinates the three agents in sequence:

```text
1. Traceability
       ↓
2. Compliance
       ↓
3. Supply-Chain Analysis
       ↓
4. Final Assurance Result
```

Endpoint:

```text
GET /workflow/{product_id}
```

Example successful workflow:

```json
{
  "success": true,
  "product_id": "HNY-003",
  "workflow": {
    "traceability": {},
    "compliance": {
      "success": true,
      "compliant": true,
      "violations": []
    },
    "supply_chain_analysis": {}
  }
}
```

---

## ⚠️ Tool Failure and Recovery

The workflow includes basic failure handling.

If an agent or tool fails, the workflow:

1. Identifies the failed stage.
2. Records the failure through telemetry.
3. Stops the workflow safely.
4. Returns structured recovery information.
5. Provides the next recommended action.

Example:

```json
{
  "success": false,
  "stage": "traceability",
  "message": "Product not found",
  "recovery": {
    "status": "handled",
    "action": "Workflow stopped safely because traceability failed.",
    "next_step": "Verify that the product exists before retrying."
  }
}
```

---

## 📊 Telemetry

The system records workflow events including:

- Workflow started
- Workflow completed
- Workflow failed

Each telemetry event records:

```text
Timestamp
Event Type
Product ID
Details
```

This provides basic observability for the agent workflow.

---

## 🔐 Authorization and Security

The project includes basic authorization controls.

### User Roles

```text
ADMIN
OPERATOR
VIEWER
```

Permissions are assigned according to the user's role.

The workflow endpoint also uses an API key for access protection.

Example:

```text
x-api-key: <your-api-key>
```

API keys are stored through environment variables rather than hard-coded in the source code.

---

## ⚙️ Configuration

Create a `.env` file in the project root:

```env
APP_NAME=Blockchain Honey Traceability Assurance Agent
APP_ENV=production
API_KEY=your-secure-api-key
```

The `.env` file should **never be committed to GitHub**.

The project `.gitignore` excludes:

```text
.env
venv/
__pycache__/
*.pyc
*.db
.pytest_cache/
```

---

## 📁 Project Structure

```text
blockchain-honey-traceability/
│
├── .env
├── .gitignore
│
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   │
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── traceability_agent.py
│   │   ├── compliance_agent.py
│   │   └── supply_chain_agent.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── product_routes.py
│   │   ├── traceability.py
│   │   ├── compliance.py
│   │   ├── supply_chain.py
│   │   └── workflow.py
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── product_store.py
│   │   └── honey_traceability.db
│   │
│   ├── rag/
│   │   ├── __init__.py
│   │   ├── traceability_rules.py
│   │   └── rule_retriever.py
│   │
│   ├── workflow/
│   │   ├── __init__.py
│   │   └── orchestrator.py
│   │
│   ├── security/
│   │   ├── __init__.py
│   │   └── authorization.py
│   │
│   ├── telemetry/
│   │   ├── __init__.py
│   │   └── telemetry.py
│   │
│   └── tests/
│       ├── __init__.py
│       └── test_agents.py
│
└── README.md
```

---

## 🛠️ Technologies Used

- **Python**
- **FastAPI**
- **Uvicorn**
- **Pydantic**
- **SQLite**
- **Python-dotenv**
- **Pytest**
- **OpenTelemetry API**

---

## 🚀 Local Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/blockchain-honey-traceability.git
cd blockchain-honey-traceability
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell activation is restricted, use Command Prompt:

```cmd
venv\Scripts\activate
```

### 4. Install dependencies

```bash
python -m pip install fastapi uvicorn pydantic python-dotenv pytest opentelemetry-api
```

### 5. Configure environment variables

Create `.env`:

```env
APP_NAME=Blockchain Honey Traceability Assurance Agent
APP_ENV=development
API_KEY=your-development-api-key
```

---

## ▶️ Run the Application

From the project root:

```bash
python -m uvicorn backend.main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

Swagger API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 🧪 Testing

Run the automated tests:

```bash
python -m pytest backend/tests/test_agents.py
```

Current test coverage includes:

- Traceability failure handling
- Compliance failure handling
- Supply-chain analysis failure handling
- Workflow failure and recovery

Expected result:

```text
4 passed
```

---

## 🌐 Deployment

The backend has been deployed as a web service using **Render**.

Live API:

```text
https://blockchain-honey-traceability.onrender.com
```

Interactive API documentation:

```text
https://blockchain-honey-traceability.onrender.com/docs
```

The production deployment was tested successfully with:

```text
HTTP 200 OK
```

for the complete workflow.

---

## ✅ Live Workflow Validation

A test product was created:

```text
Product ID: HNY-003
Product Name: Himalayan Organic Honey
Origin: Nepal
Current Stage: harvested
Location: Kaski, Nepal
Actor: ABC Beekeepers
```

The deployed workflow successfully returned:

```text
success: true
```

with:

```text
Traceability → Successful
Compliance → Compliant
Supply-Chain Analysis → Successful
Workflow → Successful
```

---

## 🔒 Security Notes

Sensitive configuration values such as API keys are stored using environment variables.

Do not commit:

```text
.env
```

to GitHub.

For production deployment, configure secrets through the deployment platform's environment-variable settings.

---

## 📌 Project Scope

This project focuses on the requirements of the **Blockchain Honey Traceability Assurance Agent** assignment:

- Traceability Agent
- Compliance Agent
- Supply-Chain Analysis Agent
- Database integration
- Product state maintenance
- RAG-based traceability rules
- Workflow chaining
- Tool failure and recovery
- Testing
- Telemetry
- Authorization
- Secure deployment

The current implementation uses **SQLite for persistent database-backed product records**. It does not claim to implement a live blockchain network.

---

## 👨‍💻 Author

**Deepak Chaudhary**

B.Tech Computer Science & Engineering  
Data Science Specialization

---

## 📄 License

This project is developed for academic/project purposes.
