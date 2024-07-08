from . import schemas, crud, Session, models
from .handlers import get_current_month

def add_expense(db: Session, expense: schemas.ExpenseCreate):
    return crud.create_expense(db, expense)

def add_income(db: Session, income: schemas.IncomeCreate):
    return crud.create_income(db, income)

def get_expenses(db: Session, skip: int = 0, limit: int = 100):
    return crud.get_expenses(db, skip=skip, limit=limit)

def get_incomes(db: Session, skip: int = 0, limit: int = 100):
    return crud.get_incomes(db, skip=skip, limit=limit)

def get_monthly_expenses(db: Session, skip: int = 0, limit: int = 100):

    all_expenses = get_expenses(db)
    current_month = get_current_month()
    monthly_expenses = list()

    for expense in all_expenses:
        if(current_month == expense.date.month):
            monthly_expenses.append(expense)

    return monthly_expenses

def get_monthly_income(db: Session, skip: int = 0, limit: int = 100):

    all_incomes = get_incomes(db)
    current_month = get_current_month()
    monthly_incomes = list()

    for income in all_incomes:
        if(current_month == income.date.month):
            monthly_incomes.append(income)

    return monthly_incomes