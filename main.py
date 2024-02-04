import time
import schedule
import sys
from  wrapper import chat, superchats
from apscheduler.schedulers.background import BackgroundScheduler
def exit_script():
    sys.exit()

scheduler = BackgroundScheduler()
scheduler.start()
print("running!!!")

#chatlogs
scheduler.add_job(chat, 'interval', minutes=10, args=["https://www.youtube.com/@meerkat_mob","meerkat"])
scheduler.add_job(chat, 'interval', minutes=20, args=["https://www.youtube.com/@DSPThrowback","throwback"])
scheduler.add_job(chat, 'interval', minutes=10, args=["https://www.youtube.com/@DSPGaming","dsp"])
scheduler.add_job(chat, 'interval', minutes=9, args=["https://www.youtube.com/@DarkDavesMirror ","ddm"])
scheduler.add_job(chat, 'interval', minutes=9, args=["https://www.youtube.com/@RawPhil","raw"])
scheduler.add_job(chat, 'interval', minutes=9, args=["https://www.youtube.com/@dspraw","raw"])
scheduler.add_job(chat, 'interval', minutes=20, args=["https://www.youtube.com/@DSPReacts","reacts"])
scheduler.add_job(chat, 'interval', minutes=10, args=["https://www.youtube.com/@ShinkoFleur","shinko"])
scheduler.add_job(chat, 'interval', minutes=20, args=["https://www.youtube.com/@AgentProper","proper"])
scheduler.add_job(chat, 'interval', minutes=15, args=["https://www.youtube.com/@WPIG1651","wpig"])
scheduler.add_job(chat, 'interval', minutes=15, args=["https://www.youtube.com/@ThatBeingSaid","tbs"])
scheduler.add_job(chat, 'interval', minutes=20, args=["https://www.youtube.com/@TheDecepticron","decepticron"])
scheduler.add_job(chat, 'interval', minutes=15, args=["https://www.youtube.com/@Aqua_Teal","aqua"])
scheduler.add_job(chat, 'interval', minutes=14, args=["https://www.youtube.com/@detractorbeam","beam"])
scheduler.add_job(chat, 'interval', minutes=11, args=["https://www.youtube.com/@PieceofPeace","pop"])
scheduler.add_job(chat, 'interval', minutes=11, args=["https://www.youtube.com/@doodystreams","doody"])
# #superchats
schedule.every(10).minutes.do(lambda: superchats("https://www.youtube.com/@DSPGaming","dsp"))
schedule.every(10).minutes.do(lambda: superchats("https://www.youtube.com/@DSPReacts","reacts"))
schedule.every(15).minutes.do(lambda: superchats("https://www.youtube.com/@doodystreams","doody"))
schedule.every(15).minutes.do(lambda: superchats("https://www.youtube.com/@DSPThrowback","throwback"))
#schedule.every().day.at("09:00").do(exit_script)
try:
    while True:
        time.sleep(1)
        schedule.run_pending()
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
    schedule.clear()