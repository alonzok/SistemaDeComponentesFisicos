#from gtts import gTTS
#from io import BytesIO

#mp3_fp = BytesIO()
#tts = gTTS("hello", lang = 'en')
#tts.write_to_fp(mp3_fp)

from gtts import gTTS
import os

myText = "Hola Alondra, como estas hoy?"
language = "en"

myobj = gTTS(text = myText, lang = language, slow = False)

#myobj.save("welcome.mp3")

os.system("espeak -v es '" + myText + "'")