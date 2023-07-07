import moviepy.editor as mp
import speech_recognition as sr
import moviepy.editor as mp
import sys
from pydub import AudioSegment

#convertendo mp4 em mp3

path = 'teste.mp4'
clip = mp.VideoFileClip(path).subclip()
clip.audio.write_audiofile('teste.mp3')

#tranformando de mp3 em wav

scr = (r'./teste.mp3')
sound = AudioSegment.from_mp3(scr)
sound.export('./teste.wav', format='wav')
file_audio = sr.AudioFile(r'./teste.wav')

#transcrevendo

r = sr.Recognizer()
with file_audio as source: 
    audio_text = r.record(source)
    text = r.recognize_google(audio_text, language='pt-BR')

#salvando

arq = open('transcricao.txt', 'w')
arq.write(text)
arq.close()
print(text)