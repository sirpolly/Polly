def longest_word_length(text):
    # Разделяем текст на слова
    words = text.split()

    # Проверяем, если слова в тексте есть
    if not words:
        print("Введённый текст пуст.")
        return

    # Инициализируем переменную для хранения длины самого длинного слова
    max_length = 0

    # Обходим все слова и ищем длину самого длинного
    for word in words:
        # Убираем знаки препинания в начале и в конце слова и получаем его длину
        clean_word = word.strip(".,!?\"'")
        word_length = len(clean_word)

        # Обновляем максимальную длину, если текущая длина больше
        if word_length > max_length:
            max_length = word_length

    # Выводим результат
    print(f"Самое длинное слово, букв: {max_length}.")


# Запрашиваем ввод у пользователя
input_text = input("Введите текст: ")
longest_word_length(input_text)
