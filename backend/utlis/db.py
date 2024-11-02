from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

db = SQLAlchemy(model_class=Base)

class User(Base):
    __tablename__ = "user"

    username: Mapped[str] = mapped_column(String(32))
    password: Mapped[str]
    email: Mapped[str]
    name: Mapped[str]
    BUPTID: Mapped[int]


class Bill(Base):
    content: Mapped[str]
    payer: Mapped["User"] = relationship(
        back_populates="username"
    )
    price: Mapped[float]
