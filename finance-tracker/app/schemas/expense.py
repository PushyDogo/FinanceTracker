from . import date, BaseModel

class ExpenseBase(BaseModel):
    amount: float
    date: date
    category_id: int

class ExpenseCreate(ExpenseBase):
    pass

class Expense(ExpenseBase):
    id: int

    class Config:
        orm_mode = True