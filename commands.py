import pyttsx3
import os
import webbrowser as wb
from get_answer import Fetcher

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "si", "sure", "do it", "yeah", "confirm"]
        self.cancel = ["no", "negative", "negative soldier", "don't", "wait","cancel"]

    def discover(self, text):
        if "what" in text and "name" in text:
            if "my" in text:
                self.respond("you haven't told me your name yet")
            else:
                self.respond("My name is lily. How are you?")

        else:
            f = Fetcher("https://www.google.com/search?q="+text)
            answer = f.lookup()
            self.respond(answer)
        
    
        if "launch" or "open" or "browser" or "chrome"in text:
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            app = text.split(" ", 1)[-1]
            self.respond("Opening Browser")
            wb.get(chromepath).open_new_tab()


    def respond(self, response):
        print(response)
        engine.say(response)

