def calculate_milk(stalls):
    # Количество молока, производимого в зависимости от стойла
    milk_per_stall = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    # Инициализируем переменную для суммарного молока
    total_milk = 0

    # Обходим строку и суммируем молоко из занятых стойл
    for i in range(len(stalls)):
        if stalls[i] == "b":  # Если стойло занято
            total_milk += milk_per_stall[i]

    return total_milk

# Запрашиваем ввод у пользователя
while True:
    input_stalls = input("Введите 10 стойл в одну строку (a — свободное стойло, b — занятое): ")

    # Проверяем правильность введенной строки
    if len(input_stalls) == 10 and all(c in "ab" for c in input_stalls):
        # Вычисляем общее количество молока
        produced_milk = calculate_milk(input_stalls)
        
        # Выводим результат
        print(f"Произведено молока за день: {produced_milk}л")
        break
    else:
        print("Ошибка: строка должна содержать ровно 10 символов 'a' или 'b'.")
