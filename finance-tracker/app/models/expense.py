from . import Base, Column, Integer, Float, ForeignKey, Date, relationship

class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    date = Column(Date)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category")