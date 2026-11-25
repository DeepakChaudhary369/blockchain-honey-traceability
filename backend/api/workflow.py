from fastapi import APIRouter, HTTPException, Header

from backend.workflow.orchestrator import workflow_orchestrator
from backend.security.authorization import authorization, UserRole


router = APIRouter(
    prefix="/workflow",
    tags=["Workflow"]
)


@router.get("/{product_id}")
def run_workflow(
    product_id: str,
    role: UserRole = UserRole.ADMIN,
    x_api_key: str | None = Header(default=None)
):
    # Check API key
    if not authorization.is_valid_api_key(x_api_key or ""):
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key"
        )

    # Check role permission
    if not authorization.is_authorized(role, "run_workflow"):
        raise HTTPException(
            status_code=403,
            detail="User is not authorized to run the workflow"
        )

    result = workflow_orchestrator.run_workflow(product_id)

    if not result["success"]:
        raise HTTPException(
            status_code=404,
            detail=result
        )

    return result