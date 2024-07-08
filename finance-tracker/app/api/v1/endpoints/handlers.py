from datetime import datetime

def get_current_month():
    return datetime.now().month

def get_current_date():
    return datetime.now().date()