##################################################################
#                                                                #
#                                                                #
#                          workflows.py                          #
#                                                                #
#                                                                #
##################################################################
#
# History
# MM-DD-YYYY  Name Description
# 01-20-2025  MEMA Creation


# This file will define the endpoints for managing workflows
#----------------------------------------------------------------#
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Workflow

# Initialize the router
router = APIRouter()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new workflow
@router.post("/workflows/")
def create_workflow(workflow_name: str, trigger: str, actions: str, db: Session = Depends(get_db)):
    workflow = Workflow(workflow_name=workflow_name, trigger=trigger, actions=actions)
    db.add(workflow)
    db.commit()
    db.refresh(workflow)
    return {"message": "Workflow created successfully", "workflow": workflow}

# Get all workflows
@router.get("/workflows/")
def read_workflows(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    workflows = db.query(Workflow).offset(skip).limit(limit).all()
    return {"workflows": workflows}

# Update a workflow by ID
@router.put("/workflows/{workflow_id}")
def update_workflow(workflow_id: int, workflow_name: str = None, trigger: str = None, actions: str = None, db: Session = Depends(get_db)):
    workflow = db.query(Workflow).filter(Workflow.id == workflow_id).first()
    if not workflow:
        raise HTTPException(status_code=404, detail="Workflow not found")
    if workflow_name:
        workflow.workflow_name = workflow_name
    if trigger:
        workflow.trigger = trigger
    if actions:
        workflow.actions = actions
    db.commit()
    db.refresh(workflow)
    return {"message": "Workflow updated successfully", "workflow": workflow}

# Delete a workflow by ID
@router.delete("/workflows/{workflow_id}")
def delete_workflow(workflow_id: int, db: Session = Depends(get_db)):
    workflow = db.query(Workflow).filter(Workflow.id == workflow_id).first()
    if not workflow:
        raise HTTPException(status_code=404, detail="Workflow not found")
    db.delete(workflow)
    db.commit()
    return {"message": "Workflow deleted successfully"}
