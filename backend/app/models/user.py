from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column,relationship
from app.database import Base


class User(Base):
    __tablename__="users"
    user_id: Mapped[str] = mapped_column(String(50), primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    name:Mapped[str]=mapped_column(String(100))
    surname:Mapped[str]=mapped_column(String(100))
    phone_number:Mapped[str]=mapped_column(String(30))
    vat_number:Mapped[str|None]=mapped_column(String(20))
    street:Mapped[str]=mapped_column(String(255))
    cap: Mapped[str] = mapped_column(String(10))
    city: Mapped[str] = mapped_column(String(100))
    roles: Mapped[list["Role"]] = relationship(
        "Role",
        secondary="user_roles",
        back_populates="users"
    )