import speech_recognition as sr
import sounddevice as sd
import scipy.io.wavfile as wav
import numpy as np



voice_file = "ZOOM01.WAV"
recognize = sr.Recognizer()

def recognize_from_file(file):
    with sr.AudioFile(file) as source:
        #load audio to memory
        audio_data= recognize.record(source)
        #convert from speech to text
        text = recognize.recognize_google(audio_data, language="us-US")
        return text
    

if __name__ == "__main__":
    result = recognize_from_file(voice_file)
    print(result)

    