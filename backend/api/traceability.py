from fastapi import APIRouter, HTTPException

from backend.agents.traceability_agent import traceability_agent


router = APIRouter(prefix="/traceability", tags=["Traceability"])


@router.get("/{product_id}")
def trace_product(product_id: str):

    result = traceability_agent.trace_product(product_id)

    if not result["success"]:
        raise HTTPException(
            status_code=404,
            detail=result["message"]
        )

    return result