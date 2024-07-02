from . import create_engine, sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Example for SQLite
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname"  # Example for PostgreSQL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}  # Required only for SQLite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()