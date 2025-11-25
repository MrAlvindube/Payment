from fastapi import FastAPI

from .database import init_db
from .schemas import PaymentCreate, PaymentResponse
from .services import PaymentService

app = FastAPI(title="Payment Platform", version="1.0.0")


@app.on_event("startup")
def on_startup() -> None:
    init_db()


@app.post("/payments", response_model=PaymentResponse, status_code=201)
def create_payment(payload: PaymentCreate) -> PaymentResponse:
    return PaymentService.create_payment(payload)


@app.get("/payments", response_model=list[PaymentResponse])
def list_payments() -> list[PaymentResponse]:
    return PaymentService.list_payments()


@app.get("/payments/{payment_id}", response_model=PaymentResponse)
def get_payment(payment_id: str) -> PaymentResponse:
    return PaymentService.get_payment(payment_id)


@app.post("/payments/{payment_id}/authorize", response_model=PaymentResponse)
def authorize_payment(payment_id: str) -> PaymentResponse:
    return PaymentService.authorize_payment(payment_id)


@app.post("/payments/{payment_id}/capture", response_model=PaymentResponse)
def capture_payment(payment_id: str) -> PaymentResponse:
    return PaymentService.capture_payment(payment_id)


@app.post("/payments/{payment_id}/refund", response_model=PaymentResponse)
def refund_payment(payment_id: str) -> PaymentResponse:
    return PaymentService.refund_payment(payment_id)
