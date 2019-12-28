import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Powiedz coś!')
    audio = r.listen(source)
    print('Ok, dość')

try:
    print("Text: " + r.recognize_google(audio))
except:
    pass
