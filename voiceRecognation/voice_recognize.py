import speech_recognition as sr
import sounddevice as sd
import scipy.io.wavfile as wav
import numpy as np


recognize = sr.Recognizer()


def recognize_from_microphone(file_to_write):
    sample_rate = 44100
    duration = 2

    print("Recording...")
    audio_recording = sd.rec(duration*sample_rate,
                             samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()
    print("Audio recording complete")

    sd.play(audio_recording, sample_rate)
    sd.wait()

    wav.write(file_to_write, sample_rate, audio_recording)


def recognize_from_file(file):
    with sr.AudioFile(file) as source:
        # load audio to memory
        audio_data = recognize.record(source)
        # convert from speech to text
        text = recognize.recognize_google(audio_data, language="en-US")
        return text


def save_audio_to_file(text: str, filename):
    with open(filename, 'w') as file:
        file.write(str(text))


if __name__ == "__main__":
    wav_path = "voiceRecognation/voice_from_mic.wav"
    text_path = "voiceRecognation/recognized_text.txt"
    recognize_from_microphone(wav_path)
    recognized_text = recognize_from_file(wav_path)
    print("Recognized text:", recognized_text)
    save_audio_to_file(recognized_text, text_path)
    print("Text saved to:", text_path)
