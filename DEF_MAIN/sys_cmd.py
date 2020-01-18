import os
import re
from colorama import Fore, Style
from selenium import webdriver

def SYS_CMD(command):
    command = command.split(' ')
    obj_name = False
    proc_name = False
    q_name = False
    for word in command:
        if re.match(r"start|run|activate|get|enter|do|trigger|edit|check|out|show|play", word, re.IGNORECASE):
            obj_name = command[command.index(word) + 1]
        elif re.match(r"kill|terminate|close|destroy|show|me", word, re.IGNORECASE):
            proc_name = command[command.index(word) + 1]
        elif re.match(r"search|find", word, re.IGNORECASE):
            q_name = command[command.index(word) + 1]

        if obj_name:
            if re.match(r"program|app|application|software|system|binary", word, re.IGNORECASE):
                RUN_PROGRAM(obj_name)
            elif re.match(r"document|paper|form|report|file|script|page|diary|archive|record", word, re.IGNORECASE):
                EDIT_DOCUMENT(obj_name)
            elif re.match(r"version", word, re.IGNORECASE):
                CHECK_VERSION(obj_name)
            elif re.match(r"date", word, re.IGNORECASE):
                CHECK_DATE()
            elif re.match(r"programs|tasklist", word, re.IGNORECASE):
                SHOW_TASK_LIST()
            elif re.match(r"movie|video", word, re.IGNORECASE):
                PLAY_YOUTUBE(obj_name)
        elif proc_name:
            CLOSE_PROCES(proc_name)
        elif q_name:
            SEARCH(q_name)

def RUN_PROGRAM(program_name):
    print(Fore.GREEN, "I'm sure you have this program in your taskbar, there are easier ways to fire it", Style.RESET_ALL )
    if program_name == 'Spotify' or program_name == 'spotify':
        os.system("start C:\\path\\to\\your\\Spotify.exe")
    else:
        print(Fore.GREEN, "Or maybe some existing program?", Style.RESET_ALL)

def CHECK_VERSION(command_name):
    print(Fore.GREEN + "Oh, you wanna check", command_name, " version? How cute", Style.RESET_ALL)
    cmd = command_name + " --version"
    os.system(cmd)

def CHECK_DATE():
    print(Fore.GREEN + "You know you have a watch in the lower right corner?", Style.RESET_ALL)
    os.system("date/T")
    os.system("time/T")

def EDIT_DOCUMENT(document_name):
    print(Fore.GREEN + "Text files? What year is it?")
    print(Style.RESET_ALL)
    os.system("start C:\\path\\to\\your\\Documents\\" + document_name + ".txt")

def PLAY_YOUTUBE(video_name):
    global ff
    ff = webdriver.Chrome(executable_path=r"C:\\path\\to\\your\\chromedriver.exe")
    ff.get("https://www.youtube.com/results?search_query=" + video_name)
    element = ff.find_element_by_id("video-title")
    element.click()
    return ff

def SEARCH(query_name):
    global ff
    ff = webdriver.Chrome(executable_path=r"C:\\path\\to\\your\\chromedriver.exe")
    ff.get("https://www.google.pl/search?q=" + query_name)

def SHOW_TASK_LIST():
    os.system("tasklist")

def CLOSE_PROCES(proces_name):
    print(proces_name)
    os.system("taskkill /IM " + proces_name + ".exe /F")
