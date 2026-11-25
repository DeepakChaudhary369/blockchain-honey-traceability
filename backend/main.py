from fastapi import FastAPI

from backend.api.product_routes import router as product_router
from backend.api.traceability import router as traceability_router
from backend.api.compliance import router as compliance_router
from backend.api.supply_chain import router as supply_chain_router
from backend.api.workflow import router as workflow_router


app = FastAPI(
    title="Blockchain Honey Traceability Assurance Agent",
    description="Backend API for honey product traceability and assurance.",
    version="1.0.0"
)

app.include_router(product_router)
app.include_router(traceability_router)
app.include_router(compliance_router)
app.include_router(supply_chain_router)
app.include_router(workflow_router)


@app.get("/")
def root():
    return {
        "message": "Blockchain Honey Traceability Assurance Agent API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }