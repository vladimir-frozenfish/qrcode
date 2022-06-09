## Программа генерации и чтения QRCode

- создайте виртуальное окружение:
```
python -m venv venv
source venv/Scripts/activate
``` 

- установите зависимости:
```
pip install -r requirements.txt
```
- для сохранения изображений qrcode создайте папку:
```
./img/
```

### Версия 1 - qrcode_1.py
- создает qrcode из заданной строки и сохраняет в файл /img/qrcode.png
- читает указанный файл, декодирует qrcode, выводит в терминал результат 
