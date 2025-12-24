import pytest
from calculator import Calculator


class TestCalculatorPytest:
    """
    Класс для тестирования методов класса Calculator с использованием pytest.
    """
    
    @pytest.fixture
    def calculator(self):
        """
        Фикстура, которая создает экземпляр калькулятора для каждого теста.
        """
        return Calculator()
    
    # Тесты для метода add
    @pytest.mark.parametrize("a,b,expected", [
        (2, 3, 5),          # положительные числа
        (-2, -3, -5),       # отрицательные числа
        (5, -3, 2),         # числа с разными знаками
        (5, 0, 5),          # сложение с нулем
        (2.5, 3.1, 5.6),    # дробные числа
    ])
    def test_add(self, calculator, a, b, expected):
        """Параметризованный тест для метода add."""
        result = calculator.add(a, b)
        assert result == expected, f"Сложение {a} и {b} должно давать {expected}"
    
    # Тесты для метода subtract
    @pytest.mark.parametrize("a,b,expected", [
        (5, 3, 2),
        (-2, -3, 1),
        (0, 5, -5),
    ])
    def test_subtract(self, calculator, a, b, expected):
        """Параметризованный тест для метода subtract."""
        result = calculator.subtract(a, b)
        assert result == expected
    
    # Тесты для метода multiply
    @pytest.mark.parametrize("a,b,expected", [
        (2, 3, 6),
        (-2, 3, -6),
        (5, 0, 0),
    ])
    def test_multiply(self, calculator, a, b, expected):
        """Параметризованный тест для метода multiply."""
        result = calculator.multiply(a, b)
        assert result == expected
    
    # Тесты для метода divide
    @pytest.mark.parametrize("a,b,expected", [
        (6, 3, 2),
        (-6, -3, 2),
        (5, 2, 2.5),
        (0, 5, 0),
    ])
    def test_divide_normal(self, calculator, a, b, expected):
        """Параметризованный тест для метода divide (обычные случаи)."""
        result = calculator.divide(a, b)
        assert result == expected
    
    def test_divide_by_zero(self, calculator):
        """
        Тест деления на ноль.
        
        Проверяем, что деление на ноль вызывает исключение ValueError
        с правильным сообщением об ошибке.
        """
        with pytest.raises(ValueError) as exc_info:
            calculator.divide(5, 0)
        
        # Проверяем текст исключения
        assert str(exc_info.value) == "Деление на ноль невозможно"
    
    # Тесты для метода is_prime_number
    @pytest.mark.parametrize("number,expected", [
        (2, True),   # наименьшее простое
        (3, True),
        (5, True),
        (7, True),
        (11, True),
        (13, True),
        (17, True),
        (19, True),
        (23, True),
    ])
    def test_is_prime_number_true(self, calculator, number, expected):
        """Тест для простых чисел."""
        result = calculator.is_prime_number(number)
        assert result == expected, f"{number} должно быть простым числом"
    
    @pytest.mark.parametrize("number,expected", [
        (1, False),   # 1 не является простым
        (4, False),
        (6, False),
        (8, False),
        (9, False),
        (10, False),
        (12, False),
        (14, False),
        (15, False),
        (-5, False),  # отрицательные числа не являются простыми
        (0, False),   # 0 не является простым
    ])
    def test_is_prime_number_false(self, calculator, number, expected):
        """Тест для составных чисел."""
        result = calculator.is_prime_number(number)
        assert result == expected, f"{number} не должно быть простым числом"
    
    # Граничные тесты
    @pytest.mark.parametrize("number", [
        997,  # большое простое число
        1000, # большое составное число
    ])
    def test_is_prime_number_large(self, calculator, number):
        """Тест для больших чисел."""
        # Для проверки можно использовать известные значения
        if number == 997:
            assert calculator.is_prime_number(number) == True
        else:
            assert calculator.is_prime_number(number) == False
    
    # Тест на производительность (опционально)
    @pytest.mark.timeout(1)  # тест должен выполняться не более 1 секунды
    def test_is_prime_number_performance(self, calculator):
        """Тест производительности метода is_prime_number."""
        result = calculator.is_prime_number(1000003)
        assert result == True  # 1000003 - простое число


# Дополнительные тесты без использования класса
@pytest.fixture
def calc():
    """Альтернативная фикстура для создания калькулятора."""
    return Calculator()


def test_add_with_fixture(calc):
    """Тест с использованием фикстуры вне класса."""
    assert calc.add(2, 2) == 4


# Группировка тестов с помощью маркеров
@pytest.mark.slow
def test_slow_operation():
    """Тест, помеченный как медленный (можно запускать отдельно)."""
    calc = Calculator()
    # Имитация медленной операции
    for i in range(1000000):
        calc.add(i, i)
    assert True