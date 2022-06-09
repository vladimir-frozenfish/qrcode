"""
генерация qrcode
можно строку ввести в формате: python qrcode_2_generate.py <строка для кодирования>
если такую команду не выполнить, программа предложит ввести строку и затем файл для сохранения
файл сохраняется в ./img/<имя_файла>.png
"""


import sys
import pyqrcode


if len(sys.argv) > 1:
    qr_str = sys.argv[1]
else:
    qr_str = input('Введите строку для генерации QRcode: ')

try:
    qr = pyqrcode.create(qr_str)
except UnicodeEncodeError as error:
    print('Не получилось создать QRcode! Попробуйте другую строку.')
    print(error)
    sys.exit()

qr_file_name = input('Введите имя файла для QRcode: ')
qr.png(f'img/{qr_file_name}.png', scale=10)

