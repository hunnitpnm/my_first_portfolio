# Документация для [OpenWeatherAPI](https://openweathermap.org/)

>*Версия документации: 1.0*  
>*Последнее обновление: 19 января 2026*  
>*Автор: Новикова Елена*

Все примеры кода написаны на Python 3.12 с использованием библиотеки `requests`.

## Об API 

**OpenWeatherAPI** - это API от компании *OpenWeather Ltd*, позволяющий получать актуальные данные о погодных условиях в любой точке мира. К получению доступны прогнозы погоды от краткосрочных до годовых, а также исторические данные.

---

## Быстрый старт (Quick Start)
1. Получите API-ключ на [openweathermap.org](https://home.openweathermap.org/users/sign_up) (для России потребуется VPN)
2. Установите библиотеку requests: `pip install requests`
3. Используйте пример ниже:

```python
import requests

city = "Moscow"
country_code = "RU"   # Код страны (RU, US, GB и т.д.)
api_key = "ВАШ_API_КЛЮЧ"  # Получите на openweathermap.org

url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key}"
response = requests.get(url)   # Отправка GET-запроса

if response.status_code == 200:   # проверка на корректность запроса
    data = response.json()
    print(f"Погода в {city}: {data['weather'][0]['description']}")
    print(f"Температура: {data['main']['temp']}K")
else:
    print(f"Ошибка {response.status_code}: {response.text}")

```

Вывод:

```python
Погода в Moscow: scattered clouds
Температура: 258.39K  # Температура по умолчанию представляется в Кельвинах

```

> 1 градус по Кельвину = 273,15 градуса по Цельсию.

---

## Аутентификация и получение ключа

Для получения ключа необходимо сделать следующее:

1. Зарегистрируйтесь на сайте [openweathermap.org](https://home.openweathermap.org/users/sign_up)
2. Подтвердите email
3. На странице [API Keys](https://home.openweathermap.org/api_keys) создайте новый ключ
4. Подождите 10-15 минут активации

При бесплатном тарифе использования можно сгенерировать столько ключей API, сколько вам потребуется. Нагрузка суммируется по всем существующим ключам. 

```
![Создание ключа](тут будет ссылка 1)

![Создание ключа](тут будет ссылка 2)
```
