def maximum_of_two(a, b):
    """Возвращает максимум из двух чисел a и b."""
    return a if a > b else b


def maximum_of_three(x, y, z):
    """Возвращает максимум из трех чисел x, y и z, используя
    функцию maximum_of_two."""
    max_xy = maximum_of_two(x, y)  # Находим максимум из x и y
    return maximum_of_two(max_xy, z)  # Сравниваем максимум с z


# Получаем ввод от пользователя
try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    num3 = float(input("Введите третье число: "))

    max_value = maximum_of_three(num1, num2, num3)
    print(f"Самое большое число: {max_value}")
except ValueError:
    print("Пожалуйста, введите корректные числа.")
