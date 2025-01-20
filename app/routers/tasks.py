##################################################################
#                                                                #
#                                                                #
#                             tasks.py                           #
#                                                                #
#                                                                #
##################################################################
#
# History
# MM-DD-YYYY  Name Description
# 01-19-2025  MEMA Creation


# This file defines the API routes for tasks
#----------------------------------------------------------------#
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Task

# Initialize the router
router = APIRouter()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new task
@router.post("/tasks/")
def create_task(name: str, db: Session = Depends(get_db)):
    task = Task(name=name)
    db.add(task)
    db.commit()
    db.refresh(task)
    print(f"Task created: {task.id}, Name: {task.name}")
    return {"message": "Task created successfully", "task": task}

# Get all tasks
@router.get("/tasks/")
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tasks = db.query(Task).offset(skip).limit(limit).all()
    return {"tasks": tasks}

# Update a task by ID
@router.put("/tasks/{task_id}")
def update_task(task_id: int, name: str = None, status: str = None, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if name:
        task.name = name
    if status:
        task.status = status
    db.commit()
    db.refresh(task)
    return {"message": "Task updated successfully", "task": task}

# Delete a task by ID
@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}

