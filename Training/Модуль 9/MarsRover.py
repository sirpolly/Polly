# Определение размеров комнаты
room_width = 20
room_height = 15

# Начальная позиция робота
robot_x = 8
robot_y = 10


# Функция для вывода текущей позиции робота
def print_position(x, y):
    print(f"Текущая позиция робота: ({x}, {y})")


# Основной цикл управления роботом
while True:
    # Печатаем текущую позицию
    print_position(robot_x, robot_y)

    # Запрашиваем направление движения
    command = input(
        "Введите направление (W - Север, S - Юг, A - Запад, D - Восток, Q - Выход): "
    ).upper()

    # Проверка на выход из программы
    if command == "Q":
        print("Программа завершена.")
        break

    # Словарь для движения
    move_dict = {
        "W": (0, -1),  # Север
        "S": (0, 1),  # Юг
        "A": (-1, 0),  # Запад
        "D": (1, 0),  # Восток
    }

    # Проверяем, есть ли команда в словаре
    if command in move_dict:
        dx, dy = move_dict[command]
        new_x = robot_x + dx
        new_y = robot_y + dy

        # Проверяем границы
        if 0 <= new_x < room_width and 0 <= new_y < room_height:
            robot_x, robot_y = new_x, new_y  # Обновляем позицию
        else:
            print("Марсоход уперся в стену. Движение отменено.")
    else:
        print("Неверная команда. Используйте W, S, A, D для управления роботом.")
