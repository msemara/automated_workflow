##################################################################
#                                                                #
#                                                                #
#                             main.py                            #
#                                                                #
#                                                                #
##################################################################
#
# History
# MM-DD-YYYY  Name Description
# 01-19-2025  MEMA Creation


# Main application
#----------------------------------------------------------------#
from fastapi import FastAPI
from app.database import Base, engine
from app.routers import tasks, workflows, logs
from app.scheduler import scheduler  # Import the scheduler

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Include API routes
app.include_router(tasks.router, prefix="/api/v1", tags=["tasks"])
app.include_router(workflows.router, prefix="/api/v1", tags=["workflows"])
app.include_router(logs.router, prefix="/api/v1", tags=["logs"])

# Scheduler is already running in the background
@app.get("/")
def root():
    return {"message": "Welcome to the Automated Workflow Management System!"}


