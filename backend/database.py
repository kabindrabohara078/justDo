import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# 🔗 Your Neon connection string
# DATABASE_URL = "postgresql://neondb_owner:npg_iV0sJUxaZB3b@ep-cold-recipe-aiolzd4k.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require"

# Create the database engine (the engine manages the network connection to Neon)
engine = create_engine(DATABASE_URL)

# Create a SessionLocal class. Each instance of this class will be a single database transaction.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class that our database models will inherit from later
Base = declarative_base()