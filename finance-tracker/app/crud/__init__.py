from sqlalchemy import extract
from sqlalchemy.orm import Session
from app import models, schemas
from .crud_expenses import create_expense, get_expenses
from .crud_categories import get_expenses_by_category, get_monthly_expenses_by_category, get_categories, add_category
from .crud_incomes import create_income, get_incomes