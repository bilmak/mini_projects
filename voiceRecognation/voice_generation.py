from gtts import gTTS
from pydub import AudioSegment


def creating_mp3(text):
    tts = gTTS(text, lang='en')
    tts.save("voiceRecognation/test_audio.mp3")

    sound = AudioSegment.from_mp3("voiceRecognation/test_audio.mp3")
    sound.export("voice.wav", format="wav")


text = "Hello! This is my house. This is a Elsa. He's my friend"
creating_mp3(text)
