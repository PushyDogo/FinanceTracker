from sqlalchemy import extract
from sqlalchemy.orm import Session
from app import models, schemas
from .crud_expenses import create_expense
from .crud_categories import get_expenses_by_category, get_monthly_expenses_by_category