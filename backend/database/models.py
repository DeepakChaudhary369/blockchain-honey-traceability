from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class ProductStage(str, Enum):
    HARVESTED = "harvested"
    COLLECTED = "collected"
    PROCESSED = "processed"
    PACKAGED = "packaged"
    DISTRIBUTED = "distributed"
    DELIVERED = "delivered"


class SupplyChainEvent(BaseModel):
    stage: ProductStage
    location: str
    actor: str
    timestamp: datetime
    notes: str | None = None


class HoneyProduct(BaseModel):
    product_id: str = Field(..., min_length=1)
    product_name: str
    origin: str
    current_stage: ProductStage
    events: list[SupplyChainEvent] = Field(default_factory=list)