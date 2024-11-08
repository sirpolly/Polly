def average_of_multiples_of_three(a, b):
    total_sum = 0  # Сумма кратных 3 чисел
    count = 0  # Количество кратных 3 чисел

    # Проходим по каждому числу в диапазоне от a до b
    for number in range(a, b + 1):
        if number % 3 == 0:
            total_sum += number  # Добавляем число к сумме
            count += 1  # Увеличиваем счетчик

    # Если кратных 3 чисел не найдено
    if count == 0:
        return None
    else:
        return total_sum / count  # Возвращаем среднее арифметическое


# Считывание входных данных
a = int(input("Введите первое число (a): "))
b = int(input("Введите второе число (b): "))

# Вычисление среднего арифметического
average = average_of_multiples_of_three(a, b)

# Вывод результата
if average is not None:
    # Форматируем вывод, убирая ненужные нули
    formatted_average = f"{average:.1f}".rstrip("0").rstrip(".")
    print(
        f"Среднее арифметическое всех чисел от {a} до {b}, кратных 3: {formatted_average}"
    )
else:
    print(f"В отрезке от {a} до {b} нет чисел, кратных 3.")
