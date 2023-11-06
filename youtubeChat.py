from chat_downloader import ChatDownloader
from datetime import datetime

def getChat(video_id,subject):
  now = datetime.now()
  date_time = now.strftime("%Y-%m-%d")
  chat = ChatDownloader().get_chat(f"{video_id}") 
  for message in chat:
    data = f"{chat.format(message)}\n"
    with open(f"./{subject}/chatlogs/{date_time}.txt", 'a',encoding="raw_unicode_escape") as the_file:
      the_file.write(data)
   