def reverse_number(num):
    """Функция для переворота числа."""
    return str(num)[::-1]


# Ввод чисел от пользователя
n = input("Введите первое число: ")
k = input("Введите второе число: ")

# Переворот чисел
reversed_n = reverse_number(n)
reversed_k = reverse_number(k)

# Вывод результата
print(f"Первое число наоборот: {reversed_n}")
print(f"Второе число наоборот: {reversed_k}")
