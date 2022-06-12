"""
генерация qrcode
можно строку ввести в формате: python qrcode_2_generate.py <строка для кодирования>
если такую команду не выполнить, программа предложит ввести строку и затем файл для сохранения
файл сохраняется в ./img/<имя_файла>.png
"""


import time
import sys
import pyqrcode


if len(sys.argv) > 1:
    qr_str = sys.argv[1]
else:
    qr_str = input('Введите строку для генерации QRcode: ')

try:
    qr = pyqrcode.create(qr_str, encoding='utf-8')
except UnicodeEncodeError as error:
    print('Не получилось создать QRcode! Попробуйте другую строку.')
    print(error)
    sys.exit()

qr_file_name = input('Введите имя файла для QRcode (enter - по умолчанию): ')

"""если строка имени файла пустая, то имя файла формируется 
на основе текущей даты и времени"""
if not qr_file_name:
    time_file = time.localtime()
    qr_file_name = (f'qrcode_'
                    f'{time_file.tm_year}{time_file.tm_mon}{time_file.tm_mday}_'
                    f'{time_file.tm_hour}{time_file.tm_min}{time_file.tm_sec}')

qr.png(f'img/{qr_file_name}.png', scale=10)

