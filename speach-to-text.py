import speech_recognition as sr
from DEF_MAIN.sys_cmd import SYS_CMD

r = sr.Recognizer()

text = " "

while(text != "stop"):
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=3)
        print("Say something!")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
            SYS_CMD(text)
        except sr.UnknownValueError:
            print("I could not understand audio properly")
        except sr.RequestError as e:
            print("I could not request results from Google Speech Recognition service; {0}".format(e))
