""""
command:
code - кодирование строки в QRcode
decode - чтение из QRcode строки
exit - выход из программы
"""

import time
import sys
import pyqrcode

from os import path
from pyzbar.pyzbar import decode
from PIL import Image, UnidentifiedImageError


def qrcode_code(qr_str=None):
    """функция кодирования фразы в qrcode"""
    qr_str = qr_str or input('Введите строку для генерации QRcode: ')

    try:
        qr = pyqrcode.create(qr_str, encoding='utf-8')
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

    qr.png(f'img/{qr_file_name}.png', scale=10, quiet_zone=1)

    print(f'\nДля строки - "{qr_str}", создан QRcode - {qr_file_name}.png\n')


def qrcode_decode(qr_file=None):
    """функция чтения qrcode из изображения (файла)"""
    qr_file = qr_file or input('Введите путь к изображению для чтения QRcode: ')

    # проверка есть ли такой файл
    if not path.isfile(qr_file):
        print('Такого файла не существует!')
        return None

    try:
        qr_image = Image.open(qr_file)
        qr_decode = decode(qr_image)
        if qr_decode:
            print(f'QRcode на изображении {qr_file} - {qr_decode[0].data.decode("utf-8")}')
        else:
            print(f'Не удалось распознать в изображении {qr_file} QRcode!')
    except UnidentifiedImageError as error:
        print('Файл не является изображением!')
        print(error)


command_dict = {
    'code': qrcode_code,
    'decode': qrcode_decode,
    'exit': sys.exit
}


def read_sys_argv(command_argv):
    """функция чтения аргументов из командной строки,
    если такие есть"""
    if len(command_argv) != 3:
        no_error = False
        message = 'Необходимо два аргумента: команда и имя строки или файла'
        return no_error, message, None, None

    command = command_argv[1]
    name = command_argv[2]

    if command not in command_dict or command == 'exit':
        no_error = False
        message = f'Такая команда - {command} - не поддерживается!'
        return no_error, message, None, None

    no_error = True
    message = 'Ok'

    return no_error, message, command, name


while True:
    """если программа запускается из терминала
    с дополнительными аргументами, то выполняется один раз и выходит из программы"""
    if len(sys.argv) > 1:
        no_error, message, command, name = read_sys_argv(sys.argv)
        if no_error:
            command_dict[command](name)
        else:
            print(message)
        break

    """если программа запускается без дополнительных аргументов,
    то запускается цикл получения команд"""
    command = input(f'Введите команду ({",".join(list(command_dict.keys()))}): ')
    if command not in command_dict:
        print('Неизвестная команда!\n')
        continue
    command_dict[command]()
