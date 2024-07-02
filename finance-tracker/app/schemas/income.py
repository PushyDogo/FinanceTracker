from . import date, BaseModel

class IncomeBase(BaseModel):
    amount: float
    date: date

class IncomeCreate(IncomeBase):
    pass

class Income(IncomeBase):
    id: int

    class Config:
        orm_mode = True