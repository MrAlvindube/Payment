from __future__ import annotations

from datetime import datetime
from typing import List
from uuid import uuid4

from fastapi import HTTPException, status
from sqlmodel import select

from .database import get_session
from .models import Payment, PaymentStatus
from .schemas import PaymentCreate


class PaymentService:
    @staticmethod
    def create_payment(payload: PaymentCreate) -> Payment:
        payment = Payment(
            id=str(uuid4()),
            amount=payload.amount,
            currency=payload.currency.upper(),
            description=payload.description,
            status=PaymentStatus.CREATED,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )

        with get_session() as session:
            session.add(payment)
            session.commit()
            session.refresh(payment)
        return payment

    @staticmethod
    def list_payments() -> List[Payment]:
        with get_session() as session:
            payments = session.exec(select(Payment).order_by(Payment.created_at.desc())).all()
        return payments

    @staticmethod
    def get_payment(payment_id: str) -> Payment:
        with get_session() as session:
            payment = session.get(Payment, payment_id)
            if not payment:
                raise HTTPException(status.HTTP_404_NOT_FOUND, "Payment not found")
        return payment

    @staticmethod
    def authorize_payment(payment_id: str) -> Payment:
        with get_session() as session:
            payment = session.get(Payment, payment_id)
            if not payment:
                raise HTTPException(status.HTTP_404_NOT_FOUND, "Payment not found")
            if payment.status not in {PaymentStatus.CREATED, PaymentStatus.FAILED}:
                raise HTTPException(status.HTTP_400_BAD_REQUEST, "Payment cannot be authorized from current state")

            payment.status = PaymentStatus.AUTHORIZED
            payment.updated_at = datetime.utcnow()
            session.add(payment)
            session.commit()
            session.refresh(payment)
        return payment

    @staticmethod
    def capture_payment(payment_id: str) -> Payment:
        with get_session() as session:
            payment = session.get(Payment, payment_id)
            if not payment:
                raise HTTPException(status.HTTP_404_NOT_FOUND, "Payment not found")
            if payment.status not in {PaymentStatus.AUTHORIZED, PaymentStatus.CREATED}:
                raise HTTPException(status.HTTP_400_BAD_REQUEST, "Payment cannot be captured from current state")

            payment.status = PaymentStatus.CAPTURED
            payment.updated_at = datetime.utcnow()
            session.add(payment)
            session.commit()
            session.refresh(payment)
        return payment

    @staticmethod
    def refund_payment(payment_id: str) -> Payment:
        with get_session() as session:
            payment = session.get(Payment, payment_id)
            if not payment:
                raise HTTPException(status.HTTP_404_NOT_FOUND, "Payment not found")
            if payment.status != PaymentStatus.CAPTURED:
                raise HTTPException(status.HTTP_400_BAD_REQUEST, "Only captured payments can be refunded")

            payment.status = PaymentStatus.REFUNDED
            payment.updated_at = datetime.utcnow()
            session.add(payment)
            session.commit()
            session.refresh(payment)
        return payment
