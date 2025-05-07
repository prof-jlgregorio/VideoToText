import moviepy as mp #pip install moviepy
import speech_recognition as sr #pip install SpeechRecognition

videoFile = "ep02.mp4"

fileClip = mp.VideoFileClip(videoFile).subclipped

fileClip.audio.write_audiofile("audio.wav")


recognizer = sr.Recognizer()

with sr.AudioFile("audio.wav") as audioSource:
    print("Gerando transcrição. Aguarde...")
    audio = recognizer.record(audioSource)
    text = recognizer.recognize_google(audio, language='pt-BR')
    textFile = open("transcription.txt", 'w')
    textFile.write(text)
    textFile.close
    print("Transcrição gerada com sucesso!")
