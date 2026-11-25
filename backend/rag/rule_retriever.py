from backend.rag.traceability_rules import TRACEABILITY_RULES


class RuleRetriever:

    def get_all_rules(self):
        """
        Retrieve all available traceability rules.
        """
        return TRACEABILITY_RULES

    def get_rule_by_id(self, rule_id: str):
        """
        Retrieve a specific traceability rule by its ID.
        """
        for rule in TRACEABILITY_RULES:
            if rule["rule_id"] == rule_id:
                return rule

        return None

    def search_rules(self, query: str):
        """
        Retrieve traceability rules relevant to a query.
        """

        query_words = set(query.lower().split())

        results = []

        for rule in TRACEABILITY_RULES:

            searchable_text = (
                f"{rule['title']} "
                f"{rule['rule']} "
                f"{rule['requirement']}"
            ).lower()

            score = sum(
                1
                for word in query_words
                if word in searchable_text
            )

            if score > 0:
                results.append({
                    "rule": rule,
                    "score": score
                })

        results.sort(
            key=lambda item: item["score"],
            reverse=True
        )

        return [item["rule"] for item in results]


rule_retriever = RuleRetriever()