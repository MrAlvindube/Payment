from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from .models import PaymentStatus


class PaymentCreate(BaseModel):
    amount: float = Field(gt=0, description="Total amount for the payment")
    currency: str = Field(min_length=3, max_length=3, description="ISO currency code")
    description: Optional[str] = Field(None, description="Optional payment description")


class PaymentResponse(BaseModel):
    id: str
    amount: float
    currency: str
    description: Optional[str]
    status: PaymentStatus
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
