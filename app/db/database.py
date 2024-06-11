from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL for connecting to the MySQL database
SQLALCHEMY_DATABASE_URL = "mysql://user:password@localhost/db_name"

# Create an SQLAlchemy engine for database operations
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session factory for creating sessions with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()
