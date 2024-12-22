def count_numbers(num):
    """Возвращает количество цифр в числе."""
    count = 0
    temp = num
    while temp > 0:
        count += 1
        temp //= 10
    return count


def change_number(num):
    """Меняет местами первую и последнюю цифры числа и возвращает
    изменённое число."""
    num_str = str(num)
    if len(num_str) < 2:
        return num
        """Если число состоит из одной цифры, возвращаем 
        его без изменений"""
    # Меняем местами первую и последнюю цифры
    changed_num_str = num_str[-1] + num_str[1:-1] + num_str[0]
    return int(changed_num_str)


def main():
    """Основная функция, которая запрашивает ввод, выполняет
    проверки и выводит результат."""
    first_n = int(input("Введите первое число: "))
    first_num_count = count_numbers(first_n)

    if first_num_count < 3:
        print("В первом числе меньше трёх цифр.")
        return

    first_n = change_number(first_n)
    print("Изменённое первое число:", first_n)

    second_n = int(input("\nВведите второе число: "))
    second_num_count = count_numbers(second_n)

    if second_num_count < 4:
        print("Во втором числе меньше четырёх цифр.")
        return

    second_n = change_number(second_n)
    print("Изменённое второе число:", second_n)

    print("\nСумма чисел:", first_n + second_n)


# Запуск основной функции
if __name__ == "__main__":
    main()
