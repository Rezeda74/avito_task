Инструкция по запуску тестов API


Установка необходимых библиотек и зависимостей
1. Установите Python на компьютер, если он не установлен.
Скачать можно с официального сайта https://www.python.org/downloads/

2. Установите pytest и requests:
bash
pip install pytest requests

Запуск автотестов: 

1. Клонируйте репозиторий с тестами:
bash
git clone https://github.com/Rezeda74/avito_task
cd <папка_репозитория>

2. Запустите тесты:
bash
pytest testcases.py -v