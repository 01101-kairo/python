
# ffmpeg -ss 0 -t 5 -i audio-original.mp3 audio-cortado.mp3
# -ss 0 :: início do corte;
# -t 5 :: tempo em segundos a partir do corte;
# -i arquivo :: arquivo a ser cortado.
import moviepy.editor as mp
import speech_recognition as sr
import moviepy.editor as mp
import sys
from pydub import AudioSegment
import os
# os.system('clear')
file_audio = sr.AudioFile(r'./CortGrupo 6_wav')

r = sr.Recognizer()
with file_audio as source:
    audio_text = r.record(source)
    text = r.recognize_google(audio_text,language='pt-BR')

arq = open('trascricao.txt','w')
arq.write(text)
arq.close()
print(text)
