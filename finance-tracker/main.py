from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api.v1.endpoints import transactions
from app.db.session import SessionLocal, engine
import logging


logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/expenses/addexpense", response_model=schemas.Expense)
def add_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    return transactions.add_expense(db=db, expense=expense)

@app.post("/incomes/addincome", response_model=schemas.Income)
def add_income(income: schemas.IncomeCreate, db: Session = Depends(get_db)):
    return transactions.add_income(db=db, income=income)

@app.get("/expenses", response_model=list[schemas.Expense])
def read_expenses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    expenses = transactions.get_monthly_expenses(db, skip=skip, limit=limit)
    return expenses

@app.get("/incomes", response_model=list[schemas.Income])
def read_incomes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    incomes = transactions.get_incomes(db, skip=skip, limit=limit)
    return incomes

@app.get("/expenses/monthly", response_model=list[schemas.Expense])
def read_monthly_expenses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    expenses = transactions.get_monthly_expenses(db, skip=skip, limit=limit)
    return expenses

@app.get("/incomes/monthly", response_model=list[schemas.Income])
def read_monthly_incomes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    incomes = transactions.get_monthly_income(db, skip=skip, limit=limit)
    return incomes

