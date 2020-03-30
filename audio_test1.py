import speech_recognition as sr
import pyaudio

r=sr.Recognizer()

    #Microphone(device_index=i, sample_rate=48000)
with sr.Microphone( sample_rate=48000) as source:
    print("Say Something!")
    audio=r.listen(source)
    print("Time over")
try:
    print("text: "+r.recognize_google(audio))
except:
    print("Error")
