def summa_n(number):
    # Проверяем, что number является положительным целым числом
    if number <= 0:
        print("Введите положительное целое число.")
        return

    # Вычисляем сумму чисел от 1 до number
    total_sum = sum(range(1, number + 1))

    # Выводим результат
    print(f"Сумма чисел от 1 до {number} равна {total_sum}")


# Пример использования
try:
    N = int(input("Введите число: "))
    summa_n(N)
except ValueError:
    print("Пожалуйста, введите корректное целое число.")
