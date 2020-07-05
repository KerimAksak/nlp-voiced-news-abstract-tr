from trnlp import *  # trnlp -> pip3 install trnlp


metin = """Saçma ve Gereksiz Bir Yazı.
    Bakkaldan 5 TL'lik 2 çikola-
    ta al. 12.02.2018 tarihinde saat tam 15:45'te yap-
    malıyız bu işi. Tamam mı? Benimle esatmahmutbayol@gmail.com 
    adresinden iletişime geçebilirsin. Yarışta 1. oldu. Doç. Dr. 
    Esat Bayol'un(Böyle bir ünvanım yok!) yanından geliyorum.
    12 p.m. mi yoksa 12 a.m. mi? 100 milyon insan gelmiş! www.deneme.com.tr 
    adresinden sitemizi inceleyebilirsin. 24 Eylül 2018 Pazartesi günü ge-
    lecekmiş. 19 Mayıs'ı coşkuyla kutladık."""

metin2 = """Besiktas Sampiyonlugu
        tefeciler Spor Toto Süper Lig'in ilk 33 haftasında Gaziantepspor deplasmanda 4-0 mağlup eden Beşiktaş 
        ligin bitmesine 1 hafta kala şampiyonluğunu ilan etti maçın bitiş düdüğü ile birlikte kutlamalarda başlık 
        beyazdı dün gece 15 şampiyonluğunu ilan eden Karakartal formasına 3 yıldızı taktı Beşiktaşlı taraftarların 
        kutlaması taban ışıklarına kadar sürdü Gaziantep karşısında aldığı 40 sporla Mutlu sona ulaşan Beşiktaşlı 
        futbolcular sahanın içinde doyasıya eğlendikten Sonra teknik direktör Şenol Güneş'in basın toplantısını 
        bastı bütün oyuncularını Teşekkür ederim gurur duyuyorum yeteneklerim karakterlerin Geçen sene de bu sene de 
        ortaya koydular düşen takımlar ve düşmesi Muhtemelen bir takıma da şampiyonluğu getirdi gece yarısı Kalkan 
        uçakla İstanbul'a gelen Beşiktaş kafilesi Sabiha Gökçen Havalimanı'nda coşkuyla karşılandı Sabaha Dek sürdü 
        ama eğlenceye gölge düşürenler de vardı elindeki silahla halay çeken kalabalığı umursamadan havaya peşpeşe 
        ateş eden bir maganda onlardan biriydi beyaz otomobilden inen Bu sürücü ise ne arka koltukta oturan çocuğa 
        ne de Etraftaki kalabalığa aldırış etti tabancasından çıkan mermi yine bir can alabilirdi erkek basketbol 
        takımının Avrupa şampiyonu olmasının ardından 15 Temmuz Şehitler Köprüsü'ne açılan Fenerbahçe bayrağını 
        yerinden söküp yakan 4 tarafta arsa yakalandı kutlamalara gölge düşüren birkaç kendini bi"""

metin3 = "Beşiktaş Şampiyonluğu, tefeciler Spor Toto Süper Lig'in ilk 33 haftasında Gaziantepspor deplasmanda 4-0 mağlup etti."

#string değerini kelime kelime indisleme işlemi.
metin_list = list(metin3.split(" ")) 

#n-gram
obj = TrnlpToken()
obj.settext(metin2)
#print(obj.wordcounter)

"""
    !setword fonksiyonu tek bir kelime alarak çalışıyor. 
    Ayrıca Türkçe harf kurallarına uygun olmalı.
    Ve kelime sonundaki noktalama işaretleri olmamalı.
    Örnek: 
    şampiyon = sampiyon (x)
    etti. (x)
"""
# obj2.setword("Şampiyonluğu")
# print(obj2)
obj2 = TrnlpWord()
for i in metin_list:
    obj2.setword(i)
    print(obj2)
