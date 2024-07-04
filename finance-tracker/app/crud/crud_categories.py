from . import models, Session, schemas, extract

def add_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()

def get_expenses_by_category(db: Session, category_id: int):
    return db.query(models.Expense).filter(models.Expense.category_id == category_id).all()

def get_monthly_expenses_by_category(db: Session, category_id: int, month: int, year: int):
    return db.query(models.Expense).filter(models.Expense.category_id == category_id, extract('month', models.Expense.date) == month, extract('year', models.Expense.date) == year).all()