import barcode
from barcode.writer import ImageWriter

from PIL import Image

img = Image.open("barcode.png")
img.show()

def generate_barcode(data):
    BarcodeClass = barcode.get_barcode_class('code128')
    code = BarcodeClass(data, writer=ImageWriter())
    filename = code.save("barcode")
    print("Barcode saved as:", filename)

generate_barcode("2211-3145-6789")


