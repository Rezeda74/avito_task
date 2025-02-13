# pytest testcases.py -v
import http
import random
from random import randrange
import requests
import string
import pytest

base_url = "https://qa-internship.avito.com/api/1"
advert_uid = "afeaf0de-fa05-45f5-8640-a757b7a9ae55"
seller_id = randrange(111111, 999999)
class_list = [
    "Телефон",
    "Телевизор",
    "Велосипед",
    "Машина",
    "Книга",
    "Платье",
    "Ботинки",
]


#### 1 Создание
# 1.1 Успешное создание нового объявления
def test_create_item():
    url = f"{base_url}/item"
    data = {
        "name": random.choice(class_list),
        "price": randrange(100, 20000),
        "sellerId": seller_id,
        "statistics": {
            "contacts": randrange(100),
            "like": randrange(50),
            "viewCount": randrange(1000),
        },
    }
    response = requests.post(url, json=data)
    # advert_uid = response.json()
    assert response.status_code == 200


# 1.2 Попытка создать объявление с некорректным типом данных обязательного поля
# name - не строка
def test_create_item_without_required_fields1():
    url = f"{base_url}/item"
    data = {
        "name": randrange(100),
        "price": randrange(100, 20000),
        "sellerId": seller_id,
    }
    response = requests.post(url, json=data)
    assert response.status_code == 400


# price - строка
def test_create_item_without_required_fields2():
    url = f"{base_url}/item"
    data = {
        "name": random.choice(class_list),
        "price": random.choice(class_list),
        "sellerId": seller_id,
    }
    response = requests.post(url, json=data)
    assert response.status_code == 400


# sellerId - строка
def test_create_item_without_required_fields3():
    url = f"{base_url}/item"
    data = {
        "name": random.choice(class_list),
        "price": randrange(100, 20000),
        "sellerId": random.choice(class_list),
    }
    response = requests.post(url, json=data)
    assert response.status_code == 400


#### 2 Получить объявление по его идентификатору
# 2.1 Успешное получение объявления по его индентификатору
def test_get_item_success():
    url = f"{base_url}/item/{advert_uid}"
    response = requests.get(url)
    assert response.status_code == 200


# 2.2 Попытка получить объявление с несуществующим идентификатором тип строка
def test_get_item_not_found_string():
    random_length = 8
    random_string = "".join(
        [
            random.choice(string.ascii_letters + string.digits)
            for _ in range(random_length)
        ]
    )
    url = f"{base_url}/item/{random_string}"
    response = requests.get(url)
    assert response.status_code == 400


# 2.3 Попытка получить объявление с несуществующим идентификатором тип отрицательное число
def test_get_item_not_found_negative_number():
    random_negative = (randrange(-100, -1),)
    url = f"{base_url}/item/{random_negative}"
    response = requests.get(url)
    assert response.status_code == 400


# 3 Получить все объявления по идентификатору продавца
# 3.1 Получение всех объявлений по sellerId
def test_get_items_by_seller_success():
    url = f"{base_url}/{seller_id}/item"
    response = requests.get(url)
    assert response.status_code == 200
    json_response = response.json()
    assert isinstance(json_response, list)


# 3.2 Попытка получить объявления по несуществующему sellerId тип строка
def test_get_items_by_seller_not_found_string():
    random_length = 8
    random_string = "".join(
        [
            random.choice(string.ascii_letters + string.digits)
            for _ in range(random_length)
        ]
    )
    url = f"{base_url}/random_string/item"
    response = requests.get(url)
    assert response.status_code == 400


# 3.3
def test_get_items_by_seller_not_found_negative_number():
    random_negative = (randrange(-100, -1),)
    url = f"{base_url}/{random_negative}/item"
    response = requests.get(url)
    assert response.status_code == 400


# 4. Получить статистику по айтем ID


# 4.1 Получение статистики по айтем ID
def test_get_stats_by_item_id_success():

    url = f"{base_url}/statistic/{advert_uid}"
    response = requests.get(url)
    assert response.status_code == 200


# 4.2 Попытка получить статистику по несуществующему item ID тип строка
def test_get_stats_by_item_id_exist_string():
    random_length = 8
    random_string = "".join(
        [
            random.choice(string.ascii_letters + string.digits)
            for _ in range(random_length)
        ]
    )
    url = f"{base_url}/statistic/{random_string}"
    response = requests.get(url)
    assert response.status_code == 400


# 4.3 Попытка получить статистику по несуществующему item ID тип отрицательное число
def test_get_stats_by_item_id_exist_Negative_number():
    random_negative = (randrange(-100, -1),)
    url = f"{base_url}/statistic/{random_negative}"
    response = requests.get(url)
    assert response.status_code == 400
