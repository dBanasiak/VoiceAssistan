import subprocess
import re

def SYS_CMD(command):
    command = command.split(' ')
    obj_name = False
    for word in command:
        if re.match(r"start|run|activate|get|enter|do|trigger|find|edit", word, re.IGNORECASE):
            obj_name = command[command.index(word) + 1]
        if obj_name:
            if re.match(r"program|app|application|software|system|binary", word, re.IGNORECASE):
                RUN_PROGRAM(obj_name)
            elif re.match(r"document|paper|form|report|file|script|page|diary|archive|record", word, re.IGNORECASE):
                EDIT_DOCUMENT(obj_name)

def RUN_PROGRAM(program_name):
    proc = subprocess.Popen(program_name, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    o, e = proc.communicate()

    print('Output: ' + o.decode('ascii'))
    print('Error: '  + e.decode('ascii'))

def EDIT_DOCUMENT(document_name):
    proc = subprocess.Popen(document_name, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    o, e = proc.communicate()

    print('Output: ' + o.decode('ascii'))
    print('Error: '  + e.decode('ascii'))

SYS_CMD('Hello i wanna edit text.txt file for me')