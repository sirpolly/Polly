def count_letters():
    # Запрашиваем текст у пользователя
    text = input("Введите текст: ")

    # Запрашиваем цифру и букву для поиска
    digit_to_find = input("Какую цифру ищем? ")
    letter_to_find = input("Какую букву ищем? ")

    # Подсчитываем количество цифр и букв
    digit_count = text.count(digit_to_find)
    letter_count = text.count(letter_to_find)

    # Выводим результаты
    print(f"Количество цифр {digit_to_find}: {digit_count}")
    print(f"Количество букв {letter_to_find}: {letter_count}")


# Запуск функции
count_letters()
