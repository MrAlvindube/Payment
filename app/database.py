from contextlib import contextmanager
from typing import Iterator

from sqlmodel import SQLModel, Session, create_engine

DATABASE_URL = "sqlite:///./payments.db"
engine = create_engine(DATABASE_URL, echo=False)


def init_db() -> None:
    SQLModel.metadata.create_all(engine)


@contextmanager
def get_session() -> Iterator[Session]:
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()
