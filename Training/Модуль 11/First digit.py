# Ввод положительного числа
X = float(input("Введите число: "))

# Умножаем на 10 и берем целую часть
first_digit_after_decimal = int(X * 10) % 10

# Вывод результата
print(f"Первая цифра после десятичной точки: {first_digit_after_decimal}")
