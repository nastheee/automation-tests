class Calculator:
    """
    Класс Calculator предоставляет базовые арифметические операции
    и проверку чисел на простоту.
    """
    
    def add(self, a: float, b: float) -> float:
        """
        Сложение двух чисел.
        
        Args:
            a: Первое слагаемое
            b: Второе слагаемое
            
        Returns:
            Сумма a и b
        """
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """
        Вычитание двух чисел.
        
        Args:
            a: Уменьшаемое
            b: Вычитаемое
            
        Returns:
            Разность a и b
        """
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """
        Умножение двух чисел.
        
        Args:
            a: Первый множитель
            b: Второй множитель
            
        Returns:
            Произведение a и b
        """
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """
        Деление двух чисел.
        
        Args:
            a: Делимое
            b: Делитель
            
        Returns:
            Частное a и b
            
        Raises:
            ValueError: Если делитель равен нулю
        """
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b
    
    def is_prime_number(self, n: int) -> bool:
        """
        Проверка числа на простоту.
        
        Args:
            n: Проверяемое число
            
        Returns:
            True, если число простое, иначе False
            
        Note:
            Простое число - натуральное число больше 1,
            которое имеет ровно два делителя: 1 и само себя.
        """
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        
        return True