from database import engine, Base
import models  # This ensures our TodoTable model is loaded

print("Connecting to Neon and creating tables...")

# This command tells SQLAlchemy to create all tables that inherit from 'Base'
Base.metadata.create_all(bind=engine)

print("Success! Your 'todos' table has been created in the cloud.")