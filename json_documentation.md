# Документация для [JSONPlaceholder](https://jsonplaceholder.typicode.com/)

*Версия документации: 1.1*  
*Последнее обновление: 31 января 2026*  
*Автор: Новикова Елена*  

> Все примеры кода написаны на Python 3.12 с использованием библиотеки `requests`.

## Содержание
- [Быстрый старт](#desktop_computer-краткий-обзор)
- [Эндпоинты](#примеры-get-запросов-endpoints)
  - [Posts](#posts)
  - [Comments](#comments)
  - [Albums](#albums)
  - [Photos](#photos)
  - [Todos](#todos)
  - [Users](#users)
- [Особенности API](#warning-особенности-тестового-api-warning)
- [Типы ошибок](#pushpin-типы-ошибок)
- [Примеры использования](#white_check_mark-пример-использования)
- [Тестирование](#heavy_check_mark-тестирование-примеров)
- [Полезные ссылки](#pushpin-полезные-ссылки)


## :desktop_computer: Краткий обзор 

**JSON Placeholder API** — это не требующий регистрации и аутентификации бесплатный API на базе [JSON Server](https://github.com/typicode/json-server) и [LowDB](https://github.com/typicode/lowdb), который имитирует поведение REST API. Он помогает быстро получать данные для приложений, не создавая при этом собственное бэкенд-API. 

---

## Быстрый старт (Quick Start)
1. Установите библиотеку requests: `pip install requests`
2. Дождитесь установки
3. Скопируйте пример ниже

```python
import requests

url = r'https://jsonplaceholder.typicode.com/posts/1' # Пример API для получения данных
response = requests.get(url)  # Отправка GET-запроса
print(response.json()) # Вывод ответа
```
---

## Ответы (Resources)

JSON Placeholder дает возможность получать 6 видов массивов:

| Параметр| Вид данных |
|:-------:|:----------|
| /posts    | Посты (максимальное количество - 100)       |
| /comments | Комментарии (максимальное количество - 500) |
| /albums   | Альбомы (максимальное количество - 100)     |
| /photos   | Изображения (максимальное количество - 5000)|
| /todos    | Задачи (максимальное количество - 200)      |
| /users    | Пользователи (максимальное количество - 10) |

---

## Routes

Поддерживаются все методы HTTP. Для запросов можно использовать HTTP или HTTPS. 

:pushpin: Большинство эндпоинтов работают по единому принципу:
* Без параметра id возвращают массив объектов
* С параметром id возвращают один конкретный объект

| Тип запроса | Пример | Описание |
|:-------:|:------:|:------|
|GET|/albums          | Получить все альбомы                                     |
|GET|/todos/15        | Получить задачу с ID 15                                  |
|GET|/posts/1/comments| Получить все комментарии к посту с ID 1 |
|POST|/posts          | Загрузить пост (нужно тело запроса)                      |
|PUT|/posts/1         | Полностью заменить пост с ID 1                           |
|PATCH|/posts/1       | Частично заменить пост с ID 1 |
|DELETE|/posts/1      | Удалить пост с ID 1                                      |

Поддерживаемые вложенные комбинации:
* _/posts/1/comments_ - комментарии к посту
* _/albums/1/photos_ - фотографии определенного альбома
* _/users/1/albums_ - альбомы определенного пользователя
* _/users/1/todos_ - задачи определенного пользователя 
* _/users/1/posts_ - посты определенного пользователя

---

## :warning: Особенности тестового API :warning:

| Особенность | Описание | Что это значит |
|:-------------:|----------|--------------------------------|
| **Отсутствие валидации** | API принимает любой JSON, даже с ошибками | Тестировать можно с неполными данными, но нельзя проверить валидацию |
| **Данные не сохраняются** | POST/PUT/DELETE не изменяют состояние сервера | Подходит для тестирования, но не подходит для демонстрации персистентности |
| **Предсказуемые ID** | Все ID в диапазоне 1-100 (кроме новых POST) | Удобно для тестирования конкретных сценариев |

Несмотря на отсутствие валидации, рекомендуется отправлять данные в **полном** формате.

## Примеры GET-запросов (Endpoints)

> **Примечание:** Это тестовый API, поэтому данные не сохраняются между запросами.

### Path-параметры:
#### Posts

| Параметр | Тип    | Обязательный | Описание          |
|:----------:|:--------:|:--------------:|:-------------------|
| id     | integer | да | ID поста (1-100)       |
| userId | integer | да | ID автора поста (1-10) |
| title  | string  | да | Заголовок поста        |
| body   | string  | да | Тело поста             |

Пример запроса: 

```python
url = r'https://jsonplaceholder.typicode.com/posts/15' 
```

Вывод:

```python
{
"userId": 2,
"id": 15,
"title": "eveniet quod temporibus",
"body": "reprehenderit quos placeat
         velit minima officia dolores impedit repudiandae molestiae nam
         voluptas recusandae quis delectus
         officiis harum fugiat vitae"
}
```

---

#### Comments

| Параметр | Тип    | Обязательный | Описание          |
|:----------:|:--------:|:--------------:|:-----------|
| postId | integer | да | ID поста (1-100)       |
| id     | integer | да | ID комментария (1-500) |
| name   | string  | да | Заголовок комментария  |
| email  | string  | да | Почта комментатора     |
| body   | string  | да | Тело комментария       |

Пример запроса: 

```python
url = r'https://jsonplaceholder.typicode.com/comments/100' 
```

Вывод:

```python
{
"postId": 20,
"id": 100,
"name": "et sint quia dolor et est ea nulla cum",
"email": "Leone_Fay@orrin.com",
"body": "architecto dolorem ab explicabo et provident et
         et eos illo omnis mollitia ex aliquam
         atque ut ipsum nulla nihil
         quis voluptas aut debitis facilis"
}
```

---

#### Albums

| Параметр | Тип    | Обязательный | Описание          |
|:----------:|:--------:|:--------------:|:-------------------|
| userId | integer | да | ID пользователя (1-10) |
| id     | integer | да | ID альбома (1-100)     |
| title  | string  | да | Название альбома       |

Пример запроса: 

```python
url = r'https://jsonplaceholder.typicode.com/albums/27' 
```

Вывод:

```python
{
"userId": 3,
"id": 27,
"title": "id non nostrum expedita"
}
```

---

#### Photos

| Параметр | Тип    | Обязательный | Описание          |
|:----------:|:--------:|:--------------:|:-------------------|
| albumId      | integer | да | ID альбома (1-100)                       |
| id           | integer | да | ID изображения (1-5000)                  |
| title        | string  | да | Название изображения                     |
| url          | string  | да | Ссылка на изображение                    |
| thumbnailUrl | string  | да | Ссылка на уменьшенную версию изображения |

Пример запроса: 

```python
url = r'https://jsonplaceholder.typicode.com/photos/888' 
```

Вывод:

```python
{
"albumId": 18,
"id": 888,
"title": "in unde tempore quia illum ratione perferendis occaecati",
"url": "https://via.placeholder.com/600/fcf41c",
"thumbnailUrl": "https://via.placeholder.com/150/fcf41c"
}
```

---

#### Todos

| Параметр | Тип    | Обязательный | Описание          |
|:----------:|:--------:|:--------------:|:-------------------|
| userId    | integer | да | ID пользователя (1-10)       |
| id        | integer | да | ID задачи (1-200)            |
| title     | string  | да | Название задачи              |
| completed | bool    | да | Статус выполнения: true/false|

Пример запроса: 

```python
url = r'https://jsonplaceholder.typicode.com/todos/105' 
```

Вывод:

```python
{
"userId": 6,
"id": 105,
"title": "totam quia dolorem et illum repellat voluptas optio",
"completed": true  # true = выполнено, false = не выполнено
}
```

---

#### Users

##### Данные о пользователе

| Параметр | Тип     | Обязательный | Описание           |
|:--------:|:-------:|:------------:|:------------------|
| id       | integer | да | ID пользователя (1-10)       |
| name     | string  | да | Полное имя                   |
| username | string  | да | Никнейм                      |
| email    | string  | да | Email                        |
| address  | object  | да | Объект адреса (см. ниже)   |
| phone    | string  | да | Телефон                      |
| website  | string  | да | URL сайта                    |
| company  | object  | да | Компания (см. ниже)        |

##### Данные об адресе

| Параметр | Тип    | Обязательный | Описание          |
|:--------:|:------:|:------------:|:------------------|
| street  | string | да | Улица                     |
| suite   | string | да | Номер офиса/помещения     |
| city    | string | да | Город                     |
| zipcode | string | да | Почтовый индекс           |
| geo     | object | да | Геокоординаты (см. ниже)|


Пример запроса: 

```python
url = r'https://jsonplaceholder.typicode.com/users/4' 
```

Вывод:

```python
{
"id": 5,
"name": "Chelsey Dietrich",
"username": "Kamren",
"email": "Lucio_Hettinger@annie.ca",
"address": {                          # блок адреса
"street": "Skiles Walks",
"suite": "Suite 351",
"city": "Roscoeview",
"zipcode": "33263",
"geo": {                             # блок координат
"lat": "-31.8129",                   # Широта
"lng": "62.5342"                     # Долгота
}
},
"phone": "(254)954-1289",
"website": "demarco.info",
"company": {                          # блок компании
"name": "Keebler LLC",                # Название компании
"catchPhrase": "User-centric fault-tolerant solution",     # Слоган
"bs": "revolutionize end-to-end systems"             # Бизнес-стратегия
}
}
}
```

---

## Пример POST-запроса (Endpoints)

Пример запроса: 

```python
import requests
import json

url = r'https://jsonplaceholder.typicode.com/posts'
param_dict = {
    "id": 101,
    "userId": 2,
    "title": "test title",
    "body": "test post body"
}
response = requests.post(url=url, json=param_dict)
print(response.text, response.json, sep='\n')
```

Вывод:

```python
{
  "id": 101,
  "userId": 2,
  "title": "test title",
  "body": "test post body"
}
<bound method Response.json of <Response [201]>>   # код 201 указывает на успешную отправку данных. Об обозначении кодов ниже
```
:pushpin: Для других массивов - albums, photos, users и др. - процесс работает аналогично.

---

## Пример PUT-запроса (Endpoints)
#### Posts
Пример запроса: 

```python
import requests
import json

url = r'https://jsonplaceholder.typicode.com/posts/1'
param_dict = {
    "userId": 8,
    "title": 'test title',
    "body": 'test body'
}
response = requests.put(url=url, json=param_dict)
print(response.text, response.json, sep='\n')
```

Вывод:

```python
{
  "userId": 8,
  "title": "test title",
  "body": "test body",
  "id": 1
}
<bound method Response.json of <Response [200]>>   # код 200 указывает на успешную замену данных. Об обозначении кодов ниже
```

---

## Пример PATCH-запроса (Endpoints)
#### Posts
Пример запроса: 

```python
url = r'https://jsonplaceholder.typicode.com/posts/1'
param_dict = {
    "userId": 15,
}
response = requests.patch(url=url, json=param_dict)
print(response.text, response.json, sep='\n')
```

Вывод:

```python
{
  "userId": 15,    # изменение только указанного параметра, остальные поля не изменились
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit
           suscipit recusandae consequuntur expedita et cum
           reprehenderit molestiae ut ut quas totam
           nostrum rerum est autem sunt rem eveniet architecto"
}
<bound method Response.json of <Response [200]>>   # код 200 указывает на успешную замену данных. Об обозначении кодов ниже
```

---

## Пример DELETE-запроса (Endpoints)
#### Posts
Пример запроса: 

```python
import requests
import json

url = r'https://jsonplaceholder.typicode.com/posts/1'
response = requests.delete(url=url)
print(response.text, response.json, sep='\n')

```

Вывод:

```python
{}      # возвращает пустой словарь
<bound method Response.json of <Response [200]>>  # код 200 указывает на успешное удаление данных. Об обозначении кодов ниже
```

---

## :pushpin: Типы ошибок

| Код ответа HTTP | Описание          |
|:----------:|:------------------|
| 200 | Запрос успешно отправлен и сервер предоставил все данные |
| 201 | Новый ресурс успешно создан         |
| 404 | Запрашиваемая информация не была найдена |

Пример запроса: 

```python
url = r'https://jsonplaceholder.typicode.com/users/11'   # максимальное количество пользователей - 10

```

Вывод:

```python
{}      # возвращает пустой словарь
<bound method Response.json of <Response [404]>>  # код 404, так как пользователей 10, а не 11
```
---

## :white_check_mark: Пример использования 

### Фильтрация задач

Получение выполненных задач конкретного пользователя:

```python
import requests
url = r"https://jsonplaceholder.typicode.com/todos"
params = {
    "userId": 3,
    "completed": "true"
}
response = requests.get(url, params=params)
completed_todos = response.json()
print(f"Пользователь с ID {params['userId']} выполнил {len(completed_todos)} задач")
```

Вывод:
`Пользователь с ID 3 выполнил 7 задач`

---

### Контактные данные пользователя

```python
import requests

def get_user_contact(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    user = response.json()
    
    return {
        "name": user["name"],
        "email": user["email"],
        "phone": user["phone"],
        "city": user["address"]["city"]
    }

# Пример данных:

contact = get_user_contact(5)
print(f"{contact['name']} из {contact['city']}")  # Вывод: "Chelsey Dietrich из Roscoeview"
print(f"Email: {contact['email']}")               # Вывод: "Email: Lucio_Hettinger@annie.ca"
print(f"Телефон: {contact['phone']}")             # Вывод: "Телефон: (254)954-1289"
```

---

## :heavy_check_mark: Тестирование примеров

Все примеры кода в этой документации протестированы автоматически.
См. файл [test_api_examples.py](https://github.com/hunnitpnm/my_first_portfolio/blob/main/learning/test_api_examples.py "Ссылка ведет на документ для тестирования") в репозитории.

---

## :pushpin: Полезные ссылки:
- [Официальная документация JSONPlaceholder](https://jsonplaceholder.typicode.com/guide/)
- [Репозиторий на GitHub](https://github.com/typicode/jsonplaceholder)
- [Swagger UI для этого API](https://jsonplaceholder.typicode.com/)
