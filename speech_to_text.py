import speech_recognition as sr
import csv

haber_list = open('haber_list.csv','w')
writer = csv.writer(haber_list)

r = sr.Recognizer()
file = sr.AudioFile('sound/ses_dosyasi_1 _besiktas.wav')

with file as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)
    result = r.recognize_google(audio, language='tr')

writer.writerows(result)
print(result)
