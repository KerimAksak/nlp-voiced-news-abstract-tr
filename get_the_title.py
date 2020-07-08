import skimage.io as sio  # pip3 install scikit-image
import skimage 
import pytesseract # pip3 install pytesseract
from skimage.filters import threshold_otsu 
from skimage.color import rgb2gray 

image=sio.imread('haber2.jpg')
#image=rgb2gray(image) 
#otsu=threshold_otsu(image) 
#imagebinari=image>otsu 

#Tesseract Buradan itibaren kullanılıyor.
text=pytesseract.image_to_string(image,lang="tur") 
print(text)

"""
HATA: pytesseract.pytesseract.TesseractNotFoundError: tesseract is not installed or it's not in your PATH
ÇÖZÜM:
    sudo apt install tesseract-ocr
    sudo apt install libtesseract-dev
    sudo apt-get install tesseract-ocr-tur
"""