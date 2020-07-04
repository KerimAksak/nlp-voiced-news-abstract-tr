import speech_recognition as sr
import csv
import os

# mp4 dosyamız üstünde dönüşümler yapıyoruz.
# Command for video conversion
# sudo apt-get install ffmpeg
command2mp3 = "ffmpeg -i videoAndSound/haber_1_besiktas.mp4 videoAndSound/haber_1_besiktas.mp3"
command2wav = "ffmpeg -i videoAndSound/haber_1_besiktas.mp3 videoAndSound/haber_1_besiktas.wav"

# !!!İkinci kez çalıştırıldığında bulunan dosyalar üzerine tekrar yazmaya çalışıyor.
# Execute video conversion commands
os.system(command2mp3)
os.system(command2wav)

r = sr.Recognizer()
file = sr.AudioFile('videoAndSound/haber_1_besiktas.wav')

with file as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)
    result = r.recognize_google(audio, language='tr')

print(result)
text_file = open("Output.txt", "w")
text_file.write("Besiktas Sampiyonlugu\n")
text_file.write(result)
text_file.close()