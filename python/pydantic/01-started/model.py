from sqlalchemy.orm import Mapped, declarative_base, mapped_column

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]
    address: Mapped[str]

    def __repr__(self) -> str:
        return f"<User ({self.id}, {self.name}, {self.age}, {self.address})>"
