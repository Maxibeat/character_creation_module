"""
Добро пожаловать в самую лучшую программу для
вычисления квадратного корня из заданного числа.
"""
import math


def calculatesquareroot(number):
    """Вычисляет квадратный корень."""
    return math.sqrt(number)


def calc(your_number):
    """Проверяем число."""
    if your_number <= 0:
        return
    print('Мы вычислили квадратный корень из введённого вами числа.')
    print(f'Это будет: {calculatesquareroot(your_number)}')


print(__doc__)
calc(25.5)
