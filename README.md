# 🍯 Blockchain Honey Traceability Assurance Agent

An intelligent honey-product traceability and assurance system that follows product records across the supply chain, checks traceability compliance, analyzes supply-chain information, and coordinates multiple agents through a workflow orchestrator.

The project demonstrates **Traceability, Compliance, and Supply-Chain Analysis agents**, persistent product state, rule-based RAG retrieval, workflow chaining, failure handling and recovery, telemetry, authorization, and secure deployment.

## 🚀 Live Demo

**API Documentation (Swagger):**  
https://blockchain-honey-traceability.onrender.com/docs

**Backend API:**  
https://blockchain-honey-traceability.onrender.com

---

## 🎯 Project Objective

The objective of this project is to develop an intelligent traceability assistant that follows honey-product records throughout the supply chain and provides assurance about their traceability and compliance.

The system:

- Tracks honey products and their supply-chain events
- Maintains persistent product state
- Retrieves traceability rules for compliance checking
- Performs traceability analysis
- Performs compliance checking
- Performs supply-chain analysis
- Coordinates the agents through a workflow
- Handles tool failures safely
- Records workflow telemetry
- Applies role-based authorization and API-key protection
- Provides a deployed REST API

---

## 🏗️ System Architecture

```text
                    USER / CLIENT
                         |
                         v
                  TRACEABILITY API
                         |
                         v
                WORKFLOW ORCHESTRATOR
                         |
          +--------------+--------------+
          |              |              |
          v              v              v
   TRACEABILITY      COMPLIANCE     SUPPLY-CHAIN
      AGENT            AGENT          ANALYSIS
          |              |              |
          v              v              v
   Product Records   RAG Rules      Product/Supply
                    Retriever          Data
          |              |
          +--------------+
                 |
                 v
        Persistent Database
                 |
                 v
           Product State

        Workflow Monitoring
                 |
        +--------+--------+
        |                 |
        v                 v
    Telemetry      Failure & Recovery
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
- Responsible actors
- Event timestamps
- Event notes

### 2. Compliance Agent

The Compliance Agent checks a product against the available traceability rules.

The current rules cover:

- Product identification
- Product origin
- Supply-chain events
- Event location
- Event actor
- Event timestamp

The agent returns whether the product is compliant and lists any detected violations.

### 3. Supply-Chain Analysis Agent

The Supply-Chain Analysis Agent analyzes the recorded supply-chain information.

It provides:

- Current product stage
- Total number of events
- Recorded stages
- Locations
- Actors
- Basic supply-chain analysis

---

## 🔎 RAG-Based Traceability Rules

The project includes a rule retrieval component for traceability compliance.

The current implementation uses **keyword-based rule retrieval** to identify relevant traceability rules from the rule collection.

Example rules include:

```text
TR-001 — Product Identification
TR-002 — Product Origin
TR-003 — Supply Chain Events
TR-004 — Event Location
TR-005 — Event Actor
TR-006 — Event Timestamp
```

The retrieved rules are then used by the Compliance Agent during compliance checking.

> Note: This implementation uses a lightweight keyword-based retrieval approach rather than a vector database or embedding-based retrieval system.

---

## 🗄️ Persistent Product State

Product records are stored using **SQLite**.

The database maintains product information including:

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

The persistent database allows product state to remain available across application restarts.

Database file:

```text
backend/database/honey_traceability.db
```

---

## 🔄 Workflow Orchestration

The Workflow Orchestrator connects the three agents into a single assurance workflow.

### Workflow

```text
1. Traceability
       ↓
2. Compliance
       ↓
3. Supply-Chain Analysis
       ↓
4. Final Assurance Result
```

Each stage is executed sequentially.

If a stage fails, the workflow returns structured failure and recovery information instead of silently continuing.

---

## 🛠️ Failure Handling & Recovery

The workflow includes basic failure handling for agent/tool failures.

For example, if a product does not exist:

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

This demonstrates controlled workflow failure and recovery information.

---

## 📊 Telemetry

The project includes basic workflow telemetry.

Telemetry records events such as:

```text
workflow_started
workflow_failed
workflow_completed
```

Each telemetry event records:

- Timestamp
- Event type
- Product ID
- Event details

This provides visibility into workflow execution.

---

## 🔐 Authorization & Security

The system includes basic authorization controls.

### User Roles

```text
ADMIN
OPERATOR
VIEWER
```

Permissions are defined according to the user's role.

The workflow API also uses API-key validation.

Example:

```text
Valid API Key
      ↓
Role Authorization
      ↓
Workflow Execution
```

Invalid API keys are rejected with an HTTP `401 Unauthorized` response.

Unauthorized operations return an HTTP `403 Forbidden` response.

Environment-specific configuration and API keys are managed through environment variables.

---

## 🌐 REST API

The application is implemented using **FastAPI**.

### Product APIs

```text
POST /products/
GET  /products/
GET  /products/{product_id}
```

### Traceability API

```text
GET /traceability/{product_id}
```

### Compliance API

```text
GET /compliance/{product_id}
```

### Supply-Chain Analysis API

```text
GET /supply-chain/{product_id}
```

### Workflow API

```text
GET /workflow/{product_id}
```

### Health Check

```text
GET /health
```

---

## 📋 Example Product

The project includes an example honey product:

```json
{
  "product_id": "HNY-003",
  "product_name": "Himalayan Organic Honey",
  "origin": "Nepal",
  "current_stage": "harvested",
  "events": [
    {
      "stage": "harvested",
      "location": "Kaski, Nepal",
      "actor": "ABC Beekeepers",
      "timestamp": "2026-11-22T10:00:00",
      "notes": "Honey harvested from registered apiary"
    }
  ]
}
```

---

## 🧪 Testing

The project includes automated tests for the core agents and workflow.

Current test coverage includes:

- Missing product handling in Traceability Agent
- Missing product handling in Compliance Agent
- Missing product handling in Supply-Chain Analysis Agent
- Workflow failure and recovery handling

Run the tests with:

```bash
python -m pytest backend/tests/test_agents.py
```

Current result:

```text
4 passed
```

---

## 📁 Project Structure

```text
blockchain-honey-traceability/
│
├── backend/
│   ├── agents/
│   │   ├── traceability_agent.py
│   │   ├── compliance_agent.py
│   │   └── supply_chain_agent.py
│   │
│   ├── api/
│   │   ├── product_routes.py
│   │   ├── traceability.py
│   │   ├── compliance.py
│   │   ├── supply_chain.py
│   │   └── workflow.py
│   │
│   ├── database/
│   │   ├── models.py
│   │   ├── product_store.py
│   │   └── honey_traceability.db
│   │
│   ├── rag/
│   │   ├── traceability_rules.py
│   │   └── rule_retriever.py
│   │
│   ├── workflow/
│   │   └── orchestrator.py
│   │
│   ├── security/
│   │   └── authorization.py
│   │
│   ├── telemetry/
│   │   └── telemetry.py
│   │
│   ├── tests/
│   │   └── test_agents.py
│   │
│   ├── config.py
│   └── main.py
│
├── .gitignore
├── .env
├── requirements.txt
└── README.md
```

> The `.env` file should not be committed to GitHub. Secrets should be configured through environment variables.

---

## ⚙️ Technologies Used

- **Python**
- **FastAPI**
- **Uvicorn**
- **Pydantic**
- **SQLite**
- **Python-dotenv**
- **Pytest**
- **REST API**
- **Rule-based RAG retrieval**
- **Role-based authorization**
- **API-key protection**
- **Render**

---

## ▶️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/DeepakChaudhary369/blockchain-honey-traceability.git
cd blockchain-honey-traceability
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root:

```env
APP_NAME=Blockchain Honey Traceability Assurance Agent
APP_ENV=development
API_KEY=your-secure-api-key
```

### 6. Start the API

```bash
python -m uvicorn backend.main:app --reload
```

### 7. Open Swagger

```text
http://127.0.0.1:8000/docs
```

---

## ☁️ Deployment

The backend is deployed using **Render**.

Production API:

```text
https://blockchain-honey-traceability.onrender.com
```

Swagger API documentation:

```text
https://blockchain-honey-traceability.onrender.com/docs
```

The deployed service uses environment variables for production configuration and API-key protection.

---

## 🔒 Security Notes

Sensitive configuration should not be stored directly in source code.

The project uses:

- `.env` for local secrets
- Render environment variables for deployment secrets
- `.gitignore` to prevent `.env` from being committed
- API-key validation
- Role-based authorization

Never publish the actual API key in the repository, README, screenshots, or public documentation.

---

## 🎓 Project Requirements Mapping

| Requirement | Implementation |
|---|---|
| Traceability Agent | ✅ Implemented |
| Compliance Agent | ✅ Implemented |
| Supply-Chain Analysis Agent | ✅ Implemented |
| Blockchain/Database API integration | ✅ Persistent SQLite database |
| Product state maintenance | ✅ Implemented |
| RAG for traceability rules | ✅ Rule retrieval implemented |
| Workflow chaining | ✅ Implemented |
| Tool failure & recovery | ✅ Implemented |
| Testing | ✅ Pytest |
| Telemetry | ✅ Implemented |
| Authorization | ✅ Role-based authorization + API key |
| Secure deployment | ✅ Environment variables + Render deployment |

---

## 📌 Current Implementation Scope

This project focuses on the requirements defined for the **Blockchain Honey Traceability Assurance Agent**.

The current implementation uses a persistent database for product records and a lightweight rule-retrieval approach for traceability compliance. It does **not** claim to implement a live public blockchain network or production-grade vector-database RAG.

---

## 👨‍💻 Author

**Deepak Chaudhary**

B.Tech — Computer Science & Engineering (Data Science)

GitHub:  
https://github.com/DeepakChaudhary369

---

## 📄 License

This project is developed as an academic/college project for demonstrating intelligent agent workflows, honey-product traceability, compliance checking, supply-chain analysis, and assurance.
