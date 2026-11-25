from fastapi import APIRouter, HTTPException

from backend.database.models import HoneyProduct
from backend.database.product_store import product_store
from backend.security.authorization import authorization, UserRole


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post("/")
def create_product(
    product: HoneyProduct,
    role: UserRole = UserRole.ADMIN
):
    # Check authorization before creating a product
    if not authorization.is_authorized(role, "create_product"):
        raise HTTPException(
            status_code=403,
            detail="User is not authorized to create products"
        )

    existing_product = product_store.get_product(product.product_id)

    if existing_product:
        raise HTTPException(
            status_code=409,
            detail="Product already exists"
        )

    return product_store.create_product(product)


@router.get("/{product_id}")
def get_product(product_id: str):
    product = product_store.get_product(product_id)

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


@router.get("/")
def list_products():
    return product_store.list_products()