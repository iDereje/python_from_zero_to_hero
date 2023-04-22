import speech_recognition as sr
from gtts import gTTS
import os
import time

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening...")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition did not understand audio")
    except sr.RequestError as e:
        print("Request Failed; {0}".format(e))
    return data

def respond(text):
    print(text)
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")

'''
commands = {
    "what is your name": "My name is Voice Assistant.",
    "what time is it": "It is currently " + str(time.strftime("%I:%M %p")),
    "search": "What do you want me to search for?",
    "stop": "Goodbye!"
}
'''

while True:
    query = listen().lower()
    if "stop" in query:
        respond("Goodbye!")
        break
    for command in commands:
        if command in query:
            respond(commands[command])
            break
    else:
        respond("I'm sorry, I didn't understand that.")
