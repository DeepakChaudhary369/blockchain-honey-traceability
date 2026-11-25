import json
import sqlite3
from pathlib import Path
from typing import Optional

from .models import HoneyProduct


# Persistent database file
DATABASE_PATH = (
    Path(__file__).resolve().parent / "honey_traceability.db"
)


class ProductStore:

    def __init__(self):
        self.database_path = DATABASE_PATH
        self._initialize_database()

    def _get_connection(self):
        return sqlite3.connect(self.database_path)

    def _initialize_database(self):
        connection = self._get_connection()

        try:
            cursor = connection.cursor()

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS products (
                    product_id TEXT PRIMARY KEY,
                    product_data TEXT NOT NULL
                )
                """
            )

            connection.commit()

        finally:
            connection.close()

    def create_product(self, product: HoneyProduct) -> HoneyProduct:
        connection = self._get_connection()

        try:
            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO products (product_id, product_data)
                VALUES (?, ?)
                """,
                (
                    product.product_id,
                    product.model_dump_json()
                )
            )

            connection.commit()

            return product

        finally:
            connection.close()

    def get_product(self, product_id: str) -> Optional[HoneyProduct]:
        connection = self._get_connection()

        try:
            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT product_data
                FROM products
                WHERE product_id = ?
                """,
                (product_id,)
            )

            row = cursor.fetchone()

            if row is None:
                return None

            product_data = json.loads(row[0])

            return HoneyProduct.model_validate(product_data)

        finally:
            connection.close()

    def update_product(self, product: HoneyProduct) -> HoneyProduct:
        connection = self._get_connection()

        try:
            cursor = connection.cursor()

            cursor.execute(
                """
                UPDATE products
                SET product_data = ?
                WHERE product_id = ?
                """,
                (
                    product.model_dump_json(),
                    product.product_id
                )
            )

            connection.commit()

            return product

        finally:
            connection.close()

    def list_products(self):
        connection = self._get_connection()

        try:
            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT product_data
                FROM products
                """
            )

            rows = cursor.fetchall()

            return [
                HoneyProduct.model_validate(json.loads(row[0]))
                for row in rows
            ]

        finally:
            connection.close()


product_store = ProductStore()