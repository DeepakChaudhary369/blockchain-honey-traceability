from fastapi import APIRouter, HTTPException

from backend.agents.compliance_agent import compliance_agent


router = APIRouter(
    prefix="/compliance",
    tags=["Compliance"]
)


@router.get("/{product_id}")
def check_compliance(product_id: str):

    result = compliance_agent.check_compliance(product_id)

    if not result["success"]:
        raise HTTPException(
            status_code=404,
            detail=result["message"]
        )

    return result