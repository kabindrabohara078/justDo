from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List

import models
from database import SessionLocal

app = FastAPI()

# 🔐 CORS Middleware must sit immediately below app initialization
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://just-do-jet.vercel.app/"],  # Matches default Vite port
    allow_credentials=True,
    allow_methods=["*"],                      # Allows GET, POST, PATCH, DELETE, OPTIONS
    allow_headers=["*"],                      # Allows all headers
)

# 🛡️ Pydantic Schema for Input Validation
class TodoCreateSchema(BaseModel):
    title: str

# 🔌 Database Session Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 📋 1. GET ALL
@app.get("/todos")
def get_all_todos(db: Session = Depends(get_db)):
    return db.query(models.TodoTable).all()

# ➕ 2. CREATE
@app.post("/todos")
def create_todo(todo_data: TodoCreateSchema, db: Session = Depends(get_db)):
    new_todo = models.TodoTable(title=todo_data.title)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

# 🔄 3. TOGGLE STATUS (Note the absolute path format)
@app.patch("/todos/{todo_id}")
def toggle_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.TodoTable).filter(models.TodoTable.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo.completed = not todo.completed
    db.commit()
    db.refresh(todo)
    return todo

# ❌ 4. DELETE (Note the absolute path format)
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.TodoTable).filter(models.TodoTable.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return {"message": f"Successfully deleted task {todo_id}"}