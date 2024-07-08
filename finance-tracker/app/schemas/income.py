from . import date, BaseModel

class IncomeBase(BaseModel):
    amount: float

class IncomeCreate(IncomeBase):
    pass

class Income(IncomeBase):
    id: int
    date: date

    class Config:
        orm_mode = True