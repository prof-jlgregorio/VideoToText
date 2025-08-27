#python versão 3.13.3
import moviepy as mp  # pip install moviepy
import speech_recognition as sr  # pip install SpeechRecognition
from yaspin import yaspin #spinner para animação de processando

videoFile = "./temp/video01.mp4" #carrega o arquivo - caminho do arquivo

# Extrair áudio do vídeo
fileClip = mp.VideoFileClip(videoFile)
fileClip.audio.write_audiofile("./temp/audio.wav")

recognizer = sr.Recognizer() # Criar reconhecedor

#usando o arquivo de áudio gerado...
with sr.AudioFile("./temp/audio.wav") as audioSource:
    #print("Gerando transcrição. Aguarde...")
    with yaspin(text="Gerando transcrição") as spinner:
        audio = recognizer.record(audioSource)  # lê o áudio inteiro
        #usa o reconhecedor de fala para gerar o arquivo texto
        try:
            text = recognizer.recognize_google(audio, language='pt-BR')
            with open("./temp/transcription.txt", "w", encoding="utf-8") as textFile:
                textFile.write(text)
            spinner.ok("✅")  # muda para ✔ qdo terminar
        except sr.UnknownValueError:
            print("❌ Não foi possível entender o áudio.")
        except sr.RequestError as e:
            print(f"❌ Erro ao acessar serviço de reconhecimento: {e}")
