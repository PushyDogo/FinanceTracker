from . import date, BaseModel

class ExpenseBase(BaseModel):
    amount: float
    category: str

class ExpenseCreate(ExpenseBase):
    pass

class Expense(ExpenseBase):
    id: int
    date: date

    class Config:
        orm_mode = True