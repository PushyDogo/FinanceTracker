from . import models, Session, schemas, extract

def get_expenses_by_category(db: Session, category_id: int):
    return db.query(models.Expense).filter(models.Expense.category_id == category_id).all()

def get_monthly_expenses_by_category(db: Session, category_id: int, month: int, year: int):
    return db.query(models.Expense).filter(models.Expense.category_id == category_id, extract('month', models.Expense.date) == month, extract('year', models.Expense.date) == year).all()