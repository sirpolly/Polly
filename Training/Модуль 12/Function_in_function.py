def test():
    # Запрашиваем у пользователя ввод целого числа
    number = int(input("Введите число: "))

    # Проверяем, положительное ли число
    if number > 0:
        positive()
    elif number < 0:
        negative()
    else:
        print("Число равно нулю.")


def positive():
    print("Положительное")


def negative():
    print("Отрицательное")


# Основная ветка программы
test()
