from threading import Timer
from  youtubeChat import getChat
from  getVideoId import getVideoId
from superchat import superchat

def chat(url, subject):
    video_id = getVideoId(url)
    if video_id == None:
        print(f"The {subject} channel is not streaming right now...")
    else:
        print(f"Video Id: {video_id}")
        Timer(2.0, getChat(video_id, subject))

def superchats(url, subject):
    video_id = getVideoId(url)
    if video_id == None:
        print(f"The {subject} channel is not streaming right now...")
    else:
        print(f"Video Id: {video_id}")
        Timer(2.0, superchat(video_id,subject))