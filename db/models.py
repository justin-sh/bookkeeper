from datetime import date
from decimal import Decimal

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    passwd: str
    sec_tip: str
    sec_ans: str

    @property
    def is_authenticated(self) -> bool:
        return not self.is_anonymous

    @property
    def is_active(self) -> bool:
        return not self.is_anonymous

    @property
    def is_anonymous(self) -> bool:
        return self.id == 0

    def get_id(self) -> str:
        return str(self.id)


class Account(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(index=True)
    name: str
    # currency: str
    balance: Decimal = Field(default=0, max_digits=12, decimal_places=2, description="max support is 1,000,000,000.00")
    desc: str | None


class Options(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int
    type: str
    name: str
    parent_id: int = Field(default=0)
    desc: str | None


class Expenses(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int
    ent_date: date
    account_id: int
    cat_id: int
    subcat_id: int = Field(default=0, )
    amount: Decimal = Field(default=0, max_digits=12, decimal_places=2, description="max support is 1,000,000,000.00")
    currency_id: int
    desc: str | None
