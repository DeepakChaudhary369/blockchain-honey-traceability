from fastapi import APIRouter, HTTPException

from backend.agents.supply_chain_agent import supply_chain_analysis_agent


router = APIRouter(
    prefix="/supply-chain",
    tags=["Supply Chain Analysis"]
)


@router.get("/{product_id}")
def analyze_supply_chain(product_id: str):

    result = supply_chain_analysis_agent.analyze_product(product_id)

    if not result["success"]:
        raise HTTPException(
            status_code=404,
            detail=result["message"]
        )

    return result