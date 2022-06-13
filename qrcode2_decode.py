from pyzbar.pyzbar import decode
from PIL import Image, UnidentifiedImageError

# чтение QRcode
try:
    qr_image = Image.open('img/qr2.jpg')
    qr_decode = decode(qr_image)
    print(f'{qr_image= }')
    print(f'{qr_decode= }')
    if qr_decode:
        print(qr_decode[0].data.decode('utf-8'))
    else:
        print('Не удалось распознать в изображении QRcode!')
except UnidentifiedImageError as error:
    print('Загруженный файл не является изображением!')
    print(error)
