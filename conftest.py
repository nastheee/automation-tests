# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    """
    Фикстура для Selenium WebDriver.
    Использует Chrome в headless режиме для CI/CD.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Без GUI
    options.add_argument("--no-sandbox")  # Для Linux на GitHub Actions
    options.add_argument("--disable-dev-shm-usage")  # Уменьшение использования памяти
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")  # Размер окна

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    yield driver
    driver.quit()
