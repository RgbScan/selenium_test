# Selenium Tests

Этот проект содержит примеры автоматизированных тестов для веб-приложений с использованием Selenium.

## Установка

1. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/username/selenium_tests.git
   
2. Создайте виртуальное окружение и активируйте его
    ```sh
   python -m venv venv
    source venv/bin/activate  # Для Windows: venv\Scripts\activate
3. Установите зависимости:
    ```sh
   pip install -r requirements.txt

4. Запустите тесты с помощью unittest:
    ```sh
   python -m unittest discover -s tests

Список тестов:
* test_google_search.py: тестирует поиск в Google.