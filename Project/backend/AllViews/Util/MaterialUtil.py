import os
from datetime import datetime
from datetime import date
import random
import string

def getParentDir(CurrentPath, levels = 1):
    current_new = CurrentPath
    for i in range(levels + 1):
        current_new = os.path.dirname(current_new)
    
    return os.path.relpath(CurrentPath, current_new)

def getDir(group_key):
    return os.path.join(getParentDir(os.getcwd(), 0), "Chatroom", "Logs", group_key, "Content")

def FILE_HANDLE():
    pass


def FILE_EXTENSION(key, file, ext):
    path = getDir(key)
    print(path)
    match ext:
        case "txt":
            content_path = os.path.join(path, "TXT", file)
            create = open(content_path, "x")
        case "pdf":
            content_path = os.path.join(path, "PDF", file)
            create = open(content_path, "x")
        case "mp3":
            pass
        case "docx":
            pass
        case "mp4":
            pass