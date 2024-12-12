# Функция для проверки, является ли число простым
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# Основной код программы
count = int(input("Введите количество чисел: "))
prime_count = 0  # Счетчик простых чисел

for _ in range(count):
    number = int(input("Введите число: "))
    if is_prime(number):
        prime_count += 1
        print(f"{number} — простое число.")
    else:
        print(f"{number} — не простое число.")

# Вывод количества простых чисел
print(f"Количество простых чисел в последовательности: {prime_count}")
