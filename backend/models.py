from sqlalchemy import Column, Integer, String, Boolean
from database import Base  # We import the Base we just created in database.py

class TodoTable(Base):
    __tablename__ = "todos"  # This is the actual name of the table inside Neon

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    completed = Column(Boolean, default=False)