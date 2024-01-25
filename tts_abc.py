from gtts import gTTS
import playsound
import os

tts = gTTS(
    text="a b c",
    lang="en"
)
tts.save("TTS.mp3")

playsound.playsound("TTS.mp3")
os.remove("TTS.mp3")
