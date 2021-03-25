# Import the required module for text
# to speech conversion
# import subprocess
# from GetLatestPost
from gtts import gTTS

# This module is imported so that we can
# play the converted audio

# The text that you want to convert to audio
from Thesis.GetWebData import Website

website = "http://bahaphilippines2020.pythonanywhere.com/flood_data"
web = Website(website)
print(web)
if int(web.level) > 3:
    mytext = web.message

    # Language in which you want to convert
    language = 'en'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save("welcome.mp3")

    # Insert trigger of SDR


# Playing the converted file
# os.system("vlc welcome.mp3")
# subprocess.call(['C:\Program Files\VideoLAN\VLC\vlc.exe', 'welcome.mp3'])


