

from gtts import gTTS
import os

while True:

           text = input()

           language = 'en'

           speech = gTTS(text = text, lang = language, slow = False)

           speech.save("text.mp3")

           os.system("start text.mp3")
