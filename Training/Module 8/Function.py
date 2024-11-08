def calculate_function(x):
    """Вычисляет значение функции y = x^3 + 2*x^2 - 4*x + 1."""
    return x**3 + 2 * x**2 - 4 * x + 1


# Запрос ввода у пользователя
start = float(input("Введите начало отрезка: "))
end = float(input("Введите конец отрезка: "))
step = float(input("Введите отрицательный шаг: "))

# Устанавливаем шаг по умолчанию, если он не отрицательный
step = step if step < 0 else -1.0

# Обмен значений местами, если необходимо (для работы с отрицательным шагом)
if start < end:
    start, end = end, start

# Вычисление значений функции и вывод результата
for x in range(int(start), int(end) - 1, int(step)):
    y = calculate_function(x)
    print(f"В точке {x} функция равна {y}")
