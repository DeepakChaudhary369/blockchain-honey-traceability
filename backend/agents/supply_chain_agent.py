from backend.database.product_store import product_store


class SupplyChainAnalysisAgent:

    def analyze_product(self, product_id: str):
        """
        Analyze the supply-chain events and current state
        of a honey product.
        """

        product = product_store.get_product(product_id)

        if product is None:
            return {
                "success": False,
                "message": "Product not found",
                "product_id": product_id
            }

        events = product.events

        if not events:
            return {
                "success": True,
                "product_id": product.product_id,
                "product_name": product.product_name,
                "current_stage": product.current_stage.value,
                "total_events": 0,
                "analysis": "No supply-chain events available for analysis."
            }

        stages = [event.stage.value for event in events]
        locations = [event.location for event in events]
        actors = [event.actor for event in events]

        return {
            "success": True,
            "product_id": product.product_id,
            "product_name": product.product_name,
            "origin": product.origin,
            "current_stage": product.current_stage.value,
            "total_events": len(events),
            "stages": stages,
            "locations": locations,
            "actors": actors,
            "analysis": (
                f"The product has {len(events)} recorded supply-chain event(s) "
                f"and is currently at the '{product.current_stage.value}' stage."
            )
        }


supply_chain_analysis_agent = SupplyChainAnalysisAgent()