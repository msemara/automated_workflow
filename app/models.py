##################################################################
#                                                                #
#                                                                #
#                            models.py                           #
#                                                                #
#                                                                #
##################################################################
#
# History
# MM-DD-YYYY  Name Description
# 01-19-2025  MEMA Creation


# This file contains the database models (tables) for tasks, workflows and logs

#----------------------------------------------------------------#
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Task(Base):
    """Tasks Class"""
    # Purpose: Represents individual tasks in the system and tracks the status and timestamps of each task
    # Usage:   Class is used to create, update and retrieve tasks from the database
    #          Ex: a task named "Send email to client" with a "Pending" status.
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    status = Column(String, default="Pending")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Workflow(Base):
    """Workflow Class"""
    # Purpose: Represents an automation workflow and defines the trigger (what initiates the workflow) and
    #          the actions (what happens when triggered)
    # Usage:   This class defines the logic behind automation, sotring workflows for later execution
    #          Ex: workflow named "Weekly Report" that triggers on "Monday 9:00AM" and performs actions like "generate_report"
    __tablename__ = "workflows"
    id = Column(Integer, primary_key=True, index=True)
    workflow_name = Column(String, unique=True, index=True)
    trigger = Column(String)  # E.g., "email_received"
    actions = Column(String)  # E.g., "log_to_db,send_email"

class Log(Base):
    """Log Class"""
    # Purpose: Records logs or events related to workflows. Keeps track of what happened during workflow execution
    # Usage:   Class is used for tracking workflow activiy and debugging
    #          Ex: a log entry stating "Email sent to <email> at 10:00AM" for a specific workflow
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True)
    workflow_id = Column(Integer, ForeignKey("workflows.id"))
    message = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    workflow = relationship("Workflow", back_populates="logs")

Workflow.logs = relationship("Log", back_populates="workflow")
