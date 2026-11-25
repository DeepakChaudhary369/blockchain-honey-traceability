from backend.database.product_store import product_store


class TraceabilityAgent:

    def trace_product(self, product_id: str):
        """
        Retrieve the complete traceability information
        for a honey product.
        """

        product = product_store.get_product(product_id)

        if product is None:
            return {
                "success": False,
                "message": "Product not found",
                "product_id": product_id
            }

        return {
            "success": True,
            "product_id": product.product_id,
            "product_name": product.product_name,
            "origin": product.origin,
            "current_stage": product.current_stage.value,
            "events": [
                {
                    "stage": event.stage.value,
                    "location": event.location,
                    "actor": event.actor,
                    "timestamp": event.timestamp.isoformat(),
                    "notes": event.notes
                }
                for event in product.events
            ]
        }


traceability_agent = TraceabilityAgent()