from . import Session, schemas, models
from datetime import datetime

def create_income(db: Session, income: schemas.IncomeCreate):
    db_income = models.Income(**income.dict())
    db_income.date = datetime.now().date()
    db.add(db_income)
    db.commit()
    db.refresh(db_income)
    return db_income

def get_incomes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Income).offset(skip).limit(limit).all()
