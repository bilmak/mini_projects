from gtts import gTTS
from pydub import AudioSegment


def creating_mp3(text):
    tts = gTTS(text, lang='en')
    tts.save("voiceRecognation/test_audio.mp3")

    sound = AudioSegment.from_mp3("voiceRecognation/test_audio.mp3")
    sound.export("voice.wav", format="wav")


text = "Hello, this is a test version for your project."
creating_mp3(text)
