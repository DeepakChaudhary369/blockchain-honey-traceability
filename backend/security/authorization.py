import os
from enum import Enum

from dotenv import load_dotenv


load_dotenv()


class UserRole(str, Enum):
    ADMIN = "admin"
    OPERATOR = "operator"
    VIEWER = "viewer"


class Authorization:

    def __init__(self):
        self.api_key = os.getenv("API_KEY", "")

        self.permissions = {
            UserRole.ADMIN: [
                "create_product",
                "view_product",
                "run_traceability",
                "run_compliance",
                "run_supply_chain_analysis",
                "run_workflow"
            ],
            UserRole.OPERATOR: [
                "create_product",
                "view_product",
                "run_traceability",
                "run_compliance",
                "run_supply_chain_analysis",
                "run_workflow"
            ],
            UserRole.VIEWER: [
                "view_product",
                "run_traceability",
                "run_compliance",
                "run_supply_chain_analysis",
                "run_workflow"
            ]
        }

    def is_authorized(self, role: UserRole, permission: str) -> bool:
        """
        Check whether a user role has the required permission.
        """
        return permission in self.permissions.get(role, [])

    def is_valid_api_key(self, api_key: str) -> bool:
        """
        Check whether the supplied API key is valid.
        """
        return bool(self.api_key) and api_key == self.api_key


authorization = Authorization()