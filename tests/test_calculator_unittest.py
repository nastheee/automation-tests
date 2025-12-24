import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """
    Класс для тестирования методов класса Calculator с использованием unittest.
    """
    
    def setUp(self):
        """
        Метод, который вызывается перед каждым тестом.
        Здесь создается экземпляр тестируемого класса.
        """
        self.calc = Calculator()
    
    def tearDown(self):
        """
        Метод, который вызывается после каждого теста.
        Используется для очистки ресурсов.
        """
        pass
    
    # Тесты для метода add
    def test_add_positive_numbers(self):
        """Тест сложения положительных чисел."""
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)
    
    def test_add_negative_numbers(self):
        """Тест сложения отрицательных чисел."""
        result = self.calc.add(-2, -3)
        self.assertEqual(result, -5)
    
    def test_add_mixed_numbers(self):
        """Тест сложения чисел с разными знаками."""
        result = self.calc.add(5, -3)
        self.assertEqual(result, 2)
    
    def test_add_zero(self):
        """Тест сложения с нулем."""
        result = self.calc.add(5, 0)
        self.assertEqual(result, 5)
    
    def test_add_float_numbers(self):
        """Тест сложения дробных чисел."""
        result = self.calc.add(2.5, 3.1)
        self.assertAlmostEqual(result, 5.6)
    
    # Тесты для метода subtract
    def test_subtract_positive_numbers(self):
        """Тест вычитания положительных чисел."""
        result = self.calc.subtract(5, 3)
        self.assertEqual(result, 2)
    
    def test_subtract_negative_numbers(self):
        """Тест вычитания отрицательных чисел."""
        result = self.calc.subtract(-2, -3)
        self.assertEqual(result, 1)
    
    # Тесты для метода multiply
    def test_multiply_positive_numbers(self):
        """Тест умножения положительных чисел."""
        result = self.calc.multiply(2, 3)
        self.assertEqual(result, 6)
    
    def test_multiply_by_zero(self):
        """Тест умножения на ноль."""
        result = self.calc.multiply(5, 0)
        self.assertEqual(result, 0)
    
    # Тесты для метода divide
    def test_divide_positive_numbers(self):
        """Тест деления положительных чисел."""
        result = self.calc.divide(6, 3)
        self.assertEqual(result, 2)
    
    def test_divide_negative_numbers(self):
        """Тест деления отрицательных чисел."""
        result = self.calc.divide(-6, -3)
        self.assertEqual(result, 2)
    
    def test_divide_float_result(self):
        """Тест деления с дробным результатом."""
        result = self.calc.divide(5, 2)
        self.assertEqual(result, 2.5)
    
    def test_divide_by_zero_raises_exception(self):
        """
        Тест, что деление на ноль вызывает исключение ValueError.
        
        Используем метод assertRaises для проверки исключений.
        """
        with self.assertRaises(ValueError) as context:
            self.calc.divide(5, 0)
        
        # Проверяем текст сообщения об ошибке
        self.assertEqual(str(context.exception), "Деление на ноль невозможно")
    
    # Тесты для метода is_prime_number
    def test_is_prime_number_prime(self):
        """Тест для простых чисел."""
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        for prime in primes:
            with self.subTest(prime=prime):
                result = self.calc.is_prime_number(prime)
                self.assertTrue(result, f"{prime} должно быть простым числом")
    
    def test_is_prime_number_not_prime(self):
        """Тест для составных чисел."""
        not_primes = [1, 4, 6, 8, 9, 10, 12, 14, 15]
        for not_prime in not_primes:
            with self.subTest(not_prime=not_prime):
                result = self.calc.is_prime_number(not_prime)
                self.assertFalse(result, f"{not_prime} не должно быть простым числом")
    
    def test_is_prime_number_negative(self):
        """Тест для отрицательных чисел."""
        result = self.calc.is_prime_number(-5)
        self.assertFalse(result)
    
    def test_is_prime_number_zero(self):
        """Тест для нуля."""
        result = self.calc.is_prime_number(0)
        self.assertFalse(result)
    
    def test_is_prime_number_one(self):
        """Тест для единицы."""
        result = self.calc.is_prime_number(1)
        self.assertFalse(result)
    
    # Параметризованные тесты (альтернативный подход)
    def test_add_parameterized(self):
        """Параметризованный тест для сложения."""
        test_cases = [
            (1, 2, 3),
            (-1, -2, -3),
            (0, 0, 0),
            (2.5, 3.5, 6.0),
            (-2.5, 3.5, 1.0),
        ]
        
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b, expected=expected):
                result = self.calc.add(a, b)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    # Запуск всех тестов
    unittest.main(verbosity=2)