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

def getPath(group_key):
    return os.path.join(getParentDir(os.getcwd(), 0), "Chatroom", "Logs", group_key)

def create(group_key, person, chatroom_key, message):
    path = getPath(group_key)

    file_path = os.path.join(path, group_key)
    file_path = os.path.join(path, chatroom_key)

    write(file_path, "a", "Create", group_key, person, message)

def update(group_key, person, chatroom_key, old_message, new_message):
    path = getPath(group_key)

    file_path = os.path.join(path, group_key)
    file_path = os.path.join(path, chatroom_key)

    message = old_message + " -> to -> " + new_message
    write(file_path, "a", "Update", group_key, person, message)

def delete(group_key, person, chatroom_key, message):
    path = getPath(group_key)

    file_path = os.path.join(path, group_key)
    file_path = os.path.join(path, chatroom_key)

    write(file_path, "a", "Delete", group_key, person, message)

def write(path, mode, type, group_key, person, message):
    log = open(path, mode)
    log.write("[Type: {}][Group Key: {}][Date: {}][Name: {}][Message: {}]".format(type, group_key, datetime.now(), person, message) + "\n")
    log.close()

def init(group_key, person, chatroom_key):
        path = getPath(group_key)

        if not os.path.exists(path):
            os.makedirs(path)
            file_path = os.path.join(path, group_key)

            FILE_PATH_PDF = os.path.join(path, "Content", "PDF")
            FILE_PATH_TXT = os.path.join(path, "Content", "TXT")
            FILE_PATH_IMG_FOLDER = os.path.join(path, "Content", "IMAGES")
            FILE_PATH_IMG_FOLDER_PNG = os.path.join(path, "Content", "IMAGES", "PNG")
            FILE_PATH_IMG_FOLDER_JPG = os.path.join(path, "Content", "IMAGES", "JPG")

            os.makedirs(FILE_PATH_PDF)
            os.makedirs(FILE_PATH_TXT)
            os.makedirs(FILE_PATH_IMG_FOLDER)
            os.makedirs(FILE_PATH_IMG_FOLDER_PNG)
            os.makedirs(FILE_PATH_IMG_FOLDER_JPG)

            file_path = os.path.join(path, chatroom_key)
            write(file_path, "a", "Init", group_key, person, "Chatgroup Created")
            
        else:
            return "Error: File for group already exists."

