from pyzbar.pyzbar import decode
from PIL import Image

# чтение QRcode
qr_image = Image.open('img/qr4.jpg')
qr_decode = decode(qr_image)
print(f'{qr_image= }')
print(f'{qr_decode= }')
print(qr_decode[0].data.decode('utf-8'))