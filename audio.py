'''import pyglet

file = pyglet.resource.media('audio/confident.mp3')

file.play()

pyglet.app.run()'''


import pyaudio
import wave
import speech_recognition as sr
import pyttsx3
from commands import Commander
running = True
engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)
def say(text):
    engine.say(text)


def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format = pa.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate  = wf.getframerate(),
        output = True

    )
    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream  = wf.readframes(chunk)

    stream.close()
    pa.terminate()


r = sr.Recognizer()
cmd = Commander()
def initSpeech():
    print("Listening.......")
    play_audio("audio/confident1.wav")

    with sr.Microphone() as source:
        print("Say Something")
        audio = r.listen(source)

    play_audio("audio/closed.wav")

    command = ""

    try:
        command = r.recognize_google(audio)
        print("You Command")
        print(command)
        if command in ["quit", "exit", "bye", "goodbye"]:
            global running
            running = False
        
        cmd.discover(command)

        #say('You said:'+ command)

    except:
        print("Couldn't understand you!!!!!")

    


while running == True: 
    initSpeech()
engine.runAndWait()
