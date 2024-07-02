from . import Session, schemas, models

def create_income(db: Session, income: schemas.IncomeCreate):
    db_income = models.Income(**income.dict())
    db.add(db_income)
    db.commit()
    db.refresh(db_income)
    return db_income
