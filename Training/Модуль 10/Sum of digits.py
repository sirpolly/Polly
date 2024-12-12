# Функция для вычисления суммы цифр числа
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))


# Основной код программы
n = int(input("Введите количество чисел: "))
max_sum = 0
number_with_max_sum = 0

for _ in range(n):
    user_input = int(input("Введите число: "))
    digit_sum = sum_of_digits(user_input)

    # Проверка на максимальную сумму
    if digit_sum > max_sum:
        max_sum = digit_sum
        number_with_max_sum = user_input

# Вывод результата
print(f"Число {number_with_max_sum} имеет максимальную сумму цифр: {max_sum}")
