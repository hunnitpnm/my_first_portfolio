'''
Тесты для примеров из документации JSONPlaceholder API.
Запуск: python test_api_examples.py
'''

import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_post_example():   # Тест 'Получение определенного поста'
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["id"] == 1
    print("Пример GET /posts/1 работает корректно")

def test_filter_todos_example():     # Тест 'Фильтрация задач'
    params = {"userId": 1, "completed": "true"}
    response = requests.get(f"{BASE_URL}/todos", params=params)
    assert response.status_code == 200
    todos = response.json()
    assert len(todos) > 0
    print(f"'Фильтрация задач' работает, найдено {len(todos)} задач")

if __name__ == "__main__":
    test_get_post_example()
    test_filter_todos_example()
    print("\n Все примеры из документации работают корректно!")
