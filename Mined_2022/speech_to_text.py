# -*- coding: utf-8 -*-

import speech_recognition as sr
import threading
import time
from queue import Queue

source_listen = sr.Recognizer()
process_listen = sr.Recognizer()

audio_conversion = Queue()

# Store audio in queue
def callback(recognizer, audio_data):
    if audio_data:
        audio_conversion.put(audio_data)

# Listen audio while processing
def listen():
    source = sr.Microphone()
    listen_in_back = source_listen.listen_in_background(source, callback, 10)
    return listen_in_back

# Processing the audio and storing in file
def process_thread_func():
    audio_text= ""
    while True:
        f = open("patient.txt", "w")
        if audio_conversion.empty():
            time.sleep(0.5)
            continue
        audio = audio_conversion.get()
        if audio:
            try:
                text = process_listen.recognize_google(audio)
            except:
                pass
            else:
                print(text)
                audio_text+= text
                audio_text+= " "
                if "thank you" in text:
                    break
    print("Thank You for Calling...!!")
    audio_text = audio_text.replace("thank you",".")
    f.write(audio_text)
    f.close()

listen_in_back = listen()
process_thread = threading.Thread(target=process_thread_func)
process_thread.start()

input()

listen_in_back()