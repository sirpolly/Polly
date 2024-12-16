import math


def main():
    # Запрашиваем количество чисел
    n = int(input("Введите кол-во чисел: "))

    for _ in range(n):
        # Запрашиваем число
        num = float(input("Введите число: "))

        if num > 0:
            # Округление вверх для положительных чисел
            rounded_num = math.ceil(num)
            log_value = math.log(rounded_num)
            print(f"x = {rounded_num} log(x) = {log_value}")
        elif num < 1:
            # Округление вниз для отрицательных чисел
            rounded_num = math.floor(num)
            exp_value = math.exp(rounded_num)
            print(f"x = {rounded_num} exp(x) = {exp_value}")
        else:
            print("Число не должно быть нулем.")  # Обработка случая с нулем


if __name__ == "__main__":
    main()
