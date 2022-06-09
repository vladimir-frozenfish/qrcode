""""
command:
code - кодирование строки в QRcode
decode - чтение из QRcode строки
exit - выход из программы
"""

import time, sys
import pyqrcode


def read_sys_argv():
    pass


def qrcode_code():
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

    qr_file_name = input('Введите имя файла для QRcode (enter - по умолчанию): ')

    """если строка имени файла пустая, то имя файла формируется 
    на основе текущей даты и времени"""
    if not qr_file_name:
        time_file = time.localtime()
        qr_file_name = (f'qrcode_'
                        f'{time_file.tm_year}{time_file.tm_mon}{time_file.tm_mday}_'
                        f'{time_file.tm_hour}{time_file.tm_min}{time_file.tm_sec}')

    qr.png(f'img/{qr_file_name}.png', scale=10)

    print(f'\nДля строки - "{qr_str}", создан QRcode - {qr_file_name}.png\n')


def qrcode_decode():
    pass

command_dict = {
    'code': qrcode_code,
    'decode': qrcode_decode,
    'exit': sys.exit
}

while True:
    command = input('Введите команду: ')
    if command not in command_dict:
        print('Неизвестная команда!\n')
        continue
    command_dict[command]()
    # qrcode_make_png()



