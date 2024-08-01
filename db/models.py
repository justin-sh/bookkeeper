from sqlmodel import Field, SQLModel, create_engine

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
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
	id: int|None = Field(default=None, primary_key=True)
	user_id:int
	currency:str
	name:str
	balance:float
	note:str|None