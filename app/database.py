##################################################################
#                                                                #
#                                                                #
#                          database.py                           #
#                                                                #
#                                                                #
##################################################################
#
# History
# MM-DD-YYYY  Name Description
# 01-19-2025  MEMA Creation


# This file handles the database connection and setup.

#----------------------------------------------------------------#
from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"  # Use "postgresql://user:password@localhost/dbname" for PostgreSQL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
