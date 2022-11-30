import main
import pytest

# Тест функции, которая производит математические операции
class TestCalc:

    # Тестируем программу на коррктных данных. верное значение
    def test_on_correct_sign(self):
        assert main.calc(3, 5, '*') == 15

    # Тестируем программу на некорретных данных. Функция вызывает исключение ZeroDivisionError.
    def test_on_div_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            main.calc(3, 0, '/')
