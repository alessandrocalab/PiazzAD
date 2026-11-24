from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column,relationship
from app.database import Base

class role(Base):
__tablename__="roles"
name:Mapped[str]=mapped_column(String(50),primary_key=True)
users: Mapped[list["User"]] = relationship(
    "User",
    secondary="user_roles",
    back_populates="roles"
)