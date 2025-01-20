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
from datetime import datetime

def print_job():
    print(f"Job executed at {datetime.now()}")

scheduler = BackgroundScheduler()
scheduler.add_job(print_job, "interval", seconds=30)
scheduler.start()
