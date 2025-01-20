##################################################################
#                                                                #
#                                                                #
#                            logs.py                             #
#                                                                #
#                                                                #
##################################################################
#
# History
# MM-DD-YYYY  Name Description
# 01-20-2025  MEMA Creation


# This file allows the user to view logs through an API
#----------------------------------------------------------------#
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Log

router = APIRouter()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/logs/")
def get_logs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    logs = db.query(Log).offset(skip).limit(limit).all()
    return {"logs": logs}
