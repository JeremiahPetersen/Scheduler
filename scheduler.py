import schedule
import time
import subprocess
from datetime import datetime
from pytz import timezone

def run_scripts():
    scripts = ['script1.py', 'script2.py', 'script3.py']

    for script in scripts:
        subprocess.run(['python', script])

def is_weekday():
    now_pst = datetime.now(timezone('US/Pacific'))
    return now_pst.weekday() < 5  # Monday is 0 and Sunday is 6

def run_scheduled_scripts():
    if is_weekday():
        run_scripts()

# Schedule the task for 12:50 PM PST
schedule.every().day.at("12:50").do(run_scheduled_scripts)

while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
