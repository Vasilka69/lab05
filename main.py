
# Возвращает результат математической операции "sign" с числами "a" и "b"
# Входные данные - числа "a" и "b" и знак математической операции "sign"
# Граничные значения:
#   a, b - числа
#   sign - знак из множества "+, -, *, /"
# Возвращает результат математической операции
def calc(a : float, b: float, sign:str):
    res = -1
    if sign in ('+', '-', '*', '/'):
        if sign == '+':
            res = a+b
        elif sign == '-':
            res = a-b
        elif sign == '*':
            res = a*b
        elif sign == '/':
            res = a/b
    return res

# Сортирует список "a" по возрастанию
# Входные данные - натуральное число "n"
# Граничные значения:
#   a - список чисел
# Возвращает отсортированный по возрастанию список "a"
def bubblesort(a : list):
    N = len(a)
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

# Вывод списка из "n" чисел Фибоначчи
# Входные данные - натуральное число "n"
# Граничные значения:
#   a - натуральное число
# Возвращает "n" чисел Фибоначчи
def fib(n):
    if n <= 0:
        raise IndexError
    output = []
    a, b = 0, 1
    output.append(a)
    output.append(b)
    for _ in range(n-2):
        a, b = b, a + b
        output.append(b)
    return output

def main():
    print(fib(10))
    print(bubblesort([1, 5, 3, 2, 4]))
    print(calc(3, 5, '*'))


if __name__ == '__main__':
    main()