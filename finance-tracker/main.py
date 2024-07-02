from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.db.session import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/expenses/", response_model=schemas.expense.Expense)
def add_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    return crud.create_expense(db=db, expense=expense)

@app.post("/incomes/", response_model=schemas.Income)
def add_income(income: schemas.IncomeCreate, db: Session = Depends(get_db)):
    return crud.create_income(db=db, income=income)

@app.get("/expenses/category/{category_id}")
def read_expenses_by_category(category_id: int, db: Session = Depends(get_db)):
    expenses = crud.get_expenses_by_category(db, category_id=category_id)
    return expenses

@app.get("/expenses/monthly/{category_id}")
def read_monthly_expenses_by_category(category_id: int, month: int, year: int, db: Session = Depends(get_db)):
    expenses = crud.get_monthly_expenses_by_category(db, category_id=category_id, month=month, year=year)
    return expenses