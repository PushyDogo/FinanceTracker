from . import Base, Column, Integer, Float, Date

class Income(Base):
    __tablename__ = "incomes"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    date = Column(Date)