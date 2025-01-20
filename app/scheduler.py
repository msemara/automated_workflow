##################################################################
#                                                                #
#                                                                #
#                          scheduler.py                          #
#                                                                #
#                                                                #
##################################################################
#
# History
# MM-DD-YYYY  Name Description
# 01-19-2025  MEMA Creation


# This file sets up APScheduler for recurring tasks
#----------------------------------------------------------------#
from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Workflow
from app.automation import execute_workflow

def process_workflows():
    db: Session = SessionLocal()
    try:
        workflows = db.query(Workflow).all()
        for workflow in workflows:
            if workflow.trigger == "time_interval":  # Example trigger
                execute_workflow(workflow, db)  # Pass the database session
    finally:
        db.close()

scheduler = BackgroundScheduler()
scheduler.add_job(process_workflows, "interval", seconds=30)  # Runs every 30 seconds
scheduler.start()


