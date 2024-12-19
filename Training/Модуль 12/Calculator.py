def sum_of_digits(number):
    # Возвращает сумму цифр числа.
    return sum(int(digit) for digit in str(number) if digit.isdigit())


def max_digit(number):
    # Возвращает максимальную цифру числа.
    return max(int(digit) for digit in str(number) if digit.isdigit())


def min_digit(number):
    # Возвращает минимальную цифру числа.
    return min(int(digit) for digit in str(number) if digit.isdigit())


def main():
    while True:
        # Запрашиваем число у пользователя
        number = input("Введите число: ")

        # Проверка на корректность ввода числа
        if not number.isdigit():
            print("Пожалуйста, введите корректное целое число.")
            continue

        # Запрашиваем номер действия
        action = input(
            "Введите номер действия:\n"
            "1 - сумма цифр\n"
            "2 - максимальная цифра\n"
            "3 - минимальная цифра\n"
        )

        if action == "1":
            result = sum_of_digits(number)
            print(f"Сумма цифр: {result}")
        elif action == "2":
            result = max_digit(number)
            print(f"Максимальная цифра: {result}")
        elif action == "3":
            result = min_digit(number)
            print(f"Минимальная цифра: {result}")
        else:
            print("Некорректный ввод. Пожалуйста, выберите 1, 2 или 3.")

        # Запрос на продолжение работы программы
        continue_choice = input("Хотите продолжить? (да/нет): ")
        if continue_choice.lower() != "да":
            break


# Запуск основной программы
if __name__ == "__main__":
    main()
