def convert_to_float_format(x):
    """Преобразует число x в формат плавающей точки a * 10^b."""
    if x <= 0:
        raise ValueError("Число должно быть положительным и больше нуля.")

    # Определяем порядок (b) и мантиссу (a)
    b = 0
    while x >= 10:
        x /= 10
        b += 1
    while x < 1:
        x *= 10
        b -= 1

    return x, b


# Получаем ввод от пользователя
try:
    user_input = float(input("Введите число: "))
    a, b = convert_to_float_format(user_input)
    print(f"Формат плавающей точки: x = {a} * 10 ** {b}")
except ValueError as e:
    print(e)
