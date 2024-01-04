import subprocess
import time
import schedule
print("Running!!")
def index():
    scriptPath = "main.sh"
    try:
        subprocess.run([scriptPath], check=True, shell=True)
        print("Done")
    except subprocess.CalledProcessError as error:
        print(f"Error: {error}")
        
schedule.every().day.at("09:10").do(index)
try:
    while True:
        time.sleep(1)
        schedule.run_pending()
except (KeyboardInterrupt, SystemExit):
    schedule.clear()