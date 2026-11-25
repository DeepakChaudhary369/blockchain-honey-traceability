from backend.agents.traceability_agent import traceability_agent
from backend.agents.compliance_agent import compliance_agent
from backend.agents.supply_chain_agent import supply_chain_analysis_agent
from backend.telemetry.telemetry import telemetry


class WorkflowOrchestrator:

    def run_workflow(self, product_id: str):
        """
        Run the complete honey product assurance workflow.

        Workflow:
        1. Traceability
        2. Compliance
        3. Supply-chain analysis

        Includes basic failure handling and recovery information.
        """

        telemetry.record_event(
            "workflow_started",
            product_id,
            "Honey assurance workflow started"
        )

        # Step 1: Traceability
        try:
            traceability_result = traceability_agent.trace_product(product_id)

        except Exception as error:

            telemetry.record_event(
                "workflow_failed",
                product_id,
                "Traceability tool failed"
            )

            return {
                "success": False,
                "stage": "traceability",
                "message": "Traceability tool failed.",
                "product_id": product_id,
                "recovery": {
                    "status": "handled",
                    "action": "Workflow stopped safely because traceability failed.",
                    "next_step": "Retry the workflow after verifying the traceability service."
                }
            }

        if not traceability_result["success"]:

            telemetry.record_event(
                "workflow_failed",
                product_id,
                "Traceability stage failed"
            )

            return {
                "success": False,
                "stage": "traceability",
                "message": traceability_result["message"],
                "product_id": product_id,
                "recovery": {
                    "status": "handled",
                    "action": "Workflow stopped safely because traceability failed.",
                    "next_step": "Verify that the product exists before retrying."
                }
            }

        # Step 2: Compliance
        try:
            compliance_result = compliance_agent.check_compliance(product_id)

        except Exception as error:

            telemetry.record_event(
                "workflow_failed",
                product_id,
                "Compliance tool failed"
            )

            return {
                "success": False,
                "stage": "compliance",
                "message": "Compliance tool failed.",
                "product_id": product_id,
                "recovery": {
                    "status": "handled",
                    "action": "Workflow stopped safely because compliance failed.",
                    "next_step": "Retry the workflow after verifying the compliance service."
                }
            }

        if not compliance_result["success"]:

            telemetry.record_event(
                "workflow_failed",
                product_id,
                "Compliance stage failed"
            )

            return {
                "success": False,
                "stage": "compliance",
                "message": compliance_result["message"],
                "product_id": product_id,
                "recovery": {
                    "status": "handled",
                    "action": "Workflow stopped safely because compliance failed.",
                    "next_step": "Verify the product and compliance rules before retrying."
                }
            }

        # Step 3: Supply-chain analysis
        try:
            supply_chain_result = (
                supply_chain_analysis_agent.analyze_product(product_id)
            )

        except Exception as error:

            telemetry.record_event(
                "workflow_failed",
                product_id,
                "Supply-chain analysis tool failed"
            )

            return {
                "success": False,
                "stage": "supply_chain_analysis",
                "message": "Supply-chain analysis tool failed.",
                "product_id": product_id,
                "recovery": {
                    "status": "handled",
                    "action": "Workflow stopped safely because supply-chain analysis failed.",
                    "next_step": "Retry the workflow after verifying the supply-chain analysis service."
                }
            }

        if not supply_chain_result["success"]:

            telemetry.record_event(
                "workflow_failed",
                product_id,
                "Supply-chain analysis stage failed"
            )

            return {
                "success": False,
                "stage": "supply_chain_analysis",
                "message": supply_chain_result["message"],
                "product_id": product_id,
                "recovery": {
                    "status": "handled",
                    "action": "Workflow stopped safely because supply-chain analysis failed.",
                    "next_step": "Verify the product supply-chain records before retrying."
                }
            }

        telemetry.record_event(
            "workflow_completed",
            product_id,
            "Honey assurance workflow completed successfully"
        )

        # Final combined result
        return {
            "success": True,
            "product_id": product_id,
            "workflow": {
                "traceability": traceability_result,
                "compliance": compliance_result,
                "supply_chain_analysis": supply_chain_result
            }
        }


workflow_orchestrator = WorkflowOrchestrator()