# Запрос параметров у пользователя
while True:
    try:
        rows = int(input("Введите количество рядов: "))
        break
    except ValueError:
        print("Введите целое число.")

while True:
    try:
        seats = int(input("Введите количество сидений в ряду: "))
        break
    except ValueError:
        print("Пожалуйста, введите целое число.")

while True:
    try:
        distance = float(
            input(
                "Введите расстояние между рядами (в метрах, используйте '.' или ',' как разделитель): "
            ).replace(",", ".")
        )
        break
    except ValueError:
        print("Пожалуйста, введите число (можно с десятичной точкой).")

# текст для сцены
scene_text = "🏛СЦЕНА🏛"


# Функция для добавления пробелов между буквами
def add_spacing(text, space=4):
    return (" " * space).join(text)


# Выводим макет театра с отступом перед стульями
print("\n" * 0)  # Отступ сверху
for row in range(1, rows + 1):
    # Форматирование номера ряда
    row_number = f"{row}  " if row < 10 else f"{row} "

    # Формирование ряда с креслами
    row_seats = (
        "🪑" * (seats // 2) + " " * 3 + "🪑" * (seats // 2)
        if seats % 2 == 0
        else "🪑" * (seats // 2 + 1) + " " * 3 + "🪑" * (seats // 2)
    )

    # Выводим ряд
    print(f"Ряд {row_number}{row_seats}")

    # расстояние между рядами
    if row < rows:  # Не добавляем расстояние после последнего ряда
        print("\n" * int(distance), end="")  # Добавляем нужное количество пустых строк

# Вычисления для центрирования
total_seats_length = len(row_seats)
scene_length = len(scene_text)

# Центрирование сцены под учетом длины ряда сидений
spaces_needed = total_seats_length - (
    len(add_spacing(scene_text)) + (len(scene_text) - 1) * 3
)  # 3 - количество пробелов между буквами


def new_func(scene_text, add_spacing, spaces_needed):
    centered_scene = " " * (spaces_needed // 8) + add_spacing(scene_text)
    return centered_scene


centered_scene = new_func(scene_text, add_spacing, spaces_needed)

# Добавляем отступы ниже сцены
print("\n" + centered_scene + "\n")
