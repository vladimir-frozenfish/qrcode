"""генерация и расшифровка QRcode"""

import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

# генерация QRcode
qr_str = 'Hallo! My name is Vladimir Kirichenko!'
qr = pyqrcode.create(qr_str)
qr.png('img/qrcode.png', scale=10)

# чтение QRcode
qr_decode = decode(Image.open('img/qrcode.png'))
print(qr_decode[0].data.decode('ascii'))



