from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from sqlmodel import SQLModel, Field


class PaymentStatus(str, Enum):
    CREATED = "created"
    AUTHORIZED = "authorized"
    CAPTURED = "captured"
    REFUNDED = "refunded"
    FAILED = "failed"


class Payment(SQLModel, table=True):
    id: str = Field(primary_key=True, index=True)
    amount: float
    currency: str
    description: Optional[str] = None
    status: PaymentStatus
    created_at: datetime
    updated_at: datetime
