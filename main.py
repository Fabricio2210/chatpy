import time
import schedule
import sys
from  wrapper import chat, superchats
from apscheduler.schedulers.background import BackgroundScheduler
def exit_script():
    sys.exit()

scheduler = BackgroundScheduler()
scheduler.start()
def teste():
    print("testing!!")
print("running!!!!!")

#chatlogs
# scheduler.add_job(chat, 'interval', minutes=2, args=["https://www.youtube.com/@DSPGaming","dsp"])
# scheduler.add_job(chat, 'interval', minutes=3, args=["https://www.youtube.com/@DarkDavesMirror","ddm"])

# #superchats
# schedule.every(2).minutes.do(lambda: superchats("https://www.youtube.com/@DSPGaming","dsp") )
# schedule.every(3).minutes.do(lambda: superchats("https://www.youtube.com/@DarkDavesMirror","ddm"))
schedule.every(2).minutes.do(lambda: teste())
# schedule.every(5).minutes.do(lambda: superchats("https://www.youtube.com/@RawPhil","raw"))
schedule.every().day.at("09:00").do(exit_script)
try:
    while True:
        time.sleep(1)
        schedule.run_pending()
except (KeyboardInterrupt, SystemExit):
    #scheduler.shutdown()
    schedule.clear()
