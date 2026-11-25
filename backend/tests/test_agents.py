from backend.agents.traceability_agent import traceability_agent
from backend.agents.compliance_agent import compliance_agent
from backend.agents.supply_chain_agent import supply_chain_analysis_agent
from backend.workflow.orchestrator import workflow_orchestrator


def test_traceability_missing_product():
    result = traceability_agent.trace_product("TEST-999")

    assert result["success"] is False
    assert result["message"] == "Product not found"


def test_compliance_missing_product():
    result = compliance_agent.check_compliance("TEST-999")

    assert result["success"] is False
    assert result["message"] == "Product not found"


def test_supply_chain_missing_product():
    result = supply_chain_analysis_agent.analyze_product("TEST-999")

    assert result["success"] is False
    assert result["message"] == "Product not found"


def test_workflow_missing_product():
    result = workflow_orchestrator.run_workflow("TEST-999")

    assert result["success"] is False
    assert result["stage"] == "traceability"
    assert result["recovery"]["status"] == "handled"