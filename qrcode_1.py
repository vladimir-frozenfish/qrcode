"""генерация и расшифровка QRcode"""
import io

import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

# генерация QRcode
qr_str = 'Hallo! My name is Vladimir Kirichenko!'
qr = pyqrcode.create(qr_str)

qrcode_text = qr.terminal(quiet_zone=1) # сохранение qrcode в текстовом формате
print(qrcode_text)

qr.png('img/qrcode.png', scale=10)      # сохранение qrcode в файл

buffer = io.BytesIO()
qr.png(buffer)                          # сохранение qrcode в буфер
print(list(buffer.getvalue()))

qrcode_as_str = qr.png_as_base64_str(scale=5)
html_img = '<img src="data:image/png;base64,{}">'.format(qrcode_as_str)     # сохранение qrcode для html
print(qrcode_as_str)
print(html_img)


# чтение QRcode
qr_image = Image.open('img/qrcode.png')
qr_decode = decode(qr_image)
print(qr_decode[0].data.decode('ascii'))



