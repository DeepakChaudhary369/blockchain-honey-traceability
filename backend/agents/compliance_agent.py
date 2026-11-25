from backend.database.product_store import product_store
from backend.rag.rule_retriever import rule_retriever


class ComplianceAgent:

    def check_compliance(self, product_id: str):
        """
        Check whether a honey product satisfies
        the traceability rules retrieved by the RAG component.
        """

        product = product_store.get_product(product_id)

        if product is None:
            return {
                "success": False,
                "message": "Product not found",
                "product_id": product_id
            }

        violations = []

        # Retrieve relevant traceability rules using the RAG rule retriever
        rules = rule_retriever.search_rules("product identification origin supply chain events location actor timestamp")

        for rule in rules:

            rule_id = rule["rule_id"]

            # TR-001: Product Identification
            if rule_id == "TR-001":
                if not product.product_id:
                    violations.append(rule["requirement"])

            # TR-002: Product Origin
            elif rule_id == "TR-002":
                if not product.origin:
                    violations.append(rule["requirement"])

            # TR-003: Supply Chain Events
            elif rule_id == "TR-003":
                if not product.events:
                    violations.append(rule["requirement"])

            # TR-004: Event Location
            elif rule_id == "TR-004":
                for index, event in enumerate(product.events):
                    if not event.location:
                        violations.append(
                            f"Event {index + 1}: {rule['requirement']}"
                        )

            # TR-005: Event Actor
            elif rule_id == "TR-005":
                for index, event in enumerate(product.events):
                    if not event.actor:
                        violations.append(
                            f"Event {index + 1}: {rule['requirement']}"
                        )

            # TR-006: Event Timestamp
            elif rule_id == "TR-006":
                for index, event in enumerate(product.events):
                    if not event.timestamp:
                        violations.append(
                            f"Event {index + 1}: {rule['requirement']}"
                        )

        compliant = len(violations) == 0

        return {
            "success": True,
            "product_id": product.product_id,
            "compliant": compliant,
            "violations": violations
        }


compliance_agent = ComplianceAgent()