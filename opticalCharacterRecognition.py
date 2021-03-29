try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'tesseract'

def recText(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text

info = recText('/home/zahid/AI master classs pantech/Day-16 Label reading using Optical Character Recognition OCR/Day16Code(1)/PicsArt_10-30-12.02.29.png')
print(info)
file = open("result.txt","w")
file.write(info)
file.close()
print("Written Successful")
