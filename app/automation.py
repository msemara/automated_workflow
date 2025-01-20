##################################################################
#                                                                #
#                                                                #
#                          automation.py                         #
#                                                                #
#                                                                #
##################################################################
#
# History
# MM-DD-YYYY  Name Description
# 01-20-2025  MEMA Creation


# This file handles the logic for executing workflows
#----------------------------------------------------------------#
from app.models import Workflow, Log
from sqlalchemy.orm import Session
from datetime import datetime

def execute_workflow(workflow: Workflow, db: Session):
    # Extract actions from the workflow
    actions = workflow.actions.split(",")  # Example: ["log_to_db", "send_email"]

    for action in actions:
        if action == "log_to_db":
            message = f"Logging data for workflow: {workflow.workflow_name}"
            print(message)
            save_log(workflow.id, message, db)
        elif action == "send_email":
            message = f"Sending email for workflow: {workflow.workflow_name}"
            print(message)
            save_log(workflow.id, message, db)
        else:
            message = f"Unknown action: {action}"
            print(message)
            save_log(workflow.id, message, db)

def save_log(workflow_id: int, message: str, db: Session):
    # Create a new log entry
    log = Log(workflow_id=workflow_id, message=message, timestamp=datetime.utcnow())
    db.add(log)
    db.commit()

