""""
command:
code - кодирование строки в QRcode
decode - чтение из QRcode строки
exit - выход из программы
"""

import sys
import pyqrcode


def qrcode_make_png():
    if len(sys.argv) > 1:
        qr_str = sys.argv[1]
    else:
        qr_str = input('Введите строку для генерации QRcode: ')

    try:
        qr = pyqrcode.create(qr_str)
    except UnicodeEncodeError as error:
        print('Не получилось создать QRcode! Попробуйте другую строку.')
        print(error)
        return None

    qr_file_name = input('Введите имя файла для QRcode: ')
    qr.png(f'img/{qr_file_name}.png', scale=10)

    sys.exit()


command_dict = {
    'code': qrcode_make_png,
    'exit': sys.exit
}

while True:
    command = input('Введите команду: ')
    if command not in command_dict:
        print('Неизвестная команда!')
        continue
    command_dict[command]()
    # qrcode_make_png()



