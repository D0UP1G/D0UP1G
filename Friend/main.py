import json, pyaudio
from vosk import Model, KaldiRecognizer
import os
from aiogram import Bot, Dispatcher,executor, types
import tokens
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

model = Model(r'model')
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)

stream.start_stream()


def listen():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if (rec.AcceptWaveform(data)) and (len(data))>0:
            answer = json.loads(rec.Result())
            if answer['text']:
                yield answer['text']

print('GOOD')

for text in listen():
    print("Распознано: " + text)
    str(text)
    if fuzz.ratio(text, 'привет') >= 70:
        print("привет1")


