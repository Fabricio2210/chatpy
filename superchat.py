import subprocess
from datetime import datetime
import threading
import platform
import os

superchat_locks = {}

def open_new_terminal(command):
    if platform.system() == 'Windows':
        subprocess.run(['start', 'cmd', '/c', command], shell=True)
    elif platform.system() == 'Linux':
        subprocess.run(['terminator', '-e', command])
    else:
        raise Exception(f"Unsupported platform: {platform.system()}")

def superchat(video_id, subject):
    yesterday = datetime.now()
    formatted_date = yesterday.strftime("%Y-%m-%d")

    shell_script = os.path.join(subject, 'superchats', f'run_chat{subject}.sh')
    
    with open(shell_script, 'w') as file:
        file.write(f'#!/bin/bash\nchat_downloader https://www.youtube.com/watch?v={video_id} --output ./{subject}/superchats/{formatted_date}_superchats.json --message_groups "superchat"')
    
    if (video_id, subject) not in superchat_locks:
        command = f'bash {shell_script}'
        open_new_terminal(command)
        superchat_locks[(video_id, subject)] = threading.Lock()
        print(superchat_locks)
    else:
        print(f"{shell_script} already running")
